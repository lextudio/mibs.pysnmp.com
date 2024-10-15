# SNMP MIB module (CPQUPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQUPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:47 2024
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
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

_CpqUps_ObjectIdentity = ObjectIdentity
cpqUps = _CpqUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 12)
)
_CpqUpsMibRev_ObjectIdentity = ObjectIdentity
cpqUpsMibRev = _CpqUpsMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 12, 1)
)


class _CpqUpsMibRevMajor_Type(Integer32):
    """Custom type cpqUpsMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqUpsMibRevMajor_Type.__name__ = "Integer32"
_CpqUpsMibRevMajor_Object = MibScalar
cpqUpsMibRevMajor = _CpqUpsMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 1, 1),
    _CpqUpsMibRevMajor_Type()
)
cpqUpsMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsMibRevMajor.setStatus("mandatory")


class _CpqUpsMibRevMinor_Type(Integer32):
    """Custom type cpqUpsMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqUpsMibRevMinor_Type.__name__ = "Integer32"
_CpqUpsMibRevMinor_Object = MibScalar
cpqUpsMibRevMinor = _CpqUpsMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 1, 2),
    _CpqUpsMibRevMinor_Type()
)
cpqUpsMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsMibRevMinor.setStatus("mandatory")


class _CpqUpsMibCondition_Type(Integer32):
    """Custom type cpqUpsMibCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqUpsMibCondition_Type.__name__ = "Integer32"
_CpqUpsMibCondition_Object = MibScalar
cpqUpsMibCondition = _CpqUpsMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 1, 3),
    _CpqUpsMibCondition_Type()
)
cpqUpsMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsMibCondition.setStatus("mandatory")
_CpqUpsComponent_ObjectIdentity = ObjectIdentity
cpqUpsComponent = _CpqUpsComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 12, 2)
)
_CpqUpsInterface_ObjectIdentity = ObjectIdentity
cpqUpsInterface = _CpqUpsInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 1)
)
_CpqUpsOsCommon_ObjectIdentity = ObjectIdentity
cpqUpsOsCommon = _CpqUpsOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 1, 4)
)


class _CpqUpsOsCommonPollFreq_Type(Integer32):
    """Custom type cpqUpsOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqUpsOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqUpsOsCommonPollFreq_Object = MibScalar
cpqUpsOsCommonPollFreq = _CpqUpsOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 1, 4, 1),
    _CpqUpsOsCommonPollFreq_Type()
)
cpqUpsOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqUpsOsCommonPollFreq.setStatus("mandatory")
_CpqUpsOsCommonModuleTable_Object = MibTable
cpqUpsOsCommonModuleTable = _CpqUpsOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqUpsOsCommonModuleTable.setStatus("mandatory")
_CpqUpsOsCommonModuleEntry_Object = MibTableRow
cpqUpsOsCommonModuleEntry = _CpqUpsOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 1, 4, 2, 1)
)
cpqUpsOsCommonModuleEntry.setIndexNames(
    (0, "CPQUPS-MIB", "cpqUpsOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqUpsOsCommonModuleEntry.setStatus("mandatory")


class _CpqUpsOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqUpsOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqUpsOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqUpsOsCommonModuleIndex_Object = MibTableColumn
cpqUpsOsCommonModuleIndex = _CpqUpsOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 1, 4, 2, 1, 1),
    _CpqUpsOsCommonModuleIndex_Type()
)
cpqUpsOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsOsCommonModuleIndex.setStatus("mandatory")


class _CpqUpsOsCommonModuleName_Type(DisplayString):
    """Custom type cpqUpsOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqUpsOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqUpsOsCommonModuleName_Object = MibTableColumn
cpqUpsOsCommonModuleName = _CpqUpsOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 1, 4, 2, 1, 2),
    _CpqUpsOsCommonModuleName_Type()
)
cpqUpsOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsOsCommonModuleName.setStatus("mandatory")


class _CpqUpsOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqUpsOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqUpsOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqUpsOsCommonModuleVersion_Object = MibTableColumn
cpqUpsOsCommonModuleVersion = _CpqUpsOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 1, 4, 2, 1, 3),
    _CpqUpsOsCommonModuleVersion_Type()
)
cpqUpsOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsOsCommonModuleVersion.setStatus("mandatory")


class _CpqUpsOsCommonModuleDate_Type(OctetString):
    """Custom type cpqUpsOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqUpsOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqUpsOsCommonModuleDate_Object = MibTableColumn
