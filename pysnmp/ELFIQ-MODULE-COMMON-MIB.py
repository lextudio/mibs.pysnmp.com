# SNMP MIB module (ELFIQ-MODULE-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELFIQ-MODULE-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:51 2024
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

(common,
 commonConformance) = mibBuilder.importSymbols(
    "ELFIQ-INC-MIB",
    "common",
    "commonConformance")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "VariablePointer")


# MODULE-IDENTITY

commonComponent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SystIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )



# MIB Managed Objects in the order of their OIDs

_SystInfo_ObjectIdentity = ObjectIdentity
systInfo = _SystInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1)
)


class _SystNumber_Type(Integer32):
    """Custom type systNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SystNumber_Type.__name__ = "Integer32"
_SystNumber_Object = MibScalar
systNumber = _SystNumber_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 1),
    _SystNumber_Type()
)
systNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systNumber.setStatus("current")
_SystTable_Object = MibTable
systTable = _SystTable_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    systTable.setStatus("current")
_SystEntry_Object = MibTableRow
systEntry = _SystEntry_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1)
)
systEntry.setIndexNames(
    (0, "ELFIQ-MODULE-COMMON-MIB", "systIndex"),
)
if mibBuilder.loadTexts:
    systEntry.setStatus("current")
_SystIndex_Type = SystIndex
_SystIndex_Object = MibTableColumn
systIndex = _SystIndex_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 1),
    _SystIndex_Type()
)
systIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systIndex.setStatus("current")


class _SystModel_Type(DisplayString):
    """Custom type systModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystModel_Type.__name__ = "DisplayString"
_SystModel_Object = MibTableColumn
systModel = _SystModel_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 2),
    _SystModel_Type()
)
systModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systModel.setStatus("current")


class _SystHostname_Type(DisplayString):
    """Custom type systHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystHostname_Type.__name__ = "DisplayString"
_SystHostname_Object = MibTableColumn
systHostname = _SystHostname_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 3),
    _SystHostname_Type()
)
systHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systHostname.setStatus("current")
_SystVersion_Type = Integer32
_SystVersion_Object = MibTableColumn
systVersion = _SystVersion_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 4),
    _SystVersion_Type()
)
systVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systVersion.setStatus("current")
_SystRevision_Type = Integer32
_SystRevision_Object = MibTableColumn
systRevision = _SystRevision_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 5),
    _SystRevision_Type()
)
systRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systRevision.setStatus("current")
_SystRelease_Type = Integer32
_SystRelease_Object = MibTableColumn
systRelease = _SystRelease_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 6),
    _SystRelease_Type()
)
systRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systRelease.setStatus("current")
_SystBuild_Type = Integer32
_SystBuild_Object = MibTableColumn
systBuild = _SystBuild_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 7),
    _SystBuild_Type()
)
systBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systBuild.setStatus("current")


class _SystTypeDesc_Type(DisplayString):
    """Custom type systTypeDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystTypeDesc_Type.__name__ = "DisplayString"
_SystTypeDesc_Object = MibTableColumn
systTypeDesc = _SystTypeDesc_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 8),
    _SystTypeDesc_Type()
)
systTypeDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systTypeDesc.setStatus("current")
_SystTime_Type = DateAndTime
_SystTime_Object = MibTableColumn
systTime = _SystTime_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 9),
    _SystTime_Type()
)
systTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systTime.setStatus("current")


class _SystLicenceStatus_Type(Integer32):
    """Custom type systLicenceStatus based on Integer32"""
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
        *(("keyActivated", 3),
          ("notVerified", 2),
          ("ok", 1),
          ("readKeyFailed", 4))
    )


_SystLicenceStatus_Type.__name__ = "Integer32"
_SystLicenceStatus_Object = MibTableColumn
systLicenceStatus = _SystLicenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 10),
    _SystLicenceStatus_Type()
)
systLicenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systLicenceStatus.setStatus("current")


