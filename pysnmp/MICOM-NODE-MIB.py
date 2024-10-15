# SNMP MIB module (MICOM-NODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-NODE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:48 2024
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
 NotificationType,
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
    "NotificationType",
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

_Micom_ObjectIdentity = ObjectIdentity
micom = _Micom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1)
)
_Marathon_netrunner_ObjectIdentity = ObjectIdentity
marathon_netrunner = _Marathon_netrunner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 1)
)
_Micom_proxy_ObjectIdentity = ObjectIdentity
micom_proxy = _Micom_proxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2)
)
_Marathon_netrunner_proxy_ObjectIdentity = ObjectIdentity
marathon_netrunner_proxy = _Marathon_netrunner_proxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1)
)
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 1)
)


class _LcdSecurityPassword_Type(DisplayString):
    """Custom type lcdSecurityPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LcdSecurityPassword_Type.__name__ = "DisplayString"
_LcdSecurityPassword_Object = MibScalar
lcdSecurityPassword = _LcdSecurityPassword_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 1, 1),
    _LcdSecurityPassword_Type()
)
lcdSecurityPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    lcdSecurityPassword.setStatus("mandatory")
_CmdPortSecurityGroup_ObjectIdentity = ObjectIdentity
cmdPortSecurityGroup = _CmdPortSecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 1, 2)
)


class _CmdPortSecurityGlobalPassword_Type(DisplayString):
    """Custom type cmdPortSecurityGlobalPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmdPortSecurityGlobalPassword_Type.__name__ = "DisplayString"
_CmdPortSecurityGlobalPassword_Object = MibScalar
cmdPortSecurityGlobalPassword = _CmdPortSecurityGlobalPassword_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 1, 2, 1),
    _CmdPortSecurityGlobalPassword_Type()
)
cmdPortSecurityGlobalPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cmdPortSecurityGlobalPassword.setStatus("mandatory")


class _CmdPortSecurityStatusPassword_Type(DisplayString):
    """Custom type cmdPortSecurityStatusPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CmdPortSecurityStatusPassword_Type.__name__ = "DisplayString"
_CmdPortSecurityStatusPassword_Object = MibScalar
cmdPortSecurityStatusPassword = _CmdPortSecurityStatusPassword_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 1, 2, 2),
    _CmdPortSecurityStatusPassword_Type()
)
cmdPortSecurityStatusPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cmdPortSecurityStatusPassword.setStatus("mandatory")


class _NmsSecurityPPPPassword_Type(DisplayString):
    """Custom type nmsSecurityPPPPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NmsSecurityPPPPassword_Type.__name__ = "DisplayString"
_NmsSecurityPPPPassword_Object = MibScalar
nmsSecurityPPPPassword = _NmsSecurityPPPPassword_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 1, 3),
    _NmsSecurityPPPPassword_Type()
)
nmsSecurityPPPPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nmsSecurityPPPPassword.setStatus("mandatory")
_Diagnostics_ObjectIdentity = ObjectIdentity
diagnostics = _Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 2)
)


class _PingResponse_Type(Integer32):
    """Custom type pingResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notResponding", 2),
          ("responded", 1))
    )


_PingResponse_Type.__name__ = "Integer32"
_PingResponse_Object = MibScalar
pingResponse = _PingResponse_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 2, 1),
    _PingResponse_Type()
)
pingResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResponse.setStatus("mandatory")
_VoiceChannelDiagTable_Object = MibTable
voiceChannelDiagTable = _VoiceChannelDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    voiceChannelDiagTable.setStatus("mandatory")
_VoiceChannelDiagEntry_Object = MibTableRow
voiceChannelDiagEntry = _VoiceChannelDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 2, 2, 1)
)
voiceChannelDiagEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "voiceChannelDiagCardNumber"),
    (0, "MICOM-NODE-MIB", "voiceChannelDiagChannelNumber"),
)
if mibBuilder.loadTexts:
    voiceChannelDiagEntry.setStatus("mandatory")


class _VoiceChannelDiagCardNumber_Type(Integer32):
    """Custom type voiceChannelDiagCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_VoiceChannelDiagCardNumber_Type.__name__ = "Integer32"
_VoiceChannelDiagCardNumber_Object = MibTableColumn
voiceChannelDiagCardNumber = _VoiceChannelDiagCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 2, 2, 1, 1),
    _VoiceChannelDiagCardNumber_Type()
)
voiceChannelDiagCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChannelDiagCardNumber.setStatus("mandatory")


class _VoiceChannelDiagChannelNumber_Type(Integer32):
    """Custom type voiceChannelDiagChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_VoiceChannelDiagChannelNumber_Type.__name__ = "Integer32"
_VoiceChannelDiagChannelNumber_Object = MibTableColumn
voiceChannelDiagChannelNumber = _VoiceChannelDiagChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 2, 2, 1, 2),
    _VoiceChannelDiagChannelNumber_Type()
)
voiceChannelDiagChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChannelDiagChannelNumber.setStatus("mandatory")


class _VoiceChannelDiagCommand_Type(Integer32):
    """Custom type voiceChannelDiagCommand based on Integer32"""
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
        *(("inputLevelDisplay", 2),
          ("putChannelInLoopback", 4),
          ("selfTest", 3),
          ("terminateTest", 1))
    )


_VoiceChannelDiagCommand_Type.__name__ = "Integer32"
_VoiceChannelDiagCommand_Object = MibTableColumn
voiceChannelDiagCommand = _VoiceChannelDiagCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 2, 2, 1, 3),
    _VoiceChannelDiagCommand_Type()
)
voiceChannelDiagCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    voiceChannelDiagCommand.setStatus("mandatory")
_SyncChannelDiagTable_Object = MibTable
syncChannelDiagTable = _SyncChannelDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    syncChannelDiagTable.setStatus("mandatory")
_SyncChannelDiagEntry_Object = MibTableRow
syncChannelDiagEntry = _SyncChannelDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 2, 3, 1)
)
syncChannelDiagEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "syncChannelDiagCardNumber"),
    (0, "MICOM-NODE-MIB", "syncChannelDiagChannelNumber"),
)
if mibBuilder.loadTexts:
    syncChannelDiagEntry.setStatus("mandatory")


class _SyncChannelDiagCardNumber_Type(Integer32):
    """Custom type syncChannelDiagCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SyncChannelDiagCardNumber_Type.__name__ = "Integer32"
_SyncChannelDiagCardNumber_Object = MibTableColumn
syncChannelDiagCardNumber = _SyncChannelDiagCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 2, 3, 1, 1),
    _SyncChannelDiagCardNumber_Type()
)
syncChannelDiagCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChannelDiagCardNumber.setStatus("mandatory")


class _SyncChannelDiagChannelNumber_Type(Integer32):
    """Custom type syncChannelDiagChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SyncChannelDiagChannelNumber_Type.__name__ = "Integer32"
_SyncChannelDiagChannelNumber_Object = MibTableColumn
syncChannelDiagChannelNumber = _SyncChannelDiagChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 2, 3, 1, 2),
    _SyncChannelDiagChannelNumber_Type()
)
syncChannelDiagChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChannelDiagChannelNumber.setStatus("mandatory")


class _SyncChannelDiagCommand_Type(Integer32):
    """Custom type syncChannelDiagCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("putChannelInLoopback", 2),
          ("terminateTest", 1))
    )


_SyncChannelDiagCommand_Type.__name__ = "Integer32"
_SyncChannelDiagCommand_Object = MibTableColumn
syncChannelDiagCommand = _SyncChannelDiagCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 2, 3, 1, 3),
    _SyncChannelDiagCommand_Type()
)
syncChannelDiagCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    syncChannelDiagCommand.setStatus("mandatory")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1)
)
_Attributes_ObjectIdentity = ObjectIdentity
attributes = _Attributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1)
)


class _SysPromID_Type(DisplayString):
    """Custom type sysPromID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_SysPromID_Type.__name__ = "DisplayString"
_SysPromID_Object = MibScalar
sysPromID = _SysPromID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 1),
    _SysPromID_Type()
)
sysPromID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPromID.setStatus("mandatory")
_SysTypeGroup_ObjectIdentity = ObjectIdentity
sysTypeGroup = _SysTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 2)
)


class _SysSoftwareType_Type(Integer32):
    """Custom type sysSoftwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("marathon", 1),
          ("netrunner", 2))
    )


_SysSoftwareType_Type.__name__ = "Integer32"
_SysSoftwareType_Object = MibScalar
sysSoftwareType = _SysSoftwareType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 2, 1),
    _SysSoftwareType_Type()
)
sysSoftwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwareType.setStatus("mandatory")


class _SysHardwareType_Type(Integer32):
    """Custom type sysHardwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("fiftyECCM", 2),
          ("fiveKCCM", 4),
          ("fiveKTPro", 13),
          ("fiveKTurboCCM", 6),
          ("oneKCCM", 3),
          ("seventyfiveECCM", 8),
          ("seventyfiveEwithFR", 9),
          ("tenKCCM", 5),
          ("threeK", 11),
          ("twentyKCCM", 7),
          ("twentyKPro", 14),
          ("twoKCCM", 10),
          ("twoKTPro", 12),
          ("unknown", 1))
    )


_SysHardwareType_Type.__name__ = "Integer32"
_SysHardwareType_Object = MibScalar
sysHardwareType = _SysHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 2, 2),
    _SysHardwareType_Type()
)
sysHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareType.setStatus("mandatory")


class _SysOperationalType_Type(Integer32):
    """Custom type sysOperationalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("feeder", 2),
          ("node", 1))
    )


_SysOperationalType_Type.__name__ = "Integer32"
_SysOperationalType_Object = MibScalar
sysOperationalType = _SysOperationalType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 2, 3),
    _SysOperationalType_Type()
)
sysOperationalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOperationalType.setStatus("mandatory")


class _SysSoftwarePhase_Type(Integer32):
    """Custom type sysSoftwarePhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              999)
        )
    )
    namedValues = NamedValues(
        *(("aboveKnownPhases", 999),
          ("phase3dot0", 1),
          ("phase3dot1", 2),
          ("phase3dot2", 3),
          ("phase3dot2C", 4),
          ("phase4dot0", 5),
          ("phase4dot1", 6),
          ("phase4dot1G", 8),
          ("phase4dot2", 7),
          ("phase4dot2c", 9),
          ("phase4dot3", 10),
          ("phase4dot3BorC", 12),
          ("phase5dot0", 11),
          ("phase5dot0B", 13))
    )


_SysSoftwarePhase_Type.__name__ = "Integer32"
_SysSoftwarePhase_Object = MibScalar
sysSoftwarePhase = _SysSoftwarePhase_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 2, 4),
    _SysSoftwarePhase_Type()
)
sysSoftwarePhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwarePhase.setStatus("mandatory")


class _SysFeatureType_Type(Integer32):
    """Custom type sysFeatureType based on Integer32"""
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
        *(("dualBank", 2),
          ("featurePak", 1),
          ("simSingleDual", 4),
          ("singleBank", 3))
    )


_SysFeatureType_Type.__name__ = "Integer32"
_SysFeatureType_Object = MibScalar
sysFeatureType = _SysFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 2, 5),
    _SysFeatureType_Type()
)
sysFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureType.setStatus("mandatory")


class _SysFeatureRTC_Type(Integer32):
    """Custom type sysFeatureRTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1))
    )


_SysFeatureRTC_Type.__name__ = "Integer32"
_SysFeatureRTC_Object = MibScalar
sysFeatureRTC = _SysFeatureRTC_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 2, 6),
    _SysFeatureRTC_Type()
)
sysFeatureRTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureRTC.setStatus("mandatory")
_SysLocNodeLinkTable_Object = MibTable
sysLocNodeLinkTable = _SysLocNodeLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sysLocNodeLinkTable.setStatus("mandatory")
_SysLocNodeLinkEntry_Object = MibTableRow
sysLocNodeLinkEntry = _SysLocNodeLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 3, 1)
)
sysLocNodeLinkEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "sysLocNodeLinkIndex"),
)
if mibBuilder.loadTexts:
    sysLocNodeLinkEntry.setStatus("mandatory")


class _SysLocNodeLinkIndex_Type(Integer32):
    """Custom type sysLocNodeLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SysLocNodeLinkIndex_Type.__name__ = "Integer32"
_SysLocNodeLinkIndex_Object = MibTableColumn
sysLocNodeLinkIndex = _SysLocNodeLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 3, 1, 1),
    _SysLocNodeLinkIndex_Type()
)
sysLocNodeLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLocNodeLinkIndex.setStatus("mandatory")


class _SysLocNodeLinkNodeNameOfFeeder_Type(DisplayString):
    """Custom type sysLocNodeLinkNodeNameOfFeeder based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SysLocNodeLinkNodeNameOfFeeder_Type.__name__ = "DisplayString"
_SysLocNodeLinkNodeNameOfFeeder_Object = MibTableColumn
sysLocNodeLinkNodeNameOfFeeder = _SysLocNodeLinkNodeNameOfFeeder_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 3, 1, 2),
    _SysLocNodeLinkNodeNameOfFeeder_Type()
)
sysLocNodeLinkNodeNameOfFeeder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLocNodeLinkNodeNameOfFeeder.setStatus("mandatory")


class _SysLocNodeLinkNodeType_Type(Integer32):
    """Custom type sysLocNodeLinkNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marathon", 2),
          ("mbFeeder", 3),
          ("notConfigured", 1))
    )


_SysLocNodeLinkNodeType_Type.__name__ = "Integer32"
_SysLocNodeLinkNodeType_Object = MibTableColumn
sysLocNodeLinkNodeType = _SysLocNodeLinkNodeType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 3, 1, 3),
    _SysLocNodeLinkNodeType_Type()
)
sysLocNodeLinkNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLocNodeLinkNodeType.setStatus("mandatory")


class _SysLocNodeLinkNodeNumber_Type(Integer32):
    """Custom type sysLocNodeLinkNodeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysLocNodeLinkNodeNumber_Type.__name__ = "Integer32"
_SysLocNodeLinkNodeNumber_Object = MibTableColumn
sysLocNodeLinkNodeNumber = _SysLocNodeLinkNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 3, 1, 4),
    _SysLocNodeLinkNodeNumber_Type()
)
sysLocNodeLinkNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLocNodeLinkNodeNumber.setStatus("mandatory")


class _SysDateTime_Type(OctetString):
    """Custom type sysDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SysDateTime_Type.__name__ = "OctetString"
_SysDateTime_Object = MibScalar
sysDateTime = _SysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 4),
    _SysDateTime_Type()
)
sysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateTime.setStatus("mandatory")
_SysClassCfgTable_Object = MibTable
sysClassCfgTable = _SysClassCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sysClassCfgTable.setStatus("mandatory")
_SysClassCfgEntry_Object = MibTableRow
sysClassCfgEntry = _SysClassCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 5, 1)
)
sysClassCfgEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "sysClassCfgClassNumber"),
)
if mibBuilder.loadTexts:
    sysClassCfgEntry.setStatus("mandatory")


class _SysClassCfgClassNumber_Type(Integer32):
    """Custom type sysClassCfgClassNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SysClassCfgClassNumber_Type.__name__ = "Integer32"
_SysClassCfgClassNumber_Object = MibTableColumn
sysClassCfgClassNumber = _SysClassCfgClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 5, 1, 1),
    _SysClassCfgClassNumber_Type()
)
sysClassCfgClassNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysClassCfgClassNumber.setStatus("mandatory")


class _SysClassCfgClassName_Type(DisplayString):
    """Custom type sysClassCfgClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_SysClassCfgClassName_Type.__name__ = "DisplayString"
_SysClassCfgClassName_Object = MibTableColumn
sysClassCfgClassName = _SysClassCfgClassName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 5, 1, 2),
    _SysClassCfgClassName_Type()
)
sysClassCfgClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysClassCfgClassName.setStatus("mandatory")


class _SysClassCfgClassSecondary_Type(Integer32):
    """Custom type sysClassCfgClassSecondary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SysClassCfgClassSecondary_Type.__name__ = "Integer32"
_SysClassCfgClassSecondary_Object = MibTableColumn
sysClassCfgClassSecondary = _SysClassCfgClassSecondary_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 5, 1, 3),
    _SysClassCfgClassSecondary_Type()
)
sysClassCfgClassSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysClassCfgClassSecondary.setStatus("mandatory")


class _SysClassCfgClassMessage_Type(DisplayString):
    """Custom type sysClassCfgClassMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 61),
    )


_SysClassCfgClassMessage_Type.__name__ = "DisplayString"
_SysClassCfgClassMessage_Object = MibTableColumn
sysClassCfgClassMessage = _SysClassCfgClassMessage_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 5, 1, 4),
    _SysClassCfgClassMessage_Type()
)
sysClassCfgClassMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysClassCfgClassMessage.setStatus("mandatory")


class _SysClassCfgClassPassword_Type(DisplayString):
    """Custom type sysClassCfgClassPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SysClassCfgClassPassword_Type.__name__ = "DisplayString"
_SysClassCfgClassPassword_Object = MibTableColumn
sysClassCfgClassPassword = _SysClassCfgClassPassword_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 5, 1, 5),
    _SysClassCfgClassPassword_Type()
)
sysClassCfgClassPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sysClassCfgClassPassword.setStatus("mandatory")


class _SysClassCfgNoActivityTimeOut_Type(Integer32):
    """Custom type sysClassCfgNoActivityTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysClassCfgNoActivityTimeOut_Type.__name__ = "Integer32"
_SysClassCfgNoActivityTimeOut_Object = MibTableColumn
sysClassCfgNoActivityTimeOut = _SysClassCfgNoActivityTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 5, 1, 6),
    _SysClassCfgNoActivityTimeOut_Type()
)
sysClassCfgNoActivityTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysClassCfgNoActivityTimeOut.setStatus("mandatory")


class _SysClassCfgEntryStatus_Type(Integer32):
    """Custom type sysClassCfgEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_SysClassCfgEntryStatus_Type.__name__ = "Integer32"
_SysClassCfgEntryStatus_Object = MibTableColumn
sysClassCfgEntryStatus = _SysClassCfgEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 5, 1, 7),
    _SysClassCfgEntryStatus_Type()
)
sysClassCfgEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysClassCfgEntryStatus.setStatus("mandatory")


class _SysAccessNodeName_Type(DisplayString):
    """Custom type sysAccessNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SysAccessNodeName_Type.__name__ = "DisplayString"
_SysAccessNodeName_Object = MibScalar
sysAccessNodeName = _SysAccessNodeName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 6),
    _SysAccessNodeName_Type()
)
sysAccessNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAccessNodeName.setStatus("mandatory")
_SysFlashDownloadGroup_ObjectIdentity = ObjectIdentity
sysFlashDownloadGroup = _SysFlashDownloadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 7)
)


class _SysFlashDownloadPassword_Type(DisplayString):
    """Custom type sysFlashDownloadPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SysFlashDownloadPassword_Type.__name__ = "DisplayString"
_SysFlashDownloadPassword_Object = MibScalar
sysFlashDownloadPassword = _SysFlashDownloadPassword_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 7, 1),
    _SysFlashDownloadPassword_Type()
)
sysFlashDownloadPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sysFlashDownloadPassword.setStatus("mandatory")


class _SysFlashDownloadUseFile_Type(Integer32):
    """Custom type sysFlashDownloadUseFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mostRecent", 1),
          ("useFileOne", 2),
          ("useFileTwo", 3))
    )


_SysFlashDownloadUseFile_Type.__name__ = "Integer32"
_SysFlashDownloadUseFile_Object = MibScalar
sysFlashDownloadUseFile = _SysFlashDownloadUseFile_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 7, 2),
    _SysFlashDownloadUseFile_Type()
)
sysFlashDownloadUseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFlashDownloadUseFile.setStatus("mandatory")
_SysFlashDownloadDataActivityTimeout_Type = Integer32
_SysFlashDownloadDataActivityTimeout_Object = MibScalar
sysFlashDownloadDataActivityTimeout = _SysFlashDownloadDataActivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 7, 3),
    _SysFlashDownloadDataActivityTimeout_Type()
)
sysFlashDownloadDataActivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFlashDownloadDataActivityTimeout.setStatus("mandatory")


class _SysMeshRouting_Type(Integer32):
    """Custom type sysMeshRouting based on Integer32"""
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


_SysMeshRouting_Type.__name__ = "Integer32"
_SysMeshRouting_Object = MibScalar
sysMeshRouting = _SysMeshRouting_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 8),
    _SysMeshRouting_Type()
)
sysMeshRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMeshRouting.setStatus("mandatory")


class _SysBootID_Type(DisplayString):
    """Custom type sysBootID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_SysBootID_Type.__name__ = "DisplayString"
_SysBootID_Object = MibScalar
sysBootID = _SysBootID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 9),
    _SysBootID_Type()
)
sysBootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootID.setStatus("mandatory")


class _SysNetTime_Type(OctetString):
    """Custom type sysNetTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SysNetTime_Type.__name__ = "OctetString"
_SysNetTime_Object = MibScalar
sysNetTime = _SysNetTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 10),
    _SysNetTime_Type()
)
sysNetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNetTime.setStatus("mandatory")
_SysCodeDownloadGroup_ObjectIdentity = ObjectIdentity
sysCodeDownloadGroup = _SysCodeDownloadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11)
)


class _SysCodeDownloadType_Type(Integer32):
    """Custom type sysCodeDownloadType based on Integer32"""
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
        *(("ccmBase", 1),
          ("eamModule", 4),
          ("eli2Module", 5),
          ("tamModule", 3),
          ("voiceModule", 2))
    )


_SysCodeDownloadType_Type.__name__ = "Integer32"
_SysCodeDownloadType_Object = MibScalar
sysCodeDownloadType = _SysCodeDownloadType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11, 1),
    _SysCodeDownloadType_Type()
)
sysCodeDownloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCodeDownloadType.setStatus("mandatory")


class _SysCodeDownloadNodeName_Type(DisplayString):
    """Custom type sysCodeDownloadNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SysCodeDownloadNodeName_Type.__name__ = "DisplayString"
_SysCodeDownloadNodeName_Object = MibScalar
sysCodeDownloadNodeName = _SysCodeDownloadNodeName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11, 2),
    _SysCodeDownloadNodeName_Type()
)
sysCodeDownloadNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCodeDownloadNodeName.setStatus("mandatory")


class _SysCodeDownloadSlotNumber_Type(Integer32):
    """Custom type sysCodeDownloadSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SysCodeDownloadSlotNumber_Type.__name__ = "Integer32"
_SysCodeDownloadSlotNumber_Object = MibScalar
sysCodeDownloadSlotNumber = _SysCodeDownloadSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11, 3),
    _SysCodeDownloadSlotNumber_Type()
)
sysCodeDownloadSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCodeDownloadSlotNumber.setStatus("mandatory")
_SysCodeDownloadChannelNumber_Type = Integer32
_SysCodeDownloadChannelNumber_Object = MibScalar
sysCodeDownloadChannelNumber = _SysCodeDownloadChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11, 4),
    _SysCodeDownloadChannelNumber_Type()
)
sysCodeDownloadChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCodeDownloadChannelNumber.setStatus("mandatory")


class _SysCodeDownloadImageFile_Type(DisplayString):
    """Custom type sysCodeDownloadImageFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SysCodeDownloadImageFile_Type.__name__ = "DisplayString"
_SysCodeDownloadImageFile_Object = MibScalar
sysCodeDownloadImageFile = _SysCodeDownloadImageFile_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11, 5),
    _SysCodeDownloadImageFile_Type()
)
sysCodeDownloadImageFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCodeDownloadImageFile.setStatus("mandatory")


class _SysCodeDownloadFlashBank_Type(Integer32):
    """Custom type sysCodeDownloadFlashBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SysCodeDownloadFlashBank_Type.__name__ = "Integer32"
_SysCodeDownloadFlashBank_Object = MibScalar
sysCodeDownloadFlashBank = _SysCodeDownloadFlashBank_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11, 6),
    _SysCodeDownloadFlashBank_Type()
)
sysCodeDownloadFlashBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCodeDownloadFlashBank.setStatus("mandatory")


class _SysCodeDownloadRestartFromBank_Type(Integer32):
    """Custom type sysCodeDownloadRestartFromBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bankOne", 1),
          ("bankTwo", 2),
          ("mostRecent", 3))
    )


_SysCodeDownloadRestartFromBank_Type.__name__ = "Integer32"
_SysCodeDownloadRestartFromBank_Object = MibScalar
sysCodeDownloadRestartFromBank = _SysCodeDownloadRestartFromBank_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11, 7),
    _SysCodeDownloadRestartFromBank_Type()
)
sysCodeDownloadRestartFromBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCodeDownloadRestartFromBank.setStatus("mandatory")


class _SysCodeDownloadReset_Type(Integer32):
    """Custom type sysCodeDownloadReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontResetAfterDownload", 2),
          ("resetAfterDownload", 1))
    )


_SysCodeDownloadReset_Type.__name__ = "Integer32"
_SysCodeDownloadReset_Object = MibScalar
sysCodeDownloadReset = _SysCodeDownloadReset_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11, 8),
    _SysCodeDownloadReset_Type()
)
sysCodeDownloadReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCodeDownloadReset.setStatus("mandatory")
_SysCodeDownloadActionStatus_Type = Integer32
_SysCodeDownloadActionStatus_Object = MibScalar
sysCodeDownloadActionStatus = _SysCodeDownloadActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11, 9),
    _SysCodeDownloadActionStatus_Type()
)
sysCodeDownloadActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCodeDownloadActionStatus.setStatus("mandatory")
_SysCodeDownloadFileSize_Type = Integer32
_SysCodeDownloadFileSize_Object = MibScalar
sysCodeDownloadFileSize = _SysCodeDownloadFileSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11, 10),
    _SysCodeDownloadFileSize_Type()
)
sysCodeDownloadFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCodeDownloadFileSize.setStatus("mandatory")
_SysCodeDownloadBytesDownloaded_Type = Integer32
_SysCodeDownloadBytesDownloaded_Object = MibScalar
sysCodeDownloadBytesDownloaded = _SysCodeDownloadBytesDownloaded_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11, 11),
    _SysCodeDownloadBytesDownloaded_Type()
)
sysCodeDownloadBytesDownloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCodeDownloadBytesDownloaded.setStatus("mandatory")
_SysCodeDownloadNodeNumber_Type = Integer32
_SysCodeDownloadNodeNumber_Object = MibScalar
sysCodeDownloadNodeNumber = _SysCodeDownloadNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 1, 11, 12),
    _SysCodeDownloadNodeNumber_Type()
)
sysCodeDownloadNodeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCodeDownloadNodeNumber.setStatus("mandatory")
_Messages_ObjectIdentity = ObjectIdentity
messages = _Messages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2)
)


class _SysMessageWelcome_Type(DisplayString):
    """Custom type sysMessageWelcome based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 61),
    )


_SysMessageWelcome_Type.__name__ = "DisplayString"
_SysMessageWelcome_Object = MibScalar
sysMessageWelcome = _SysMessageWelcome_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 1),
    _SysMessageWelcome_Type()
)
sysMessageWelcome.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageWelcome.setStatus("mandatory")


class _SysMessageChannelPasswd_Type(DisplayString):
    """Custom type sysMessageChannelPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SysMessageChannelPasswd_Type.__name__ = "DisplayString"
_SysMessageChannelPasswd_Object = MibScalar
sysMessageChannelPasswd = _SysMessageChannelPasswd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 2),
    _SysMessageChannelPasswd_Type()
)
sysMessageChannelPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageChannelPasswd.setStatus("mandatory")


class _SysMessageClassRequest_Type(DisplayString):
    """Custom type sysMessageClassRequest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SysMessageClassRequest_Type.__name__ = "DisplayString"
_SysMessageClassRequest_Object = MibScalar
sysMessageClassRequest = _SysMessageClassRequest_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 3),
    _SysMessageClassRequest_Type()
)
sysMessageClassRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageClassRequest.setStatus("mandatory")


class _SysMessageConnected_Type(DisplayString):
    """Custom type sysMessageConnected based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SysMessageConnected_Type.__name__ = "DisplayString"
_SysMessageConnected_Object = MibScalar
sysMessageConnected = _SysMessageConnected_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 4),
    _SysMessageConnected_Type()
)
sysMessageConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageConnected.setStatus("mandatory")


class _SysMessageQueued_Type(DisplayString):
    """Custom type sysMessageQueued based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_SysMessageQueued_Type.__name__ = "DisplayString"
_SysMessageQueued_Object = MibScalar
sysMessageQueued = _SysMessageQueued_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 5),
    _SysMessageQueued_Type()
)
sysMessageQueued.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageQueued.setStatus("mandatory")


class _SysMessageDisconnected_Type(DisplayString):
    """Custom type sysMessageDisconnected based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_SysMessageDisconnected_Type.__name__ = "DisplayString"
_SysMessageDisconnected_Object = MibScalar
sysMessageDisconnected = _SysMessageDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 6),
    _SysMessageDisconnected_Type()
)
sysMessageDisconnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageDisconnected.setStatus("mandatory")


class _SysMessageCallInProgress_Type(DisplayString):
    """Custom type sysMessageCallInProgress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_SysMessageCallInProgress_Type.__name__ = "DisplayString"
_SysMessageCallInProgress_Object = MibScalar
sysMessageCallInProgress = _SysMessageCallInProgress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 7),
    _SysMessageCallInProgress_Type()
)
sysMessageCallInProgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageCallInProgress.setStatus("mandatory")


class _SysMessageNoAnswer_Type(DisplayString):
    """Custom type sysMessageNoAnswer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_SysMessageNoAnswer_Type.__name__ = "DisplayString"
_SysMessageNoAnswer_Object = MibScalar
sysMessageNoAnswer = _SysMessageNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 8),
    _SysMessageNoAnswer_Type()
)
sysMessageNoAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageNoAnswer.setStatus("mandatory")


class _SysMessageUnassigned_Type(DisplayString):
    """Custom type sysMessageUnassigned based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_SysMessageUnassigned_Type.__name__ = "DisplayString"
_SysMessageUnassigned_Object = MibScalar
sysMessageUnassigned = _SysMessageUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 9),
    _SysMessageUnassigned_Type()
)
sysMessageUnassigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageUnassigned.setStatus("mandatory")


class _SysMessageUnavailable_Type(DisplayString):
    """Custom type sysMessageUnavailable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_SysMessageUnavailable_Type.__name__ = "DisplayString"
_SysMessageUnavailable_Object = MibScalar
sysMessageUnavailable = _SysMessageUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 10),
    _SysMessageUnavailable_Type()
)
sysMessageUnavailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageUnavailable.setStatus("mandatory")


class _SysMessageBusy_Type(DisplayString):
    """Custom type sysMessageBusy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_SysMessageBusy_Type.__name__ = "DisplayString"
_SysMessageBusy_Object = MibScalar
sysMessageBusy = _SysMessageBusy_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 11),
    _SysMessageBusy_Type()
)
sysMessageBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageBusy.setStatus("mandatory")


class _SysMessageIncompatible_Type(DisplayString):
    """Custom type sysMessageIncompatible based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_SysMessageIncompatible_Type.__name__ = "DisplayString"
_SysMessageIncompatible_Object = MibScalar
sysMessageIncompatible = _SysMessageIncompatible_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 12),
    _SysMessageIncompatible_Type()
)
sysMessageIncompatible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageIncompatible.setStatus("mandatory")


class _SysMessageClassPasswd_Type(DisplayString):
    """Custom type sysMessageClassPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SysMessageClassPasswd_Type.__name__ = "DisplayString"
_SysMessageClassPasswd_Object = MibScalar
sysMessageClassPasswd = _SysMessageClassPasswd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 13),
    _SysMessageClassPasswd_Type()
)
sysMessageClassPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageClassPasswd.setStatus("mandatory")


class _SysMessageLCDKeypadBanner_Type(DisplayString):
    """Custom type sysMessageLCDKeypadBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SysMessageLCDKeypadBanner_Type.__name__ = "DisplayString"
_SysMessageLCDKeypadBanner_Object = MibScalar
sysMessageLCDKeypadBanner = _SysMessageLCDKeypadBanner_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 1, 2, 14),
    _SysMessageLCDKeypadBanner_Type()
)
sysMessageLCDKeypadBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMessageLCDKeypadBanner.setStatus("mandatory")
_Card_ObjectIdentity = ObjectIdentity
card = _Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2)
)
_CardTable_Object = MibTable
cardTable = _CardTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cardTable.setStatus("mandatory")
_CardEntry_Object = MibTableRow
cardEntry = _CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 1, 1)
)
cardEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "cardSlotNumber"),
)
if mibBuilder.loadTexts:
    cardEntry.setStatus("mandatory")


class _CardSlotNumber_Type(Integer32):
    """Custom type cardSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("slotA", 1),
          ("slotB", 2),
          ("slotC", 3),
          ("slotD", 4),
          ("slotE", 5),
          ("slotNMS", 6))
    )


_CardSlotNumber_Type.__name__ = "Integer32"
_CardSlotNumber_Object = MibTableColumn
cardSlotNumber = _CardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 1, 1, 1),
    _CardSlotNumber_Type()
)
cardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSlotNumber.setStatus("mandatory")


class _CardModuleID_Type(Integer32):
    """Custom type cardModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              8,
              9,
              12,
              13,
              14,
              15,
              16,
              18,
              20,
              24,
              28,
              36,
              48,
              49,
              52,
              53,
              56,
              57,
              60,
              61,
              64,
              68,
              72,
              76,
              78,
              80,
              82,
              84,
              85,
              92,
              94,
              96,
              97,
              104,
              105,
              108,
              109,
              112,
              116,
              117,
              120,
              121,
              156,
              320,
              321,
              322,
              340,
              344,
              992,
              993,
              994,
              995,
              996,
              997,
              998,
              999,
              1000,
              1001,
              1005,
              1008,
              1009,
              1010,
              1012,
              1013,
              1016)
        )
    )
    namedValues = NamedValues(
        *(("mod10kCcm", 16),
          ("mod10kCcmOem", 18),
          ("mod1kCcm", 12),
          ("mod1kCcmOem", 14),
          ("mod20kCcm", 20),
          ("mod20kProCcm", 36),
          ("mod2kCcm", 80),
          ("mod2kCcmOEM", 82),
          ("mod2kTurboCcm", 156),
          ("mod3kCcmDualVoice", 85),
          ("mod3kCcmSingleVoice", 84),
          ("mod50ECcm", 13),
          ("mod50ECcmOem", 15),
          ("mod5kCcm", 4),
          ("mod5kCcmOem", 6),
          ("mod5kCcmwESD", 5),
          ("mod5kTurboCcm", 24),
          ("mod5kTurboProCcm", 28),
          ("mod75ECcm", 92),
          ("mod75ECcm-FrameRelay", 76),
          ("mod75ECcm-FrameRelayOEM", 78),
          ("mod75ECcmOEM", 94),
          ("modCEM12Async-1D", 48),
          ("modCEM12Async-1DwESD", 49),
          ("modCEM12Async-LD", 52),
          ("modCEM12Async-LDwESD", 53),
          ("modCEM32-IDD", 72),
          ("modCEM32-IDD2x16", 64),
          ("modCEM6AsyncOnly", 68),
          ("modCEM6Dma", 1016),
          ("modCEM6SyncAsync", 56),
          ("modCEM6SyncAsync-ESD", 57),
          ("modCEM6SyncAsyncDma", 60),
          ("modCEM6SyncAsyncDma-ESD", 61),
          ("modCcmDmaDual20Mhz", 2),
          ("modCcmDmaESD", 1),
          ("modDigitalVoiceExp", 112),
          ("modE1AccessDualPort", 992),
          ("modE1AccessDualPortNoLinks", 994),
          ("modE1AccessSinglePort", 993),
          ("modE1AccessSinglePortNoLinks", 995),
          ("modIsdnMultipleBri", 1000),
          ("modIsdnSingleBri", 1001),
          ("modIsu-1-chan", 1012),
          ("modIsu-2-chan", 1013),
          ("modLan-RemoteLanRouter", 340),
          ("modLan-RemoteLanRouter-LowCost", 344),
          ("modLan-eli-1", 320),
          ("modLan-eli-1-DualProc", 321),
          ("modLan-eli-2", 322),
          ("modModem12dot4KbParadyne", 1009),
          ("modModem14dot4Kb", 1005),
          ("modModem19dot2KbParadyne", 1010),
          ("modModem9dot6Kb", 1008),
          ("modNMS", 8),
          ("modNMS-RTC", 9),
          ("modT1AccessDualPort", 996),
          ("modT1AccessDualPortNoLinks", 998),
          ("modT1AccessSinglePort", 997),
          ("modT1AccessSinglePortNoLinks", 999),
          ("modVoice-1-chan", 96),
          ("modVoice-1-chan-CVM", 120),
          ("modVoice-1-chan-International", 104),
          ("modVoice-1-chan-TUVM", 116),
          ("modVoice-1-chan-UVM", 108),
          ("modVoice-2-chan", 97),
          ("modVoice-2-chan-CVM", 121),
          ("modVoice-2-chan-International", 105),
          ("modVoice-2-chan-TUVM", 117),
          ("modVoice-2-chan-UVM", 109))
    )


_CardModuleID_Type.__name__ = "Integer32"
_CardModuleID_Object = MibTableColumn
cardModuleID = _CardModuleID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 1, 1, 2),
    _CardModuleID_Type()
)
cardModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardModuleID.setStatus("mandatory")


class _CardPcbRevision_Type(Integer32):
    """Custom type cardPcbRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64)
        )
    )
    namedValues = NamedValues(
        *(("rev1", 53),
          ("rev10", 62),
          ("rev11", 63),
          ("rev12", 64),
          ("rev2", 54),
          ("rev3", 55),
          ("rev4", 56),
          ("rev5", 57),
          ("rev6", 58),
          ("rev7", 59),
          ("rev8", 60),
          ("rev9", 61),
          ("revA", 1),
          ("revAA", 27),
          ("revAB", 28),
          ("revAC", 29),
          ("revAD", 30),
          ("revAE", 31),
          ("revAF", 32),
          ("revAG", 33),
          ("revAH", 34),
          ("revAI", 35),
          ("revAJ", 36),
          ("revAK", 37),
          ("revAL", 38),
          ("revAM", 39),
          ("revAN", 40),
          ("revAO", 41),
          ("revAP", 42),
          ("revAQ", 43),
          ("revAR", 44),
          ("revAS", 45),
          ("revAT", 46),
          ("revAU", 47),
          ("revAV", 48),
          ("revAW", 49),
          ("revAX", 50),
          ("revAY", 51),
          ("revAZ", 52),
          ("revB", 2),
          ("revC", 3),
          ("revD", 4),
          ("revE", 5),
          ("revF", 6),
          ("revG", 7),
          ("revH", 8),
          ("revI", 9),
          ("revJ", 10),
          ("revK", 11),
          ("revL", 12),
          ("revM", 13),
          ("revN", 14),
          ("revO", 15),
          ("revP", 16),
          ("revQ", 17),
          ("revR", 18),
          ("revS", 19),
          ("revT", 20),
          ("revU", 21),
          ("revV", 22),
          ("revW", 23),
          ("revX", 24),
          ("revY", 25),
          ("revZ", 26))
    )


_CardPcbRevision_Type.__name__ = "Integer32"
_CardPcbRevision_Object = MibTableColumn
cardPcbRevision = _CardPcbRevision_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 1, 1, 3),
    _CardPcbRevision_Type()
)
cardPcbRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPcbRevision.setStatus("mandatory")


class _NumberOfCards_Type(Integer32):
    """Custom type numberOfCards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_NumberOfCards_Type.__name__ = "Integer32"
_NumberOfCards_Object = MibScalar
numberOfCards = _NumberOfCards_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 2),
    _NumberOfCards_Type()
)
numberOfCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfCards.setStatus("mandatory")
_EliCardFunctionTable_Object = MibTable
eliCardFunctionTable = _EliCardFunctionTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    eliCardFunctionTable.setStatus("mandatory")
_EliCardFunctionEntry_Object = MibTableRow
eliCardFunctionEntry = _EliCardFunctionEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 3, 1)
)
eliCardFunctionEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "eliCardFunctionSlotNumber"),
)
if mibBuilder.loadTexts:
    eliCardFunctionEntry.setStatus("mandatory")


class _EliCardFunctionSlotNumber_Type(Integer32):
    """Custom type eliCardFunctionSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_EliCardFunctionSlotNumber_Type.__name__ = "Integer32"
_EliCardFunctionSlotNumber_Object = MibTableColumn
eliCardFunctionSlotNumber = _EliCardFunctionSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 3, 1, 1),
    _EliCardFunctionSlotNumber_Type()
)
eliCardFunctionSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eliCardFunctionSlotNumber.setStatus("mandatory")


class _EliCardFunctionPromID_Type(DisplayString):
    """Custom type eliCardFunctionPromID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_EliCardFunctionPromID_Type.__name__ = "DisplayString"
_EliCardFunctionPromID_Object = MibTableColumn
eliCardFunctionPromID = _EliCardFunctionPromID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 3, 1, 2),
    _EliCardFunctionPromID_Type()
)
eliCardFunctionPromID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eliCardFunctionPromID.setStatus("mandatory")


class _EliCardFunctionTypeRTSFunction_Type(Integer32):
    """Custom type eliCardFunctionTypeRTSFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_EliCardFunctionTypeRTSFunction_Type.__name__ = "Integer32"
_EliCardFunctionTypeRTSFunction_Object = MibTableColumn
eliCardFunctionTypeRTSFunction = _EliCardFunctionTypeRTSFunction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 3, 1, 3),
    _EliCardFunctionTypeRTSFunction_Type()
)
eliCardFunctionTypeRTSFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eliCardFunctionTypeRTSFunction.setStatus("mandatory")


class _EliCardFunctionTypeBridgeFunction_Type(Integer32):
    """Custom type eliCardFunctionTypeBridgeFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_EliCardFunctionTypeBridgeFunction_Type.__name__ = "Integer32"
_EliCardFunctionTypeBridgeFunction_Object = MibTableColumn
eliCardFunctionTypeBridgeFunction = _EliCardFunctionTypeBridgeFunction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 3, 1, 4),
    _EliCardFunctionTypeBridgeFunction_Type()
)
eliCardFunctionTypeBridgeFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eliCardFunctionTypeBridgeFunction.setStatus("mandatory")


class _EliCardFunctionTypeRouterFunction_Type(Integer32):
    """Custom type eliCardFunctionTypeRouterFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_EliCardFunctionTypeRouterFunction_Type.__name__ = "Integer32"
_EliCardFunctionTypeRouterFunction_Object = MibTableColumn
eliCardFunctionTypeRouterFunction = _EliCardFunctionTypeRouterFunction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 3, 1, 5),
    _EliCardFunctionTypeRouterFunction_Type()
)
eliCardFunctionTypeRouterFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eliCardFunctionTypeRouterFunction.setStatus("mandatory")


class _EliCardFunctionFlashMemory_Type(Integer32):
    """Custom type eliCardFunctionFlashMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_EliCardFunctionFlashMemory_Type.__name__ = "Integer32"
_EliCardFunctionFlashMemory_Object = MibTableColumn
eliCardFunctionFlashMemory = _EliCardFunctionFlashMemory_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 3, 1, 6),
    _EliCardFunctionFlashMemory_Type()
)
eliCardFunctionFlashMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eliCardFunctionFlashMemory.setStatus("mandatory")
_T1e1CardSoftwareInfoTable_Object = MibTable
t1e1CardSoftwareInfoTable = _T1e1CardSoftwareInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    t1e1CardSoftwareInfoTable.setStatus("mandatory")
_T1e1CardSoftwareInfoEntry_Object = MibTableRow
t1e1CardSoftwareInfoEntry = _T1e1CardSoftwareInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 4, 1)
)
t1e1CardSoftwareInfoEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "t1e1CardSoftwareInfoCardNumber"),
)
if mibBuilder.loadTexts:
    t1e1CardSoftwareInfoEntry.setStatus("mandatory")


class _T1e1CardSoftwareInfoCardNumber_Type(Integer32):
    """Custom type t1e1CardSoftwareInfoCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_T1e1CardSoftwareInfoCardNumber_Type.__name__ = "Integer32"
_T1e1CardSoftwareInfoCardNumber_Object = MibTableColumn
t1e1CardSoftwareInfoCardNumber = _T1e1CardSoftwareInfoCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 4, 1, 1),
    _T1e1CardSoftwareInfoCardNumber_Type()
)
t1e1CardSoftwareInfoCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CardSoftwareInfoCardNumber.setStatus("mandatory")


class _T1e1CardSoftwareInfoCardType_Type(Integer32):
    """Custom type t1e1CardSoftwareInfoCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_T1e1CardSoftwareInfoCardType_Type.__name__ = "Integer32"
_T1e1CardSoftwareInfoCardType_Object = MibTableColumn
t1e1CardSoftwareInfoCardType = _T1e1CardSoftwareInfoCardType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 4, 1, 2),
    _T1e1CardSoftwareInfoCardType_Type()
)
t1e1CardSoftwareInfoCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CardSoftwareInfoCardType.setStatus("mandatory")


class _T1e1CardSoftwareInfoReleaseLevel_Type(Integer32):
    """Custom type t1e1CardSoftwareInfoReleaseLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("releaseOne", 2),
          ("releaseTwo", 3),
          ("releaseZero", 1))
    )


_T1e1CardSoftwareInfoReleaseLevel_Type.__name__ = "Integer32"
_T1e1CardSoftwareInfoReleaseLevel_Object = MibTableColumn
t1e1CardSoftwareInfoReleaseLevel = _T1e1CardSoftwareInfoReleaseLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 4, 1, 3),
    _T1e1CardSoftwareInfoReleaseLevel_Type()
)
t1e1CardSoftwareInfoReleaseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CardSoftwareInfoReleaseLevel.setStatus("mandatory")
_T1e1CardSoftwareInfoSoftwareID_Type = DisplayString
_T1e1CardSoftwareInfoSoftwareID_Object = MibTableColumn
t1e1CardSoftwareInfoSoftwareID = _T1e1CardSoftwareInfoSoftwareID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 4, 1, 4),
    _T1e1CardSoftwareInfoSoftwareID_Type()
)
t1e1CardSoftwareInfoSoftwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CardSoftwareInfoSoftwareID.setStatus("mandatory")
_T1e1CardSoftwareInfoBootCode_Type = DisplayString
_T1e1CardSoftwareInfoBootCode_Object = MibTableColumn
t1e1CardSoftwareInfoBootCode = _T1e1CardSoftwareInfoBootCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 2, 4, 1, 5),
    _T1e1CardSoftwareInfoBootCode_Type()
)
t1e1CardSoftwareInfoBootCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CardSoftwareInfoBootCode.setStatus("mandatory")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3)
)
_PortCfgTable_Object = MibTable
portCfgTable = _PortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    portCfgTable.setStatus("mandatory")
_PortCfgEntry_Object = MibTableRow
portCfgEntry = _PortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 1, 1)
)
portCfgEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "portCfgCardNumber"),
    (0, "MICOM-NODE-MIB", "portCfgChannelNumber"),
)
if mibBuilder.loadTexts:
    portCfgEntry.setStatus("mandatory")


class _PortCfgCardNumber_Type(Integer32):
    """Custom type portCfgCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PortCfgCardNumber_Type.__name__ = "Integer32"
_PortCfgCardNumber_Object = MibTableColumn
portCfgCardNumber = _PortCfgCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 1, 1, 1),
    _PortCfgCardNumber_Type()
)
portCfgCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCfgCardNumber.setStatus("mandatory")


class _PortCfgChannelNumber_Type(Integer32):
    """Custom type portCfgChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_PortCfgChannelNumber_Type.__name__ = "Integer32"
_PortCfgChannelNumber_Object = MibTableColumn
portCfgChannelNumber = _PortCfgChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 1, 1, 2),
    _PortCfgChannelNumber_Type()
)
portCfgChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCfgChannelNumber.setStatus("mandatory")


class _PortCfgChannelType_Type(Integer32):
    """Custom type portCfgChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("esi", 4),
          ("esiSecondary", 7),
          ("frameRelay", 8),
          ("localEsi", 6),
          ("mux", 1),
          ("sync", 3),
          ("x21", 5))
    )


_PortCfgChannelType_Type.__name__ = "Integer32"
_PortCfgChannelType_Object = MibTableColumn
portCfgChannelType = _PortCfgChannelType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 1, 1, 3),
    _PortCfgChannelType_Type()
)
portCfgChannelType.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    portCfgChannelType.setStatus("mandatory")
_SyncPortCfgTable_Object = MibTable
syncPortCfgTable = _SyncPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    syncPortCfgTable.setStatus("mandatory")
_SyncPortCfgEntry_Object = MibTableRow
syncPortCfgEntry = _SyncPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 2, 1)
)
syncPortCfgEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "syncPortCfgCardNumber"),
    (0, "MICOM-NODE-MIB", "syncPortCfgChannelNumber"),
)
if mibBuilder.loadTexts:
    syncPortCfgEntry.setStatus("mandatory")


class _SyncPortCfgCardNumber_Type(Integer32):
    """Custom type syncPortCfgCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SyncPortCfgCardNumber_Type.__name__ = "Integer32"
_SyncPortCfgCardNumber_Object = MibTableColumn
syncPortCfgCardNumber = _SyncPortCfgCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 2, 1, 1),
    _SyncPortCfgCardNumber_Type()
)
syncPortCfgCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncPortCfgCardNumber.setStatus("mandatory")


class _SyncPortCfgChannelNumber_Type(Integer32):
    """Custom type syncPortCfgChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SyncPortCfgChannelNumber_Type.__name__ = "Integer32"
_SyncPortCfgChannelNumber_Object = MibTableColumn
syncPortCfgChannelNumber = _SyncPortCfgChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 2, 1, 2),
    _SyncPortCfgChannelNumber_Type()
)
syncPortCfgChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncPortCfgChannelNumber.setStatus("mandatory")


class _SyncPortCfgProtocol_Type(Integer32):
    """Custom type syncPortCfgProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("asciiBisync", 2),
          ("dlcChannel", 1),
          ("ebcdicBisync", 3),
          ("fastPacket", 9),
          ("hpSync", 4),
          ("micomDlc", 7),
          ("micomVoice", 8),
          ("rts", 5),
          ("syncPad", 6),
          ("tdm", 10))
    )


_SyncPortCfgProtocol_Type.__name__ = "Integer32"
_SyncPortCfgProtocol_Object = MibTableColumn
syncPortCfgProtocol = _SyncPortCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 2, 1, 3),
    _SyncPortCfgProtocol_Type()
)
syncPortCfgProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncPortCfgProtocol.setStatus("mandatory")
_FCmdPortPhyParaTable_Object = MibTable
fCmdPortPhyParaTable = _FCmdPortPhyParaTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    fCmdPortPhyParaTable.setStatus("mandatory")
_FCmdPortPhyParaEntry_Object = MibTableRow
fCmdPortPhyParaEntry = _FCmdPortPhyParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 3, 1)
)
fCmdPortPhyParaEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "fCmdPortPhyParaCardNumber"),
    (0, "MICOM-NODE-MIB", "fCmdPortPhyParaChannelNumber"),
)
if mibBuilder.loadTexts:
    fCmdPortPhyParaEntry.setStatus("mandatory")


class _FCmdPortPhyParaCardNumber_Type(Integer32):
    """Custom type fCmdPortPhyParaCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 6),
    )


_FCmdPortPhyParaCardNumber_Type.__name__ = "Integer32"
_FCmdPortPhyParaCardNumber_Object = MibTableColumn
fCmdPortPhyParaCardNumber = _FCmdPortPhyParaCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 3, 1, 1),
    _FCmdPortPhyParaCardNumber_Type()
)
fCmdPortPhyParaCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCmdPortPhyParaCardNumber.setStatus("mandatory")


class _FCmdPortPhyParaChannelNumber_Type(Integer32):
    """Custom type fCmdPortPhyParaChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_FCmdPortPhyParaChannelNumber_Type.__name__ = "Integer32"
_FCmdPortPhyParaChannelNumber_Object = MibTableColumn
fCmdPortPhyParaChannelNumber = _FCmdPortPhyParaChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 3, 1, 2),
    _FCmdPortPhyParaChannelNumber_Type()
)
fCmdPortPhyParaChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fCmdPortPhyParaChannelNumber.setStatus("mandatory")


class _FCmdPortPhyParaStopBits_Type(Integer32):
    """Custom type fCmdPortPhyParaStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onePointFiveBits", 2),
          ("onebit", 1),
          ("twoBits", 3))
    )


_FCmdPortPhyParaStopBits_Type.__name__ = "Integer32"
_FCmdPortPhyParaStopBits_Object = MibTableColumn
fCmdPortPhyParaStopBits = _FCmdPortPhyParaStopBits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 3, 1, 3),
    _FCmdPortPhyParaStopBits_Type()
)
fCmdPortPhyParaStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fCmdPortPhyParaStopBits.setStatus("mandatory")


class _FCmdPortPhyParaCodeLevel_Type(Integer32):
    """Custom type fCmdPortPhyParaCodeLevel based on Integer32"""
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
        *(("eightBits", 4),
          ("fiveBits", 1),
          ("nineBits", 5),
          ("sevenBits", 3),
          ("sixBits", 2))
    )


_FCmdPortPhyParaCodeLevel_Type.__name__ = "Integer32"
_FCmdPortPhyParaCodeLevel_Object = MibTableColumn
fCmdPortPhyParaCodeLevel = _FCmdPortPhyParaCodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 3, 1, 4),
    _FCmdPortPhyParaCodeLevel_Type()
)
fCmdPortPhyParaCodeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fCmdPortPhyParaCodeLevel.setStatus("mandatory")


class _FCmdPortPhyParaDataRate_Type(Integer32):
    """Custom type fCmdPortPhyParaDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("abr", 1),
          ("rate110", 4),
          ("rate1200", 11),
          ("rate134dot5", 5),
          ("rate14400", 18),
          ("rate150", 6),
          ("rate1800", 12),
          ("rate19200", 19),
          ("rate200", 7),
          ("rate225", 8),
          ("rate2400", 13),
          ("rate28800", 20),
          ("rate300", 9),
          ("rate3600", 14),
          ("rate38400", 21),
          ("rate4800", 15),
          ("rate50", 2),
          ("rate600", 10),
          ("rate7200", 16),
          ("rate75", 3),
          ("rate9600", 17))
    )


_FCmdPortPhyParaDataRate_Type.__name__ = "Integer32"
_FCmdPortPhyParaDataRate_Object = MibTableColumn
fCmdPortPhyParaDataRate = _FCmdPortPhyParaDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 3, 1, 5),
    _FCmdPortPhyParaDataRate_Type()
)
fCmdPortPhyParaDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fCmdPortPhyParaDataRate.setStatus("mandatory")


class _FCmdPortPhyParaEcho_Type(Integer32):
    """Custom type fCmdPortPhyParaEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_FCmdPortPhyParaEcho_Type.__name__ = "Integer32"
_FCmdPortPhyParaEcho_Object = MibTableColumn
fCmdPortPhyParaEcho = _FCmdPortPhyParaEcho_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 3, 1, 6),
    _FCmdPortPhyParaEcho_Type()
)
fCmdPortPhyParaEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fCmdPortPhyParaEcho.setStatus("mandatory")


class _FCmdPortPhyParaCRDelay_Type(Integer32):
    """Custom type fCmdPortPhyParaCRDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_FCmdPortPhyParaCRDelay_Type.__name__ = "Integer32"
_FCmdPortPhyParaCRDelay_Object = MibTableColumn
fCmdPortPhyParaCRDelay = _FCmdPortPhyParaCRDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 3, 1, 7),
    _FCmdPortPhyParaCRDelay_Type()
)
fCmdPortPhyParaCRDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fCmdPortPhyParaCRDelay.setStatus("mandatory")


class _FCmdPortPhyParaLFDelay_Type(Integer32):
    """Custom type fCmdPortPhyParaLFDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_FCmdPortPhyParaLFDelay_Type.__name__ = "Integer32"
_FCmdPortPhyParaLFDelay_Object = MibTableColumn
fCmdPortPhyParaLFDelay = _FCmdPortPhyParaLFDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 3, 1, 8),
    _FCmdPortPhyParaLFDelay_Type()
)
fCmdPortPhyParaLFDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fCmdPortPhyParaLFDelay.setStatus("mandatory")


class _FCmdPortPhyParaFFDelay_Type(Integer32):
    """Custom type fCmdPortPhyParaFFDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_FCmdPortPhyParaFFDelay_Type.__name__ = "Integer32"
_FCmdPortPhyParaFFDelay_Object = MibTableColumn
fCmdPortPhyParaFFDelay = _FCmdPortPhyParaFFDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 3, 1, 9),
    _FCmdPortPhyParaFFDelay_Type()
)
fCmdPortPhyParaFFDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fCmdPortPhyParaFFDelay.setStatus("mandatory")


class _FCmdPortPhyParaParity_Type(Integer32):
    """Custom type fCmdPortPhyParaParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 6),
          ("even", 3),
          ("mark", 4),
          ("none", 5),
          ("odd", 2),
          ("space", 1))
    )


_FCmdPortPhyParaParity_Type.__name__ = "Integer32"
_FCmdPortPhyParaParity_Object = MibTableColumn
fCmdPortPhyParaParity = _FCmdPortPhyParaParity_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 3, 1, 10),
    _FCmdPortPhyParaParity_Type()
)
fCmdPortPhyParaParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fCmdPortPhyParaParity.setStatus("mandatory")
_LogPortPhyParaTable_Object = MibTable
logPortPhyParaTable = _LogPortPhyParaTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    logPortPhyParaTable.setStatus("mandatory")
_LogPortPhyParaEntry_Object = MibTableRow
logPortPhyParaEntry = _LogPortPhyParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1)
)
logPortPhyParaEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "logPortPhyParaCardNumber"),
    (0, "MICOM-NODE-MIB", "logPortPhyParaChannelNumber"),
)
if mibBuilder.loadTexts:
    logPortPhyParaEntry.setStatus("mandatory")


class _LogPortPhyParaCardNumber_Type(Integer32):
    """Custom type logPortPhyParaCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 6),
    )


_LogPortPhyParaCardNumber_Type.__name__ = "Integer32"
_LogPortPhyParaCardNumber_Object = MibTableColumn
logPortPhyParaCardNumber = _LogPortPhyParaCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 1),
    _LogPortPhyParaCardNumber_Type()
)
logPortPhyParaCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logPortPhyParaCardNumber.setStatus("mandatory")


class _LogPortPhyParaChannelNumber_Type(Integer32):
    """Custom type logPortPhyParaChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_LogPortPhyParaChannelNumber_Type.__name__ = "Integer32"
_LogPortPhyParaChannelNumber_Object = MibTableColumn
logPortPhyParaChannelNumber = _LogPortPhyParaChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 2),
    _LogPortPhyParaChannelNumber_Type()
)
logPortPhyParaChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logPortPhyParaChannelNumber.setStatus("mandatory")


class _LogPortPhyParaStopBits_Type(Integer32):
    """Custom type logPortPhyParaStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneBit", 1),
          ("onePointFiveBits", 2),
          ("twoBits", 3))
    )


_LogPortPhyParaStopBits_Type.__name__ = "Integer32"
_LogPortPhyParaStopBits_Object = MibTableColumn
logPortPhyParaStopBits = _LogPortPhyParaStopBits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 3),
    _LogPortPhyParaStopBits_Type()
)
logPortPhyParaStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPortPhyParaStopBits.setStatus("mandatory")


class _LogPortPhyParaCodeLevel_Type(Integer32):
    """Custom type logPortPhyParaCodeLevel based on Integer32"""
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
        *(("eightBits", 4),
          ("fiveBits", 1),
          ("nineBits", 5),
          ("sevenBits", 3),
          ("sixBits", 2))
    )


_LogPortPhyParaCodeLevel_Type.__name__ = "Integer32"
_LogPortPhyParaCodeLevel_Object = MibTableColumn
logPortPhyParaCodeLevel = _LogPortPhyParaCodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 4),
    _LogPortPhyParaCodeLevel_Type()
)
logPortPhyParaCodeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPortPhyParaCodeLevel.setStatus("mandatory")


class _LogPortPhyParaDataRate_Type(Integer32):
    """Custom type logPortPhyParaDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("rate110", 4),
          ("rate1200", 11),
          ("rate134dot5", 5),
          ("rate14400", 18),
          ("rate150", 6),
          ("rate1800", 12),
          ("rate19200", 19),
          ("rate200", 7),
          ("rate2400", 13),
          ("rate28800", 20),
          ("rate300", 9),
          ("rate3600", 14),
          ("rate38400", 21),
          ("rate4800", 15),
          ("rate50", 2),
          ("rate600", 10),
          ("rate7200", 16),
          ("rate75", 3),
          ("rate9600", 17))
    )


_LogPortPhyParaDataRate_Type.__name__ = "Integer32"
_LogPortPhyParaDataRate_Object = MibTableColumn
logPortPhyParaDataRate = _LogPortPhyParaDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 5),
    _LogPortPhyParaDataRate_Type()
)
logPortPhyParaDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPortPhyParaDataRate.setStatus("mandatory")


class _LogPortPhyParaCRDelay_Type(Integer32):
    """Custom type logPortPhyParaCRDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_LogPortPhyParaCRDelay_Type.__name__ = "Integer32"
_LogPortPhyParaCRDelay_Object = MibTableColumn
logPortPhyParaCRDelay = _LogPortPhyParaCRDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 6),
    _LogPortPhyParaCRDelay_Type()
)
logPortPhyParaCRDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPortPhyParaCRDelay.setStatus("mandatory")


class _LogPortPhyParaLFDelay_Type(Integer32):
    """Custom type logPortPhyParaLFDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_LogPortPhyParaLFDelay_Type.__name__ = "Integer32"
_LogPortPhyParaLFDelay_Object = MibTableColumn
logPortPhyParaLFDelay = _LogPortPhyParaLFDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 7),
    _LogPortPhyParaLFDelay_Type()
)
logPortPhyParaLFDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPortPhyParaLFDelay.setStatus("mandatory")


class _LogPortPhyParaFFDelay_Type(Integer32):
    """Custom type logPortPhyParaFFDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_LogPortPhyParaFFDelay_Type.__name__ = "Integer32"
_LogPortPhyParaFFDelay_Object = MibTableColumn
logPortPhyParaFFDelay = _LogPortPhyParaFFDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 8),
    _LogPortPhyParaFFDelay_Type()
)
logPortPhyParaFFDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPortPhyParaFFDelay.setStatus("mandatory")


class _LogPortPhyParaXONChar_Type(Integer32):
    """Custom type logPortPhyParaXONChar based on Integer32"""
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
        *(("dc1", 1),
          ("dc2", 2),
          ("dc3", 3),
          ("dc4", 4))
    )


_LogPortPhyParaXONChar_Type.__name__ = "Integer32"
_LogPortPhyParaXONChar_Object = MibTableColumn
logPortPhyParaXONChar = _LogPortPhyParaXONChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 9),
    _LogPortPhyParaXONChar_Type()
)
logPortPhyParaXONChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPortPhyParaXONChar.setStatus("mandatory")


class _LogPortPhyParaXOFFChar_Type(Integer32):
    """Custom type logPortPhyParaXOFFChar based on Integer32"""
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
        *(("dc1", 1),
          ("dc2", 2),
          ("dc3", 3),
          ("dc4", 4))
    )


_LogPortPhyParaXOFFChar_Type.__name__ = "Integer32"
_LogPortPhyParaXOFFChar_Object = MibTableColumn
logPortPhyParaXOFFChar = _LogPortPhyParaXOFFChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 10),
    _LogPortPhyParaXOFFChar_Type()
)
logPortPhyParaXOFFChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPortPhyParaXOFFChar.setStatus("mandatory")


class _LogPortPhyParaFlowControl_Type(Integer32):
    """Custom type logPortPhyParaFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dataGeneral", 7),
          ("dtr", 3),
          ("none", 1),
          ("rts", 6),
          ("wangx", 5),
          ("xonXof", 2),
          ("xonXofDtr", 4))
    )


_LogPortPhyParaFlowControl_Type.__name__ = "Integer32"
_LogPortPhyParaFlowControl_Object = MibTableColumn
logPortPhyParaFlowControl = _LogPortPhyParaFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 11),
    _LogPortPhyParaFlowControl_Type()
)
logPortPhyParaFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPortPhyParaFlowControl.setStatus("mandatory")


class _LogPortPhyParaBufferControl_Type(Integer32):
    """Custom type logPortPhyParaBufferControl based on Integer32"""
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
        *(("cts", 3),
          ("none", 1),
          ("wangx", 4),
          ("xonXof", 2))
    )


_LogPortPhyParaBufferControl_Type.__name__ = "Integer32"
_LogPortPhyParaBufferControl_Object = MibTableColumn
logPortPhyParaBufferControl = _LogPortPhyParaBufferControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 12),
    _LogPortPhyParaBufferControl_Type()
)
logPortPhyParaBufferControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPortPhyParaBufferControl.setStatus("mandatory")


class _LogPortPhyParaParity_Type(Integer32):
    """Custom type logPortPhyParaParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 5),
          ("odd", 2),
          ("space", 1))
    )


_LogPortPhyParaParity_Type.__name__ = "Integer32"
_LogPortPhyParaParity_Object = MibTableColumn
logPortPhyParaParity = _LogPortPhyParaParity_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 4, 1, 13),
    _LogPortPhyParaParity_Type()
)
logPortPhyParaParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPortPhyParaParity.setStatus("mandatory")


class _CommandPortExtModemNumber_Type(DisplayString):
    """Custom type commandPortExtModemNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CommandPortExtModemNumber_Type.__name__ = "DisplayString"
_CommandPortExtModemNumber_Object = MibScalar
commandPortExtModemNumber = _CommandPortExtModemNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 5),
    _CommandPortExtModemNumber_Type()
)
commandPortExtModemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandPortExtModemNumber.setStatus("mandatory")


class _CommandPortDataActivityTimeout_Type(Integer32):
    """Custom type commandPortDataActivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CommandPortDataActivityTimeout_Type.__name__ = "Integer32"
_CommandPortDataActivityTimeout_Object = MibScalar
commandPortDataActivityTimeout = _CommandPortDataActivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 6),
    _CommandPortDataActivityTimeout_Type()
)
commandPortDataActivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandPortDataActivityTimeout.setStatus("mandatory")
_SyncPortPreConfigTable_Object = MibTable
syncPortPreConfigTable = _SyncPortPreConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 7)
)
if mibBuilder.loadTexts:
    syncPortPreConfigTable.setStatus("mandatory")
_SyncPortPreConfigEntry_Object = MibTableRow
syncPortPreConfigEntry = _SyncPortPreConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 7, 1)
)
syncPortPreConfigEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "syncPortPreConfigCardNumber"),
    (0, "MICOM-NODE-MIB", "syncPortPreConfigChannelNumber"),
)
if mibBuilder.loadTexts:
    syncPortPreConfigEntry.setStatus("mandatory")


class _SyncPortPreConfigCardNumber_Type(Integer32):
    """Custom type syncPortPreConfigCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SyncPortPreConfigCardNumber_Type.__name__ = "Integer32"
_SyncPortPreConfigCardNumber_Object = MibTableColumn
syncPortPreConfigCardNumber = _SyncPortPreConfigCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 7, 1, 1),
    _SyncPortPreConfigCardNumber_Type()
)
syncPortPreConfigCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncPortPreConfigCardNumber.setStatus("mandatory")


class _SyncPortPreConfigChannelNumber_Type(Integer32):
    """Custom type syncPortPreConfigChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SyncPortPreConfigChannelNumber_Type.__name__ = "Integer32"
_SyncPortPreConfigChannelNumber_Object = MibTableColumn
syncPortPreConfigChannelNumber = _SyncPortPreConfigChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 7, 1, 2),
    _SyncPortPreConfigChannelNumber_Type()
)
syncPortPreConfigChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncPortPreConfigChannelNumber.setStatus("mandatory")


class _SyncPortPreConfigProtocol_Type(Integer32):
    """Custom type syncPortPreConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("asciiBisync", 2),
          ("dlcChannel", 1),
          ("ebcdicBisync", 3),
          ("fastPacket", 9),
          ("hpSync", 4),
          ("micomDlc", 7),
          ("micomVoice", 8),
          ("rts", 5),
          ("syncPad", 6),
          ("tdm", 10))
    )


_SyncPortPreConfigProtocol_Type.__name__ = "Integer32"
_SyncPortPreConfigProtocol_Object = MibTableColumn
syncPortPreConfigProtocol = _SyncPortPreConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 3, 7, 1, 3),
    _SyncPortPreConfigProtocol_Type()
)
syncPortPreConfigProtocol.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    syncPortPreConfigProtocol.setStatus("mandatory")
_Channel_ObjectIdentity = ObjectIdentity
channel = _Channel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4)
)
_Sync_channel_ObjectIdentity = ObjectIdentity
sync_channel = _Sync_channel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1)
)
_SyncChPhyParaTable_Object = MibTable
syncChPhyParaTable = _SyncChPhyParaTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    syncChPhyParaTable.setStatus("mandatory")
_SyncChPhyParaEntry_Object = MibTableRow
syncChPhyParaEntry = _SyncChPhyParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1)
)
syncChPhyParaEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "syncChPhyParaCardNumber"),
    (0, "MICOM-NODE-MIB", "syncChPhyParaChannelNumber"),
)
if mibBuilder.loadTexts:
    syncChPhyParaEntry.setStatus("mandatory")


class _SyncChPhyParaCardNumber_Type(Integer32):
    """Custom type syncChPhyParaCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SyncChPhyParaCardNumber_Type.__name__ = "Integer32"
_SyncChPhyParaCardNumber_Object = MibTableColumn
syncChPhyParaCardNumber = _SyncChPhyParaCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 1),
    _SyncChPhyParaCardNumber_Type()
)
syncChPhyParaCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChPhyParaCardNumber.setStatus("mandatory")


class _SyncChPhyParaChannelNumber_Type(Integer32):
    """Custom type syncChPhyParaChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SyncChPhyParaChannelNumber_Type.__name__ = "Integer32"
_SyncChPhyParaChannelNumber_Object = MibTableColumn
syncChPhyParaChannelNumber = _SyncChPhyParaChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 2),
    _SyncChPhyParaChannelNumber_Type()
)
syncChPhyParaChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChPhyParaChannelNumber.setStatus("mandatory")


class _SyncChPhyParaDataRate_Type(Integer32):
    """Custom type syncChPhyParaDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("rate1200", 1),
          ("rate12000", 7),
          ("rate14400", 8),
          ("rate16800", 9),
          ("rate19200", 10),
          ("rate2400", 2),
          ("rate28800", 11),
          ("rate3600", 3),
          ("rate38400", 12),
          ("rate4800", 4),
          ("rate48000", 13),
          ("rate56000", 14),
          ("rate64000", 15),
          ("rate7200", 5),
          ("rate9600", 6))
    )


_SyncChPhyParaDataRate_Type.__name__ = "Integer32"
_SyncChPhyParaDataRate_Object = MibTableColumn
syncChPhyParaDataRate = _SyncChPhyParaDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 3),
    _SyncChPhyParaDataRate_Type()
)
syncChPhyParaDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaDataRate.setStatus("mandatory")


class _SyncChPhyParaCarrierMode_Type(Integer32):
    """Custom type syncChPhyParaCarrierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constant", 2),
          ("variable", 1))
    )


_SyncChPhyParaCarrierMode_Type.__name__ = "Integer32"
_SyncChPhyParaCarrierMode_Object = MibTableColumn
syncChPhyParaCarrierMode = _SyncChPhyParaCarrierMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 4),
    _SyncChPhyParaCarrierMode_Type()
)
syncChPhyParaCarrierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaCarrierMode.setStatus("mandatory")


class _SyncChPhyParaInterfaceType_Type(Integer32):
    """Custom type syncChPhyParaInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("toDCE", 2),
          ("toDTE", 1))
    )


_SyncChPhyParaInterfaceType_Type.__name__ = "Integer32"
_SyncChPhyParaInterfaceType_Object = MibTableColumn
syncChPhyParaInterfaceType = _SyncChPhyParaInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 5),
    _SyncChPhyParaInterfaceType_Type()
)
syncChPhyParaInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaInterfaceType.setStatus("mandatory")


class _SyncChPhyParaIdleFill_Type(Integer32):
    """Custom type syncChPhyParaIdleFill based on Integer32"""
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
        *(("auto", 2),
          ("autoMod128", 3),
          ("flagFill", 1),
          ("markFill", 4))
    )


_SyncChPhyParaIdleFill_Type.__name__ = "Integer32"
_SyncChPhyParaIdleFill_Object = MibTableColumn
syncChPhyParaIdleFill = _SyncChPhyParaIdleFill_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 6),
    _SyncChPhyParaIdleFill_Type()
)
syncChPhyParaIdleFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaIdleFill.setStatus("mandatory")


class _SyncChPhyParaHighSyncChar_Type(OctetString):
    """Custom type syncChPhyParaHighSyncChar based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SyncChPhyParaHighSyncChar_Type.__name__ = "OctetString"
_SyncChPhyParaHighSyncChar_Object = MibTableColumn
syncChPhyParaHighSyncChar = _SyncChPhyParaHighSyncChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 7),
    _SyncChPhyParaHighSyncChar_Type()
)
syncChPhyParaHighSyncChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaHighSyncChar.setStatus("mandatory")


class _SyncChPhyParaLowSyncChar_Type(OctetString):
    """Custom type syncChPhyParaLowSyncChar based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SyncChPhyParaLowSyncChar_Type.__name__ = "OctetString"
_SyncChPhyParaLowSyncChar_Object = MibTableColumn
syncChPhyParaLowSyncChar = _SyncChPhyParaLowSyncChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 8),
    _SyncChPhyParaLowSyncChar_Type()
)
syncChPhyParaLowSyncChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaLowSyncChar.setStatus("mandatory")


class _SyncChPhyParaNumLeadSyncCount_Type(Integer32):
    """Custom type syncChPhyParaNumLeadSyncCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_SyncChPhyParaNumLeadSyncCount_Type.__name__ = "Integer32"
_SyncChPhyParaNumLeadSyncCount_Object = MibTableColumn
syncChPhyParaNumLeadSyncCount = _SyncChPhyParaNumLeadSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 9),
    _SyncChPhyParaNumLeadSyncCount_Type()
)
syncChPhyParaNumLeadSyncCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaNumLeadSyncCount.setStatus("mandatory")


class _SyncChPhyParaMaxTxBlockSize_Type(Integer32):
    """Custom type syncChPhyParaMaxTxBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_SyncChPhyParaMaxTxBlockSize_Type.__name__ = "Integer32"
_SyncChPhyParaMaxTxBlockSize_Object = MibTableColumn
syncChPhyParaMaxTxBlockSize = _SyncChPhyParaMaxTxBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 10),
    _SyncChPhyParaMaxTxBlockSize_Type()
)
syncChPhyParaMaxTxBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaMaxTxBlockSize.setStatus("mandatory")


class _SyncChPhyParaPadChar_Type(OctetString):
    """Custom type syncChPhyParaPadChar based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SyncChPhyParaPadChar_Type.__name__ = "OctetString"
_SyncChPhyParaPadChar_Object = MibTableColumn
syncChPhyParaPadChar = _SyncChPhyParaPadChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 11),
    _SyncChPhyParaPadChar_Type()
)
syncChPhyParaPadChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaPadChar.setStatus("mandatory")


class _SyncChPhyParaNumLeadingPads_Type(Integer32):
    """Custom type syncChPhyParaNumLeadingPads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_SyncChPhyParaNumLeadingPads_Type.__name__ = "Integer32"
_SyncChPhyParaNumLeadingPads_Object = MibTableColumn
syncChPhyParaNumLeadingPads = _SyncChPhyParaNumLeadingPads_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 12),
    _SyncChPhyParaNumLeadingPads_Type()
)
syncChPhyParaNumLeadingPads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaNumLeadingPads.setStatus("mandatory")


class _SyncChPhyParaNumTrailingPads_Type(Integer32):
    """Custom type syncChPhyParaNumTrailingPads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_SyncChPhyParaNumTrailingPads_Type.__name__ = "Integer32"
_SyncChPhyParaNumTrailingPads_Object = MibTableColumn
syncChPhyParaNumTrailingPads = _SyncChPhyParaNumTrailingPads_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 13),
    _SyncChPhyParaNumTrailingPads_Type()
)
syncChPhyParaNumTrailingPads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaNumTrailingPads.setStatus("mandatory")


class _SyncChPhyParaClockFlowControl_Type(Integer32):
    """Custom type syncChPhyParaClockFlowControl based on Integer32"""
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


_SyncChPhyParaClockFlowControl_Type.__name__ = "Integer32"
_SyncChPhyParaClockFlowControl_Object = MibTableColumn
syncChPhyParaClockFlowControl = _SyncChPhyParaClockFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 14),
    _SyncChPhyParaClockFlowControl_Type()
)
syncChPhyParaClockFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaClockFlowControl.setStatus("mandatory")


class _SyncChPhyParaEncoding_Type(Integer32):
    """Custom type syncChPhyParaEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("nrzi", 2))
    )


_SyncChPhyParaEncoding_Type.__name__ = "Integer32"
_SyncChPhyParaEncoding_Object = MibTableColumn
syncChPhyParaEncoding = _SyncChPhyParaEncoding_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 15),
    _SyncChPhyParaEncoding_Type()
)
syncChPhyParaEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaEncoding.setStatus("mandatory")


class _SyncChPhyParaChTxClocking_Type(Integer32):
    """Custom type syncChPhyParaChTxClocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_SyncChPhyParaChTxClocking_Type.__name__ = "Integer32"
_SyncChPhyParaChTxClocking_Object = MibTableColumn
syncChPhyParaChTxClocking = _SyncChPhyParaChTxClocking_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 16),
    _SyncChPhyParaChTxClocking_Type()
)
syncChPhyParaChTxClocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaChTxClocking.setStatus("mandatory")


class _SyncChPhyParaChRxClocking_Type(Integer32):
    """Custom type syncChPhyParaChRxClocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_SyncChPhyParaChRxClocking_Type.__name__ = "Integer32"
_SyncChPhyParaChRxClocking_Object = MibTableColumn
syncChPhyParaChRxClocking = _SyncChPhyParaChRxClocking_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 17),
    _SyncChPhyParaChRxClocking_Type()
)
syncChPhyParaChRxClocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaChRxClocking.setStatus("mandatory")


class _SyncChPhyParaPriority_Type(Integer32):
    """Custom type syncChPhyParaPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_SyncChPhyParaPriority_Type.__name__ = "Integer32"
_SyncChPhyParaPriority_Object = MibTableColumn
syncChPhyParaPriority = _SyncChPhyParaPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 18),
    _SyncChPhyParaPriority_Type()
)
syncChPhyParaPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaPriority.setStatus("mandatory")


class _SyncChPhyParaDSRControl_Type(Integer32):
    """Custom type syncChPhyParaDSRControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fornedOn", 2),
          ("localDTR", 3),
          ("normal", 1))
    )


_SyncChPhyParaDSRControl_Type.__name__ = "Integer32"
_SyncChPhyParaDSRControl_Object = MibTableColumn
syncChPhyParaDSRControl = _SyncChPhyParaDSRControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 19),
    _SyncChPhyParaDSRControl_Type()
)
syncChPhyParaDSRControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaDSRControl.setStatus("mandatory")


class _SyncChPhyParaBufferControl_Type(Integer32):
    """Custom type syncChPhyParaBufferControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cts", 2),
          ("none", 1))
    )


_SyncChPhyParaBufferControl_Type.__name__ = "Integer32"
_SyncChPhyParaBufferControl_Object = MibTableColumn
syncChPhyParaBufferControl = _SyncChPhyParaBufferControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 20),
    _SyncChPhyParaBufferControl_Type()
)
syncChPhyParaBufferControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaBufferControl.setStatus("mandatory")


class _SyncChPhyParaMaxRxBlockSize_Type(Integer32):
    """Custom type syncChPhyParaMaxRxBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_SyncChPhyParaMaxRxBlockSize_Type.__name__ = "Integer32"
_SyncChPhyParaMaxRxBlockSize_Object = MibTableColumn
syncChPhyParaMaxRxBlockSize = _SyncChPhyParaMaxRxBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 21),
    _SyncChPhyParaMaxRxBlockSize_Type()
)
syncChPhyParaMaxRxBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaMaxRxBlockSize.setStatus("mandatory")


class _SyncChPhyParaProtocol_Type(Integer32):
    """Custom type syncChPhyParaProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("asciiBisync", 2),
          ("dlc", 1),
          ("ebcdicBisync", 3),
          ("fastPacket", 9),
          ("hpSync", 4),
          ("micomDlc", 7),
          ("micomVoice", 8),
          ("rtsCts", 5),
          ("syncPad", 6),
          ("tdm", 10))
    )


_SyncChPhyParaProtocol_Type.__name__ = "Integer32"
_SyncChPhyParaProtocol_Object = MibTableColumn
syncChPhyParaProtocol = _SyncChPhyParaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 22),
    _SyncChPhyParaProtocol_Type()
)
syncChPhyParaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChPhyParaProtocol.setStatus("mandatory")
_SyncChPhyParaClaimedBandwidth_Type = Integer32
_SyncChPhyParaClaimedBandwidth_Object = MibTableColumn
syncChPhyParaClaimedBandwidth = _SyncChPhyParaClaimedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 23),
    _SyncChPhyParaClaimedBandwidth_Type()
)
syncChPhyParaClaimedBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaClaimedBandwidth.setStatus("mandatory")


class _SyncChPhyParaDLCTransitRate_Type(Integer32):
    """Custom type syncChPhyParaDLCTransitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("channelRate", 1),
          ("rate1200", 2),
          ("rate12000", 8),
          ("rate14400", 9),
          ("rate16800", 10),
          ("rate19200", 11),
          ("rate2400", 3),
          ("rate28800", 12),
          ("rate3600", 4),
          ("rate38400", 13),
          ("rate4800", 5),
          ("rate48000", 14),
          ("rate56000", 15),
          ("rate64000", 16),
          ("rate7200", 6),
          ("rate9600", 7))
    )


_SyncChPhyParaDLCTransitRate_Type.__name__ = "Integer32"
_SyncChPhyParaDLCTransitRate_Object = MibTableColumn
syncChPhyParaDLCTransitRate = _SyncChPhyParaDLCTransitRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 1, 1, 1, 24),
    _SyncChPhyParaDLCTransitRate_Type()
)
syncChPhyParaDLCTransitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncChPhyParaDLCTransitRate.setStatus("mandatory")
_Async_channel_ObjectIdentity = ObjectIdentity
async_channel = _Async_channel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2)
)
_AsyncChPhyParaTable_Object = MibTable
asyncChPhyParaTable = _AsyncChPhyParaTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    asyncChPhyParaTable.setStatus("mandatory")
_AsyncChPhyParaEntry_Object = MibTableRow
asyncChPhyParaEntry = _AsyncChPhyParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1)
)
asyncChPhyParaEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "asyncChPhyParaCardNumber"),
    (0, "MICOM-NODE-MIB", "asyncChPhyParaChannelNumber"),
)
if mibBuilder.loadTexts:
    asyncChPhyParaEntry.setStatus("mandatory")


class _AsyncChPhyParaCardNumber_Type(Integer32):
    """Custom type asyncChPhyParaCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AsyncChPhyParaCardNumber_Type.__name__ = "Integer32"
_AsyncChPhyParaCardNumber_Object = MibTableColumn
asyncChPhyParaCardNumber = _AsyncChPhyParaCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 1),
    _AsyncChPhyParaCardNumber_Type()
)
asyncChPhyParaCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChPhyParaCardNumber.setStatus("mandatory")


class _AsyncChPhyParaChannelNumber_Type(Integer32):
    """Custom type asyncChPhyParaChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AsyncChPhyParaChannelNumber_Type.__name__ = "Integer32"
_AsyncChPhyParaChannelNumber_Object = MibTableColumn
asyncChPhyParaChannelNumber = _AsyncChPhyParaChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 2),
    _AsyncChPhyParaChannelNumber_Type()
)
asyncChPhyParaChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChPhyParaChannelNumber.setStatus("mandatory")


class _AsyncChPhyParaStopBits_Type(Integer32):
    """Custom type asyncChPhyParaStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneBit", 1),
          ("onePointFiveBits", 2),
          ("twoBits", 3))
    )


_AsyncChPhyParaStopBits_Type.__name__ = "Integer32"
_AsyncChPhyParaStopBits_Object = MibTableColumn
asyncChPhyParaStopBits = _AsyncChPhyParaStopBits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 3),
    _AsyncChPhyParaStopBits_Type()
)
asyncChPhyParaStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaStopBits.setStatus("mandatory")


class _AsyncChPhyParaCodeLevel_Type(Integer32):
    """Custom type asyncChPhyParaCodeLevel based on Integer32"""
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
        *(("eightBits", 4),
          ("fiveBits", 1),
          ("nineBits", 5),
          ("sevenBits", 3),
          ("sixBits", 2))
    )


_AsyncChPhyParaCodeLevel_Type.__name__ = "Integer32"
_AsyncChPhyParaCodeLevel_Object = MibTableColumn
asyncChPhyParaCodeLevel = _AsyncChPhyParaCodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 4),
    _AsyncChPhyParaCodeLevel_Type()
)
asyncChPhyParaCodeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaCodeLevel.setStatus("mandatory")


class _AsyncChPhyParaDataRate_Type(Integer32):
    """Custom type asyncChPhyParaDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("abr", 1),
          ("rate110", 4),
          ("rate1200", 11),
          ("rate134dot5", 5),
          ("rate14400", 18),
          ("rate150", 6),
          ("rate1800", 12),
          ("rate19200", 19),
          ("rate200", 7),
          ("rate225", 8),
          ("rate2400", 13),
          ("rate28800", 20),
          ("rate300", 9),
          ("rate3600", 14),
          ("rate38400", 21),
          ("rate4800", 15),
          ("rate50", 2),
          ("rate600", 10),
          ("rate7200", 16),
          ("rate75", 3),
          ("rate9600", 17))
    )


_AsyncChPhyParaDataRate_Type.__name__ = "Integer32"
_AsyncChPhyParaDataRate_Object = MibTableColumn
asyncChPhyParaDataRate = _AsyncChPhyParaDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 5),
    _AsyncChPhyParaDataRate_Type()
)
asyncChPhyParaDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaDataRate.setStatus("mandatory")


class _AsyncChPhyParaEcho_Type(Integer32):
    """Custom type asyncChPhyParaEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsyncChPhyParaEcho_Type.__name__ = "Integer32"
_AsyncChPhyParaEcho_Object = MibTableColumn
asyncChPhyParaEcho = _AsyncChPhyParaEcho_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 6),
    _AsyncChPhyParaEcho_Type()
)
asyncChPhyParaEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaEcho.setStatus("mandatory")


class _AsyncChPhyParaHPXMode_Type(Integer32):
    """Custom type asyncChPhyParaHPXMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsyncChPhyParaHPXMode_Type.__name__ = "Integer32"
_AsyncChPhyParaHPXMode_Object = MibTableColumn
asyncChPhyParaHPXMode = _AsyncChPhyParaHPXMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 7),
    _AsyncChPhyParaHPXMode_Type()
)
asyncChPhyParaHPXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaHPXMode.setStatus("mandatory")


class _AsyncChPhyParaConnectTo_Type(Integer32):
    """Custom type asyncChPhyParaConnectTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("terminal", 2))
    )


_AsyncChPhyParaConnectTo_Type.__name__ = "Integer32"
_AsyncChPhyParaConnectTo_Object = MibTableColumn
asyncChPhyParaConnectTo = _AsyncChPhyParaConnectTo_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 8),
    _AsyncChPhyParaConnectTo_Type()
)
asyncChPhyParaConnectTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaConnectTo.setStatus("mandatory")


class _AsyncChPhyParaRemCTSControl_Type(Integer32):
    """Custom type asyncChPhyParaRemCTSControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcedOn", 1),
          ("normal", 2))
    )


_AsyncChPhyParaRemCTSControl_Type.__name__ = "Integer32"
_AsyncChPhyParaRemCTSControl_Object = MibTableColumn
asyncChPhyParaRemCTSControl = _AsyncChPhyParaRemCTSControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 9),
    _AsyncChPhyParaRemCTSControl_Type()
)
asyncChPhyParaRemCTSControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaRemCTSControl.setStatus("mandatory")


class _AsyncChPhyParaCRDelay_Type(Integer32):
    """Custom type asyncChPhyParaCRDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AsyncChPhyParaCRDelay_Type.__name__ = "Integer32"
_AsyncChPhyParaCRDelay_Object = MibTableColumn
asyncChPhyParaCRDelay = _AsyncChPhyParaCRDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 10),
    _AsyncChPhyParaCRDelay_Type()
)
asyncChPhyParaCRDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaCRDelay.setStatus("mandatory")


class _AsyncChPhyParaLFDelay_Type(Integer32):
    """Custom type asyncChPhyParaLFDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AsyncChPhyParaLFDelay_Type.__name__ = "Integer32"
_AsyncChPhyParaLFDelay_Object = MibTableColumn
asyncChPhyParaLFDelay = _AsyncChPhyParaLFDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 11),
    _AsyncChPhyParaLFDelay_Type()
)
asyncChPhyParaLFDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaLFDelay.setStatus("mandatory")


class _AsyncChPhyParaFFDelay_Type(Integer32):
    """Custom type asyncChPhyParaFFDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AsyncChPhyParaFFDelay_Type.__name__ = "Integer32"
_AsyncChPhyParaFFDelay_Object = MibTableColumn
asyncChPhyParaFFDelay = _AsyncChPhyParaFFDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 12),
    _AsyncChPhyParaFFDelay_Type()
)
asyncChPhyParaFFDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaFFDelay.setStatus("mandatory")


class _AsyncChPhyParaXONChar_Type(Integer32):
    """Custom type asyncChPhyParaXONChar based on Integer32"""
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
        *(("dc1", 1),
          ("dc2", 2),
          ("dc3", 3),
          ("dc4", 4))
    )


_AsyncChPhyParaXONChar_Type.__name__ = "Integer32"
_AsyncChPhyParaXONChar_Object = MibTableColumn
asyncChPhyParaXONChar = _AsyncChPhyParaXONChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 13),
    _AsyncChPhyParaXONChar_Type()
)
asyncChPhyParaXONChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaXONChar.setStatus("mandatory")


class _AsyncChPhyParaXOFFChar_Type(Integer32):
    """Custom type asyncChPhyParaXOFFChar based on Integer32"""
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
        *(("dc1", 1),
          ("dc2", 2),
          ("dc3", 3),
          ("dc4", 4))
    )


_AsyncChPhyParaXOFFChar_Type.__name__ = "Integer32"
_AsyncChPhyParaXOFFChar_Object = MibTableColumn
asyncChPhyParaXOFFChar = _AsyncChPhyParaXOFFChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 14),
    _AsyncChPhyParaXOFFChar_Type()
)
asyncChPhyParaXOFFChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaXOFFChar.setStatus("mandatory")


class _AsyncChPhyParaCmdFacilityAccess_Type(Integer32):
    """Custom type asyncChPhyParaCmdFacilityAccess based on Integer32"""
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


_AsyncChPhyParaCmdFacilityAccess_Type.__name__ = "Integer32"
_AsyncChPhyParaCmdFacilityAccess_Object = MibTableColumn
asyncChPhyParaCmdFacilityAccess = _AsyncChPhyParaCmdFacilityAccess_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 15),
    _AsyncChPhyParaCmdFacilityAccess_Type()
)
asyncChPhyParaCmdFacilityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaCmdFacilityAccess.setStatus("mandatory")


class _AsyncChPhyParaCmdModeEntry_Type(Integer32):
    """Custom type asyncChPhyParaCmdModeEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctlXbreak", 2),
          ("ctlXctlY", 1))
    )


_AsyncChPhyParaCmdModeEntry_Type.__name__ = "Integer32"
_AsyncChPhyParaCmdModeEntry_Object = MibTableColumn
asyncChPhyParaCmdModeEntry = _AsyncChPhyParaCmdModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 16),
    _AsyncChPhyParaCmdModeEntry_Type()
)
asyncChPhyParaCmdModeEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaCmdModeEntry.setStatus("mandatory")


class _AsyncChPhyParaLocChannelConfig_Type(Integer32):
    """Custom type asyncChPhyParaLocChannelConfig based on Integer32"""
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


_AsyncChPhyParaLocChannelConfig_Type.__name__ = "Integer32"
_AsyncChPhyParaLocChannelConfig_Object = MibTableColumn
asyncChPhyParaLocChannelConfig = _AsyncChPhyParaLocChannelConfig_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 17),
    _AsyncChPhyParaLocChannelConfig_Type()
)
asyncChPhyParaLocChannelConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaLocChannelConfig.setStatus("mandatory")


class _AsyncChPhyParaCmdModeAccess_Type(Integer32):
    """Custom type asyncChPhyParaCmdModeAccess based on Integer32"""
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


_AsyncChPhyParaCmdModeAccess_Type.__name__ = "Integer32"
_AsyncChPhyParaCmdModeAccess_Object = MibTableColumn
asyncChPhyParaCmdModeAccess = _AsyncChPhyParaCmdModeAccess_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 18),
    _AsyncChPhyParaCmdModeAccess_Type()
)
asyncChPhyParaCmdModeAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaCmdModeAccess.setStatus("mandatory")


class _AsyncChPhyParaTandemSupport_Type(Integer32):
    """Custom type asyncChPhyParaTandemSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsyncChPhyParaTandemSupport_Type.__name__ = "Integer32"
_AsyncChPhyParaTandemSupport_Object = MibTableColumn
asyncChPhyParaTandemSupport = _AsyncChPhyParaTandemSupport_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 19),
    _AsyncChPhyParaTandemSupport_Type()
)
asyncChPhyParaTandemSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaTandemSupport.setStatus("mandatory")


class _AsyncChPhyParaSmoothScroll_Type(Integer32):
    """Custom type asyncChPhyParaSmoothScroll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsyncChPhyParaSmoothScroll_Type.__name__ = "Integer32"
_AsyncChPhyParaSmoothScroll_Object = MibTableColumn
asyncChPhyParaSmoothScroll = _AsyncChPhyParaSmoothScroll_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 20),
    _AsyncChPhyParaSmoothScroll_Type()
)
asyncChPhyParaSmoothScroll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaSmoothScroll.setStatus("mandatory")


class _AsyncChPhyParaFlowControl_Type(Integer32):
    """Custom type asyncChPhyParaFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dataGeneral", 7),
          ("dtr", 3),
          ("none", 1),
          ("rts", 6),
          ("wangx", 5),
          ("xonXof", 2),
          ("xonXofDtr", 4))
    )


_AsyncChPhyParaFlowControl_Type.__name__ = "Integer32"
_AsyncChPhyParaFlowControl_Object = MibTableColumn
asyncChPhyParaFlowControl = _AsyncChPhyParaFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 21),
    _AsyncChPhyParaFlowControl_Type()
)
asyncChPhyParaFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaFlowControl.setStatus("mandatory")


class _AsyncChPhyParaBufferControl_Type(Integer32):
    """Custom type asyncChPhyParaBufferControl based on Integer32"""
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
        *(("cts", 3),
          ("none", 1),
          ("wangx", 4),
          ("xonXof", 2))
    )


_AsyncChPhyParaBufferControl_Type.__name__ = "Integer32"
_AsyncChPhyParaBufferControl_Object = MibTableColumn
asyncChPhyParaBufferControl = _AsyncChPhyParaBufferControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 22),
    _AsyncChPhyParaBufferControl_Type()
)
asyncChPhyParaBufferControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaBufferControl.setStatus("mandatory")


class _AsyncChPhyParaFlowControlStrip_Type(Integer32):
    """Custom type asyncChPhyParaFlowControlStrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 2),
          ("strip", 1))
    )


_AsyncChPhyParaFlowControlStrip_Type.__name__ = "Integer32"
_AsyncChPhyParaFlowControlStrip_Object = MibTableColumn
asyncChPhyParaFlowControlStrip = _AsyncChPhyParaFlowControlStrip_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 23),
    _AsyncChPhyParaFlowControlStrip_Type()
)
asyncChPhyParaFlowControlStrip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaFlowControlStrip.setStatus("mandatory")


class _AsyncChPhyParaSyncLossDisconnect_Type(Integer32):
    """Custom type asyncChPhyParaSyncLossDisconnect based on Integer32"""
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


_AsyncChPhyParaSyncLossDisconnect_Type.__name__ = "Integer32"
_AsyncChPhyParaSyncLossDisconnect_Object = MibTableColumn
asyncChPhyParaSyncLossDisconnect = _AsyncChPhyParaSyncLossDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 24),
    _AsyncChPhyParaSyncLossDisconnect_Type()
)
asyncChPhyParaSyncLossDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaSyncLossDisconnect.setStatus("mandatory")


class _AsyncChPhyParaEIAControls_Type(Integer32):
    """Custom type asyncChPhyParaEIAControls based on Integer32"""
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


_AsyncChPhyParaEIAControls_Type.__name__ = "Integer32"
_AsyncChPhyParaEIAControls_Object = MibTableColumn
asyncChPhyParaEIAControls = _AsyncChPhyParaEIAControls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 25),
    _AsyncChPhyParaEIAControls_Type()
)
asyncChPhyParaEIAControls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaEIAControls.setStatus("mandatory")


class _AsyncChPhyParaPriority_Type(Integer32):
    """Custom type asyncChPhyParaPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_AsyncChPhyParaPriority_Type.__name__ = "Integer32"
_AsyncChPhyParaPriority_Object = MibTableColumn
asyncChPhyParaPriority = _AsyncChPhyParaPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 26),
    _AsyncChPhyParaPriority_Type()
)
asyncChPhyParaPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaPriority.setStatus("mandatory")


class _AsyncChPhyParaParity_Type(Integer32):
    """Custom type asyncChPhyParaParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 5),
          ("odd", 2),
          ("space", 1))
    )


_AsyncChPhyParaParity_Type.__name__ = "Integer32"
_AsyncChPhyParaParity_Object = MibTableColumn
asyncChPhyParaParity = _AsyncChPhyParaParity_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 27),
    _AsyncChPhyParaParity_Type()
)
asyncChPhyParaParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaParity.setStatus("mandatory")


class _AsyncChPhyParaCompression_Type(Integer32):
    """Custom type asyncChPhyParaCompression based on Integer32"""
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


_AsyncChPhyParaCompression_Type.__name__ = "Integer32"
_AsyncChPhyParaCompression_Object = MibTableColumn
asyncChPhyParaCompression = _AsyncChPhyParaCompression_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 1, 1, 28),
    _AsyncChPhyParaCompression_Type()
)
asyncChPhyParaCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChPhyParaCompression.setStatus("mandatory")
_AsyncChSwParaTable_Object = MibTable
asyncChSwParaTable = _AsyncChSwParaTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    asyncChSwParaTable.setStatus("mandatory")
_AsyncChSwParaEntry_Object = MibTableRow
asyncChSwParaEntry = _AsyncChSwParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2, 1)
)
asyncChSwParaEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "asyncChSwParaCardNumber"),
    (0, "MICOM-NODE-MIB", "asyncChSwParaChannelNumber"),
)
if mibBuilder.loadTexts:
    asyncChSwParaEntry.setStatus("mandatory")


class _AsyncChSwParaCardNumber_Type(Integer32):
    """Custom type asyncChSwParaCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AsyncChSwParaCardNumber_Type.__name__ = "Integer32"
_AsyncChSwParaCardNumber_Object = MibTableColumn
asyncChSwParaCardNumber = _AsyncChSwParaCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2, 1, 1),
    _AsyncChSwParaCardNumber_Type()
)
asyncChSwParaCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChSwParaCardNumber.setStatus("mandatory")


class _AsyncChSwParaChannelNumber_Type(Integer32):
    """Custom type asyncChSwParaChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AsyncChSwParaChannelNumber_Type.__name__ = "Integer32"
_AsyncChSwParaChannelNumber_Object = MibTableColumn
asyncChSwParaChannelNumber = _AsyncChSwParaChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2, 1, 2),
    _AsyncChSwParaChannelNumber_Type()
)
asyncChSwParaChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChSwParaChannelNumber.setStatus("mandatory")


class _AsyncChSwParaDestinationClass_Type(DisplayString):
    """Custom type asyncChSwParaDestinationClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AsyncChSwParaDestinationClass_Type.__name__ = "DisplayString"
_AsyncChSwParaDestinationClass_Object = MibTableColumn
asyncChSwParaDestinationClass = _AsyncChSwParaDestinationClass_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2, 1, 3),
    _AsyncChSwParaDestinationClass_Type()
)
asyncChSwParaDestinationClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChSwParaDestinationClass.setStatus("mandatory")


class _AsyncChSwParaConnectProtocol_Type(Integer32):
    """Custom type asyncChSwParaConnectProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoAnswer", 3),
          ("dedicated", 1),
          ("dtr", 2))
    )


_AsyncChSwParaConnectProtocol_Type.__name__ = "Integer32"
_AsyncChSwParaConnectProtocol_Object = MibTableColumn
asyncChSwParaConnectProtocol = _AsyncChSwParaConnectProtocol_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2, 1, 4),
    _AsyncChSwParaConnectProtocol_Type()
)
asyncChSwParaConnectProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChSwParaConnectProtocol.setStatus("mandatory")


class _AsyncChSwParaRcvInhibit_Type(Integer32):
    """Custom type asyncChSwParaRcvInhibit based on Integer32"""
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


_AsyncChSwParaRcvInhibit_Type.__name__ = "Integer32"
_AsyncChSwParaRcvInhibit_Object = MibTableColumn
asyncChSwParaRcvInhibit = _AsyncChSwParaRcvInhibit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2, 1, 5),
    _AsyncChSwParaRcvInhibit_Type()
)
asyncChSwParaRcvInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChSwParaRcvInhibit.setStatus("mandatory")


class _AsyncChSwParaResourceClassNumber_Type(Integer32):
    """Custom type asyncChSwParaResourceClassNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AsyncChSwParaResourceClassNumber_Type.__name__ = "Integer32"
_AsyncChSwParaResourceClassNumber_Object = MibTableColumn
asyncChSwParaResourceClassNumber = _AsyncChSwParaResourceClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2, 1, 6),
    _AsyncChSwParaResourceClassNumber_Type()
)
asyncChSwParaResourceClassNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChSwParaResourceClassNumber.setStatus("mandatory")


class _AsyncChSwParaCallInhibit_Type(Integer32):
    """Custom type asyncChSwParaCallInhibit based on Integer32"""
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


_AsyncChSwParaCallInhibit_Type.__name__ = "Integer32"
_AsyncChSwParaCallInhibit_Object = MibTableColumn
asyncChSwParaCallInhibit = _AsyncChSwParaCallInhibit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2, 1, 7),
    _AsyncChSwParaCallInhibit_Type()
)
asyncChSwParaCallInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChSwParaCallInhibit.setStatus("mandatory")


class _AsyncChSwParaUnbalanceRates_Type(Integer32):
    """Custom type asyncChSwParaUnbalanceRates based on Integer32"""
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


_AsyncChSwParaUnbalanceRates_Type.__name__ = "Integer32"
_AsyncChSwParaUnbalanceRates_Object = MibTableColumn
asyncChSwParaUnbalanceRates = _AsyncChSwParaUnbalanceRates_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2, 1, 8),
    _AsyncChSwParaUnbalanceRates_Type()
)
asyncChSwParaUnbalanceRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChSwParaUnbalanceRates.setStatus("mandatory")


class _AsyncChSwParaCharacterSet_Type(Integer32):
    """Custom type asyncChSwParaCharacterSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("nonAscii", 2))
    )


_AsyncChSwParaCharacterSet_Type.__name__ = "Integer32"
_AsyncChSwParaCharacterSet_Object = MibTableColumn
asyncChSwParaCharacterSet = _AsyncChSwParaCharacterSet_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2, 1, 9),
    _AsyncChSwParaCharacterSet_Type()
)
asyncChSwParaCharacterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChSwParaCharacterSet.setStatus("mandatory")


class _AsyncChSwParaMatrixSwitching_Type(Integer32):
    """Custom type asyncChSwParaMatrixSwitching based on Integer32"""
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


_AsyncChSwParaMatrixSwitching_Type.__name__ = "Integer32"
_AsyncChSwParaMatrixSwitching_Object = MibTableColumn
asyncChSwParaMatrixSwitching = _AsyncChSwParaMatrixSwitching_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2, 1, 10),
    _AsyncChSwParaMatrixSwitching_Type()
)
asyncChSwParaMatrixSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncChSwParaMatrixSwitching.setStatus("mandatory")


class _AsyncChSwParaChannelPassword_Type(DisplayString):
    """Custom type asyncChSwParaChannelPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AsyncChSwParaChannelPassword_Type.__name__ = "DisplayString"
_AsyncChSwParaChannelPassword_Object = MibTableColumn
asyncChSwParaChannelPassword = _AsyncChSwParaChannelPassword_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 2, 2, 1, 11),
    _AsyncChSwParaChannelPassword_Type()
)
asyncChSwParaChannelPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    asyncChSwParaChannelPassword.setStatus("mandatory")
_Voice_fax_channel_ObjectIdentity = ObjectIdentity
voice_fax_channel = _Voice_fax_channel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3)
)
_VoiceFaxChPhyParaTable_Object = MibTable
voiceFaxChPhyParaTable = _VoiceFaxChPhyParaTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    voiceFaxChPhyParaTable.setStatus("mandatory")
_VoiceFaxChPhyParaEntry_Object = MibTableRow
voiceFaxChPhyParaEntry = _VoiceFaxChPhyParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1)
)
voiceFaxChPhyParaEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "voiceFaxChPhyParaCardNumber"),
    (0, "MICOM-NODE-MIB", "voiceFaxChPhyParaChannelNumber"),
)
if mibBuilder.loadTexts:
    voiceFaxChPhyParaEntry.setStatus("mandatory")


class _VoiceFaxChPhyParaCardNumber_Type(Integer32):
    """Custom type voiceFaxChPhyParaCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_VoiceFaxChPhyParaCardNumber_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaCardNumber_Object = MibTableColumn
voiceFaxChPhyParaCardNumber = _VoiceFaxChPhyParaCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 1),
    _VoiceFaxChPhyParaCardNumber_Type()
)
voiceFaxChPhyParaCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaCardNumber.setStatus("mandatory")


class _VoiceFaxChPhyParaChannelNumber_Type(Integer32):
    """Custom type voiceFaxChPhyParaChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_VoiceFaxChPhyParaChannelNumber_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaChannelNumber_Object = MibTableColumn
voiceFaxChPhyParaChannelNumber = _VoiceFaxChPhyParaChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 2),
    _VoiceFaxChPhyParaChannelNumber_Type()
)
voiceFaxChPhyParaChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaChannelNumber.setStatus("mandatory")


class _VoiceFaxChPhyParaWireOperation_Type(Integer32):
    """Custom type voiceFaxChPhyParaWireOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourWire", 1),
          ("twoWire", 2))
    )


_VoiceFaxChPhyParaWireOperation_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaWireOperation_Object = MibTableColumn
voiceFaxChPhyParaWireOperation = _VoiceFaxChPhyParaWireOperation_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 3),
    _VoiceFaxChPhyParaWireOperation_Type()
)
voiceFaxChPhyParaWireOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaWireOperation.setStatus("mandatory")


class _VoiceFaxChPhyParaViewSignallingType_Type(Integer32):
    """Custom type voiceFaxChPhyParaViewSignallingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("emPulseVDc", 16),
          ("emPulsedDc", 11),
          ("emPulsedIDc", 12),
          ("emPulsedIIDc", 13),
          ("emPulsedIIIDc", 14),
          ("emPulsedIVDc", 15),
          ("emTypeI2280", 6),
          ("emTypeII2280", 7),
          ("emTypeIII2280", 8),
          ("emTypeIIIdc", 3),
          ("emTypeIIdc", 2),
          ("emTypeIV2280", 9),
          ("emTypeIVdc", 4),
          ("emTypeIdc", 1),
          ("emTypeV2280", 10),
          ("emTypeVdc", 5),
          ("faxIterrupted", 29),
          ("fxo", 27),
          ("fxsFaxInterrupt1by2", 26),
          ("fxsFaxInterrupt2by4", 25),
          ("fxsFaxRepeated", 24),
          ("fxsInterrupt1by2", 23),
          ("fxsInterrupt2by4", 22),
          ("fxsIterrupted", 28),
          ("fxsRepeated", 21),
          ("ktsInterrupt1by2", 19),
          ("ktsInterrupt2by4", 18),
          ("ktsRepeated", 17),
          ("opx", 20))
    )


_VoiceFaxChPhyParaViewSignallingType_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaViewSignallingType_Object = MibTableColumn
voiceFaxChPhyParaViewSignallingType = _VoiceFaxChPhyParaViewSignallingType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 4),
    _VoiceFaxChPhyParaViewSignallingType_Type()
)
voiceFaxChPhyParaViewSignallingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaViewSignallingType.setStatus("mandatory")


class _VoiceFaxChPhyParaBergStrapType_Type(Integer32):
    """Custom type voiceFaxChPhyParaBergStrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("em", 2),
          ("enhancedEm", 5),
          ("enhancedFxo", 6),
          ("enhancedFxs", 4),
          ("groundstartFxo", 11),
          ("groundstartFxs", 10),
          ("kts", 1),
          ("opx", 3),
          ("standardEm", 8),
          ("standardFxo", 9),
          ("standardFxs", 7),
          ("threePort", 12))
    )


_VoiceFaxChPhyParaBergStrapType_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaBergStrapType_Object = MibTableColumn
voiceFaxChPhyParaBergStrapType = _VoiceFaxChPhyParaBergStrapType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 5),
    _VoiceFaxChPhyParaBergStrapType_Type()
)
voiceFaxChPhyParaBergStrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaBergStrapType.setStatus("mandatory")
_VoiceFaxChPhyParaSuppression_Type = Integer32
_VoiceFaxChPhyParaSuppression_Object = MibTableColumn
voiceFaxChPhyParaSuppression = _VoiceFaxChPhyParaSuppression_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 6),
    _VoiceFaxChPhyParaSuppression_Type()
)
voiceFaxChPhyParaSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaSuppression.setStatus("mandatory")


class _VoiceFaxChPhyParaCfgSignallingType_Type(Integer32):
    """Custom type voiceFaxChPhyParaCfgSignallingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("em2280Tone", 2),
          ("emDc", 1),
          ("emPulsedDc", 4),
          ("emWink", 3),
          ("interrupt1by2", 7),
          ("interruptOR2by4", 6),
          ("repeated", 5))
    )


_VoiceFaxChPhyParaCfgSignallingType_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaCfgSignallingType_Object = MibTableColumn
voiceFaxChPhyParaCfgSignallingType = _VoiceFaxChPhyParaCfgSignallingType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 7),
    _VoiceFaxChPhyParaCfgSignallingType_Type()
)
voiceFaxChPhyParaCfgSignallingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaCfgSignallingType.setStatus("mandatory")


class _VoiceFaxChPhyParaOPXNumberOfRings_Type(Integer32):
    """Custom type voiceFaxChPhyParaOPXNumberOfRings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_VoiceFaxChPhyParaOPXNumberOfRings_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaOPXNumberOfRings_Object = MibTableColumn
voiceFaxChPhyParaOPXNumberOfRings = _VoiceFaxChPhyParaOPXNumberOfRings_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 8),
    _VoiceFaxChPhyParaOPXNumberOfRings_Type()
)
voiceFaxChPhyParaOPXNumberOfRings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaOPXNumberOfRings.setStatus("mandatory")


class _VoiceFaxChPhyParaFXOSupervisorDisc_Type(Integer32):
    """Custom type voiceFaxChPhyParaFXOSupervisorDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerInterrupt", 1),
          ("tone", 2))
    )


_VoiceFaxChPhyParaFXOSupervisorDisc_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaFXOSupervisorDisc_Object = MibTableColumn
voiceFaxChPhyParaFXOSupervisorDisc = _VoiceFaxChPhyParaFXOSupervisorDisc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 9),
    _VoiceFaxChPhyParaFXOSupervisorDisc_Type()
)
voiceFaxChPhyParaFXOSupervisorDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaFXOSupervisorDisc.setStatus("mandatory")


class _VoiceFaxChPhyParaRingFrequency_Type(Integer32):
    """Custom type voiceFaxChPhyParaRingFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freq25Hz", 1),
          ("freq50Hz", 2))
    )


_VoiceFaxChPhyParaRingFrequency_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaRingFrequency_Object = MibTableColumn
voiceFaxChPhyParaRingFrequency = _VoiceFaxChPhyParaRingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 10),
    _VoiceFaxChPhyParaRingFrequency_Type()
)
voiceFaxChPhyParaRingFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaRingFrequency.setStatus("mandatory")
_VoiceFaxChPhyParaJitter_Type = Integer32
_VoiceFaxChPhyParaJitter_Object = MibTableColumn
voiceFaxChPhyParaJitter = _VoiceFaxChPhyParaJitter_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 11),
    _VoiceFaxChPhyParaJitter_Type()
)
voiceFaxChPhyParaJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaJitter.setStatus("mandatory")


class _VoiceFaxChPhyParaDTMFRegeneration_Type(Integer32):
    """Custom type voiceFaxChPhyParaDTMFRegeneration based on Integer32"""
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


_VoiceFaxChPhyParaDTMFRegeneration_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaDTMFRegeneration_Object = MibTableColumn
voiceFaxChPhyParaDTMFRegeneration = _VoiceFaxChPhyParaDTMFRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 12),
    _VoiceFaxChPhyParaDTMFRegeneration_Type()
)
voiceFaxChPhyParaDTMFRegeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaDTMFRegeneration.setStatus("mandatory")


class _VoiceFaxChPhyParaAutoLevelEnhancement_Type(Integer32):
    """Custom type voiceFaxChPhyParaAutoLevelEnhancement based on Integer32"""
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


_VoiceFaxChPhyParaAutoLevelEnhancement_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaAutoLevelEnhancement_Object = MibTableColumn
voiceFaxChPhyParaAutoLevelEnhancement = _VoiceFaxChPhyParaAutoLevelEnhancement_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 13),
    _VoiceFaxChPhyParaAutoLevelEnhancement_Type()
)
voiceFaxChPhyParaAutoLevelEnhancement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaAutoLevelEnhancement.setStatus("mandatory")


class _VoiceFaxChPhyParaBackground_Type(Integer32):
    """Custom type voiceFaxChPhyParaBackground based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regenerated", 1),
          ("silence", 2))
    )


_VoiceFaxChPhyParaBackground_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaBackground_Object = MibTableColumn
voiceFaxChPhyParaBackground = _VoiceFaxChPhyParaBackground_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 14),
    _VoiceFaxChPhyParaBackground_Type()
)
voiceFaxChPhyParaBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaBackground.setStatus("mandatory")


class _VoiceFaxChPhyParaDigitizingRate_Type(Integer32):
    """Custom type voiceFaxChPhyParaDigitizingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("rate12000", 7),
          ("rate14400", 8),
          ("rate16000", 9),
          ("rate4000", 1),
          ("rate4800", 2),
          ("rate6400", 3),
          ("rate7200", 4),
          ("rate8000", 5),
          ("rate9600", 6),
          ("rateG729", 10))
    )


_VoiceFaxChPhyParaDigitizingRate_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaDigitizingRate_Object = MibTableColumn
voiceFaxChPhyParaDigitizingRate = _VoiceFaxChPhyParaDigitizingRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 15),
    _VoiceFaxChPhyParaDigitizingRate_Type()
)
voiceFaxChPhyParaDigitizingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaDigitizingRate.setStatus("mandatory")


class _VoiceFaxChPhyParaBusyMode_Type(Integer32):
    """Custom type voiceFaxChPhyParaBusyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forcedOff", 1),
          ("forcedOn", 2),
          ("systemControlled", 3))
    )


_VoiceFaxChPhyParaBusyMode_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaBusyMode_Object = MibTableColumn
voiceFaxChPhyParaBusyMode = _VoiceFaxChPhyParaBusyMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 16),
    _VoiceFaxChPhyParaBusyMode_Type()
)
voiceFaxChPhyParaBusyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaBusyMode.setStatus("mandatory")


class _VoiceFaxChPhyParaVoiceFaxMode_Type(Integer32):
    """Custom type voiceFaxChPhyParaVoiceFaxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voiceFax", 1),
          ("voiceOnly", 2))
    )


_VoiceFaxChPhyParaVoiceFaxMode_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaVoiceFaxMode_Object = MibTableColumn
voiceFaxChPhyParaVoiceFaxMode = _VoiceFaxChPhyParaVoiceFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 17),
    _VoiceFaxChPhyParaVoiceFaxMode_Type()
)
voiceFaxChPhyParaVoiceFaxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaVoiceFaxMode.setStatus("mandatory")


class _VoiceFaxChPhyParaBandwidthAssignment_Type(Integer32):
    """Custom type voiceFaxChPhyParaBandwidthAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 2),
          ("dynamic", 3),
          ("voiceActivated", 1))
    )


_VoiceFaxChPhyParaBandwidthAssignment_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaBandwidthAssignment_Object = MibTableColumn
voiceFaxChPhyParaBandwidthAssignment = _VoiceFaxChPhyParaBandwidthAssignment_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 18),
    _VoiceFaxChPhyParaBandwidthAssignment_Type()
)
voiceFaxChPhyParaBandwidthAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaBandwidthAssignment.setStatus("mandatory")


class _VoiceFaxChPhyParaInputGain_Type(Integer32):
    """Custom type voiceFaxChPhyParaInputGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, 22),
    )


_VoiceFaxChPhyParaInputGain_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaInputGain_Object = MibTableColumn
voiceFaxChPhyParaInputGain = _VoiceFaxChPhyParaInputGain_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 19),
    _VoiceFaxChPhyParaInputGain_Type()
)
voiceFaxChPhyParaInputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaInputGain.setStatus("mandatory")
_VoiceFaxChPhyParaChannelType_Type = Integer32
_VoiceFaxChPhyParaChannelType_Object = MibTableColumn
voiceFaxChPhyParaChannelType = _VoiceFaxChPhyParaChannelType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 20),
    _VoiceFaxChPhyParaChannelType_Type()
)
voiceFaxChPhyParaChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaChannelType.setStatus("mandatory")


class _VoiceFaxChPhyParaEMTypeStrapping_Type(Integer32):
    """Custom type voiceFaxChPhyParaEMTypeStrapping based on Integer32"""
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
        *(("emTypeI", 1),
          ("emTypeII", 2),
          ("emTypeIII", 3),
          ("emTypeIV", 4),
          ("emTypeV", 5))
    )


_VoiceFaxChPhyParaEMTypeStrapping_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaEMTypeStrapping_Object = MibTableColumn
voiceFaxChPhyParaEMTypeStrapping = _VoiceFaxChPhyParaEMTypeStrapping_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 21),
    _VoiceFaxChPhyParaEMTypeStrapping_Type()
)
voiceFaxChPhyParaEMTypeStrapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaEMTypeStrapping.setStatus("mandatory")


class _VoiceFaxChPhyParaOutputAttenuation_Type(Integer32):
    """Custom type voiceFaxChPhyParaOutputAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_VoiceFaxChPhyParaOutputAttenuation_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaOutputAttenuation_Object = MibTableColumn
voiceFaxChPhyParaOutputAttenuation = _VoiceFaxChPhyParaOutputAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 22),
    _VoiceFaxChPhyParaOutputAttenuation_Type()
)
voiceFaxChPhyParaOutputAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaOutputAttenuation.setStatus("mandatory")


class _VoiceFaxChPhyParaPriority_Type(Integer32):
    """Custom type voiceFaxChPhyParaPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_VoiceFaxChPhyParaPriority_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaPriority_Object = MibTableColumn
voiceFaxChPhyParaPriority = _VoiceFaxChPhyParaPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 23),
    _VoiceFaxChPhyParaPriority_Type()
)
voiceFaxChPhyParaPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaPriority.setStatus("mandatory")


class _VoiceFaxChPhyParaFaxDigitizingRate_Type(Integer32):
    """Custom type voiceFaxChPhyParaFaxDigitizingRate based on Integer32"""
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
        *(("rate2400", 2),
          ("rate4800", 3),
          ("rate7200", 4),
          ("rate9600", 5),
          ("useVoiceRate", 1))
    )


_VoiceFaxChPhyParaFaxDigitizingRate_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaFaxDigitizingRate_Object = MibTableColumn
voiceFaxChPhyParaFaxDigitizingRate = _VoiceFaxChPhyParaFaxDigitizingRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 24),
    _VoiceFaxChPhyParaFaxDigitizingRate_Type()
)
voiceFaxChPhyParaFaxDigitizingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaFaxDigitizingRate.setStatus("mandatory")


class _VoiceFaxChPhyParaLineImpedance_Type(Integer32):
    """Custom type voiceFaxChPhyParaLineImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complex", 2),
          ("impedance600Ohms", 1))
    )


_VoiceFaxChPhyParaLineImpedance_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaLineImpedance_Object = MibTableColumn
voiceFaxChPhyParaLineImpedance = _VoiceFaxChPhyParaLineImpedance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 25),
    _VoiceFaxChPhyParaLineImpedance_Type()
)
voiceFaxChPhyParaLineImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaLineImpedance.setStatus("mandatory")


class _VoiceFaxChPhyParaMaxOutputLevel_Type(Integer32):
    """Custom type voiceFaxChPhyParaMaxOutputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level0dBmNominal", 1),
          ("levelPlus7dBm", 2))
    )


_VoiceFaxChPhyParaMaxOutputLevel_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaMaxOutputLevel_Object = MibTableColumn
voiceFaxChPhyParaMaxOutputLevel = _VoiceFaxChPhyParaMaxOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 26),
    _VoiceFaxChPhyParaMaxOutputLevel_Type()
)
voiceFaxChPhyParaMaxOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaMaxOutputLevel.setStatus("mandatory")


class _VoiceFaxChPhyParaRegenerationDelay_Type(Integer32):
    """Custom type voiceFaxChPhyParaRegenerationDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_VoiceFaxChPhyParaRegenerationDelay_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaRegenerationDelay_Object = MibTableColumn
voiceFaxChPhyParaRegenerationDelay = _VoiceFaxChPhyParaRegenerationDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 27),
    _VoiceFaxChPhyParaRegenerationDelay_Type()
)
voiceFaxChPhyParaRegenerationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaRegenerationDelay.setStatus("mandatory")


class _VoiceFaxChPhyParaMaxDialDigitTimeLimit_Type(Integer32):
    """Custom type voiceFaxChPhyParaMaxDialDigitTimeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_VoiceFaxChPhyParaMaxDialDigitTimeLimit_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaMaxDialDigitTimeLimit_Object = MibTableColumn
voiceFaxChPhyParaMaxDialDigitTimeLimit = _VoiceFaxChPhyParaMaxDialDigitTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 28),
    _VoiceFaxChPhyParaMaxDialDigitTimeLimit_Type()
)
voiceFaxChPhyParaMaxDialDigitTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaMaxDialDigitTimeLimit.setStatus("mandatory")


class _VoiceFaxChPhyParaMaxNumFwdDigits_Type(Integer32):
    """Custom type voiceFaxChPhyParaMaxNumFwdDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_VoiceFaxChPhyParaMaxNumFwdDigits_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaMaxNumFwdDigits_Object = MibTableColumn
voiceFaxChPhyParaMaxNumFwdDigits = _VoiceFaxChPhyParaMaxNumFwdDigits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 29),
    _VoiceFaxChPhyParaMaxNumFwdDigits_Type()
)
voiceFaxChPhyParaMaxNumFwdDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaMaxNumFwdDigits.setStatus("mandatory")


class _VoiceFaxChPhyParaCallProgressionTones_Type(Integer32):
    """Custom type voiceFaxChPhyParaCallProgressionTones based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("australia", 8),
          ("centralAmerica", 6),
          ("chile", 7),
          ("france", 5),
          ("germany", 4),
          ("japan", 2),
          ("northAmerica", 1),
          ("unitedKingdom", 3))
    )


_VoiceFaxChPhyParaCallProgressionTones_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaCallProgressionTones_Object = MibTableColumn
voiceFaxChPhyParaCallProgressionTones = _VoiceFaxChPhyParaCallProgressionTones_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 30),
    _VoiceFaxChPhyParaCallProgressionTones_Type()
)
voiceFaxChPhyParaCallProgressionTones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaCallProgressionTones.setStatus("mandatory")


class _VoiceFaxChPhyParaRegenFormat_Type(Integer32):
    """Custom type voiceFaxChPhyParaRegenFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmfDialing", 2),
          ("pulsedDialing", 1))
    )


_VoiceFaxChPhyParaRegenFormat_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaRegenFormat_Object = MibTableColumn
voiceFaxChPhyParaRegenFormat = _VoiceFaxChPhyParaRegenFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 31),
    _VoiceFaxChPhyParaRegenFormat_Type()
)
voiceFaxChPhyParaRegenFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaRegenFormat.setStatus("mandatory")


class _VoiceFaxChPhyParaChannelVersion_Type(Integer32):
    """Custom type voiceFaxChPhyParaChannelVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("casVer2", 8),
          ("dtmfRegne", 7),
          ("g729DigitizingRateSupported", 5),
          ("phase1and2and2dot5Fconn", 1),
          ("phase3VSW", 2),
          ("phase3dot1UV", 3),
          ("phase5dot1", 6),
          ("voiceDialingImprovement", 4))
    )


_VoiceFaxChPhyParaChannelVersion_Type.__name__ = "Integer32"
_VoiceFaxChPhyParaChannelVersion_Object = MibTableColumn
voiceFaxChPhyParaChannelVersion = _VoiceFaxChPhyParaChannelVersion_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 1, 1, 32),
    _VoiceFaxChPhyParaChannelVersion_Type()
)
voiceFaxChPhyParaChannelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFaxChPhyParaChannelVersion.setStatus("mandatory")
_VoiceFaxChSwParaTable_Object = MibTable
voiceFaxChSwParaTable = _VoiceFaxChSwParaTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 2)
)
if mibBuilder.loadTexts:
    voiceFaxChSwParaTable.setStatus("mandatory")
_VoiceFaxChSwParaEntry_Object = MibTableRow
voiceFaxChSwParaEntry = _VoiceFaxChSwParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 2, 1)
)
voiceFaxChSwParaEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "voiceFaxChSwParaCardNumber"),
    (0, "MICOM-NODE-MIB", "voiceFaxChSwParaChannelNumber"),
)
if mibBuilder.loadTexts:
    voiceFaxChSwParaEntry.setStatus("mandatory")


class _VoiceFaxChSwParaCardNumber_Type(Integer32):
    """Custom type voiceFaxChSwParaCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_VoiceFaxChSwParaCardNumber_Type.__name__ = "Integer32"
_VoiceFaxChSwParaCardNumber_Object = MibTableColumn
voiceFaxChSwParaCardNumber = _VoiceFaxChSwParaCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 2, 1, 1),
    _VoiceFaxChSwParaCardNumber_Type()
)
voiceFaxChSwParaCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFaxChSwParaCardNumber.setStatus("mandatory")


class _VoiceFaxChSwParaChannelNumber_Type(Integer32):
    """Custom type voiceFaxChSwParaChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_VoiceFaxChSwParaChannelNumber_Type.__name__ = "Integer32"
_VoiceFaxChSwParaChannelNumber_Object = MibTableColumn
voiceFaxChSwParaChannelNumber = _VoiceFaxChSwParaChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 2, 1, 2),
    _VoiceFaxChSwParaChannelNumber_Type()
)
voiceFaxChSwParaChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFaxChSwParaChannelNumber.setStatus("mandatory")


class _VoiceFaxChSwParaVoiceExtension_Type(DisplayString):
    """Custom type voiceFaxChSwParaVoiceExtension based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_VoiceFaxChSwParaVoiceExtension_Type.__name__ = "DisplayString"
_VoiceFaxChSwParaVoiceExtension_Object = MibTableColumn
voiceFaxChSwParaVoiceExtension = _VoiceFaxChSwParaVoiceExtension_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 2, 1, 3),
    _VoiceFaxChSwParaVoiceExtension_Type()
)
voiceFaxChSwParaVoiceExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChSwParaVoiceExtension.setStatus("mandatory")


class _VoiceFaxChSwParaFaxExtension_Type(DisplayString):
    """Custom type voiceFaxChSwParaFaxExtension based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_VoiceFaxChSwParaFaxExtension_Type.__name__ = "DisplayString"
_VoiceFaxChSwParaFaxExtension_Object = MibTableColumn
voiceFaxChSwParaFaxExtension = _VoiceFaxChSwParaFaxExtension_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 2, 1, 4),
    _VoiceFaxChSwParaFaxExtension_Type()
)
voiceFaxChSwParaFaxExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChSwParaFaxExtension.setStatus("mandatory")


class _VoiceFaxChSwParaAutoCallNumber_Type(DisplayString):
    """Custom type voiceFaxChSwParaAutoCallNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_VoiceFaxChSwParaAutoCallNumber_Type.__name__ = "DisplayString"
_VoiceFaxChSwParaAutoCallNumber_Object = MibTableColumn
voiceFaxChSwParaAutoCallNumber = _VoiceFaxChSwParaAutoCallNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 2, 1, 5),
    _VoiceFaxChSwParaAutoCallNumber_Type()
)
voiceFaxChSwParaAutoCallNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChSwParaAutoCallNumber.setStatus("mandatory")


class _VoiceFaxChSwParaReceiveInhibit_Type(Integer32):
    """Custom type voiceFaxChSwParaReceiveInhibit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_VoiceFaxChSwParaReceiveInhibit_Type.__name__ = "Integer32"
_VoiceFaxChSwParaReceiveInhibit_Object = MibTableColumn
voiceFaxChSwParaReceiveInhibit = _VoiceFaxChSwParaReceiveInhibit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 2, 1, 6),
    _VoiceFaxChSwParaReceiveInhibit_Type()
)
voiceFaxChSwParaReceiveInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChSwParaReceiveInhibit.setStatus("mandatory")


class _VoiceFaxChSwParaCallInhibit_Type(Integer32):
    """Custom type voiceFaxChSwParaCallInhibit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_VoiceFaxChSwParaCallInhibit_Type.__name__ = "Integer32"
_VoiceFaxChSwParaCallInhibit_Object = MibTableColumn
voiceFaxChSwParaCallInhibit = _VoiceFaxChSwParaCallInhibit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 2, 1, 7),
    _VoiceFaxChSwParaCallInhibit_Type()
)
voiceFaxChSwParaCallInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChSwParaCallInhibit.setStatus("mandatory")


class _VoiceFaxChSwNumberOfDigitsInPhoneNumber_Type(Integer32):
    """Custom type voiceFaxChSwNumberOfDigitsInPhoneNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_VoiceFaxChSwNumberOfDigitsInPhoneNumber_Type.__name__ = "Integer32"
_VoiceFaxChSwNumberOfDigitsInPhoneNumber_Object = MibScalar
voiceFaxChSwNumberOfDigitsInPhoneNumber = _VoiceFaxChSwNumberOfDigitsInPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 3, 3),
    _VoiceFaxChSwNumberOfDigitsInPhoneNumber_Type()
)
voiceFaxChSwNumberOfDigitsInPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceFaxChSwNumberOfDigitsInPhoneNumber.setStatus("mandatory")
_Digital_voice_channel_ObjectIdentity = ObjectIdentity
digital_voice_channel = _Digital_voice_channel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4)
)
_DigitalVoiceChPhyParaTable_Object = MibTable
digitalVoiceChPhyParaTable = _DigitalVoiceChPhyParaTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaTable.setStatus("mandatory")
_DigitalVoiceChPhyParaEntry_Object = MibTableRow
digitalVoiceChPhyParaEntry = _DigitalVoiceChPhyParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1)
)
digitalVoiceChPhyParaEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "digitalVoiceChPhyParaCardNumber"),
    (0, "MICOM-NODE-MIB", "digitalVoiceChPhyParaChannelNumber"),
)
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaEntry.setStatus("mandatory")


class _DigitalVoiceChPhyParaCardNumber_Type(Integer32):
    """Custom type digitalVoiceChPhyParaCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_DigitalVoiceChPhyParaCardNumber_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaCardNumber_Object = MibTableColumn
digitalVoiceChPhyParaCardNumber = _DigitalVoiceChPhyParaCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 1),
    _DigitalVoiceChPhyParaCardNumber_Type()
)
digitalVoiceChPhyParaCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaCardNumber.setStatus("mandatory")


class _DigitalVoiceChPhyParaChannelNumber_Type(Integer32):
    """Custom type digitalVoiceChPhyParaChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DigitalVoiceChPhyParaChannelNumber_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaChannelNumber_Object = MibTableColumn
digitalVoiceChPhyParaChannelNumber = _DigitalVoiceChPhyParaChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 2),
    _DigitalVoiceChPhyParaChannelNumber_Type()
)
digitalVoiceChPhyParaChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaChannelNumber.setStatus("mandatory")


class _DigitalVoiceChPhyParaViewSignallingType_Type(Integer32):
    """Custom type digitalVoiceChPhyParaViewSignallingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("casVers01", 6),
          ("dc5b", 5),
          ("dc5bInvert", 3),
          ("r2byQdot421", 7),
          ("tieInvert", 4),
          ("tieTrunk", 1),
          ("transparent", 2))
    )


_DigitalVoiceChPhyParaViewSignallingType_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaViewSignallingType_Object = MibTableColumn
digitalVoiceChPhyParaViewSignallingType = _DigitalVoiceChPhyParaViewSignallingType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 3),
    _DigitalVoiceChPhyParaViewSignallingType_Type()
)
digitalVoiceChPhyParaViewSignallingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaViewSignallingType.setStatus("mandatory")


class _DigitalVoiceChPhyParaBergStrapType_Type(Integer32):
    """Custom type digitalVoiceChPhyParaBergStrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("digitalVoiceModule", 1)
    )


_DigitalVoiceChPhyParaBergStrapType_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaBergStrapType_Object = MibTableColumn
digitalVoiceChPhyParaBergStrapType = _DigitalVoiceChPhyParaBergStrapType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 4),
    _DigitalVoiceChPhyParaBergStrapType_Type()
)
digitalVoiceChPhyParaBergStrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaBergStrapType.setStatus("mandatory")


class _DigitalVoiceChPhyParaPortEmulation_Type(Integer32):
    """Custom type digitalVoiceChPhyParaPortEmulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("casVers01", 6),
          ("dc5b", 5),
          ("dc5bInvert", 3),
          ("r2byQdot421", 7),
          ("tieInvert", 2),
          ("tieTrunk", 1),
          ("transparent", 4))
    )


_DigitalVoiceChPhyParaPortEmulation_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaPortEmulation_Object = MibTableColumn
digitalVoiceChPhyParaPortEmulation = _DigitalVoiceChPhyParaPortEmulation_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 5),
    _DigitalVoiceChPhyParaPortEmulation_Type()
)
digitalVoiceChPhyParaPortEmulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaPortEmulation.setStatus("mandatory")
_DigitalVoiceChPhyParaSuppression_Type = Integer32
_DigitalVoiceChPhyParaSuppression_Object = MibTableColumn
digitalVoiceChPhyParaSuppression = _DigitalVoiceChPhyParaSuppression_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 6),
    _DigitalVoiceChPhyParaSuppression_Type()
)
digitalVoiceChPhyParaSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaSuppression.setStatus("mandatory")
_DigitalVoiceChPhyParaJitter_Type = Integer32
_DigitalVoiceChPhyParaJitter_Object = MibTableColumn
digitalVoiceChPhyParaJitter = _DigitalVoiceChPhyParaJitter_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 7),
    _DigitalVoiceChPhyParaJitter_Type()
)
digitalVoiceChPhyParaJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaJitter.setStatus("mandatory")


class _DigitalVoiceChPhyParaDTMFRegeneration_Type(Integer32):
    """Custom type digitalVoiceChPhyParaDTMFRegeneration based on Integer32"""
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


_DigitalVoiceChPhyParaDTMFRegeneration_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaDTMFRegeneration_Object = MibTableColumn
digitalVoiceChPhyParaDTMFRegeneration = _DigitalVoiceChPhyParaDTMFRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 8),
    _DigitalVoiceChPhyParaDTMFRegeneration_Type()
)
digitalVoiceChPhyParaDTMFRegeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaDTMFRegeneration.setStatus("mandatory")


class _DigitalVoiceChPhyParaAutoGainControl_Type(Integer32):
    """Custom type digitalVoiceChPhyParaAutoGainControl based on Integer32"""
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


_DigitalVoiceChPhyParaAutoGainControl_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaAutoGainControl_Object = MibTableColumn
digitalVoiceChPhyParaAutoGainControl = _DigitalVoiceChPhyParaAutoGainControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 9),
    _DigitalVoiceChPhyParaAutoGainControl_Type()
)
digitalVoiceChPhyParaAutoGainControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaAutoGainControl.setStatus("mandatory")


class _DigitalVoiceChPhyParaBackground_Type(Integer32):
    """Custom type digitalVoiceChPhyParaBackground based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regenerated", 1),
          ("silence", 2))
    )


_DigitalVoiceChPhyParaBackground_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaBackground_Object = MibTableColumn
digitalVoiceChPhyParaBackground = _DigitalVoiceChPhyParaBackground_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 10),
    _DigitalVoiceChPhyParaBackground_Type()
)
digitalVoiceChPhyParaBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaBackground.setStatus("mandatory")


class _DigitalVoiceChPhyParaDigitizingRate_Type(Integer32):
    """Custom type digitalVoiceChPhyParaDigitizingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("rate12000", 7),
          ("rate14400", 8),
          ("rate16000", 9),
          ("rate4000", 1),
          ("rate4800", 2),
          ("rate6400", 3),
          ("rate7200", 4),
          ("rate8000", 5),
          ("rate9600", 6),
          ("rateG729", 10))
    )


_DigitalVoiceChPhyParaDigitizingRate_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaDigitizingRate_Object = MibTableColumn
digitalVoiceChPhyParaDigitizingRate = _DigitalVoiceChPhyParaDigitizingRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 11),
    _DigitalVoiceChPhyParaDigitizingRate_Type()
)
digitalVoiceChPhyParaDigitizingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaDigitizingRate.setStatus("mandatory")


class _DigitalVoiceChPhyParaBusyMode_Type(Integer32):
    """Custom type digitalVoiceChPhyParaBusyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forcedOff", 1),
          ("forcedOn", 2),
          ("systemControlled", 3))
    )


_DigitalVoiceChPhyParaBusyMode_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaBusyMode_Object = MibTableColumn
digitalVoiceChPhyParaBusyMode = _DigitalVoiceChPhyParaBusyMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 12),
    _DigitalVoiceChPhyParaBusyMode_Type()
)
digitalVoiceChPhyParaBusyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaBusyMode.setStatus("mandatory")


class _DigitalVoiceChPhyParaVoiceFaxMode_Type(Integer32):
    """Custom type digitalVoiceChPhyParaVoiceFaxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voiceFax", 1),
          ("voiceOnly", 2))
    )


_DigitalVoiceChPhyParaVoiceFaxMode_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaVoiceFaxMode_Object = MibTableColumn
digitalVoiceChPhyParaVoiceFaxMode = _DigitalVoiceChPhyParaVoiceFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 13),
    _DigitalVoiceChPhyParaVoiceFaxMode_Type()
)
digitalVoiceChPhyParaVoiceFaxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaVoiceFaxMode.setStatus("mandatory")


class _DigitalVoiceChPhyParaBandwidthAssignment_Type(Integer32):
    """Custom type digitalVoiceChPhyParaBandwidthAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 2),
          ("dynamic", 3),
          ("voiceActivated", 1))
    )


_DigitalVoiceChPhyParaBandwidthAssignment_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaBandwidthAssignment_Object = MibTableColumn
digitalVoiceChPhyParaBandwidthAssignment = _DigitalVoiceChPhyParaBandwidthAssignment_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 14),
    _DigitalVoiceChPhyParaBandwidthAssignment_Type()
)
digitalVoiceChPhyParaBandwidthAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaBandwidthAssignment.setStatus("mandatory")


class _DigitalVoiceChPhyParaInputGain_Type(Integer32):
    """Custom type digitalVoiceChPhyParaInputGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, 8),
    )


_DigitalVoiceChPhyParaInputGain_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaInputGain_Object = MibTableColumn
digitalVoiceChPhyParaInputGain = _DigitalVoiceChPhyParaInputGain_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 15),
    _DigitalVoiceChPhyParaInputGain_Type()
)
digitalVoiceChPhyParaInputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaInputGain.setStatus("mandatory")
_DigitalVoiceChPhyParaChannelType_Type = Integer32
_DigitalVoiceChPhyParaChannelType_Object = MibTableColumn
digitalVoiceChPhyParaChannelType = _DigitalVoiceChPhyParaChannelType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 16),
    _DigitalVoiceChPhyParaChannelType_Type()
)
digitalVoiceChPhyParaChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaChannelType.setStatus("mandatory")


class _DigitalVoiceChPhyParaOutputAttenuation_Type(Integer32):
    """Custom type digitalVoiceChPhyParaOutputAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DigitalVoiceChPhyParaOutputAttenuation_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaOutputAttenuation_Object = MibTableColumn
digitalVoiceChPhyParaOutputAttenuation = _DigitalVoiceChPhyParaOutputAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 17),
    _DigitalVoiceChPhyParaOutputAttenuation_Type()
)
digitalVoiceChPhyParaOutputAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaOutputAttenuation.setStatus("mandatory")


class _DigitalVoiceChPhyParaPriority_Type(Integer32):
    """Custom type digitalVoiceChPhyParaPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_DigitalVoiceChPhyParaPriority_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaPriority_Object = MibTableColumn
digitalVoiceChPhyParaPriority = _DigitalVoiceChPhyParaPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 18),
    _DigitalVoiceChPhyParaPriority_Type()
)
digitalVoiceChPhyParaPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaPriority.setStatus("mandatory")


class _DigitalVoiceChPhyParaFaxDigitizingRate_Type(Integer32):
    """Custom type digitalVoiceChPhyParaFaxDigitizingRate based on Integer32"""
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
        *(("rate2400", 2),
          ("rate4800", 3),
          ("rate7200", 4),
          ("rate9600", 5),
          ("useVoiceRate", 1))
    )


_DigitalVoiceChPhyParaFaxDigitizingRate_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaFaxDigitizingRate_Object = MibTableColumn
digitalVoiceChPhyParaFaxDigitizingRate = _DigitalVoiceChPhyParaFaxDigitizingRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 19),
    _DigitalVoiceChPhyParaFaxDigitizingRate_Type()
)
digitalVoiceChPhyParaFaxDigitizingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaFaxDigitizingRate.setStatus("mandatory")


class _DigitalVoiceChPhyParaRegenerationDelay_Type(Integer32):
    """Custom type digitalVoiceChPhyParaRegenerationDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DigitalVoiceChPhyParaRegenerationDelay_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaRegenerationDelay_Object = MibTableColumn
digitalVoiceChPhyParaRegenerationDelay = _DigitalVoiceChPhyParaRegenerationDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 20),
    _DigitalVoiceChPhyParaRegenerationDelay_Type()
)
digitalVoiceChPhyParaRegenerationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaRegenerationDelay.setStatus("mandatory")


class _DigitalVoiceChPhyParaMaxDialDigitTimeLimit_Type(Integer32):
    """Custom type digitalVoiceChPhyParaMaxDialDigitTimeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DigitalVoiceChPhyParaMaxDialDigitTimeLimit_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaMaxDialDigitTimeLimit_Object = MibTableColumn
digitalVoiceChPhyParaMaxDialDigitTimeLimit = _DigitalVoiceChPhyParaMaxDialDigitTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 21),
    _DigitalVoiceChPhyParaMaxDialDigitTimeLimit_Type()
)
digitalVoiceChPhyParaMaxDialDigitTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaMaxDialDigitTimeLimit.setStatus("mandatory")


class _DigitalVoiceChPhyParaMaxNumFwdDigits_Type(Integer32):
    """Custom type digitalVoiceChPhyParaMaxNumFwdDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DigitalVoiceChPhyParaMaxNumFwdDigits_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaMaxNumFwdDigits_Object = MibTableColumn
digitalVoiceChPhyParaMaxNumFwdDigits = _DigitalVoiceChPhyParaMaxNumFwdDigits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 22),
    _DigitalVoiceChPhyParaMaxNumFwdDigits_Type()
)
digitalVoiceChPhyParaMaxNumFwdDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaMaxNumFwdDigits.setStatus("mandatory")


class _DigitalVoiceChPhyParaCallProgressionTones_Type(Integer32):
    """Custom type digitalVoiceChPhyParaCallProgressionTones based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("australia", 8),
          ("centralAmerica", 6),
          ("chile", 7),
          ("france", 5),
          ("germany", 4),
          ("japan", 2),
          ("northAmerica", 1),
          ("unitedKingdom", 3))
    )


_DigitalVoiceChPhyParaCallProgressionTones_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaCallProgressionTones_Object = MibTableColumn
digitalVoiceChPhyParaCallProgressionTones = _DigitalVoiceChPhyParaCallProgressionTones_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 23),
    _DigitalVoiceChPhyParaCallProgressionTones_Type()
)
digitalVoiceChPhyParaCallProgressionTones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaCallProgressionTones.setStatus("mandatory")


class _DigitalVoiceChPhyParaRegenerationFormat_Type(Integer32):
    """Custom type digitalVoiceChPhyParaRegenerationFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmfDialing", 2),
          ("pulsedDialing", 1))
    )


_DigitalVoiceChPhyParaRegenerationFormat_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaRegenerationFormat_Object = MibTableColumn
digitalVoiceChPhyParaRegenerationFormat = _DigitalVoiceChPhyParaRegenerationFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 24),
    _DigitalVoiceChPhyParaRegenerationFormat_Type()
)
digitalVoiceChPhyParaRegenerationFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaRegenerationFormat.setStatus("mandatory")


class _DigitalVoiceChPhyParaCompander_Type(Integer32):
    """Custom type digitalVoiceChPhyParaCompander based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 2),
          ("uLaw", 1))
    )


_DigitalVoiceChPhyParaCompander_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaCompander_Object = MibTableColumn
digitalVoiceChPhyParaCompander = _DigitalVoiceChPhyParaCompander_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 25),
    _DigitalVoiceChPhyParaCompander_Type()
)
digitalVoiceChPhyParaCompander.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaCompander.setStatus("mandatory")


class _DigitalVoiceChPhyParaPremiumVoice_Type(Integer32):
    """Custom type digitalVoiceChPhyParaPremiumVoice based on Integer32"""
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


_DigitalVoiceChPhyParaPremiumVoice_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaPremiumVoice_Object = MibTableColumn
digitalVoiceChPhyParaPremiumVoice = _DigitalVoiceChPhyParaPremiumVoice_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 26),
    _DigitalVoiceChPhyParaPremiumVoice_Type()
)
digitalVoiceChPhyParaPremiumVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaPremiumVoice.setStatus("mandatory")


class _DigitalVoiceChPhyParaModuleIdentification_Type(Integer32):
    """Custom type digitalVoiceChPhyParaModuleIdentification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("invalid", 3),
          ("t1", 1))
    )


_DigitalVoiceChPhyParaModuleIdentification_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaModuleIdentification_Object = MibTableColumn
digitalVoiceChPhyParaModuleIdentification = _DigitalVoiceChPhyParaModuleIdentification_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 27),
    _DigitalVoiceChPhyParaModuleIdentification_Type()
)
digitalVoiceChPhyParaModuleIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaModuleIdentification.setStatus("mandatory")


class _DigitalVoiceChPhyParaChannelVersion_Type(Integer32):
    """Custom type digitalVoiceChPhyParaChannelVersion based on Integer32"""
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
        *(("casVer2", 5),
          ("digitalVoiceModule", 1),
          ("dtmfRegne", 4),
          ("g729DigitizingRateSupported", 2),
          ("phase5dot1", 3))
    )


_DigitalVoiceChPhyParaChannelVersion_Type.__name__ = "Integer32"
_DigitalVoiceChPhyParaChannelVersion_Object = MibTableColumn
digitalVoiceChPhyParaChannelVersion = _DigitalVoiceChPhyParaChannelVersion_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 1, 1, 28),
    _DigitalVoiceChPhyParaChannelVersion_Type()
)
digitalVoiceChPhyParaChannelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalVoiceChPhyParaChannelVersion.setStatus("mandatory")
_DigitalVoiceChSwParaTable_Object = MibTable
digitalVoiceChSwParaTable = _DigitalVoiceChSwParaTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 2)
)
if mibBuilder.loadTexts:
    digitalVoiceChSwParaTable.setStatus("mandatory")
_DigitalVoiceChSwParaEntry_Object = MibTableRow
digitalVoiceChSwParaEntry = _DigitalVoiceChSwParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 2, 1)
)
digitalVoiceChSwParaEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "digitalVoiceChSwParaCardNumber"),
    (0, "MICOM-NODE-MIB", "digitalVoiceChSwParaChannelNumber"),
)
if mibBuilder.loadTexts:
    digitalVoiceChSwParaEntry.setStatus("mandatory")


class _DigitalVoiceChSwParaCardNumber_Type(Integer32):
    """Custom type digitalVoiceChSwParaCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_DigitalVoiceChSwParaCardNumber_Type.__name__ = "Integer32"
_DigitalVoiceChSwParaCardNumber_Object = MibTableColumn
digitalVoiceChSwParaCardNumber = _DigitalVoiceChSwParaCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 2, 1, 1),
    _DigitalVoiceChSwParaCardNumber_Type()
)
digitalVoiceChSwParaCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalVoiceChSwParaCardNumber.setStatus("mandatory")


class _DigitalVoiceChSwParaChannelNumber_Type(Integer32):
    """Custom type digitalVoiceChSwParaChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DigitalVoiceChSwParaChannelNumber_Type.__name__ = "Integer32"
_DigitalVoiceChSwParaChannelNumber_Object = MibTableColumn
digitalVoiceChSwParaChannelNumber = _DigitalVoiceChSwParaChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 2, 1, 2),
    _DigitalVoiceChSwParaChannelNumber_Type()
)
digitalVoiceChSwParaChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalVoiceChSwParaChannelNumber.setStatus("mandatory")


class _DigitalVoiceChSwParaVoiceExtension_Type(DisplayString):
    """Custom type digitalVoiceChSwParaVoiceExtension based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_DigitalVoiceChSwParaVoiceExtension_Type.__name__ = "DisplayString"
_DigitalVoiceChSwParaVoiceExtension_Object = MibTableColumn
digitalVoiceChSwParaVoiceExtension = _DigitalVoiceChSwParaVoiceExtension_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 2, 1, 3),
    _DigitalVoiceChSwParaVoiceExtension_Type()
)
digitalVoiceChSwParaVoiceExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChSwParaVoiceExtension.setStatus("mandatory")


class _DigitalVoiceChSwParaAutoCallNumber_Type(DisplayString):
    """Custom type digitalVoiceChSwParaAutoCallNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_DigitalVoiceChSwParaAutoCallNumber_Type.__name__ = "DisplayString"
_DigitalVoiceChSwParaAutoCallNumber_Object = MibTableColumn
digitalVoiceChSwParaAutoCallNumber = _DigitalVoiceChSwParaAutoCallNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 2, 1, 4),
    _DigitalVoiceChSwParaAutoCallNumber_Type()
)
digitalVoiceChSwParaAutoCallNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChSwParaAutoCallNumber.setStatus("mandatory")


class _DigitalVoiceChSwParaReceiveInhibit_Type(Integer32):
    """Custom type digitalVoiceChSwParaReceiveInhibit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_DigitalVoiceChSwParaReceiveInhibit_Type.__name__ = "Integer32"
_DigitalVoiceChSwParaReceiveInhibit_Object = MibTableColumn
digitalVoiceChSwParaReceiveInhibit = _DigitalVoiceChSwParaReceiveInhibit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 2, 1, 5),
    _DigitalVoiceChSwParaReceiveInhibit_Type()
)
digitalVoiceChSwParaReceiveInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChSwParaReceiveInhibit.setStatus("mandatory")


class _DigitalVoiceChSwParaCallInhibit_Type(Integer32):
    """Custom type digitalVoiceChSwParaCallInhibit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_DigitalVoiceChSwParaCallInhibit_Type.__name__ = "Integer32"
_DigitalVoiceChSwParaCallInhibit_Object = MibTableColumn
digitalVoiceChSwParaCallInhibit = _DigitalVoiceChSwParaCallInhibit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 4, 4, 2, 1, 6),
    _DigitalVoiceChSwParaCallInhibit_Type()
)
digitalVoiceChSwParaCallInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalVoiceChSwParaCallInhibit.setStatus("mandatory")
_Link_ObjectIdentity = ObjectIdentity
link = _Link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5)
)
_Mux_link_ObjectIdentity = ObjectIdentity
mux_link = _Mux_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 1)
)
_MuxLinkCfgTable_Object = MibTable
muxLinkCfgTable = _MuxLinkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    muxLinkCfgTable.setStatus("mandatory")
_MuxLinkCfgEntry_Object = MibTableRow
muxLinkCfgEntry = _MuxLinkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 1, 1, 1)
)
muxLinkCfgEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "muxLinkCfgCardNumber"),
    (0, "MICOM-NODE-MIB", "muxLinkCfgChannelNumber"),
)
if mibBuilder.loadTexts:
    muxLinkCfgEntry.setStatus("mandatory")


class _MuxLinkCfgCardNumber_Type(Integer32):
    """Custom type muxLinkCfgCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MuxLinkCfgCardNumber_Type.__name__ = "Integer32"
_MuxLinkCfgCardNumber_Object = MibTableColumn
muxLinkCfgCardNumber = _MuxLinkCfgCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 1, 1, 1, 1),
    _MuxLinkCfgCardNumber_Type()
)
muxLinkCfgCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxLinkCfgCardNumber.setStatus("mandatory")


class _MuxLinkCfgChannelNumber_Type(Integer32):
    """Custom type muxLinkCfgChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_MuxLinkCfgChannelNumber_Type.__name__ = "Integer32"
_MuxLinkCfgChannelNumber_Object = MibTableColumn
muxLinkCfgChannelNumber = _MuxLinkCfgChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 1, 1, 1, 2),
    _MuxLinkCfgChannelNumber_Type()
)
muxLinkCfgChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxLinkCfgChannelNumber.setStatus("mandatory")


class _MuxLinkCfgDataRate_Type(Integer32):
    """Custom type muxLinkCfgDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("rate12000Sync", 5),
          ("rate1200Async", 11),
          ("rate14400Sync", 6),
          ("rate16800Sync", 7),
          ("rate1800Async", 10),
          ("rate19200Sync", 8),
          ("rate2400Sync", 2),
          ("rate4800Sync", 3),
          ("rate9600Async", 9),
          ("rate9600Sync", 4))
    )


_MuxLinkCfgDataRate_Type.__name__ = "Integer32"
_MuxLinkCfgDataRate_Object = MibTableColumn
muxLinkCfgDataRate = _MuxLinkCfgDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 1, 1, 1, 3),
    _MuxLinkCfgDataRate_Type()
)
muxLinkCfgDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxLinkCfgDataRate.setStatus("mandatory")
_MuxOrLEsiPreConfigTable_Object = MibTable
muxOrLEsiPreConfigTable = _MuxOrLEsiPreConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    muxOrLEsiPreConfigTable.setStatus("mandatory")
_MuxOrLEsiPreConfigEntry_Object = MibTableRow
muxOrLEsiPreConfigEntry = _MuxOrLEsiPreConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 1, 2, 1)
)
muxOrLEsiPreConfigEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "muxOrLEsiPreConfigCardNumber"),
    (0, "MICOM-NODE-MIB", "muxOrLEsiPreConfigChannelNumber"),
)
if mibBuilder.loadTexts:
    muxOrLEsiPreConfigEntry.setStatus("mandatory")


class _MuxOrLEsiPreConfigCardNumber_Type(Integer32):
    """Custom type muxOrLEsiPreConfigCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MuxOrLEsiPreConfigCardNumber_Type.__name__ = "Integer32"
_MuxOrLEsiPreConfigCardNumber_Object = MibTableColumn
muxOrLEsiPreConfigCardNumber = _MuxOrLEsiPreConfigCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 1, 2, 1, 1),
    _MuxOrLEsiPreConfigCardNumber_Type()
)
muxOrLEsiPreConfigCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxOrLEsiPreConfigCardNumber.setStatus("mandatory")


class _MuxOrLEsiPreConfigChannelNumber_Type(Integer32):
    """Custom type muxOrLEsiPreConfigChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_MuxOrLEsiPreConfigChannelNumber_Type.__name__ = "Integer32"
_MuxOrLEsiPreConfigChannelNumber_Object = MibTableColumn
muxOrLEsiPreConfigChannelNumber = _MuxOrLEsiPreConfigChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 1, 2, 1, 2),
    _MuxOrLEsiPreConfigChannelNumber_Type()
)
muxOrLEsiPreConfigChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxOrLEsiPreConfigChannelNumber.setStatus("mandatory")


class _MuxOrLEsiPreConfigDataRate_Type(Integer32):
    """Custom type muxOrLEsiPreConfigDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("lEsiRate126000", 13),
          ("lEsiRate192000", 14),
          ("lEsiRate252000", 15),
          ("lEsiRate64000", 12),
          ("muxOrLEsiExternal", 1),
          ("muxRate12000Sync", 5),
          ("muxRate1200Async", 11),
          ("muxRate14400Sync", 6),
          ("muxRate16800Sync", 7),
          ("muxRate1800Async", 10),
          ("muxRate19200Sync", 8),
          ("muxRate2400Sync", 2),
          ("muxRate4800Sync", 3),
          ("muxRate9600Async", 9),
          ("muxRate9600Sync", 4))
    )


_MuxOrLEsiPreConfigDataRate_Type.__name__ = "Integer32"
_MuxOrLEsiPreConfigDataRate_Object = MibTableColumn
muxOrLEsiPreConfigDataRate = _MuxOrLEsiPreConfigDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 1, 2, 1, 3),
    _MuxOrLEsiPreConfigDataRate_Type()
)
muxOrLEsiPreConfigDataRate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    muxOrLEsiPreConfigDataRate.setStatus("mandatory")
_Esi_link_ObjectIdentity = ObjectIdentity
esi_link = _Esi_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2)
)
_EsiLinkCfgTable_Object = MibTable
esiLinkCfgTable = _EsiLinkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    esiLinkCfgTable.setStatus("mandatory")
_EsiLinkCfgEntry_Object = MibTableRow
esiLinkCfgEntry = _EsiLinkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 1, 1)
)
esiLinkCfgEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "esiLinkCfgCardNumber"),
    (0, "MICOM-NODE-MIB", "esiLinkCfgChannelNumber"),
)
if mibBuilder.loadTexts:
    esiLinkCfgEntry.setStatus("mandatory")


class _EsiLinkCfgCardNumber_Type(Integer32):
    """Custom type esiLinkCfgCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_EsiLinkCfgCardNumber_Type.__name__ = "Integer32"
_EsiLinkCfgCardNumber_Object = MibTableColumn
esiLinkCfgCardNumber = _EsiLinkCfgCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 1, 1, 1),
    _EsiLinkCfgCardNumber_Type()
)
esiLinkCfgCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiLinkCfgCardNumber.setStatus("mandatory")


class _EsiLinkCfgChannelNumber_Type(Integer32):
    """Custom type esiLinkCfgChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_EsiLinkCfgChannelNumber_Type.__name__ = "Integer32"
_EsiLinkCfgChannelNumber_Object = MibTableColumn
esiLinkCfgChannelNumber = _EsiLinkCfgChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 1, 1, 2),
    _EsiLinkCfgChannelNumber_Type()
)
esiLinkCfgChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiLinkCfgChannelNumber.setStatus("mandatory")


class _EsiLinkCfgDataRate_Type(Integer32):
    """Custom type esiLinkCfgDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("rate12000Sync", 5),
          ("rate14400Sync", 6),
          ("rate16800Sync", 7),
          ("rate19200Sync", 8),
          ("rate2400Sync", 2),
          ("rate38400Sync", 9),
          ("rate4800Sync", 3),
          ("rate56000Sync", 10),
          ("rate64000Sync", 11),
          ("rate9600Sync", 4))
    )


_EsiLinkCfgDataRate_Type.__name__ = "Integer32"
_EsiLinkCfgDataRate_Object = MibTableColumn
esiLinkCfgDataRate = _EsiLinkCfgDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 1, 1, 3),
    _EsiLinkCfgDataRate_Type()
)
esiLinkCfgDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiLinkCfgDataRate.setStatus("mandatory")
_EsiOrSecLinkPreConfigTable_Object = MibTable
esiOrSecLinkPreConfigTable = _EsiOrSecLinkPreConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    esiOrSecLinkPreConfigTable.setStatus("mandatory")
_EsiOrSecLinkPreConfigEntry_Object = MibTableRow
esiOrSecLinkPreConfigEntry = _EsiOrSecLinkPreConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 2, 1)
)
esiOrSecLinkPreConfigEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "esiOrSecLinkPreConfigCardNumber"),
    (0, "MICOM-NODE-MIB", "esiOrSecLinkPreConfigChannelNumber"),
)
if mibBuilder.loadTexts:
    esiOrSecLinkPreConfigEntry.setStatus("mandatory")


class _EsiOrSecLinkPreConfigCardNumber_Type(Integer32):
    """Custom type esiOrSecLinkPreConfigCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_EsiOrSecLinkPreConfigCardNumber_Type.__name__ = "Integer32"
_EsiOrSecLinkPreConfigCardNumber_Object = MibTableColumn
esiOrSecLinkPreConfigCardNumber = _EsiOrSecLinkPreConfigCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 2, 1, 1),
    _EsiOrSecLinkPreConfigCardNumber_Type()
)
esiOrSecLinkPreConfigCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiOrSecLinkPreConfigCardNumber.setStatus("mandatory")


class _EsiOrSecLinkPreConfigChannelNumber_Type(Integer32):
    """Custom type esiOrSecLinkPreConfigChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_EsiOrSecLinkPreConfigChannelNumber_Type.__name__ = "Integer32"
_EsiOrSecLinkPreConfigChannelNumber_Object = MibTableColumn
esiOrSecLinkPreConfigChannelNumber = _EsiOrSecLinkPreConfigChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 2, 1, 2),
    _EsiOrSecLinkPreConfigChannelNumber_Type()
)
esiOrSecLinkPreConfigChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiOrSecLinkPreConfigChannelNumber.setStatus("mandatory")


class _EsiOrSecLinkPreConfigDataRate_Type(Integer32):
    """Custom type esiOrSecLinkPreConfigDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("rate12000Sync", 5),
          ("rate14400Sync", 6),
          ("rate16800Sync", 7),
          ("rate19200Sync", 8),
          ("rate2400Sync", 2),
          ("rate38400Sync", 9),
          ("rate4800Sync", 3),
          ("rate56000Sync", 10),
          ("rate64000Sync", 11),
          ("rate9600Sync", 4))
    )


_EsiOrSecLinkPreConfigDataRate_Type.__name__ = "Integer32"
_EsiOrSecLinkPreConfigDataRate_Object = MibTableColumn
esiOrSecLinkPreConfigDataRate = _EsiOrSecLinkPreConfigDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 2, 1, 3),
    _EsiOrSecLinkPreConfigDataRate_Type()
)
esiOrSecLinkPreConfigDataRate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    esiOrSecLinkPreConfigDataRate.setStatus("mandatory")
_EsiOrSecLinkAssignCfgTable_Object = MibTable
esiOrSecLinkAssignCfgTable = _EsiOrSecLinkAssignCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 3)
)
if mibBuilder.loadTexts:
    esiOrSecLinkAssignCfgTable.setStatus("mandatory")
_EsiOrSecLinkAssignCfgEntry_Object = MibTableRow
esiOrSecLinkAssignCfgEntry = _EsiOrSecLinkAssignCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 3, 1)
)
esiOrSecLinkAssignCfgEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "esiOrSecLinkAssignCfgCardNumber"),
    (0, "MICOM-NODE-MIB", "esiOrSecLinkAssignCfgChannelNumber"),
)
if mibBuilder.loadTexts:
    esiOrSecLinkAssignCfgEntry.setStatus("mandatory")
_EsiOrSecLinkAssignCfgCardNumber_Type = Integer32
_EsiOrSecLinkAssignCfgCardNumber_Object = MibTableColumn
esiOrSecLinkAssignCfgCardNumber = _EsiOrSecLinkAssignCfgCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 3, 1, 1),
    _EsiOrSecLinkAssignCfgCardNumber_Type()
)
esiOrSecLinkAssignCfgCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiOrSecLinkAssignCfgCardNumber.setStatus("mandatory")
_EsiOrSecLinkAssignCfgChannelNumber_Type = Integer32
_EsiOrSecLinkAssignCfgChannelNumber_Object = MibTableColumn
esiOrSecLinkAssignCfgChannelNumber = _EsiOrSecLinkAssignCfgChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 3, 1, 2),
    _EsiOrSecLinkAssignCfgChannelNumber_Type()
)
esiOrSecLinkAssignCfgChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiOrSecLinkAssignCfgChannelNumber.setStatus("mandatory")


class _EsiOrSecLinkAssignCfgLinkForcedOn_Type(Integer32):
    """Custom type esiOrSecLinkAssignCfgLinkForcedOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_EsiOrSecLinkAssignCfgLinkForcedOn_Type.__name__ = "Integer32"
_EsiOrSecLinkAssignCfgLinkForcedOn_Object = MibTableColumn
esiOrSecLinkAssignCfgLinkForcedOn = _EsiOrSecLinkAssignCfgLinkForcedOn_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 3, 1, 3),
    _EsiOrSecLinkAssignCfgLinkForcedOn_Type()
)
esiOrSecLinkAssignCfgLinkForcedOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiOrSecLinkAssignCfgLinkForcedOn.setStatus("mandatory")


class _EsiOrSecLinkAssignCfgSecLinkBackUpOnly_Type(Integer32):
    """Custom type esiOrSecLinkAssignCfgSecLinkBackUpOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_EsiOrSecLinkAssignCfgSecLinkBackUpOnly_Type.__name__ = "Integer32"
_EsiOrSecLinkAssignCfgSecLinkBackUpOnly_Object = MibTableColumn
esiOrSecLinkAssignCfgSecLinkBackUpOnly = _EsiOrSecLinkAssignCfgSecLinkBackUpOnly_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 3, 1, 4),
    _EsiOrSecLinkAssignCfgSecLinkBackUpOnly_Type()
)
esiOrSecLinkAssignCfgSecLinkBackUpOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiOrSecLinkAssignCfgSecLinkBackUpOnly.setStatus("mandatory")


class _EsiOrSecLinkAssignCfgUtilThresholdToActivateSec_Type(Integer32):
    """Custom type esiOrSecLinkAssignCfgUtilThresholdToActivateSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_EsiOrSecLinkAssignCfgUtilThresholdToActivateSec_Type.__name__ = "Integer32"
_EsiOrSecLinkAssignCfgUtilThresholdToActivateSec_Object = MibTableColumn
esiOrSecLinkAssignCfgUtilThresholdToActivateSec = _EsiOrSecLinkAssignCfgUtilThresholdToActivateSec_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 3, 1, 5),
    _EsiOrSecLinkAssignCfgUtilThresholdToActivateSec_Type()
)
esiOrSecLinkAssignCfgUtilThresholdToActivateSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiOrSecLinkAssignCfgUtilThresholdToActivateSec.setStatus("mandatory")


class _EsiOrSecLinkAssignCfgUtilThresholdToDeactivateSec_Type(Integer32):
    """Custom type esiOrSecLinkAssignCfgUtilThresholdToDeactivateSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_EsiOrSecLinkAssignCfgUtilThresholdToDeactivateSec_Type.__name__ = "Integer32"
_EsiOrSecLinkAssignCfgUtilThresholdToDeactivateSec_Object = MibTableColumn
esiOrSecLinkAssignCfgUtilThresholdToDeactivateSec = _EsiOrSecLinkAssignCfgUtilThresholdToDeactivateSec_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 3, 1, 6),
    _EsiOrSecLinkAssignCfgUtilThresholdToDeactivateSec_Type()
)
esiOrSecLinkAssignCfgUtilThresholdToDeactivateSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiOrSecLinkAssignCfgUtilThresholdToDeactivateSec.setStatus("mandatory")


class _EsiOrSecLinkAssignCfgTimeThresholdExceedToActivateSec_Type(Integer32):
    """Custom type esiOrSecLinkAssignCfgTimeThresholdExceedToActivateSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_EsiOrSecLinkAssignCfgTimeThresholdExceedToActivateSec_Type.__name__ = "Integer32"
_EsiOrSecLinkAssignCfgTimeThresholdExceedToActivateSec_Object = MibTableColumn
esiOrSecLinkAssignCfgTimeThresholdExceedToActivateSec = _EsiOrSecLinkAssignCfgTimeThresholdExceedToActivateSec_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 3, 1, 7),
    _EsiOrSecLinkAssignCfgTimeThresholdExceedToActivateSec_Type()
)
esiOrSecLinkAssignCfgTimeThresholdExceedToActivateSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiOrSecLinkAssignCfgTimeThresholdExceedToActivateSec.setStatus("mandatory")


class _EsiOrSecLinkAssignCfgTimeThresholdBelowToDeactivateSec_Type(Integer32):
    """Custom type esiOrSecLinkAssignCfgTimeThresholdBelowToDeactivateSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_EsiOrSecLinkAssignCfgTimeThresholdBelowToDeactivateSec_Type.__name__ = "Integer32"
_EsiOrSecLinkAssignCfgTimeThresholdBelowToDeactivateSec_Object = MibTableColumn
esiOrSecLinkAssignCfgTimeThresholdBelowToDeactivateSec = _EsiOrSecLinkAssignCfgTimeThresholdBelowToDeactivateSec_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 3, 1, 8),
    _EsiOrSecLinkAssignCfgTimeThresholdBelowToDeactivateSec_Type()
)
esiOrSecLinkAssignCfgTimeThresholdBelowToDeactivateSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiOrSecLinkAssignCfgTimeThresholdBelowToDeactivateSec.setStatus("mandatory")


class _EsiOrSecLinkAssignCfgTerminateCallonDeactivation_Type(Integer32):
    """Custom type esiOrSecLinkAssignCfgTerminateCallonDeactivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_EsiOrSecLinkAssignCfgTerminateCallonDeactivation_Type.__name__ = "Integer32"
_EsiOrSecLinkAssignCfgTerminateCallonDeactivation_Object = MibTableColumn
esiOrSecLinkAssignCfgTerminateCallonDeactivation = _EsiOrSecLinkAssignCfgTerminateCallonDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 3, 1, 9),
    _EsiOrSecLinkAssignCfgTerminateCallonDeactivation_Type()
)
esiOrSecLinkAssignCfgTerminateCallonDeactivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiOrSecLinkAssignCfgTerminateCallonDeactivation.setStatus("mandatory")
_EsiOrSecLinkTODActivationTable_Object = MibTable
esiOrSecLinkTODActivationTable = _EsiOrSecLinkTODActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 4)
)
if mibBuilder.loadTexts:
    esiOrSecLinkTODActivationTable.setStatus("mandatory")
_EsiOrSecLinkTODActivationEntry_Object = MibTableRow
esiOrSecLinkTODActivationEntry = _EsiOrSecLinkTODActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 4, 1)
)
esiOrSecLinkTODActivationEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "esiOrSecLinkTODActivationCardNumber"),
    (0, "MICOM-NODE-MIB", "esiOrSecLinkTODActivationChannelNumber"),
    (0, "MICOM-NODE-MIB", "esiOrSecLinkTODActivationSetSchedule"),
    (0, "MICOM-NODE-MIB", "esiOrSecLinkTODActivationTenMinInterval"),
)
if mibBuilder.loadTexts:
    esiOrSecLinkTODActivationEntry.setStatus("mandatory")
_EsiOrSecLinkTODActivationCardNumber_Type = Integer32
_EsiOrSecLinkTODActivationCardNumber_Object = MibTableColumn
esiOrSecLinkTODActivationCardNumber = _EsiOrSecLinkTODActivationCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 4, 1, 1),
    _EsiOrSecLinkTODActivationCardNumber_Type()
)
esiOrSecLinkTODActivationCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiOrSecLinkTODActivationCardNumber.setStatus("mandatory")
_EsiOrSecLinkTODActivationChannelNumber_Type = Integer32
_EsiOrSecLinkTODActivationChannelNumber_Object = MibTableColumn
esiOrSecLinkTODActivationChannelNumber = _EsiOrSecLinkTODActivationChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 4, 1, 2),
    _EsiOrSecLinkTODActivationChannelNumber_Type()
)
esiOrSecLinkTODActivationChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiOrSecLinkTODActivationChannelNumber.setStatus("mandatory")


class _EsiOrSecLinkTODActivationSetSchedule_Type(Integer32):
    """Custom type esiOrSecLinkTODActivationSetSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("saturday", 3),
          ("sunday", 1),
          ("weekdays", 2))
    )


_EsiOrSecLinkTODActivationSetSchedule_Type.__name__ = "Integer32"
_EsiOrSecLinkTODActivationSetSchedule_Object = MibTableColumn
esiOrSecLinkTODActivationSetSchedule = _EsiOrSecLinkTODActivationSetSchedule_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 4, 1, 3),
    _EsiOrSecLinkTODActivationSetSchedule_Type()
)
esiOrSecLinkTODActivationSetSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiOrSecLinkTODActivationSetSchedule.setStatus("mandatory")


class _EsiOrSecLinkTODActivationTenMinInterval_Type(Integer32):
    """Custom type esiOrSecLinkTODActivationTenMinInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 144),
    )


_EsiOrSecLinkTODActivationTenMinInterval_Type.__name__ = "Integer32"
_EsiOrSecLinkTODActivationTenMinInterval_Object = MibTableColumn
esiOrSecLinkTODActivationTenMinInterval = _EsiOrSecLinkTODActivationTenMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 4, 1, 4),
    _EsiOrSecLinkTODActivationTenMinInterval_Type()
)
esiOrSecLinkTODActivationTenMinInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiOrSecLinkTODActivationTenMinInterval.setStatus("mandatory")


class _EsiOrSecLinkTODActivationLinkState_Type(Integer32):
    """Custom type esiOrSecLinkTODActivationLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EsiOrSecLinkTODActivationLinkState_Type.__name__ = "Integer32"
_EsiOrSecLinkTODActivationLinkState_Object = MibTableColumn
esiOrSecLinkTODActivationLinkState = _EsiOrSecLinkTODActivationLinkState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 2, 4, 1, 5),
    _EsiOrSecLinkTODActivationLinkState_Type()
)
esiOrSecLinkTODActivationLinkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiOrSecLinkTODActivationLinkState.setStatus("mandatory")
_X_dot_21_link_ObjectIdentity = ObjectIdentity
x_dot_21_link = _X_dot_21_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3)
)
_X21LinkCfgTable_Object = MibTable
x21LinkCfgTable = _X21LinkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    x21LinkCfgTable.setStatus("mandatory")
_X21LinkCfgEntry_Object = MibTableRow
x21LinkCfgEntry = _X21LinkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 1, 1)
)
x21LinkCfgEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "x21LinkCfgCardNumber"),
    (0, "MICOM-NODE-MIB", "x21LinkCfgChannelNumber"),
)
if mibBuilder.loadTexts:
    x21LinkCfgEntry.setStatus("mandatory")
_X21LinkCfgCardNumber_Type = Integer32
_X21LinkCfgCardNumber_Object = MibTableColumn
x21LinkCfgCardNumber = _X21LinkCfgCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 1, 1, 1),
    _X21LinkCfgCardNumber_Type()
)
x21LinkCfgCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21LinkCfgCardNumber.setStatus("mandatory")
_X21LinkCfgChannelNumber_Type = Integer32
_X21LinkCfgChannelNumber_Object = MibTableColumn
x21LinkCfgChannelNumber = _X21LinkCfgChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 1, 1, 2),
    _X21LinkCfgChannelNumber_Type()
)
x21LinkCfgChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21LinkCfgChannelNumber.setStatus("mandatory")


class _X21LinkCfgLocalConnectMode_Type(Integer32):
    """Custom type x21LinkCfgLocalConnectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataActivityConnect", 1),
          ("dtrConnect", 2))
    )


_X21LinkCfgLocalConnectMode_Type.__name__ = "Integer32"
_X21LinkCfgLocalConnectMode_Object = MibTableColumn
x21LinkCfgLocalConnectMode = _X21LinkCfgLocalConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 1, 1, 3),
    _X21LinkCfgLocalConnectMode_Type()
)
x21LinkCfgLocalConnectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LinkCfgLocalConnectMode.setStatus("mandatory")


class _X21LinkCfgRemoteConnectMode_Type(Integer32):
    """Custom type x21LinkCfgRemoteConnectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataActivityConnect", 1),
          ("dtrConnect", 2))
    )


_X21LinkCfgRemoteConnectMode_Type.__name__ = "Integer32"
_X21LinkCfgRemoteConnectMode_Object = MibTableColumn
x21LinkCfgRemoteConnectMode = _X21LinkCfgRemoteConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 1, 1, 4),
    _X21LinkCfgRemoteConnectMode_Type()
)
x21LinkCfgRemoteConnectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LinkCfgRemoteConnectMode.setStatus("mandatory")


class _X21LinkCfgLocalConnectTimeout_Type(Integer32):
    """Custom type x21LinkCfgLocalConnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_X21LinkCfgLocalConnectTimeout_Type.__name__ = "Integer32"
_X21LinkCfgLocalConnectTimeout_Object = MibTableColumn
x21LinkCfgLocalConnectTimeout = _X21LinkCfgLocalConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 1, 1, 5),
    _X21LinkCfgLocalConnectTimeout_Type()
)
x21LinkCfgLocalConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LinkCfgLocalConnectTimeout.setStatus("mandatory")


class _X21LinkCfgRemoteConnectTimeout_Type(Integer32):
    """Custom type x21LinkCfgRemoteConnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_X21LinkCfgRemoteConnectTimeout_Type.__name__ = "Integer32"
_X21LinkCfgRemoteConnectTimeout_Object = MibTableColumn
x21LinkCfgRemoteConnectTimeout = _X21LinkCfgRemoteConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 1, 1, 6),
    _X21LinkCfgRemoteConnectTimeout_Type()
)
x21LinkCfgRemoteConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LinkCfgRemoteConnectTimeout.setStatus("mandatory")


class _X21LinkCfgLocalConnectRetries_Type(Integer32):
    """Custom type x21LinkCfgLocalConnectRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_X21LinkCfgLocalConnectRetries_Type.__name__ = "Integer32"
_X21LinkCfgLocalConnectRetries_Object = MibTableColumn
x21LinkCfgLocalConnectRetries = _X21LinkCfgLocalConnectRetries_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 1, 1, 7),
    _X21LinkCfgLocalConnectRetries_Type()
)
x21LinkCfgLocalConnectRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LinkCfgLocalConnectRetries.setStatus("mandatory")


class _X21LinkCfgRemoteConnectRetries_Type(Integer32):
    """Custom type x21LinkCfgRemoteConnectRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_X21LinkCfgRemoteConnectRetries_Type.__name__ = "Integer32"
_X21LinkCfgRemoteConnectRetries_Object = MibTableColumn
x21LinkCfgRemoteConnectRetries = _X21LinkCfgRemoteConnectRetries_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 1, 1, 8),
    _X21LinkCfgRemoteConnectRetries_Type()
)
x21LinkCfgRemoteConnectRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x21LinkCfgRemoteConnectRetries.setStatus("mandatory")
_X21LinkPreConfigTable_Object = MibTable
x21LinkPreConfigTable = _X21LinkPreConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    x21LinkPreConfigTable.setStatus("mandatory")
_X21LinkPreConfigEntry_Object = MibTableRow
x21LinkPreConfigEntry = _X21LinkPreConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 2, 1)
)
x21LinkPreConfigEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "x21LinkPreConfigCardNumber"),
    (0, "MICOM-NODE-MIB", "x21LinkPreConfigChannelNumber"),
)
if mibBuilder.loadTexts:
    x21LinkPreConfigEntry.setStatus("mandatory")


class _X21LinkPreConfigCardNumber_Type(Integer32):
    """Custom type x21LinkPreConfigCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_X21LinkPreConfigCardNumber_Type.__name__ = "Integer32"
_X21LinkPreConfigCardNumber_Object = MibTableColumn
x21LinkPreConfigCardNumber = _X21LinkPreConfigCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 2, 1, 1),
    _X21LinkPreConfigCardNumber_Type()
)
x21LinkPreConfigCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21LinkPreConfigCardNumber.setStatus("mandatory")


class _X21LinkPreConfigChannelNumber_Type(Integer32):
    """Custom type x21LinkPreConfigChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_X21LinkPreConfigChannelNumber_Type.__name__ = "Integer32"
_X21LinkPreConfigChannelNumber_Object = MibTableColumn
x21LinkPreConfigChannelNumber = _X21LinkPreConfigChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 2, 1, 2),
    _X21LinkPreConfigChannelNumber_Type()
)
x21LinkPreConfigChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x21LinkPreConfigChannelNumber.setStatus("mandatory")


class _X21LinkPreConfigLocalConnectMode_Type(Integer32):
    """Custom type x21LinkPreConfigLocalConnectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataActivityConnect", 1),
          ("dtrConnect", 2))
    )


_X21LinkPreConfigLocalConnectMode_Type.__name__ = "Integer32"
_X21LinkPreConfigLocalConnectMode_Object = MibTableColumn
x21LinkPreConfigLocalConnectMode = _X21LinkPreConfigLocalConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 2, 1, 3),
    _X21LinkPreConfigLocalConnectMode_Type()
)
x21LinkPreConfigLocalConnectMode.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    x21LinkPreConfigLocalConnectMode.setStatus("mandatory")


class _X21LinkPreConfigRemoteConnectMode_Type(Integer32):
    """Custom type x21LinkPreConfigRemoteConnectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataActivityConnect", 1),
          ("dtrConnect", 2))
    )


_X21LinkPreConfigRemoteConnectMode_Type.__name__ = "Integer32"
_X21LinkPreConfigRemoteConnectMode_Object = MibTableColumn
x21LinkPreConfigRemoteConnectMode = _X21LinkPreConfigRemoteConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 2, 1, 4),
    _X21LinkPreConfigRemoteConnectMode_Type()
)
x21LinkPreConfigRemoteConnectMode.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    x21LinkPreConfigRemoteConnectMode.setStatus("mandatory")


class _X21LinkPreConfigLocalConnectTimeout_Type(Integer32):
    """Custom type x21LinkPreConfigLocalConnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_X21LinkPreConfigLocalConnectTimeout_Type.__name__ = "Integer32"
_X21LinkPreConfigLocalConnectTimeout_Object = MibTableColumn
x21LinkPreConfigLocalConnectTimeout = _X21LinkPreConfigLocalConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 2, 1, 5),
    _X21LinkPreConfigLocalConnectTimeout_Type()
)
x21LinkPreConfigLocalConnectTimeout.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    x21LinkPreConfigLocalConnectTimeout.setStatus("mandatory")


class _X21LinkPreConfigRemoteConnectTimeout_Type(Integer32):
    """Custom type x21LinkPreConfigRemoteConnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_X21LinkPreConfigRemoteConnectTimeout_Type.__name__ = "Integer32"
_X21LinkPreConfigRemoteConnectTimeout_Object = MibTableColumn
x21LinkPreConfigRemoteConnectTimeout = _X21LinkPreConfigRemoteConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 2, 1, 6),
    _X21LinkPreConfigRemoteConnectTimeout_Type()
)
x21LinkPreConfigRemoteConnectTimeout.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    x21LinkPreConfigRemoteConnectTimeout.setStatus("mandatory")


class _X21LinkPreConfigLocalConnectRetries_Type(Integer32):
    """Custom type x21LinkPreConfigLocalConnectRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_X21LinkPreConfigLocalConnectRetries_Type.__name__ = "Integer32"
_X21LinkPreConfigLocalConnectRetries_Object = MibTableColumn
x21LinkPreConfigLocalConnectRetries = _X21LinkPreConfigLocalConnectRetries_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 2, 1, 7),
    _X21LinkPreConfigLocalConnectRetries_Type()
)
x21LinkPreConfigLocalConnectRetries.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    x21LinkPreConfigLocalConnectRetries.setStatus("mandatory")


class _X21LinkPreConfigRemoteConnectRetries_Type(Integer32):
    """Custom type x21LinkPreConfigRemoteConnectRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_X21LinkPreConfigRemoteConnectRetries_Type.__name__ = "Integer32"
_X21LinkPreConfigRemoteConnectRetries_Object = MibTableColumn
x21LinkPreConfigRemoteConnectRetries = _X21LinkPreConfigRemoteConnectRetries_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 3, 2, 1, 8),
    _X21LinkPreConfigRemoteConnectRetries_Type()
)
x21LinkPreConfigRemoteConnectRetries.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    x21LinkPreConfigRemoteConnectRetries.setStatus("mandatory")
_Local_esi_link_ObjectIdentity = ObjectIdentity
local_esi_link = _Local_esi_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 4)
)
_LocalESILinkCfgTable_Object = MibTable
localESILinkCfgTable = _LocalESILinkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 4, 1)
)
if mibBuilder.loadTexts:
    localESILinkCfgTable.setStatus("mandatory")
_LocalESILinkCfgEntry_Object = MibTableRow
localESILinkCfgEntry = _LocalESILinkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 4, 1, 1)
)
localESILinkCfgEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "localESILinkCfgCardNumber"),
    (0, "MICOM-NODE-MIB", "localESILinkCfgChannelNumber"),
)
if mibBuilder.loadTexts:
    localESILinkCfgEntry.setStatus("mandatory")


class _LocalESILinkCfgCardNumber_Type(Integer32):
    """Custom type localESILinkCfgCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_LocalESILinkCfgCardNumber_Type.__name__ = "Integer32"
_LocalESILinkCfgCardNumber_Object = MibTableColumn
localESILinkCfgCardNumber = _LocalESILinkCfgCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 4, 1, 1, 1),
    _LocalESILinkCfgCardNumber_Type()
)
localESILinkCfgCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localESILinkCfgCardNumber.setStatus("mandatory")


class _LocalESILinkCfgChannelNumber_Type(Integer32):
    """Custom type localESILinkCfgChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_LocalESILinkCfgChannelNumber_Type.__name__ = "Integer32"
_LocalESILinkCfgChannelNumber_Object = MibTableColumn
localESILinkCfgChannelNumber = _LocalESILinkCfgChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 4, 1, 1, 2),
    _LocalESILinkCfgChannelNumber_Type()
)
localESILinkCfgChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localESILinkCfgChannelNumber.setStatus("mandatory")


class _LocalESILinkCfgDataRate_Type(Integer32):
    """Custom type localESILinkCfgDataRate based on Integer32"""
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
        *(("external", 1),
          ("rate126000", 3),
          ("rate192000", 4),
          ("rate252000", 5),
          ("rate64000", 2))
    )


_LocalESILinkCfgDataRate_Type.__name__ = "Integer32"
_LocalESILinkCfgDataRate_Object = MibTableColumn
localESILinkCfgDataRate = _LocalESILinkCfgDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 4, 1, 1, 3),
    _LocalESILinkCfgDataRate_Type()
)
localESILinkCfgDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localESILinkCfgDataRate.setStatus("mandatory")
_Esi_secondary_link_ObjectIdentity = ObjectIdentity
esi_secondary_link = _Esi_secondary_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5)
)
_EsiSecLinkCfgTable_Object = MibTable
esiSecLinkCfgTable = _EsiSecLinkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5, 1)
)
if mibBuilder.loadTexts:
    esiSecLinkCfgTable.setStatus("mandatory")
_EsiSecLinkCfgEntry_Object = MibTableRow
esiSecLinkCfgEntry = _EsiSecLinkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5, 1, 1)
)
esiSecLinkCfgEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "esiSecLinkCfgCardNumber"),
    (0, "MICOM-NODE-MIB", "esiSecLinkCfgChannelNumber"),
)
if mibBuilder.loadTexts:
    esiSecLinkCfgEntry.setStatus("mandatory")


class _EsiSecLinkCfgCardNumber_Type(Integer32):
    """Custom type esiSecLinkCfgCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_EsiSecLinkCfgCardNumber_Type.__name__ = "Integer32"
_EsiSecLinkCfgCardNumber_Object = MibTableColumn
esiSecLinkCfgCardNumber = _EsiSecLinkCfgCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5, 1, 1, 1),
    _EsiSecLinkCfgCardNumber_Type()
)
esiSecLinkCfgCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiSecLinkCfgCardNumber.setStatus("mandatory")


class _EsiSecLinkCfgChannelNumber_Type(Integer32):
    """Custom type esiSecLinkCfgChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_EsiSecLinkCfgChannelNumber_Type.__name__ = "Integer32"
_EsiSecLinkCfgChannelNumber_Object = MibTableColumn
esiSecLinkCfgChannelNumber = _EsiSecLinkCfgChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5, 1, 1, 2),
    _EsiSecLinkCfgChannelNumber_Type()
)
esiSecLinkCfgChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiSecLinkCfgChannelNumber.setStatus("mandatory")


class _EsiSecLinkCfgDataRate_Type(Integer32):
    """Custom type esiSecLinkCfgDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("rate12000Sync", 5),
          ("rate14400Sync", 6),
          ("rate16800Sync", 7),
          ("rate19200Sync", 8),
          ("rate2400Sync", 2),
          ("rate38400Sync", 9),
          ("rate4800Sync", 3),
          ("rate56000Sync", 10),
          ("rate64000Sync", 11),
          ("rate9600Sync", 4))
    )


_EsiSecLinkCfgDataRate_Type.__name__ = "Integer32"
_EsiSecLinkCfgDataRate_Object = MibTableColumn
esiSecLinkCfgDataRate = _EsiSecLinkCfgDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5, 1, 1, 3),
    _EsiSecLinkCfgDataRate_Type()
)
esiSecLinkCfgDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiSecLinkCfgDataRate.setStatus("mandatory")
_EsiSecLinkAssignmentTable_Object = MibTable
esiSecLinkAssignmentTable = _EsiSecLinkAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5, 2)
)
if mibBuilder.loadTexts:
    esiSecLinkAssignmentTable.setStatus("mandatory")
_EsiSecLinkAssignmentEntry_Object = MibTableRow
esiSecLinkAssignmentEntry = _EsiSecLinkAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5, 2, 1)
)
esiSecLinkAssignmentEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "esiSecLinkAssignmentSecCardNumber"),
    (0, "MICOM-NODE-MIB", "esiSecLinkAssignmentSecChannelNumber"),
)
if mibBuilder.loadTexts:
    esiSecLinkAssignmentEntry.setStatus("mandatory")
_EsiSecLinkAssignmentSecCardNumber_Type = Integer32
_EsiSecLinkAssignmentSecCardNumber_Object = MibTableColumn
esiSecLinkAssignmentSecCardNumber = _EsiSecLinkAssignmentSecCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5, 2, 1, 1),
    _EsiSecLinkAssignmentSecCardNumber_Type()
)
esiSecLinkAssignmentSecCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiSecLinkAssignmentSecCardNumber.setStatus("mandatory")
_EsiSecLinkAssignmentSecChannelNumber_Type = Integer32
_EsiSecLinkAssignmentSecChannelNumber_Object = MibTableColumn
esiSecLinkAssignmentSecChannelNumber = _EsiSecLinkAssignmentSecChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5, 2, 1, 2),
    _EsiSecLinkAssignmentSecChannelNumber_Type()
)
esiSecLinkAssignmentSecChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiSecLinkAssignmentSecChannelNumber.setStatus("mandatory")


class _EsiSecLinkAssignmentEntryAction_Type(Integer32):
    """Custom type esiSecLinkAssignmentEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_EsiSecLinkAssignmentEntryAction_Type.__name__ = "Integer32"
_EsiSecLinkAssignmentEntryAction_Object = MibTableColumn
esiSecLinkAssignmentEntryAction = _EsiSecLinkAssignmentEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5, 2, 1, 3),
    _EsiSecLinkAssignmentEntryAction_Type()
)
esiSecLinkAssignmentEntryAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    esiSecLinkAssignmentEntryAction.setStatus("mandatory")
_EsiSecLinkAssignmentPriCardNumber_Type = Integer32
_EsiSecLinkAssignmentPriCardNumber_Object = MibTableColumn
esiSecLinkAssignmentPriCardNumber = _EsiSecLinkAssignmentPriCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5, 2, 1, 4),
    _EsiSecLinkAssignmentPriCardNumber_Type()
)
esiSecLinkAssignmentPriCardNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiSecLinkAssignmentPriCardNumber.setStatus("mandatory")
_EsiSecLinkAssignmentPriChannelNumber_Type = Integer32
_EsiSecLinkAssignmentPriChannelNumber_Object = MibTableColumn
esiSecLinkAssignmentPriChannelNumber = _EsiSecLinkAssignmentPriChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 5, 2, 1, 5),
    _EsiSecLinkAssignmentPriChannelNumber_Type()
)
esiSecLinkAssignmentPriChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiSecLinkAssignmentPriChannelNumber.setStatus("mandatory")
_Frame_relay_link_ObjectIdentity = ObjectIdentity
frame_relay_link = _Frame_relay_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6)
)
_FrameRelayLinkCfgTable_Object = MibTable
frameRelayLinkCfgTable = _FrameRelayLinkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1)
)
if mibBuilder.loadTexts:
    frameRelayLinkCfgTable.setStatus("mandatory")
_FrameRelayLinkCfgEntry_Object = MibTableRow
frameRelayLinkCfgEntry = _FrameRelayLinkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1)
)
frameRelayLinkCfgEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "frameRelayLinkCfgCardNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayLinkCfgChannelNumber"),
)
if mibBuilder.loadTexts:
    frameRelayLinkCfgEntry.setStatus("mandatory")
_FrameRelayLinkCfgCardNumber_Type = Integer32
_FrameRelayLinkCfgCardNumber_Object = MibTableColumn
frameRelayLinkCfgCardNumber = _FrameRelayLinkCfgCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 1),
    _FrameRelayLinkCfgCardNumber_Type()
)
frameRelayLinkCfgCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkCfgCardNumber.setStatus("mandatory")
_FrameRelayLinkCfgChannelNumber_Type = Integer32
_FrameRelayLinkCfgChannelNumber_Object = MibTableColumn
frameRelayLinkCfgChannelNumber = _FrameRelayLinkCfgChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 2),
    _FrameRelayLinkCfgChannelNumber_Type()
)
frameRelayLinkCfgChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkCfgChannelNumber.setStatus("mandatory")


class _FrameRelayLinkCfgDataRate_Type(Integer32):
    """Custom type frameRelayLinkCfgDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("rate126000", 4),
          ("rate126400", 5),
          ("rate128000", 6),
          ("rate189500", 7),
          ("rate19200", 2),
          ("rate192000", 8),
          ("rate246400", 9),
          ("rate252000", 10),
          ("rate256000", 11),
          ("rate308000", 12),
          ("rate310200", 13),
          ("rate336000", 14),
          ("rate366500", 15),
          ("rate379100", 16),
          ("rate384000", 17),
          ("rate448000", 18),
          ("rate492800", 19),
          ("rate504000", 20),
          ("rate537600", 21),
          ("rate64000", 3),
          ("rate9600", 1))
    )


_FrameRelayLinkCfgDataRate_Type.__name__ = "Integer32"
_FrameRelayLinkCfgDataRate_Object = MibTableColumn
frameRelayLinkCfgDataRate = _FrameRelayLinkCfgDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 3),
    _FrameRelayLinkCfgDataRate_Type()
)
frameRelayLinkCfgDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgDataRate.setStatus("mandatory")


class _FrameRelayLinkCfgLocalMgmtProtocol_Type(Integer32):
    """Custom type frameRelayLinkCfgLocalMgmtProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annexD", 2),
          ("lmi", 3),
          ("none", 1))
    )


_FrameRelayLinkCfgLocalMgmtProtocol_Type.__name__ = "Integer32"
_FrameRelayLinkCfgLocalMgmtProtocol_Object = MibTableColumn
frameRelayLinkCfgLocalMgmtProtocol = _FrameRelayLinkCfgLocalMgmtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 4),
    _FrameRelayLinkCfgLocalMgmtProtocol_Type()
)
frameRelayLinkCfgLocalMgmtProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgLocalMgmtProtocol.setStatus("mandatory")


class _FrameRelayLinkCfgFullStatusPollingCounter_Type(Integer32):
    """Custom type frameRelayLinkCfgFullStatusPollingCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrameRelayLinkCfgFullStatusPollingCounter_Type.__name__ = "Integer32"
_FrameRelayLinkCfgFullStatusPollingCounter_Object = MibTableColumn
frameRelayLinkCfgFullStatusPollingCounter = _FrameRelayLinkCfgFullStatusPollingCounter_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 5),
    _FrameRelayLinkCfgFullStatusPollingCounter_Type()
)
frameRelayLinkCfgFullStatusPollingCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgFullStatusPollingCounter.setStatus("mandatory")


class _FrameRelayLinkCfgErrorThreshold_Type(Integer32):
    """Custom type frameRelayLinkCfgErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrameRelayLinkCfgErrorThreshold_Type.__name__ = "Integer32"
_FrameRelayLinkCfgErrorThreshold_Object = MibTableColumn
frameRelayLinkCfgErrorThreshold = _FrameRelayLinkCfgErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 6),
    _FrameRelayLinkCfgErrorThreshold_Type()
)
frameRelayLinkCfgErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgErrorThreshold.setStatus("mandatory")


class _FrameRelayLinkCfgEventCount_Type(Integer32):
    """Custom type frameRelayLinkCfgEventCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrameRelayLinkCfgEventCount_Type.__name__ = "Integer32"
_FrameRelayLinkCfgEventCount_Object = MibTableColumn
frameRelayLinkCfgEventCount = _FrameRelayLinkCfgEventCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 7),
    _FrameRelayLinkCfgEventCount_Type()
)
frameRelayLinkCfgEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgEventCount.setStatus("mandatory")


class _FrameRelayLinkCfgLinkIntegrityVerificationTimer_Type(Integer32):
    """Custom type frameRelayLinkCfgLinkIntegrityVerificationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrameRelayLinkCfgLinkIntegrityVerificationTimer_Type.__name__ = "Integer32"
_FrameRelayLinkCfgLinkIntegrityVerificationTimer_Object = MibTableColumn
frameRelayLinkCfgLinkIntegrityVerificationTimer = _FrameRelayLinkCfgLinkIntegrityVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 8),
    _FrameRelayLinkCfgLinkIntegrityVerificationTimer_Type()
)
frameRelayLinkCfgLinkIntegrityVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgLinkIntegrityVerificationTimer.setStatus("mandatory")


class _FrameRelayLinkCfgPollingVerificationTimer_Type(Integer32):
    """Custom type frameRelayLinkCfgPollingVerificationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrameRelayLinkCfgPollingVerificationTimer_Type.__name__ = "Integer32"
_FrameRelayLinkCfgPollingVerificationTimer_Object = MibTableColumn
frameRelayLinkCfgPollingVerificationTimer = _FrameRelayLinkCfgPollingVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 9),
    _FrameRelayLinkCfgPollingVerificationTimer_Type()
)
frameRelayLinkCfgPollingVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgPollingVerificationTimer.setStatus("mandatory")


class _FrameRelayLinkCfgMaxFrameSize_Type(Integer32):
    """Custom type frameRelayLinkCfgMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8189),
    )


_FrameRelayLinkCfgMaxFrameSize_Type.__name__ = "Integer32"
_FrameRelayLinkCfgMaxFrameSize_Object = MibTableColumn
frameRelayLinkCfgMaxFrameSize = _FrameRelayLinkCfgMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 10),
    _FrameRelayLinkCfgMaxFrameSize_Type()
)
frameRelayLinkCfgMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgMaxFrameSize.setStatus("mandatory")


class _FrameRelayLinkCfgRxClockingSource_Type(Integer32):
    """Custom type frameRelayLinkCfgRxClockingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2))
    )


_FrameRelayLinkCfgRxClockingSource_Type.__name__ = "Integer32"
_FrameRelayLinkCfgRxClockingSource_Object = MibTableColumn
frameRelayLinkCfgRxClockingSource = _FrameRelayLinkCfgRxClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 11),
    _FrameRelayLinkCfgRxClockingSource_Type()
)
frameRelayLinkCfgRxClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgRxClockingSource.setStatus("mandatory")


class _FrameRelayLinkCfgTxClockingSource_Type(Integer32):
    """Custom type frameRelayLinkCfgTxClockingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2))
    )


_FrameRelayLinkCfgTxClockingSource_Type.__name__ = "Integer32"
_FrameRelayLinkCfgTxClockingSource_Object = MibTableColumn
frameRelayLinkCfgTxClockingSource = _FrameRelayLinkCfgTxClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 12),
    _FrameRelayLinkCfgTxClockingSource_Type()
)
frameRelayLinkCfgTxClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgTxClockingSource.setStatus("mandatory")


class _FrameRelayLinkCfgNetworkAddress_Type(OctetString):
    """Custom type frameRelayLinkCfgNetworkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FrameRelayLinkCfgNetworkAddress_Type.__name__ = "OctetString"
_FrameRelayLinkCfgNetworkAddress_Object = MibTableColumn
frameRelayLinkCfgNetworkAddress = _FrameRelayLinkCfgNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 13),
    _FrameRelayLinkCfgNetworkAddress_Type()
)
frameRelayLinkCfgNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgNetworkAddress.setStatus("mandatory")


class _FrameRelayLinkCfgAccessLinkMode_Type(Integer32):
    """Custom type frameRelayLinkCfgAccessLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("networkMode", 2),
          ("userEquipmentMode", 1))
    )


_FrameRelayLinkCfgAccessLinkMode_Type.__name__ = "Integer32"
_FrameRelayLinkCfgAccessLinkMode_Object = MibTableColumn
frameRelayLinkCfgAccessLinkMode = _FrameRelayLinkCfgAccessLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 1, 1, 14),
    _FrameRelayLinkCfgAccessLinkMode_Type()
)
frameRelayLinkCfgAccessLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgAccessLinkMode.setStatus("mandatory")
_FrameRelayLinkCfgDLCITable_Object = MibTable
frameRelayLinkCfgDLCITable = _FrameRelayLinkCfgDLCITable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 2)
)
if mibBuilder.loadTexts:
    frameRelayLinkCfgDLCITable.setStatus("mandatory")
_FrameRelayLinkCfgDLCIEntry_Object = MibTableRow
frameRelayLinkCfgDLCIEntry = _FrameRelayLinkCfgDLCIEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 2, 1)
)
frameRelayLinkCfgDLCIEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "frameRelayLinkCfgDLCICardNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayLinkCfgDLCIChannelNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayLinkCfgDLCINumber"),
)
if mibBuilder.loadTexts:
    frameRelayLinkCfgDLCIEntry.setStatus("mandatory")
_FrameRelayLinkCfgDLCICardNumber_Type = Integer32
_FrameRelayLinkCfgDLCICardNumber_Object = MibTableColumn
frameRelayLinkCfgDLCICardNumber = _FrameRelayLinkCfgDLCICardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 2, 1, 1),
    _FrameRelayLinkCfgDLCICardNumber_Type()
)
frameRelayLinkCfgDLCICardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkCfgDLCICardNumber.setStatus("mandatory")
_FrameRelayLinkCfgDLCIChannelNumber_Type = Integer32
_FrameRelayLinkCfgDLCIChannelNumber_Object = MibTableColumn
frameRelayLinkCfgDLCIChannelNumber = _FrameRelayLinkCfgDLCIChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 2, 1, 2),
    _FrameRelayLinkCfgDLCIChannelNumber_Type()
)
frameRelayLinkCfgDLCIChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkCfgDLCIChannelNumber.setStatus("mandatory")
_FrameRelayLinkCfgDLCINumber_Type = Integer32
_FrameRelayLinkCfgDLCINumber_Object = MibTableColumn
frameRelayLinkCfgDLCINumber = _FrameRelayLinkCfgDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 2, 1, 3),
    _FrameRelayLinkCfgDLCINumber_Type()
)
frameRelayLinkCfgDLCINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkCfgDLCINumber.setStatus("mandatory")


class _FrameRelayLinkCfgDLCIType_Type(Integer32):
    """Custom type frameRelayLinkCfgDLCIType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("annexDType", 2),
          ("fragmentation", 6),
          ("lmi", 4),
          ("transparent", 5),
          ("undefined", 1),
          ("virtualLink", 3))
    )


_FrameRelayLinkCfgDLCIType_Type.__name__ = "Integer32"
_FrameRelayLinkCfgDLCIType_Object = MibTableColumn
frameRelayLinkCfgDLCIType = _FrameRelayLinkCfgDLCIType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 2, 1, 4),
    _FrameRelayLinkCfgDLCIType_Type()
)
frameRelayLinkCfgDLCIType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkCfgDLCIType.setStatus("mandatory")


class _FrameRelayLinkCfgDLCICommittedInfoRateForward_Type(Integer32):
    """Custom type frameRelayLinkCfgDLCICommittedInfoRateForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_FrameRelayLinkCfgDLCICommittedInfoRateForward_Type.__name__ = "Integer32"
_FrameRelayLinkCfgDLCICommittedInfoRateForward_Object = MibTableColumn
frameRelayLinkCfgDLCICommittedInfoRateForward = _FrameRelayLinkCfgDLCICommittedInfoRateForward_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 2, 1, 5),
    _FrameRelayLinkCfgDLCICommittedInfoRateForward_Type()
)
frameRelayLinkCfgDLCICommittedInfoRateForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgDLCICommittedInfoRateForward.setStatus("mandatory")


class _FrameRelayLinkCfgDLCICommittedInfoRateBackward_Type(Integer32):
    """Custom type frameRelayLinkCfgDLCICommittedInfoRateBackward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_FrameRelayLinkCfgDLCICommittedInfoRateBackward_Type.__name__ = "Integer32"
_FrameRelayLinkCfgDLCICommittedInfoRateBackward_Object = MibTableColumn
frameRelayLinkCfgDLCICommittedInfoRateBackward = _FrameRelayLinkCfgDLCICommittedInfoRateBackward_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 2, 1, 6),
    _FrameRelayLinkCfgDLCICommittedInfoRateBackward_Type()
)
frameRelayLinkCfgDLCICommittedInfoRateBackward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgDLCICommittedInfoRateBackward.setStatus("mandatory")


class _FrameRelayLinkCfgDLCICommittedBurstSizeForward_Type(Integer32):
    """Custom type frameRelayLinkCfgDLCICommittedBurstSizeForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_FrameRelayLinkCfgDLCICommittedBurstSizeForward_Type.__name__ = "Integer32"
_FrameRelayLinkCfgDLCICommittedBurstSizeForward_Object = MibTableColumn
frameRelayLinkCfgDLCICommittedBurstSizeForward = _FrameRelayLinkCfgDLCICommittedBurstSizeForward_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 2, 1, 7),
    _FrameRelayLinkCfgDLCICommittedBurstSizeForward_Type()
)
frameRelayLinkCfgDLCICommittedBurstSizeForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgDLCICommittedBurstSizeForward.setStatus("mandatory")


class _FrameRelayLinkCfgDLCICommittedBurstSizeBackward_Type(Integer32):
    """Custom type frameRelayLinkCfgDLCICommittedBurstSizeBackward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_FrameRelayLinkCfgDLCICommittedBurstSizeBackward_Type.__name__ = "Integer32"
_FrameRelayLinkCfgDLCICommittedBurstSizeBackward_Object = MibTableColumn
frameRelayLinkCfgDLCICommittedBurstSizeBackward = _FrameRelayLinkCfgDLCICommittedBurstSizeBackward_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 2, 1, 8),
    _FrameRelayLinkCfgDLCICommittedBurstSizeBackward_Type()
)
frameRelayLinkCfgDLCICommittedBurstSizeBackward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgDLCICommittedBurstSizeBackward.setStatus("mandatory")


class _FrameRelayLinkCfgDLCIExcessBurstSizeForward_Type(Integer32):
    """Custom type frameRelayLinkCfgDLCIExcessBurstSizeForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_FrameRelayLinkCfgDLCIExcessBurstSizeForward_Type.__name__ = "Integer32"
_FrameRelayLinkCfgDLCIExcessBurstSizeForward_Object = MibTableColumn
frameRelayLinkCfgDLCIExcessBurstSizeForward = _FrameRelayLinkCfgDLCIExcessBurstSizeForward_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 2, 1, 9),
    _FrameRelayLinkCfgDLCIExcessBurstSizeForward_Type()
)
frameRelayLinkCfgDLCIExcessBurstSizeForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgDLCIExcessBurstSizeForward.setStatus("mandatory")


class _FrameRelayLinkCfgDLCIExcessBurstSizeBackward_Type(Integer32):
    """Custom type frameRelayLinkCfgDLCIExcessBurstSizeBackward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_FrameRelayLinkCfgDLCIExcessBurstSizeBackward_Type.__name__ = "Integer32"
_FrameRelayLinkCfgDLCIExcessBurstSizeBackward_Object = MibTableColumn
frameRelayLinkCfgDLCIExcessBurstSizeBackward = _FrameRelayLinkCfgDLCIExcessBurstSizeBackward_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 2, 1, 10),
    _FrameRelayLinkCfgDLCIExcessBurstSizeBackward_Type()
)
frameRelayLinkCfgDLCIExcessBurstSizeBackward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayLinkCfgDLCIExcessBurstSizeBackward.setStatus("mandatory")
_FrameRelayLinkControlTable_Object = MibTable
frameRelayLinkControlTable = _FrameRelayLinkControlTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 3)
)
if mibBuilder.loadTexts:
    frameRelayLinkControlTable.setStatus("mandatory")
_FrameRelayLinkControlEntry_Object = MibTableRow
frameRelayLinkControlEntry = _FrameRelayLinkControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 3, 1)
)
frameRelayLinkControlEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "frameRelayLinkControlLinkCardNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayLinkControlLinkChannelNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayLinkControlDLCINumber"),
)
if mibBuilder.loadTexts:
    frameRelayLinkControlEntry.setStatus("mandatory")
_FrameRelayLinkControlLinkCardNumber_Type = Integer32
_FrameRelayLinkControlLinkCardNumber_Object = MibTableColumn
frameRelayLinkControlLinkCardNumber = _FrameRelayLinkControlLinkCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 3, 1, 1),
    _FrameRelayLinkControlLinkCardNumber_Type()
)
frameRelayLinkControlLinkCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkControlLinkCardNumber.setStatus("mandatory")
_FrameRelayLinkControlLinkChannelNumber_Type = Integer32
_FrameRelayLinkControlLinkChannelNumber_Object = MibTableColumn
frameRelayLinkControlLinkChannelNumber = _FrameRelayLinkControlLinkChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 3, 1, 2),
    _FrameRelayLinkControlLinkChannelNumber_Type()
)
frameRelayLinkControlLinkChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkControlLinkChannelNumber.setStatus("mandatory")


class _FrameRelayLinkControlDLCINumber_Type(Integer32):
    """Custom type frameRelayLinkControlDLCINumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_FrameRelayLinkControlDLCINumber_Type.__name__ = "Integer32"
_FrameRelayLinkControlDLCINumber_Object = MibTableColumn
frameRelayLinkControlDLCINumber = _FrameRelayLinkControlDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 3, 1, 3),
    _FrameRelayLinkControlDLCINumber_Type()
)
frameRelayLinkControlDLCINumber.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frameRelayLinkControlDLCINumber.setStatus("mandatory")


class _FrameRelayLinkControlCommand_Type(Integer32):
    """Custom type frameRelayLinkControlCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addDLCI", 1),
          ("deleteDLCI", 2))
    )


_FrameRelayLinkControlCommand_Type.__name__ = "Integer32"
_FrameRelayLinkControlCommand_Object = MibTableColumn
frameRelayLinkControlCommand = _FrameRelayLinkControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 3, 1, 4),
    _FrameRelayLinkControlCommand_Type()
)
frameRelayLinkControlCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frameRelayLinkControlCommand.setStatus("mandatory")


class _FrameRelayLinkControlDLCIType_Type(Integer32):
    """Custom type frameRelayLinkControlDLCIType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fragmentation", 3),
          ("transparent", 2),
          ("virtualLink", 1))
    )


_FrameRelayLinkControlDLCIType_Type.__name__ = "Integer32"
_FrameRelayLinkControlDLCIType_Object = MibTableColumn
frameRelayLinkControlDLCIType = _FrameRelayLinkControlDLCIType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 3, 1, 5),
    _FrameRelayLinkControlDLCIType_Type()
)
frameRelayLinkControlDLCIType.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frameRelayLinkControlDLCIType.setStatus("mandatory")
_FrameRelayDLCIControlTable_Object = MibTable
frameRelayDLCIControlTable = _FrameRelayDLCIControlTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 4)
)
if mibBuilder.loadTexts:
    frameRelayDLCIControlTable.setStatus("mandatory")
_FrameRelayDLCIControlEntry_Object = MibTableRow
frameRelayDLCIControlEntry = _FrameRelayDLCIControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 4, 1)
)
frameRelayDLCIControlEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "frameRelayDLCIControlLinkCardNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayDLCIControlLinkChannelNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayDLCIControlDLCINumber"),
)
if mibBuilder.loadTexts:
    frameRelayDLCIControlEntry.setStatus("mandatory")
_FrameRelayDLCIControlLinkCardNumber_Type = Integer32
_FrameRelayDLCIControlLinkCardNumber_Object = MibTableColumn
frameRelayDLCIControlLinkCardNumber = _FrameRelayDLCIControlLinkCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 4, 1, 1),
    _FrameRelayDLCIControlLinkCardNumber_Type()
)
frameRelayDLCIControlLinkCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDLCIControlLinkCardNumber.setStatus("mandatory")
_FrameRelayDLCIControlLinkChannelNumber_Type = Integer32
_FrameRelayDLCIControlLinkChannelNumber_Object = MibTableColumn
frameRelayDLCIControlLinkChannelNumber = _FrameRelayDLCIControlLinkChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 4, 1, 2),
    _FrameRelayDLCIControlLinkChannelNumber_Type()
)
frameRelayDLCIControlLinkChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDLCIControlLinkChannelNumber.setStatus("mandatory")


class _FrameRelayDLCIControlDLCINumber_Type(Integer32):
    """Custom type frameRelayDLCIControlDLCINumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_FrameRelayDLCIControlDLCINumber_Type.__name__ = "Integer32"
_FrameRelayDLCIControlDLCINumber_Object = MibTableColumn
frameRelayDLCIControlDLCINumber = _FrameRelayDLCIControlDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 4, 1, 3),
    _FrameRelayDLCIControlDLCINumber_Type()
)
frameRelayDLCIControlDLCINumber.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frameRelayDLCIControlDLCINumber.setStatus("mandatory")


class _FrameRelayDLCIControlCommand_Type(Integer32):
    """Custom type frameRelayDLCIControlCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connectDLCI", 1),
          ("disconnectDLCI", 2))
    )


_FrameRelayDLCIControlCommand_Type.__name__ = "Integer32"
_FrameRelayDLCIControlCommand_Object = MibTableColumn
frameRelayDLCIControlCommand = _FrameRelayDLCIControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 4, 1, 4),
    _FrameRelayDLCIControlCommand_Type()
)
frameRelayDLCIControlCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frameRelayDLCIControlCommand.setStatus("mandatory")


class _FrameRelayDLCIControlFconnNodeName_Type(DisplayString):
    """Custom type frameRelayDLCIControlFconnNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FrameRelayDLCIControlFconnNodeName_Type.__name__ = "DisplayString"
_FrameRelayDLCIControlFconnNodeName_Object = MibTableColumn
frameRelayDLCIControlFconnNodeName = _FrameRelayDLCIControlFconnNodeName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 4, 1, 5),
    _FrameRelayDLCIControlFconnNodeName_Type()
)
frameRelayDLCIControlFconnNodeName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frameRelayDLCIControlFconnNodeName.setStatus("mandatory")
_FrameRelayDLCIControlFconnCardNumber_Type = Integer32
_FrameRelayDLCIControlFconnCardNumber_Object = MibTableColumn
frameRelayDLCIControlFconnCardNumber = _FrameRelayDLCIControlFconnCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 4, 1, 6),
    _FrameRelayDLCIControlFconnCardNumber_Type()
)
frameRelayDLCIControlFconnCardNumber.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frameRelayDLCIControlFconnCardNumber.setStatus("mandatory")
_FrameRelayDLCIControlFconnChannelNumber_Type = Integer32
_FrameRelayDLCIControlFconnChannelNumber_Object = MibTableColumn
frameRelayDLCIControlFconnChannelNumber = _FrameRelayDLCIControlFconnChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 4, 1, 7),
    _FrameRelayDLCIControlFconnChannelNumber_Type()
)
frameRelayDLCIControlFconnChannelNumber.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frameRelayDLCIControlFconnChannelNumber.setStatus("mandatory")
_FrameRelayDLCIControlFconnDLCINumber_Type = Integer32
_FrameRelayDLCIControlFconnDLCINumber_Object = MibTableColumn
frameRelayDLCIControlFconnDLCINumber = _FrameRelayDLCIControlFconnDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 4, 1, 8),
    _FrameRelayDLCIControlFconnDLCINumber_Type()
)
frameRelayDLCIControlFconnDLCINumber.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frameRelayDLCIControlFconnDLCINumber.setStatus("mandatory")
_FrameRelayDLCIConnectsTable_Object = MibTable
frameRelayDLCIConnectsTable = _FrameRelayDLCIConnectsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 5)
)
if mibBuilder.loadTexts:
    frameRelayDLCIConnectsTable.setStatus("mandatory")
_FrameRelayDLCIConnectsEntry_Object = MibTableRow
frameRelayDLCIConnectsEntry = _FrameRelayDLCIConnectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 5, 1)
)
frameRelayDLCIConnectsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "frameRelayDLCIConnectsLinkCardNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayDLCIConnectsLinkChannelNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayDLCIConnectsDLCIConnected"),
)
if mibBuilder.loadTexts:
    frameRelayDLCIConnectsEntry.setStatus("mandatory")
_FrameRelayDLCIConnectsLinkCardNumber_Type = Integer32
_FrameRelayDLCIConnectsLinkCardNumber_Object = MibTableColumn
frameRelayDLCIConnectsLinkCardNumber = _FrameRelayDLCIConnectsLinkCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 5, 1, 1),
    _FrameRelayDLCIConnectsLinkCardNumber_Type()
)
frameRelayDLCIConnectsLinkCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDLCIConnectsLinkCardNumber.setStatus("mandatory")
_FrameRelayDLCIConnectsLinkChannelNumber_Type = Integer32
_FrameRelayDLCIConnectsLinkChannelNumber_Object = MibTableColumn
frameRelayDLCIConnectsLinkChannelNumber = _FrameRelayDLCIConnectsLinkChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 5, 1, 2),
    _FrameRelayDLCIConnectsLinkChannelNumber_Type()
)
frameRelayDLCIConnectsLinkChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDLCIConnectsLinkChannelNumber.setStatus("mandatory")
_FrameRelayDLCIConnectsDLCIConnected_Type = Integer32
_FrameRelayDLCIConnectsDLCIConnected_Object = MibTableColumn
frameRelayDLCIConnectsDLCIConnected = _FrameRelayDLCIConnectsDLCIConnected_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 5, 1, 3),
    _FrameRelayDLCIConnectsDLCIConnected_Type()
)
frameRelayDLCIConnectsDLCIConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDLCIConnectsDLCIConnected.setStatus("mandatory")
_FrameRelayDLCIConnectsDestCardNumber_Type = Integer32
_FrameRelayDLCIConnectsDestCardNumber_Object = MibTableColumn
frameRelayDLCIConnectsDestCardNumber = _FrameRelayDLCIConnectsDestCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 5, 1, 4),
    _FrameRelayDLCIConnectsDestCardNumber_Type()
)
frameRelayDLCIConnectsDestCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDLCIConnectsDestCardNumber.setStatus("mandatory")
_FrameRelayDLCIConnectsDestChannelNumber_Type = Integer32
_FrameRelayDLCIConnectsDestChannelNumber_Object = MibTableColumn
frameRelayDLCIConnectsDestChannelNumber = _FrameRelayDLCIConnectsDestChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 5, 1, 5),
    _FrameRelayDLCIConnectsDestChannelNumber_Type()
)
frameRelayDLCIConnectsDestChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDLCIConnectsDestChannelNumber.setStatus("mandatory")
_FrameRelayDLCIConnectsDestDLCINumber_Type = Integer32
_FrameRelayDLCIConnectsDestDLCINumber_Object = MibTableColumn
frameRelayDLCIConnectsDestDLCINumber = _FrameRelayDLCIConnectsDestDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 5, 6, 5, 1, 6),
    _FrameRelayDLCIConnectsDestDLCINumber_Type()
)
frameRelayDLCIConnectsDestDLCINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDLCIConnectsDestDLCINumber.setStatus("mandatory")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6)
)
_T1_interface_ObjectIdentity = ObjectIdentity
t1_interface = _T1_interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1)
)
_T1DS1InterfaceTable_Object = MibTable
t1DS1InterfaceTable = _T1DS1InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    t1DS1InterfaceTable.setStatus("mandatory")
_T1DS1InterfaceEntry_Object = MibTableRow
t1DS1InterfaceEntry = _T1DS1InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 1, 1)
)
t1DS1InterfaceEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "t1DS1InterfaceDS0Index"),
)
if mibBuilder.loadTexts:
    t1DS1InterfaceEntry.setStatus("mandatory")


class _T1DS1InterfaceDS0Index_Type(Integer32):
    """Custom type t1DS1InterfaceDS0Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_T1DS1InterfaceDS0Index_Type.__name__ = "Integer32"
_T1DS1InterfaceDS0Index_Object = MibTableColumn
t1DS1InterfaceDS0Index = _T1DS1InterfaceDS0Index_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 1, 1, 1),
    _T1DS1InterfaceDS0Index_Type()
)
t1DS1InterfaceDS0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1DS1InterfaceDS0Index.setStatus("mandatory")


class _T1DS1InterfaceConnectionState_Type(Integer32):
    """Custom type t1DS1InterfaceConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("bypassData", 3),
          ("bypassVoice", 2),
          ("idle", 1),
          ("toCCMLinkA1", 4),
          ("toCCMLinkA2", 5),
          ("toCCMLinkA3", 6),
          ("toCCMLinkA4", 7),
          ("toCCMLinkA5", 8),
          ("toCCMLinkA6", 9),
          ("toDataPort1", 10),
          ("toDataPort2", 11),
          ("toVChOnSlotCDVM1", 18),
          ("toVChOnSlotCDVM10", 27),
          ("toVChOnSlotCDVM11", 28),
          ("toVChOnSlotCDVM12", 29),
          ("toVChOnSlotCDVM2", 19),
          ("toVChOnSlotCDVM3", 20),
          ("toVChOnSlotCDVM4", 21),
          ("toVChOnSlotCDVM5", 22),
          ("toVChOnSlotCDVM6", 23),
          ("toVChOnSlotCDVM7", 24),
          ("toVChOnSlotCDVM8", 25),
          ("toVChOnSlotCDVM9", 26),
          ("toVChOnSlotDDVM1", 30),
          ("toVChOnSlotDDVM10", 39),
          ("toVChOnSlotDDVM11", 40),
          ("toVChOnSlotDDVM12", 41),
          ("toVChOnSlotDDVM2", 31),
          ("toVChOnSlotDDVM3", 32),
          ("toVChOnSlotDDVM4", 33),
          ("toVChOnSlotDDVM5", 34),
          ("toVChOnSlotDDVM6", 35),
          ("toVChOnSlotDDVM7", 36),
          ("toVChOnSlotDDVM8", 37),
          ("toVChOnSlotDDVM9", 38),
          ("toVChOnT1DVM1", 12),
          ("toVChOnT1DVM2", 13),
          ("toVChOnT1DVM3", 14),
          ("toVChOnT1DVM4", 15),
          ("toVChOnT1DVM5", 16),
          ("toVChOnT1DVM6", 17))
    )


_T1DS1InterfaceConnectionState_Type.__name__ = "Integer32"
_T1DS1InterfaceConnectionState_Object = MibTableColumn
t1DS1InterfaceConnectionState = _T1DS1InterfaceConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 1, 1, 2),
    _T1DS1InterfaceConnectionState_Type()
)
t1DS1InterfaceConnectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1DS1InterfaceConnectionState.setStatus("mandatory")
_T1DSX1InterfaceTable_Object = MibTable
t1DSX1InterfaceTable = _T1DSX1InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    t1DSX1InterfaceTable.setStatus("mandatory")
_T1DSX1InterfaceEntry_Object = MibTableRow
t1DSX1InterfaceEntry = _T1DSX1InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 2, 1)
)
t1DSX1InterfaceEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "t1DSX1InterfaceDS0Index"),
)
if mibBuilder.loadTexts:
    t1DSX1InterfaceEntry.setStatus("mandatory")


class _T1DSX1InterfaceDS0Index_Type(Integer32):
    """Custom type t1DSX1InterfaceDS0Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_T1DSX1InterfaceDS0Index_Type.__name__ = "Integer32"
_T1DSX1InterfaceDS0Index_Object = MibTableColumn
t1DSX1InterfaceDS0Index = _T1DSX1InterfaceDS0Index_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 2, 1, 1),
    _T1DSX1InterfaceDS0Index_Type()
)
t1DSX1InterfaceDS0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1DSX1InterfaceDS0Index.setStatus("mandatory")


class _T1DSX1InterfaceConnectionState_Type(Integer32):
    """Custom type t1DSX1InterfaceConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("bypassData", 3),
          ("bypassVoice", 2),
          ("idle", 1),
          ("toCCMLinkA1", 4),
          ("toCCMLinkA2", 5),
          ("toCCMLinkA3", 6),
          ("toCCMLinkA4", 7),
          ("toCCMLinkA5", 8),
          ("toCCMLinkA6", 9),
          ("toDataPort1", 10),
          ("toDataPort2", 11),
          ("toVChOnSlotCDVM1", 18),
          ("toVChOnSlotCDVM10", 27),
          ("toVChOnSlotCDVM11", 28),
          ("toVChOnSlotCDVM12", 29),
          ("toVChOnSlotCDVM2", 19),
          ("toVChOnSlotCDVM3", 20),
          ("toVChOnSlotCDVM4", 21),
          ("toVChOnSlotCDVM5", 22),
          ("toVChOnSlotCDVM6", 23),
          ("toVChOnSlotCDVM7", 24),
          ("toVChOnSlotCDVM8", 25),
          ("toVChOnSlotCDVM9", 26),
          ("toVChOnSlotDDVM1", 30),
          ("toVChOnSlotDDVM10", 39),
          ("toVChOnSlotDDVM11", 40),
          ("toVChOnSlotDDVM12", 41),
          ("toVChOnSlotDDVM2", 31),
          ("toVChOnSlotDDVM3", 32),
          ("toVChOnSlotDDVM4", 33),
          ("toVChOnSlotDDVM5", 34),
          ("toVChOnSlotDDVM6", 35),
          ("toVChOnSlotDDVM7", 36),
          ("toVChOnSlotDDVM8", 37),
          ("toVChOnSlotDDVM9", 38),
          ("toVChOnT1DVM1", 12),
          ("toVChOnT1DVM2", 13),
          ("toVChOnT1DVM3", 14),
          ("toVChOnT1DVM4", 15),
          ("toVChOnT1DVM5", 16),
          ("toVChOnT1DVM6", 17))
    )


_T1DSX1InterfaceConnectionState_Type.__name__ = "Integer32"
_T1DSX1InterfaceConnectionState_Object = MibTableColumn
t1DSX1InterfaceConnectionState = _T1DSX1InterfaceConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 2, 1, 2),
    _T1DSX1InterfaceConnectionState_Type()
)
t1DSX1InterfaceConnectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1DSX1InterfaceConnectionState.setStatus("mandatory")
_T1CfgGroup_ObjectIdentity = ObjectIdentity
t1CfgGroup = _T1CfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3)
)


class _T1CfgDSX1FrameFormat_Type(Integer32):
    """Custom type t1CfgDSX1FrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extendedSuperFrame", 2),
          ("superFrame", 1))
    )


_T1CfgDSX1FrameFormat_Type.__name__ = "Integer32"
_T1CfgDSX1FrameFormat_Object = MibScalar
t1CfgDSX1FrameFormat = _T1CfgDSX1FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 1),
    _T1CfgDSX1FrameFormat_Type()
)
t1CfgDSX1FrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDSX1FrameFormat.setStatus("mandatory")


class _T1CfgDSX1LineCode_Type(Integer32):
    """Custom type t1CfgDSX1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2))
    )


_T1CfgDSX1LineCode_Type.__name__ = "Integer32"
_T1CfgDSX1LineCode_Object = MibScalar
t1CfgDSX1LineCode = _T1CfgDSX1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 2),
    _T1CfgDSX1LineCode_Type()
)
t1CfgDSX1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDSX1LineCode.setStatus("mandatory")


class _T1CfgDSX1IdleCode_Type(OctetString):
    """Custom type t1CfgDSX1IdleCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T1CfgDSX1IdleCode_Type.__name__ = "OctetString"
_T1CfgDSX1IdleCode_Object = MibScalar
t1CfgDSX1IdleCode = _T1CfgDSX1IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 3),
    _T1CfgDSX1IdleCode_Type()
)
t1CfgDSX1IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDSX1IdleCode.setStatus("mandatory")


class _T1CfgDSX1lineBuildout_Type(Integer32):
    """Custom type t1CfgDSX1lineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("externalLBO", 5),
          ("greaterThan665Feet", 6),
          ("lessThan110Feet", 1),
          ("lessThan220Feet", 2),
          ("lessThan330Feet", 3),
          ("lessThan440Feet", 4),
          ("lessThan550Feet", 7),
          ("lessThan660Feet", 8))
    )


_T1CfgDSX1lineBuildout_Type.__name__ = "Integer32"
_T1CfgDSX1lineBuildout_Object = MibScalar
t1CfgDSX1lineBuildout = _T1CfgDSX1lineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 4),
    _T1CfgDSX1lineBuildout_Type()
)
t1CfgDSX1lineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDSX1lineBuildout.setStatus("mandatory")


class _T1CfgDSX1NetworkInvokedLoopback_Type(Integer32):
    """Custom type t1CfgDSX1NetworkInvokedLoopback based on Integer32"""
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


_T1CfgDSX1NetworkInvokedLoopback_Type.__name__ = "Integer32"
_T1CfgDSX1NetworkInvokedLoopback_Object = MibScalar
t1CfgDSX1NetworkInvokedLoopback = _T1CfgDSX1NetworkInvokedLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 5),
    _T1CfgDSX1NetworkInvokedLoopback_Type()
)
t1CfgDSX1NetworkInvokedLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDSX1NetworkInvokedLoopback.setStatus("mandatory")


class _T1CfgDS1FrameFormat_Type(Integer32):
    """Custom type t1CfgDS1FrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extendedSuperFrame", 2),
          ("superFrame", 1))
    )


_T1CfgDS1FrameFormat_Type.__name__ = "Integer32"
_T1CfgDS1FrameFormat_Object = MibScalar
t1CfgDS1FrameFormat = _T1CfgDS1FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 6),
    _T1CfgDS1FrameFormat_Type()
)
t1CfgDS1FrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDS1FrameFormat.setStatus("mandatory")


class _T1CfgDS1LineCode_Type(Integer32):
    """Custom type t1CfgDS1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2))
    )


_T1CfgDS1LineCode_Type.__name__ = "Integer32"
_T1CfgDS1LineCode_Object = MibScalar
t1CfgDS1LineCode = _T1CfgDS1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 7),
    _T1CfgDS1LineCode_Type()
)
t1CfgDS1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDS1LineCode.setStatus("mandatory")


class _T1CfgDS1IdleCode_Type(OctetString):
    """Custom type t1CfgDS1IdleCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T1CfgDS1IdleCode_Type.__name__ = "OctetString"
_T1CfgDS1IdleCode_Object = MibScalar
t1CfgDS1IdleCode = _T1CfgDS1IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 8),
    _T1CfgDS1IdleCode_Type()
)
t1CfgDS1IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDS1IdleCode.setStatus("mandatory")


class _T1CfgDS1NetworkInvokedLoopback_Type(Integer32):
    """Custom type t1CfgDS1NetworkInvokedLoopback based on Integer32"""
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


_T1CfgDS1NetworkInvokedLoopback_Type.__name__ = "Integer32"
_T1CfgDS1NetworkInvokedLoopback_Object = MibScalar
t1CfgDS1NetworkInvokedLoopback = _T1CfgDS1NetworkInvokedLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 9),
    _T1CfgDS1NetworkInvokedLoopback_Type()
)
t1CfgDS1NetworkInvokedLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDS1NetworkInvokedLoopback.setStatus("mandatory")


class _T1CfgDataPort1Rate_Type(Integer32):
    """Custom type t1CfgDataPort1Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_T1CfgDataPort1Rate_Type.__name__ = "Integer32"
_T1CfgDataPort1Rate_Object = MibScalar
t1CfgDataPort1Rate = _T1CfgDataPort1Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 10),
    _T1CfgDataPort1Rate_Type()
)
t1CfgDataPort1Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDataPort1Rate.setStatus("mandatory")


class _T1CfgDataPort1Timing_Type(Integer32):
    """Custom type t1CfgDataPort1Timing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internallySuppliedNormal", 1),
          ("tailCircuit", 2))
    )


_T1CfgDataPort1Timing_Type.__name__ = "Integer32"
_T1CfgDataPort1Timing_Object = MibScalar
t1CfgDataPort1Timing = _T1CfgDataPort1Timing_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 11),
    _T1CfgDataPort1Timing_Type()
)
t1CfgDataPort1Timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDataPort1Timing.setStatus("mandatory")


class _T1CfgDataPort1DTRControl_Type(Integer32):
    """Custom type t1CfgDataPort1DTRControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtrForced", 2),
          ("dtrNormal", 1))
    )


_T1CfgDataPort1DTRControl_Type.__name__ = "Integer32"
_T1CfgDataPort1DTRControl_Object = MibScalar
t1CfgDataPort1DTRControl = _T1CfgDataPort1DTRControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 12),
    _T1CfgDataPort1DTRControl_Type()
)
t1CfgDataPort1DTRControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDataPort1DTRControl.setStatus("mandatory")


class _T1CfgDataPort1RTSControl_Type(Integer32):
    """Custom type t1CfgDataPort1RTSControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtsForced", 2),
          ("rtsNormal", 1))
    )


_T1CfgDataPort1RTSControl_Type.__name__ = "Integer32"
_T1CfgDataPort1RTSControl_Object = MibScalar
t1CfgDataPort1RTSControl = _T1CfgDataPort1RTSControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 13),
    _T1CfgDataPort1RTSControl_Type()
)
t1CfgDataPort1RTSControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDataPort1RTSControl.setStatus("mandatory")


class _T1CfgDataPort2Rate_Type(Integer32):
    """Custom type t1CfgDataPort2Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_T1CfgDataPort2Rate_Type.__name__ = "Integer32"
_T1CfgDataPort2Rate_Object = MibScalar
t1CfgDataPort2Rate = _T1CfgDataPort2Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 14),
    _T1CfgDataPort2Rate_Type()
)
t1CfgDataPort2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDataPort2Rate.setStatus("mandatory")


class _T1CfgDataPort2Timing_Type(Integer32):
    """Custom type t1CfgDataPort2Timing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internallySupplied", 1),
          ("tailCircuit", 2))
    )


_T1CfgDataPort2Timing_Type.__name__ = "Integer32"
_T1CfgDataPort2Timing_Object = MibScalar
t1CfgDataPort2Timing = _T1CfgDataPort2Timing_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 15),
    _T1CfgDataPort2Timing_Type()
)
t1CfgDataPort2Timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDataPort2Timing.setStatus("mandatory")


class _T1CfgDataPort2DTRControl_Type(Integer32):
    """Custom type t1CfgDataPort2DTRControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtr", 1),
          ("dtrForcedOn", 2))
    )


_T1CfgDataPort2DTRControl_Type.__name__ = "Integer32"
_T1CfgDataPort2DTRControl_Object = MibScalar
t1CfgDataPort2DTRControl = _T1CfgDataPort2DTRControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 16),
    _T1CfgDataPort2DTRControl_Type()
)
t1CfgDataPort2DTRControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDataPort2DTRControl.setStatus("mandatory")


class _T1CfgDataPort2RTSControl_Type(Integer32):
    """Custom type t1CfgDataPort2RTSControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rts", 1),
          ("rtsForcedOn", 2))
    )


_T1CfgDataPort2RTSControl_Type.__name__ = "Integer32"
_T1CfgDataPort2RTSControl_Object = MibScalar
t1CfgDataPort2RTSControl = _T1CfgDataPort2RTSControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 17),
    _T1CfgDataPort2RTSControl_Type()
)
t1CfgDataPort2RTSControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgDataPort2RTSControl.setStatus("mandatory")


class _T1CfgCCMLinkA1Rate_Type(Integer32):
    """Custom type t1CfgCCMLinkA1Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_T1CfgCCMLinkA1Rate_Type.__name__ = "Integer32"
_T1CfgCCMLinkA1Rate_Object = MibScalar
t1CfgCCMLinkA1Rate = _T1CfgCCMLinkA1Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 18),
    _T1CfgCCMLinkA1Rate_Type()
)
t1CfgCCMLinkA1Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgCCMLinkA1Rate.setStatus("mandatory")


class _T1CfgCCMLinkA2Rate_Type(Integer32):
    """Custom type t1CfgCCMLinkA2Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_T1CfgCCMLinkA2Rate_Type.__name__ = "Integer32"
_T1CfgCCMLinkA2Rate_Object = MibScalar
t1CfgCCMLinkA2Rate = _T1CfgCCMLinkA2Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 19),
    _T1CfgCCMLinkA2Rate_Type()
)
t1CfgCCMLinkA2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgCCMLinkA2Rate.setStatus("mandatory")


class _T1CfgCCMLinkA3Rate_Type(Integer32):
    """Custom type t1CfgCCMLinkA3Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_T1CfgCCMLinkA3Rate_Type.__name__ = "Integer32"
_T1CfgCCMLinkA3Rate_Object = MibScalar
t1CfgCCMLinkA3Rate = _T1CfgCCMLinkA3Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 20),
    _T1CfgCCMLinkA3Rate_Type()
)
t1CfgCCMLinkA3Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgCCMLinkA3Rate.setStatus("mandatory")


class _T1CfgCCMLinkA4Rate_Type(Integer32):
    """Custom type t1CfgCCMLinkA4Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_T1CfgCCMLinkA4Rate_Type.__name__ = "Integer32"
_T1CfgCCMLinkA4Rate_Object = MibScalar
t1CfgCCMLinkA4Rate = _T1CfgCCMLinkA4Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 21),
    _T1CfgCCMLinkA4Rate_Type()
)
t1CfgCCMLinkA4Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgCCMLinkA4Rate.setStatus("mandatory")


class _T1CfgCCMLinkA5Rate_Type(Integer32):
    """Custom type t1CfgCCMLinkA5Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_T1CfgCCMLinkA5Rate_Type.__name__ = "Integer32"
_T1CfgCCMLinkA5Rate_Object = MibScalar
t1CfgCCMLinkA5Rate = _T1CfgCCMLinkA5Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 22),
    _T1CfgCCMLinkA5Rate_Type()
)
t1CfgCCMLinkA5Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgCCMLinkA5Rate.setStatus("mandatory")


class _T1CfgCCMLinkA6Rate_Type(Integer32):
    """Custom type t1CfgCCMLinkA6Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_T1CfgCCMLinkA6Rate_Type.__name__ = "Integer32"
_T1CfgCCMLinkA6Rate_Object = MibScalar
t1CfgCCMLinkA6Rate = _T1CfgCCMLinkA6Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 23),
    _T1CfgCCMLinkA6Rate_Type()
)
t1CfgCCMLinkA6Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgCCMLinkA6Rate.setStatus("mandatory")


class _T1CfgSystemClockSource_Type(Integer32):
    """Custom type t1CfgSystemClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds1ClockDerived", 1),
          ("dsx1Clockderived", 2),
          ("internalClocking", 3))
    )


_T1CfgSystemClockSource_Type.__name__ = "Integer32"
_T1CfgSystemClockSource_Object = MibScalar
t1CfgSystemClockSource = _T1CfgSystemClockSource_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 24),
    _T1CfgSystemClockSource_Type()
)
t1CfgSystemClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1CfgSystemClockSource.setStatus("mandatory")


class _T1CfgDS1Config_Type(Integer32):
    """Custom type t1CfgDS1Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commit", 2),
          ("init", 1))
    )


_T1CfgDS1Config_Type.__name__ = "Integer32"
_T1CfgDS1Config_Object = MibScalar
t1CfgDS1Config = _T1CfgDS1Config_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 25),
    _T1CfgDS1Config_Type()
)
t1CfgDS1Config.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    t1CfgDS1Config.setStatus("mandatory")


class _T1CfgDSX1Config_Type(Integer32):
    """Custom type t1CfgDSX1Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commit", 2),
          ("init", 1))
    )


_T1CfgDSX1Config_Type.__name__ = "Integer32"
_T1CfgDSX1Config_Object = MibScalar
t1CfgDSX1Config = _T1CfgDSX1Config_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 3, 26),
    _T1CfgDSX1Config_Type()
)
t1CfgDSX1Config.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    t1CfgDSX1Config.setStatus("mandatory")
_T1FlashControlTable_Object = MibTable
t1FlashControlTable = _T1FlashControlTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 4)
)
if mibBuilder.loadTexts:
    t1FlashControlTable.setStatus("mandatory")
_T1FlashControlEntry_Object = MibTableRow
t1FlashControlEntry = _T1FlashControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 4, 1)
)
t1FlashControlEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "t1FlashControlCardNumber"),
)
if mibBuilder.loadTexts:
    t1FlashControlEntry.setStatus("mandatory")


class _T1FlashControlCardNumber_Type(Integer32):
    """Custom type t1FlashControlCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_T1FlashControlCardNumber_Type.__name__ = "Integer32"
_T1FlashControlCardNumber_Object = MibTableColumn
t1FlashControlCardNumber = _T1FlashControlCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 4, 1, 1),
    _T1FlashControlCardNumber_Type()
)
t1FlashControlCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1FlashControlCardNumber.setStatus("mandatory")


class _T1FlashControlCommand_Type(Integer32):
    """Custom type t1FlashControlCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eraseCardFlash", 1)
    )


_T1FlashControlCommand_Type.__name__ = "Integer32"
_T1FlashControlCommand_Object = MibTableColumn
t1FlashControlCommand = _T1FlashControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 4, 1, 2),
    _T1FlashControlCommand_Type()
)
t1FlashControlCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    t1FlashControlCommand.setStatus("mandatory")


class _T1FlashControlFlashStatus_Type(Integer32):
    """Custom type t1FlashControlFlashStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bootImageCorrupt", 1),
          ("eraseAborted", 6),
          ("securityViolation", 5),
          ("t1FlashErased", 3),
          ("t1FlashImageInvalid", 4),
          ("t1FlashImageValid", 2))
    )


_T1FlashControlFlashStatus_Type.__name__ = "Integer32"
_T1FlashControlFlashStatus_Object = MibTableColumn
t1FlashControlFlashStatus = _T1FlashControlFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 1, 4, 1, 3),
    _T1FlashControlFlashStatus_Type()
)
t1FlashControlFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1FlashControlFlashStatus.setStatus("mandatory")
_E1_interface_ObjectIdentity = ObjectIdentity
e1_interface = _E1_interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2)
)
_E1L1InterfaceTable_Object = MibTable
e1L1InterfaceTable = _E1L1InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    e1L1InterfaceTable.setStatus("mandatory")
_E1L1InterfaceEntry_Object = MibTableRow
e1L1InterfaceEntry = _E1L1InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 1, 1)
)
e1L1InterfaceEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "e1L1InterfaceDS0Index"),
)
if mibBuilder.loadTexts:
    e1L1InterfaceEntry.setStatus("mandatory")


class _E1L1InterfaceDS0Index_Type(Integer32):
    """Custom type e1L1InterfaceDS0Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_E1L1InterfaceDS0Index_Type.__name__ = "Integer32"
_E1L1InterfaceDS0Index_Object = MibTableColumn
e1L1InterfaceDS0Index = _E1L1InterfaceDS0Index_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 1, 1, 1),
    _E1L1InterfaceDS0Index_Type()
)
e1L1InterfaceDS0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1L1InterfaceDS0Index.setStatus("mandatory")


class _E1L1InterfaceConnectionState_Type(Integer32):
    """Custom type e1L1InterfaceConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("idle", 1),
          ("toCCMLinkA1", 3),
          ("toCCMLinkA2", 4),
          ("toCCMLinkA3", 5),
          ("toCCMLinkA4", 6),
          ("toCCMLinkA5", 7),
          ("toCCMLinkA6", 8),
          ("toDataPort1", 9),
          ("toDataPort2", 10),
          ("toVChOnE1DVM1", 11),
          ("toVChOnE1DVM2", 12),
          ("toVChOnE1DVM3", 13),
          ("toVChOnE1DVM4", 14),
          ("toVChOnE1DVM5", 15),
          ("toVChOnE1DVM6", 16),
          ("toVChOnSlotCDVM1", 17),
          ("toVChOnSlotCDVM10", 26),
          ("toVChOnSlotCDVM11", 27),
          ("toVChOnSlotCDVM12", 28),
          ("toVChOnSlotCDVM2", 18),
          ("toVChOnSlotCDVM3", 19),
          ("toVChOnSlotCDVM4", 20),
          ("toVChOnSlotCDVM5", 21),
          ("toVChOnSlotCDVM6", 22),
          ("toVChOnSlotCDVM7", 23),
          ("toVChOnSlotCDVM8", 24),
          ("toVChOnSlotCDVM9", 25),
          ("toVChOnSlotDDVM1", 29),
          ("toVChOnSlotDDVM10", 38),
          ("toVChOnSlotDDVM11", 39),
          ("toVChOnSlotDDVM12", 40),
          ("toVChOnSlotDDVM2", 30),
          ("toVChOnSlotDDVM3", 31),
          ("toVChOnSlotDDVM4", 32),
          ("toVChOnSlotDDVM5", 33),
          ("toVChOnSlotDDVM6", 34),
          ("toVChOnSlotDDVM7", 35),
          ("toVChOnSlotDDVM8", 36),
          ("toVChOnSlotDDVM9", 37))
    )


_E1L1InterfaceConnectionState_Type.__name__ = "Integer32"
_E1L1InterfaceConnectionState_Object = MibTableColumn
e1L1InterfaceConnectionState = _E1L1InterfaceConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 1, 1, 2),
    _E1L1InterfaceConnectionState_Type()
)
e1L1InterfaceConnectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1L1InterfaceConnectionState.setStatus("mandatory")
_E1L2InterfaceTable_Object = MibTable
e1L2InterfaceTable = _E1L2InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 2)
)
if mibBuilder.loadTexts:
    e1L2InterfaceTable.setStatus("mandatory")
_E1L2InterfaceEntry_Object = MibTableRow
e1L2InterfaceEntry = _E1L2InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 2, 1)
)
e1L2InterfaceEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "e1L2InterfaceDS0Index"),
)
if mibBuilder.loadTexts:
    e1L2InterfaceEntry.setStatus("mandatory")


class _E1L2InterfaceDS0Index_Type(Integer32):
    """Custom type e1L2InterfaceDS0Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_E1L2InterfaceDS0Index_Type.__name__ = "Integer32"
_E1L2InterfaceDS0Index_Object = MibTableColumn
e1L2InterfaceDS0Index = _E1L2InterfaceDS0Index_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 2, 1, 1),
    _E1L2InterfaceDS0Index_Type()
)
e1L2InterfaceDS0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1L2InterfaceDS0Index.setStatus("mandatory")


class _E1L2InterfaceConnectionState_Type(Integer32):
    """Custom type e1L2InterfaceConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("idle", 1),
          ("toCCMLinkA1", 3),
          ("toCCMLinkA2", 4),
          ("toCCMLinkA3", 5),
          ("toCCMLinkA4", 6),
          ("toCCMLinkA5", 7),
          ("toCCMLinkA6", 8),
          ("toDataPort1", 9),
          ("toDataPort2", 10),
          ("toVChOnE1DVM1", 11),
          ("toVChOnE1DVM2", 12),
          ("toVChOnE1DVM3", 13),
          ("toVChOnE1DVM4", 14),
          ("toVChOnE1DVM5", 15),
          ("toVChOnE1DVM6", 16),
          ("toVChOnSlotCDVM1", 17),
          ("toVChOnSlotCDVM10", 26),
          ("toVChOnSlotCDVM11", 27),
          ("toVChOnSlotCDVM12", 28),
          ("toVChOnSlotCDVM2", 18),
          ("toVChOnSlotCDVM3", 19),
          ("toVChOnSlotCDVM4", 20),
          ("toVChOnSlotCDVM5", 21),
          ("toVChOnSlotCDVM6", 22),
          ("toVChOnSlotCDVM7", 23),
          ("toVChOnSlotCDVM8", 24),
          ("toVChOnSlotCDVM9", 25),
          ("toVChOnSlotDDVM1", 29),
          ("toVChOnSlotDDVM10", 38),
          ("toVChOnSlotDDVM11", 39),
          ("toVChOnSlotDDVM12", 40),
          ("toVChOnSlotDDVM2", 30),
          ("toVChOnSlotDDVM3", 31),
          ("toVChOnSlotDDVM4", 32),
          ("toVChOnSlotDDVM5", 33),
          ("toVChOnSlotDDVM6", 34),
          ("toVChOnSlotDDVM7", 35),
          ("toVChOnSlotDDVM8", 36),
          ("toVChOnSlotDDVM9", 37))
    )


_E1L2InterfaceConnectionState_Type.__name__ = "Integer32"
_E1L2InterfaceConnectionState_Object = MibTableColumn
e1L2InterfaceConnectionState = _E1L2InterfaceConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 2, 1, 2),
    _E1L2InterfaceConnectionState_Type()
)
e1L2InterfaceConnectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1L2InterfaceConnectionState.setStatus("mandatory")
_E1CfgGroup_ObjectIdentity = ObjectIdentity
e1CfgGroup = _E1CfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3)
)


class _E1CfgL1LineCode_Type(Integer32):
    """Custom type e1CfgL1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("hdb3", 2))
    )


_E1CfgL1LineCode_Type.__name__ = "Integer32"
_E1CfgL1LineCode_Object = MibScalar
e1CfgL1LineCode = _E1CfgL1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 1),
    _E1CfgL1LineCode_Type()
)
e1CfgL1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgL1LineCode.setStatus("mandatory")


class _E1CfgL1IdleCode_Type(OctetString):
    """Custom type e1CfgL1IdleCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_E1CfgL1IdleCode_Type.__name__ = "OctetString"
_E1CfgL1IdleCode_Object = MibScalar
e1CfgL1IdleCode = _E1CfgL1IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 2),
    _E1CfgL1IdleCode_Type()
)
e1CfgL1IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgL1IdleCode.setStatus("mandatory")


class _E1CfgL1SignallingMode_Type(Integer32):
    """Custom type e1CfgL1SignallingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("cas", 1),
          ("casTS16Bypass", 10),
          ("ccsTS16Bypass", 11),
          ("transparentIdle", 2),
          ("transparentTS16ToA2", 3),
          ("transparentTS16ToA3", 4),
          ("transparentTS16ToA4", 5),
          ("transparentTS16ToA5", 6),
          ("transparentTS16ToA6", 7),
          ("transparentTS16ToDP1", 8),
          ("transparentTS16ToDP2", 9))
    )


_E1CfgL1SignallingMode_Type.__name__ = "Integer32"
_E1CfgL1SignallingMode_Object = MibScalar
e1CfgL1SignallingMode = _E1CfgL1SignallingMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 3),
    _E1CfgL1SignallingMode_Type()
)
e1CfgL1SignallingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgL1SignallingMode.setStatus("mandatory")


class _E1CfgL2LineCode_Type(Integer32):
    """Custom type e1CfgL2LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("hdb3", 2))
    )


_E1CfgL2LineCode_Type.__name__ = "Integer32"
_E1CfgL2LineCode_Object = MibScalar
e1CfgL2LineCode = _E1CfgL2LineCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 4),
    _E1CfgL2LineCode_Type()
)
e1CfgL2LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgL2LineCode.setStatus("mandatory")


class _E1CfgL2IdleCode_Type(OctetString):
    """Custom type e1CfgL2IdleCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_E1CfgL2IdleCode_Type.__name__ = "OctetString"
_E1CfgL2IdleCode_Object = MibScalar
e1CfgL2IdleCode = _E1CfgL2IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 5),
    _E1CfgL2IdleCode_Type()
)
e1CfgL2IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgL2IdleCode.setStatus("mandatory")


class _E1CfgL2SignallingMode_Type(Integer32):
    """Custom type e1CfgL2SignallingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("cas", 1),
          ("casTS16Bypass", 10),
          ("ccsTS16Bypass", 11),
          ("transparentIdle", 2),
          ("transparentTS16ToA2", 3),
          ("transparentTS16ToA3", 4),
          ("transparentTS16ToA4", 5),
          ("transparentTS16ToA5", 6),
          ("transparentTS16ToA6", 7),
          ("transparentTS16ToDP1", 8),
          ("transparentTS16ToDP2", 9))
    )


_E1CfgL2SignallingMode_Type.__name__ = "Integer32"
_E1CfgL2SignallingMode_Object = MibScalar
e1CfgL2SignallingMode = _E1CfgL2SignallingMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 6),
    _E1CfgL2SignallingMode_Type()
)
e1CfgL2SignallingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgL2SignallingMode.setStatus("mandatory")


class _E1CfgDataPort1BaseRate_Type(Integer32):
    """Custom type e1CfgDataPort1BaseRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_E1CfgDataPort1BaseRate_Type.__name__ = "Integer32"
_E1CfgDataPort1BaseRate_Object = MibScalar
e1CfgDataPort1BaseRate = _E1CfgDataPort1BaseRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 7),
    _E1CfgDataPort1BaseRate_Type()
)
e1CfgDataPort1BaseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgDataPort1BaseRate.setStatus("mandatory")


class _E1CfgDataPort1Timing_Type(Integer32):
    """Custom type e1CfgDataPort1Timing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("tailCircuit", 2))
    )


_E1CfgDataPort1Timing_Type.__name__ = "Integer32"
_E1CfgDataPort1Timing_Object = MibScalar
e1CfgDataPort1Timing = _E1CfgDataPort1Timing_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 8),
    _E1CfgDataPort1Timing_Type()
)
e1CfgDataPort1Timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgDataPort1Timing.setStatus("mandatory")


class _E1CfgDataPort1DTRControl_Type(Integer32):
    """Custom type e1CfgDataPort1DTRControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtrForced", 2),
          ("dtrNormal", 1))
    )


_E1CfgDataPort1DTRControl_Type.__name__ = "Integer32"
_E1CfgDataPort1DTRControl_Object = MibScalar
e1CfgDataPort1DTRControl = _E1CfgDataPort1DTRControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 9),
    _E1CfgDataPort1DTRControl_Type()
)
e1CfgDataPort1DTRControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgDataPort1DTRControl.setStatus("mandatory")


class _E1CfgDataPort1RTSControl_Type(Integer32):
    """Custom type e1CfgDataPort1RTSControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtsForced", 2),
          ("rtsNormal", 1))
    )


_E1CfgDataPort1RTSControl_Type.__name__ = "Integer32"
_E1CfgDataPort1RTSControl_Object = MibScalar
e1CfgDataPort1RTSControl = _E1CfgDataPort1RTSControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 10),
    _E1CfgDataPort1RTSControl_Type()
)
e1CfgDataPort1RTSControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgDataPort1RTSControl.setStatus("mandatory")


class _E1CfgDataPort2BaseRate_Type(Integer32):
    """Custom type e1CfgDataPort2BaseRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_E1CfgDataPort2BaseRate_Type.__name__ = "Integer32"
_E1CfgDataPort2BaseRate_Object = MibScalar
e1CfgDataPort2BaseRate = _E1CfgDataPort2BaseRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 11),
    _E1CfgDataPort2BaseRate_Type()
)
e1CfgDataPort2BaseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgDataPort2BaseRate.setStatus("mandatory")


class _E1CfgDataPort2Timing_Type(Integer32):
    """Custom type e1CfgDataPort2Timing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("tailCircuit", 2))
    )


_E1CfgDataPort2Timing_Type.__name__ = "Integer32"
_E1CfgDataPort2Timing_Object = MibScalar
e1CfgDataPort2Timing = _E1CfgDataPort2Timing_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 12),
    _E1CfgDataPort2Timing_Type()
)
e1CfgDataPort2Timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgDataPort2Timing.setStatus("mandatory")


class _E1CfgDataPort2DTRControl_Type(Integer32):
    """Custom type e1CfgDataPort2DTRControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtrForced", 2),
          ("dtrNormal", 1))
    )


_E1CfgDataPort2DTRControl_Type.__name__ = "Integer32"
_E1CfgDataPort2DTRControl_Object = MibScalar
e1CfgDataPort2DTRControl = _E1CfgDataPort2DTRControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 13),
    _E1CfgDataPort2DTRControl_Type()
)
e1CfgDataPort2DTRControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgDataPort2DTRControl.setStatus("mandatory")


class _E1CfgDataPort2RTSControl_Type(Integer32):
    """Custom type e1CfgDataPort2RTSControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtsForced", 2),
          ("rtsNormal", 1))
    )


_E1CfgDataPort2RTSControl_Type.__name__ = "Integer32"
_E1CfgDataPort2RTSControl_Object = MibScalar
e1CfgDataPort2RTSControl = _E1CfgDataPort2RTSControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 14),
    _E1CfgDataPort2RTSControl_Type()
)
e1CfgDataPort2RTSControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgDataPort2RTSControl.setStatus("mandatory")


class _E1CfgCCMLinkA1Rate_Type(Integer32):
    """Custom type e1CfgCCMLinkA1Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_E1CfgCCMLinkA1Rate_Type.__name__ = "Integer32"
_E1CfgCCMLinkA1Rate_Object = MibScalar
e1CfgCCMLinkA1Rate = _E1CfgCCMLinkA1Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 15),
    _E1CfgCCMLinkA1Rate_Type()
)
e1CfgCCMLinkA1Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgCCMLinkA1Rate.setStatus("mandatory")


class _E1CfgCCMLinkA2Rate_Type(Integer32):
    """Custom type e1CfgCCMLinkA2Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_E1CfgCCMLinkA2Rate_Type.__name__ = "Integer32"
_E1CfgCCMLinkA2Rate_Object = MibScalar
e1CfgCCMLinkA2Rate = _E1CfgCCMLinkA2Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 16),
    _E1CfgCCMLinkA2Rate_Type()
)
e1CfgCCMLinkA2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgCCMLinkA2Rate.setStatus("mandatory")


class _E1CfgCCMLinkA3Rate_Type(Integer32):
    """Custom type e1CfgCCMLinkA3Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_E1CfgCCMLinkA3Rate_Type.__name__ = "Integer32"
_E1CfgCCMLinkA3Rate_Object = MibScalar
e1CfgCCMLinkA3Rate = _E1CfgCCMLinkA3Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 17),
    _E1CfgCCMLinkA3Rate_Type()
)
e1CfgCCMLinkA3Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgCCMLinkA3Rate.setStatus("mandatory")


class _E1CfgCCMLinkA4Rate_Type(Integer32):
    """Custom type e1CfgCCMLinkA4Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_E1CfgCCMLinkA4Rate_Type.__name__ = "Integer32"
_E1CfgCCMLinkA4Rate_Object = MibScalar
e1CfgCCMLinkA4Rate = _E1CfgCCMLinkA4Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 18),
    _E1CfgCCMLinkA4Rate_Type()
)
e1CfgCCMLinkA4Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgCCMLinkA4Rate.setStatus("mandatory")


class _E1CfgCCMLinkA5Rate_Type(Integer32):
    """Custom type e1CfgCCMLinkA5Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_E1CfgCCMLinkA5Rate_Type.__name__ = "Integer32"
_E1CfgCCMLinkA5Rate_Object = MibScalar
e1CfgCCMLinkA5Rate = _E1CfgCCMLinkA5Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 19),
    _E1CfgCCMLinkA5Rate_Type()
)
e1CfgCCMLinkA5Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgCCMLinkA5Rate.setStatus("mandatory")


class _E1CfgCCMLinkA6Rate_Type(Integer32):
    """Custom type e1CfgCCMLinkA6Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleOf56kbps", 2),
          ("multipleOf64kbps", 1))
    )


_E1CfgCCMLinkA6Rate_Type.__name__ = "Integer32"
_E1CfgCCMLinkA6Rate_Object = MibScalar
e1CfgCCMLinkA6Rate = _E1CfgCCMLinkA6Rate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 20),
    _E1CfgCCMLinkA6Rate_Type()
)
e1CfgCCMLinkA6Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgCCMLinkA6Rate.setStatus("mandatory")


class _E1CfgSystemClockSource_Type(Integer32):
    """Custom type e1CfgSystemClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clockDerivedL1", 1),
          ("clockDerivedL2", 2),
          ("internalClocking", 3))
    )


_E1CfgSystemClockSource_Type.__name__ = "Integer32"
_E1CfgSystemClockSource_Object = MibScalar
e1CfgSystemClockSource = _E1CfgSystemClockSource_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 21),
    _E1CfgSystemClockSource_Type()
)
e1CfgSystemClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgSystemClockSource.setStatus("mandatory")


class _E1CfgL1Crc4_Type(Integer32):
    """Custom type e1CfgL1Crc4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_E1CfgL1Crc4_Type.__name__ = "Integer32"
_E1CfgL1Crc4_Object = MibScalar
e1CfgL1Crc4 = _E1CfgL1Crc4_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 22),
    _E1CfgL1Crc4_Type()
)
e1CfgL1Crc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgL1Crc4.setStatus("mandatory")


class _E1CfgL2Crc4_Type(Integer32):
    """Custom type e1CfgL2Crc4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_E1CfgL2Crc4_Type.__name__ = "Integer32"
_E1CfgL2Crc4_Object = MibScalar
e1CfgL2Crc4 = _E1CfgL2Crc4_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 23),
    _E1CfgL2Crc4_Type()
)
e1CfgL2Crc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1CfgL2Crc4.setStatus("mandatory")


class _E1CfgL1Config_Type(Integer32):
    """Custom type e1CfgL1Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commit", 2),
          ("init", 1))
    )


_E1CfgL1Config_Type.__name__ = "Integer32"
_E1CfgL1Config_Object = MibScalar
e1CfgL1Config = _E1CfgL1Config_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 24),
    _E1CfgL1Config_Type()
)
e1CfgL1Config.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    e1CfgL1Config.setStatus("mandatory")


class _E1CfgL2Config_Type(Integer32):
    """Custom type e1CfgL2Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commit", 2),
          ("init", 1))
    )


_E1CfgL2Config_Type.__name__ = "Integer32"
_E1CfgL2Config_Object = MibScalar
e1CfgL2Config = _E1CfgL2Config_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 3, 25),
    _E1CfgL2Config_Type()
)
e1CfgL2Config.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    e1CfgL2Config.setStatus("mandatory")
_E1FlashControlTable_Object = MibTable
e1FlashControlTable = _E1FlashControlTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 4)
)
if mibBuilder.loadTexts:
    e1FlashControlTable.setStatus("mandatory")
_E1FlashControlEntry_Object = MibTableRow
e1FlashControlEntry = _E1FlashControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 4, 1)
)
e1FlashControlEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "e1FlashControlCardNumber"),
)
if mibBuilder.loadTexts:
    e1FlashControlEntry.setStatus("mandatory")


class _E1FlashControlCardNumber_Type(Integer32):
    """Custom type e1FlashControlCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_E1FlashControlCardNumber_Type.__name__ = "Integer32"
_E1FlashControlCardNumber_Object = MibTableColumn
e1FlashControlCardNumber = _E1FlashControlCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 4, 1, 1),
    _E1FlashControlCardNumber_Type()
)
e1FlashControlCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FlashControlCardNumber.setStatus("mandatory")


class _E1FlashControlCommand_Type(Integer32):
    """Custom type e1FlashControlCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eraseCardFlash", 1)
    )


_E1FlashControlCommand_Type.__name__ = "Integer32"
_E1FlashControlCommand_Object = MibTableColumn
e1FlashControlCommand = _E1FlashControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 4, 1, 2),
    _E1FlashControlCommand_Type()
)
e1FlashControlCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    e1FlashControlCommand.setStatus("mandatory")


class _E1FlashControlFlashStatus_Type(Integer32):
    """Custom type e1FlashControlFlashStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bootImageCorrupt", 1),
          ("eraseAborted", 6),
          ("securityViolation", 5),
          ("t1FlashErased", 3),
          ("t1FlashImageInvalid", 4),
          ("t1FlashImageValid", 2))
    )


_E1FlashControlFlashStatus_Type.__name__ = "Integer32"
_E1FlashControlFlashStatus_Object = MibTableColumn
e1FlashControlFlashStatus = _E1FlashControlFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 6, 2, 4, 1, 3),
    _E1FlashControlFlashStatus_Type()
)
e1FlashControlFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FlashControlFlashStatus.setStatus("mandatory")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7)
)
_TrapAlarmEventReportingGroup_ObjectIdentity = ObjectIdentity
trapAlarmEventReportingGroup = _TrapAlarmEventReportingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 1)
)


class _TrapAlarmEventReportingAlarms_Type(Integer32):
    """Custom type trapAlarmEventReportingAlarms based on Integer32"""
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


_TrapAlarmEventReportingAlarms_Type.__name__ = "Integer32"
_TrapAlarmEventReportingAlarms_Object = MibScalar
trapAlarmEventReportingAlarms = _TrapAlarmEventReportingAlarms_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 1, 1),
    _TrapAlarmEventReportingAlarms_Type()
)
trapAlarmEventReportingAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAlarmEventReportingAlarms.setStatus("mandatory")


class _TrapAlarmEventReportingEvents_Type(Integer32):
    """Custom type trapAlarmEventReportingEvents based on Integer32"""
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


_TrapAlarmEventReportingEvents_Type.__name__ = "Integer32"
_TrapAlarmEventReportingEvents_Object = MibScalar
trapAlarmEventReportingEvents = _TrapAlarmEventReportingEvents_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 1, 2),
    _TrapAlarmEventReportingEvents_Type()
)
trapAlarmEventReportingEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAlarmEventReportingEvents.setStatus("mandatory")


class _TrapEventsCollectionInterval_Type(Integer32):
    """Custom type trapEventsCollectionInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TrapEventsCollectionInterval_Type.__name__ = "Integer32"
_TrapEventsCollectionInterval_Object = MibScalar
trapEventsCollectionInterval = _TrapEventsCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 2),
    _TrapEventsCollectionInterval_Type()
)
trapEventsCollectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapEventsCollectionInterval.setStatus("mandatory")
_TrapSubsTable_Object = MibTable
trapSubsTable = _TrapSubsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 3)
)
if mibBuilder.loadTexts:
    trapSubsTable.setStatus("mandatory")
_TrapSubsEntry_Object = MibTableRow
trapSubsEntry = _TrapSubsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 3, 1)
)
trapSubsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "trapSubsIPAddress"),
)
if mibBuilder.loadTexts:
    trapSubsEntry.setStatus("mandatory")
_TrapSubsIPAddress_Type = IpAddress
_TrapSubsIPAddress_Object = MibTableColumn
trapSubsIPAddress = _TrapSubsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 3, 1, 1),
    _TrapSubsIPAddress_Type()
)
trapSubsIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSubsIPAddress.setStatus("mandatory")
_TrapSubsCommunityString_Type = DisplayString
_TrapSubsCommunityString_Object = MibTableColumn
trapSubsCommunityString = _TrapSubsCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 3, 1, 2),
    _TrapSubsCommunityString_Type()
)
trapSubsCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSubsCommunityString.setStatus("mandatory")


class _TrapSubsAction_Type(Integer32):
    """Custom type trapSubsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancelSubscription", 2),
          ("subscribe", 1))
    )


_TrapSubsAction_Type.__name__ = "Integer32"
_TrapSubsAction_Object = MibTableColumn
trapSubsAction = _TrapSubsAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 3, 1, 3),
    _TrapSubsAction_Type()
)
trapSubsAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    trapSubsAction.setStatus("mandatory")
_TrapCfgAlarmEventsPortGroup_ObjectIdentity = ObjectIdentity
trapCfgAlarmEventsPortGroup = _TrapCfgAlarmEventsPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 4)
)


class _TrapCfgTrapPort_Type(Integer32):
    """Custom type trapCfgTrapPort based on Integer32"""
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
        *(("externalModem", 4),
          ("localCommandPort", 1),
          ("localLogPort", 2),
          ("remoteNode", 3))
    )


_TrapCfgTrapPort_Type.__name__ = "Integer32"
_TrapCfgTrapPort_Object = MibScalar
trapCfgTrapPort = _TrapCfgTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 4, 1),
    _TrapCfgTrapPort_Type()
)
trapCfgTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCfgTrapPort.setStatus("mandatory")


class _TrapCfgExtModemPriority_Type(Integer32):
    """Custom type trapCfgExtModemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_TrapCfgExtModemPriority_Type.__name__ = "Integer32"
_TrapCfgExtModemPriority_Object = MibScalar
trapCfgExtModemPriority = _TrapCfgExtModemPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 4, 2),
    _TrapCfgExtModemPriority_Type()
)
trapCfgExtModemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCfgExtModemPriority.setStatus("mandatory")


class _TrapCfgExtAlarmRelay_Type(Integer32):
    """Custom type trapCfgExtAlarmRelay based on Integer32"""
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


_TrapCfgExtAlarmRelay_Type.__name__ = "Integer32"
_TrapCfgExtAlarmRelay_Object = MibScalar
trapCfgExtAlarmRelay = _TrapCfgExtAlarmRelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 5),
    _TrapCfgExtAlarmRelay_Type()
)
trapCfgExtAlarmRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCfgExtAlarmRelay.setStatus("mandatory")
_TrapNodeName_Type = DisplayString
_TrapNodeName_Object = MibScalar
trapNodeName = _TrapNodeName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 6),
    _TrapNodeName_Type()
)
trapNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapNodeName.setStatus("mandatory")
_TrapCardNumber_Type = Integer32
_TrapCardNumber_Object = MibScalar
trapCardNumber = _TrapCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 7),
    _TrapCardNumber_Type()
)
trapCardNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapCardNumber.setStatus("mandatory")
_TrapChannelNumber_Type = Integer32
_TrapChannelNumber_Object = MibScalar
trapChannelNumber = _TrapChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 8),
    _TrapChannelNumber_Type()
)
trapChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapChannelNumber.setStatus("mandatory")
_TrapFirstNodeName_Type = DisplayString
_TrapFirstNodeName_Object = MibScalar
trapFirstNodeName = _TrapFirstNodeName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 9),
    _TrapFirstNodeName_Type()
)
trapFirstNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapFirstNodeName.setStatus("mandatory")
_TrapFirstCardNumberOrInternalFacilityIndication_Type = Integer32
_TrapFirstCardNumberOrInternalFacilityIndication_Object = MibScalar
trapFirstCardNumberOrInternalFacilityIndication = _TrapFirstCardNumberOrInternalFacilityIndication_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 10),
    _TrapFirstCardNumberOrInternalFacilityIndication_Type()
)
trapFirstCardNumberOrInternalFacilityIndication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapFirstCardNumberOrInternalFacilityIndication.setStatus("mandatory")
_TrapFirstChannelNumberOrInternalFacility_Type = Integer32
_TrapFirstChannelNumberOrInternalFacility_Object = MibScalar
trapFirstChannelNumberOrInternalFacility = _TrapFirstChannelNumberOrInternalFacility_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 11),
    _TrapFirstChannelNumberOrInternalFacility_Type()
)
trapFirstChannelNumberOrInternalFacility.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapFirstChannelNumberOrInternalFacility.setStatus("mandatory")
_TrapSecondNodeName_Type = DisplayString
_TrapSecondNodeName_Object = MibScalar
trapSecondNodeName = _TrapSecondNodeName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 12),
    _TrapSecondNodeName_Type()
)
trapSecondNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapSecondNodeName.setStatus("mandatory")


class _TrapSecondCardNumberOrInternalFacilityIndication_Type(Integer32):
    """Custom type trapSecondCardNumberOrInternalFacilityIndication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TrapSecondCardNumberOrInternalFacilityIndication_Type.__name__ = "Integer32"
_TrapSecondCardNumberOrInternalFacilityIndication_Object = MibScalar
trapSecondCardNumberOrInternalFacilityIndication = _TrapSecondCardNumberOrInternalFacilityIndication_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 13),
    _TrapSecondCardNumberOrInternalFacilityIndication_Type()
)
trapSecondCardNumberOrInternalFacilityIndication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapSecondCardNumberOrInternalFacilityIndication.setStatus("mandatory")
_TrapSecondChannelNumberOrInternalFacility_Type = Integer32
_TrapSecondChannelNumberOrInternalFacility_Object = MibScalar
trapSecondChannelNumberOrInternalFacility = _TrapSecondChannelNumberOrInternalFacility_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 14),
    _TrapSecondChannelNumberOrInternalFacility_Type()
)
trapSecondChannelNumberOrInternalFacility.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapSecondChannelNumberOrInternalFacility.setStatus("mandatory")
_TrapClassRequestedOrMatrixRequest_Type = Integer32
_TrapClassRequestedOrMatrixRequest_Object = MibScalar
trapClassRequestedOrMatrixRequest = _TrapClassRequestedOrMatrixRequest_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 15),
    _TrapClassRequestedOrMatrixRequest_Type()
)
trapClassRequestedOrMatrixRequest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapClassRequestedOrMatrixRequest.setStatus("mandatory")


class _TrapLinkType_Type(Integer32):
    """Custom type trapLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameRelayDLCI", 2),
          ("physicalLink", 1))
    )


_TrapLinkType_Type.__name__ = "Integer32"
_TrapLinkType_Object = MibScalar
trapLinkType = _TrapLinkType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 16),
    _TrapLinkType_Type()
)
trapLinkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapLinkType.setStatus("mandatory")
_TrapDLCINumber_Type = Integer32
_TrapDLCINumber_Object = MibScalar
trapDLCINumber = _TrapDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 17),
    _TrapDLCINumber_Type()
)
trapDLCINumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDLCINumber.setStatus("mandatory")
_TrapDLCIFirstLinkCardNumber_Type = Integer32
_TrapDLCIFirstLinkCardNumber_Object = MibScalar
trapDLCIFirstLinkCardNumber = _TrapDLCIFirstLinkCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 18),
    _TrapDLCIFirstLinkCardNumber_Type()
)
trapDLCIFirstLinkCardNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDLCIFirstLinkCardNumber.setStatus("mandatory")
_TrapDLCIFirstLinkChannelNumber_Type = Integer32
_TrapDLCIFirstLinkChannelNumber_Object = MibScalar
trapDLCIFirstLinkChannelNumber = _TrapDLCIFirstLinkChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 19),
    _TrapDLCIFirstLinkChannelNumber_Type()
)
trapDLCIFirstLinkChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDLCIFirstLinkChannelNumber.setStatus("mandatory")
_TrapDLCIFirstLinkDLCINumber_Type = Integer32
_TrapDLCIFirstLinkDLCINumber_Object = MibScalar
trapDLCIFirstLinkDLCINumber = _TrapDLCIFirstLinkDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 20),
    _TrapDLCIFirstLinkDLCINumber_Type()
)
trapDLCIFirstLinkDLCINumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDLCIFirstLinkDLCINumber.setStatus("mandatory")
_TrapDLCISecondLinkCardNumber_Type = Integer32
_TrapDLCISecondLinkCardNumber_Object = MibScalar
trapDLCISecondLinkCardNumber = _TrapDLCISecondLinkCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 21),
    _TrapDLCISecondLinkCardNumber_Type()
)
trapDLCISecondLinkCardNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDLCISecondLinkCardNumber.setStatus("mandatory")
_TrapDLCISecondLinkChannelNumber_Type = Integer32
_TrapDLCISecondLinkChannelNumber_Object = MibScalar
trapDLCISecondLinkChannelNumber = _TrapDLCISecondLinkChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 22),
    _TrapDLCISecondLinkChannelNumber_Type()
)
trapDLCISecondLinkChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDLCISecondLinkChannelNumber.setStatus("mandatory")
_TrapDLCISecondLinkDLCINumber_Type = Integer32
_TrapDLCISecondLinkDLCINumber_Object = MibScalar
trapDLCISecondLinkDLCINumber = _TrapDLCISecondLinkDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 7, 23),
    _TrapDLCISecondLinkDLCINumber_Type()
)
trapDLCISecondLinkDLCINumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDLCISecondLinkDLCINumber.setStatus("mandatory")
_Proxy_ObjectIdentity = ObjectIdentity
proxy = _Proxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8)
)
_PxyVersionNumber_Type = DisplayString
_PxyVersionNumber_Object = MibScalar
pxyVersionNumber = _PxyVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 1),
    _PxyVersionNumber_Type()
)
pxyVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxyVersionNumber.setStatus("mandatory")


class _PxyCfgProxySwitch_Type(Integer32):
    """Custom type pxyCfgProxySwitch based on Integer32"""
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


_PxyCfgProxySwitch_Type.__name__ = "Integer32"
_PxyCfgProxySwitch_Object = MibScalar
pxyCfgProxySwitch = _PxyCfgProxySwitch_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 2),
    _PxyCfgProxySwitch_Type()
)
pxyCfgProxySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxyCfgProxySwitch.setStatus("mandatory")
_PxyAddressMapTableNumber_Type = Integer32
_PxyAddressMapTableNumber_Object = MibScalar
pxyAddressMapTableNumber = _PxyAddressMapTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 3),
    _PxyAddressMapTableNumber_Type()
)
pxyAddressMapTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxyAddressMapTableNumber.setStatus("mandatory")
_PxyAddressMapTable_Object = MibTable
pxyAddressMapTable = _PxyAddressMapTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 4)
)
if mibBuilder.loadTexts:
    pxyAddressMapTable.setStatus("mandatory")
_PxyAddressMapEntry_Object = MibTableRow
pxyAddressMapEntry = _PxyAddressMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 4, 1)
)
pxyAddressMapEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "pxyAddressMapNodeNumber"),
)
if mibBuilder.loadTexts:
    pxyAddressMapEntry.setStatus("mandatory")
_PxyAddressMapNodeNumber_Type = Integer32
_PxyAddressMapNodeNumber_Object = MibTableColumn
pxyAddressMapNodeNumber = _PxyAddressMapNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 4, 1, 1),
    _PxyAddressMapNodeNumber_Type()
)
pxyAddressMapNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxyAddressMapNodeNumber.setStatus("mandatory")


class _PxyAddressMapEntryStatus_Type(Integer32):
    """Custom type pxyAddressMapEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_PxyAddressMapEntryStatus_Type.__name__ = "Integer32"
_PxyAddressMapEntryStatus_Object = MibTableColumn
pxyAddressMapEntryStatus = _PxyAddressMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 4, 1, 2),
    _PxyAddressMapEntryStatus_Type()
)
pxyAddressMapEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxyAddressMapEntryStatus.setStatus("mandatory")


class _PxyAddressMapNodeNameAndCommunity_Type(DisplayString):
    """Custom type pxyAddressMapNodeNameAndCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_PxyAddressMapNodeNameAndCommunity_Type.__name__ = "DisplayString"
_PxyAddressMapNodeNameAndCommunity_Object = MibTableColumn
pxyAddressMapNodeNameAndCommunity = _PxyAddressMapNodeNameAndCommunity_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 4, 1, 3),
    _PxyAddressMapNodeNameAndCommunity_Type()
)
pxyAddressMapNodeNameAndCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxyAddressMapNodeNameAndCommunity.setStatus("mandatory")
_PxyAddressMapChangeNodeNumberTo_Type = Integer32
_PxyAddressMapChangeNodeNumberTo_Object = MibTableColumn
pxyAddressMapChangeNodeNumberTo = _PxyAddressMapChangeNodeNumberTo_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 4, 1, 4),
    _PxyAddressMapChangeNodeNumberTo_Type()
)
pxyAddressMapChangeNodeNumberTo.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pxyAddressMapChangeNodeNumberTo.setStatus("mandatory")
_PxySupportedVersionTable_Object = MibTable
pxySupportedVersionTable = _PxySupportedVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 5)
)
if mibBuilder.loadTexts:
    pxySupportedVersionTable.setStatus("mandatory")
_PxySupportedVersionEntry_Object = MibTableRow
pxySupportedVersionEntry = _PxySupportedVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 5, 1)
)
pxySupportedVersionEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "pxySupportedIndex"),
)
if mibBuilder.loadTexts:
    pxySupportedVersionEntry.setStatus("mandatory")
_PxySupportedIndex_Type = Integer32
_PxySupportedIndex_Object = MibTableColumn
pxySupportedIndex = _PxySupportedIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 5, 1, 1),
    _PxySupportedIndex_Type()
)
pxySupportedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxySupportedIndex.setStatus("mandatory")


class _PxySupportedVersionNumber_Type(Integer32):
    """Custom type pxySupportedVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("phase5dot0", 1),
          ("phase5dot0plus", 2))
    )


_PxySupportedVersionNumber_Type.__name__ = "Integer32"
_PxySupportedVersionNumber_Object = MibTableColumn
pxySupportedVersionNumber = _PxySupportedVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 5, 1, 2),
    _PxySupportedVersionNumber_Type()
)
pxySupportedVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxySupportedVersionNumber.setStatus("mandatory")
_PxyStatisticsLastNodeServed_Type = Integer32
_PxyStatisticsLastNodeServed_Object = MibScalar
pxyStatisticsLastNodeServed = _PxyStatisticsLastNodeServed_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 6),
    _PxyStatisticsLastNodeServed_Type()
)
pxyStatisticsLastNodeServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxyStatisticsLastNodeServed.setStatus("mandatory")
_PxyStatisticsLastErrorNode_Type = Integer32
_PxyStatisticsLastErrorNode_Object = MibScalar
pxyStatisticsLastErrorNode = _PxyStatisticsLastErrorNode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 7),
    _PxyStatisticsLastErrorNode_Type()
)
pxyStatisticsLastErrorNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxyStatisticsLastErrorNode.setStatus("mandatory")
_PxyStatisticsLastSNMPError_Type = Integer32
_PxyStatisticsLastSNMPError_Object = MibScalar
pxyStatisticsLastSNMPError = _PxyStatisticsLastSNMPError_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 8),
    _PxyStatisticsLastSNMPError_Type()
)
pxyStatisticsLastSNMPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxyStatisticsLastSNMPError.setStatus("mandatory")
_PxyStatisticsLastErrorReturnCode_Type = Integer32
_PxyStatisticsLastErrorReturnCode_Object = MibScalar
pxyStatisticsLastErrorReturnCode = _PxyStatisticsLastErrorReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 9),
    _PxyStatisticsLastErrorReturnCode_Type()
)
pxyStatisticsLastErrorReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxyStatisticsLastErrorReturnCode.setStatus("mandatory")
_PxyStatisticsTotalRequests_Type = Counter32
_PxyStatisticsTotalRequests_Object = MibScalar
pxyStatisticsTotalRequests = _PxyStatisticsTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 10),
    _PxyStatisticsTotalRequests_Type()
)
pxyStatisticsTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxyStatisticsTotalRequests.setStatus("mandatory")
_PxyStatisticsTotalInternalTraps_Type = Counter32
_PxyStatisticsTotalInternalTraps_Object = MibScalar
pxyStatisticsTotalInternalTraps = _PxyStatisticsTotalInternalTraps_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 11),
    _PxyStatisticsTotalInternalTraps_Type()
)
pxyStatisticsTotalInternalTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxyStatisticsTotalInternalTraps.setStatus("mandatory")
_PxyPPPTotalCounts_Type = Counter32
_PxyPPPTotalCounts_Object = MibScalar
pxyPPPTotalCounts = _PxyPPPTotalCounts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 12),
    _PxyPPPTotalCounts_Type()
)
pxyPPPTotalCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxyPPPTotalCounts.setStatus("mandatory")
_PxyPPPRejectCounts_Type = Counter32
_PxyPPPRejectCounts_Object = MibScalar
pxyPPPRejectCounts = _PxyPPPRejectCounts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 13),
    _PxyPPPRejectCounts_Type()
)
pxyPPPRejectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxyPPPRejectCounts.setStatus("mandatory")


class _PxyCacheUpdate_Type(Integer32):
    """Custom type pxyCacheUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cdChanTable", 1)
    )


_PxyCacheUpdate_Type.__name__ = "Integer32"
_PxyCacheUpdate_Object = MibScalar
pxyCacheUpdate = _PxyCacheUpdate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 14),
    _PxyCacheUpdate_Type()
)
pxyCacheUpdate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pxyCacheUpdate.setStatus("mandatory")


class _PxyNetworkAccessNodeName_Type(DisplayString):
    """Custom type pxyNetworkAccessNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_PxyNetworkAccessNodeName_Type.__name__ = "DisplayString"
_PxyNetworkAccessNodeName_Object = MibScalar
pxyNetworkAccessNodeName = _PxyNetworkAccessNodeName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 3, 8, 15),
    _PxyNetworkAccessNodeName_Type()
)
pxyNetworkAccessNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxyNetworkAccessNodeName.setStatus("mandatory")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4)
)
_NodeResetGroup_ObjectIdentity = ObjectIdentity
nodeResetGroup = _NodeResetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 1)
)


class _NodeResetCode_Type(Integer32):
    """Custom type nodeResetCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coldRestart", 1),
          ("warmRestart", 2))
    )


_NodeResetCode_Type.__name__ = "Integer32"
_NodeResetCode_Object = MibScalar
nodeResetCode = _NodeResetCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 1, 1),
    _NodeResetCode_Type()
)
nodeResetCode.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nodeResetCode.setStatus("mandatory")


class _NodeResetType_Type(Integer32):
    """Custom type nodeResetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reloadSoftwareFromFlash", 2),
          ("restartCurrentSoftware", 1))
    )


_NodeResetType_Type.__name__ = "Integer32"
_NodeResetType_Object = MibScalar
nodeResetType = _NodeResetType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 1, 2),
    _NodeResetType_Type()
)
nodeResetType.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nodeResetType.setStatus("mandatory")
_AsyncResetTable_Object = MibTable
asyncResetTable = _AsyncResetTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    asyncResetTable.setStatus("mandatory")
_AsyncResetEntry_Object = MibTableRow
asyncResetEntry = _AsyncResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 2, 1)
)
asyncResetEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "asyncResetCardNumber"),
    (0, "MICOM-NODE-MIB", "asyncResetChannelNumber"),
)
if mibBuilder.loadTexts:
    asyncResetEntry.setStatus("mandatory")


class _AsyncResetCardNumber_Type(Integer32):
    """Custom type asyncResetCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AsyncResetCardNumber_Type.__name__ = "Integer32"
_AsyncResetCardNumber_Object = MibTableColumn
asyncResetCardNumber = _AsyncResetCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 2, 1, 1),
    _AsyncResetCardNumber_Type()
)
asyncResetCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncResetCardNumber.setStatus("mandatory")


class _AsyncResetChannelNumber_Type(Integer32):
    """Custom type asyncResetChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AsyncResetChannelNumber_Type.__name__ = "Integer32"
_AsyncResetChannelNumber_Object = MibTableColumn
asyncResetChannelNumber = _AsyncResetChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 2, 1, 2),
    _AsyncResetChannelNumber_Type()
)
asyncResetChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncResetChannelNumber.setStatus("mandatory")


class _AsyncResetCommand_Type(Integer32):
    """Custom type asyncResetCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetChannel", 1)
    )


_AsyncResetCommand_Type.__name__ = "Integer32"
_AsyncResetCommand_Object = MibTableColumn
asyncResetCommand = _AsyncResetCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 2, 1, 3),
    _AsyncResetCommand_Type()
)
asyncResetCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    asyncResetCommand.setStatus("mandatory")
_SyncResetTable_Object = MibTable
syncResetTable = _SyncResetTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    syncResetTable.setStatus("mandatory")
_SyncResetEntry_Object = MibTableRow
syncResetEntry = _SyncResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 3, 1)
)
syncResetEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "syncResetCardNumber"),
    (0, "MICOM-NODE-MIB", "syncResetChannelNumber"),
)
if mibBuilder.loadTexts:
    syncResetEntry.setStatus("mandatory")


class _SyncResetCardNumber_Type(Integer32):
    """Custom type syncResetCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SyncResetCardNumber_Type.__name__ = "Integer32"
_SyncResetCardNumber_Object = MibTableColumn
syncResetCardNumber = _SyncResetCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 3, 1, 1),
    _SyncResetCardNumber_Type()
)
syncResetCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncResetCardNumber.setStatus("mandatory")


class _SyncResetChannelNumber_Type(Integer32):
    """Custom type syncResetChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SyncResetChannelNumber_Type.__name__ = "Integer32"
_SyncResetChannelNumber_Object = MibTableColumn
syncResetChannelNumber = _SyncResetChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 3, 1, 2),
    _SyncResetChannelNumber_Type()
)
syncResetChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncResetChannelNumber.setStatus("mandatory")


class _SyncResetCommand_Type(Integer32):
    """Custom type syncResetCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetChannel", 1)
    )


_SyncResetCommand_Type.__name__ = "Integer32"
_SyncResetCommand_Object = MibTableColumn
syncResetCommand = _SyncResetCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 3, 1, 3),
    _SyncResetCommand_Type()
)
syncResetCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    syncResetCommand.setStatus("mandatory")
_VoiceResetTable_Object = MibTable
voiceResetTable = _VoiceResetTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    voiceResetTable.setStatus("mandatory")
_VoiceResetEntry_Object = MibTableRow
voiceResetEntry = _VoiceResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 4, 1)
)
voiceResetEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "voiceResetCardNumber"),
    (0, "MICOM-NODE-MIB", "voiceResetChannelNumber"),
)
if mibBuilder.loadTexts:
    voiceResetEntry.setStatus("mandatory")


class _VoiceResetCardNumber_Type(Integer32):
    """Custom type voiceResetCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_VoiceResetCardNumber_Type.__name__ = "Integer32"
_VoiceResetCardNumber_Object = MibTableColumn
voiceResetCardNumber = _VoiceResetCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 4, 1, 1),
    _VoiceResetCardNumber_Type()
)
voiceResetCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceResetCardNumber.setStatus("mandatory")
_VoiceResetChannelNumber_Type = Integer32
_VoiceResetChannelNumber_Object = MibTableColumn
voiceResetChannelNumber = _VoiceResetChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 4, 1, 2),
    _VoiceResetChannelNumber_Type()
)
voiceResetChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceResetChannelNumber.setStatus("mandatory")


class _VoiceResetCommand_Type(Integer32):
    """Custom type voiceResetCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetVoiceChannel", 1)
    )


_VoiceResetCommand_Type.__name__ = "Integer32"
_VoiceResetCommand_Object = MibTableColumn
voiceResetCommand = _VoiceResetCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 4, 1, 3),
    _VoiceResetCommand_Type()
)
voiceResetCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    voiceResetCommand.setStatus("mandatory")
_LinkResetTable_Object = MibTable
linkResetTable = _LinkResetTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    linkResetTable.setStatus("mandatory")
_LinkResetEntry_Object = MibTableRow
linkResetEntry = _LinkResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 5, 1)
)
linkResetEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "linkResetCardNumber"),
    (0, "MICOM-NODE-MIB", "linkResetChannelNumber"),
)
if mibBuilder.loadTexts:
    linkResetEntry.setStatus("mandatory")


class _LinkResetCardNumber_Type(Integer32):
    """Custom type linkResetCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_LinkResetCardNumber_Type.__name__ = "Integer32"
_LinkResetCardNumber_Object = MibTableColumn
linkResetCardNumber = _LinkResetCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 5, 1, 1),
    _LinkResetCardNumber_Type()
)
linkResetCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkResetCardNumber.setStatus("mandatory")


class _LinkResetChannelNumber_Type(Integer32):
    """Custom type linkResetChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_LinkResetChannelNumber_Type.__name__ = "Integer32"
_LinkResetChannelNumber_Object = MibTableColumn
linkResetChannelNumber = _LinkResetChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 5, 1, 2),
    _LinkResetChannelNumber_Type()
)
linkResetChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkResetChannelNumber.setStatus("mandatory")


class _LinkResetCommand_Type(Integer32):
    """Custom type linkResetCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetLink", 1)
    )


_LinkResetCommand_Type.__name__ = "Integer32"
_LinkResetCommand_Object = MibTableColumn
linkResetCommand = _LinkResetCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 5, 1, 3),
    _LinkResetCommand_Type()
)
linkResetCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    linkResetCommand.setStatus("mandatory")


class _ClearLatchedAlarms_Type(Integer32):
    """Custom type clearLatchedAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearLatchedAlarms", 1)
    )


_ClearLatchedAlarms_Type.__name__ = "Integer32"
_ClearLatchedAlarms_Object = MibScalar
clearLatchedAlarms = _ClearLatchedAlarms_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 6),
    _ClearLatchedAlarms_Type()
)
clearLatchedAlarms.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    clearLatchedAlarms.setStatus("mandatory")
_PppLinkOperationGroup_ObjectIdentity = ObjectIdentity
pppLinkOperationGroup = _PppLinkOperationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 7)
)


class _PppLinkOperationAction_Type(Integer32):
    """Custom type pppLinkOperationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resumeNormalOperation", 1)
    )


_PppLinkOperationAction_Type.__name__ = "Integer32"
_PppLinkOperationAction_Object = MibScalar
pppLinkOperationAction = _PppLinkOperationAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 7, 1),
    _PppLinkOperationAction_Type()
)
pppLinkOperationAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pppLinkOperationAction.setStatus("mandatory")


class _PppLinkTimeOutAction_Type(Integer32):
    """Custom type pppLinkTimeOutAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disableLinkTimeout", 1)
    )


_PppLinkTimeOutAction_Type.__name__ = "Integer32"
_PppLinkTimeOutAction_Object = MibScalar
pppLinkTimeOutAction = _PppLinkTimeOutAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 7, 2),
    _PppLinkTimeOutAction_Type()
)
pppLinkTimeOutAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pppLinkTimeOutAction.setStatus("mandatory")


class _PppLinkDumpAction_Type(Integer32):
    """Custom type pppLinkDumpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dumpRejectedNmsCmdToLogport", 1)
    )


_PppLinkDumpAction_Type.__name__ = "Integer32"
_PppLinkDumpAction_Object = MibScalar
pppLinkDumpAction = _PppLinkDumpAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 7, 3),
    _PppLinkDumpAction_Type()
)
pppLinkDumpAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pppLinkDumpAction.setStatus("mandatory")


class _FlashEPROMCommand_Type(Integer32):
    """Custom type flashEPROMCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eraseBankOne", 2),
          ("eraseBankTwo", 3),
          ("eraseBothBanks", 1))
    )


_FlashEPROMCommand_Type.__name__ = "Integer32"
_FlashEPROMCommand_Object = MibScalar
flashEPROMCommand = _FlashEPROMCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 8),
    _FlashEPROMCommand_Type()
)
flashEPROMCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    flashEPROMCommand.setStatus("mandatory")
_VoiceFlashEPROMTable_Object = MibTable
voiceFlashEPROMTable = _VoiceFlashEPROMTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 9)
)
if mibBuilder.loadTexts:
    voiceFlashEPROMTable.setStatus("mandatory")
_VoiceFlashEPROMEntry_Object = MibTableRow
voiceFlashEPROMEntry = _VoiceFlashEPROMEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 9, 1)
)
voiceFlashEPROMEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "voiceFlashEPROMCardNumber"),
    (0, "MICOM-NODE-MIB", "voiceFlashEPROMChannelNumber"),
)
if mibBuilder.loadTexts:
    voiceFlashEPROMEntry.setStatus("mandatory")


class _VoiceFlashEPROMCardNumber_Type(Integer32):
    """Custom type voiceFlashEPROMCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_VoiceFlashEPROMCardNumber_Type.__name__ = "Integer32"
_VoiceFlashEPROMCardNumber_Object = MibTableColumn
voiceFlashEPROMCardNumber = _VoiceFlashEPROMCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 9, 1, 1),
    _VoiceFlashEPROMCardNumber_Type()
)
voiceFlashEPROMCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFlashEPROMCardNumber.setStatus("mandatory")


class _VoiceFlashEPROMChannelNumber_Type(Integer32):
    """Custom type voiceFlashEPROMChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_VoiceFlashEPROMChannelNumber_Type.__name__ = "Integer32"
_VoiceFlashEPROMChannelNumber_Object = MibTableColumn
voiceFlashEPROMChannelNumber = _VoiceFlashEPROMChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 9, 1, 2),
    _VoiceFlashEPROMChannelNumber_Type()
)
voiceFlashEPROMChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceFlashEPROMChannelNumber.setStatus("mandatory")


class _VoiceFlashEPROMCommand_Type(Integer32):
    """Custom type voiceFlashEPROMCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eraseFlash", 1)
    )


_VoiceFlashEPROMCommand_Type.__name__ = "Integer32"
_VoiceFlashEPROMCommand_Object = MibTableColumn
voiceFlashEPROMCommand = _VoiceFlashEPROMCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 9, 1, 3),
    _VoiceFlashEPROMCommand_Type()
)
voiceFlashEPROMCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    voiceFlashEPROMCommand.setStatus("mandatory")
_LanCardResetTable_Object = MibTable
lanCardResetTable = _LanCardResetTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 10)
)
if mibBuilder.loadTexts:
    lanCardResetTable.setStatus("mandatory")
_LanCardResetEntry_Object = MibTableRow
lanCardResetEntry = _LanCardResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 10, 1)
)
lanCardResetEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "lanCardResetCardNumber"),
)
if mibBuilder.loadTexts:
    lanCardResetEntry.setStatus("mandatory")


class _LanCardResetCardNumber_Type(Integer32):
    """Custom type lanCardResetCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_LanCardResetCardNumber_Type.__name__ = "Integer32"
_LanCardResetCardNumber_Object = MibTableColumn
lanCardResetCardNumber = _LanCardResetCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 10, 1, 1),
    _LanCardResetCardNumber_Type()
)
lanCardResetCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCardResetCardNumber.setStatus("mandatory")


class _LanCardResetType_Type(Integer32):
    """Custom type lanCardResetType based on Integer32"""
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
        *(("lanToLanDownload", 4),
          ("resetWithCurrentValues", 1),
          ("resetWithDefaultValues", 2),
          ("wanToLanDownload", 3))
    )


_LanCardResetType_Type.__name__ = "Integer32"
_LanCardResetType_Object = MibTableColumn
lanCardResetType = _LanCardResetType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 10, 1, 2),
    _LanCardResetType_Type()
)
lanCardResetType.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    lanCardResetType.setStatus("mandatory")
_ChControlTable_Object = MibTable
chControlTable = _ChControlTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 11)
)
if mibBuilder.loadTexts:
    chControlTable.setStatus("mandatory")
_ChControlEntry_Object = MibTableRow
chControlEntry = _ChControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 11, 1)
)
chControlEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "chControlCardNumber"),
    (0, "MICOM-NODE-MIB", "chControlChannelNumber"),
)
if mibBuilder.loadTexts:
    chControlEntry.setStatus("mandatory")


class _ChControlCardNumber_Type(Integer32):
    """Custom type chControlCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ChControlCardNumber_Type.__name__ = "Integer32"
_ChControlCardNumber_Object = MibTableColumn
chControlCardNumber = _ChControlCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 11, 1, 1),
    _ChControlCardNumber_Type()
)
chControlCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chControlCardNumber.setStatus("mandatory")
_ChControlChannelNumber_Type = Integer32
_ChControlChannelNumber_Object = MibTableColumn
chControlChannelNumber = _ChControlChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 11, 1, 2),
    _ChControlChannelNumber_Type()
)
chControlChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chControlChannelNumber.setStatus("mandatory")


class _ChControlCommand_Type(Integer32):
    """Custom type chControlCommand based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("forcedConnect", 3),
          ("forcedDisconnect", 4))
    )


_ChControlCommand_Type.__name__ = "Integer32"
_ChControlCommand_Object = MibTableColumn
chControlCommand = _ChControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 11, 1, 3),
    _ChControlCommand_Type()
)
chControlCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    chControlCommand.setStatus("mandatory")


class _ChControlForceConnToNodeName_Type(DisplayString):
    """Custom type chControlForceConnToNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ChControlForceConnToNodeName_Type.__name__ = "DisplayString"
_ChControlForceConnToNodeName_Object = MibTableColumn
chControlForceConnToNodeName = _ChControlForceConnToNodeName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 11, 1, 4),
    _ChControlForceConnToNodeName_Type()
)
chControlForceConnToNodeName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    chControlForceConnToNodeName.setStatus("mandatory")


class _ChControlForceConnToCard_Type(Integer32):
    """Custom type chControlForceConnToCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ChControlForceConnToCard_Type.__name__ = "Integer32"
_ChControlForceConnToCard_Object = MibTableColumn
chControlForceConnToCard = _ChControlForceConnToCard_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 11, 1, 5),
    _ChControlForceConnToCard_Type()
)
chControlForceConnToCard.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    chControlForceConnToCard.setStatus("mandatory")
_ChControlForceConnToChannel_Type = Integer32
_ChControlForceConnToChannel_Object = MibTableColumn
chControlForceConnToChannel = _ChControlForceConnToChannel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 11, 1, 6),
    _ChControlForceConnToChannel_Type()
)
chControlForceConnToChannel.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    chControlForceConnToChannel.setStatus("mandatory")
_FrameRelayDLCIResetTable_Object = MibTable
frameRelayDLCIResetTable = _FrameRelayDLCIResetTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 12)
)
if mibBuilder.loadTexts:
    frameRelayDLCIResetTable.setStatus("mandatory")
_FrameRelayDLCIResetEntry_Object = MibTableRow
frameRelayDLCIResetEntry = _FrameRelayDLCIResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 12, 1)
)
frameRelayDLCIResetEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "frameRelayDLCIResetCardNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayDLCIResetChannelNumber"),
)
if mibBuilder.loadTexts:
    frameRelayDLCIResetEntry.setStatus("mandatory")


class _FrameRelayDLCIResetCardNumber_Type(Integer32):
    """Custom type frameRelayDLCIResetCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FrameRelayDLCIResetCardNumber_Type.__name__ = "Integer32"
_FrameRelayDLCIResetCardNumber_Object = MibTableColumn
frameRelayDLCIResetCardNumber = _FrameRelayDLCIResetCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 12, 1, 1),
    _FrameRelayDLCIResetCardNumber_Type()
)
frameRelayDLCIResetCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDLCIResetCardNumber.setStatus("mandatory")


class _FrameRelayDLCIResetChannelNumber_Type(Integer32):
    """Custom type frameRelayDLCIResetChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FrameRelayDLCIResetChannelNumber_Type.__name__ = "Integer32"
_FrameRelayDLCIResetChannelNumber_Object = MibTableColumn
frameRelayDLCIResetChannelNumber = _FrameRelayDLCIResetChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 12, 1, 2),
    _FrameRelayDLCIResetChannelNumber_Type()
)
frameRelayDLCIResetChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayDLCIResetChannelNumber.setStatus("mandatory")
_FrameRelayDLCIResetDLCINumber_Type = Integer32
_FrameRelayDLCIResetDLCINumber_Object = MibTableColumn
frameRelayDLCIResetDLCINumber = _FrameRelayDLCIResetDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 12, 1, 3),
    _FrameRelayDLCIResetDLCINumber_Type()
)
frameRelayDLCIResetDLCINumber.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frameRelayDLCIResetDLCINumber.setStatus("mandatory")
_FrameRelayAllDLCIResetTable_Object = MibTable
frameRelayAllDLCIResetTable = _FrameRelayAllDLCIResetTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 13)
)
if mibBuilder.loadTexts:
    frameRelayAllDLCIResetTable.setStatus("mandatory")
_FrameRelayAllDLCIResetEntry_Object = MibTableRow
frameRelayAllDLCIResetEntry = _FrameRelayAllDLCIResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 13, 1)
)
frameRelayAllDLCIResetEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "frameRelayAllDLCIResetCardNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayAllDLCIResetChannelNumber"),
)
if mibBuilder.loadTexts:
    frameRelayAllDLCIResetEntry.setStatus("mandatory")


class _FrameRelayAllDLCIResetCardNumber_Type(Integer32):
    """Custom type frameRelayAllDLCIResetCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FrameRelayAllDLCIResetCardNumber_Type.__name__ = "Integer32"
_FrameRelayAllDLCIResetCardNumber_Object = MibTableColumn
frameRelayAllDLCIResetCardNumber = _FrameRelayAllDLCIResetCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 13, 1, 1),
    _FrameRelayAllDLCIResetCardNumber_Type()
)
frameRelayAllDLCIResetCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayAllDLCIResetCardNumber.setStatus("mandatory")


class _FrameRelayAllDLCIResetChannelNumber_Type(Integer32):
    """Custom type frameRelayAllDLCIResetChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FrameRelayAllDLCIResetChannelNumber_Type.__name__ = "Integer32"
_FrameRelayAllDLCIResetChannelNumber_Object = MibTableColumn
frameRelayAllDLCIResetChannelNumber = _FrameRelayAllDLCIResetChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 13, 1, 2),
    _FrameRelayAllDLCIResetChannelNumber_Type()
)
frameRelayAllDLCIResetChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayAllDLCIResetChannelNumber.setStatus("mandatory")


class _FrameRelayAllDLCIResetCommand_Type(Integer32):
    """Custom type frameRelayAllDLCIResetCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetAllDLCI", 1)
    )


_FrameRelayAllDLCIResetCommand_Type.__name__ = "Integer32"
_FrameRelayAllDLCIResetCommand_Object = MibTableColumn
frameRelayAllDLCIResetCommand = _FrameRelayAllDLCIResetCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 13, 1, 3),
    _FrameRelayAllDLCIResetCommand_Type()
)
frameRelayAllDLCIResetCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frameRelayAllDLCIResetCommand.setStatus("mandatory")
_T1e1CardResetTable_Object = MibTable
t1e1CardResetTable = _T1e1CardResetTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 14)
)
if mibBuilder.loadTexts:
    t1e1CardResetTable.setStatus("mandatory")
_T1e1CardResetEntry_Object = MibTableRow
t1e1CardResetEntry = _T1e1CardResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 14, 1)
)
t1e1CardResetEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "t1e1CardResetCardNumber"),
)
if mibBuilder.loadTexts:
    t1e1CardResetEntry.setStatus("mandatory")


class _T1e1CardResetCardNumber_Type(Integer32):
    """Custom type t1e1CardResetCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_T1e1CardResetCardNumber_Type.__name__ = "Integer32"
_T1e1CardResetCardNumber_Object = MibTableColumn
t1e1CardResetCardNumber = _T1e1CardResetCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 14, 1, 1),
    _T1e1CardResetCardNumber_Type()
)
t1e1CardResetCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CardResetCardNumber.setStatus("mandatory")


class _T1e1CardResetCommand_Type(Integer32):
    """Custom type t1e1CardResetCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coldReset", 2),
          ("warmReset", 1))
    )


_T1e1CardResetCommand_Type.__name__ = "Integer32"
_T1e1CardResetCommand_Object = MibTableColumn
t1e1CardResetCommand = _T1e1CardResetCommand_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 14, 1, 2),
    _T1e1CardResetCommand_Type()
)
t1e1CardResetCommand.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    t1e1CardResetCommand.setStatus("mandatory")


class _NvflashUpdate_Type(Integer32):
    """Custom type nvflashUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("writeToFlash", 1)
    )


_NvflashUpdate_Type.__name__ = "Integer32"
_NvflashUpdate_Object = MibScalar
nvflashUpdate = _NvflashUpdate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 4, 15),
    _NvflashUpdate_Type()
)
nvflashUpdate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nvflashUpdate.setStatus("mandatory")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5)
)
_PortTypeStatusTable_Object = MibTable
portTypeStatusTable = _PortTypeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    portTypeStatusTable.setStatus("mandatory")
_PortTypeStatusEntry_Object = MibTableRow
portTypeStatusEntry = _PortTypeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 1, 1)
)
portTypeStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "portTypeStatusCardNumber"),
    (0, "MICOM-NODE-MIB", "portTypeStatusChannelNumber"),
)
if mibBuilder.loadTexts:
    portTypeStatusEntry.setStatus("mandatory")
_PortTypeStatusCardNumber_Type = Integer32
_PortTypeStatusCardNumber_Object = MibTableColumn
portTypeStatusCardNumber = _PortTypeStatusCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 1, 1, 1),
    _PortTypeStatusCardNumber_Type()
)
portTypeStatusCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTypeStatusCardNumber.setStatus("mandatory")
_PortTypeStatusChannelNumber_Type = Integer32
_PortTypeStatusChannelNumber_Object = MibTableColumn
portTypeStatusChannelNumber = _PortTypeStatusChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 1, 1, 2),
    _PortTypeStatusChannelNumber_Type()
)
portTypeStatusChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTypeStatusChannelNumber.setStatus("mandatory")


class _PortTypeStatusChannelType_Type(Integer32):
    """Custom type portTypeStatusChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("badChannel", 6),
          ("digitalVoice", 12),
          ("disabledViaConfig", 11),
          ("esi", 5),
          ("esiSecondary", 9),
          ("frameRelay", 10),
          ("localEsi", 8),
          ("mux", 1),
          ("sync", 3),
          ("voice", 4),
          ("x21", 7))
    )


_PortTypeStatusChannelType_Type.__name__ = "Integer32"
_PortTypeStatusChannelType_Object = MibTableColumn
portTypeStatusChannelType = _PortTypeStatusChannelType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 1, 1, 3),
    _PortTypeStatusChannelType_Type()
)
portTypeStatusChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTypeStatusChannelType.setStatus("mandatory")
_AsyncChStatusTable_Object = MibTable
asyncChStatusTable = _AsyncChStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    asyncChStatusTable.setStatus("mandatory")
_AsyncChStatusEntry_Object = MibTableRow
asyncChStatusEntry = _AsyncChStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 2, 1)
)
asyncChStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "asyncChStatusCardNumber"),
    (0, "MICOM-NODE-MIB", "asyncChStatusChannelNumber"),
)
if mibBuilder.loadTexts:
    asyncChStatusEntry.setStatus("mandatory")


class _AsyncChStatusCardNumber_Type(Integer32):
    """Custom type asyncChStatusCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AsyncChStatusCardNumber_Type.__name__ = "Integer32"
_AsyncChStatusCardNumber_Object = MibTableColumn
asyncChStatusCardNumber = _AsyncChStatusCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 2, 1, 1),
    _AsyncChStatusCardNumber_Type()
)
asyncChStatusCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChStatusCardNumber.setStatus("mandatory")


class _AsyncChStatusChannelNumber_Type(Integer32):
    """Custom type asyncChStatusChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AsyncChStatusChannelNumber_Type.__name__ = "Integer32"
_AsyncChStatusChannelNumber_Object = MibTableColumn
asyncChStatusChannelNumber = _AsyncChStatusChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 2, 1, 2),
    _AsyncChStatusChannelNumber_Type()
)
asyncChStatusChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChStatusChannelNumber.setStatus("mandatory")


class _AsyncChStatusEiaInputsRTSStatus_Type(Integer32):
    """Custom type asyncChStatusEiaInputsRTSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsyncChStatusEiaInputsRTSStatus_Type.__name__ = "Integer32"
_AsyncChStatusEiaInputsRTSStatus_Object = MibTableColumn
asyncChStatusEiaInputsRTSStatus = _AsyncChStatusEiaInputsRTSStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 2, 1, 3),
    _AsyncChStatusEiaInputsRTSStatus_Type()
)
asyncChStatusEiaInputsRTSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChStatusEiaInputsRTSStatus.setStatus("mandatory")


class _AsyncChStatusEiaInputsDTRStatus_Type(Integer32):
    """Custom type asyncChStatusEiaInputsDTRStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsyncChStatusEiaInputsDTRStatus_Type.__name__ = "Integer32"
_AsyncChStatusEiaInputsDTRStatus_Object = MibTableColumn
asyncChStatusEiaInputsDTRStatus = _AsyncChStatusEiaInputsDTRStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 2, 1, 4),
    _AsyncChStatusEiaInputsDTRStatus_Type()
)
asyncChStatusEiaInputsDTRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChStatusEiaInputsDTRStatus.setStatus("mandatory")


class _AsyncChStatusEiaInputsUAStatus_Type(Integer32):
    """Custom type asyncChStatusEiaInputsUAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsyncChStatusEiaInputsUAStatus_Type.__name__ = "Integer32"
_AsyncChStatusEiaInputsUAStatus_Object = MibTableColumn
asyncChStatusEiaInputsUAStatus = _AsyncChStatusEiaInputsUAStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 2, 1, 5),
    _AsyncChStatusEiaInputsUAStatus_Type()
)
asyncChStatusEiaInputsUAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChStatusEiaInputsUAStatus.setStatus("mandatory")


class _AsyncChStatusEiaInputsBUSYStatus_Type(Integer32):
    """Custom type asyncChStatusEiaInputsBUSYStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsyncChStatusEiaInputsBUSYStatus_Type.__name__ = "Integer32"
_AsyncChStatusEiaInputsBUSYStatus_Object = MibTableColumn
asyncChStatusEiaInputsBUSYStatus = _AsyncChStatusEiaInputsBUSYStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 2, 1, 6),
    _AsyncChStatusEiaInputsBUSYStatus_Type()
)
asyncChStatusEiaInputsBUSYStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChStatusEiaInputsBUSYStatus.setStatus("mandatory")


class _AsyncChStatusEiaOutputsRIStatus_Type(Integer32):
    """Custom type asyncChStatusEiaOutputsRIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsyncChStatusEiaOutputsRIStatus_Type.__name__ = "Integer32"
_AsyncChStatusEiaOutputsRIStatus_Object = MibTableColumn
asyncChStatusEiaOutputsRIStatus = _AsyncChStatusEiaOutputsRIStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 2, 1, 7),
    _AsyncChStatusEiaOutputsRIStatus_Type()
)
asyncChStatusEiaOutputsRIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChStatusEiaOutputsRIStatus.setStatus("mandatory")


class _AsyncChStatusEiaOutputsRLSDStatus_Type(Integer32):
    """Custom type asyncChStatusEiaOutputsRLSDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsyncChStatusEiaOutputsRLSDStatus_Type.__name__ = "Integer32"
_AsyncChStatusEiaOutputsRLSDStatus_Object = MibTableColumn
asyncChStatusEiaOutputsRLSDStatus = _AsyncChStatusEiaOutputsRLSDStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 2, 1, 8),
    _AsyncChStatusEiaOutputsRLSDStatus_Type()
)
asyncChStatusEiaOutputsRLSDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChStatusEiaOutputsRLSDStatus.setStatus("mandatory")


class _AsyncChStatusEiaOutputsCTSStatus_Type(Integer32):
    """Custom type asyncChStatusEiaOutputsCTSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsyncChStatusEiaOutputsCTSStatus_Type.__name__ = "Integer32"
_AsyncChStatusEiaOutputsCTSStatus_Object = MibTableColumn
asyncChStatusEiaOutputsCTSStatus = _AsyncChStatusEiaOutputsCTSStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 2, 1, 9),
    _AsyncChStatusEiaOutputsCTSStatus_Type()
)
asyncChStatusEiaOutputsCTSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChStatusEiaOutputsCTSStatus.setStatus("mandatory")


class _AsyncChStatusEiaOutputsDSRStatus_Type(Integer32):
    """Custom type asyncChStatusEiaOutputsDSRStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsyncChStatusEiaOutputsDSRStatus_Type.__name__ = "Integer32"
_AsyncChStatusEiaOutputsDSRStatus_Object = MibTableColumn
asyncChStatusEiaOutputsDSRStatus = _AsyncChStatusEiaOutputsDSRStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 2, 1, 10),
    _AsyncChStatusEiaOutputsDSRStatus_Type()
)
asyncChStatusEiaOutputsDSRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncChStatusEiaOutputsDSRStatus.setStatus("mandatory")
_SyncChStatusTable_Object = MibTable
syncChStatusTable = _SyncChStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    syncChStatusTable.setStatus("mandatory")
_SyncChStatusEntry_Object = MibTableRow
syncChStatusEntry = _SyncChStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 3, 1)
)
syncChStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "syncChStatusCardNumber"),
    (0, "MICOM-NODE-MIB", "syncChStatusChannelNumber"),
)
if mibBuilder.loadTexts:
    syncChStatusEntry.setStatus("mandatory")


class _SyncChStatusCardNumber_Type(Integer32):
    """Custom type syncChStatusCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SyncChStatusCardNumber_Type.__name__ = "Integer32"
_SyncChStatusCardNumber_Object = MibTableColumn
syncChStatusCardNumber = _SyncChStatusCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 3, 1, 1),
    _SyncChStatusCardNumber_Type()
)
syncChStatusCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChStatusCardNumber.setStatus("mandatory")


class _SyncChStatusChannelNumber_Type(Integer32):
    """Custom type syncChStatusChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SyncChStatusChannelNumber_Type.__name__ = "Integer32"
_SyncChStatusChannelNumber_Object = MibTableColumn
syncChStatusChannelNumber = _SyncChStatusChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 3, 1, 2),
    _SyncChStatusChannelNumber_Type()
)
syncChStatusChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChStatusChannelNumber.setStatus("mandatory")


class _SyncChStatusEiaInputsRTSStatus_Type(Integer32):
    """Custom type syncChStatusEiaInputsRTSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SyncChStatusEiaInputsRTSStatus_Type.__name__ = "Integer32"
_SyncChStatusEiaInputsRTSStatus_Object = MibTableColumn
syncChStatusEiaInputsRTSStatus = _SyncChStatusEiaInputsRTSStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 3, 1, 3),
    _SyncChStatusEiaInputsRTSStatus_Type()
)
syncChStatusEiaInputsRTSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChStatusEiaInputsRTSStatus.setStatus("mandatory")


class _SyncChStatusEiaInputsDTRStatus_Type(Integer32):
    """Custom type syncChStatusEiaInputsDTRStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SyncChStatusEiaInputsDTRStatus_Type.__name__ = "Integer32"
_SyncChStatusEiaInputsDTRStatus_Object = MibTableColumn
syncChStatusEiaInputsDTRStatus = _SyncChStatusEiaInputsDTRStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 3, 1, 4),
    _SyncChStatusEiaInputsDTRStatus_Type()
)
syncChStatusEiaInputsDTRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChStatusEiaInputsDTRStatus.setStatus("mandatory")


class _SyncChStatusEiaInputsUAStatus_Type(Integer32):
    """Custom type syncChStatusEiaInputsUAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SyncChStatusEiaInputsUAStatus_Type.__name__ = "Integer32"
_SyncChStatusEiaInputsUAStatus_Object = MibTableColumn
syncChStatusEiaInputsUAStatus = _SyncChStatusEiaInputsUAStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 3, 1, 5),
    _SyncChStatusEiaInputsUAStatus_Type()
)
syncChStatusEiaInputsUAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChStatusEiaInputsUAStatus.setStatus("mandatory")


class _SyncChStatusEiaInputsBUSYStatus_Type(Integer32):
    """Custom type syncChStatusEiaInputsBUSYStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SyncChStatusEiaInputsBUSYStatus_Type.__name__ = "Integer32"
_SyncChStatusEiaInputsBUSYStatus_Object = MibTableColumn
syncChStatusEiaInputsBUSYStatus = _SyncChStatusEiaInputsBUSYStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 3, 1, 6),
    _SyncChStatusEiaInputsBUSYStatus_Type()
)
syncChStatusEiaInputsBUSYStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChStatusEiaInputsBUSYStatus.setStatus("mandatory")


class _SyncChStatusEiaOutputsRIStatus_Type(Integer32):
    """Custom type syncChStatusEiaOutputsRIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SyncChStatusEiaOutputsRIStatus_Type.__name__ = "Integer32"
_SyncChStatusEiaOutputsRIStatus_Object = MibTableColumn
syncChStatusEiaOutputsRIStatus = _SyncChStatusEiaOutputsRIStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 3, 1, 7),
    _SyncChStatusEiaOutputsRIStatus_Type()
)
syncChStatusEiaOutputsRIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChStatusEiaOutputsRIStatus.setStatus("mandatory")


class _SyncChStatusEiaOutputsRLSDStatus_Type(Integer32):
    """Custom type syncChStatusEiaOutputsRLSDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SyncChStatusEiaOutputsRLSDStatus_Type.__name__ = "Integer32"
_SyncChStatusEiaOutputsRLSDStatus_Object = MibTableColumn
syncChStatusEiaOutputsRLSDStatus = _SyncChStatusEiaOutputsRLSDStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 3, 1, 8),
    _SyncChStatusEiaOutputsRLSDStatus_Type()
)
syncChStatusEiaOutputsRLSDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChStatusEiaOutputsRLSDStatus.setStatus("mandatory")


class _SyncChStatusEiaOutputsCTSStatus_Type(Integer32):
    """Custom type syncChStatusEiaOutputsCTSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SyncChStatusEiaOutputsCTSStatus_Type.__name__ = "Integer32"
_SyncChStatusEiaOutputsCTSStatus_Object = MibTableColumn
syncChStatusEiaOutputsCTSStatus = _SyncChStatusEiaOutputsCTSStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 3, 1, 9),
    _SyncChStatusEiaOutputsCTSStatus_Type()
)
syncChStatusEiaOutputsCTSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChStatusEiaOutputsCTSStatus.setStatus("mandatory")


class _SyncChStatusEiaOutputsDSRStatus_Type(Integer32):
    """Custom type syncChStatusEiaOutputsDSRStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SyncChStatusEiaOutputsDSRStatus_Type.__name__ = "Integer32"
_SyncChStatusEiaOutputsDSRStatus_Object = MibTableColumn
syncChStatusEiaOutputsDSRStatus = _SyncChStatusEiaOutputsDSRStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 3, 1, 10),
    _SyncChStatusEiaOutputsDSRStatus_Type()
)
syncChStatusEiaOutputsDSRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncChStatusEiaOutputsDSRStatus.setStatus("mandatory")
_VoiceChStatusTable_Object = MibTable
voiceChStatusTable = _VoiceChStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    voiceChStatusTable.setStatus("mandatory")
_VoiceChStatusEntry_Object = MibTableRow
voiceChStatusEntry = _VoiceChStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1)
)
voiceChStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "voiceChStatusCardNumber"),
    (0, "MICOM-NODE-MIB", "voiceChStatusChannelNumber"),
)
if mibBuilder.loadTexts:
    voiceChStatusEntry.setStatus("mandatory")


class _VoiceChStatusCardNumber_Type(Integer32):
    """Custom type voiceChStatusCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_VoiceChStatusCardNumber_Type.__name__ = "Integer32"
_VoiceChStatusCardNumber_Object = MibTableColumn
voiceChStatusCardNumber = _VoiceChStatusCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 1),
    _VoiceChStatusCardNumber_Type()
)
voiceChStatusCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusCardNumber.setStatus("mandatory")
_VoiceChStatusChannelNumber_Type = Integer32
_VoiceChStatusChannelNumber_Object = MibTableColumn
voiceChStatusChannelNumber = _VoiceChStatusChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 2),
    _VoiceChStatusChannelNumber_Type()
)
voiceChStatusChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusChannelNumber.setStatus("mandatory")


class _VoiceChStatusInputLevel_Type(Integer32):
    """Custom type voiceChStatusInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("level0dBm", 15),
          ("levelLessThanNeg25dBm", 1),
          ("levelNeg10dBm", 7),
          ("levelNeg12dBm", 6),
          ("levelNeg15dBm", 5),
          ("levelNeg18dBm", 4),
          ("levelNeg1dBm", 14),
          ("levelNeg21dBm", 3),
          ("levelNeg24dBm", 2),
          ("levelNeg2dBm", 13),
          ("levelNeg3dBm", 12),
          ("levelNeg4dBm", 11),
          ("levelNeg5dBm", 10),
          ("levelNeg6dBm", 9),
          ("levelNeg8dBm", 8),
          ("levelNotAvailable", 17),
          ("levelgreaterThan0dBm", 16))
    )


_VoiceChStatusInputLevel_Type.__name__ = "Integer32"
_VoiceChStatusInputLevel_Object = MibTableColumn
voiceChStatusInputLevel = _VoiceChStatusInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 3),
    _VoiceChStatusInputLevel_Type()
)
voiceChStatusInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusInputLevel.setStatus("mandatory")


class _VoiceChStatusStatus_Type(Integer32):
    """Custom type voiceChStatusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("offHook", 2),
          ("onHook", 1))
    )


_VoiceChStatusStatus_Type.__name__ = "Integer32"
_VoiceChStatusStatus_Object = MibTableColumn
voiceChStatusStatus = _VoiceChStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 4),
    _VoiceChStatusStatus_Type()
)
voiceChStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusStatus.setStatus("mandatory")


class _VoiceChStatusPromID_Type(DisplayString):
    """Custom type voiceChStatusPromID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_VoiceChStatusPromID_Type.__name__ = "DisplayString"
_VoiceChStatusPromID_Object = MibTableColumn
voiceChStatusPromID = _VoiceChStatusPromID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 5),
    _VoiceChStatusPromID_Type()
)
voiceChStatusPromID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusPromID.setStatus("mandatory")


class _VoiceChStatusSoftwareRevision_Type(DisplayString):
    """Custom type voiceChStatusSoftwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_VoiceChStatusSoftwareRevision_Type.__name__ = "DisplayString"
_VoiceChStatusSoftwareRevision_Object = MibTableColumn
voiceChStatusSoftwareRevision = _VoiceChStatusSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 6),
    _VoiceChStatusSoftwareRevision_Type()
)
voiceChStatusSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusSoftwareRevision.setStatus("mandatory")


class _VoiceChStatusTestMode_Type(Integer32):
    """Custom type voiceChStatusTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("levelDisplay", 2),
          ("localLoopback", 4),
          ("localSelfTest", 3),
          ("none", 1),
          ("remoteLoopback", 6),
          ("remoteSelfTest", 5))
    )


_VoiceChStatusTestMode_Type.__name__ = "Integer32"
_VoiceChStatusTestMode_Object = MibTableColumn
voiceChStatusTestMode = _VoiceChStatusTestMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 7),
    _VoiceChStatusTestMode_Type()
)
voiceChStatusTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusTestMode.setStatus("mandatory")


class _VoiceChStatusTestDSPResult_Type(Integer32):
    """Custom type voiceChStatusTestDSPResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_VoiceChStatusTestDSPResult_Type.__name__ = "Integer32"
_VoiceChStatusTestDSPResult_Object = MibTableColumn
voiceChStatusTestDSPResult = _VoiceChStatusTestDSPResult_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 8),
    _VoiceChStatusTestDSPResult_Type()
)
voiceChStatusTestDSPResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusTestDSPResult.setStatus("mandatory")


class _VoiceChStatusTestDataRAMResult_Type(Integer32):
    """Custom type voiceChStatusTestDataRAMResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_VoiceChStatusTestDataRAMResult_Type.__name__ = "Integer32"
_VoiceChStatusTestDataRAMResult_Object = MibTableColumn
voiceChStatusTestDataRAMResult = _VoiceChStatusTestDataRAMResult_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 9),
    _VoiceChStatusTestDataRAMResult_Type()
)
voiceChStatusTestDataRAMResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusTestDataRAMResult.setStatus("mandatory")


class _VoiceChStatusTestCodeRAMResult_Type(Integer32):
    """Custom type voiceChStatusTestCodeRAMResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_VoiceChStatusTestCodeRAMResult_Type.__name__ = "Integer32"
_VoiceChStatusTestCodeRAMResult_Object = MibTableColumn
voiceChStatusTestCodeRAMResult = _VoiceChStatusTestCodeRAMResult_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 10),
    _VoiceChStatusTestCodeRAMResult_Type()
)
voiceChStatusTestCodeRAMResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusTestCodeRAMResult.setStatus("mandatory")


class _VoiceChStatusTestAnalogHwResult_Type(Integer32):
    """Custom type voiceChStatusTestAnalogHwResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_VoiceChStatusTestAnalogHwResult_Type.__name__ = "Integer32"
_VoiceChStatusTestAnalogHwResult_Object = MibTableColumn
voiceChStatusTestAnalogHwResult = _VoiceChStatusTestAnalogHwResult_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 11),
    _VoiceChStatusTestAnalogHwResult_Type()
)
voiceChStatusTestAnalogHwResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusTestAnalogHwResult.setStatus("mandatory")


class _VoiceChStatusTestDeviceCfgResult_Type(Integer32):
    """Custom type voiceChStatusTestDeviceCfgResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_VoiceChStatusTestDeviceCfgResult_Type.__name__ = "Integer32"
_VoiceChStatusTestDeviceCfgResult_Object = MibTableColumn
voiceChStatusTestDeviceCfgResult = _VoiceChStatusTestDeviceCfgResult_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 12),
    _VoiceChStatusTestDeviceCfgResult_Type()
)
voiceChStatusTestDeviceCfgResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusTestDeviceCfgResult.setStatus("mandatory")


class _VoiceChStatusFlashState_Type(Integer32):
    """Custom type voiceChStatusFlashState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("erased", 3),
          ("invalidChecksum", 4),
          ("noAnalogDriver", 5),
          ("notInstalled", 1),
          ("securityViolation", 6),
          ("valid", 2))
    )


_VoiceChStatusFlashState_Type.__name__ = "Integer32"
_VoiceChStatusFlashState_Object = MibTableColumn
voiceChStatusFlashState = _VoiceChStatusFlashState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 13),
    _VoiceChStatusFlashState_Type()
)
voiceChStatusFlashState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusFlashState.setStatus("mandatory")


class _VoiceChStatusEPROMStatus_Type(Integer32):
    """Custom type voiceChStatusEPROMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("currentlyOperating", 2),
          ("notInstalled", 1),
          ("presentButNotOperating", 3))
    )


_VoiceChStatusEPROMStatus_Type.__name__ = "Integer32"
_VoiceChStatusEPROMStatus_Object = MibTableColumn
voiceChStatusEPROMStatus = _VoiceChStatusEPROMStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 4, 1, 14),
    _VoiceChStatusEPROMStatus_Type()
)
voiceChStatusEPROMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceChStatusEPROMStatus.setStatus("mandatory")
_LinkStatusTable_Object = MibTable
linkStatusTable = _LinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    linkStatusTable.setStatus("mandatory")
_LinkStatusEntry_Object = MibTableRow
linkStatusEntry = _LinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1)
)
linkStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "linkStatusCardNumber"),
    (0, "MICOM-NODE-MIB", "linkStatusChannelNumber"),
)
if mibBuilder.loadTexts:
    linkStatusEntry.setStatus("mandatory")


class _LinkStatusCardNumber_Type(Integer32):
    """Custom type linkStatusCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_LinkStatusCardNumber_Type.__name__ = "Integer32"
_LinkStatusCardNumber_Object = MibTableColumn
linkStatusCardNumber = _LinkStatusCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 1),
    _LinkStatusCardNumber_Type()
)
linkStatusCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusCardNumber.setStatus("mandatory")
_LinkStatusChannelNumber_Type = Integer32
_LinkStatusChannelNumber_Object = MibTableColumn
linkStatusChannelNumber = _LinkStatusChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 2),
    _LinkStatusChannelNumber_Type()
)
linkStatusChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusChannelNumber.setStatus("mandatory")


class _LinkStatusLinkType_Type(Integer32):
    """Custom type linkStatusLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("esi", 2),
          ("esiSecondary", 5),
          ("frameRelay", 6),
          ("localESI", 4),
          ("muxLink", 1),
          ("x21MuxLink", 3))
    )


_LinkStatusLinkType_Type.__name__ = "Integer32"
_LinkStatusLinkType_Object = MibTableColumn
linkStatusLinkType = _LinkStatusLinkType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 3),
    _LinkStatusLinkType_Type()
)
linkStatusLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusLinkType.setStatus("mandatory")


class _LinkStatusIntegralDevType_Type(Integer32):
    """Custom type linkStatusIntegralDevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isu56K", 2),
          ("none", 1))
    )


_LinkStatusIntegralDevType_Type.__name__ = "Integer32"
_LinkStatusIntegralDevType_Object = MibTableColumn
linkStatusIntegralDevType = _LinkStatusIntegralDevType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 4),
    _LinkStatusIntegralDevType_Type()
)
linkStatusIntegralDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusIntegralDevType.setStatus("mandatory")


class _LinkStatusIntegralDevSlotNumber_Type(Integer32):
    """Custom type linkStatusIntegralDevSlotNumber based on Integer32"""
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
        *(("slotA", 1),
          ("slotB", 2),
          ("slotC", 3),
          ("slotD", 4),
          ("slotE", 5))
    )


_LinkStatusIntegralDevSlotNumber_Type.__name__ = "Integer32"
_LinkStatusIntegralDevSlotNumber_Object = MibTableColumn
linkStatusIntegralDevSlotNumber = _LinkStatusIntegralDevSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 5),
    _LinkStatusIntegralDevSlotNumber_Type()
)
linkStatusIntegralDevSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusIntegralDevSlotNumber.setStatus("mandatory")


class _LinkStatusIntegralDeviceNumber_Type(Integer32):
    """Custom type linkStatusIntegralDeviceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channel1", 1),
          ("channel2", 2))
    )


_LinkStatusIntegralDeviceNumber_Type.__name__ = "Integer32"
_LinkStatusIntegralDeviceNumber_Object = MibTableColumn
linkStatusIntegralDeviceNumber = _LinkStatusIntegralDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 6),
    _LinkStatusIntegralDeviceNumber_Type()
)
linkStatusIntegralDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusIntegralDeviceNumber.setStatus("mandatory")


class _LinkStatusStatus_Type(Integer32):
    """Custom type linkStatusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("loopback", 3),
          ("up", 2))
    )


_LinkStatusStatus_Type.__name__ = "Integer32"
_LinkStatusStatus_Object = MibTableColumn
linkStatusStatus = _LinkStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 7),
    _LinkStatusStatus_Type()
)
linkStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusStatus.setStatus("mandatory")
_LinkStatusNodeNumber_Type = Integer32
_LinkStatusNodeNumber_Object = MibTableColumn
linkStatusNodeNumber = _LinkStatusNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 8),
    _LinkStatusNodeNumber_Type()
)
linkStatusNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusNodeNumber.setStatus("mandatory")
_LinkStatusRemoteChannelNumber_Type = Integer32
_LinkStatusRemoteChannelNumber_Object = MibTableColumn
linkStatusRemoteChannelNumber = _LinkStatusRemoteChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 9),
    _LinkStatusRemoteChannelNumber_Type()
)
linkStatusRemoteChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusRemoteChannelNumber.setStatus("mandatory")
_LinkStatusRemoteCardNumber_Type = Integer32
_LinkStatusRemoteCardNumber_Object = MibTableColumn
linkStatusRemoteCardNumber = _LinkStatusRemoteCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 10),
    _LinkStatusRemoteCardNumber_Type()
)
linkStatusRemoteCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusRemoteCardNumber.setStatus("mandatory")


class _LinkStatusEiaOutputsRTSStatus_Type(Integer32):
    """Custom type linkStatusEiaOutputsRTSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LinkStatusEiaOutputsRTSStatus_Type.__name__ = "Integer32"
_LinkStatusEiaOutputsRTSStatus_Object = MibTableColumn
linkStatusEiaOutputsRTSStatus = _LinkStatusEiaOutputsRTSStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 11),
    _LinkStatusEiaOutputsRTSStatus_Type()
)
linkStatusEiaOutputsRTSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusEiaOutputsRTSStatus.setStatus("mandatory")


class _LinkStatusEiaOutputsDTRStatus_Type(Integer32):
    """Custom type linkStatusEiaOutputsDTRStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LinkStatusEiaOutputsDTRStatus_Type.__name__ = "Integer32"
_LinkStatusEiaOutputsDTRStatus_Object = MibTableColumn
linkStatusEiaOutputsDTRStatus = _LinkStatusEiaOutputsDTRStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 12),
    _LinkStatusEiaOutputsDTRStatus_Type()
)
linkStatusEiaOutputsDTRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusEiaOutputsDTRStatus.setStatus("mandatory")


class _LinkStatusEiaOutputsBUSYStatus_Type(Integer32):
    """Custom type linkStatusEiaOutputsBUSYStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LinkStatusEiaOutputsBUSYStatus_Type.__name__ = "Integer32"
_LinkStatusEiaOutputsBUSYStatus_Object = MibTableColumn
linkStatusEiaOutputsBUSYStatus = _LinkStatusEiaOutputsBUSYStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 13),
    _LinkStatusEiaOutputsBUSYStatus_Type()
)
linkStatusEiaOutputsBUSYStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusEiaOutputsBUSYStatus.setStatus("mandatory")


class _LinkStatusEiaOutputsUAStatus_Type(Integer32):
    """Custom type linkStatusEiaOutputsUAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LinkStatusEiaOutputsUAStatus_Type.__name__ = "Integer32"
_LinkStatusEiaOutputsUAStatus_Object = MibTableColumn
linkStatusEiaOutputsUAStatus = _LinkStatusEiaOutputsUAStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 14),
    _LinkStatusEiaOutputsUAStatus_Type()
)
linkStatusEiaOutputsUAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusEiaOutputsUAStatus.setStatus("mandatory")


class _LinkStatusEiaInputsRLSDStatus_Type(Integer32):
    """Custom type linkStatusEiaInputsRLSDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LinkStatusEiaInputsRLSDStatus_Type.__name__ = "Integer32"
_LinkStatusEiaInputsRLSDStatus_Object = MibTableColumn
linkStatusEiaInputsRLSDStatus = _LinkStatusEiaInputsRLSDStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 15),
    _LinkStatusEiaInputsRLSDStatus_Type()
)
linkStatusEiaInputsRLSDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusEiaInputsRLSDStatus.setStatus("mandatory")


class _LinkStatusEiaInputsDSRStatus_Type(Integer32):
    """Custom type linkStatusEiaInputsDSRStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LinkStatusEiaInputsDSRStatus_Type.__name__ = "Integer32"
_LinkStatusEiaInputsDSRStatus_Object = MibTableColumn
linkStatusEiaInputsDSRStatus = _LinkStatusEiaInputsDSRStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 16),
    _LinkStatusEiaInputsDSRStatus_Type()
)
linkStatusEiaInputsDSRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusEiaInputsDSRStatus.setStatus("mandatory")


class _LinkStatusEiaInputsRIStatus_Type(Integer32):
    """Custom type linkStatusEiaInputsRIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LinkStatusEiaInputsRIStatus_Type.__name__ = "Integer32"
_LinkStatusEiaInputsRIStatus_Object = MibTableColumn
linkStatusEiaInputsRIStatus = _LinkStatusEiaInputsRIStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 17),
    _LinkStatusEiaInputsRIStatus_Type()
)
linkStatusEiaInputsRIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusEiaInputsRIStatus.setStatus("mandatory")


class _LinkStatusEiaInputsCTSStatus_Type(Integer32):
    """Custom type linkStatusEiaInputsCTSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LinkStatusEiaInputsCTSStatus_Type.__name__ = "Integer32"
_LinkStatusEiaInputsCTSStatus_Object = MibTableColumn
linkStatusEiaInputsCTSStatus = _LinkStatusEiaInputsCTSStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 5, 1, 18),
    _LinkStatusEiaInputsCTSStatus_Type()
)
linkStatusEiaInputsCTSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusEiaInputsCTSStatus.setStatus("mandatory")
_FrameRelayLinkDLCIStatusTable_Object = MibTable
frameRelayLinkDLCIStatusTable = _FrameRelayLinkDLCIStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6)
)
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusTable.setStatus("mandatory")
_FrameRelayLinkDLCIStatusEntry_Object = MibTableRow
frameRelayLinkDLCIStatusEntry = _FrameRelayLinkDLCIStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1)
)
frameRelayLinkDLCIStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "frameRelayLinkDLCIStatusCardNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayLinkDLCIStatusChannelNumber"),
    (0, "MICOM-NODE-MIB", "frameRelayLinkDLCIStatusDLCINumber"),
)
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusEntry.setStatus("mandatory")
_FrameRelayLinkDLCIStatusCardNumber_Type = Integer32
_FrameRelayLinkDLCIStatusCardNumber_Object = MibTableColumn
frameRelayLinkDLCIStatusCardNumber = _FrameRelayLinkDLCIStatusCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1, 1),
    _FrameRelayLinkDLCIStatusCardNumber_Type()
)
frameRelayLinkDLCIStatusCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusCardNumber.setStatus("mandatory")
_FrameRelayLinkDLCIStatusChannelNumber_Type = Integer32
_FrameRelayLinkDLCIStatusChannelNumber_Object = MibTableColumn
frameRelayLinkDLCIStatusChannelNumber = _FrameRelayLinkDLCIStatusChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1, 2),
    _FrameRelayLinkDLCIStatusChannelNumber_Type()
)
frameRelayLinkDLCIStatusChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusChannelNumber.setStatus("mandatory")
_FrameRelayLinkDLCIStatusDLCINumber_Type = Integer32
_FrameRelayLinkDLCIStatusDLCINumber_Object = MibTableColumn
frameRelayLinkDLCIStatusDLCINumber = _FrameRelayLinkDLCIStatusDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1, 3),
    _FrameRelayLinkDLCIStatusDLCINumber_Type()
)
frameRelayLinkDLCIStatusDLCINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusDLCINumber.setStatus("mandatory")
_FrameRelayLinkDLCIStatusNumberOfDLCIs_Type = Integer32
_FrameRelayLinkDLCIStatusNumberOfDLCIs_Object = MibTableColumn
frameRelayLinkDLCIStatusNumberOfDLCIs = _FrameRelayLinkDLCIStatusNumberOfDLCIs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1, 4),
    _FrameRelayLinkDLCIStatusNumberOfDLCIs_Type()
)
frameRelayLinkDLCIStatusNumberOfDLCIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusNumberOfDLCIs.setStatus("mandatory")


class _FrameRelayLinkDLCIStatusConfOnMarathon_Type(Integer32):
    """Custom type frameRelayLinkDLCIStatusConfOnMarathon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_FrameRelayLinkDLCIStatusConfOnMarathon_Type.__name__ = "Integer32"
_FrameRelayLinkDLCIStatusConfOnMarathon_Object = MibTableColumn
frameRelayLinkDLCIStatusConfOnMarathon = _FrameRelayLinkDLCIStatusConfOnMarathon_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1, 5),
    _FrameRelayLinkDLCIStatusConfOnMarathon_Type()
)
frameRelayLinkDLCIStatusConfOnMarathon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusConfOnMarathon.setStatus("mandatory")


class _FrameRelayLinkDLCIStatusReportedByPBX_Type(Integer32):
    """Custom type frameRelayLinkDLCIStatusReportedByPBX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_FrameRelayLinkDLCIStatusReportedByPBX_Type.__name__ = "Integer32"
_FrameRelayLinkDLCIStatusReportedByPBX_Object = MibTableColumn
frameRelayLinkDLCIStatusReportedByPBX = _FrameRelayLinkDLCIStatusReportedByPBX_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1, 6),
    _FrameRelayLinkDLCIStatusReportedByPBX_Type()
)
frameRelayLinkDLCIStatusReportedByPBX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusReportedByPBX.setStatus("mandatory")


class _FrameRelayLinkDLCIStatusActive_Type(Integer32):
    """Custom type frameRelayLinkDLCIStatusActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_FrameRelayLinkDLCIStatusActive_Type.__name__ = "Integer32"
_FrameRelayLinkDLCIStatusActive_Object = MibTableColumn
frameRelayLinkDLCIStatusActive = _FrameRelayLinkDLCIStatusActive_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1, 7),
    _FrameRelayLinkDLCIStatusActive_Type()
)
frameRelayLinkDLCIStatusActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusActive.setStatus("mandatory")


class _FrameRelayLinkDLCIStatusLinkStatus_Type(Integer32):
    """Custom type frameRelayLinkDLCIStatusLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_FrameRelayLinkDLCIStatusLinkStatus_Type.__name__ = "Integer32"
_FrameRelayLinkDLCIStatusLinkStatus_Object = MibTableColumn
frameRelayLinkDLCIStatusLinkStatus = _FrameRelayLinkDLCIStatusLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1, 8),
    _FrameRelayLinkDLCIStatusLinkStatus_Type()
)
frameRelayLinkDLCIStatusLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusLinkStatus.setStatus("mandatory")
_FrameRelayLinkDLCIStatusUpConnectedNodeNumber_Type = Integer32
_FrameRelayLinkDLCIStatusUpConnectedNodeNumber_Object = MibTableColumn
frameRelayLinkDLCIStatusUpConnectedNodeNumber = _FrameRelayLinkDLCIStatusUpConnectedNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1, 9),
    _FrameRelayLinkDLCIStatusUpConnectedNodeNumber_Type()
)
frameRelayLinkDLCIStatusUpConnectedNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusUpConnectedNodeNumber.setStatus("mandatory")
_FrameRelayLinkDLCIStatusUpConnectedChannelNumber_Type = Integer32
_FrameRelayLinkDLCIStatusUpConnectedChannelNumber_Object = MibTableColumn
frameRelayLinkDLCIStatusUpConnectedChannelNumber = _FrameRelayLinkDLCIStatusUpConnectedChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1, 10),
    _FrameRelayLinkDLCIStatusUpConnectedChannelNumber_Type()
)
frameRelayLinkDLCIStatusUpConnectedChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusUpConnectedChannelNumber.setStatus("mandatory")
_FrameRelayLinkDLCIStatusUpConnectedCardNumber_Type = Integer32
_FrameRelayLinkDLCIStatusUpConnectedCardNumber_Object = MibTableColumn
frameRelayLinkDLCIStatusUpConnectedCardNumber = _FrameRelayLinkDLCIStatusUpConnectedCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1, 11),
    _FrameRelayLinkDLCIStatusUpConnectedCardNumber_Type()
)
frameRelayLinkDLCIStatusUpConnectedCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusUpConnectedCardNumber.setStatus("mandatory")
_FrameRelayLinkDLCIStatusUpRemoteDLCINumber_Type = Integer32
_FrameRelayLinkDLCIStatusUpRemoteDLCINumber_Object = MibTableColumn
frameRelayLinkDLCIStatusUpRemoteDLCINumber = _FrameRelayLinkDLCIStatusUpRemoteDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 6, 1, 12),
    _FrameRelayLinkDLCIStatusUpRemoteDLCINumber_Type()
)
frameRelayLinkDLCIStatusUpRemoteDLCINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayLinkDLCIStatusUpRemoteDLCINumber.setStatus("mandatory")
_ChConnectionStatusTable_Object = MibTable
chConnectionStatusTable = _ChConnectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 7)
)
if mibBuilder.loadTexts:
    chConnectionStatusTable.setStatus("mandatory")
_ChConnectionStatusEntry_Object = MibTableRow
chConnectionStatusEntry = _ChConnectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 7, 1)
)
chConnectionStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "chConnectionStatusCardNumber"),
    (0, "MICOM-NODE-MIB", "chConnectionStatusChannelNumber"),
)
if mibBuilder.loadTexts:
    chConnectionStatusEntry.setStatus("mandatory")


class _ChConnectionStatusCardNumber_Type(Integer32):
    """Custom type chConnectionStatusCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ChConnectionStatusCardNumber_Type.__name__ = "Integer32"
_ChConnectionStatusCardNumber_Object = MibTableColumn
chConnectionStatusCardNumber = _ChConnectionStatusCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 7, 1, 1),
    _ChConnectionStatusCardNumber_Type()
)
chConnectionStatusCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chConnectionStatusCardNumber.setStatus("mandatory")
_ChConnectionStatusChannelNumber_Type = Integer32
_ChConnectionStatusChannelNumber_Object = MibTableColumn
chConnectionStatusChannelNumber = _ChConnectionStatusChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 7, 1, 2),
    _ChConnectionStatusChannelNumber_Type()
)
chConnectionStatusChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chConnectionStatusChannelNumber.setStatus("mandatory")


class _ChConnectionStatusChannelStatus_Type(Integer32):
    """Custom type chConnectionStatusChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("connectInProgress", 2),
          ("connected", 5),
          ("disconnectInProgress", 7),
          ("fconnInProgress", 3),
          ("forceConnected", 6),
          ("idle", 1),
          ("outOfService", 8),
          ("queued", 4))
    )


_ChConnectionStatusChannelStatus_Type.__name__ = "Integer32"
_ChConnectionStatusChannelStatus_Object = MibTableColumn
chConnectionStatusChannelStatus = _ChConnectionStatusChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 7, 1, 3),
    _ChConnectionStatusChannelStatus_Type()
)
chConnectionStatusChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chConnectionStatusChannelStatus.setStatus("mandatory")
_ChConnectionStatusConnectedToNode_Type = Integer32
_ChConnectionStatusConnectedToNode_Object = MibTableColumn
chConnectionStatusConnectedToNode = _ChConnectionStatusConnectedToNode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 7, 1, 4),
    _ChConnectionStatusConnectedToNode_Type()
)
chConnectionStatusConnectedToNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chConnectionStatusConnectedToNode.setStatus("mandatory")
_ChConnectionStatusConnectedToChannel_Type = Integer32
_ChConnectionStatusConnectedToChannel_Object = MibTableColumn
chConnectionStatusConnectedToChannel = _ChConnectionStatusConnectedToChannel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 7, 1, 5),
    _ChConnectionStatusConnectedToChannel_Type()
)
chConnectionStatusConnectedToChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chConnectionStatusConnectedToChannel.setStatus("mandatory")
_ChConnectionStatusConnectedToCard_Type = Integer32
_ChConnectionStatusConnectedToCard_Object = MibTableColumn
chConnectionStatusConnectedToCard = _ChConnectionStatusConnectedToCard_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 7, 1, 6),
    _ChConnectionStatusConnectedToCard_Type()
)
chConnectionStatusConnectedToCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chConnectionStatusConnectedToCard.setStatus("mandatory")


class _ChConnectionStatusConnectedToInternalFacility_Type(Integer32):
    """Custom type chConnectionStatusConnectedToInternalFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dollarCMDFacility", 2),
          ("dollarPPPFacility", 3),
          ("notApplicable", 1))
    )


_ChConnectionStatusConnectedToInternalFacility_Type.__name__ = "Integer32"
_ChConnectionStatusConnectedToInternalFacility_Object = MibTableColumn
chConnectionStatusConnectedToInternalFacility = _ChConnectionStatusConnectedToInternalFacility_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 7, 1, 7),
    _ChConnectionStatusConnectedToInternalFacility_Type()
)
chConnectionStatusConnectedToInternalFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chConnectionStatusConnectedToInternalFacility.setStatus("mandatory")
_RemoteNodeStatusTable_Object = MibTable
remoteNodeStatusTable = _RemoteNodeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 8)
)
if mibBuilder.loadTexts:
    remoteNodeStatusTable.setStatus("mandatory")
_RemoteNodeStatusEntry_Object = MibTableRow
remoteNodeStatusEntry = _RemoteNodeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 8, 1)
)
remoteNodeStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "remoteNodeStatusIndex"),
)
if mibBuilder.loadTexts:
    remoteNodeStatusEntry.setStatus("mandatory")
_RemoteNodeStatusIndex_Type = Integer32
_RemoteNodeStatusIndex_Object = MibTableColumn
remoteNodeStatusIndex = _RemoteNodeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 8, 1, 1),
    _RemoteNodeStatusIndex_Type()
)
remoteNodeStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteNodeStatusIndex.setStatus("mandatory")


class _RemoteNodeStatusName_Type(DisplayString):
    """Custom type remoteNodeStatusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RemoteNodeStatusName_Type.__name__ = "DisplayString"
_RemoteNodeStatusName_Object = MibTableColumn
remoteNodeStatusName = _RemoteNodeStatusName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 8, 1, 2),
    _RemoteNodeStatusName_Type()
)
remoteNodeStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteNodeStatusName.setStatus("mandatory")


class _RemoteNodeStatusType_Type(Integer32):
    """Custom type remoteNodeStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("feederMux", 2),
          ("marathonNode", 1))
    )


_RemoteNodeStatusType_Type.__name__ = "Integer32"
_RemoteNodeStatusType_Object = MibTableColumn
remoteNodeStatusType = _RemoteNodeStatusType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 8, 1, 3),
    _RemoteNodeStatusType_Type()
)
remoteNodeStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteNodeStatusType.setStatus("mandatory")
_RemoteNodeStatusNumber_Type = Integer32
_RemoteNodeStatusNumber_Object = MibTableColumn
remoteNodeStatusNumber = _RemoteNodeStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 8, 1, 4),
    _RemoteNodeStatusNumber_Type()
)
remoteNodeStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteNodeStatusNumber.setStatus("mandatory")
_ClassStatusTable_Object = MibTable
classStatusTable = _ClassStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 9)
)
if mibBuilder.loadTexts:
    classStatusTable.setStatus("mandatory")
_ClassStatusEntry_Object = MibTableRow
classStatusEntry = _ClassStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 9, 1)
)
classStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "classStatusCfgClassIndex"),
)
if mibBuilder.loadTexts:
    classStatusEntry.setStatus("mandatory")
_ClassStatusCfgClassIndex_Type = Integer32
_ClassStatusCfgClassIndex_Object = MibTableColumn
classStatusCfgClassIndex = _ClassStatusCfgClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 9, 1, 1),
    _ClassStatusCfgClassIndex_Type()
)
classStatusCfgClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classStatusCfgClassIndex.setStatus("mandatory")
_ClassStatusCfgClassNumber_Type = Integer32
_ClassStatusCfgClassNumber_Object = MibTableColumn
classStatusCfgClassNumber = _ClassStatusCfgClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 9, 1, 2),
    _ClassStatusCfgClassNumber_Type()
)
classStatusCfgClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classStatusCfgClassNumber.setStatus("mandatory")
_ClassQueueStatusTable_Object = MibTable
classQueueStatusTable = _ClassQueueStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 10)
)
if mibBuilder.loadTexts:
    classQueueStatusTable.setStatus("mandatory")
_ClassQueueStatusEntry_Object = MibTableRow
classQueueStatusEntry = _ClassQueueStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 10, 1)
)
classQueueStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "classQueueStatusClassNum"),
)
if mibBuilder.loadTexts:
    classQueueStatusEntry.setStatus("mandatory")


class _ClassQueueStatusClassNum_Type(Integer32):
    """Custom type classQueueStatusClassNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ClassQueueStatusClassNum_Type.__name__ = "Integer32"
_ClassQueueStatusClassNum_Object = MibTableColumn
classQueueStatusClassNum = _ClassQueueStatusClassNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 10, 1, 1),
    _ClassQueueStatusClassNum_Type()
)
classQueueStatusClassNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classQueueStatusClassNum.setStatus("mandatory")
_ClassQueueStatusChCount_Type = Integer32
_ClassQueueStatusChCount_Object = MibTableColumn
classQueueStatusChCount = _ClassQueueStatusChCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 10, 1, 2),
    _ClassQueueStatusChCount_Type()
)
classQueueStatusChCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classQueueStatusChCount.setStatus("mandatory")
_ClassChannelStatusTable_Object = MibTable
classChannelStatusTable = _ClassChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 11)
)
if mibBuilder.loadTexts:
    classChannelStatusTable.setStatus("mandatory")
_ClassChannelStatusEntry_Object = MibTableRow
classChannelStatusEntry = _ClassChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 11, 1)
)
classChannelStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "classQueueStatusClassNum"),
    (0, "MICOM-NODE-MIB", "classQueueStatusChannelIndex"),
)
if mibBuilder.loadTexts:
    classChannelStatusEntry.setStatus("mandatory")


class _ClassChannelStatusClassNum_Type(Integer32):
    """Custom type classChannelStatusClassNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ClassChannelStatusClassNum_Type.__name__ = "Integer32"
_ClassChannelStatusClassNum_Object = MibTableColumn
classChannelStatusClassNum = _ClassChannelStatusClassNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 11, 1, 1),
    _ClassChannelStatusClassNum_Type()
)
classChannelStatusClassNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classChannelStatusClassNum.setStatus("mandatory")
_ClassQueueStatusChannelIndex_Type = Integer32
_ClassQueueStatusChannelIndex_Object = MibTableColumn
classQueueStatusChannelIndex = _ClassQueueStatusChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 11, 1, 2),
    _ClassQueueStatusChannelIndex_Type()
)
classQueueStatusChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classQueueStatusChannelIndex.setStatus("mandatory")
_ClassChannelStatusNode_Type = Integer32
_ClassChannelStatusNode_Object = MibTableColumn
classChannelStatusNode = _ClassChannelStatusNode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 11, 1, 3),
    _ClassChannelStatusNode_Type()
)
classChannelStatusNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classChannelStatusNode.setStatus("mandatory")
_ClassChannelStatusChannel_Type = Integer32
_ClassChannelStatusChannel_Object = MibTableColumn
classChannelStatusChannel = _ClassChannelStatusChannel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 11, 1, 4),
    _ClassChannelStatusChannel_Type()
)
classChannelStatusChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classChannelStatusChannel.setStatus("mandatory")
_ClassChannelStatusCard_Type = Integer32
_ClassChannelStatusCard_Object = MibTableColumn
classChannelStatusCard = _ClassChannelStatusCard_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 11, 1, 5),
    _ClassChannelStatusCard_Type()
)
classChannelStatusCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classChannelStatusCard.setStatus("mandatory")
_FlashMemoryStatusTable_Object = MibTable
flashMemoryStatusTable = _FlashMemoryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12)
)
if mibBuilder.loadTexts:
    flashMemoryStatusTable.setStatus("mandatory")
_FlashMemoryStatusEntry_Object = MibTableRow
flashMemoryStatusEntry = _FlashMemoryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1)
)
flashMemoryStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "flashMemoryStatusFlashNumber"),
)
if mibBuilder.loadTexts:
    flashMemoryStatusEntry.setStatus("mandatory")


class _FlashMemoryStatusFlashNumber_Type(Integer32):
    """Custom type flashMemoryStatusFlashNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FlashMemoryStatusFlashNumber_Type.__name__ = "Integer32"
_FlashMemoryStatusFlashNumber_Object = MibTableColumn
flashMemoryStatusFlashNumber = _FlashMemoryStatusFlashNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1, 1),
    _FlashMemoryStatusFlashNumber_Type()
)
flashMemoryStatusFlashNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashMemoryStatusFlashNumber.setStatus("mandatory")
_FlashMemoryStatusFileHeaderSize_Type = Integer32
_FlashMemoryStatusFileHeaderSize_Object = MibTableColumn
flashMemoryStatusFileHeaderSize = _FlashMemoryStatusFileHeaderSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1, 2),
    _FlashMemoryStatusFileHeaderSize_Type()
)
flashMemoryStatusFileHeaderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashMemoryStatusFileHeaderSize.setStatus("mandatory")


class _FlashMemoryStatusFileType_Type(Integer32):
    """Custom type flashMemoryStatusFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compressed", 1),
          ("erased", 3),
          ("uncompressed", 2))
    )


_FlashMemoryStatusFileType_Type.__name__ = "Integer32"
_FlashMemoryStatusFileType_Object = MibTableColumn
flashMemoryStatusFileType = _FlashMemoryStatusFileType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1, 3),
    _FlashMemoryStatusFileType_Type()
)
flashMemoryStatusFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashMemoryStatusFileType.setStatus("mandatory")
_FlashMemoryStatusMarathonImageSize_Type = Integer32
_FlashMemoryStatusMarathonImageSize_Object = MibTableColumn
flashMemoryStatusMarathonImageSize = _FlashMemoryStatusMarathonImageSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1, 4),
    _FlashMemoryStatusMarathonImageSize_Type()
)
flashMemoryStatusMarathonImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashMemoryStatusMarathonImageSize.setStatus("mandatory")
_FlashMemoryStatusCreationHours_Type = Integer32
_FlashMemoryStatusCreationHours_Object = MibTableColumn
flashMemoryStatusCreationHours = _FlashMemoryStatusCreationHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1, 5),
    _FlashMemoryStatusCreationHours_Type()
)
flashMemoryStatusCreationHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashMemoryStatusCreationHours.setStatus("mandatory")
_FlashMemoryStatusCreationMinutes_Type = Integer32
_FlashMemoryStatusCreationMinutes_Object = MibTableColumn
flashMemoryStatusCreationMinutes = _FlashMemoryStatusCreationMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1, 6),
    _FlashMemoryStatusCreationMinutes_Type()
)
flashMemoryStatusCreationMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashMemoryStatusCreationMinutes.setStatus("mandatory")
_FlashMemoryStatusCreationSeconds_Type = Integer32
_FlashMemoryStatusCreationSeconds_Object = MibTableColumn
flashMemoryStatusCreationSeconds = _FlashMemoryStatusCreationSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1, 7),
    _FlashMemoryStatusCreationSeconds_Type()
)
flashMemoryStatusCreationSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashMemoryStatusCreationSeconds.setStatus("mandatory")
_FlashMemoryStatusCreationYear_Type = Integer32
_FlashMemoryStatusCreationYear_Object = MibTableColumn
flashMemoryStatusCreationYear = _FlashMemoryStatusCreationYear_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1, 8),
    _FlashMemoryStatusCreationYear_Type()
)
flashMemoryStatusCreationYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashMemoryStatusCreationYear.setStatus("mandatory")
_FlashMemoryStatusCreationMonth_Type = Integer32
_FlashMemoryStatusCreationMonth_Object = MibTableColumn
flashMemoryStatusCreationMonth = _FlashMemoryStatusCreationMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1, 9),
    _FlashMemoryStatusCreationMonth_Type()
)
flashMemoryStatusCreationMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashMemoryStatusCreationMonth.setStatus("mandatory")
_FlashMemoryStatusCreationDay_Type = Integer32
_FlashMemoryStatusCreationDay_Object = MibTableColumn
flashMemoryStatusCreationDay = _FlashMemoryStatusCreationDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1, 10),
    _FlashMemoryStatusCreationDay_Type()
)
flashMemoryStatusCreationDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashMemoryStatusCreationDay.setStatus("mandatory")
_FlashMemoryStatusImageChecksum_Type = Integer32
_FlashMemoryStatusImageChecksum_Object = MibTableColumn
flashMemoryStatusImageChecksum = _FlashMemoryStatusImageChecksum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1, 11),
    _FlashMemoryStatusImageChecksum_Type()
)
flashMemoryStatusImageChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashMemoryStatusImageChecksum.setStatus("mandatory")


class _FlashMemoryStatusPromID_Type(DisplayString):
    """Custom type flashMemoryStatusPromID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_FlashMemoryStatusPromID_Type.__name__ = "DisplayString"
_FlashMemoryStatusPromID_Object = MibTableColumn
flashMemoryStatusPromID = _FlashMemoryStatusPromID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 12, 1, 12),
    _FlashMemoryStatusPromID_Type()
)
flashMemoryStatusPromID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashMemoryStatusPromID.setStatus("mandatory")
_ChForceConnStatusTable_Object = MibTable
chForceConnStatusTable = _ChForceConnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 13)
)
if mibBuilder.loadTexts:
    chForceConnStatusTable.setStatus("mandatory")
_ChForceConnStatusEntry_Object = MibTableRow
chForceConnStatusEntry = _ChForceConnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 13, 1)
)
chForceConnStatusEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "chForceConnStatusCardNumber"),
    (0, "MICOM-NODE-MIB", "chForceConnStatusChannelNumber"),
)
if mibBuilder.loadTexts:
    chForceConnStatusEntry.setStatus("mandatory")


class _ChForceConnStatusCardNumber_Type(Integer32):
    """Custom type chForceConnStatusCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ChForceConnStatusCardNumber_Type.__name__ = "Integer32"
_ChForceConnStatusCardNumber_Object = MibTableColumn
chForceConnStatusCardNumber = _ChForceConnStatusCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 13, 1, 1),
    _ChForceConnStatusCardNumber_Type()
)
chForceConnStatusCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chForceConnStatusCardNumber.setStatus("mandatory")


class _ChForceConnStatusChannelNumber_Type(Integer32):
    """Custom type chForceConnStatusChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ChForceConnStatusChannelNumber_Type.__name__ = "Integer32"
_ChForceConnStatusChannelNumber_Object = MibTableColumn
chForceConnStatusChannelNumber = _ChForceConnStatusChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 13, 1, 2),
    _ChForceConnStatusChannelNumber_Type()
)
chForceConnStatusChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chForceConnStatusChannelNumber.setStatus("mandatory")


class _ChForceConnStatusNodeNumber_Type(Integer32):
    """Custom type chForceConnStatusNodeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChForceConnStatusNodeNumber_Type.__name__ = "Integer32"
_ChForceConnStatusNodeNumber_Object = MibTableColumn
chForceConnStatusNodeNumber = _ChForceConnStatusNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 13, 1, 3),
    _ChForceConnStatusNodeNumber_Type()
)
chForceConnStatusNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chForceConnStatusNodeNumber.setStatus("mandatory")


class _ChForceConnStatusToNodeNumber_Type(Integer32):
    """Custom type chForceConnStatusToNodeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChForceConnStatusToNodeNumber_Type.__name__ = "Integer32"
_ChForceConnStatusToNodeNumber_Object = MibTableColumn
chForceConnStatusToNodeNumber = _ChForceConnStatusToNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 13, 1, 4),
    _ChForceConnStatusToNodeNumber_Type()
)
chForceConnStatusToNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chForceConnStatusToNodeNumber.setStatus("mandatory")


class _ChForceConnStatusToCardNumber_Type(Integer32):
    """Custom type chForceConnStatusToCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ChForceConnStatusToCardNumber_Type.__name__ = "Integer32"
_ChForceConnStatusToCardNumber_Object = MibTableColumn
chForceConnStatusToCardNumber = _ChForceConnStatusToCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 13, 1, 5),
    _ChForceConnStatusToCardNumber_Type()
)
chForceConnStatusToCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chForceConnStatusToCardNumber.setStatus("mandatory")


class _ChForceConnStatusToChannelNumber_Type(Integer32):
    """Custom type chForceConnStatusToChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ChForceConnStatusToChannelNumber_Type.__name__ = "Integer32"
_ChForceConnStatusToChannelNumber_Object = MibTableColumn
chForceConnStatusToChannelNumber = _ChForceConnStatusToChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 5, 13, 1, 6),
    _ChForceConnStatusToChannelNumber_Type()
)
chForceConnStatusToChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chForceConnStatusToChannelNumber.setStatus("mandatory")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6)
)
_Statistics_configuration_ObjectIdentity = ObjectIdentity
statistics_configuration = _Statistics_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 1)
)
_SysPeriodicStatisticsReportGroup_ObjectIdentity = ObjectIdentity
sysPeriodicStatisticsReportGroup = _SysPeriodicStatisticsReportGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 1, 1)
)


class _SysPeriodicStatisticsReportInterval_Type(Integer32):
    """Custom type sysPeriodicStatisticsReportInterval based on Integer32"""
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
        *(("sixty", 5),
          ("ten", 2),
          ("thirty", 4),
          ("twenty", 3),
          ("zero", 1))
    )


_SysPeriodicStatisticsReportInterval_Type.__name__ = "Integer32"
_SysPeriodicStatisticsReportInterval_Object = MibScalar
sysPeriodicStatisticsReportInterval = _SysPeriodicStatisticsReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 1, 1, 1),
    _SysPeriodicStatisticsReportInterval_Type()
)
sysPeriodicStatisticsReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPeriodicStatisticsReportInterval.setStatus("mandatory")


class _SysReportDestination_Type(Integer32):
    """Custom type sysReportDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localCommandPort", 1),
          ("localLogPort", 2),
          ("remoteNode", 3))
    )


_SysReportDestination_Type.__name__ = "Integer32"
_SysReportDestination_Object = MibScalar
sysReportDestination = _SysReportDestination_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 1, 1, 2),
    _SysReportDestination_Type()
)
sysReportDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysReportDestination.setStatus("mandatory")


class _SysRemoteLogNodeName_Type(DisplayString):
    """Custom type sysRemoteLogNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SysRemoteLogNodeName_Type.__name__ = "DisplayString"
_SysRemoteLogNodeName_Object = MibScalar
sysRemoteLogNodeName = _SysRemoteLogNodeName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 1, 2),
    _SysRemoteLogNodeName_Type()
)
sysRemoteLogNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRemoteLogNodeName.setStatus("mandatory")
_LastPeriodicStatisticsTimeGroup_ObjectIdentity = ObjectIdentity
lastPeriodicStatisticsTimeGroup = _LastPeriodicStatisticsTimeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 1, 3)
)


class _LastPeriodicStatisticsTimeMonth_Type(Integer32):
    """Custom type lastPeriodicStatisticsTimeMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_LastPeriodicStatisticsTimeMonth_Type.__name__ = "Integer32"
_LastPeriodicStatisticsTimeMonth_Object = MibScalar
lastPeriodicStatisticsTimeMonth = _LastPeriodicStatisticsTimeMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 1, 3, 1),
    _LastPeriodicStatisticsTimeMonth_Type()
)
lastPeriodicStatisticsTimeMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodicStatisticsTimeMonth.setStatus("mandatory")


class _LastPeriodicStatisticsTimeDay_Type(Integer32):
    """Custom type lastPeriodicStatisticsTimeDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_LastPeriodicStatisticsTimeDay_Type.__name__ = "Integer32"
_LastPeriodicStatisticsTimeDay_Object = MibScalar
lastPeriodicStatisticsTimeDay = _LastPeriodicStatisticsTimeDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 1, 3, 2),
    _LastPeriodicStatisticsTimeDay_Type()
)
lastPeriodicStatisticsTimeDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodicStatisticsTimeDay.setStatus("mandatory")


class _LastPeriodicStatisticsTimeHours_Type(Integer32):
    """Custom type lastPeriodicStatisticsTimeHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LastPeriodicStatisticsTimeHours_Type.__name__ = "Integer32"
_LastPeriodicStatisticsTimeHours_Object = MibScalar
lastPeriodicStatisticsTimeHours = _LastPeriodicStatisticsTimeHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 1, 3, 3),
    _LastPeriodicStatisticsTimeHours_Type()
)
lastPeriodicStatisticsTimeHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodicStatisticsTimeHours.setStatus("mandatory")


class _LastPeriodicStatisticsTimeMinutes_Type(Integer32):
    """Custom type lastPeriodicStatisticsTimeMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LastPeriodicStatisticsTimeMinutes_Type.__name__ = "Integer32"
_LastPeriodicStatisticsTimeMinutes_Object = MibScalar
lastPeriodicStatisticsTimeMinutes = _LastPeriodicStatisticsTimeMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 1, 3, 4),
    _LastPeriodicStatisticsTimeMinutes_Type()
)
lastPeriodicStatisticsTimeMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodicStatisticsTimeMinutes.setStatus("mandatory")


class _LastPeriodicStatisticsTimeSeconds_Type(Integer32):
    """Custom type lastPeriodicStatisticsTimeSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LastPeriodicStatisticsTimeSeconds_Type.__name__ = "Integer32"
_LastPeriodicStatisticsTimeSeconds_Object = MibScalar
lastPeriodicStatisticsTimeSeconds = _LastPeriodicStatisticsTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 1, 3, 5),
    _LastPeriodicStatisticsTimeSeconds_Type()
)
lastPeriodicStatisticsTimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPeriodicStatisticsTimeSeconds.setStatus("mandatory")


class _SwitchStatistics_Type(Integer32):
    """Custom type switchStatistics based on Integer32"""
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


_SwitchStatistics_Type.__name__ = "Integer32"
_SwitchStatistics_Object = MibScalar
switchStatistics = _SwitchStatistics_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 1, 4),
    _SwitchStatistics_Type()
)
switchStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchStatistics.setStatus("mandatory")
_Statistics_periodic_ObjectIdentity = ObjectIdentity
statistics_periodic = _Statistics_periodic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2)
)
_ChPeriodicStatisticsTable_Object = MibTable
chPeriodicStatisticsTable = _ChPeriodicStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    chPeriodicStatisticsTable.setStatus("mandatory")
_ChPeriodicStatisticsEntry_Object = MibTableRow
chPeriodicStatisticsEntry = _ChPeriodicStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 1, 1)
)
chPeriodicStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "chPeriodicStatisticsCardNumber"),
    (0, "MICOM-NODE-MIB", "chPeriodicStatisticsChannelNumber"),
)
if mibBuilder.loadTexts:
    chPeriodicStatisticsEntry.setStatus("mandatory")


class _ChPeriodicStatisticsCardNumber_Type(Integer32):
    """Custom type chPeriodicStatisticsCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ChPeriodicStatisticsCardNumber_Type.__name__ = "Integer32"
_ChPeriodicStatisticsCardNumber_Object = MibTableColumn
chPeriodicStatisticsCardNumber = _ChPeriodicStatisticsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 1, 1, 1),
    _ChPeriodicStatisticsCardNumber_Type()
)
chPeriodicStatisticsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPeriodicStatisticsCardNumber.setStatus("mandatory")
_ChPeriodicStatisticsChannelNumber_Type = Integer32
_ChPeriodicStatisticsChannelNumber_Object = MibTableColumn
chPeriodicStatisticsChannelNumber = _ChPeriodicStatisticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 1, 1, 2),
    _ChPeriodicStatisticsChannelNumber_Type()
)
chPeriodicStatisticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPeriodicStatisticsChannelNumber.setStatus("mandatory")


class _ChPeriodicStatisticsMonth_Type(Integer32):
    """Custom type chPeriodicStatisticsMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ChPeriodicStatisticsMonth_Type.__name__ = "Integer32"
_ChPeriodicStatisticsMonth_Object = MibTableColumn
chPeriodicStatisticsMonth = _ChPeriodicStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 1, 1, 3),
    _ChPeriodicStatisticsMonth_Type()
)
chPeriodicStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPeriodicStatisticsMonth.setStatus("mandatory")


class _ChPeriodicStatisticsDay_Type(Integer32):
    """Custom type chPeriodicStatisticsDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ChPeriodicStatisticsDay_Type.__name__ = "Integer32"
_ChPeriodicStatisticsDay_Object = MibTableColumn
chPeriodicStatisticsDay = _ChPeriodicStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 1, 1, 4),
    _ChPeriodicStatisticsDay_Type()
)
chPeriodicStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPeriodicStatisticsDay.setStatus("mandatory")


class _ChPeriodicStatisticsHours_Type(Integer32):
    """Custom type chPeriodicStatisticsHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_ChPeriodicStatisticsHours_Type.__name__ = "Integer32"
_ChPeriodicStatisticsHours_Object = MibTableColumn
chPeriodicStatisticsHours = _ChPeriodicStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 1, 1, 5),
    _ChPeriodicStatisticsHours_Type()
)
chPeriodicStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPeriodicStatisticsHours.setStatus("mandatory")


class _ChPeriodicStatisticsMinutes_Type(Integer32):
    """Custom type chPeriodicStatisticsMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_ChPeriodicStatisticsMinutes_Type.__name__ = "Integer32"
_ChPeriodicStatisticsMinutes_Object = MibTableColumn
chPeriodicStatisticsMinutes = _ChPeriodicStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 1, 1, 6),
    _ChPeriodicStatisticsMinutes_Type()
)
chPeriodicStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPeriodicStatisticsMinutes.setStatus("mandatory")


class _ChPeriodicStatisticsSeconds_Type(Integer32):
    """Custom type chPeriodicStatisticsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_ChPeriodicStatisticsSeconds_Type.__name__ = "Integer32"
_ChPeriodicStatisticsSeconds_Object = MibTableColumn
chPeriodicStatisticsSeconds = _ChPeriodicStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 1, 1, 7),
    _ChPeriodicStatisticsSeconds_Type()
)
chPeriodicStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPeriodicStatisticsSeconds.setStatus("mandatory")
_ChPeriodicStatisticsBuffUtilization_Type = Gauge32
_ChPeriodicStatisticsBuffUtilization_Object = MibTableColumn
chPeriodicStatisticsBuffUtilization = _ChPeriodicStatisticsBuffUtilization_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 1, 1, 8),
    _ChPeriodicStatisticsBuffUtilization_Type()
)
chPeriodicStatisticsBuffUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPeriodicStatisticsBuffUtilization.setStatus("mandatory")


class _ChPeriodicStatisticsChannelBusiedOut_Type(Integer32):
    """Custom type chPeriodicStatisticsChannelBusiedOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ChPeriodicStatisticsChannelBusiedOut_Type.__name__ = "Integer32"
_ChPeriodicStatisticsChannelBusiedOut_Object = MibTableColumn
chPeriodicStatisticsChannelBusiedOut = _ChPeriodicStatisticsChannelBusiedOut_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 1, 1, 9),
    _ChPeriodicStatisticsChannelBusiedOut_Type()
)
chPeriodicStatisticsChannelBusiedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPeriodicStatisticsChannelBusiedOut.setStatus("mandatory")


class _ChPeriodicStatisticsChannelInFlowControl_Type(Integer32):
    """Custom type chPeriodicStatisticsChannelInFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ChPeriodicStatisticsChannelInFlowControl_Type.__name__ = "Integer32"
_ChPeriodicStatisticsChannelInFlowControl_Object = MibTableColumn
chPeriodicStatisticsChannelInFlowControl = _ChPeriodicStatisticsChannelInFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 1, 1, 10),
    _ChPeriodicStatisticsChannelInFlowControl_Type()
)
chPeriodicStatisticsChannelInFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPeriodicStatisticsChannelInFlowControl.setStatus("mandatory")
_ChVPeriodicStatisticsTable_Object = MibTable
chVPeriodicStatisticsTable = _ChVPeriodicStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    chVPeriodicStatisticsTable.setStatus("mandatory")
_ChVPeriodicStatisticsEntry_Object = MibTableRow
chVPeriodicStatisticsEntry = _ChVPeriodicStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1)
)
chVPeriodicStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "chVPeriodicStatisticsCardNumber"),
    (0, "MICOM-NODE-MIB", "chVPeriodicStatisticsChannelNumber"),
)
if mibBuilder.loadTexts:
    chVPeriodicStatisticsEntry.setStatus("mandatory")


class _ChVPeriodicStatisticsCardNumber_Type(Integer32):
    """Custom type chVPeriodicStatisticsCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_ChVPeriodicStatisticsCardNumber_Type.__name__ = "Integer32"
_ChVPeriodicStatisticsCardNumber_Object = MibTableColumn
chVPeriodicStatisticsCardNumber = _ChVPeriodicStatisticsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 1),
    _ChVPeriodicStatisticsCardNumber_Type()
)
chVPeriodicStatisticsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsCardNumber.setStatus("mandatory")
_ChVPeriodicStatisticsChannelNumber_Type = Integer32
_ChVPeriodicStatisticsChannelNumber_Object = MibTableColumn
chVPeriodicStatisticsChannelNumber = _ChVPeriodicStatisticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 2),
    _ChVPeriodicStatisticsChannelNumber_Type()
)
chVPeriodicStatisticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsChannelNumber.setStatus("mandatory")


class _ChVPeriodicStatisticsMonth_Type(Integer32):
    """Custom type chVPeriodicStatisticsMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ChVPeriodicStatisticsMonth_Type.__name__ = "Integer32"
_ChVPeriodicStatisticsMonth_Object = MibTableColumn
chVPeriodicStatisticsMonth = _ChVPeriodicStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 3),
    _ChVPeriodicStatisticsMonth_Type()
)
chVPeriodicStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsMonth.setStatus("mandatory")


class _ChVPeriodicStatisticsDay_Type(Integer32):
    """Custom type chVPeriodicStatisticsDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ChVPeriodicStatisticsDay_Type.__name__ = "Integer32"
_ChVPeriodicStatisticsDay_Object = MibTableColumn
chVPeriodicStatisticsDay = _ChVPeriodicStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 4),
    _ChVPeriodicStatisticsDay_Type()
)
chVPeriodicStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsDay.setStatus("mandatory")


class _ChVPeriodicStatisticsHours_Type(Integer32):
    """Custom type chVPeriodicStatisticsHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_ChVPeriodicStatisticsHours_Type.__name__ = "Integer32"
_ChVPeriodicStatisticsHours_Object = MibTableColumn
chVPeriodicStatisticsHours = _ChVPeriodicStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 5),
    _ChVPeriodicStatisticsHours_Type()
)
chVPeriodicStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsHours.setStatus("mandatory")


class _ChVPeriodicStatisticsMinutes_Type(Integer32):
    """Custom type chVPeriodicStatisticsMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_ChVPeriodicStatisticsMinutes_Type.__name__ = "Integer32"
_ChVPeriodicStatisticsMinutes_Object = MibTableColumn
chVPeriodicStatisticsMinutes = _ChVPeriodicStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 6),
    _ChVPeriodicStatisticsMinutes_Type()
)
chVPeriodicStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsMinutes.setStatus("mandatory")


class _ChVPeriodicStatisticsSeconds_Type(Integer32):
    """Custom type chVPeriodicStatisticsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_ChVPeriodicStatisticsSeconds_Type.__name__ = "Integer32"
_ChVPeriodicStatisticsSeconds_Object = MibTableColumn
chVPeriodicStatisticsSeconds = _ChVPeriodicStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 7),
    _ChVPeriodicStatisticsSeconds_Type()
)
chVPeriodicStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsSeconds.setStatus("mandatory")
_ChVPeriodicStatisticsConnectTime_Type = Integer32
_ChVPeriodicStatisticsConnectTime_Object = MibTableColumn
chVPeriodicStatisticsConnectTime = _ChVPeriodicStatisticsConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 8),
    _ChVPeriodicStatisticsConnectTime_Type()
)
chVPeriodicStatisticsConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsConnectTime.setStatus("mandatory")
_ChVPeriodicStatisticsTotalCalls_Type = Counter32
_ChVPeriodicStatisticsTotalCalls_Object = MibTableColumn
chVPeriodicStatisticsTotalCalls = _ChVPeriodicStatisticsTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 9),
    _ChVPeriodicStatisticsTotalCalls_Type()
)
chVPeriodicStatisticsTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsTotalCalls.setStatus("mandatory")
_ChVPeriodicStatisticsAvgCallDuration_Type = Integer32
_ChVPeriodicStatisticsAvgCallDuration_Object = MibTableColumn
chVPeriodicStatisticsAvgCallDuration = _ChVPeriodicStatisticsAvgCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 10),
    _ChVPeriodicStatisticsAvgCallDuration_Type()
)
chVPeriodicStatisticsAvgCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsAvgCallDuration.setStatus("mandatory")
_ChVPeriodicStatisticsBusyOutTime_Type = Integer32
_ChVPeriodicStatisticsBusyOutTime_Object = MibTableColumn
chVPeriodicStatisticsBusyOutTime = _ChVPeriodicStatisticsBusyOutTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 11),
    _ChVPeriodicStatisticsBusyOutTime_Type()
)
chVPeriodicStatisticsBusyOutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsBusyOutTime.setStatus("mandatory")
_ChVPeriodicStatisticsNumOfCallAttempts_Type = Counter32
_ChVPeriodicStatisticsNumOfCallAttempts_Object = MibTableColumn
chVPeriodicStatisticsNumOfCallAttempts = _ChVPeriodicStatisticsNumOfCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 12),
    _ChVPeriodicStatisticsNumOfCallAttempts_Type()
)
chVPeriodicStatisticsNumOfCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsNumOfCallAttempts.setStatus("mandatory")
_ChVPeriodicStatisticsDiscardedFrameCounts_Type = Counter32
_ChVPeriodicStatisticsDiscardedFrameCounts_Object = MibTableColumn
chVPeriodicStatisticsDiscardedFrameCounts = _ChVPeriodicStatisticsDiscardedFrameCounts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 13),
    _ChVPeriodicStatisticsDiscardedFrameCounts_Type()
)
chVPeriodicStatisticsDiscardedFrameCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsDiscardedFrameCounts.setStatus("mandatory")
_ChVPeriodicStatisticsTimeInFaxMode_Type = Integer32
_ChVPeriodicStatisticsTimeInFaxMode_Object = MibTableColumn
chVPeriodicStatisticsTimeInFaxMode = _ChVPeriodicStatisticsTimeInFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 14),
    _ChVPeriodicStatisticsTimeInFaxMode_Type()
)
chVPeriodicStatisticsTimeInFaxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsTimeInFaxMode.setStatus("mandatory")
_ChVPeriodicStatisticsPercentInFaxMode_Type = Gauge32
_ChVPeriodicStatisticsPercentInFaxMode_Object = MibTableColumn
chVPeriodicStatisticsPercentInFaxMode = _ChVPeriodicStatisticsPercentInFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 2, 1, 15),
    _ChVPeriodicStatisticsPercentInFaxMode_Type()
)
chVPeriodicStatisticsPercentInFaxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVPeriodicStatisticsPercentInFaxMode.setStatus("mandatory")
_LinkPeriodicStatisticsTable_Object = MibTable
linkPeriodicStatisticsTable = _LinkPeriodicStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    linkPeriodicStatisticsTable.setStatus("mandatory")
_LinkPeriodicStatisticsEntry_Object = MibTableRow
linkPeriodicStatisticsEntry = _LinkPeriodicStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1)
)
linkPeriodicStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "linkPeriodicStatisticsCardNumber"),
    (0, "MICOM-NODE-MIB", "linkPeriodicStatisticsChannelNumber"),
)
if mibBuilder.loadTexts:
    linkPeriodicStatisticsEntry.setStatus("mandatory")


class _LinkPeriodicStatisticsCardNumber_Type(Integer32):
    """Custom type linkPeriodicStatisticsCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_LinkPeriodicStatisticsCardNumber_Type.__name__ = "Integer32"
_LinkPeriodicStatisticsCardNumber_Object = MibTableColumn
linkPeriodicStatisticsCardNumber = _LinkPeriodicStatisticsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 1),
    _LinkPeriodicStatisticsCardNumber_Type()
)
linkPeriodicStatisticsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsCardNumber.setStatus("mandatory")
_LinkPeriodicStatisticsChannelNumber_Type = Integer32
_LinkPeriodicStatisticsChannelNumber_Object = MibTableColumn
linkPeriodicStatisticsChannelNumber = _LinkPeriodicStatisticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 2),
    _LinkPeriodicStatisticsChannelNumber_Type()
)
linkPeriodicStatisticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsChannelNumber.setStatus("mandatory")


class _LinkPeriodicStatisticsMonth_Type(Integer32):
    """Custom type linkPeriodicStatisticsMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_LinkPeriodicStatisticsMonth_Type.__name__ = "Integer32"
_LinkPeriodicStatisticsMonth_Object = MibTableColumn
linkPeriodicStatisticsMonth = _LinkPeriodicStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 3),
    _LinkPeriodicStatisticsMonth_Type()
)
linkPeriodicStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsMonth.setStatus("mandatory")


class _LinkPeriodicStatisticsDay_Type(Integer32):
    """Custom type linkPeriodicStatisticsDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_LinkPeriodicStatisticsDay_Type.__name__ = "Integer32"
_LinkPeriodicStatisticsDay_Object = MibTableColumn
linkPeriodicStatisticsDay = _LinkPeriodicStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 4),
    _LinkPeriodicStatisticsDay_Type()
)
linkPeriodicStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsDay.setStatus("mandatory")


class _LinkPeriodicStatisticsHours_Type(Integer32):
    """Custom type linkPeriodicStatisticsHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LinkPeriodicStatisticsHours_Type.__name__ = "Integer32"
_LinkPeriodicStatisticsHours_Object = MibTableColumn
linkPeriodicStatisticsHours = _LinkPeriodicStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 5),
    _LinkPeriodicStatisticsHours_Type()
)
linkPeriodicStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsHours.setStatus("mandatory")


class _LinkPeriodicStatisticsMinutes_Type(Integer32):
    """Custom type linkPeriodicStatisticsMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LinkPeriodicStatisticsMinutes_Type.__name__ = "Integer32"
_LinkPeriodicStatisticsMinutes_Object = MibTableColumn
linkPeriodicStatisticsMinutes = _LinkPeriodicStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 6),
    _LinkPeriodicStatisticsMinutes_Type()
)
linkPeriodicStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsMinutes.setStatus("mandatory")


class _LinkPeriodicStatisticsSeconds_Type(Integer32):
    """Custom type linkPeriodicStatisticsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LinkPeriodicStatisticsSeconds_Type.__name__ = "Integer32"
_LinkPeriodicStatisticsSeconds_Object = MibTableColumn
linkPeriodicStatisticsSeconds = _LinkPeriodicStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 7),
    _LinkPeriodicStatisticsSeconds_Type()
)
linkPeriodicStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsSeconds.setStatus("mandatory")


class _LinkPeriodicStatisticsLinkType_Type(Integer32):
    """Custom type linkPeriodicStatisticsLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("esi", 2),
          ("esiSecondary", 5),
          ("esm", 1),
          ("frameRelay", 6),
          ("localEsi", 4),
          ("xDot21", 3))
    )


_LinkPeriodicStatisticsLinkType_Type.__name__ = "Integer32"
_LinkPeriodicStatisticsLinkType_Object = MibTableColumn
linkPeriodicStatisticsLinkType = _LinkPeriodicStatisticsLinkType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 8),
    _LinkPeriodicStatisticsLinkType_Type()
)
linkPeriodicStatisticsLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsLinkType.setStatus("mandatory")
_LinkPeriodicStatisticsTxFrames_Type = Counter32
_LinkPeriodicStatisticsTxFrames_Object = MibTableColumn
linkPeriodicStatisticsTxFrames = _LinkPeriodicStatisticsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 9),
    _LinkPeriodicStatisticsTxFrames_Type()
)
linkPeriodicStatisticsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsTxFrames.setStatus("mandatory")
_LinkPeriodicStatisticsRxFrames_Type = Counter32
_LinkPeriodicStatisticsRxFrames_Object = MibTableColumn
linkPeriodicStatisticsRxFrames = _LinkPeriodicStatisticsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 10),
    _LinkPeriodicStatisticsRxFrames_Type()
)
linkPeriodicStatisticsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsRxFrames.setStatus("mandatory")
_LinkPeriodicStatisticsLocCompositeUtil_Type = Gauge32
_LinkPeriodicStatisticsLocCompositeUtil_Object = MibTableColumn
linkPeriodicStatisticsLocCompositeUtil = _LinkPeriodicStatisticsLocCompositeUtil_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 11),
    _LinkPeriodicStatisticsLocCompositeUtil_Type()
)
linkPeriodicStatisticsLocCompositeUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsLocCompositeUtil.setStatus("mandatory")
_LinkPeriodicStatisticsRemCompositeUtil_Type = Gauge32
_LinkPeriodicStatisticsRemCompositeUtil_Object = MibTableColumn
linkPeriodicStatisticsRemCompositeUtil = _LinkPeriodicStatisticsRemCompositeUtil_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 12),
    _LinkPeriodicStatisticsRemCompositeUtil_Type()
)
linkPeriodicStatisticsRemCompositeUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsRemCompositeUtil.setStatus("mandatory")
_LinkPeriodicStatisticsLocBufferUtil_Type = Gauge32
_LinkPeriodicStatisticsLocBufferUtil_Object = MibTableColumn
linkPeriodicStatisticsLocBufferUtil = _LinkPeriodicStatisticsLocBufferUtil_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 13),
    _LinkPeriodicStatisticsLocBufferUtil_Type()
)
linkPeriodicStatisticsLocBufferUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsLocBufferUtil.setStatus("mandatory")
_LinkPeriodicStatisticsRemBufferUtil_Type = Gauge32
_LinkPeriodicStatisticsRemBufferUtil_Object = MibTableColumn
linkPeriodicStatisticsRemBufferUtil = _LinkPeriodicStatisticsRemBufferUtil_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 14),
    _LinkPeriodicStatisticsRemBufferUtil_Type()
)
linkPeriodicStatisticsRemBufferUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsRemBufferUtil.setStatus("mandatory")
_LinkPeriodicStatisticsLocRetransmits_Type = Counter32
_LinkPeriodicStatisticsLocRetransmits_Object = MibTableColumn
linkPeriodicStatisticsLocRetransmits = _LinkPeriodicStatisticsLocRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 15),
    _LinkPeriodicStatisticsLocRetransmits_Type()
)
linkPeriodicStatisticsLocRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsLocRetransmits.setStatus("mandatory")
_LinkPeriodicStatisticsRemRetransmits_Type = Counter32
_LinkPeriodicStatisticsRemRetransmits_Object = MibTableColumn
linkPeriodicStatisticsRemRetransmits = _LinkPeriodicStatisticsRemRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 16),
    _LinkPeriodicStatisticsRemRetransmits_Type()
)
linkPeriodicStatisticsRemRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsRemRetransmits.setStatus("mandatory")
_LinkPeriodicStatisticsLocLineAlarms_Type = Integer32
_LinkPeriodicStatisticsLocLineAlarms_Object = MibTableColumn
linkPeriodicStatisticsLocLineAlarms = _LinkPeriodicStatisticsLocLineAlarms_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 17),
    _LinkPeriodicStatisticsLocLineAlarms_Type()
)
linkPeriodicStatisticsLocLineAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsLocLineAlarms.setStatus("mandatory")
_LinkPeriodicStatisticsRemLineAlarms_Type = Integer32
_LinkPeriodicStatisticsRemLineAlarms_Object = MibTableColumn
linkPeriodicStatisticsRemLineAlarms = _LinkPeriodicStatisticsRemLineAlarms_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 18),
    _LinkPeriodicStatisticsRemLineAlarms_Type()
)
linkPeriodicStatisticsRemLineAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsRemLineAlarms.setStatus("mandatory")
_LinkPeriodicStatisticsLocTimeInSysFlowCtrl_Type = Integer32
_LinkPeriodicStatisticsLocTimeInSysFlowCtrl_Object = MibTableColumn
linkPeriodicStatisticsLocTimeInSysFlowCtrl = _LinkPeriodicStatisticsLocTimeInSysFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 19),
    _LinkPeriodicStatisticsLocTimeInSysFlowCtrl_Type()
)
linkPeriodicStatisticsLocTimeInSysFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsLocTimeInSysFlowCtrl.setStatus("mandatory")
_LinkPeriodicStatisticsRemTimeInSysFlowCtrl_Type = Integer32
_LinkPeriodicStatisticsRemTimeInSysFlowCtrl_Object = MibTableColumn
linkPeriodicStatisticsRemTimeInSysFlowCtrl = _LinkPeriodicStatisticsRemTimeInSysFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 20),
    _LinkPeriodicStatisticsRemTimeInSysFlowCtrl_Type()
)
linkPeriodicStatisticsRemTimeInSysFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsRemTimeInSysFlowCtrl.setStatus("mandatory")
_LinkPeriodicStatisticsLocTimeInSyncLossOrX21Connect_Type = Integer32
_LinkPeriodicStatisticsLocTimeInSyncLossOrX21Connect_Object = MibTableColumn
linkPeriodicStatisticsLocTimeInSyncLossOrX21Connect = _LinkPeriodicStatisticsLocTimeInSyncLossOrX21Connect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 21),
    _LinkPeriodicStatisticsLocTimeInSyncLossOrX21Connect_Type()
)
linkPeriodicStatisticsLocTimeInSyncLossOrX21Connect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsLocTimeInSyncLossOrX21Connect.setStatus("mandatory")
_LinkPeriodicStatisticsRemTimeInSyncLoss_Type = Integer32
_LinkPeriodicStatisticsRemTimeInSyncLoss_Object = MibTableColumn
linkPeriodicStatisticsRemTimeInSyncLoss = _LinkPeriodicStatisticsRemTimeInSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 22),
    _LinkPeriodicStatisticsRemTimeInSyncLoss_Type()
)
linkPeriodicStatisticsRemTimeInSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsRemTimeInSyncLoss.setStatus("mandatory")
_LinkPeriodicStatisticsLocTimeInCarrierLoss_Type = Integer32
_LinkPeriodicStatisticsLocTimeInCarrierLoss_Object = MibTableColumn
linkPeriodicStatisticsLocTimeInCarrierLoss = _LinkPeriodicStatisticsLocTimeInCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 23),
    _LinkPeriodicStatisticsLocTimeInCarrierLoss_Type()
)
linkPeriodicStatisticsLocTimeInCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsLocTimeInCarrierLoss.setStatus("mandatory")
_LinkPeriodicStatisticsRemTimeInCarrierLoss_Type = Integer32
_LinkPeriodicStatisticsRemTimeInCarrierLoss_Object = MibTableColumn
linkPeriodicStatisticsRemTimeInCarrierLoss = _LinkPeriodicStatisticsRemTimeInCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 3, 1, 24),
    _LinkPeriodicStatisticsRemTimeInCarrierLoss_Type()
)
linkPeriodicStatisticsRemTimeInCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeriodicStatisticsRemTimeInCarrierLoss.setStatus("mandatory")
_LinkFRPeriodicStatisticsTable_Object = MibTable
linkFRPeriodicStatisticsTable = _LinkFRPeriodicStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4)
)
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsTable.setStatus("mandatory")
_LinkFRPeriodicStatisticsEntry_Object = MibTableRow
linkFRPeriodicStatisticsEntry = _LinkFRPeriodicStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1)
)
linkFRPeriodicStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "linkFRPeriodicStatisticsCardNumber"),
    (0, "MICOM-NODE-MIB", "linkFRPeriodicStatisticsChannelNumber"),
)
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsEntry.setStatus("mandatory")


class _LinkFRPeriodicStatisticsCardNumber_Type(Integer32):
    """Custom type linkFRPeriodicStatisticsCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_LinkFRPeriodicStatisticsCardNumber_Type.__name__ = "Integer32"
_LinkFRPeriodicStatisticsCardNumber_Object = MibTableColumn
linkFRPeriodicStatisticsCardNumber = _LinkFRPeriodicStatisticsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 1),
    _LinkFRPeriodicStatisticsCardNumber_Type()
)
linkFRPeriodicStatisticsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsCardNumber.setStatus("mandatory")
_LinkFRPeriodicStatisticsChannelNumber_Type = Integer32
_LinkFRPeriodicStatisticsChannelNumber_Object = MibTableColumn
linkFRPeriodicStatisticsChannelNumber = _LinkFRPeriodicStatisticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 2),
    _LinkFRPeriodicStatisticsChannelNumber_Type()
)
linkFRPeriodicStatisticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsChannelNumber.setStatus("mandatory")
_LinkFRPeriodicStatisticsMonth_Type = Integer32
_LinkFRPeriodicStatisticsMonth_Object = MibTableColumn
linkFRPeriodicStatisticsMonth = _LinkFRPeriodicStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 3),
    _LinkFRPeriodicStatisticsMonth_Type()
)
linkFRPeriodicStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsMonth.setStatus("mandatory")
_LinkFRPeriodicStatisticsDay_Type = Integer32
_LinkFRPeriodicStatisticsDay_Object = MibTableColumn
linkFRPeriodicStatisticsDay = _LinkFRPeriodicStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 4),
    _LinkFRPeriodicStatisticsDay_Type()
)
linkFRPeriodicStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsDay.setStatus("mandatory")
_LinkFRPeriodicStatisticsHours_Type = Integer32
_LinkFRPeriodicStatisticsHours_Object = MibTableColumn
linkFRPeriodicStatisticsHours = _LinkFRPeriodicStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 5),
    _LinkFRPeriodicStatisticsHours_Type()
)
linkFRPeriodicStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsHours.setStatus("mandatory")
_LinkFRPeriodicStatisticsMinutes_Type = Integer32
_LinkFRPeriodicStatisticsMinutes_Object = MibTableColumn
linkFRPeriodicStatisticsMinutes = _LinkFRPeriodicStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 6),
    _LinkFRPeriodicStatisticsMinutes_Type()
)
linkFRPeriodicStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsMinutes.setStatus("mandatory")
_LinkFRPeriodicStatisticsSeconds_Type = Integer32
_LinkFRPeriodicStatisticsSeconds_Object = MibTableColumn
linkFRPeriodicStatisticsSeconds = _LinkFRPeriodicStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 7),
    _LinkFRPeriodicStatisticsSeconds_Type()
)
linkFRPeriodicStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsSeconds.setStatus("mandatory")
_LinkFRPeriodicStatisticsCRCErrs_Type = Counter32
_LinkFRPeriodicStatisticsCRCErrs_Object = MibTableColumn
linkFRPeriodicStatisticsCRCErrs = _LinkFRPeriodicStatisticsCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 8),
    _LinkFRPeriodicStatisticsCRCErrs_Type()
)
linkFRPeriodicStatisticsCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsCRCErrs.setStatus("mandatory")
_LinkFRPeriodicStatisticsLostStatusMsgCounts_Type = Counter32
_LinkFRPeriodicStatisticsLostStatusMsgCounts_Object = MibTableColumn
linkFRPeriodicStatisticsLostStatusMsgCounts = _LinkFRPeriodicStatisticsLostStatusMsgCounts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 9),
    _LinkFRPeriodicStatisticsLostStatusMsgCounts_Type()
)
linkFRPeriodicStatisticsLostStatusMsgCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsLostStatusMsgCounts.setStatus("mandatory")
_LinkFRPeriodicStatisticsStatusMsgProtocolErrs_Type = Counter32
_LinkFRPeriodicStatisticsStatusMsgProtocolErrs_Object = MibTableColumn
linkFRPeriodicStatisticsStatusMsgProtocolErrs = _LinkFRPeriodicStatisticsStatusMsgProtocolErrs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 10),
    _LinkFRPeriodicStatisticsStatusMsgProtocolErrs_Type()
)
linkFRPeriodicStatisticsStatusMsgProtocolErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsStatusMsgProtocolErrs.setStatus("mandatory")
_LinkFRPeriodicStatisticsNetworkResets_Type = Counter32
_LinkFRPeriodicStatisticsNetworkResets_Object = MibTableColumn
linkFRPeriodicStatisticsNetworkResets = _LinkFRPeriodicStatisticsNetworkResets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 11),
    _LinkFRPeriodicStatisticsNetworkResets_Type()
)
linkFRPeriodicStatisticsNetworkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsNetworkResets.setStatus("mandatory")
_LinkFRPeriodicStatisticsLinkResets_Type = Counter32
_LinkFRPeriodicStatisticsLinkResets_Object = MibTableColumn
linkFRPeriodicStatisticsLinkResets = _LinkFRPeriodicStatisticsLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 12),
    _LinkFRPeriodicStatisticsLinkResets_Type()
)
linkFRPeriodicStatisticsLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsLinkResets.setStatus("mandatory")
_LinkFRPeriodicStatisticsNumOfDLCIs_Type = Integer32
_LinkFRPeriodicStatisticsNumOfDLCIs_Object = MibTableColumn
linkFRPeriodicStatisticsNumOfDLCIs = _LinkFRPeriodicStatisticsNumOfDLCIs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 4, 1, 13),
    _LinkFRPeriodicStatisticsNumOfDLCIs_Type()
)
linkFRPeriodicStatisticsNumOfDLCIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRPeriodicStatisticsNumOfDLCIs.setStatus("mandatory")
_LinkFRDLCIPeriodicStatisticsTable_Object = MibTable
linkFRDLCIPeriodicStatisticsTable = _LinkFRDLCIPeriodicStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5)
)
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsTable.setStatus("mandatory")
_LinkFRDLCIPeriodicStatisticsEntry_Object = MibTableRow
linkFRDLCIPeriodicStatisticsEntry = _LinkFRDLCIPeriodicStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1)
)
linkFRDLCIPeriodicStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "linkFRDLCIPeriodicStatisticsCardNumber"),
    (0, "MICOM-NODE-MIB", "linkFRDLCIPeriodicStatisticsChannelNumber"),
    (0, "MICOM-NODE-MIB", "linkFRDLCIPeriodicStatisticsDLCINumber"),
)
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsEntry.setStatus("mandatory")


class _LinkFRDLCIPeriodicStatisticsCardNumber_Type(Integer32):
    """Custom type linkFRDLCIPeriodicStatisticsCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_LinkFRDLCIPeriodicStatisticsCardNumber_Type.__name__ = "Integer32"
_LinkFRDLCIPeriodicStatisticsCardNumber_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsCardNumber = _LinkFRDLCIPeriodicStatisticsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 1),
    _LinkFRDLCIPeriodicStatisticsCardNumber_Type()
)
linkFRDLCIPeriodicStatisticsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsCardNumber.setStatus("mandatory")
_LinkFRDLCIPeriodicStatisticsChannelNumber_Type = Integer32
_LinkFRDLCIPeriodicStatisticsChannelNumber_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsChannelNumber = _LinkFRDLCIPeriodicStatisticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 2),
    _LinkFRDLCIPeriodicStatisticsChannelNumber_Type()
)
linkFRDLCIPeriodicStatisticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsChannelNumber.setStatus("mandatory")
_LinkFRDLCIPeriodicStatisticsDLCINumber_Type = Integer32
_LinkFRDLCIPeriodicStatisticsDLCINumber_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsDLCINumber = _LinkFRDLCIPeriodicStatisticsDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 3),
    _LinkFRDLCIPeriodicStatisticsDLCINumber_Type()
)
linkFRDLCIPeriodicStatisticsDLCINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsDLCINumber.setStatus("mandatory")


class _LinkFRDLCIPeriodicStatisticsMonth_Type(Integer32):
    """Custom type linkFRDLCIPeriodicStatisticsMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_LinkFRDLCIPeriodicStatisticsMonth_Type.__name__ = "Integer32"
_LinkFRDLCIPeriodicStatisticsMonth_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsMonth = _LinkFRDLCIPeriodicStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 4),
    _LinkFRDLCIPeriodicStatisticsMonth_Type()
)
linkFRDLCIPeriodicStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsMonth.setStatus("mandatory")


class _LinkFRDLCIPeriodicStatisticsDay_Type(Integer32):
    """Custom type linkFRDLCIPeriodicStatisticsDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_LinkFRDLCIPeriodicStatisticsDay_Type.__name__ = "Integer32"
_LinkFRDLCIPeriodicStatisticsDay_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsDay = _LinkFRDLCIPeriodicStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 5),
    _LinkFRDLCIPeriodicStatisticsDay_Type()
)
linkFRDLCIPeriodicStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsDay.setStatus("mandatory")


class _LinkFRDLCIPeriodicStatisticsHours_Type(Integer32):
    """Custom type linkFRDLCIPeriodicStatisticsHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LinkFRDLCIPeriodicStatisticsHours_Type.__name__ = "Integer32"
_LinkFRDLCIPeriodicStatisticsHours_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsHours = _LinkFRDLCIPeriodicStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 6),
    _LinkFRDLCIPeriodicStatisticsHours_Type()
)
linkFRDLCIPeriodicStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsHours.setStatus("mandatory")


class _LinkFRDLCIPeriodicStatisticsMinutes_Type(Integer32):
    """Custom type linkFRDLCIPeriodicStatisticsMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LinkFRDLCIPeriodicStatisticsMinutes_Type.__name__ = "Integer32"
_LinkFRDLCIPeriodicStatisticsMinutes_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsMinutes = _LinkFRDLCIPeriodicStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 7),
    _LinkFRDLCIPeriodicStatisticsMinutes_Type()
)
linkFRDLCIPeriodicStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsMinutes.setStatus("mandatory")


class _LinkFRDLCIPeriodicStatisticsSeconds_Type(Integer32):
    """Custom type linkFRDLCIPeriodicStatisticsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LinkFRDLCIPeriodicStatisticsSeconds_Type.__name__ = "Integer32"
_LinkFRDLCIPeriodicStatisticsSeconds_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsSeconds = _LinkFRDLCIPeriodicStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 8),
    _LinkFRDLCIPeriodicStatisticsSeconds_Type()
)
linkFRDLCIPeriodicStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsSeconds.setStatus("mandatory")
_LinkFRDLCIPeriodicStatisticsTxCharacters_Type = Counter32
_LinkFRDLCIPeriodicStatisticsTxCharacters_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsTxCharacters = _LinkFRDLCIPeriodicStatisticsTxCharacters_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 9),
    _LinkFRDLCIPeriodicStatisticsTxCharacters_Type()
)
linkFRDLCIPeriodicStatisticsTxCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsTxCharacters.setStatus("mandatory")
_LinkFRDLCIPeriodicStatisticsRxCharacters_Type = Counter32
_LinkFRDLCIPeriodicStatisticsRxCharacters_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsRxCharacters = _LinkFRDLCIPeriodicStatisticsRxCharacters_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 10),
    _LinkFRDLCIPeriodicStatisticsRxCharacters_Type()
)
linkFRDLCIPeriodicStatisticsRxCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsRxCharacters.setStatus("mandatory")
_LinkFRDLCIPeriodicStatisticsTxFrames_Type = Counter32
_LinkFRDLCIPeriodicStatisticsTxFrames_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsTxFrames = _LinkFRDLCIPeriodicStatisticsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 11),
    _LinkFRDLCIPeriodicStatisticsTxFrames_Type()
)
linkFRDLCIPeriodicStatisticsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsTxFrames.setStatus("mandatory")
_LinkFRDLCIPeriodicStatisticsRxFrames_Type = Counter32
_LinkFRDLCIPeriodicStatisticsRxFrames_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsRxFrames = _LinkFRDLCIPeriodicStatisticsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 12),
    _LinkFRDLCIPeriodicStatisticsRxFrames_Type()
)
linkFRDLCIPeriodicStatisticsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsRxFrames.setStatus("mandatory")
_LinkFRDLCIPeriodicStatisticsTimeActive_Type = Integer32
_LinkFRDLCIPeriodicStatisticsTimeActive_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsTimeActive = _LinkFRDLCIPeriodicStatisticsTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 13),
    _LinkFRDLCIPeriodicStatisticsTimeActive_Type()
)
linkFRDLCIPeriodicStatisticsTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsTimeActive.setStatus("mandatory")
_LinkFRDLCIPeriodicStatisticsTimeCongestedForward_Type = Integer32
_LinkFRDLCIPeriodicStatisticsTimeCongestedForward_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsTimeCongestedForward = _LinkFRDLCIPeriodicStatisticsTimeCongestedForward_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 14),
    _LinkFRDLCIPeriodicStatisticsTimeCongestedForward_Type()
)
linkFRDLCIPeriodicStatisticsTimeCongestedForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsTimeCongestedForward.setStatus("mandatory")
_LinkFRDLCIPeriodicStatisticsTimeCongestedBackward_Type = Integer32
_LinkFRDLCIPeriodicStatisticsTimeCongestedBackward_Object = MibTableColumn
linkFRDLCIPeriodicStatisticsTimeCongestedBackward = _LinkFRDLCIPeriodicStatisticsTimeCongestedBackward_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 5, 1, 15),
    _LinkFRDLCIPeriodicStatisticsTimeCongestedBackward_Type()
)
linkFRDLCIPeriodicStatisticsTimeCongestedBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIPeriodicStatisticsTimeCongestedBackward.setStatus("mandatory")
_SwPeriodicStatisticsNumOfCurrentConnects_Type = Integer32
_SwPeriodicStatisticsNumOfCurrentConnects_Object = MibScalar
swPeriodicStatisticsNumOfCurrentConnects = _SwPeriodicStatisticsNumOfCurrentConnects_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 6),
    _SwPeriodicStatisticsNumOfCurrentConnects_Type()
)
swPeriodicStatisticsNumOfCurrentConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPeriodicStatisticsNumOfCurrentConnects.setStatus("mandatory")
_SwPeriodicStatisticsTable_Object = MibTable
swPeriodicStatisticsTable = _SwPeriodicStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 7)
)
if mibBuilder.loadTexts:
    swPeriodicStatisticsTable.setStatus("mandatory")
_SwPeriodicStatisticsEntry_Object = MibTableRow
swPeriodicStatisticsEntry = _SwPeriodicStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 7, 1)
)
swPeriodicStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "swPeriodicStatisticsClassNumber"),
)
if mibBuilder.loadTexts:
    swPeriodicStatisticsEntry.setStatus("mandatory")
_SwPeriodicStatisticsClassNumber_Type = Integer32
_SwPeriodicStatisticsClassNumber_Object = MibTableColumn
swPeriodicStatisticsClassNumber = _SwPeriodicStatisticsClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 7, 1, 1),
    _SwPeriodicStatisticsClassNumber_Type()
)
swPeriodicStatisticsClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPeriodicStatisticsClassNumber.setStatus("mandatory")


class _SwPeriodicStatisticsMonth_Type(Integer32):
    """Custom type swPeriodicStatisticsMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SwPeriodicStatisticsMonth_Type.__name__ = "Integer32"
_SwPeriodicStatisticsMonth_Object = MibTableColumn
swPeriodicStatisticsMonth = _SwPeriodicStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 7, 1, 2),
    _SwPeriodicStatisticsMonth_Type()
)
swPeriodicStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPeriodicStatisticsMonth.setStatus("mandatory")


class _SwPeriodicStatisticsDay_Type(Integer32):
    """Custom type swPeriodicStatisticsDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SwPeriodicStatisticsDay_Type.__name__ = "Integer32"
_SwPeriodicStatisticsDay_Object = MibTableColumn
swPeriodicStatisticsDay = _SwPeriodicStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 7, 1, 3),
    _SwPeriodicStatisticsDay_Type()
)
swPeriodicStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPeriodicStatisticsDay.setStatus("mandatory")


class _SwPeriodicStatisticsHours_Type(Integer32):
    """Custom type swPeriodicStatisticsHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SwPeriodicStatisticsHours_Type.__name__ = "Integer32"
_SwPeriodicStatisticsHours_Object = MibTableColumn
swPeriodicStatisticsHours = _SwPeriodicStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 7, 1, 4),
    _SwPeriodicStatisticsHours_Type()
)
swPeriodicStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPeriodicStatisticsHours.setStatus("mandatory")


class _SwPeriodicStatisticsMinutes_Type(Integer32):
    """Custom type swPeriodicStatisticsMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SwPeriodicStatisticsMinutes_Type.__name__ = "Integer32"
_SwPeriodicStatisticsMinutes_Object = MibTableColumn
swPeriodicStatisticsMinutes = _SwPeriodicStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 7, 1, 5),
    _SwPeriodicStatisticsMinutes_Type()
)
swPeriodicStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPeriodicStatisticsMinutes.setStatus("mandatory")


class _SwPeriodicStatisticsSeconds_Type(Integer32):
    """Custom type swPeriodicStatisticsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SwPeriodicStatisticsSeconds_Type.__name__ = "Integer32"
_SwPeriodicStatisticsSeconds_Object = MibTableColumn
swPeriodicStatisticsSeconds = _SwPeriodicStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 7, 1, 6),
    _SwPeriodicStatisticsSeconds_Type()
)
swPeriodicStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPeriodicStatisticsSeconds.setStatus("mandatory")
_SwPeriodicStatisticsNumOfSuccessfulConnects_Type = Counter32
_SwPeriodicStatisticsNumOfSuccessfulConnects_Object = MibTableColumn
swPeriodicStatisticsNumOfSuccessfulConnects = _SwPeriodicStatisticsNumOfSuccessfulConnects_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 7, 1, 7),
    _SwPeriodicStatisticsNumOfSuccessfulConnects_Type()
)
swPeriodicStatisticsNumOfSuccessfulConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPeriodicStatisticsNumOfSuccessfulConnects.setStatus("mandatory")
_SwPeriodicStatisticsNumOfUnsuccessfulAttempts_Type = Counter32
_SwPeriodicStatisticsNumOfUnsuccessfulAttempts_Object = MibTableColumn
swPeriodicStatisticsNumOfUnsuccessfulAttempts = _SwPeriodicStatisticsNumOfUnsuccessfulAttempts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 7, 1, 8),
    _SwPeriodicStatisticsNumOfUnsuccessfulAttempts_Type()
)
swPeriodicStatisticsNumOfUnsuccessfulAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPeriodicStatisticsNumOfUnsuccessfulAttempts.setStatus("mandatory")
_SwPeriodicStatisticsMaxNumInQueue_Type = Integer32
_SwPeriodicStatisticsMaxNumInQueue_Object = MibTableColumn
swPeriodicStatisticsMaxNumInQueue = _SwPeriodicStatisticsMaxNumInQueue_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 7, 1, 9),
    _SwPeriodicStatisticsMaxNumInQueue_Type()
)
swPeriodicStatisticsMaxNumInQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPeriodicStatisticsMaxNumInQueue.setStatus("mandatory")
_LinkFRAccLnkPeriodicStatisticsTable_Object = MibTable
linkFRAccLnkPeriodicStatisticsTable = _LinkFRAccLnkPeriodicStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8)
)
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsTable.setStatus("mandatory")
_LinkFRAccLnkPeriodicStatisticsEntry_Object = MibTableRow
linkFRAccLnkPeriodicStatisticsEntry = _LinkFRAccLnkPeriodicStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1)
)
linkFRAccLnkPeriodicStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "linkFRAccLnkPeriodicStatisticsCardNumber"),
    (0, "MICOM-NODE-MIB", "linkFRAccLnkPeriodicStatisticsChannelNumber"),
)
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsEntry.setStatus("mandatory")


class _LinkFRAccLnkPeriodicStatisticsCardNumber_Type(Integer32):
    """Custom type linkFRAccLnkPeriodicStatisticsCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_LinkFRAccLnkPeriodicStatisticsCardNumber_Type.__name__ = "Integer32"
_LinkFRAccLnkPeriodicStatisticsCardNumber_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsCardNumber = _LinkFRAccLnkPeriodicStatisticsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 1),
    _LinkFRAccLnkPeriodicStatisticsCardNumber_Type()
)
linkFRAccLnkPeriodicStatisticsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsCardNumber.setStatus("mandatory")
_LinkFRAccLnkPeriodicStatisticsChannelNumber_Type = Integer32
_LinkFRAccLnkPeriodicStatisticsChannelNumber_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsChannelNumber = _LinkFRAccLnkPeriodicStatisticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 2),
    _LinkFRAccLnkPeriodicStatisticsChannelNumber_Type()
)
linkFRAccLnkPeriodicStatisticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsChannelNumber.setStatus("mandatory")


class _LinkFRAccLnkPeriodicStatisticsMonth_Type(Integer32):
    """Custom type linkFRAccLnkPeriodicStatisticsMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_LinkFRAccLnkPeriodicStatisticsMonth_Type.__name__ = "Integer32"
_LinkFRAccLnkPeriodicStatisticsMonth_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsMonth = _LinkFRAccLnkPeriodicStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 3),
    _LinkFRAccLnkPeriodicStatisticsMonth_Type()
)
linkFRAccLnkPeriodicStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsMonth.setStatus("mandatory")


class _LinkFRAccLnkPeriodicStatisticsDay_Type(Integer32):
    """Custom type linkFRAccLnkPeriodicStatisticsDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_LinkFRAccLnkPeriodicStatisticsDay_Type.__name__ = "Integer32"
_LinkFRAccLnkPeriodicStatisticsDay_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsDay = _LinkFRAccLnkPeriodicStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 4),
    _LinkFRAccLnkPeriodicStatisticsDay_Type()
)
linkFRAccLnkPeriodicStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsDay.setStatus("mandatory")


class _LinkFRAccLnkPeriodicStatisticsHours_Type(Integer32):
    """Custom type linkFRAccLnkPeriodicStatisticsHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LinkFRAccLnkPeriodicStatisticsHours_Type.__name__ = "Integer32"
_LinkFRAccLnkPeriodicStatisticsHours_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsHours = _LinkFRAccLnkPeriodicStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 5),
    _LinkFRAccLnkPeriodicStatisticsHours_Type()
)
linkFRAccLnkPeriodicStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsHours.setStatus("mandatory")


class _LinkFRAccLnkPeriodicStatisticsMinutes_Type(Integer32):
    """Custom type linkFRAccLnkPeriodicStatisticsMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LinkFRAccLnkPeriodicStatisticsMinutes_Type.__name__ = "Integer32"
_LinkFRAccLnkPeriodicStatisticsMinutes_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsMinutes = _LinkFRAccLnkPeriodicStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 6),
    _LinkFRAccLnkPeriodicStatisticsMinutes_Type()
)
linkFRAccLnkPeriodicStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsMinutes.setStatus("mandatory")


class _LinkFRAccLnkPeriodicStatisticsSeconds_Type(Integer32):
    """Custom type linkFRAccLnkPeriodicStatisticsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LinkFRAccLnkPeriodicStatisticsSeconds_Type.__name__ = "Integer32"
_LinkFRAccLnkPeriodicStatisticsSeconds_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsSeconds = _LinkFRAccLnkPeriodicStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 7),
    _LinkFRAccLnkPeriodicStatisticsSeconds_Type()
)
linkFRAccLnkPeriodicStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsSeconds.setStatus("mandatory")
_LinkFRAccLnkPeriodicStatisticsLocalCompositeUtilization_Type = Gauge32
_LinkFRAccLnkPeriodicStatisticsLocalCompositeUtilization_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsLocalCompositeUtilization = _LinkFRAccLnkPeriodicStatisticsLocalCompositeUtilization_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 8),
    _LinkFRAccLnkPeriodicStatisticsLocalCompositeUtilization_Type()
)
linkFRAccLnkPeriodicStatisticsLocalCompositeUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsLocalCompositeUtilization.setStatus("mandatory")
_LinkFRAccLnkPeriodicStatisticsLocalBufferUtilization_Type = Gauge32
_LinkFRAccLnkPeriodicStatisticsLocalBufferUtilization_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsLocalBufferUtilization = _LinkFRAccLnkPeriodicStatisticsLocalBufferUtilization_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 9),
    _LinkFRAccLnkPeriodicStatisticsLocalBufferUtilization_Type()
)
linkFRAccLnkPeriodicStatisticsLocalBufferUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsLocalBufferUtilization.setStatus("mandatory")
_LinkFRAccLnkPeriodicStatisticsLocalLineAlarms_Type = Counter32
_LinkFRAccLnkPeriodicStatisticsLocalLineAlarms_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsLocalLineAlarms = _LinkFRAccLnkPeriodicStatisticsLocalLineAlarms_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 10),
    _LinkFRAccLnkPeriodicStatisticsLocalLineAlarms_Type()
)
linkFRAccLnkPeriodicStatisticsLocalLineAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsLocalLineAlarms.setStatus("mandatory")
_LinkFRAccLnkPeriodicStatisticsLocalSecInSysFlowControl_Type = Integer32
_LinkFRAccLnkPeriodicStatisticsLocalSecInSysFlowControl_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsLocalSecInSysFlowControl = _LinkFRAccLnkPeriodicStatisticsLocalSecInSysFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 11),
    _LinkFRAccLnkPeriodicStatisticsLocalSecInSysFlowControl_Type()
)
linkFRAccLnkPeriodicStatisticsLocalSecInSysFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsLocalSecInSysFlowControl.setStatus("mandatory")
_LinkFRAccLnkPeriodicStatisticsLocalSecInSyncLoss_Type = Integer32
_LinkFRAccLnkPeriodicStatisticsLocalSecInSyncLoss_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsLocalSecInSyncLoss = _LinkFRAccLnkPeriodicStatisticsLocalSecInSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 12),
    _LinkFRAccLnkPeriodicStatisticsLocalSecInSyncLoss_Type()
)
linkFRAccLnkPeriodicStatisticsLocalSecInSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsLocalSecInSyncLoss.setStatus("mandatory")
_LinkFRAccLnkPeriodicStatisticsLocalSecInCarrierLoss_Type = Integer32
_LinkFRAccLnkPeriodicStatisticsLocalSecInCarrierLoss_Object = MibTableColumn
linkFRAccLnkPeriodicStatisticsLocalSecInCarrierLoss = _LinkFRAccLnkPeriodicStatisticsLocalSecInCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 2, 8, 1, 13),
    _LinkFRAccLnkPeriodicStatisticsLocalSecInCarrierLoss_Type()
)
linkFRAccLnkPeriodicStatisticsLocalSecInCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkPeriodicStatisticsLocalSecInCarrierLoss.setStatus("mandatory")
_Statistics_accumulated_ObjectIdentity = ObjectIdentity
statistics_accumulated = _Statistics_accumulated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3)
)
_ChAccumStatisticsTable_Object = MibTable
chAccumStatisticsTable = _ChAccumStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    chAccumStatisticsTable.setStatus("mandatory")
_ChAccumStatisticsEntry_Object = MibTableRow
chAccumStatisticsEntry = _ChAccumStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 1, 1)
)
chAccumStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "chAccumStatisticsCardNumber"),
    (0, "MICOM-NODE-MIB", "chAccumStatisticsChannelNumber"),
)
if mibBuilder.loadTexts:
    chAccumStatisticsEntry.setStatus("mandatory")


class _ChAccumStatisticsCardNumber_Type(Integer32):
    """Custom type chAccumStatisticsCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ChAccumStatisticsCardNumber_Type.__name__ = "Integer32"
_ChAccumStatisticsCardNumber_Object = MibTableColumn
chAccumStatisticsCardNumber = _ChAccumStatisticsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 1, 1, 1),
    _ChAccumStatisticsCardNumber_Type()
)
chAccumStatisticsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chAccumStatisticsCardNumber.setStatus("mandatory")
_ChAccumStatisticsChannelNumber_Type = Integer32
_ChAccumStatisticsChannelNumber_Object = MibTableColumn
chAccumStatisticsChannelNumber = _ChAccumStatisticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 1, 1, 2),
    _ChAccumStatisticsChannelNumber_Type()
)
chAccumStatisticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chAccumStatisticsChannelNumber.setStatus("mandatory")


class _ChAccumStatisticsMonth_Type(Integer32):
    """Custom type chAccumStatisticsMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ChAccumStatisticsMonth_Type.__name__ = "Integer32"
_ChAccumStatisticsMonth_Object = MibTableColumn
chAccumStatisticsMonth = _ChAccumStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 1, 1, 3),
    _ChAccumStatisticsMonth_Type()
)
chAccumStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chAccumStatisticsMonth.setStatus("mandatory")


class _ChAccumStatisticsDay_Type(Integer32):
    """Custom type chAccumStatisticsDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ChAccumStatisticsDay_Type.__name__ = "Integer32"
_ChAccumStatisticsDay_Object = MibTableColumn
chAccumStatisticsDay = _ChAccumStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 1, 1, 4),
    _ChAccumStatisticsDay_Type()
)
chAccumStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chAccumStatisticsDay.setStatus("mandatory")


class _ChAccumStatisticsHours_Type(Integer32):
    """Custom type chAccumStatisticsHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_ChAccumStatisticsHours_Type.__name__ = "Integer32"
_ChAccumStatisticsHours_Object = MibTableColumn
chAccumStatisticsHours = _ChAccumStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 1, 1, 5),
    _ChAccumStatisticsHours_Type()
)
chAccumStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chAccumStatisticsHours.setStatus("mandatory")


class _ChAccumStatisticsMinutes_Type(Integer32):
    """Custom type chAccumStatisticsMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_ChAccumStatisticsMinutes_Type.__name__ = "Integer32"
_ChAccumStatisticsMinutes_Object = MibTableColumn
chAccumStatisticsMinutes = _ChAccumStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 1, 1, 6),
    _ChAccumStatisticsMinutes_Type()
)
chAccumStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chAccumStatisticsMinutes.setStatus("mandatory")


class _ChAccumStatisticsSeconds_Type(Integer32):
    """Custom type chAccumStatisticsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_ChAccumStatisticsSeconds_Type.__name__ = "Integer32"
_ChAccumStatisticsSeconds_Object = MibTableColumn
chAccumStatisticsSeconds = _ChAccumStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 1, 1, 7),
    _ChAccumStatisticsSeconds_Type()
)
chAccumStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chAccumStatisticsSeconds.setStatus("mandatory")
_ChAccumStatisticsBuffUtilization_Type = Gauge32
_ChAccumStatisticsBuffUtilization_Object = MibTableColumn
chAccumStatisticsBuffUtilization = _ChAccumStatisticsBuffUtilization_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 1, 1, 8),
    _ChAccumStatisticsBuffUtilization_Type()
)
chAccumStatisticsBuffUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chAccumStatisticsBuffUtilization.setStatus("mandatory")


class _ChAccumStatisticsChannelBusiedOut_Type(Integer32):
    """Custom type chAccumStatisticsChannelBusiedOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ChAccumStatisticsChannelBusiedOut_Type.__name__ = "Integer32"
_ChAccumStatisticsChannelBusiedOut_Object = MibTableColumn
chAccumStatisticsChannelBusiedOut = _ChAccumStatisticsChannelBusiedOut_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 1, 1, 9),
    _ChAccumStatisticsChannelBusiedOut_Type()
)
chAccumStatisticsChannelBusiedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chAccumStatisticsChannelBusiedOut.setStatus("mandatory")


class _ChAccumStatisticsChannelInFlowControl_Type(Integer32):
    """Custom type chAccumStatisticsChannelInFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ChAccumStatisticsChannelInFlowControl_Type.__name__ = "Integer32"
_ChAccumStatisticsChannelInFlowControl_Object = MibTableColumn
chAccumStatisticsChannelInFlowControl = _ChAccumStatisticsChannelInFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 1, 1, 10),
    _ChAccumStatisticsChannelInFlowControl_Type()
)
chAccumStatisticsChannelInFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chAccumStatisticsChannelInFlowControl.setStatus("mandatory")
_ChVAccumStatisticsTable_Object = MibTable
chVAccumStatisticsTable = _ChVAccumStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    chVAccumStatisticsTable.setStatus("mandatory")
_ChVAccumStatisticsEntry_Object = MibTableRow
chVAccumStatisticsEntry = _ChVAccumStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1)
)
chVAccumStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "chVAccumStatisticsCardNumber"),
    (0, "MICOM-NODE-MIB", "chVAccumStatisticsChannelNumber"),
)
if mibBuilder.loadTexts:
    chVAccumStatisticsEntry.setStatus("mandatory")


class _ChVAccumStatisticsCardNumber_Type(Integer32):
    """Custom type chVAccumStatisticsCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_ChVAccumStatisticsCardNumber_Type.__name__ = "Integer32"
_ChVAccumStatisticsCardNumber_Object = MibTableColumn
chVAccumStatisticsCardNumber = _ChVAccumStatisticsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 1),
    _ChVAccumStatisticsCardNumber_Type()
)
chVAccumStatisticsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsCardNumber.setStatus("mandatory")
_ChVAccumStatisticsChannelNumber_Type = Integer32
_ChVAccumStatisticsChannelNumber_Object = MibTableColumn
chVAccumStatisticsChannelNumber = _ChVAccumStatisticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 2),
    _ChVAccumStatisticsChannelNumber_Type()
)
chVAccumStatisticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsChannelNumber.setStatus("mandatory")


class _ChVAccumStatisticsMonth_Type(Integer32):
    """Custom type chVAccumStatisticsMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ChVAccumStatisticsMonth_Type.__name__ = "Integer32"
_ChVAccumStatisticsMonth_Object = MibTableColumn
chVAccumStatisticsMonth = _ChVAccumStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 3),
    _ChVAccumStatisticsMonth_Type()
)
chVAccumStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsMonth.setStatus("mandatory")


class _ChVAccumStatisticsDay_Type(Integer32):
    """Custom type chVAccumStatisticsDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ChVAccumStatisticsDay_Type.__name__ = "Integer32"
_ChVAccumStatisticsDay_Object = MibTableColumn
chVAccumStatisticsDay = _ChVAccumStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 4),
    _ChVAccumStatisticsDay_Type()
)
chVAccumStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsDay.setStatus("mandatory")


class _ChVAccumStatisticsHours_Type(Integer32):
    """Custom type chVAccumStatisticsHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_ChVAccumStatisticsHours_Type.__name__ = "Integer32"
_ChVAccumStatisticsHours_Object = MibTableColumn
chVAccumStatisticsHours = _ChVAccumStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 5),
    _ChVAccumStatisticsHours_Type()
)
chVAccumStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsHours.setStatus("mandatory")


class _ChVAccumStatisticsMinutes_Type(Integer32):
    """Custom type chVAccumStatisticsMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_ChVAccumStatisticsMinutes_Type.__name__ = "Integer32"
_ChVAccumStatisticsMinutes_Object = MibTableColumn
chVAccumStatisticsMinutes = _ChVAccumStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 6),
    _ChVAccumStatisticsMinutes_Type()
)
chVAccumStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsMinutes.setStatus("mandatory")


class _ChVAccumStatisticsSeconds_Type(Integer32):
    """Custom type chVAccumStatisticsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_ChVAccumStatisticsSeconds_Type.__name__ = "Integer32"
_ChVAccumStatisticsSeconds_Object = MibTableColumn
chVAccumStatisticsSeconds = _ChVAccumStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 7),
    _ChVAccumStatisticsSeconds_Type()
)
chVAccumStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsSeconds.setStatus("mandatory")
_ChVAccumStatisticsConnectTime_Type = Integer32
_ChVAccumStatisticsConnectTime_Object = MibTableColumn
chVAccumStatisticsConnectTime = _ChVAccumStatisticsConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 8),
    _ChVAccumStatisticsConnectTime_Type()
)
chVAccumStatisticsConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsConnectTime.setStatus("mandatory")
_ChVAccumStatisticsTotalCalls_Type = Counter32
_ChVAccumStatisticsTotalCalls_Object = MibTableColumn
chVAccumStatisticsTotalCalls = _ChVAccumStatisticsTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 9),
    _ChVAccumStatisticsTotalCalls_Type()
)
chVAccumStatisticsTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsTotalCalls.setStatus("mandatory")
_ChVAccumStatisticsAvgCallDuration_Type = Integer32
_ChVAccumStatisticsAvgCallDuration_Object = MibTableColumn
chVAccumStatisticsAvgCallDuration = _ChVAccumStatisticsAvgCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 10),
    _ChVAccumStatisticsAvgCallDuration_Type()
)
chVAccumStatisticsAvgCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsAvgCallDuration.setStatus("mandatory")
_ChVAccumStatisticsBusyOutTime_Type = Integer32
_ChVAccumStatisticsBusyOutTime_Object = MibTableColumn
chVAccumStatisticsBusyOutTime = _ChVAccumStatisticsBusyOutTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 11),
    _ChVAccumStatisticsBusyOutTime_Type()
)
chVAccumStatisticsBusyOutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsBusyOutTime.setStatus("mandatory")
_ChVAccumStatisticsNumOfCallAttempts_Type = Counter32
_ChVAccumStatisticsNumOfCallAttempts_Object = MibTableColumn
chVAccumStatisticsNumOfCallAttempts = _ChVAccumStatisticsNumOfCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 12),
    _ChVAccumStatisticsNumOfCallAttempts_Type()
)
chVAccumStatisticsNumOfCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsNumOfCallAttempts.setStatus("mandatory")
_ChVAccumStatisticsDiscardedFrameCounts_Type = Counter32
_ChVAccumStatisticsDiscardedFrameCounts_Object = MibTableColumn
chVAccumStatisticsDiscardedFrameCounts = _ChVAccumStatisticsDiscardedFrameCounts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 13),
    _ChVAccumStatisticsDiscardedFrameCounts_Type()
)
chVAccumStatisticsDiscardedFrameCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsDiscardedFrameCounts.setStatus("mandatory")
_ChVAccumStatisticsTimeInFaxMode_Type = Integer32
_ChVAccumStatisticsTimeInFaxMode_Object = MibTableColumn
chVAccumStatisticsTimeInFaxMode = _ChVAccumStatisticsTimeInFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 14),
    _ChVAccumStatisticsTimeInFaxMode_Type()
)
chVAccumStatisticsTimeInFaxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsTimeInFaxMode.setStatus("mandatory")
_ChVAccumStatisticsPercentInFaxMode_Type = Gauge32
_ChVAccumStatisticsPercentInFaxMode_Object = MibTableColumn
chVAccumStatisticsPercentInFaxMode = _ChVAccumStatisticsPercentInFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 2, 1, 15),
    _ChVAccumStatisticsPercentInFaxMode_Type()
)
chVAccumStatisticsPercentInFaxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVAccumStatisticsPercentInFaxMode.setStatus("mandatory")
_LinkAccumStatisticsTable_Object = MibTable
linkAccumStatisticsTable = _LinkAccumStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3)
)
if mibBuilder.loadTexts:
    linkAccumStatisticsTable.setStatus("mandatory")
_LinkAccumStatisticsEntry_Object = MibTableRow
linkAccumStatisticsEntry = _LinkAccumStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1)
)
linkAccumStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "linkAccumStatisticsCardNumber"),
    (0, "MICOM-NODE-MIB", "linkAccumStatisticsChannelNumber"),
)
if mibBuilder.loadTexts:
    linkAccumStatisticsEntry.setStatus("mandatory")


class _LinkAccumStatisticsCardNumber_Type(Integer32):
    """Custom type linkAccumStatisticsCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_LinkAccumStatisticsCardNumber_Type.__name__ = "Integer32"
_LinkAccumStatisticsCardNumber_Object = MibTableColumn
linkAccumStatisticsCardNumber = _LinkAccumStatisticsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 1),
    _LinkAccumStatisticsCardNumber_Type()
)
linkAccumStatisticsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsCardNumber.setStatus("mandatory")
_LinkAccumStatisticsChannelNumber_Type = Integer32
_LinkAccumStatisticsChannelNumber_Object = MibTableColumn
linkAccumStatisticsChannelNumber = _LinkAccumStatisticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 2),
    _LinkAccumStatisticsChannelNumber_Type()
)
linkAccumStatisticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsChannelNumber.setStatus("mandatory")


class _LinkAccumStatisticsMonth_Type(Integer32):
    """Custom type linkAccumStatisticsMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_LinkAccumStatisticsMonth_Type.__name__ = "Integer32"
_LinkAccumStatisticsMonth_Object = MibTableColumn
linkAccumStatisticsMonth = _LinkAccumStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 3),
    _LinkAccumStatisticsMonth_Type()
)
linkAccumStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsMonth.setStatus("mandatory")


class _LinkAccumStatisticsDay_Type(Integer32):
    """Custom type linkAccumStatisticsDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_LinkAccumStatisticsDay_Type.__name__ = "Integer32"
_LinkAccumStatisticsDay_Object = MibTableColumn
linkAccumStatisticsDay = _LinkAccumStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 4),
    _LinkAccumStatisticsDay_Type()
)
linkAccumStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsDay.setStatus("mandatory")


class _LinkAccumStatisticsHours_Type(Integer32):
    """Custom type linkAccumStatisticsHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LinkAccumStatisticsHours_Type.__name__ = "Integer32"
_LinkAccumStatisticsHours_Object = MibTableColumn
linkAccumStatisticsHours = _LinkAccumStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 5),
    _LinkAccumStatisticsHours_Type()
)
linkAccumStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsHours.setStatus("mandatory")


class _LinkAccumStatisticsMinutes_Type(Integer32):
    """Custom type linkAccumStatisticsMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LinkAccumStatisticsMinutes_Type.__name__ = "Integer32"
_LinkAccumStatisticsMinutes_Object = MibTableColumn
linkAccumStatisticsMinutes = _LinkAccumStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 6),
    _LinkAccumStatisticsMinutes_Type()
)
linkAccumStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsMinutes.setStatus("mandatory")


class _LinkAccumStatisticsSeconds_Type(Integer32):
    """Custom type linkAccumStatisticsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LinkAccumStatisticsSeconds_Type.__name__ = "Integer32"
_LinkAccumStatisticsSeconds_Object = MibTableColumn
linkAccumStatisticsSeconds = _LinkAccumStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 7),
    _LinkAccumStatisticsSeconds_Type()
)
linkAccumStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsSeconds.setStatus("mandatory")


class _LinkAccumStatisticsLinkType_Type(Integer32):
    """Custom type linkAccumStatisticsLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("esi", 2),
          ("esiSecondary", 5),
          ("esm", 1),
          ("frameRelay", 6),
          ("localEsi", 4),
          ("xDot21", 3))
    )


_LinkAccumStatisticsLinkType_Type.__name__ = "Integer32"
_LinkAccumStatisticsLinkType_Object = MibTableColumn
linkAccumStatisticsLinkType = _LinkAccumStatisticsLinkType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 8),
    _LinkAccumStatisticsLinkType_Type()
)
linkAccumStatisticsLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsLinkType.setStatus("mandatory")
_LinkAccumStatisticsTxFrames_Type = Counter32
_LinkAccumStatisticsTxFrames_Object = MibTableColumn
linkAccumStatisticsTxFrames = _LinkAccumStatisticsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 9),
    _LinkAccumStatisticsTxFrames_Type()
)
linkAccumStatisticsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsTxFrames.setStatus("mandatory")
_LinkAccumStatisticsRxFrames_Type = Counter32
_LinkAccumStatisticsRxFrames_Object = MibTableColumn
linkAccumStatisticsRxFrames = _LinkAccumStatisticsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 10),
    _LinkAccumStatisticsRxFrames_Type()
)
linkAccumStatisticsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsRxFrames.setStatus("mandatory")
_LinkAccumStatisticsLocCompositeUtil_Type = Gauge32
_LinkAccumStatisticsLocCompositeUtil_Object = MibTableColumn
linkAccumStatisticsLocCompositeUtil = _LinkAccumStatisticsLocCompositeUtil_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 11),
    _LinkAccumStatisticsLocCompositeUtil_Type()
)
linkAccumStatisticsLocCompositeUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsLocCompositeUtil.setStatus("mandatory")
_LinkAccumStatisticsRemCompositeUtil_Type = Gauge32
_LinkAccumStatisticsRemCompositeUtil_Object = MibTableColumn
linkAccumStatisticsRemCompositeUtil = _LinkAccumStatisticsRemCompositeUtil_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 12),
    _LinkAccumStatisticsRemCompositeUtil_Type()
)
linkAccumStatisticsRemCompositeUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsRemCompositeUtil.setStatus("mandatory")
_LinkAccumStatisticsLocBufferUtil_Type = Gauge32
_LinkAccumStatisticsLocBufferUtil_Object = MibTableColumn
linkAccumStatisticsLocBufferUtil = _LinkAccumStatisticsLocBufferUtil_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 13),
    _LinkAccumStatisticsLocBufferUtil_Type()
)
linkAccumStatisticsLocBufferUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsLocBufferUtil.setStatus("mandatory")
_LinkAccumStatisticsRemBufferUtil_Type = Gauge32
_LinkAccumStatisticsRemBufferUtil_Object = MibTableColumn
linkAccumStatisticsRemBufferUtil = _LinkAccumStatisticsRemBufferUtil_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 14),
    _LinkAccumStatisticsRemBufferUtil_Type()
)
linkAccumStatisticsRemBufferUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsRemBufferUtil.setStatus("mandatory")
_LinkAccumStatisticsLocRetransmits_Type = Counter32
_LinkAccumStatisticsLocRetransmits_Object = MibTableColumn
linkAccumStatisticsLocRetransmits = _LinkAccumStatisticsLocRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 15),
    _LinkAccumStatisticsLocRetransmits_Type()
)
linkAccumStatisticsLocRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsLocRetransmits.setStatus("mandatory")
_LinkAccumStatisticsRemRetransmits_Type = Counter32
_LinkAccumStatisticsRemRetransmits_Object = MibTableColumn
linkAccumStatisticsRemRetransmits = _LinkAccumStatisticsRemRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 16),
    _LinkAccumStatisticsRemRetransmits_Type()
)
linkAccumStatisticsRemRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsRemRetransmits.setStatus("mandatory")
_LinkAccumStatisticsLocLineAlarms_Type = Integer32
_LinkAccumStatisticsLocLineAlarms_Object = MibTableColumn
linkAccumStatisticsLocLineAlarms = _LinkAccumStatisticsLocLineAlarms_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 17),
    _LinkAccumStatisticsLocLineAlarms_Type()
)
linkAccumStatisticsLocLineAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsLocLineAlarms.setStatus("mandatory")
_LinkAccumStatisticsRemLineAlarms_Type = Integer32
_LinkAccumStatisticsRemLineAlarms_Object = MibTableColumn
linkAccumStatisticsRemLineAlarms = _LinkAccumStatisticsRemLineAlarms_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 18),
    _LinkAccumStatisticsRemLineAlarms_Type()
)
linkAccumStatisticsRemLineAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsRemLineAlarms.setStatus("mandatory")
_LinkAccumStatisticsLocTimeInSysFlowCtrl_Type = Integer32
_LinkAccumStatisticsLocTimeInSysFlowCtrl_Object = MibTableColumn
linkAccumStatisticsLocTimeInSysFlowCtrl = _LinkAccumStatisticsLocTimeInSysFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 19),
    _LinkAccumStatisticsLocTimeInSysFlowCtrl_Type()
)
linkAccumStatisticsLocTimeInSysFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsLocTimeInSysFlowCtrl.setStatus("mandatory")
_LinkAccumStatisticsRemTimeInSysFlowCtrl_Type = Integer32
_LinkAccumStatisticsRemTimeInSysFlowCtrl_Object = MibTableColumn
linkAccumStatisticsRemTimeInSysFlowCtrl = _LinkAccumStatisticsRemTimeInSysFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 20),
    _LinkAccumStatisticsRemTimeInSysFlowCtrl_Type()
)
linkAccumStatisticsRemTimeInSysFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsRemTimeInSysFlowCtrl.setStatus("mandatory")
_LinkAccumStatisticsLocTimeInSyncLossOrX21Connect_Type = Integer32
_LinkAccumStatisticsLocTimeInSyncLossOrX21Connect_Object = MibTableColumn
linkAccumStatisticsLocTimeInSyncLossOrX21Connect = _LinkAccumStatisticsLocTimeInSyncLossOrX21Connect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 21),
    _LinkAccumStatisticsLocTimeInSyncLossOrX21Connect_Type()
)
linkAccumStatisticsLocTimeInSyncLossOrX21Connect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsLocTimeInSyncLossOrX21Connect.setStatus("mandatory")
_LinkAccumStatisticsRemTimeInSyncLoss_Type = Integer32
_LinkAccumStatisticsRemTimeInSyncLoss_Object = MibTableColumn
linkAccumStatisticsRemTimeInSyncLoss = _LinkAccumStatisticsRemTimeInSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 22),
    _LinkAccumStatisticsRemTimeInSyncLoss_Type()
)
linkAccumStatisticsRemTimeInSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsRemTimeInSyncLoss.setStatus("mandatory")
_LinkAccumStatisticsLocTimeInCarrierLoss_Type = Integer32
_LinkAccumStatisticsLocTimeInCarrierLoss_Object = MibTableColumn
linkAccumStatisticsLocTimeInCarrierLoss = _LinkAccumStatisticsLocTimeInCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 23),
    _LinkAccumStatisticsLocTimeInCarrierLoss_Type()
)
linkAccumStatisticsLocTimeInCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsLocTimeInCarrierLoss.setStatus("mandatory")
_LinkAccumStatisticsRemTimeInCarrierLoss_Type = Integer32
_LinkAccumStatisticsRemTimeInCarrierLoss_Object = MibTableColumn
linkAccumStatisticsRemTimeInCarrierLoss = _LinkAccumStatisticsRemTimeInCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 3, 1, 24),
    _LinkAccumStatisticsRemTimeInCarrierLoss_Type()
)
linkAccumStatisticsRemTimeInCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAccumStatisticsRemTimeInCarrierLoss.setStatus("mandatory")
_LinkFRAccumStatisticsTable_Object = MibTable
linkFRAccumStatisticsTable = _LinkFRAccumStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4)
)
if mibBuilder.loadTexts:
    linkFRAccumStatisticsTable.setStatus("mandatory")
_LinkFRAccumStatisticsEntry_Object = MibTableRow
linkFRAccumStatisticsEntry = _LinkFRAccumStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1)
)
linkFRAccumStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "linkFRAccumStatisticsCardNumber"),
    (0, "MICOM-NODE-MIB", "linkFRAccumStatisticsChannelNumber"),
)
if mibBuilder.loadTexts:
    linkFRAccumStatisticsEntry.setStatus("mandatory")


class _LinkFRAccumStatisticsCardNumber_Type(Integer32):
    """Custom type linkFRAccumStatisticsCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_LinkFRAccumStatisticsCardNumber_Type.__name__ = "Integer32"
_LinkFRAccumStatisticsCardNumber_Object = MibTableColumn
linkFRAccumStatisticsCardNumber = _LinkFRAccumStatisticsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 1),
    _LinkFRAccumStatisticsCardNumber_Type()
)
linkFRAccumStatisticsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsCardNumber.setStatus("mandatory")
_LinkFRAccumStatisticsChannelNumber_Type = Integer32
_LinkFRAccumStatisticsChannelNumber_Object = MibTableColumn
linkFRAccumStatisticsChannelNumber = _LinkFRAccumStatisticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 2),
    _LinkFRAccumStatisticsChannelNumber_Type()
)
linkFRAccumStatisticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsChannelNumber.setStatus("mandatory")
_LinkFRAccumStatisticsMonth_Type = Integer32
_LinkFRAccumStatisticsMonth_Object = MibTableColumn
linkFRAccumStatisticsMonth = _LinkFRAccumStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 3),
    _LinkFRAccumStatisticsMonth_Type()
)
linkFRAccumStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsMonth.setStatus("mandatory")
_LinkFRAccumStatisticsDay_Type = Integer32
_LinkFRAccumStatisticsDay_Object = MibTableColumn
linkFRAccumStatisticsDay = _LinkFRAccumStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 4),
    _LinkFRAccumStatisticsDay_Type()
)
linkFRAccumStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsDay.setStatus("mandatory")
_LinkFRAccumStatisticsHours_Type = Integer32
_LinkFRAccumStatisticsHours_Object = MibTableColumn
linkFRAccumStatisticsHours = _LinkFRAccumStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 5),
    _LinkFRAccumStatisticsHours_Type()
)
linkFRAccumStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsHours.setStatus("mandatory")
_LinkFRAccumStatisticsMinutes_Type = Integer32
_LinkFRAccumStatisticsMinutes_Object = MibTableColumn
linkFRAccumStatisticsMinutes = _LinkFRAccumStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 6),
    _LinkFRAccumStatisticsMinutes_Type()
)
linkFRAccumStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsMinutes.setStatus("mandatory")
_LinkFRAccumStatisticsSeconds_Type = Integer32
_LinkFRAccumStatisticsSeconds_Object = MibTableColumn
linkFRAccumStatisticsSeconds = _LinkFRAccumStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 7),
    _LinkFRAccumStatisticsSeconds_Type()
)
linkFRAccumStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsSeconds.setStatus("mandatory")
_LinkFRAccumStatisticsCRCErrs_Type = Counter32
_LinkFRAccumStatisticsCRCErrs_Object = MibTableColumn
linkFRAccumStatisticsCRCErrs = _LinkFRAccumStatisticsCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 8),
    _LinkFRAccumStatisticsCRCErrs_Type()
)
linkFRAccumStatisticsCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsCRCErrs.setStatus("mandatory")
_LinkFRAccumStatisticsLostStatusMsgCounts_Type = Counter32
_LinkFRAccumStatisticsLostStatusMsgCounts_Object = MibTableColumn
linkFRAccumStatisticsLostStatusMsgCounts = _LinkFRAccumStatisticsLostStatusMsgCounts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 9),
    _LinkFRAccumStatisticsLostStatusMsgCounts_Type()
)
linkFRAccumStatisticsLostStatusMsgCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsLostStatusMsgCounts.setStatus("mandatory")
_LinkFRAccumStatisticsStatusMsgProtocolErrs_Type = Counter32
_LinkFRAccumStatisticsStatusMsgProtocolErrs_Object = MibTableColumn
linkFRAccumStatisticsStatusMsgProtocolErrs = _LinkFRAccumStatisticsStatusMsgProtocolErrs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 10),
    _LinkFRAccumStatisticsStatusMsgProtocolErrs_Type()
)
linkFRAccumStatisticsStatusMsgProtocolErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsStatusMsgProtocolErrs.setStatus("mandatory")
_LinkFRAccumStatisticsNetworkResets_Type = Counter32
_LinkFRAccumStatisticsNetworkResets_Object = MibTableColumn
linkFRAccumStatisticsNetworkResets = _LinkFRAccumStatisticsNetworkResets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 11),
    _LinkFRAccumStatisticsNetworkResets_Type()
)
linkFRAccumStatisticsNetworkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsNetworkResets.setStatus("mandatory")
_LinkFRAccumStatisticsLinkResets_Type = Counter32
_LinkFRAccumStatisticsLinkResets_Object = MibTableColumn
linkFRAccumStatisticsLinkResets = _LinkFRAccumStatisticsLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 12),
    _LinkFRAccumStatisticsLinkResets_Type()
)
linkFRAccumStatisticsLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsLinkResets.setStatus("mandatory")
_LinkFRAccumStatisticsNumOfDLCIs_Type = Integer32
_LinkFRAccumStatisticsNumOfDLCIs_Object = MibTableColumn
linkFRAccumStatisticsNumOfDLCIs = _LinkFRAccumStatisticsNumOfDLCIs_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 4, 1, 13),
    _LinkFRAccumStatisticsNumOfDLCIs_Type()
)
linkFRAccumStatisticsNumOfDLCIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccumStatisticsNumOfDLCIs.setStatus("mandatory")
_LinkFRDLCIAccumStatisticsTable_Object = MibTable
linkFRDLCIAccumStatisticsTable = _LinkFRDLCIAccumStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5)
)
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsTable.setStatus("mandatory")
_LinkFRDLCIAccumStatisticsEntry_Object = MibTableRow
linkFRDLCIAccumStatisticsEntry = _LinkFRDLCIAccumStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1)
)
linkFRDLCIAccumStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "linkFRDLCIAccumStatisticsCardNumber"),
    (0, "MICOM-NODE-MIB", "linkFRDLCIAccumStatisticsChannelNumber"),
    (0, "MICOM-NODE-MIB", "linkFRDLCIAccumStatisticsDLCINumber"),
)
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsEntry.setStatus("mandatory")


class _LinkFRDLCIAccumStatisticsCardNumber_Type(Integer32):
    """Custom type linkFRDLCIAccumStatisticsCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_LinkFRDLCIAccumStatisticsCardNumber_Type.__name__ = "Integer32"
_LinkFRDLCIAccumStatisticsCardNumber_Object = MibTableColumn
linkFRDLCIAccumStatisticsCardNumber = _LinkFRDLCIAccumStatisticsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 1),
    _LinkFRDLCIAccumStatisticsCardNumber_Type()
)
linkFRDLCIAccumStatisticsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsCardNumber.setStatus("mandatory")
_LinkFRDLCIAccumStatisticsChannelNumber_Type = Integer32
_LinkFRDLCIAccumStatisticsChannelNumber_Object = MibTableColumn
linkFRDLCIAccumStatisticsChannelNumber = _LinkFRDLCIAccumStatisticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 2),
    _LinkFRDLCIAccumStatisticsChannelNumber_Type()
)
linkFRDLCIAccumStatisticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsChannelNumber.setStatus("mandatory")
_LinkFRDLCIAccumStatisticsDLCINumber_Type = Integer32
_LinkFRDLCIAccumStatisticsDLCINumber_Object = MibTableColumn
linkFRDLCIAccumStatisticsDLCINumber = _LinkFRDLCIAccumStatisticsDLCINumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 3),
    _LinkFRDLCIAccumStatisticsDLCINumber_Type()
)
linkFRDLCIAccumStatisticsDLCINumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsDLCINumber.setStatus("mandatory")


class _LinkFRDLCIAccumStatisticsMonth_Type(Integer32):
    """Custom type linkFRDLCIAccumStatisticsMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_LinkFRDLCIAccumStatisticsMonth_Type.__name__ = "Integer32"
_LinkFRDLCIAccumStatisticsMonth_Object = MibTableColumn
linkFRDLCIAccumStatisticsMonth = _LinkFRDLCIAccumStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 4),
    _LinkFRDLCIAccumStatisticsMonth_Type()
)
linkFRDLCIAccumStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsMonth.setStatus("mandatory")


class _LinkFRDLCIAccumStatisticsDay_Type(Integer32):
    """Custom type linkFRDLCIAccumStatisticsDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_LinkFRDLCIAccumStatisticsDay_Type.__name__ = "Integer32"
_LinkFRDLCIAccumStatisticsDay_Object = MibTableColumn
linkFRDLCIAccumStatisticsDay = _LinkFRDLCIAccumStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 5),
    _LinkFRDLCIAccumStatisticsDay_Type()
)
linkFRDLCIAccumStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsDay.setStatus("mandatory")


class _LinkFRDLCIAccumStatisticsHours_Type(Integer32):
    """Custom type linkFRDLCIAccumStatisticsHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LinkFRDLCIAccumStatisticsHours_Type.__name__ = "Integer32"
_LinkFRDLCIAccumStatisticsHours_Object = MibTableColumn
linkFRDLCIAccumStatisticsHours = _LinkFRDLCIAccumStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 6),
    _LinkFRDLCIAccumStatisticsHours_Type()
)
linkFRDLCIAccumStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsHours.setStatus("mandatory")


class _LinkFRDLCIAccumStatisticsMinutes_Type(Integer32):
    """Custom type linkFRDLCIAccumStatisticsMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LinkFRDLCIAccumStatisticsMinutes_Type.__name__ = "Integer32"
_LinkFRDLCIAccumStatisticsMinutes_Object = MibTableColumn
linkFRDLCIAccumStatisticsMinutes = _LinkFRDLCIAccumStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 7),
    _LinkFRDLCIAccumStatisticsMinutes_Type()
)
linkFRDLCIAccumStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsMinutes.setStatus("mandatory")


class _LinkFRDLCIAccumStatisticsSeconds_Type(Integer32):
    """Custom type linkFRDLCIAccumStatisticsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LinkFRDLCIAccumStatisticsSeconds_Type.__name__ = "Integer32"
_LinkFRDLCIAccumStatisticsSeconds_Object = MibTableColumn
linkFRDLCIAccumStatisticsSeconds = _LinkFRDLCIAccumStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 8),
    _LinkFRDLCIAccumStatisticsSeconds_Type()
)
linkFRDLCIAccumStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsSeconds.setStatus("mandatory")
_LinkFRDLCIAccumStatisticsTxCharacters_Type = Counter32
_LinkFRDLCIAccumStatisticsTxCharacters_Object = MibTableColumn
linkFRDLCIAccumStatisticsTxCharacters = _LinkFRDLCIAccumStatisticsTxCharacters_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 9),
    _LinkFRDLCIAccumStatisticsTxCharacters_Type()
)
linkFRDLCIAccumStatisticsTxCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsTxCharacters.setStatus("mandatory")
_LinkFRDLCIAccumStatisticsRxCharacters_Type = Counter32
_LinkFRDLCIAccumStatisticsRxCharacters_Object = MibTableColumn
linkFRDLCIAccumStatisticsRxCharacters = _LinkFRDLCIAccumStatisticsRxCharacters_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 10),
    _LinkFRDLCIAccumStatisticsRxCharacters_Type()
)
linkFRDLCIAccumStatisticsRxCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsRxCharacters.setStatus("mandatory")
_LinkFRDLCIAccumStatisticsTxFrames_Type = Counter32
_LinkFRDLCIAccumStatisticsTxFrames_Object = MibTableColumn
linkFRDLCIAccumStatisticsTxFrames = _LinkFRDLCIAccumStatisticsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 11),
    _LinkFRDLCIAccumStatisticsTxFrames_Type()
)
linkFRDLCIAccumStatisticsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsTxFrames.setStatus("mandatory")
_LinkFRDLCIAccumStatisticsRxFrames_Type = Counter32
_LinkFRDLCIAccumStatisticsRxFrames_Object = MibTableColumn
linkFRDLCIAccumStatisticsRxFrames = _LinkFRDLCIAccumStatisticsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 12),
    _LinkFRDLCIAccumStatisticsRxFrames_Type()
)
linkFRDLCIAccumStatisticsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsRxFrames.setStatus("mandatory")
_LinkFRDLCIAccumStatisticsTimeActive_Type = Integer32
_LinkFRDLCIAccumStatisticsTimeActive_Object = MibTableColumn
linkFRDLCIAccumStatisticsTimeActive = _LinkFRDLCIAccumStatisticsTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 13),
    _LinkFRDLCIAccumStatisticsTimeActive_Type()
)
linkFRDLCIAccumStatisticsTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsTimeActive.setStatus("mandatory")
_LinkFRDLCIAccumStatisticsTimeCongestedForward_Type = Integer32
_LinkFRDLCIAccumStatisticsTimeCongestedForward_Object = MibTableColumn
linkFRDLCIAccumStatisticsTimeCongestedForward = _LinkFRDLCIAccumStatisticsTimeCongestedForward_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 14),
    _LinkFRDLCIAccumStatisticsTimeCongestedForward_Type()
)
linkFRDLCIAccumStatisticsTimeCongestedForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsTimeCongestedForward.setStatus("mandatory")
_LinkFRDLCIAccumStatisticsTimeCongestedBackward_Type = Integer32
_LinkFRDLCIAccumStatisticsTimeCongestedBackward_Object = MibTableColumn
linkFRDLCIAccumStatisticsTimeCongestedBackward = _LinkFRDLCIAccumStatisticsTimeCongestedBackward_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 5, 1, 15),
    _LinkFRDLCIAccumStatisticsTimeCongestedBackward_Type()
)
linkFRDLCIAccumStatisticsTimeCongestedBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRDLCIAccumStatisticsTimeCongestedBackward.setStatus("mandatory")
_SwAccumStatisticsNumOfCurrentConnects_Type = Counter32
_SwAccumStatisticsNumOfCurrentConnects_Object = MibTableColumn
swAccumStatisticsNumOfCurrentConnects = _SwAccumStatisticsNumOfCurrentConnects_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 6),
    _SwAccumStatisticsNumOfCurrentConnects_Type()
)
swAccumStatisticsNumOfCurrentConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAccumStatisticsNumOfCurrentConnects.setStatus("mandatory")
_SwAccumStatisticsTable_Object = MibTable
swAccumStatisticsTable = _SwAccumStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 7)
)
if mibBuilder.loadTexts:
    swAccumStatisticsTable.setStatus("mandatory")
_SwAccumStatisticsEntry_Object = MibTableRow
swAccumStatisticsEntry = _SwAccumStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 7, 1)
)
swAccumStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "swAccumStatisticsClassNumber"),
)
if mibBuilder.loadTexts:
    swAccumStatisticsEntry.setStatus("mandatory")
_SwAccumStatisticsClassNumber_Type = Integer32
_SwAccumStatisticsClassNumber_Object = MibTableColumn
swAccumStatisticsClassNumber = _SwAccumStatisticsClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 7, 1, 1),
    _SwAccumStatisticsClassNumber_Type()
)
swAccumStatisticsClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAccumStatisticsClassNumber.setStatus("mandatory")


class _SwAccumStatisticsMonth_Type(Integer32):
    """Custom type swAccumStatisticsMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SwAccumStatisticsMonth_Type.__name__ = "Integer32"
_SwAccumStatisticsMonth_Object = MibTableColumn
swAccumStatisticsMonth = _SwAccumStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 7, 1, 2),
    _SwAccumStatisticsMonth_Type()
)
swAccumStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAccumStatisticsMonth.setStatus("mandatory")


class _SwAccumStatisticsDay_Type(Integer32):
    """Custom type swAccumStatisticsDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SwAccumStatisticsDay_Type.__name__ = "Integer32"
_SwAccumStatisticsDay_Object = MibTableColumn
swAccumStatisticsDay = _SwAccumStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 7, 1, 3),
    _SwAccumStatisticsDay_Type()
)
swAccumStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAccumStatisticsDay.setStatus("mandatory")


class _SwAccumStatisticsHours_Type(Integer32):
    """Custom type swAccumStatisticsHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SwAccumStatisticsHours_Type.__name__ = "Integer32"
_SwAccumStatisticsHours_Object = MibTableColumn
swAccumStatisticsHours = _SwAccumStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 7, 1, 4),
    _SwAccumStatisticsHours_Type()
)
swAccumStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAccumStatisticsHours.setStatus("mandatory")


class _SwAccumStatisticsMinutes_Type(Integer32):
    """Custom type swAccumStatisticsMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SwAccumStatisticsMinutes_Type.__name__ = "Integer32"
_SwAccumStatisticsMinutes_Object = MibTableColumn
swAccumStatisticsMinutes = _SwAccumStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 7, 1, 5),
    _SwAccumStatisticsMinutes_Type()
)
swAccumStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAccumStatisticsMinutes.setStatus("mandatory")


class _SwAccumStatisticsSeconds_Type(Integer32):
    """Custom type swAccumStatisticsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SwAccumStatisticsSeconds_Type.__name__ = "Integer32"
_SwAccumStatisticsSeconds_Object = MibTableColumn
swAccumStatisticsSeconds = _SwAccumStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 7, 1, 6),
    _SwAccumStatisticsSeconds_Type()
)
swAccumStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAccumStatisticsSeconds.setStatus("mandatory")
_SwAccumStatisticsNumOfSuccessfulConnects_Type = Counter32
_SwAccumStatisticsNumOfSuccessfulConnects_Object = MibTableColumn
swAccumStatisticsNumOfSuccessfulConnects = _SwAccumStatisticsNumOfSuccessfulConnects_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 7, 1, 7),
    _SwAccumStatisticsNumOfSuccessfulConnects_Type()
)
swAccumStatisticsNumOfSuccessfulConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAccumStatisticsNumOfSuccessfulConnects.setStatus("mandatory")
_SwAccumStatisticsNumOfUnsuccessfulAttempts_Type = Counter32
_SwAccumStatisticsNumOfUnsuccessfulAttempts_Object = MibTableColumn
swAccumStatisticsNumOfUnsuccessfulAttempts = _SwAccumStatisticsNumOfUnsuccessfulAttempts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 7, 1, 8),
    _SwAccumStatisticsNumOfUnsuccessfulAttempts_Type()
)
swAccumStatisticsNumOfUnsuccessfulAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAccumStatisticsNumOfUnsuccessfulAttempts.setStatus("mandatory")
_SwAccumStatisticsMaxNumInQueue_Type = Integer32
_SwAccumStatisticsMaxNumInQueue_Object = MibTableColumn
swAccumStatisticsMaxNumInQueue = _SwAccumStatisticsMaxNumInQueue_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 7, 1, 9),
    _SwAccumStatisticsMaxNumInQueue_Type()
)
swAccumStatisticsMaxNumInQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAccumStatisticsMaxNumInQueue.setStatus("mandatory")
_LinkFRAccLnkAccumStatisticsTable_Object = MibTable
linkFRAccLnkAccumStatisticsTable = _LinkFRAccLnkAccumStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8)
)
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsTable.setStatus("mandatory")
_LinkFRAccLnkAccumStatisticsEntry_Object = MibTableRow
linkFRAccLnkAccumStatisticsEntry = _LinkFRAccLnkAccumStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1)
)
linkFRAccLnkAccumStatisticsEntry.setIndexNames(
    (0, "MICOM-NODE-MIB", "linkFRAccLnkAccumStatisticsCardNumber"),
    (0, "MICOM-NODE-MIB", "linkFRAccLnkAccumStatisticsChannelNumber"),
)
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsEntry.setStatus("mandatory")


class _LinkFRAccLnkAccumStatisticsCardNumber_Type(Integer32):
    """Custom type linkFRAccLnkAccumStatisticsCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_LinkFRAccLnkAccumStatisticsCardNumber_Type.__name__ = "Integer32"
_LinkFRAccLnkAccumStatisticsCardNumber_Object = MibTableColumn
linkFRAccLnkAccumStatisticsCardNumber = _LinkFRAccLnkAccumStatisticsCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 1),
    _LinkFRAccLnkAccumStatisticsCardNumber_Type()
)
linkFRAccLnkAccumStatisticsCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsCardNumber.setStatus("mandatory")
_LinkFRAccLnkAccumStatisticsChannelNumber_Type = Integer32
_LinkFRAccLnkAccumStatisticsChannelNumber_Object = MibTableColumn
linkFRAccLnkAccumStatisticsChannelNumber = _LinkFRAccLnkAccumStatisticsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 2),
    _LinkFRAccLnkAccumStatisticsChannelNumber_Type()
)
linkFRAccLnkAccumStatisticsChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsChannelNumber.setStatus("mandatory")


class _LinkFRAccLnkAccumStatisticsMonth_Type(Integer32):
    """Custom type linkFRAccLnkAccumStatisticsMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_LinkFRAccLnkAccumStatisticsMonth_Type.__name__ = "Integer32"
_LinkFRAccLnkAccumStatisticsMonth_Object = MibTableColumn
linkFRAccLnkAccumStatisticsMonth = _LinkFRAccLnkAccumStatisticsMonth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 3),
    _LinkFRAccLnkAccumStatisticsMonth_Type()
)
linkFRAccLnkAccumStatisticsMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsMonth.setStatus("mandatory")


class _LinkFRAccLnkAccumStatisticsDay_Type(Integer32):
    """Custom type linkFRAccLnkAccumStatisticsDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_LinkFRAccLnkAccumStatisticsDay_Type.__name__ = "Integer32"
_LinkFRAccLnkAccumStatisticsDay_Object = MibTableColumn
linkFRAccLnkAccumStatisticsDay = _LinkFRAccLnkAccumStatisticsDay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 4),
    _LinkFRAccLnkAccumStatisticsDay_Type()
)
linkFRAccLnkAccumStatisticsDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsDay.setStatus("mandatory")


class _LinkFRAccLnkAccumStatisticsHours_Type(Integer32):
    """Custom type linkFRAccLnkAccumStatisticsHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LinkFRAccLnkAccumStatisticsHours_Type.__name__ = "Integer32"
_LinkFRAccLnkAccumStatisticsHours_Object = MibTableColumn
linkFRAccLnkAccumStatisticsHours = _LinkFRAccLnkAccumStatisticsHours_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 5),
    _LinkFRAccLnkAccumStatisticsHours_Type()
)
linkFRAccLnkAccumStatisticsHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsHours.setStatus("mandatory")


class _LinkFRAccLnkAccumStatisticsMinutes_Type(Integer32):
    """Custom type linkFRAccLnkAccumStatisticsMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LinkFRAccLnkAccumStatisticsMinutes_Type.__name__ = "Integer32"
_LinkFRAccLnkAccumStatisticsMinutes_Object = MibTableColumn
linkFRAccLnkAccumStatisticsMinutes = _LinkFRAccLnkAccumStatisticsMinutes_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 6),
    _LinkFRAccLnkAccumStatisticsMinutes_Type()
)
linkFRAccLnkAccumStatisticsMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsMinutes.setStatus("mandatory")


class _LinkFRAccLnkAccumStatisticsSeconds_Type(Integer32):
    """Custom type linkFRAccLnkAccumStatisticsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LinkFRAccLnkAccumStatisticsSeconds_Type.__name__ = "Integer32"
_LinkFRAccLnkAccumStatisticsSeconds_Object = MibTableColumn
linkFRAccLnkAccumStatisticsSeconds = _LinkFRAccLnkAccumStatisticsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 7),
    _LinkFRAccLnkAccumStatisticsSeconds_Type()
)
linkFRAccLnkAccumStatisticsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsSeconds.setStatus("mandatory")
_LinkFRAccLnkAccumStatisticsLocalCompositeUtilization_Type = Gauge32
_LinkFRAccLnkAccumStatisticsLocalCompositeUtilization_Object = MibTableColumn
linkFRAccLnkAccumStatisticsLocalCompositeUtilization = _LinkFRAccLnkAccumStatisticsLocalCompositeUtilization_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 8),
    _LinkFRAccLnkAccumStatisticsLocalCompositeUtilization_Type()
)
linkFRAccLnkAccumStatisticsLocalCompositeUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsLocalCompositeUtilization.setStatus("mandatory")
_LinkFRAccLnkAccumStatisticsLocalBufferUtilization_Type = Gauge32
_LinkFRAccLnkAccumStatisticsLocalBufferUtilization_Object = MibTableColumn
linkFRAccLnkAccumStatisticsLocalBufferUtilization = _LinkFRAccLnkAccumStatisticsLocalBufferUtilization_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 9),
    _LinkFRAccLnkAccumStatisticsLocalBufferUtilization_Type()
)
linkFRAccLnkAccumStatisticsLocalBufferUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsLocalBufferUtilization.setStatus("mandatory")
_LinkFRAccLnkAccumStatisticsLocalLineAlarms_Type = Counter32
_LinkFRAccLnkAccumStatisticsLocalLineAlarms_Object = MibTableColumn
linkFRAccLnkAccumStatisticsLocalLineAlarms = _LinkFRAccLnkAccumStatisticsLocalLineAlarms_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 10),
    _LinkFRAccLnkAccumStatisticsLocalLineAlarms_Type()
)
linkFRAccLnkAccumStatisticsLocalLineAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsLocalLineAlarms.setStatus("mandatory")
_LinkFRAccLnkAccumStatisticsLocalSecInSysFlowControl_Type = Integer32
_LinkFRAccLnkAccumStatisticsLocalSecInSysFlowControl_Object = MibTableColumn
linkFRAccLnkAccumStatisticsLocalSecInSysFlowControl = _LinkFRAccLnkAccumStatisticsLocalSecInSysFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 11),
    _LinkFRAccLnkAccumStatisticsLocalSecInSysFlowControl_Type()
)
linkFRAccLnkAccumStatisticsLocalSecInSysFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsLocalSecInSysFlowControl.setStatus("mandatory")
_LinkFRAccLnkAccumStatisticsLocalSecInSyncLoss_Type = Integer32
_LinkFRAccLnkAccumStatisticsLocalSecInSyncLoss_Object = MibTableColumn
linkFRAccLnkAccumStatisticsLocalSecInSyncLoss = _LinkFRAccLnkAccumStatisticsLocalSecInSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 12),
    _LinkFRAccLnkAccumStatisticsLocalSecInSyncLoss_Type()
)
linkFRAccLnkAccumStatisticsLocalSecInSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsLocalSecInSyncLoss.setStatus("mandatory")
_LinkFRAccLnkAccumStatisticsLocalSecInCarrierLoss_Type = Integer32
_LinkFRAccLnkAccumStatisticsLocalSecInCarrierLoss_Object = MibTableColumn
linkFRAccLnkAccumStatisticsLocalSecInCarrierLoss = _LinkFRAccLnkAccumStatisticsLocalSecInCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 2, 1, 6, 3, 8, 1, 13),
    _LinkFRAccLnkAccumStatisticsLocalSecInCarrierLoss_Type()
)
linkFRAccLnkAccumStatisticsLocalSecInCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFRAccLnkAccumStatisticsLocalSecInCarrierLoss.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcmEventConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 1)
)
mcmEventConnect.setObjects(
      *(("MICOM-NODE-MIB", "trapFirstNodeName"),
        ("MICOM-NODE-MIB", "trapFirstCardNumberOrInternalFacilityIndication"),
        ("MICOM-NODE-MIB", "trapFirstChannelNumberOrInternalFacility"),
        ("MICOM-NODE-MIB", "trapSecondNodeName"),
        ("MICOM-NODE-MIB", "trapSecondCardNumberOrInternalFacilityIndication"),
        ("MICOM-NODE-MIB", "trapSecondChannelNumberOrInternalFacility"))
)
if mibBuilder.loadTexts:
    mcmEventConnect.setStatus(
        ""
    )

mcmEventDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 2)
)
mcmEventDisconnect.setObjects(
      *(("MICOM-NODE-MIB", "trapFirstNodeName"),
        ("MICOM-NODE-MIB", "trapFirstCardNumberOrInternalFacilityIndication"),
        ("MICOM-NODE-MIB", "trapFirstChannelNumberOrInternalFacility"),
        ("MICOM-NODE-MIB", "trapSecondNodeName"),
        ("MICOM-NODE-MIB", "trapSecondCardNumberOrInternalFacilityIndication"),
        ("MICOM-NODE-MIB", "trapSecondChannelNumberOrInternalFacility"))
)
if mibBuilder.loadTexts:
    mcmEventDisconnect.setStatus(
        ""
    )

mcmEventQueueEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 3)
)
mcmEventQueueEntry.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapClassRequestedOrMatrixRequest"))
)
if mibBuilder.loadTexts:
    mcmEventQueueEntry.setStatus(
        ""
    )

mcmEventCallFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 4)
)
mcmEventCallFail.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapClassRequestedOrMatrixRequest"))
)
if mibBuilder.loadTexts:
    mcmEventCallFail.setStatus(
        ""
    )

mcmEventDDSInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 5)
)
mcmEventDDSInService.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventDDSInService.setStatus(
        ""
    )

mcmEventDDSOutService = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 6)
)
mcmEventDDSOutService.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventDDSOutService.setStatus(
        ""
    )

mcmEventDDSLoopTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 7)
)
mcmEventDDSLoopTest.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventDDSLoopTest.setStatus(
        ""
    )

mcmEventADBConnectMade = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 8)
)
mcmEventADBConnectMade.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBConnectMade.setStatus(
        ""
    )

mcmEventADBConnectDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 9)
)
mcmEventADBConnectDrop.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBConnectDrop.setStatus(
        ""
    )

mcmEventForcedDialMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 10)
)
mcmEventForcedDialMode.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventForcedDialMode.setStatus(
        ""
    )

mcmEventForcedLeaseMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 11)
)
mcmEventForcedLeaseMode.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventForcedLeaseMode.setStatus(
        ""
    )

mcmEventLeasedConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 12)
)
mcmEventLeasedConnect.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventLeasedConnect.setStatus(
        ""
    )

mcmEventLeaseLineRetry = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 13)
)
mcmEventLeaseLineRetry.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventLeaseLineRetry.setStatus(
        ""
    )

mcmEventLinkRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 14)
)
mcmEventLinkRestart.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmEventLinkRestart.setStatus(
        ""
    )

mcmEventRemoteLinkRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 15)
)
mcmEventRemoteLinkRestart.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmEventRemoteLinkRestart.setStatus(
        ""
    )

mcmEventNoADBNumber = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 16)
)
mcmEventNoADBNumber.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventNoADBNumber.setStatus(
        ""
    )

mcmEventADBNoRXDialTone = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 17)
)
mcmEventADBNoRXDialTone.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBNoRXDialTone.setStatus(
        ""
    )

mcmEventADBNoTxDialTone = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 18)
)
mcmEventADBNoTxDialTone.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBNoTxDialTone.setStatus(
        ""
    )

mcmEventADBRxDialing = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 19)
)
mcmEventADBRxDialing.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBRxDialing.setStatus(
        ""
    )

mcmEventADBTxDialing = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 20)
)
mcmEventADBTxDialing.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBTxDialing.setStatus(
        ""
    )

mcmEventADBNoAnswer = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 21)
)
mcmEventADBNoAnswer.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBNoAnswer.setStatus(
        ""
    )

mcmEventADBRxBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 22)
)
mcmEventADBRxBusy.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBRxBusy.setStatus(
        ""
    )

mcmEventADBTxBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 23)
)
mcmEventADBTxBusy.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBTxBusy.setStatus(
        ""
    )

mcmEventADBRxRinging = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 24)
)
mcmEventADBRxRinging.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBRxRinging.setStatus(
        ""
    )

mcmEventADBTxRinging = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 25)
)
mcmEventADBTxRinging.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBTxRinging.setStatus(
        ""
    )

mcmEventADBRingDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 26)
)
mcmEventADBRingDetect.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBRingDetect.setStatus(
        ""
    )

mcmEventADBNoDialTone = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 27)
)
mcmEventADBNoDialTone.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBNoDialTone.setStatus(
        ""
    )

mcmEventVoiceBusyOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 28)
)
mcmEventVoiceBusyOut.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventVoiceBusyOut.setStatus(
        ""
    )

mcmEventVoiceClearBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 29)
)
mcmEventVoiceClearBusy.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventVoiceClearBusy.setStatus(
        ""
    )

mcmEventADBRxConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 30)
)
mcmEventADBRxConnect.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBRxConnect.setStatus(
        ""
    )

mcmEventADBTxConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 31)
)
mcmEventADBTxConnect.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBTxConnect.setStatus(
        ""
    )

mcmEventADBLineBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 32)
)
mcmEventADBLineBusy.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBLineBusy.setStatus(
        ""
    )

mcmEventADBRIDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 33)
)
mcmEventADBRIDetect.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBRIDetect.setStatus(
        ""
    )

mcmEventADBAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 34)
)
mcmEventADBAbort.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventADBAbort.setStatus(
        ""
    )

mcmEventLeasedLineOOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 35)
)
mcmEventLeasedLineOOS.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmEventLeasedLineOOS.setStatus(
        ""
    )

mcmEventNewDLCI = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 36)
)
mcmEventNewDLCI.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmEventNewDLCI.setStatus(
        ""
    )

mcmEventDLCIActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 37)
)
mcmEventDLCIActive.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmEventDLCIActive.setStatus(
        ""
    )

mcmEventConfigurationUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 38)
)
mcmEventConfigurationUpdate.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmEventConfigurationUpdate.setStatus(
        ""
    )

mcmEventDLCIConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 39)
)
mcmEventDLCIConnect.setObjects(
      *(("MICOM-NODE-MIB", "trapDLCIFirstLinkCardNumber"),
        ("MICOM-NODE-MIB", "trapDLCIFirstLinkChannelNumber"),
        ("MICOM-NODE-MIB", "trapDLCIFirstLinkDLCINumber"),
        ("MICOM-NODE-MIB", "trapDLCISecondLinkCardNumber"),
        ("MICOM-NODE-MIB", "trapDLCISecondLinkChannelNumber"),
        ("MICOM-NODE-MIB", "trapDLCISecondLinkDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmEventDLCIConnect.setStatus(
        ""
    )

mcmEventDLCIDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 40)
)
mcmEventDLCIDisconnect.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmEventDLCIDisconnect.setStatus(
        ""
    )

mcmAlarmSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 101)
)
mcmAlarmSystemReset.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmSystemReset.setStatus(
        ""
    )

mcmAlarmBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 102)
)
mcmAlarmBatteryLow.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmBatteryLow.setStatus(
        ""
    )

mcmAlarmCmosError = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 103)
)
mcmAlarmCmosError.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmCmosError.setStatus(
        ""
    )

mcmAlarmSystemFlowControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 104)
)
mcmAlarmSystemFlowControl.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmSystemFlowControl.setStatus(
        ""
    )

mcmAlarmNodeTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 105)
)
mcmAlarmNodeTableFull.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmNodeTableFull.setStatus(
        ""
    )

mcmAlarmDuplicateNodeNumber = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 106)
)
mcmAlarmDuplicateNodeNumber.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmDuplicateNodeNumber.setStatus(
        ""
    )

mcmAlarmInvalidLinkCfg = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 107)
)
mcmAlarmInvalidLinkCfg.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmInvalidLinkCfg.setStatus(
        ""
    )

mcmAlarmBufferOverFlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 120)
)
mcmAlarmBufferOverFlow.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmBufferOverFlow.setStatus(
        ""
    )

mcmAlarmLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 121)
)
mcmAlarmLinkDown.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmLinkDown.setStatus(
        ""
    )

mcmAlarmSyncLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 122)
)
mcmAlarmSyncLoss.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmSyncLoss.setStatus(
        ""
    )

mcmAlarmSyncAcquire = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 123)
)
mcmAlarmSyncAcquire.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmSyncAcquire.setStatus(
        ""
    )

mcmAlarmCarrierLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 124)
)
mcmAlarmCarrierLoss.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmCarrierLoss.setStatus(
        ""
    )

mcmAlarmCarrierAcquire = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 125)
)
mcmAlarmCarrierAcquire.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmCarrierAcquire.setStatus(
        ""
    )

mcmAlarmLineAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 126)
)
mcmAlarmLineAlarm.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmLineAlarm.setStatus(
        ""
    )

mcmAlarmSyncChannelStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 127)
)
mcmAlarmSyncChannelStopped.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmSyncChannelStopped.setStatus(
        ""
    )

mcmAlarmLANCardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 128)
)
mcmAlarmLANCardUp.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmLANCardUp.setStatus(
        ""
    )

mcmAlarmLANCardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 129)
)
mcmAlarmLANCardDown.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmLANCardDown.setStatus(
        ""
    )

mcmAlarmX21CallFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 130)
)
mcmAlarmX21CallFail.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmX21CallFail.setStatus(
        ""
    )

mcmAlarmPrimaryESIDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 131)
)
mcmAlarmPrimaryESIDown.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmPrimaryESIDown.setStatus(
        ""
    )

mcmAlarmStartESISecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 132)
)
mcmAlarmStartESISecondary.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmStartESISecondary.setStatus(
        ""
    )

mcmAlarmSecondaryUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 133)
)
mcmAlarmSecondaryUp.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmSecondaryUp.setStatus(
        ""
    )

mcmAlarmSecondaryTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 134)
)
mcmAlarmSecondaryTerminated.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmSecondaryTerminated.setStatus(
        ""
    )

mcmAlarmSecondaryDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 135)
)
mcmAlarmSecondaryDown.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmSecondaryDown.setStatus(
        ""
    )

mcmAlarmSecondaryReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 136)
)
mcmAlarmSecondaryReset.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmSecondaryReset.setStatus(
        ""
    )

mcmAlarmPrimaryESIUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 137)
)
mcmAlarmPrimaryESIUp.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmPrimaryESIUp.setStatus(
        ""
    )

mcmAlarmDLCIDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 138)
)
mcmAlarmDLCIDeleted.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmDLCIDeleted.setStatus(
        ""
    )

mcmAlarmDLCIInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 139)
)
mcmAlarmDLCIInactive.setObjects(
      *(("MICOM-NODE-MIB", "trapNodeName"),
        ("MICOM-NODE-MIB", "trapCardNumber"),
        ("MICOM-NODE-MIB", "trapChannelNumber"),
        ("MICOM-NODE-MIB", "trapLinkType"),
        ("MICOM-NODE-MIB", "trapDLCINumber"))
)
if mibBuilder.loadTexts:
    mcmAlarmDLCIInactive.setStatus(
        ""
    )

mcmAlarmT1NetworkRedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 140)
)
mcmAlarmT1NetworkRedAlarm.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmT1NetworkRedAlarm.setStatus(
        ""
    )

mcmAlarmT1NetworkRedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 141)
)
mcmAlarmT1NetworkRedClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmT1NetworkRedClear.setStatus(
        ""
    )

mcmAlarmT1LocalRedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 142)
)
mcmAlarmT1LocalRedAlarm.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmT1LocalRedAlarm.setStatus(
        ""
    )

mcmAlarmT1LocalRedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 143)
)
mcmAlarmT1LocalRedClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmT1LocalRedClear.setStatus(
        ""
    )

mcmAlarmT1NetworkYellowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 144)
)
mcmAlarmT1NetworkYellowAlarm.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmT1NetworkYellowAlarm.setStatus(
        ""
    )

mcmAlarmT1NetworkYellowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 145)
)
mcmAlarmT1NetworkYellowClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmT1NetworkYellowClear.setStatus(
        ""
    )

mcmAlarmT1LocalYellowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 146)
)
mcmAlarmT1LocalYellowAlarm.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmT1LocalYellowAlarm.setStatus(
        ""
    )

mcmAlarmT1LocalYellowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 147)
)
mcmAlarmT1LocalYellowClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmT1LocalYellowClear.setStatus(
        ""
    )

mcmAlarmT1NetworkAlarmInd = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 148)
)
mcmAlarmT1NetworkAlarmInd.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmT1NetworkAlarmInd.setStatus(
        ""
    )

mcmAlarmT1NetworkAlarmIndClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 149)
)
mcmAlarmT1NetworkAlarmIndClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmT1NetworkAlarmIndClear.setStatus(
        ""
    )

mcmAlarmT1LocalAlarmInd = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 150)
)
mcmAlarmT1LocalAlarmInd.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmT1LocalAlarmInd.setStatus(
        ""
    )

mcmAlarmT1LocalAlarmIndClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 151)
)
mcmAlarmT1LocalAlarmIndClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmT1LocalAlarmIndClear.setStatus(
        ""
    )

mcmAlarmCheckConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 152)
)
mcmAlarmCheckConfiguration.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmCheckConfiguration.setStatus(
        ""
    )

mcmAlarmE1L2RedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 153)
)
mcmAlarmE1L2RedAlarm.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L2RedAlarm.setStatus(
        ""
    )

mcmAlarmE1L2RedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 154)
)
mcmAlarmE1L2RedAlarmClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L2RedAlarmClear.setStatus(
        ""
    )

mcmAlarmE1L1RedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 155)
)
mcmAlarmE1L1RedAlarm.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L1RedAlarm.setStatus(
        ""
    )

mcmAlarmE1L1RedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 156)
)
mcmAlarmE1L1RedAlarmClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L1RedAlarmClear.setStatus(
        ""
    )

mcmAlarmE1L2AlarmIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 157)
)
mcmAlarmE1L2AlarmIndication.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L2AlarmIndication.setStatus(
        ""
    )

mcmAlarmE1L2AlarmIndicationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 158)
)
mcmAlarmE1L2AlarmIndicationClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L2AlarmIndicationClear.setStatus(
        ""
    )

mcmAlarmE1L1AlarmIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 159)
)
mcmAlarmE1L1AlarmIndication.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L1AlarmIndication.setStatus(
        ""
    )

mcmAlarmE1L1AlarmIndicationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 160)
)
mcmAlarmE1L1AlarmIndicationClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L1AlarmIndicationClear.setStatus(
        ""
    )

mcmAlarmE1L2OOCASFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 161)
)
mcmAlarmE1L2OOCASFrame.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L2OOCASFrame.setStatus(
        ""
    )

mcmAlarmE1L2OOCASFrameClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 162)
)
mcmAlarmE1L2OOCASFrameClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L2OOCASFrameClear.setStatus(
        ""
    )

mcmAlarmE1L1OOCASFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 163)
)
mcmAlarmE1L1OOCASFrame.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L1OOCASFrame.setStatus(
        ""
    )

mcmAlarmE1L1OOCASFrameClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 164)
)
mcmAlarmE1L1OOCASFrameClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L1OOCASFrameClear.setStatus(
        ""
    )

mcmAlarmE1L2TS16AISAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 165)
)
mcmAlarmE1L2TS16AISAlarm.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L2TS16AISAlarm.setStatus(
        ""
    )

mcmAlarmE1L2TS16AISAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 166)
)
mcmAlarmE1L2TS16AISAlarmClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L2TS16AISAlarmClear.setStatus(
        ""
    )

mcmAlarmE1L1TS16AISAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 167)
)
mcmAlarmE1L1TS16AISAlarm.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L1TS16AISAlarm.setStatus(
        ""
    )

mcmAlarmE1L1TS16AISAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 168)
)
mcmAlarmE1L1TS16AISAlarmClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L1TS16AISAlarmClear.setStatus(
        ""
    )

mcmAlarmE1L2RemoteYAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 169)
)
mcmAlarmE1L2RemoteYAlarm.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L2RemoteYAlarm.setStatus(
        ""
    )

mcmAlarmE1L2RemoteYAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 170)
)
mcmAlarmE1L2RemoteYAlarmClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L2RemoteYAlarmClear.setStatus(
        ""
    )

mcmAlarmE1L1RemoteYAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 171)
)
mcmAlarmE1L1RemoteYAlarm.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L1RemoteYAlarm.setStatus(
        ""
    )

mcmAlarmE1L1RemoteYAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 172)
)
mcmAlarmE1L1RemoteYAlarmClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L1RemoteYAlarmClear.setStatus(
        ""
    )

mcmAlarmE1L2RemoteAAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 173)
)
mcmAlarmE1L2RemoteAAlarm.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L2RemoteAAlarm.setStatus(
        ""
    )

mcmAlarmE1L2RemoteAAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 174)
)
mcmAlarmE1L2RemoteAAlarmClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L2RemoteAAlarmClear.setStatus(
        ""
    )

mcmAlarmE1L1RemoteAAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 175)
)
mcmAlarmE1L1RemoteAAlarm.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L1RemoteAAlarm.setStatus(
        ""
    )

mcmAlarmE1L1RemoteAAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 176)
)
mcmAlarmE1L1RemoteAAlarmClear.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmAlarmE1L1RemoteAAlarmClear.setStatus(
        ""
    )

mcmProxyAlarmNodeUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 500)
)
mcmProxyAlarmNodeUnreachable.setObjects(
    ("MICOM-NODE-MIB", "trapNodeName")
)
if mibBuilder.loadTexts:
    mcmProxyAlarmNodeUnreachable.setStatus(
        ""
    )

mcmProxyEventPollingBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 600)
)
if mibBuilder.loadTexts:
    mcmProxyEventPollingBegin.setStatus(
        ""
    )

mcmProxyEventPollingEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 0, 601)
)
if mibBuilder.loadTexts:
    mcmProxyEventPollingEnd.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-NODE-MIB",
    **{"micom": micom,
       "mcmEventConnect": mcmEventConnect,
       "mcmEventDisconnect": mcmEventDisconnect,
       "mcmEventQueueEntry": mcmEventQueueEntry,
       "mcmEventCallFail": mcmEventCallFail,
       "mcmEventDDSInService": mcmEventDDSInService,
       "mcmEventDDSOutService": mcmEventDDSOutService,
       "mcmEventDDSLoopTest": mcmEventDDSLoopTest,
       "mcmEventADBConnectMade": mcmEventADBConnectMade,
       "mcmEventADBConnectDrop": mcmEventADBConnectDrop,
       "mcmEventForcedDialMode": mcmEventForcedDialMode,
       "mcmEventForcedLeaseMode": mcmEventForcedLeaseMode,
       "mcmEventLeasedConnect": mcmEventLeasedConnect,
       "mcmEventLeaseLineRetry": mcmEventLeaseLineRetry,
       "mcmEventLinkRestart": mcmEventLinkRestart,
       "mcmEventRemoteLinkRestart": mcmEventRemoteLinkRestart,
       "mcmEventNoADBNumber": mcmEventNoADBNumber,
       "mcmEventADBNoRXDialTone": mcmEventADBNoRXDialTone,
       "mcmEventADBNoTxDialTone": mcmEventADBNoTxDialTone,
       "mcmEventADBRxDialing": mcmEventADBRxDialing,
       "mcmEventADBTxDialing": mcmEventADBTxDialing,
       "mcmEventADBNoAnswer": mcmEventADBNoAnswer,
       "mcmEventADBRxBusy": mcmEventADBRxBusy,
       "mcmEventADBTxBusy": mcmEventADBTxBusy,
       "mcmEventADBRxRinging": mcmEventADBRxRinging,
       "mcmEventADBTxRinging": mcmEventADBTxRinging,
       "mcmEventADBRingDetect": mcmEventADBRingDetect,
       "mcmEventADBNoDialTone": mcmEventADBNoDialTone,
       "mcmEventVoiceBusyOut": mcmEventVoiceBusyOut,
       "mcmEventVoiceClearBusy": mcmEventVoiceClearBusy,
       "mcmEventADBRxConnect": mcmEventADBRxConnect,
       "mcmEventADBTxConnect": mcmEventADBTxConnect,
       "mcmEventADBLineBusy": mcmEventADBLineBusy,
       "mcmEventADBRIDetect": mcmEventADBRIDetect,
       "mcmEventADBAbort": mcmEventADBAbort,
       "mcmEventLeasedLineOOS": mcmEventLeasedLineOOS,
       "mcmEventNewDLCI": mcmEventNewDLCI,
       "mcmEventDLCIActive": mcmEventDLCIActive,
       "mcmEventConfigurationUpdate": mcmEventConfigurationUpdate,
       "mcmEventDLCIConnect": mcmEventDLCIConnect,
       "mcmEventDLCIDisconnect": mcmEventDLCIDisconnect,
       "mcmAlarmSystemReset": mcmAlarmSystemReset,
       "mcmAlarmBatteryLow": mcmAlarmBatteryLow,
       "mcmAlarmCmosError": mcmAlarmCmosError,
       "mcmAlarmSystemFlowControl": mcmAlarmSystemFlowControl,
       "mcmAlarmNodeTableFull": mcmAlarmNodeTableFull,
       "mcmAlarmDuplicateNodeNumber": mcmAlarmDuplicateNodeNumber,
       "mcmAlarmInvalidLinkCfg": mcmAlarmInvalidLinkCfg,
       "mcmAlarmBufferOverFlow": mcmAlarmBufferOverFlow,
       "mcmAlarmLinkDown": mcmAlarmLinkDown,
       "mcmAlarmSyncLoss": mcmAlarmSyncLoss,
       "mcmAlarmSyncAcquire": mcmAlarmSyncAcquire,
       "mcmAlarmCarrierLoss": mcmAlarmCarrierLoss,
       "mcmAlarmCarrierAcquire": mcmAlarmCarrierAcquire,
       "mcmAlarmLineAlarm": mcmAlarmLineAlarm,
       "mcmAlarmSyncChannelStopped": mcmAlarmSyncChannelStopped,
       "mcmAlarmLANCardUp": mcmAlarmLANCardUp,
       "mcmAlarmLANCardDown": mcmAlarmLANCardDown,
       "mcmAlarmX21CallFail": mcmAlarmX21CallFail,
       "mcmAlarmPrimaryESIDown": mcmAlarmPrimaryESIDown,
       "mcmAlarmStartESISecondary": mcmAlarmStartESISecondary,
       "mcmAlarmSecondaryUp": mcmAlarmSecondaryUp,
       "mcmAlarmSecondaryTerminated": mcmAlarmSecondaryTerminated,
       "mcmAlarmSecondaryDown": mcmAlarmSecondaryDown,
       "mcmAlarmSecondaryReset": mcmAlarmSecondaryReset,
       "mcmAlarmPrimaryESIUp": mcmAlarmPrimaryESIUp,
       "mcmAlarmDLCIDeleted": mcmAlarmDLCIDeleted,
       "mcmAlarmDLCIInactive": mcmAlarmDLCIInactive,
       "mcmAlarmT1NetworkRedAlarm": mcmAlarmT1NetworkRedAlarm,
       "mcmAlarmT1NetworkRedClear": mcmAlarmT1NetworkRedClear,
       "mcmAlarmT1LocalRedAlarm": mcmAlarmT1LocalRedAlarm,
       "mcmAlarmT1LocalRedClear": mcmAlarmT1LocalRedClear,
       "mcmAlarmT1NetworkYellowAlarm": mcmAlarmT1NetworkYellowAlarm,
       "mcmAlarmT1NetworkYellowClear": mcmAlarmT1NetworkYellowClear,
       "mcmAlarmT1LocalYellowAlarm": mcmAlarmT1LocalYellowAlarm,
       "mcmAlarmT1LocalYellowClear": mcmAlarmT1LocalYellowClear,
       "mcmAlarmT1NetworkAlarmInd": mcmAlarmT1NetworkAlarmInd,
       "mcmAlarmT1NetworkAlarmIndClear": mcmAlarmT1NetworkAlarmIndClear,
       "mcmAlarmT1LocalAlarmInd": mcmAlarmT1LocalAlarmInd,
       "mcmAlarmT1LocalAlarmIndClear": mcmAlarmT1LocalAlarmIndClear,
       "mcmAlarmCheckConfiguration": mcmAlarmCheckConfiguration,
       "mcmAlarmE1L2RedAlarm": mcmAlarmE1L2RedAlarm,
       "mcmAlarmE1L2RedAlarmClear": mcmAlarmE1L2RedAlarmClear,
       "mcmAlarmE1L1RedAlarm": mcmAlarmE1L1RedAlarm,
       "mcmAlarmE1L1RedAlarmClear": mcmAlarmE1L1RedAlarmClear,
       "mcmAlarmE1L2AlarmIndication": mcmAlarmE1L2AlarmIndication,
       "mcmAlarmE1L2AlarmIndicationClear": mcmAlarmE1L2AlarmIndicationClear,
       "mcmAlarmE1L1AlarmIndication": mcmAlarmE1L1AlarmIndication,
       "mcmAlarmE1L1AlarmIndicationClear": mcmAlarmE1L1AlarmIndicationClear,
       "mcmAlarmE1L2OOCASFrame": mcmAlarmE1L2OOCASFrame,
       "mcmAlarmE1L2OOCASFrameClear": mcmAlarmE1L2OOCASFrameClear,
       "mcmAlarmE1L1OOCASFrame": mcmAlarmE1L1OOCASFrame,
       "mcmAlarmE1L1OOCASFrameClear": mcmAlarmE1L1OOCASFrameClear,
       "mcmAlarmE1L2TS16AISAlarm": mcmAlarmE1L2TS16AISAlarm,
       "mcmAlarmE1L2TS16AISAlarmClear": mcmAlarmE1L2TS16AISAlarmClear,
       "mcmAlarmE1L1TS16AISAlarm": mcmAlarmE1L1TS16AISAlarm,
       "mcmAlarmE1L1TS16AISAlarmClear": mcmAlarmE1L1TS16AISAlarmClear,
       "mcmAlarmE1L2RemoteYAlarm": mcmAlarmE1L2RemoteYAlarm,
       "mcmAlarmE1L2RemoteYAlarmClear": mcmAlarmE1L2RemoteYAlarmClear,
       "mcmAlarmE1L1RemoteYAlarm": mcmAlarmE1L1RemoteYAlarm,
       "mcmAlarmE1L1RemoteYAlarmClear": mcmAlarmE1L1RemoteYAlarmClear,
       "mcmAlarmE1L2RemoteAAlarm": mcmAlarmE1L2RemoteAAlarm,
       "mcmAlarmE1L2RemoteAAlarmClear": mcmAlarmE1L2RemoteAAlarmClear,
       "mcmAlarmE1L1RemoteAAlarm": mcmAlarmE1L1RemoteAAlarm,
       "mcmAlarmE1L1RemoteAAlarmClear": mcmAlarmE1L1RemoteAAlarmClear,
       "mcmProxyAlarmNodeUnreachable": mcmProxyAlarmNodeUnreachable,
       "mcmProxyEventPollingBegin": mcmProxyEventPollingBegin,
       "mcmProxyEventPollingEnd": mcmProxyEventPollingEnd,
       "products": products,
       "marathon-netrunner": marathon_netrunner,
       "micom-proxy": micom_proxy,
       "marathon-netrunner-proxy": marathon_netrunner_proxy,
       "security": security,
       "lcdSecurityPassword": lcdSecurityPassword,
       "cmdPortSecurityGroup": cmdPortSecurityGroup,
       "cmdPortSecurityGlobalPassword": cmdPortSecurityGlobalPassword,
       "cmdPortSecurityStatusPassword": cmdPortSecurityStatusPassword,
       "nmsSecurityPPPPassword": nmsSecurityPPPPassword,
       "diagnostics": diagnostics,
       "pingResponse": pingResponse,
       "voiceChannelDiagTable": voiceChannelDiagTable,
       "voiceChannelDiagEntry": voiceChannelDiagEntry,
       "voiceChannelDiagCardNumber": voiceChannelDiagCardNumber,
       "voiceChannelDiagChannelNumber": voiceChannelDiagChannelNumber,
       "voiceChannelDiagCommand": voiceChannelDiagCommand,
       "syncChannelDiagTable": syncChannelDiagTable,
       "syncChannelDiagEntry": syncChannelDiagEntry,
       "syncChannelDiagCardNumber": syncChannelDiagCardNumber,
       "syncChannelDiagChannelNumber": syncChannelDiagChannelNumber,
       "syncChannelDiagCommand": syncChannelDiagCommand,
       "configuration": configuration,
       "system": system,
       "attributes": attributes,
       "sysPromID": sysPromID,
       "sysTypeGroup": sysTypeGroup,
       "sysSoftwareType": sysSoftwareType,
       "sysHardwareType": sysHardwareType,
       "sysOperationalType": sysOperationalType,
       "sysSoftwarePhase": sysSoftwarePhase,
       "sysFeatureType": sysFeatureType,
       "sysFeatureRTC": sysFeatureRTC,
       "sysLocNodeLinkTable": sysLocNodeLinkTable,
       "sysLocNodeLinkEntry": sysLocNodeLinkEntry,
       "sysLocNodeLinkIndex": sysLocNodeLinkIndex,
       "sysLocNodeLinkNodeNameOfFeeder": sysLocNodeLinkNodeNameOfFeeder,
       "sysLocNodeLinkNodeType": sysLocNodeLinkNodeType,
       "sysLocNodeLinkNodeNumber": sysLocNodeLinkNodeNumber,
       "sysDateTime": sysDateTime,
       "sysClassCfgTable": sysClassCfgTable,
       "sysClassCfgEntry": sysClassCfgEntry,
       "sysClassCfgClassNumber": sysClassCfgClassNumber,
       "sysClassCfgClassName": sysClassCfgClassName,
       "sysClassCfgClassSecondary": sysClassCfgClassSecondary,
       "sysClassCfgClassMessage": sysClassCfgClassMessage,
       "sysClassCfgClassPassword": sysClassCfgClassPassword,
       "sysClassCfgNoActivityTimeOut": sysClassCfgNoActivityTimeOut,
       "sysClassCfgEntryStatus": sysClassCfgEntryStatus,
       "sysAccessNodeName": sysAccessNodeName,
       "sysFlashDownloadGroup": sysFlashDownloadGroup,
       "sysFlashDownloadPassword": sysFlashDownloadPassword,
       "sysFlashDownloadUseFile": sysFlashDownloadUseFile,
       "sysFlashDownloadDataActivityTimeout": sysFlashDownloadDataActivityTimeout,
       "sysMeshRouting": sysMeshRouting,
       "sysBootID": sysBootID,
       "sysNetTime": sysNetTime,
       "sysCodeDownloadGroup": sysCodeDownloadGroup,
       "sysCodeDownloadType": sysCodeDownloadType,
       "sysCodeDownloadNodeName": sysCodeDownloadNodeName,
       "sysCodeDownloadSlotNumber": sysCodeDownloadSlotNumber,
       "sysCodeDownloadChannelNumber": sysCodeDownloadChannelNumber,
       "sysCodeDownloadImageFile": sysCodeDownloadImageFile,
       "sysCodeDownloadFlashBank": sysCodeDownloadFlashBank,
       "sysCodeDownloadRestartFromBank": sysCodeDownloadRestartFromBank,
       "sysCodeDownloadReset": sysCodeDownloadReset,
       "sysCodeDownloadActionStatus": sysCodeDownloadActionStatus,
       "sysCodeDownloadFileSize": sysCodeDownloadFileSize,
       "sysCodeDownloadBytesDownloaded": sysCodeDownloadBytesDownloaded,
       "sysCodeDownloadNodeNumber": sysCodeDownloadNodeNumber,
       "messages": messages,
       "sysMessageWelcome": sysMessageWelcome,
       "sysMessageChannelPasswd": sysMessageChannelPasswd,
       "sysMessageClassRequest": sysMessageClassRequest,
       "sysMessageConnected": sysMessageConnected,
       "sysMessageQueued": sysMessageQueued,
       "sysMessageDisconnected": sysMessageDisconnected,
       "sysMessageCallInProgress": sysMessageCallInProgress,
       "sysMessageNoAnswer": sysMessageNoAnswer,
       "sysMessageUnassigned": sysMessageUnassigned,
       "sysMessageUnavailable": sysMessageUnavailable,
       "sysMessageBusy": sysMessageBusy,
       "sysMessageIncompatible": sysMessageIncompatible,
       "sysMessageClassPasswd": sysMessageClassPasswd,
       "sysMessageLCDKeypadBanner": sysMessageLCDKeypadBanner,
       "card": card,
       "cardTable": cardTable,
       "cardEntry": cardEntry,
       "cardSlotNumber": cardSlotNumber,
       "cardModuleID": cardModuleID,
       "cardPcbRevision": cardPcbRevision,
       "numberOfCards": numberOfCards,
       "eliCardFunctionTable": eliCardFunctionTable,
       "eliCardFunctionEntry": eliCardFunctionEntry,
       "eliCardFunctionSlotNumber": eliCardFunctionSlotNumber,
       "eliCardFunctionPromID": eliCardFunctionPromID,
       "eliCardFunctionTypeRTSFunction": eliCardFunctionTypeRTSFunction,
       "eliCardFunctionTypeBridgeFunction": eliCardFunctionTypeBridgeFunction,
       "eliCardFunctionTypeRouterFunction": eliCardFunctionTypeRouterFunction,
       "eliCardFunctionFlashMemory": eliCardFunctionFlashMemory,
       "t1e1CardSoftwareInfoTable": t1e1CardSoftwareInfoTable,
       "t1e1CardSoftwareInfoEntry": t1e1CardSoftwareInfoEntry,
       "t1e1CardSoftwareInfoCardNumber": t1e1CardSoftwareInfoCardNumber,
       "t1e1CardSoftwareInfoCardType": t1e1CardSoftwareInfoCardType,
       "t1e1CardSoftwareInfoReleaseLevel": t1e1CardSoftwareInfoReleaseLevel,
       "t1e1CardSoftwareInfoSoftwareID": t1e1CardSoftwareInfoSoftwareID,
       "t1e1CardSoftwareInfoBootCode": t1e1CardSoftwareInfoBootCode,
       "port": port,
       "portCfgTable": portCfgTable,
       "portCfgEntry": portCfgEntry,
       "portCfgCardNumber": portCfgCardNumber,
       "portCfgChannelNumber": portCfgChannelNumber,
       "portCfgChannelType": portCfgChannelType,
       "syncPortCfgTable": syncPortCfgTable,
       "syncPortCfgEntry": syncPortCfgEntry,
       "syncPortCfgCardNumber": syncPortCfgCardNumber,
       "syncPortCfgChannelNumber": syncPortCfgChannelNumber,
       "syncPortCfgProtocol": syncPortCfgProtocol,
       "fCmdPortPhyParaTable": fCmdPortPhyParaTable,
       "fCmdPortPhyParaEntry": fCmdPortPhyParaEntry,
       "fCmdPortPhyParaCardNumber": fCmdPortPhyParaCardNumber,
       "fCmdPortPhyParaChannelNumber": fCmdPortPhyParaChannelNumber,
       "fCmdPortPhyParaStopBits": fCmdPortPhyParaStopBits,
       "fCmdPortPhyParaCodeLevel": fCmdPortPhyParaCodeLevel,
       "fCmdPortPhyParaDataRate": fCmdPortPhyParaDataRate,
       "fCmdPortPhyParaEcho": fCmdPortPhyParaEcho,
       "fCmdPortPhyParaCRDelay": fCmdPortPhyParaCRDelay,
       "fCmdPortPhyParaLFDelay": fCmdPortPhyParaLFDelay,
       "fCmdPortPhyParaFFDelay": fCmdPortPhyParaFFDelay,
       "fCmdPortPhyParaParity": fCmdPortPhyParaParity,
       "logPortPhyParaTable": logPortPhyParaTable,
       "logPortPhyParaEntry": logPortPhyParaEntry,
       "logPortPhyParaCardNumber": logPortPhyParaCardNumber,
       "logPortPhyParaChannelNumber": logPortPhyParaChannelNumber,
       "logPortPhyParaStopBits": logPortPhyParaStopBits,
       "logPortPhyParaCodeLevel": logPortPhyParaCodeLevel,
       "logPortPhyParaDataRate": logPortPhyParaDataRate,
       "logPortPhyParaCRDelay": logPortPhyParaCRDelay,
       "logPortPhyParaLFDelay": logPortPhyParaLFDelay,
       "logPortPhyParaFFDelay": logPortPhyParaFFDelay,
       "logPortPhyParaXONChar": logPortPhyParaXONChar,
       "logPortPhyParaXOFFChar": logPortPhyParaXOFFChar,
       "logPortPhyParaFlowControl": logPortPhyParaFlowControl,
       "logPortPhyParaBufferControl": logPortPhyParaBufferControl,
       "logPortPhyParaParity": logPortPhyParaParity,
       "commandPortExtModemNumber": commandPortExtModemNumber,
       "commandPortDataActivityTimeout": commandPortDataActivityTimeout,
       "syncPortPreConfigTable": syncPortPreConfigTable,
       "syncPortPreConfigEntry": syncPortPreConfigEntry,
       "syncPortPreConfigCardNumber": syncPortPreConfigCardNumber,
       "syncPortPreConfigChannelNumber": syncPortPreConfigChannelNumber,
       "syncPortPreConfigProtocol": syncPortPreConfigProtocol,
       "channel": channel,
       "sync-channel": sync_channel,
       "syncChPhyParaTable": syncChPhyParaTable,
       "syncChPhyParaEntry": syncChPhyParaEntry,
       "syncChPhyParaCardNumber": syncChPhyParaCardNumber,
       "syncChPhyParaChannelNumber": syncChPhyParaChannelNumber,
       "syncChPhyParaDataRate": syncChPhyParaDataRate,
       "syncChPhyParaCarrierMode": syncChPhyParaCarrierMode,
       "syncChPhyParaInterfaceType": syncChPhyParaInterfaceType,
       "syncChPhyParaIdleFill": syncChPhyParaIdleFill,
       "syncChPhyParaHighSyncChar": syncChPhyParaHighSyncChar,
       "syncChPhyParaLowSyncChar": syncChPhyParaLowSyncChar,
       "syncChPhyParaNumLeadSyncCount": syncChPhyParaNumLeadSyncCount,
       "syncChPhyParaMaxTxBlockSize": syncChPhyParaMaxTxBlockSize,
       "syncChPhyParaPadChar": syncChPhyParaPadChar,
       "syncChPhyParaNumLeadingPads": syncChPhyParaNumLeadingPads,
       "syncChPhyParaNumTrailingPads": syncChPhyParaNumTrailingPads,
       "syncChPhyParaClockFlowControl": syncChPhyParaClockFlowControl,
       "syncChPhyParaEncoding": syncChPhyParaEncoding,
       "syncChPhyParaChTxClocking": syncChPhyParaChTxClocking,
       "syncChPhyParaChRxClocking": syncChPhyParaChRxClocking,
       "syncChPhyParaPriority": syncChPhyParaPriority,
       "syncChPhyParaDSRControl": syncChPhyParaDSRControl,
       "syncChPhyParaBufferControl": syncChPhyParaBufferControl,
       "syncChPhyParaMaxRxBlockSize": syncChPhyParaMaxRxBlockSize,
       "syncChPhyParaProtocol": syncChPhyParaProtocol,
       "syncChPhyParaClaimedBandwidth": syncChPhyParaClaimedBandwidth,
       "syncChPhyParaDLCTransitRate": syncChPhyParaDLCTransitRate,
       "async-channel": async_channel,
       "asyncChPhyParaTable": asyncChPhyParaTable,
       "asyncChPhyParaEntry": asyncChPhyParaEntry,
       "asyncChPhyParaCardNumber": asyncChPhyParaCardNumber,
       "asyncChPhyParaChannelNumber": asyncChPhyParaChannelNumber,
       "asyncChPhyParaStopBits": asyncChPhyParaStopBits,
       "asyncChPhyParaCodeLevel": asyncChPhyParaCodeLevel,
       "asyncChPhyParaDataRate": asyncChPhyParaDataRate,
       "asyncChPhyParaEcho": asyncChPhyParaEcho,
       "asyncChPhyParaHPXMode": asyncChPhyParaHPXMode,
       "asyncChPhyParaConnectTo": asyncChPhyParaConnectTo,
       "asyncChPhyParaRemCTSControl": asyncChPhyParaRemCTSControl,
       "asyncChPhyParaCRDelay": asyncChPhyParaCRDelay,
       "asyncChPhyParaLFDelay": asyncChPhyParaLFDelay,
       "asyncChPhyParaFFDelay": asyncChPhyParaFFDelay,
       "asyncChPhyParaXONChar": asyncChPhyParaXONChar,
       "asyncChPhyParaXOFFChar": asyncChPhyParaXOFFChar,
       "asyncChPhyParaCmdFacilityAccess": asyncChPhyParaCmdFacilityAccess,
       "asyncChPhyParaCmdModeEntry": asyncChPhyParaCmdModeEntry,
       "asyncChPhyParaLocChannelConfig": asyncChPhyParaLocChannelConfig,
       "asyncChPhyParaCmdModeAccess": asyncChPhyParaCmdModeAccess,
       "asyncChPhyParaTandemSupport": asyncChPhyParaTandemSupport,
       "asyncChPhyParaSmoothScroll": asyncChPhyParaSmoothScroll,
       "asyncChPhyParaFlowControl": asyncChPhyParaFlowControl,
       "asyncChPhyParaBufferControl": asyncChPhyParaBufferControl,
       "asyncChPhyParaFlowControlStrip": asyncChPhyParaFlowControlStrip,
       "asyncChPhyParaSyncLossDisconnect": asyncChPhyParaSyncLossDisconnect,
       "asyncChPhyParaEIAControls": asyncChPhyParaEIAControls,
       "asyncChPhyParaPriority": asyncChPhyParaPriority,
       "asyncChPhyParaParity": asyncChPhyParaParity,
       "asyncChPhyParaCompression": asyncChPhyParaCompression,
       "asyncChSwParaTable": asyncChSwParaTable,
       "asyncChSwParaEntry": asyncChSwParaEntry,
       "asyncChSwParaCardNumber": asyncChSwParaCardNumber,
       "asyncChSwParaChannelNumber": asyncChSwParaChannelNumber,
       "asyncChSwParaDestinationClass": asyncChSwParaDestinationClass,
       "asyncChSwParaConnectProtocol": asyncChSwParaConnectProtocol,
       "asyncChSwParaRcvInhibit": asyncChSwParaRcvInhibit,
       "asyncChSwParaResourceClassNumber": asyncChSwParaResourceClassNumber,
       "asyncChSwParaCallInhibit": asyncChSwParaCallInhibit,
       "asyncChSwParaUnbalanceRates": asyncChSwParaUnbalanceRates,
       "asyncChSwParaCharacterSet": asyncChSwParaCharacterSet,
       "asyncChSwParaMatrixSwitching": asyncChSwParaMatrixSwitching,
       "asyncChSwParaChannelPassword": asyncChSwParaChannelPassword,
       "voice-fax-channel": voice_fax_channel,
       "voiceFaxChPhyParaTable": voiceFaxChPhyParaTable,
       "voiceFaxChPhyParaEntry": voiceFaxChPhyParaEntry,
       "voiceFaxChPhyParaCardNumber": voiceFaxChPhyParaCardNumber,
       "voiceFaxChPhyParaChannelNumber": voiceFaxChPhyParaChannelNumber,
       "voiceFaxChPhyParaWireOperation": voiceFaxChPhyParaWireOperation,
       "voiceFaxChPhyParaViewSignallingType": voiceFaxChPhyParaViewSignallingType,
       "voiceFaxChPhyParaBergStrapType": voiceFaxChPhyParaBergStrapType,
       "voiceFaxChPhyParaSuppression": voiceFaxChPhyParaSuppression,
       "voiceFaxChPhyParaCfgSignallingType": voiceFaxChPhyParaCfgSignallingType,
       "voiceFaxChPhyParaOPXNumberOfRings": voiceFaxChPhyParaOPXNumberOfRings,
       "voiceFaxChPhyParaFXOSupervisorDisc": voiceFaxChPhyParaFXOSupervisorDisc,
       "voiceFaxChPhyParaRingFrequency": voiceFaxChPhyParaRingFrequency,
       "voiceFaxChPhyParaJitter": voiceFaxChPhyParaJitter,
       "voiceFaxChPhyParaDTMFRegeneration": voiceFaxChPhyParaDTMFRegeneration,
       "voiceFaxChPhyParaAutoLevelEnhancement": voiceFaxChPhyParaAutoLevelEnhancement,
       "voiceFaxChPhyParaBackground": voiceFaxChPhyParaBackground,
       "voiceFaxChPhyParaDigitizingRate": voiceFaxChPhyParaDigitizingRate,
       "voiceFaxChPhyParaBusyMode": voiceFaxChPhyParaBusyMode,
       "voiceFaxChPhyParaVoiceFaxMode": voiceFaxChPhyParaVoiceFaxMode,
       "voiceFaxChPhyParaBandwidthAssignment": voiceFaxChPhyParaBandwidthAssignment,
       "voiceFaxChPhyParaInputGain": voiceFaxChPhyParaInputGain,
       "voiceFaxChPhyParaChannelType": voiceFaxChPhyParaChannelType,
       "voiceFaxChPhyParaEMTypeStrapping": voiceFaxChPhyParaEMTypeStrapping,
       "voiceFaxChPhyParaOutputAttenuation": voiceFaxChPhyParaOutputAttenuation,
       "voiceFaxChPhyParaPriority": voiceFaxChPhyParaPriority,
       "voiceFaxChPhyParaFaxDigitizingRate": voiceFaxChPhyParaFaxDigitizingRate,
       "voiceFaxChPhyParaLineImpedance": voiceFaxChPhyParaLineImpedance,
       "voiceFaxChPhyParaMaxOutputLevel": voiceFaxChPhyParaMaxOutputLevel,
       "voiceFaxChPhyParaRegenerationDelay": voiceFaxChPhyParaRegenerationDelay,
       "voiceFaxChPhyParaMaxDialDigitTimeLimit": voiceFaxChPhyParaMaxDialDigitTimeLimit,
       "voiceFaxChPhyParaMaxNumFwdDigits": voiceFaxChPhyParaMaxNumFwdDigits,
       "voiceFaxChPhyParaCallProgressionTones": voiceFaxChPhyParaCallProgressionTones,
       "voiceFaxChPhyParaRegenFormat": voiceFaxChPhyParaRegenFormat,
       "voiceFaxChPhyParaChannelVersion": voiceFaxChPhyParaChannelVersion,
       "voiceFaxChSwParaTable": voiceFaxChSwParaTable,
       "voiceFaxChSwParaEntry": voiceFaxChSwParaEntry,
       "voiceFaxChSwParaCardNumber": voiceFaxChSwParaCardNumber,
       "voiceFaxChSwParaChannelNumber": voiceFaxChSwParaChannelNumber,
       "voiceFaxChSwParaVoiceExtension": voiceFaxChSwParaVoiceExtension,
       "voiceFaxChSwParaFaxExtension": voiceFaxChSwParaFaxExtension,
       "voiceFaxChSwParaAutoCallNumber": voiceFaxChSwParaAutoCallNumber,
       "voiceFaxChSwParaReceiveInhibit": voiceFaxChSwParaReceiveInhibit,
       "voiceFaxChSwParaCallInhibit": voiceFaxChSwParaCallInhibit,
       "voiceFaxChSwNumberOfDigitsInPhoneNumber": voiceFaxChSwNumberOfDigitsInPhoneNumber,
       "digital-voice-channel": digital_voice_channel,
       "digitalVoiceChPhyParaTable": digitalVoiceChPhyParaTable,
       "digitalVoiceChPhyParaEntry": digitalVoiceChPhyParaEntry,
       "digitalVoiceChPhyParaCardNumber": digitalVoiceChPhyParaCardNumber,
       "digitalVoiceChPhyParaChannelNumber": digitalVoiceChPhyParaChannelNumber,
       "digitalVoiceChPhyParaViewSignallingType": digitalVoiceChPhyParaViewSignallingType,
       "digitalVoiceChPhyParaBergStrapType": digitalVoiceChPhyParaBergStrapType,
       "digitalVoiceChPhyParaPortEmulation": digitalVoiceChPhyParaPortEmulation,
       "digitalVoiceChPhyParaSuppression": digitalVoiceChPhyParaSuppression,
       "digitalVoiceChPhyParaJitter": digitalVoiceChPhyParaJitter,
       "digitalVoiceChPhyParaDTMFRegeneration": digitalVoiceChPhyParaDTMFRegeneration,
       "digitalVoiceChPhyParaAutoGainControl": digitalVoiceChPhyParaAutoGainControl,
       "digitalVoiceChPhyParaBackground": digitalVoiceChPhyParaBackground,
       "digitalVoiceChPhyParaDigitizingRate": digitalVoiceChPhyParaDigitizingRate,
       "digitalVoiceChPhyParaBusyMode": digitalVoiceChPhyParaBusyMode,
       "digitalVoiceChPhyParaVoiceFaxMode": digitalVoiceChPhyParaVoiceFaxMode,
       "digitalVoiceChPhyParaBandwidthAssignment": digitalVoiceChPhyParaBandwidthAssignment,
       "digitalVoiceChPhyParaInputGain": digitalVoiceChPhyParaInputGain,
       "digitalVoiceChPhyParaChannelType": digitalVoiceChPhyParaChannelType,
       "digitalVoiceChPhyParaOutputAttenuation": digitalVoiceChPhyParaOutputAttenuation,
       "digitalVoiceChPhyParaPriority": digitalVoiceChPhyParaPriority,
       "digitalVoiceChPhyParaFaxDigitizingRate": digitalVoiceChPhyParaFaxDigitizingRate,
       "digitalVoiceChPhyParaRegenerationDelay": digitalVoiceChPhyParaRegenerationDelay,
       "digitalVoiceChPhyParaMaxDialDigitTimeLimit": digitalVoiceChPhyParaMaxDialDigitTimeLimit,
       "digitalVoiceChPhyParaMaxNumFwdDigits": digitalVoiceChPhyParaMaxNumFwdDigits,
       "digitalVoiceChPhyParaCallProgressionTones": digitalVoiceChPhyParaCallProgressionTones,
       "digitalVoiceChPhyParaRegenerationFormat": digitalVoiceChPhyParaRegenerationFormat,
       "digitalVoiceChPhyParaCompander": digitalVoiceChPhyParaCompander,
       "digitalVoiceChPhyParaPremiumVoice": digitalVoiceChPhyParaPremiumVoice,
       "digitalVoiceChPhyParaModuleIdentification": digitalVoiceChPhyParaModuleIdentification,
       "digitalVoiceChPhyParaChannelVersion": digitalVoiceChPhyParaChannelVersion,
       "digitalVoiceChSwParaTable": digitalVoiceChSwParaTable,
       "digitalVoiceChSwParaEntry": digitalVoiceChSwParaEntry,
       "digitalVoiceChSwParaCardNumber": digitalVoiceChSwParaCardNumber,
       "digitalVoiceChSwParaChannelNumber": digitalVoiceChSwParaChannelNumber,
       "digitalVoiceChSwParaVoiceExtension": digitalVoiceChSwParaVoiceExtension,
       "digitalVoiceChSwParaAutoCallNumber": digitalVoiceChSwParaAutoCallNumber,
       "digitalVoiceChSwParaReceiveInhibit": digitalVoiceChSwParaReceiveInhibit,
       "digitalVoiceChSwParaCallInhibit": digitalVoiceChSwParaCallInhibit,
       "link": link,
       "mux-link": mux_link,
       "muxLinkCfgTable": muxLinkCfgTable,
       "muxLinkCfgEntry": muxLinkCfgEntry,
       "muxLinkCfgCardNumber": muxLinkCfgCardNumber,
       "muxLinkCfgChannelNumber": muxLinkCfgChannelNumber,
       "muxLinkCfgDataRate": muxLinkCfgDataRate,
       "muxOrLEsiPreConfigTable": muxOrLEsiPreConfigTable,
       "muxOrLEsiPreConfigEntry": muxOrLEsiPreConfigEntry,
       "muxOrLEsiPreConfigCardNumber": muxOrLEsiPreConfigCardNumber,
       "muxOrLEsiPreConfigChannelNumber": muxOrLEsiPreConfigChannelNumber,
       "muxOrLEsiPreConfigDataRate": muxOrLEsiPreConfigDataRate,
       "esi-link": esi_link,
       "esiLinkCfgTable": esiLinkCfgTable,
       "esiLinkCfgEntry": esiLinkCfgEntry,
       "esiLinkCfgCardNumber": esiLinkCfgCardNumber,
       "esiLinkCfgChannelNumber": esiLinkCfgChannelNumber,
       "esiLinkCfgDataRate": esiLinkCfgDataRate,
       "esiOrSecLinkPreConfigTable": esiOrSecLinkPreConfigTable,
       "esiOrSecLinkPreConfigEntry": esiOrSecLinkPreConfigEntry,
       "esiOrSecLinkPreConfigCardNumber": esiOrSecLinkPreConfigCardNumber,
       "esiOrSecLinkPreConfigChannelNumber": esiOrSecLinkPreConfigChannelNumber,
       "esiOrSecLinkPreConfigDataRate": esiOrSecLinkPreConfigDataRate,
       "esiOrSecLinkAssignCfgTable": esiOrSecLinkAssignCfgTable,
       "esiOrSecLinkAssignCfgEntry": esiOrSecLinkAssignCfgEntry,
       "esiOrSecLinkAssignCfgCardNumber": esiOrSecLinkAssignCfgCardNumber,
       "esiOrSecLinkAssignCfgChannelNumber": esiOrSecLinkAssignCfgChannelNumber,
       "esiOrSecLinkAssignCfgLinkForcedOn": esiOrSecLinkAssignCfgLinkForcedOn,
       "esiOrSecLinkAssignCfgSecLinkBackUpOnly": esiOrSecLinkAssignCfgSecLinkBackUpOnly,
       "esiOrSecLinkAssignCfgUtilThresholdToActivateSec": esiOrSecLinkAssignCfgUtilThresholdToActivateSec,
       "esiOrSecLinkAssignCfgUtilThresholdToDeactivateSec": esiOrSecLinkAssignCfgUtilThresholdToDeactivateSec,
       "esiOrSecLinkAssignCfgTimeThresholdExceedToActivateSec": esiOrSecLinkAssignCfgTimeThresholdExceedToActivateSec,
       "esiOrSecLinkAssignCfgTimeThresholdBelowToDeactivateSec": esiOrSecLinkAssignCfgTimeThresholdBelowToDeactivateSec,
       "esiOrSecLinkAssignCfgTerminateCallonDeactivation": esiOrSecLinkAssignCfgTerminateCallonDeactivation,
       "esiOrSecLinkTODActivationTable": esiOrSecLinkTODActivationTable,
       "esiOrSecLinkTODActivationEntry": esiOrSecLinkTODActivationEntry,
       "esiOrSecLinkTODActivationCardNumber": esiOrSecLinkTODActivationCardNumber,
       "esiOrSecLinkTODActivationChannelNumber": esiOrSecLinkTODActivationChannelNumber,
       "esiOrSecLinkTODActivationSetSchedule": esiOrSecLinkTODActivationSetSchedule,
       "esiOrSecLinkTODActivationTenMinInterval": esiOrSecLinkTODActivationTenMinInterval,
       "esiOrSecLinkTODActivationLinkState": esiOrSecLinkTODActivationLinkState,
       "x-dot-21-link": x_dot_21_link,
       "x21LinkCfgTable": x21LinkCfgTable,
       "x21LinkCfgEntry": x21LinkCfgEntry,
       "x21LinkCfgCardNumber": x21LinkCfgCardNumber,
       "x21LinkCfgChannelNumber": x21LinkCfgChannelNumber,
       "x21LinkCfgLocalConnectMode": x21LinkCfgLocalConnectMode,
       "x21LinkCfgRemoteConnectMode": x21LinkCfgRemoteConnectMode,
       "x21LinkCfgLocalConnectTimeout": x21LinkCfgLocalConnectTimeout,
       "x21LinkCfgRemoteConnectTimeout": x21LinkCfgRemoteConnectTimeout,
       "x21LinkCfgLocalConnectRetries": x21LinkCfgLocalConnectRetries,
       "x21LinkCfgRemoteConnectRetries": x21LinkCfgRemoteConnectRetries,
       "x21LinkPreConfigTable": x21LinkPreConfigTable,
       "x21LinkPreConfigEntry": x21LinkPreConfigEntry,
       "x21LinkPreConfigCardNumber": x21LinkPreConfigCardNumber,
       "x21LinkPreConfigChannelNumber": x21LinkPreConfigChannelNumber,
       "x21LinkPreConfigLocalConnectMode": x21LinkPreConfigLocalConnectMode,
       "x21LinkPreConfigRemoteConnectMode": x21LinkPreConfigRemoteConnectMode,
       "x21LinkPreConfigLocalConnectTimeout": x21LinkPreConfigLocalConnectTimeout,
       "x21LinkPreConfigRemoteConnectTimeout": x21LinkPreConfigRemoteConnectTimeout,
       "x21LinkPreConfigLocalConnectRetries": x21LinkPreConfigLocalConnectRetries,
       "x21LinkPreConfigRemoteConnectRetries": x21LinkPreConfigRemoteConnectRetries,
       "local-esi-link": local_esi_link,
       "localESILinkCfgTable": localESILinkCfgTable,
       "localESILinkCfgEntry": localESILinkCfgEntry,
       "localESILinkCfgCardNumber": localESILinkCfgCardNumber,
       "localESILinkCfgChannelNumber": localESILinkCfgChannelNumber,
       "localESILinkCfgDataRate": localESILinkCfgDataRate,
       "esi-secondary-link": esi_secondary_link,
       "esiSecLinkCfgTable": esiSecLinkCfgTable,
       "esiSecLinkCfgEntry": esiSecLinkCfgEntry,
       "esiSecLinkCfgCardNumber": esiSecLinkCfgCardNumber,
       "esiSecLinkCfgChannelNumber": esiSecLinkCfgChannelNumber,
       "esiSecLinkCfgDataRate": esiSecLinkCfgDataRate,
       "esiSecLinkAssignmentTable": esiSecLinkAssignmentTable,
       "esiSecLinkAssignmentEntry": esiSecLinkAssignmentEntry,
       "esiSecLinkAssignmentSecCardNumber": esiSecLinkAssignmentSecCardNumber,
       "esiSecLinkAssignmentSecChannelNumber": esiSecLinkAssignmentSecChannelNumber,
       "esiSecLinkAssignmentEntryAction": esiSecLinkAssignmentEntryAction,
       "esiSecLinkAssignmentPriCardNumber": esiSecLinkAssignmentPriCardNumber,
       "esiSecLinkAssignmentPriChannelNumber": esiSecLinkAssignmentPriChannelNumber,
       "frame-relay-link": frame_relay_link,
       "frameRelayLinkCfgTable": frameRelayLinkCfgTable,
       "frameRelayLinkCfgEntry": frameRelayLinkCfgEntry,
       "frameRelayLinkCfgCardNumber": frameRelayLinkCfgCardNumber,
       "frameRelayLinkCfgChannelNumber": frameRelayLinkCfgChannelNumber,
       "frameRelayLinkCfgDataRate": frameRelayLinkCfgDataRate,
       "frameRelayLinkCfgLocalMgmtProtocol": frameRelayLinkCfgLocalMgmtProtocol,
       "frameRelayLinkCfgFullStatusPollingCounter": frameRelayLinkCfgFullStatusPollingCounter,
       "frameRelayLinkCfgErrorThreshold": frameRelayLinkCfgErrorThreshold,
       "frameRelayLinkCfgEventCount": frameRelayLinkCfgEventCount,
       "frameRelayLinkCfgLinkIntegrityVerificationTimer": frameRelayLinkCfgLinkIntegrityVerificationTimer,
       "frameRelayLinkCfgPollingVerificationTimer": frameRelayLinkCfgPollingVerificationTimer,
       "frameRelayLinkCfgMaxFrameSize": frameRelayLinkCfgMaxFrameSize,
       "frameRelayLinkCfgRxClockingSource": frameRelayLinkCfgRxClockingSource,
       "frameRelayLinkCfgTxClockingSource": frameRelayLinkCfgTxClockingSource,
       "frameRelayLinkCfgNetworkAddress": frameRelayLinkCfgNetworkAddress,
       "frameRelayLinkCfgAccessLinkMode": frameRelayLinkCfgAccessLinkMode,
       "frameRelayLinkCfgDLCITable": frameRelayLinkCfgDLCITable,
       "frameRelayLinkCfgDLCIEntry": frameRelayLinkCfgDLCIEntry,
       "frameRelayLinkCfgDLCICardNumber": frameRelayLinkCfgDLCICardNumber,
       "frameRelayLinkCfgDLCIChannelNumber": frameRelayLinkCfgDLCIChannelNumber,
       "frameRelayLinkCfgDLCINumber": frameRelayLinkCfgDLCINumber,
       "frameRelayLinkCfgDLCIType": frameRelayLinkCfgDLCIType,
       "frameRelayLinkCfgDLCICommittedInfoRateForward": frameRelayLinkCfgDLCICommittedInfoRateForward,
       "frameRelayLinkCfgDLCICommittedInfoRateBackward": frameRelayLinkCfgDLCICommittedInfoRateBackward,
       "frameRelayLinkCfgDLCICommittedBurstSizeForward": frameRelayLinkCfgDLCICommittedBurstSizeForward,
       "frameRelayLinkCfgDLCICommittedBurstSizeBackward": frameRelayLinkCfgDLCICommittedBurstSizeBackward,
       "frameRelayLinkCfgDLCIExcessBurstSizeForward": frameRelayLinkCfgDLCIExcessBurstSizeForward,
       "frameRelayLinkCfgDLCIExcessBurstSizeBackward": frameRelayLinkCfgDLCIExcessBurstSizeBackward,
       "frameRelayLinkControlTable": frameRelayLinkControlTable,
       "frameRelayLinkControlEntry": frameRelayLinkControlEntry,
       "frameRelayLinkControlLinkCardNumber": frameRelayLinkControlLinkCardNumber,
       "frameRelayLinkControlLinkChannelNumber": frameRelayLinkControlLinkChannelNumber,
       "frameRelayLinkControlDLCINumber": frameRelayLinkControlDLCINumber,
       "frameRelayLinkControlCommand": frameRelayLinkControlCommand,
       "frameRelayLinkControlDLCIType": frameRelayLinkControlDLCIType,
       "frameRelayDLCIControlTable": frameRelayDLCIControlTable,
       "frameRelayDLCIControlEntry": frameRelayDLCIControlEntry,
       "frameRelayDLCIControlLinkCardNumber": frameRelayDLCIControlLinkCardNumber,
       "frameRelayDLCIControlLinkChannelNumber": frameRelayDLCIControlLinkChannelNumber,
       "frameRelayDLCIControlDLCINumber": frameRelayDLCIControlDLCINumber,
       "frameRelayDLCIControlCommand": frameRelayDLCIControlCommand,
       "frameRelayDLCIControlFconnNodeName": frameRelayDLCIControlFconnNodeName,
       "frameRelayDLCIControlFconnCardNumber": frameRelayDLCIControlFconnCardNumber,
       "frameRelayDLCIControlFconnChannelNumber": frameRelayDLCIControlFconnChannelNumber,
       "frameRelayDLCIControlFconnDLCINumber": frameRelayDLCIControlFconnDLCINumber,
       "frameRelayDLCIConnectsTable": frameRelayDLCIConnectsTable,
       "frameRelayDLCIConnectsEntry": frameRelayDLCIConnectsEntry,
       "frameRelayDLCIConnectsLinkCardNumber": frameRelayDLCIConnectsLinkCardNumber,
       "frameRelayDLCIConnectsLinkChannelNumber": frameRelayDLCIConnectsLinkChannelNumber,
       "frameRelayDLCIConnectsDLCIConnected": frameRelayDLCIConnectsDLCIConnected,
       "frameRelayDLCIConnectsDestCardNumber": frameRelayDLCIConnectsDestCardNumber,
       "frameRelayDLCIConnectsDestChannelNumber": frameRelayDLCIConnectsDestChannelNumber,
       "frameRelayDLCIConnectsDestDLCINumber": frameRelayDLCIConnectsDestDLCINumber,
       "interface": interface,
       "t1-interface": t1_interface,
       "t1DS1InterfaceTable": t1DS1InterfaceTable,
       "t1DS1InterfaceEntry": t1DS1InterfaceEntry,
       "t1DS1InterfaceDS0Index": t1DS1InterfaceDS0Index,
       "t1DS1InterfaceConnectionState": t1DS1InterfaceConnectionState,
       "t1DSX1InterfaceTable": t1DSX1InterfaceTable,
       "t1DSX1InterfaceEntry": t1DSX1InterfaceEntry,
       "t1DSX1InterfaceDS0Index": t1DSX1InterfaceDS0Index,
       "t1DSX1InterfaceConnectionState": t1DSX1InterfaceConnectionState,
       "t1CfgGroup": t1CfgGroup,
       "t1CfgDSX1FrameFormat": t1CfgDSX1FrameFormat,
       "t1CfgDSX1LineCode": t1CfgDSX1LineCode,
       "t1CfgDSX1IdleCode": t1CfgDSX1IdleCode,
       "t1CfgDSX1lineBuildout": t1CfgDSX1lineBuildout,
       "t1CfgDSX1NetworkInvokedLoopback": t1CfgDSX1NetworkInvokedLoopback,
       "t1CfgDS1FrameFormat": t1CfgDS1FrameFormat,
       "t1CfgDS1LineCode": t1CfgDS1LineCode,
       "t1CfgDS1IdleCode": t1CfgDS1IdleCode,
       "t1CfgDS1NetworkInvokedLoopback": t1CfgDS1NetworkInvokedLoopback,
       "t1CfgDataPort1Rate": t1CfgDataPort1Rate,
       "t1CfgDataPort1Timing": t1CfgDataPort1Timing,
       "t1CfgDataPort1DTRControl": t1CfgDataPort1DTRControl,
       "t1CfgDataPort1RTSControl": t1CfgDataPort1RTSControl,
       "t1CfgDataPort2Rate": t1CfgDataPort2Rate,
       "t1CfgDataPort2Timing": t1CfgDataPort2Timing,
       "t1CfgDataPort2DTRControl": t1CfgDataPort2DTRControl,
       "t1CfgDataPort2RTSControl": t1CfgDataPort2RTSControl,
       "t1CfgCCMLinkA1Rate": t1CfgCCMLinkA1Rate,
       "t1CfgCCMLinkA2Rate": t1CfgCCMLinkA2Rate,
       "t1CfgCCMLinkA3Rate": t1CfgCCMLinkA3Rate,
       "t1CfgCCMLinkA4Rate": t1CfgCCMLinkA4Rate,
       "t1CfgCCMLinkA5Rate": t1CfgCCMLinkA5Rate,
       "t1CfgCCMLinkA6Rate": t1CfgCCMLinkA6Rate,
       "t1CfgSystemClockSource": t1CfgSystemClockSource,
       "t1CfgDS1Config": t1CfgDS1Config,
       "t1CfgDSX1Config": t1CfgDSX1Config,
       "t1FlashControlTable": t1FlashControlTable,
       "t1FlashControlEntry": t1FlashControlEntry,
       "t1FlashControlCardNumber": t1FlashControlCardNumber,
       "t1FlashControlCommand": t1FlashControlCommand,
       "t1FlashControlFlashStatus": t1FlashControlFlashStatus,
       "e1-interface": e1_interface,
       "e1L1InterfaceTable": e1L1InterfaceTable,
       "e1L1InterfaceEntry": e1L1InterfaceEntry,
       "e1L1InterfaceDS0Index": e1L1InterfaceDS0Index,
       "e1L1InterfaceConnectionState": e1L1InterfaceConnectionState,
       "e1L2InterfaceTable": e1L2InterfaceTable,
       "e1L2InterfaceEntry": e1L2InterfaceEntry,
       "e1L2InterfaceDS0Index": e1L2InterfaceDS0Index,
       "e1L2InterfaceConnectionState": e1L2InterfaceConnectionState,
       "e1CfgGroup": e1CfgGroup,
       "e1CfgL1LineCode": e1CfgL1LineCode,
       "e1CfgL1IdleCode": e1CfgL1IdleCode,
       "e1CfgL1SignallingMode": e1CfgL1SignallingMode,
       "e1CfgL2LineCode": e1CfgL2LineCode,
       "e1CfgL2IdleCode": e1CfgL2IdleCode,
       "e1CfgL2SignallingMode": e1CfgL2SignallingMode,
       "e1CfgDataPort1BaseRate": e1CfgDataPort1BaseRate,
       "e1CfgDataPort1Timing": e1CfgDataPort1Timing,
       "e1CfgDataPort1DTRControl": e1CfgDataPort1DTRControl,
       "e1CfgDataPort1RTSControl": e1CfgDataPort1RTSControl,
       "e1CfgDataPort2BaseRate": e1CfgDataPort2BaseRate,
       "e1CfgDataPort2Timing": e1CfgDataPort2Timing,
       "e1CfgDataPort2DTRControl": e1CfgDataPort2DTRControl,
       "e1CfgDataPort2RTSControl": e1CfgDataPort2RTSControl,
       "e1CfgCCMLinkA1Rate": e1CfgCCMLinkA1Rate,
       "e1CfgCCMLinkA2Rate": e1CfgCCMLinkA2Rate,
       "e1CfgCCMLinkA3Rate": e1CfgCCMLinkA3Rate,
       "e1CfgCCMLinkA4Rate": e1CfgCCMLinkA4Rate,
       "e1CfgCCMLinkA5Rate": e1CfgCCMLinkA5Rate,
       "e1CfgCCMLinkA6Rate": e1CfgCCMLinkA6Rate,
       "e1CfgSystemClockSource": e1CfgSystemClockSource,
       "e1CfgL1Crc4": e1CfgL1Crc4,
       "e1CfgL2Crc4": e1CfgL2Crc4,
       "e1CfgL1Config": e1CfgL1Config,
       "e1CfgL2Config": e1CfgL2Config,
       "e1FlashControlTable": e1FlashControlTable,
       "e1FlashControlEntry": e1FlashControlEntry,
       "e1FlashControlCardNumber": e1FlashControlCardNumber,
       "e1FlashControlCommand": e1FlashControlCommand,
       "e1FlashControlFlashStatus": e1FlashControlFlashStatus,
       "trap": trap,
       "trapAlarmEventReportingGroup": trapAlarmEventReportingGroup,
       "trapAlarmEventReportingAlarms": trapAlarmEventReportingAlarms,
       "trapAlarmEventReportingEvents": trapAlarmEventReportingEvents,
       "trapEventsCollectionInterval": trapEventsCollectionInterval,
       "trapSubsTable": trapSubsTable,
       "trapSubsEntry": trapSubsEntry,
       "trapSubsIPAddress": trapSubsIPAddress,
       "trapSubsCommunityString": trapSubsCommunityString,
       "trapSubsAction": trapSubsAction,
       "trapCfgAlarmEventsPortGroup": trapCfgAlarmEventsPortGroup,
       "trapCfgTrapPort": trapCfgTrapPort,
       "trapCfgExtModemPriority": trapCfgExtModemPriority,
       "trapCfgExtAlarmRelay": trapCfgExtAlarmRelay,
       "trapNodeName": trapNodeName,
       "trapCardNumber": trapCardNumber,
       "trapChannelNumber": trapChannelNumber,
       "trapFirstNodeName": trapFirstNodeName,
       "trapFirstCardNumberOrInternalFacilityIndication": trapFirstCardNumberOrInternalFacilityIndication,
       "trapFirstChannelNumberOrInternalFacility": trapFirstChannelNumberOrInternalFacility,
       "trapSecondNodeName": trapSecondNodeName,
       "trapSecondCardNumberOrInternalFacilityIndication": trapSecondCardNumberOrInternalFacilityIndication,
       "trapSecondChannelNumberOrInternalFacility": trapSecondChannelNumberOrInternalFacility,
       "trapClassRequestedOrMatrixRequest": trapClassRequestedOrMatrixRequest,
       "trapLinkType": trapLinkType,
       "trapDLCINumber": trapDLCINumber,
       "trapDLCIFirstLinkCardNumber": trapDLCIFirstLinkCardNumber,
       "trapDLCIFirstLinkChannelNumber": trapDLCIFirstLinkChannelNumber,
       "trapDLCIFirstLinkDLCINumber": trapDLCIFirstLinkDLCINumber,
       "trapDLCISecondLinkCardNumber": trapDLCISecondLinkCardNumber,
       "trapDLCISecondLinkChannelNumber": trapDLCISecondLinkChannelNumber,
       "trapDLCISecondLinkDLCINumber": trapDLCISecondLinkDLCINumber,
       "proxy": proxy,
       "pxyVersionNumber": pxyVersionNumber,
       "pxyCfgProxySwitch": pxyCfgProxySwitch,
       "pxyAddressMapTableNumber": pxyAddressMapTableNumber,
       "pxyAddressMapTable": pxyAddressMapTable,
       "pxyAddressMapEntry": pxyAddressMapEntry,
       "pxyAddressMapNodeNumber": pxyAddressMapNodeNumber,
       "pxyAddressMapEntryStatus": pxyAddressMapEntryStatus,
       "pxyAddressMapNodeNameAndCommunity": pxyAddressMapNodeNameAndCommunity,
       "pxyAddressMapChangeNodeNumberTo": pxyAddressMapChangeNodeNumberTo,
       "pxySupportedVersionTable": pxySupportedVersionTable,
       "pxySupportedVersionEntry": pxySupportedVersionEntry,
       "pxySupportedIndex": pxySupportedIndex,
       "pxySupportedVersionNumber": pxySupportedVersionNumber,
       "pxyStatisticsLastNodeServed": pxyStatisticsLastNodeServed,
       "pxyStatisticsLastErrorNode": pxyStatisticsLastErrorNode,
       "pxyStatisticsLastSNMPError": pxyStatisticsLastSNMPError,
       "pxyStatisticsLastErrorReturnCode": pxyStatisticsLastErrorReturnCode,
       "pxyStatisticsTotalRequests": pxyStatisticsTotalRequests,
       "pxyStatisticsTotalInternalTraps": pxyStatisticsTotalInternalTraps,
       "pxyPPPTotalCounts": pxyPPPTotalCounts,
       "pxyPPPRejectCounts": pxyPPPRejectCounts,
       "pxyCacheUpdate": pxyCacheUpdate,
       "pxyNetworkAccessNodeName": pxyNetworkAccessNodeName,
       "control": control,
       "nodeResetGroup": nodeResetGroup,
       "nodeResetCode": nodeResetCode,
       "nodeResetType": nodeResetType,
       "asyncResetTable": asyncResetTable,
       "asyncResetEntry": asyncResetEntry,
       "asyncResetCardNumber": asyncResetCardNumber,
       "asyncResetChannelNumber": asyncResetChannelNumber,
       "asyncResetCommand": asyncResetCommand,
       "syncResetTable": syncResetTable,
       "syncResetEntry": syncResetEntry,
       "syncResetCardNumber": syncResetCardNumber,
       "syncResetChannelNumber": syncResetChannelNumber,
       "syncResetCommand": syncResetCommand,
       "voiceResetTable": voiceResetTable,
       "voiceResetEntry": voiceResetEntry,
       "voiceResetCardNumber": voiceResetCardNumber,
       "voiceResetChannelNumber": voiceResetChannelNumber,
       "voiceResetCommand": voiceResetCommand,
       "linkResetTable": linkResetTable,
       "linkResetEntry": linkResetEntry,
       "linkResetCardNumber": linkResetCardNumber,
       "linkResetChannelNumber": linkResetChannelNumber,
       "linkResetCommand": linkResetCommand,
       "clearLatchedAlarms": clearLatchedAlarms,
       "pppLinkOperationGroup": pppLinkOperationGroup,
       "pppLinkOperationAction": pppLinkOperationAction,
       "pppLinkTimeOutAction": pppLinkTimeOutAction,
       "pppLinkDumpAction": pppLinkDumpAction,
       "flashEPROMCommand": flashEPROMCommand,
       "voiceFlashEPROMTable": voiceFlashEPROMTable,
       "voiceFlashEPROMEntry": voiceFlashEPROMEntry,
       "voiceFlashEPROMCardNumber": voiceFlashEPROMCardNumber,
       "voiceFlashEPROMChannelNumber": voiceFlashEPROMChannelNumber,
       "voiceFlashEPROMCommand": voiceFlashEPROMCommand,
       "lanCardResetTable": lanCardResetTable,
       "lanCardResetEntry": lanCardResetEntry,
       "lanCardResetCardNumber": lanCardResetCardNumber,
       "lanCardResetType": lanCardResetType,
       "chControlTable": chControlTable,
       "chControlEntry": chControlEntry,
       "chControlCardNumber": chControlCardNumber,
       "chControlChannelNumber": chControlChannelNumber,
       "chControlCommand": chControlCommand,
       "chControlForceConnToNodeName": chControlForceConnToNodeName,
       "chControlForceConnToCard": chControlForceConnToCard,
       "chControlForceConnToChannel": chControlForceConnToChannel,
       "frameRelayDLCIResetTable": frameRelayDLCIResetTable,
       "frameRelayDLCIResetEntry": frameRelayDLCIResetEntry,
       "frameRelayDLCIResetCardNumber": frameRelayDLCIResetCardNumber,
       "frameRelayDLCIResetChannelNumber": frameRelayDLCIResetChannelNumber,
       "frameRelayDLCIResetDLCINumber": frameRelayDLCIResetDLCINumber,
       "frameRelayAllDLCIResetTable": frameRelayAllDLCIResetTable,
       "frameRelayAllDLCIResetEntry": frameRelayAllDLCIResetEntry,
       "frameRelayAllDLCIResetCardNumber": frameRelayAllDLCIResetCardNumber,
       "frameRelayAllDLCIResetChannelNumber": frameRelayAllDLCIResetChannelNumber,
       "frameRelayAllDLCIResetCommand": frameRelayAllDLCIResetCommand,
       "t1e1CardResetTable": t1e1CardResetTable,
       "t1e1CardResetEntry": t1e1CardResetEntry,
       "t1e1CardResetCardNumber": t1e1CardResetCardNumber,
       "t1e1CardResetCommand": t1e1CardResetCommand,
       "nvflashUpdate": nvflashUpdate,
       "status": status,
       "portTypeStatusTable": portTypeStatusTable,
       "portTypeStatusEntry": portTypeStatusEntry,
       "portTypeStatusCardNumber": portTypeStatusCardNumber,
       "portTypeStatusChannelNumber": portTypeStatusChannelNumber,
       "portTypeStatusChannelType": portTypeStatusChannelType,
       "asyncChStatusTable": asyncChStatusTable,
       "asyncChStatusEntry": asyncChStatusEntry,
       "asyncChStatusCardNumber": asyncChStatusCardNumber,
       "asyncChStatusChannelNumber": asyncChStatusChannelNumber,
       "asyncChStatusEiaInputsRTSStatus": asyncChStatusEiaInputsRTSStatus,
       "asyncChStatusEiaInputsDTRStatus": asyncChStatusEiaInputsDTRStatus,
       "asyncChStatusEiaInputsUAStatus": asyncChStatusEiaInputsUAStatus,
       "asyncChStatusEiaInputsBUSYStatus": asyncChStatusEiaInputsBUSYStatus,
       "asyncChStatusEiaOutputsRIStatus": asyncChStatusEiaOutputsRIStatus,
       "asyncChStatusEiaOutputsRLSDStatus": asyncChStatusEiaOutputsRLSDStatus,
       "asyncChStatusEiaOutputsCTSStatus": asyncChStatusEiaOutputsCTSStatus,
       "asyncChStatusEiaOutputsDSRStatus": asyncChStatusEiaOutputsDSRStatus,
       "syncChStatusTable": syncChStatusTable,
       "syncChStatusEntry": syncChStatusEntry,
       "syncChStatusCardNumber": syncChStatusCardNumber,
       "syncChStatusChannelNumber": syncChStatusChannelNumber,
       "syncChStatusEiaInputsRTSStatus": syncChStatusEiaInputsRTSStatus,
       "syncChStatusEiaInputsDTRStatus": syncChStatusEiaInputsDTRStatus,
       "syncChStatusEiaInputsUAStatus": syncChStatusEiaInputsUAStatus,
       "syncChStatusEiaInputsBUSYStatus": syncChStatusEiaInputsBUSYStatus,
       "syncChStatusEiaOutputsRIStatus": syncChStatusEiaOutputsRIStatus,
       "syncChStatusEiaOutputsRLSDStatus": syncChStatusEiaOutputsRLSDStatus,
       "syncChStatusEiaOutputsCTSStatus": syncChStatusEiaOutputsCTSStatus,
       "syncChStatusEiaOutputsDSRStatus": syncChStatusEiaOutputsDSRStatus,
       "voiceChStatusTable": voiceChStatusTable,
       "voiceChStatusEntry": voiceChStatusEntry,
       "voiceChStatusCardNumber": voiceChStatusCardNumber,
       "voiceChStatusChannelNumber": voiceChStatusChannelNumber,
       "voiceChStatusInputLevel": voiceChStatusInputLevel,
       "voiceChStatusStatus": voiceChStatusStatus,
       "voiceChStatusPromID": voiceChStatusPromID,
       "voiceChStatusSoftwareRevision": voiceChStatusSoftwareRevision,
       "voiceChStatusTestMode": voiceChStatusTestMode,
       "voiceChStatusTestDSPResult": voiceChStatusTestDSPResult,
       "voiceChStatusTestDataRAMResult": voiceChStatusTestDataRAMResult,
       "voiceChStatusTestCodeRAMResult": voiceChStatusTestCodeRAMResult,
       "voiceChStatusTestAnalogHwResult": voiceChStatusTestAnalogHwResult,
       "voiceChStatusTestDeviceCfgResult": voiceChStatusTestDeviceCfgResult,
       "voiceChStatusFlashState": voiceChStatusFlashState,
       "voiceChStatusEPROMStatus": voiceChStatusEPROMStatus,
       "linkStatusTable": linkStatusTable,
       "linkStatusEntry": linkStatusEntry,
       "linkStatusCardNumber": linkStatusCardNumber,
       "linkStatusChannelNumber": linkStatusChannelNumber,
       "linkStatusLinkType": linkStatusLinkType,
       "linkStatusIntegralDevType": linkStatusIntegralDevType,
       "linkStatusIntegralDevSlotNumber": linkStatusIntegralDevSlotNumber,
       "linkStatusIntegralDeviceNumber": linkStatusIntegralDeviceNumber,
       "linkStatusStatus": linkStatusStatus,
       "linkStatusNodeNumber": linkStatusNodeNumber,
       "linkStatusRemoteChannelNumber": linkStatusRemoteChannelNumber,
       "linkStatusRemoteCardNumber": linkStatusRemoteCardNumber,
       "linkStatusEiaOutputsRTSStatus": linkStatusEiaOutputsRTSStatus,
       "linkStatusEiaOutputsDTRStatus": linkStatusEiaOutputsDTRStatus,
       "linkStatusEiaOutputsBUSYStatus": linkStatusEiaOutputsBUSYStatus,
       "linkStatusEiaOutputsUAStatus": linkStatusEiaOutputsUAStatus,
       "linkStatusEiaInputsRLSDStatus": linkStatusEiaInputsRLSDStatus,
       "linkStatusEiaInputsDSRStatus": linkStatusEiaInputsDSRStatus,
       "linkStatusEiaInputsRIStatus": linkStatusEiaInputsRIStatus,
       "linkStatusEiaInputsCTSStatus": linkStatusEiaInputsCTSStatus,
       "frameRelayLinkDLCIStatusTable": frameRelayLinkDLCIStatusTable,
       "frameRelayLinkDLCIStatusEntry": frameRelayLinkDLCIStatusEntry,
       "frameRelayLinkDLCIStatusCardNumber": frameRelayLinkDLCIStatusCardNumber,
       "frameRelayLinkDLCIStatusChannelNumber": frameRelayLinkDLCIStatusChannelNumber,
       "frameRelayLinkDLCIStatusDLCINumber": frameRelayLinkDLCIStatusDLCINumber,
       "frameRelayLinkDLCIStatusNumberOfDLCIs": frameRelayLinkDLCIStatusNumberOfDLCIs,
       "frameRelayLinkDLCIStatusConfOnMarathon": frameRelayLinkDLCIStatusConfOnMarathon,
       "frameRelayLinkDLCIStatusReportedByPBX": frameRelayLinkDLCIStatusReportedByPBX,
       "frameRelayLinkDLCIStatusActive": frameRelayLinkDLCIStatusActive,
       "frameRelayLinkDLCIStatusLinkStatus": frameRelayLinkDLCIStatusLinkStatus,
       "frameRelayLinkDLCIStatusUpConnectedNodeNumber": frameRelayLinkDLCIStatusUpConnectedNodeNumber,
       "frameRelayLinkDLCIStatusUpConnectedChannelNumber": frameRelayLinkDLCIStatusUpConnectedChannelNumber,
       "frameRelayLinkDLCIStatusUpConnectedCardNumber": frameRelayLinkDLCIStatusUpConnectedCardNumber,
       "frameRelayLinkDLCIStatusUpRemoteDLCINumber": frameRelayLinkDLCIStatusUpRemoteDLCINumber,
       "chConnectionStatusTable": chConnectionStatusTable,
       "chConnectionStatusEntry": chConnectionStatusEntry,
       "chConnectionStatusCardNumber": chConnectionStatusCardNumber,
       "chConnectionStatusChannelNumber": chConnectionStatusChannelNumber,
       "chConnectionStatusChannelStatus": chConnectionStatusChannelStatus,
       "chConnectionStatusConnectedToNode": chConnectionStatusConnectedToNode,
       "chConnectionStatusConnectedToChannel": chConnectionStatusConnectedToChannel,
       "chConnectionStatusConnectedToCard": chConnectionStatusConnectedToCard,
       "chConnectionStatusConnectedToInternalFacility": chConnectionStatusConnectedToInternalFacility,
       "remoteNodeStatusTable": remoteNodeStatusTable,
       "remoteNodeStatusEntry": remoteNodeStatusEntry,
       "remoteNodeStatusIndex": remoteNodeStatusIndex,
       "remoteNodeStatusName": remoteNodeStatusName,
       "remoteNodeStatusType": remoteNodeStatusType,
       "remoteNodeStatusNumber": remoteNodeStatusNumber,
       "classStatusTable": classStatusTable,
       "classStatusEntry": classStatusEntry,
       "classStatusCfgClassIndex": classStatusCfgClassIndex,
       "classStatusCfgClassNumber": classStatusCfgClassNumber,
       "classQueueStatusTable": classQueueStatusTable,
       "classQueueStatusEntry": classQueueStatusEntry,
       "classQueueStatusClassNum": classQueueStatusClassNum,
       "classQueueStatusChCount": classQueueStatusChCount,
       "classChannelStatusTable": classChannelStatusTable,
       "classChannelStatusEntry": classChannelStatusEntry,
       "classChannelStatusClassNum": classChannelStatusClassNum,
       "classQueueStatusChannelIndex": classQueueStatusChannelIndex,
       "classChannelStatusNode": classChannelStatusNode,
       "classChannelStatusChannel": classChannelStatusChannel,
       "classChannelStatusCard": classChannelStatusCard,
       "flashMemoryStatusTable": flashMemoryStatusTable,
       "flashMemoryStatusEntry": flashMemoryStatusEntry,
       "flashMemoryStatusFlashNumber": flashMemoryStatusFlashNumber,
       "flashMemoryStatusFileHeaderSize": flashMemoryStatusFileHeaderSize,
       "flashMemoryStatusFileType": flashMemoryStatusFileType,
       "flashMemoryStatusMarathonImageSize": flashMemoryStatusMarathonImageSize,
       "flashMemoryStatusCreationHours": flashMemoryStatusCreationHours,
       "flashMemoryStatusCreationMinutes": flashMemoryStatusCreationMinutes,
       "flashMemoryStatusCreationSeconds": flashMemoryStatusCreationSeconds,
       "flashMemoryStatusCreationYear": flashMemoryStatusCreationYear,
       "flashMemoryStatusCreationMonth": flashMemoryStatusCreationMonth,
       "flashMemoryStatusCreationDay": flashMemoryStatusCreationDay,
       "flashMemoryStatusImageChecksum": flashMemoryStatusImageChecksum,
       "flashMemoryStatusPromID": flashMemoryStatusPromID,
       "chForceConnStatusTable": chForceConnStatusTable,
       "chForceConnStatusEntry": chForceConnStatusEntry,
       "chForceConnStatusCardNumber": chForceConnStatusCardNumber,
       "chForceConnStatusChannelNumber": chForceConnStatusChannelNumber,
       "chForceConnStatusNodeNumber": chForceConnStatusNodeNumber,
       "chForceConnStatusToNodeNumber": chForceConnStatusToNodeNumber,
       "chForceConnStatusToCardNumber": chForceConnStatusToCardNumber,
       "chForceConnStatusToChannelNumber": chForceConnStatusToChannelNumber,
       "statistics": statistics,
       "statistics-configuration": statistics_configuration,
       "sysPeriodicStatisticsReportGroup": sysPeriodicStatisticsReportGroup,
       "sysPeriodicStatisticsReportInterval": sysPeriodicStatisticsReportInterval,
       "sysReportDestination": sysReportDestination,
       "sysRemoteLogNodeName": sysRemoteLogNodeName,
       "lastPeriodicStatisticsTimeGroup": lastPeriodicStatisticsTimeGroup,
       "lastPeriodicStatisticsTimeMonth": lastPeriodicStatisticsTimeMonth,
       "lastPeriodicStatisticsTimeDay": lastPeriodicStatisticsTimeDay,
       "lastPeriodicStatisticsTimeHours": lastPeriodicStatisticsTimeHours,
       "lastPeriodicStatisticsTimeMinutes": lastPeriodicStatisticsTimeMinutes,
       "lastPeriodicStatisticsTimeSeconds": lastPeriodicStatisticsTimeSeconds,
       "switchStatistics": switchStatistics,
       "statistics-periodic": statistics_periodic,
       "chPeriodicStatisticsTable": chPeriodicStatisticsTable,
       "chPeriodicStatisticsEntry": chPeriodicStatisticsEntry,
       "chPeriodicStatisticsCardNumber": chPeriodicStatisticsCardNumber,
       "chPeriodicStatisticsChannelNumber": chPeriodicStatisticsChannelNumber,
       "chPeriodicStatisticsMonth": chPeriodicStatisticsMonth,
       "chPeriodicStatisticsDay": chPeriodicStatisticsDay,
       "chPeriodicStatisticsHours": chPeriodicStatisticsHours,
       "chPeriodicStatisticsMinutes": chPeriodicStatisticsMinutes,
       "chPeriodicStatisticsSeconds": chPeriodicStatisticsSeconds,
       "chPeriodicStatisticsBuffUtilization": chPeriodicStatisticsBuffUtilization,
       "chPeriodicStatisticsChannelBusiedOut": chPeriodicStatisticsChannelBusiedOut,
       "chPeriodicStatisticsChannelInFlowControl": chPeriodicStatisticsChannelInFlowControl,
       "chVPeriodicStatisticsTable": chVPeriodicStatisticsTable,
       "chVPeriodicStatisticsEntry": chVPeriodicStatisticsEntry,
       "chVPeriodicStatisticsCardNumber": chVPeriodicStatisticsCardNumber,
       "chVPeriodicStatisticsChannelNumber": chVPeriodicStatisticsChannelNumber,
       "chVPeriodicStatisticsMonth": chVPeriodicStatisticsMonth,
       "chVPeriodicStatisticsDay": chVPeriodicStatisticsDay,
       "chVPeriodicStatisticsHours": chVPeriodicStatisticsHours,
       "chVPeriodicStatisticsMinutes": chVPeriodicStatisticsMinutes,
       "chVPeriodicStatisticsSeconds": chVPeriodicStatisticsSeconds,
       "chVPeriodicStatisticsConnectTime": chVPeriodicStatisticsConnectTime,
       "chVPeriodicStatisticsTotalCalls": chVPeriodicStatisticsTotalCalls,
       "chVPeriodicStatisticsAvgCallDuration": chVPeriodicStatisticsAvgCallDuration,
       "chVPeriodicStatisticsBusyOutTime": chVPeriodicStatisticsBusyOutTime,
       "chVPeriodicStatisticsNumOfCallAttempts": chVPeriodicStatisticsNumOfCallAttempts,
       "chVPeriodicStatisticsDiscardedFrameCounts": chVPeriodicStatisticsDiscardedFrameCounts,
       "chVPeriodicStatisticsTimeInFaxMode": chVPeriodicStatisticsTimeInFaxMode,
       "chVPeriodicStatisticsPercentInFaxMode": chVPeriodicStatisticsPercentInFaxMode,
       "linkPeriodicStatisticsTable": linkPeriodicStatisticsTable,
       "linkPeriodicStatisticsEntry": linkPeriodicStatisticsEntry,
       "linkPeriodicStatisticsCardNumber": linkPeriodicStatisticsCardNumber,
       "linkPeriodicStatisticsChannelNumber": linkPeriodicStatisticsChannelNumber,
       "linkPeriodicStatisticsMonth": linkPeriodicStatisticsMonth,
       "linkPeriodicStatisticsDay": linkPeriodicStatisticsDay,
       "linkPeriodicStatisticsHours": linkPeriodicStatisticsHours,
       "linkPeriodicStatisticsMinutes": linkPeriodicStatisticsMinutes,
       "linkPeriodicStatisticsSeconds": linkPeriodicStatisticsSeconds,
       "linkPeriodicStatisticsLinkType": linkPeriodicStatisticsLinkType,
       "linkPeriodicStatisticsTxFrames": linkPeriodicStatisticsTxFrames,
       "linkPeriodicStatisticsRxFrames": linkPeriodicStatisticsRxFrames,
       "linkPeriodicStatisticsLocCompositeUtil": linkPeriodicStatisticsLocCompositeUtil,
       "linkPeriodicStatisticsRemCompositeUtil": linkPeriodicStatisticsRemCompositeUtil,
       "linkPeriodicStatisticsLocBufferUtil": linkPeriodicStatisticsLocBufferUtil,
       "linkPeriodicStatisticsRemBufferUtil": linkPeriodicStatisticsRemBufferUtil,
       "linkPeriodicStatisticsLocRetransmits": linkPeriodicStatisticsLocRetransmits,
       "linkPeriodicStatisticsRemRetransmits": linkPeriodicStatisticsRemRetransmits,
       "linkPeriodicStatisticsLocLineAlarms": linkPeriodicStatisticsLocLineAlarms,
       "linkPeriodicStatisticsRemLineAlarms": linkPeriodicStatisticsRemLineAlarms,
       "linkPeriodicStatisticsLocTimeInSysFlowCtrl": linkPeriodicStatisticsLocTimeInSysFlowCtrl,
       "linkPeriodicStatisticsRemTimeInSysFlowCtrl": linkPeriodicStatisticsRemTimeInSysFlowCtrl,
       "linkPeriodicStatisticsLocTimeInSyncLossOrX21Connect": linkPeriodicStatisticsLocTimeInSyncLossOrX21Connect,
       "linkPeriodicStatisticsRemTimeInSyncLoss": linkPeriodicStatisticsRemTimeInSyncLoss,
       "linkPeriodicStatisticsLocTimeInCarrierLoss": linkPeriodicStatisticsLocTimeInCarrierLoss,
       "linkPeriodicStatisticsRemTimeInCarrierLoss": linkPeriodicStatisticsRemTimeInCarrierLoss,
       "linkFRPeriodicStatisticsTable": linkFRPeriodicStatisticsTable,
       "linkFRPeriodicStatisticsEntry": linkFRPeriodicStatisticsEntry,
       "linkFRPeriodicStatisticsCardNumber": linkFRPeriodicStatisticsCardNumber,
       "linkFRPeriodicStatisticsChannelNumber": linkFRPeriodicStatisticsChannelNumber,
       "linkFRPeriodicStatisticsMonth": linkFRPeriodicStatisticsMonth,
       "linkFRPeriodicStatisticsDay": linkFRPeriodicStatisticsDay,
       "linkFRPeriodicStatisticsHours": linkFRPeriodicStatisticsHours,
       "linkFRPeriodicStatisticsMinutes": linkFRPeriodicStatisticsMinutes,
       "linkFRPeriodicStatisticsSeconds": linkFRPeriodicStatisticsSeconds,
       "linkFRPeriodicStatisticsCRCErrs": linkFRPeriodicStatisticsCRCErrs,
       "linkFRPeriodicStatisticsLostStatusMsgCounts": linkFRPeriodicStatisticsLostStatusMsgCounts,
       "linkFRPeriodicStatisticsStatusMsgProtocolErrs": linkFRPeriodicStatisticsStatusMsgProtocolErrs,
       "linkFRPeriodicStatisticsNetworkResets": linkFRPeriodicStatisticsNetworkResets,
       "linkFRPeriodicStatisticsLinkResets": linkFRPeriodicStatisticsLinkResets,
       "linkFRPeriodicStatisticsNumOfDLCIs": linkFRPeriodicStatisticsNumOfDLCIs,
       "linkFRDLCIPeriodicStatisticsTable": linkFRDLCIPeriodicStatisticsTable,
       "linkFRDLCIPeriodicStatisticsEntry": linkFRDLCIPeriodicStatisticsEntry,
       "linkFRDLCIPeriodicStatisticsCardNumber": linkFRDLCIPeriodicStatisticsCardNumber,
       "linkFRDLCIPeriodicStatisticsChannelNumber": linkFRDLCIPeriodicStatisticsChannelNumber,
       "linkFRDLCIPeriodicStatisticsDLCINumber": linkFRDLCIPeriodicStatisticsDLCINumber,
       "linkFRDLCIPeriodicStatisticsMonth": linkFRDLCIPeriodicStatisticsMonth,
       "linkFRDLCIPeriodicStatisticsDay": linkFRDLCIPeriodicStatisticsDay,
       "linkFRDLCIPeriodicStatisticsHours": linkFRDLCIPeriodicStatisticsHours,
       "linkFRDLCIPeriodicStatisticsMinutes": linkFRDLCIPeriodicStatisticsMinutes,
       "linkFRDLCIPeriodicStatisticsSeconds": linkFRDLCIPeriodicStatisticsSeconds,
       "linkFRDLCIPeriodicStatisticsTxCharacters": linkFRDLCIPeriodicStatisticsTxCharacters,
       "linkFRDLCIPeriodicStatisticsRxCharacters": linkFRDLCIPeriodicStatisticsRxCharacters,
       "linkFRDLCIPeriodicStatisticsTxFrames": linkFRDLCIPeriodicStatisticsTxFrames,
       "linkFRDLCIPeriodicStatisticsRxFrames": linkFRDLCIPeriodicStatisticsRxFrames,
       "linkFRDLCIPeriodicStatisticsTimeActive": linkFRDLCIPeriodicStatisticsTimeActive,
       "linkFRDLCIPeriodicStatisticsTimeCongestedForward": linkFRDLCIPeriodicStatisticsTimeCongestedForward,
       "linkFRDLCIPeriodicStatisticsTimeCongestedBackward": linkFRDLCIPeriodicStatisticsTimeCongestedBackward,
       "swPeriodicStatisticsNumOfCurrentConnects": swPeriodicStatisticsNumOfCurrentConnects,
       "swPeriodicStatisticsTable": swPeriodicStatisticsTable,
       "swPeriodicStatisticsEntry": swPeriodicStatisticsEntry,
       "swPeriodicStatisticsClassNumber": swPeriodicStatisticsClassNumber,
       "swPeriodicStatisticsMonth": swPeriodicStatisticsMonth,
       "swPeriodicStatisticsDay": swPeriodicStatisticsDay,
       "swPeriodicStatisticsHours": swPeriodicStatisticsHours,
       "swPeriodicStatisticsMinutes": swPeriodicStatisticsMinutes,
       "swPeriodicStatisticsSeconds": swPeriodicStatisticsSeconds,
       "swPeriodicStatisticsNumOfSuccessfulConnects": swPeriodicStatisticsNumOfSuccessfulConnects,
       "swPeriodicStatisticsNumOfUnsuccessfulAttempts": swPeriodicStatisticsNumOfUnsuccessfulAttempts,
       "swPeriodicStatisticsMaxNumInQueue": swPeriodicStatisticsMaxNumInQueue,
       "linkFRAccLnkPeriodicStatisticsTable": linkFRAccLnkPeriodicStatisticsTable,
       "linkFRAccLnkPeriodicStatisticsEntry": linkFRAccLnkPeriodicStatisticsEntry,
       "linkFRAccLnkPeriodicStatisticsCardNumber": linkFRAccLnkPeriodicStatisticsCardNumber,
       "linkFRAccLnkPeriodicStatisticsChannelNumber": linkFRAccLnkPeriodicStatisticsChannelNumber,
       "linkFRAccLnkPeriodicStatisticsMonth": linkFRAccLnkPeriodicStatisticsMonth,
       "linkFRAccLnkPeriodicStatisticsDay": linkFRAccLnkPeriodicStatisticsDay,
       "linkFRAccLnkPeriodicStatisticsHours": linkFRAccLnkPeriodicStatisticsHours,
       "linkFRAccLnkPeriodicStatisticsMinutes": linkFRAccLnkPeriodicStatisticsMinutes,
       "linkFRAccLnkPeriodicStatisticsSeconds": linkFRAccLnkPeriodicStatisticsSeconds,
       "linkFRAccLnkPeriodicStatisticsLocalCompositeUtilization": linkFRAccLnkPeriodicStatisticsLocalCompositeUtilization,
       "linkFRAccLnkPeriodicStatisticsLocalBufferUtilization": linkFRAccLnkPeriodicStatisticsLocalBufferUtilization,
       "linkFRAccLnkPeriodicStatisticsLocalLineAlarms": linkFRAccLnkPeriodicStatisticsLocalLineAlarms,
       "linkFRAccLnkPeriodicStatisticsLocalSecInSysFlowControl": linkFRAccLnkPeriodicStatisticsLocalSecInSysFlowControl,
       "linkFRAccLnkPeriodicStatisticsLocalSecInSyncLoss": linkFRAccLnkPeriodicStatisticsLocalSecInSyncLoss,
       "linkFRAccLnkPeriodicStatisticsLocalSecInCarrierLoss": linkFRAccLnkPeriodicStatisticsLocalSecInCarrierLoss,
       "statistics-accumulated": statistics_accumulated,
       "chAccumStatisticsTable": chAccumStatisticsTable,
       "chAccumStatisticsEntry": chAccumStatisticsEntry,
       "chAccumStatisticsCardNumber": chAccumStatisticsCardNumber,
       "chAccumStatisticsChannelNumber": chAccumStatisticsChannelNumber,
       "chAccumStatisticsMonth": chAccumStatisticsMonth,
       "chAccumStatisticsDay": chAccumStatisticsDay,
       "chAccumStatisticsHours": chAccumStatisticsHours,
       "chAccumStatisticsMinutes": chAccumStatisticsMinutes,
       "chAccumStatisticsSeconds": chAccumStatisticsSeconds,
       "chAccumStatisticsBuffUtilization": chAccumStatisticsBuffUtilization,
       "chAccumStatisticsChannelBusiedOut": chAccumStatisticsChannelBusiedOut,
       "chAccumStatisticsChannelInFlowControl": chAccumStatisticsChannelInFlowControl,
       "chVAccumStatisticsTable": chVAccumStatisticsTable,
       "chVAccumStatisticsEntry": chVAccumStatisticsEntry,
       "chVAccumStatisticsCardNumber": chVAccumStatisticsCardNumber,
       "chVAccumStatisticsChannelNumber": chVAccumStatisticsChannelNumber,
       "chVAccumStatisticsMonth": chVAccumStatisticsMonth,
       "chVAccumStatisticsDay": chVAccumStatisticsDay,
       "chVAccumStatisticsHours": chVAccumStatisticsHours,
       "chVAccumStatisticsMinutes": chVAccumStatisticsMinutes,
       "chVAccumStatisticsSeconds": chVAccumStatisticsSeconds,
       "chVAccumStatisticsConnectTime": chVAccumStatisticsConnectTime,
       "chVAccumStatisticsTotalCalls": chVAccumStatisticsTotalCalls,
       "chVAccumStatisticsAvgCallDuration": chVAccumStatisticsAvgCallDuration,
       "chVAccumStatisticsBusyOutTime": chVAccumStatisticsBusyOutTime,
       "chVAccumStatisticsNumOfCallAttempts": chVAccumStatisticsNumOfCallAttempts,
       "chVAccumStatisticsDiscardedFrameCounts": chVAccumStatisticsDiscardedFrameCounts,
       "chVAccumStatisticsTimeInFaxMode": chVAccumStatisticsTimeInFaxMode,
       "chVAccumStatisticsPercentInFaxMode": chVAccumStatisticsPercentInFaxMode,
       "linkAccumStatisticsTable": linkAccumStatisticsTable,
       "linkAccumStatisticsEntry": linkAccumStatisticsEntry,
       "linkAccumStatisticsCardNumber": linkAccumStatisticsCardNumber,
       "linkAccumStatisticsChannelNumber": linkAccumStatisticsChannelNumber,
       "linkAccumStatisticsMonth": linkAccumStatisticsMonth,
       "linkAccumStatisticsDay": linkAccumStatisticsDay,
       "linkAccumStatisticsHours": linkAccumStatisticsHours,
       "linkAccumStatisticsMinutes": linkAccumStatisticsMinutes,
       "linkAccumStatisticsSeconds": linkAccumStatisticsSeconds,
       "linkAccumStatisticsLinkType": linkAccumStatisticsLinkType,
       "linkAccumStatisticsTxFrames": linkAccumStatisticsTxFrames,
       "linkAccumStatisticsRxFrames": linkAccumStatisticsRxFrames,
       "linkAccumStatisticsLocCompositeUtil": linkAccumStatisticsLocCompositeUtil,
       "linkAccumStatisticsRemCompositeUtil": linkAccumStatisticsRemCompositeUtil,
       "linkAccumStatisticsLocBufferUtil": linkAccumStatisticsLocBufferUtil,
       "linkAccumStatisticsRemBufferUtil": linkAccumStatisticsRemBufferUtil,
       "linkAccumStatisticsLocRetransmits": linkAccumStatisticsLocRetransmits,
       "linkAccumStatisticsRemRetransmits": linkAccumStatisticsRemRetransmits,
       "linkAccumStatisticsLocLineAlarms": linkAccumStatisticsLocLineAlarms,
       "linkAccumStatisticsRemLineAlarms": linkAccumStatisticsRemLineAlarms,
       "linkAccumStatisticsLocTimeInSysFlowCtrl": linkAccumStatisticsLocTimeInSysFlowCtrl,
       "linkAccumStatisticsRemTimeInSysFlowCtrl": linkAccumStatisticsRemTimeInSysFlowCtrl,
       "linkAccumStatisticsLocTimeInSyncLossOrX21Connect": linkAccumStatisticsLocTimeInSyncLossOrX21Connect,
       "linkAccumStatisticsRemTimeInSyncLoss": linkAccumStatisticsRemTimeInSyncLoss,
       "linkAccumStatisticsLocTimeInCarrierLoss": linkAccumStatisticsLocTimeInCarrierLoss,
       "linkAccumStatisticsRemTimeInCarrierLoss": linkAccumStatisticsRemTimeInCarrierLoss,
       "linkFRAccumStatisticsTable": linkFRAccumStatisticsTable,
       "linkFRAccumStatisticsEntry": linkFRAccumStatisticsEntry,
       "linkFRAccumStatisticsCardNumber": linkFRAccumStatisticsCardNumber,
       "linkFRAccumStatisticsChannelNumber": linkFRAccumStatisticsChannelNumber,
       "linkFRAccumStatisticsMonth": linkFRAccumStatisticsMonth,
       "linkFRAccumStatisticsDay": linkFRAccumStatisticsDay,
       "linkFRAccumStatisticsHours": linkFRAccumStatisticsHours,
       "linkFRAccumStatisticsMinutes": linkFRAccumStatisticsMinutes,
       "linkFRAccumStatisticsSeconds": linkFRAccumStatisticsSeconds,
       "linkFRAccumStatisticsCRCErrs": linkFRAccumStatisticsCRCErrs,
       "linkFRAccumStatisticsLostStatusMsgCounts": linkFRAccumStatisticsLostStatusMsgCounts,
       "linkFRAccumStatisticsStatusMsgProtocolErrs": linkFRAccumStatisticsStatusMsgProtocolErrs,
       "linkFRAccumStatisticsNetworkResets": linkFRAccumStatisticsNetworkResets,
       "linkFRAccumStatisticsLinkResets": linkFRAccumStatisticsLinkResets,
       "linkFRAccumStatisticsNumOfDLCIs": linkFRAccumStatisticsNumOfDLCIs,
       "linkFRDLCIAccumStatisticsTable": linkFRDLCIAccumStatisticsTable,
       "linkFRDLCIAccumStatisticsEntry": linkFRDLCIAccumStatisticsEntry,
       "linkFRDLCIAccumStatisticsCardNumber": linkFRDLCIAccumStatisticsCardNumber,
       "linkFRDLCIAccumStatisticsChannelNumber": linkFRDLCIAccumStatisticsChannelNumber,
       "linkFRDLCIAccumStatisticsDLCINumber": linkFRDLCIAccumStatisticsDLCINumber,
       "linkFRDLCIAccumStatisticsMonth": linkFRDLCIAccumStatisticsMonth,
       "linkFRDLCIAccumStatisticsDay": linkFRDLCIAccumStatisticsDay,
       "linkFRDLCIAccumStatisticsHours": linkFRDLCIAccumStatisticsHours,
       "linkFRDLCIAccumStatisticsMinutes": linkFRDLCIAccumStatisticsMinutes,
       "linkFRDLCIAccumStatisticsSeconds": linkFRDLCIAccumStatisticsSeconds,
       "linkFRDLCIAccumStatisticsTxCharacters": linkFRDLCIAccumStatisticsTxCharacters,
       "linkFRDLCIAccumStatisticsRxCharacters": linkFRDLCIAccumStatisticsRxCharacters,
       "linkFRDLCIAccumStatisticsTxFrames": linkFRDLCIAccumStatisticsTxFrames,
       "linkFRDLCIAccumStatisticsRxFrames": linkFRDLCIAccumStatisticsRxFrames,
       "linkFRDLCIAccumStatisticsTimeActive": linkFRDLCIAccumStatisticsTimeActive,
       "linkFRDLCIAccumStatisticsTimeCongestedForward": linkFRDLCIAccumStatisticsTimeCongestedForward,
       "linkFRDLCIAccumStatisticsTimeCongestedBackward": linkFRDLCIAccumStatisticsTimeCongestedBackward,
       "swAccumStatisticsNumOfCurrentConnects": swAccumStatisticsNumOfCurrentConnects,
       "swAccumStatisticsTable": swAccumStatisticsTable,
       "swAccumStatisticsEntry": swAccumStatisticsEntry,
       "swAccumStatisticsClassNumber": swAccumStatisticsClassNumber,
       "swAccumStatisticsMonth": swAccumStatisticsMonth,
       "swAccumStatisticsDay": swAccumStatisticsDay,
       "swAccumStatisticsHours": swAccumStatisticsHours,
       "swAccumStatisticsMinutes": swAccumStatisticsMinutes,
       "swAccumStatisticsSeconds": swAccumStatisticsSeconds,
       "swAccumStatisticsNumOfSuccessfulConnects": swAccumStatisticsNumOfSuccessfulConnects,
       "swAccumStatisticsNumOfUnsuccessfulAttempts": swAccumStatisticsNumOfUnsuccessfulAttempts,
       "swAccumStatisticsMaxNumInQueue": swAccumStatisticsMaxNumInQueue,
       "linkFRAccLnkAccumStatisticsTable": linkFRAccLnkAccumStatisticsTable,
       "linkFRAccLnkAccumStatisticsEntry": linkFRAccLnkAccumStatisticsEntry,
       "linkFRAccLnkAccumStatisticsCardNumber": linkFRAccLnkAccumStatisticsCardNumber,
       "linkFRAccLnkAccumStatisticsChannelNumber": linkFRAccLnkAccumStatisticsChannelNumber,
       "linkFRAccLnkAccumStatisticsMonth": linkFRAccLnkAccumStatisticsMonth,
       "linkFRAccLnkAccumStatisticsDay": linkFRAccLnkAccumStatisticsDay,
       "linkFRAccLnkAccumStatisticsHours": linkFRAccLnkAccumStatisticsHours,
       "linkFRAccLnkAccumStatisticsMinutes": linkFRAccLnkAccumStatisticsMinutes,
       "linkFRAccLnkAccumStatisticsSeconds": linkFRAccLnkAccumStatisticsSeconds,
       "linkFRAccLnkAccumStatisticsLocalCompositeUtilization": linkFRAccLnkAccumStatisticsLocalCompositeUtilization,
       "linkFRAccLnkAccumStatisticsLocalBufferUtilization": linkFRAccLnkAccumStatisticsLocalBufferUtilization,
       "linkFRAccLnkAccumStatisticsLocalLineAlarms": linkFRAccLnkAccumStatisticsLocalLineAlarms,
       "linkFRAccLnkAccumStatisticsLocalSecInSysFlowControl": linkFRAccLnkAccumStatisticsLocalSecInSysFlowControl,
       "linkFRAccLnkAccumStatisticsLocalSecInSyncLoss": linkFRAccLnkAccumStatisticsLocalSecInSyncLoss,
       "linkFRAccLnkAccumStatisticsLocalSecInCarrierLoss": linkFRAccLnkAccumStatisticsLocalSecInCarrierLoss}
)