cpqUpsOsCommonModuleDate = _CpqUpsOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 1, 4, 2, 1, 4),
    _CpqUpsOsCommonModuleDate_Type()
)
cpqUpsOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsOsCommonModuleDate.setStatus("mandatory")


class _CpqUpsOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqUpsOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqUpsOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqUpsOsCommonModulePurpose_Object = MibTableColumn
cpqUpsOsCommonModulePurpose = _CpqUpsOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 1, 4, 2, 1, 5),
    _CpqUpsOsCommonModulePurpose_Type()
)
cpqUpsOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsOsCommonModulePurpose.setStatus("mandatory")
_CpqUpsBasic_ObjectIdentity = ObjectIdentity
cpqUpsBasic = _CpqUpsBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 2)
)


class _CpqUpsLineStatus_Type(Integer32):
    """Custom type cpqUpsLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqUpsLineStatus_Type.__name__ = "Integer32"
_CpqUpsLineStatus_Object = MibScalar
cpqUpsLineStatus = _CpqUpsLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 2, 1),
    _CpqUpsLineStatus_Type()
)
cpqUpsLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsLineStatus.setStatus("mandatory")


class _CpqUpsName_Type(DisplayString):
    """Custom type cpqUpsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CpqUpsName_Type.__name__ = "DisplayString"
_CpqUpsName_Object = MibScalar
cpqUpsName = _CpqUpsName_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 2, 2),
    _CpqUpsName_Type()
)
cpqUpsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsName.setStatus("mandatory")
_CpqUpsEstimatedBatteryLife_Type = Integer32
_CpqUpsEstimatedBatteryLife_Object = MibScalar
cpqUpsEstimatedBatteryLife = _CpqUpsEstimatedBatteryLife_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 2, 3),
    _CpqUpsEstimatedBatteryLife_Type()
)
cpqUpsEstimatedBatteryLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsEstimatedBatteryLife.setStatus("mandatory")
_CpqUpsAutoShutdownDelay_Type = Integer32
_CpqUpsAutoShutdownDelay_Object = MibScalar
cpqUpsAutoShutdownDelay = _CpqUpsAutoShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 2, 4),
    _CpqUpsAutoShutdownDelay_Type()
)
cpqUpsAutoShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqUpsAutoShutdownDelay.setStatus("mandatory")


class _CpqUpsLaunchCommand_Type(OctetString):
    """Custom type cpqUpsLaunchCommand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_CpqUpsLaunchCommand_Type.__name__ = "OctetString"
_CpqUpsLaunchCommand_Object = MibScalar
cpqUpsLaunchCommand = _CpqUpsLaunchCommand_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 2, 5),
    _CpqUpsLaunchCommand_Type()
)
cpqUpsLaunchCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsLaunchCommand.setStatus("mandatory")


class _CpqUpsAlarm_Type(DisplayString):
    """Custom type cpqUpsAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_CpqUpsAlarm_Type.__name__ = "DisplayString"
_CpqUpsAlarm_Object = MibScalar
cpqUpsAlarm = _CpqUpsAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 2, 6),
    _CpqUpsAlarm_Type()
)
cpqUpsAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqUpsAlarm.setStatus("mandatory")
_CpqUpsFamily_ObjectIdentity = ObjectIdentity
cpqUpsFamily = _CpqUpsFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 3)
)
_CpqUpsMemberTable_Object = MibTable
cpqUpsMemberTable = _CpqUpsMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpqUpsMemberTable.setStatus("mandatory")
_CpqUpsMemberEntry_Object = MibTableRow
cpqUpsMemberEntry = _CpqUpsMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 3, 1, 1)
)
cpqUpsMemberEntry.setIndexNames(
    (0, "CPQUPS-MIB", "cpqUpsMemberIndex"),
)
if mibBuilder.loadTexts:
    cpqUpsMemberEntry.setStatus("mandatory")