class _SystLicenceType_Type(Integer32):
    """Custom type systLicenceType based on Integer32"""
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
        *(("demo", 2),
          ("endUser", 1),
          ("hrl", 4),
          ("isp", 5),
          ("nfr", 3))
    )


_SystLicenceType_Type.__name__ = "Integer32"
_SystLicenceType_Object = MibTableColumn
systLicenceType = _SystLicenceType_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 11),
    _SystLicenceType_Type()
)
systLicenceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systLicenceType.setStatus("current")
_SystNbVfiActivated_Type = Integer32
_SystNbVfiActivated_Object = MibTableColumn
systNbVfiActivated = _SystNbVfiActivated_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 12),
    _SystNbVfiActivated_Type()
)
systNbVfiActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systNbVfiActivated.setStatus("current")
_SystCpuUsePct_Type = Integer32
_SystCpuUsePct_Object = MibTableColumn
systCpuUsePct = _SystCpuUsePct_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 13),
    _SystCpuUsePct_Type()
)
systCpuUsePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systCpuUsePct.setStatus("current")
_SystRamUsePct_Type = Integer32
_SystRamUsePct_Object = MibTableColumn
systRamUsePct = _SystRamUsePct_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 14),
    _SystRamUsePct_Type()
)
systRamUsePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systRamUsePct.setStatus("current")
_SystFanSpeed_Type = Integer32
_SystFanSpeed_Object = MibTableColumn
systFanSpeed = _SystFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 15),
    _SystFanSpeed_Type()
)
systFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systFanSpeed.setStatus("current")
_SystCpuTemp_Type = Integer32
_SystCpuTemp_Object = MibTableColumn
systCpuTemp = _SystCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 16),
    _SystCpuTemp_Type()
)
systCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systCpuTemp.setStatus("current")


class _SystSmptSeverity_Type(Integer32):
    """Custom type systSmptSeverity based on Integer32"""
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
        *(("alert", 1),
          ("info", 4),
          ("notice", 3),
          ("warning", 2))
    )


_SystSmptSeverity_Type.__name__ = "Integer32"
_SystSmptSeverity_Object = MibTableColumn
systSmptSeverity = _SystSmptSeverity_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 17),
    _SystSmptSeverity_Type()
)
systSmptSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systSmptSeverity.setStatus("current")


class _SystSmtpReciptient1_Type(DisplayString):
    """Custom type systSmtpReciptient1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystSmtpReciptient1_Type.__name__ = "DisplayString"
_SystSmtpReciptient1_Object = MibTableColumn
systSmtpReciptient1 = _SystSmtpReciptient1_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 18),
    _SystSmtpReciptient1_Type()
)
systSmtpReciptient1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systSmtpReciptient1.setStatus("current")


class _SystSmtpReciptient2_Type(DisplayString):
    """Custom type systSmtpReciptient2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystSmtpReciptient2_Type.__name__ = "DisplayString"
_SystSmtpReciptient2_Object = MibTableColumn
systSmtpReciptient2 = _SystSmtpReciptient2_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 19),
    _SystSmtpReciptient2_Type()
)
systSmtpReciptient2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systSmtpReciptient2.setStatus("current")


class _SystSmtpReciptient3_Type(DisplayString):
    """Custom type systSmtpReciptient3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystSmtpReciptient3_Type.__name__ = "DisplayString"
_SystSmtpReciptient3_Object = MibTableColumn
systSmtpReciptient3 = _SystSmtpReciptient3_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 20),
    _SystSmtpReciptient3_Type()
)
systSmtpReciptient3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systSmtpReciptient3.setStatus("current")


class _SystSmtpReciptient4_Type(DisplayString):
    """Custom type systSmtpReciptient4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystSmtpReciptient4_Type.__name__ = "DisplayString"
_SystSmtpReciptient4_Object = MibTableColumn
systSmtpReciptient4 = _SystSmtpReciptient4_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 21),
    _SystSmtpReciptient4_Type()
)
systSmtpReciptient4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systSmtpReciptient4.setStatus("current")


class _SystSmtpReciptient5_Type(DisplayString):
    """Custom type systSmtpReciptient5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystSmtpReciptient5_Type.__name__ = "DisplayString"
_SystSmtpReciptient5_Object = MibTableColumn
systSmtpReciptient5 = _SystSmtpReciptient5_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 22),
    _SystSmtpReciptient5_Type()
)
systSmtpReciptient5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systSmtpReciptient5.setStatus("current")


class _SystSmtpReciptient6_Type(DisplayString):
    """Custom type systSmtpReciptient6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystSmtpReciptient6_Type.__name__ = "DisplayString"
_SystSmtpReciptient6_Object = MibTableColumn
systSmtpReciptient6 = _SystSmtpReciptient6_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 23),
    _SystSmtpReciptient6_Type()
)
systSmtpReciptient6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systSmtpReciptient6.setStatus("current")


class _SystSmtpReciptient7_Type(DisplayString):
    """Custom type systSmtpReciptient7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystSmtpReciptient7_Type.__name__ = "DisplayString"
_SystSmtpReciptient7_Object = MibTableColumn
systSmtpReciptient7 = _SystSmtpReciptient7_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 24),
    _SystSmtpReciptient7_Type()
)
systSmtpReciptient7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systSmtpReciptient7.setStatus("current")


class _SystSmtpReciptient8_Type(DisplayString):
    """Custom type systSmtpReciptient8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystSmtpReciptient8_Type.__name__ = "DisplayString"
_SystSmtpReciptient8_Object = MibTableColumn
systSmtpReciptient8 = _SystSmtpReciptient8_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 1, 1, 2, 1, 25),
    _SystSmtpReciptient8_Type()
)
systSmtpReciptient8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systSmtpReciptient8.setStatus("current")
_CommonNotification_ObjectIdentity = ObjectIdentity
commonNotification = _CommonNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 2)
)
_SystNotification_ObjectIdentity = ObjectIdentity
systNotification = _SystNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 2, 1)
)
_SystGroups_ObjectIdentity = ObjectIdentity
systGroups = _SystGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 2, 1, 1)
)

# Managed Objects groups

systInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19713, 2, 1, 1, 1)
)
systInfoGroup.setObjects(
      *(("ELFIQ-MODULE-COMMON-MIB", "systNumber"),
        ("ELFIQ-MODULE-COMMON-MIB", "systIndex"),
        ("ELFIQ-MODULE-COMMON-MIB", "systModel"),
        ("ELFIQ-MODULE-COMMON-MIB", "systHostname"),
        ("ELFIQ-MODULE-COMMON-MIB", "systVersion"),
        ("ELFIQ-MODULE-COMMON-MIB", "systRevision"),
        ("ELFIQ-MODULE-COMMON-MIB", "systRelease"),
        ("ELFIQ-MODULE-COMMON-MIB", "systBuild"),
        ("ELFIQ-MODULE-COMMON-MIB", "systTypeDesc"),
        ("ELFIQ-MODULE-COMMON-MIB", "systTime"),
        ("ELFIQ-MODULE-COMMON-MIB", "systLicenceStatus"),
        ("ELFIQ-MODULE-COMMON-MIB", "systLicenceType"),
        ("ELFIQ-MODULE-COMMON-MIB", "systNbVfiActivated"),
        ("ELFIQ-MODULE-COMMON-MIB", "systCpuUsePct"),
        ("ELFIQ-MODULE-COMMON-MIB", "systFanSpeed"),
        ("ELFIQ-MODULE-COMMON-MIB", "systCpuTemp"),
        ("ELFIQ-MODULE-COMMON-MIB", "systRamUsePct"),
        ("ELFIQ-MODULE-COMMON-MIB", "systSmptSeverity"),
        ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient1"),
        ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient2"),
        ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient3"),
        ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient4"),
        ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient5"),
        ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient6"),
        ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient7"),
        ("ELFIQ-MODULE-COMMON-MIB", "systSmtpReciptient8"))
)
if mibBuilder.loadTexts:
    systInfoGroup.setStatus("current")