class _CpqUpsMemberIndex_Type(Integer32):
    """Custom type cpqUpsMemberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CpqUpsMemberIndex_Type.__name__ = "Integer32"
_CpqUpsMemberIndex_Object = MibTableColumn
cpqUpsMemberIndex = _CpqUpsMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 3, 1, 1, 1),
    _CpqUpsMemberIndex_Type()
)
cpqUpsMemberIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqUpsMemberIndex.setStatus("mandatory")


class _CpqUpsMemberName_Type(DisplayString):
    """Custom type cpqUpsMemberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqUpsMemberName_Type.__name__ = "DisplayString"
_CpqUpsMemberName_Object = MibTableColumn
cpqUpsMemberName = _CpqUpsMemberName_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 3, 1, 1, 2),
    _CpqUpsMemberName_Type()
)
cpqUpsMemberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqUpsMemberName.setStatus("mandatory")


class _CpqUpsMemberCommunityStr_Type(DisplayString):
    """Custom type cpqUpsMemberCommunityStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqUpsMemberCommunityStr_Type.__name__ = "DisplayString"
_CpqUpsMemberCommunityStr_Object = MibTableColumn
cpqUpsMemberCommunityStr = _CpqUpsMemberCommunityStr_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 3, 1, 1, 3),
    _CpqUpsMemberCommunityStr_Type()
)
cpqUpsMemberCommunityStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqUpsMemberCommunityStr.setStatus("mandatory")


class _CpqUpsAddMemberName_Type(DisplayString):
    """Custom type cpqUpsAddMemberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqUpsAddMemberName_Type.__name__ = "DisplayString"
_CpqUpsAddMemberName_Object = MibScalar
cpqUpsAddMemberName = _CpqUpsAddMemberName_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 3, 2),
    _CpqUpsAddMemberName_Type()
)
cpqUpsAddMemberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqUpsAddMemberName.setStatus("mandatory")


class _CpqUpsAddMemberCommunityStr_Type(DisplayString):
    """Custom type cpqUpsAddMemberCommunityStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqUpsAddMemberCommunityStr_Type.__name__ = "DisplayString"
_CpqUpsAddMemberCommunityStr_Object = MibScalar
cpqUpsAddMemberCommunityStr = _CpqUpsAddMemberCommunityStr_Object(
    (1, 3, 6, 1, 4, 1, 232, 12, 2, 3, 3),
    _CpqUpsAddMemberCommunityStr_Type()
)
cpqUpsAddMemberCommunityStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqUpsAddMemberCommunityStr.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqUpsLineFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12001)
)
cpqUpsLineFailed.setObjects(
    ("CPQUPS-MIB", "cpqUpsEstimatedBatteryLife")
)
if mibBuilder.loadTexts:
    cpqUpsLineFailed.setStatus(
        ""
    )

cpqUpsLineOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12002)
)
if mibBuilder.loadTexts:
    cpqUpsLineOk.setStatus(
        ""
    )

cpqUpsShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12003)
)
if mibBuilder.loadTexts:
    cpqUpsShutdown.setStatus(
        ""
    )

cpqUpsConfirmation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12004)
)
if mibBuilder.loadTexts:
    cpqUpsConfirmation.setStatus(
        ""
    )

cpqUpsBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12005)
)
if mibBuilder.loadTexts:
    cpqUpsBatteryLow.setStatus(
        ""
    )

cpqUps2LineFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12006)
)
cpqUps2LineFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQUPS-MIB", "cpqUpsEstimatedBatteryLife"))
)
if mibBuilder.loadTexts:
    cpqUps2LineFailed.setStatus(
        ""
    )

cpqUps2LineOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12007)
)
cpqUps2LineOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqUps2LineOk.setStatus(
        ""
    )

cpqUps2Shutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12008)
)
cpqUps2Shutdown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqUps2Shutdown.setStatus(
        ""
    )

cpqUps2Confirmation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12009)
)
cpqUps2Confirmation.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqUps2Confirmation.setStatus(
        ""
    )

cpqUps2BatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12010)
)
cpqUps2BatteryLow.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqUps2BatteryLow.setStatus(
        ""
    )

cpqUpsOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12011)
)
cpqUpsOverload.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqUpsOverload.setStatus(
        ""
    )

cpqUpsPendingBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12012)
)
cpqUpsPendingBatteryFailure.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqUpsPendingBatteryFailure.setStatus(
        ""
    )

cpqUpsGenericCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12013)
)
cpqUpsGenericCritical.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQUPS-MIB", "cpqUpsAlarm"))
)
if mibBuilder.loadTexts:
    cpqUpsGenericCritical.setStatus(
        ""
    )

cpqUpsGenericInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 12014)
)
cpqUpsGenericInfo.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQUPS-MIB", "cpqUpsAlarm"))
)
if mibBuilder.loadTexts:
    cpqUpsGenericInfo.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQUPS-MIB",
    **{"cpqUpsLineFailed": cpqUpsLineFailed,
       "cpqUpsLineOk": cpqUpsLineOk,
       "cpqUpsShutdown": cpqUpsShutdown,
       "cpqUpsConfirmation": cpqUpsConfirmation,
       "cpqUpsBatteryLow": cpqUpsBatteryLow,
       "cpqUps2LineFailed": cpqUps2LineFailed,
       "cpqUps2LineOk": cpqUps2LineOk,
       "cpqUps2Shutdown": cpqUps2Shutdown,
       "cpqUps2Confirmation": cpqUps2Confirmation,
       "cpqUps2BatteryLow": cpqUps2BatteryLow,
       "cpqUpsOverload": cpqUpsOverload,
       "cpqUpsPendingBatteryFailure": cpqUpsPendingBatteryFailure,
       "cpqUpsGenericCritical": cpqUpsGenericCritical,
       "cpqUpsGenericInfo": cpqUpsGenericInfo,
       "cpqUps": cpqUps,
       "cpqUpsMibRev": cpqUpsMibRev,
       "cpqUpsMibRevMajor": cpqUpsMibRevMajor,
       "cpqUpsMibRevMinor": cpqUpsMibRevMinor,
       "cpqUpsMibCondition": cpqUpsMibCondition,
       "cpqUpsComponent": cpqUpsComponent,
       "cpqUpsInterface": cpqUpsInterface,
       "cpqUpsOsCommon": cpqUpsOsCommon,
       "cpqUpsOsCommonPollFreq": cpqUpsOsCommonPollFreq,
       "cpqUpsOsCommonModuleTable": cpqUpsOsCommonModuleTable,
       "cpqUpsOsCommonModuleEntry": cpqUpsOsCommonModuleEntry,
       "cpqUpsOsCommonModuleIndex": cpqUpsOsCommonModuleIndex,
       "cpqUpsOsCommonModuleName": cpqUpsOsCommonModuleName,
       "cpqUpsOsCommonModuleVersion": cpqUpsOsCommonModuleVersion,
       "cpqUpsOsCommonModuleDate": cpqUpsOsCommonModuleDate,
       "cpqUpsOsCommonModulePurpose": cpqUpsOsCommonModulePurpose,
       "cpqUpsBasic": cpqUpsBasic,
       "cpqUpsLineStatus": cpqUpsLineStatus,
       "cpqUpsName": cpqUpsName,
       "cpqUpsEstimatedBatteryLife": cpqUpsEstimatedBatteryLife,
       "cpqUpsAutoShutdownDelay": cpqUpsAutoShutdownDelay,
       "cpqUpsLaunchCommand": cpqUpsLaunchCommand,
       "cpqUpsAlarm": cpqUpsAlarm,
       "cpqUpsFamily": cpqUpsFamily,
       "cpqUpsMemberTable": cpqUpsMemberTable,
       "cpqUpsMemberEntry": cpqUpsMemberEntry,
       "cpqUpsMemberIndex": cpqUpsMemberIndex,
       "cpqUpsMemberName": cpqUpsMemberName,
       "cpqUpsMemberCommunityStr": cpqUpsMemberCommunityStr,
       "cpqUpsAddMemberName": cpqUpsAddMemberName,
       "cpqUpsAddMemberCommunityStr": cpqUpsAddMemberCommunityStr}
)