# Notification objects

systEOSStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 2, 1, 1)
)
systEOSStart.setObjects(
    ("ELFIQ-MODULE-COMMON-MIB", "systHostname")
)
if mibBuilder.loadTexts:
    systEOSStart.setStatus(
        "current"
    )

systCPUTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 2, 1, 2)
)
systCPUTemp.setObjects(
      *(("ELFIQ-MODULE-COMMON-MIB", "systHostname"),
        ("ELFIQ-MODULE-COMMON-MIB", "systCpuTemp"))
)
if mibBuilder.loadTexts:
    systCPUTemp.setStatus(
        "current"
    )

systCPUUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 2, 1, 3)
)
systCPUUsage.setObjects(
    ("ELFIQ-MODULE-COMMON-MIB", "systHostname")
)
if mibBuilder.loadTexts:
    systCPUUsage.setStatus(
        "current"
    )

systCPUFan = NotificationType(
    (1, 3, 6, 1, 4, 1, 19713, 1, 1, 2, 1, 4)
)
systCPUFan.setObjects(
    ("ELFIQ-MODULE-COMMON-MIB", "systHostname")
)
if mibBuilder.loadTexts:
    systCPUFan.setStatus(
        "current"
    )


# Notifications groups

systNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 19713, 2, 1, 1, 2)
)
systNotificationGroup.setObjects(
      *(("ELFIQ-MODULE-COMMON-MIB", "systEOSStart"),
        ("ELFIQ-MODULE-COMMON-MIB", "systCPUTemp"),
        ("ELFIQ-MODULE-COMMON-MIB", "systCPUUsage"),
        ("ELFIQ-MODULE-COMMON-MIB", "systCPUFan"))
)
if mibBuilder.loadTexts:
    systNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELFIQ-MODULE-COMMON-MIB",
    **{"SystIndex": SystIndex,
       "commonComponent": commonComponent,
       "systInfo": systInfo,
       "systNumber": systNumber,
       "systTable": systTable,
       "systEntry": systEntry,
       "systIndex": systIndex,
       "systModel": systModel,
       "systHostname": systHostname,
       "systVersion": systVersion,
       "systRevision": systRevision,
       "systRelease": systRelease,
       "systBuild": systBuild,
       "systTypeDesc": systTypeDesc,
       "systTime": systTime,
       "systLicenceStatus": systLicenceStatus,
       "systLicenceType": systLicenceType,
       "systNbVfiActivated": systNbVfiActivated,
       "systCpuUsePct": systCpuUsePct,
       "systRamUsePct": systRamUsePct,
       "systFanSpeed": systFanSpeed,
       "systCpuTemp": systCpuTemp,
       "systSmptSeverity": systSmptSeverity,
       "systSmtpReciptient1": systSmtpReciptient1,
       "systSmtpReciptient2": systSmtpReciptient2,
       "systSmtpReciptient3": systSmtpReciptient3,
       "systSmtpReciptient4": systSmtpReciptient4,
       "systSmtpReciptient5": systSmtpReciptient5,
       "systSmtpReciptient6": systSmtpReciptient6,
       "systSmtpReciptient7": systSmtpReciptient7,
       "systSmtpReciptient8": systSmtpReciptient8,
       "commonNotification": commonNotification,
       "systNotification": systNotification,
       "systEOSStart": systEOSStart,
       "systCPUTemp": systCPUTemp,
       "systCPUUsage": systCPUUsage,
       "systCPUFan": systCPUFan,
       "systGroups": systGroups,
       "systInfoGroup": systInfoGroup,
       "systNotificationGroup": systNotificationGroup}
)
