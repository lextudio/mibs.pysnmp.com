# SNMP MIB module (RDN-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:03 2024
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

(docsDevEvLevel,) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevEvLevel")

(ifAdminStatus,
 ifDescr,
 ifIndex,
 ifOperStatus,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifDescr",
    "ifIndex",
    "ifOperStatus",
    "ifType")

(riverdelta,) = mibBuilder.importSymbols(
    "RDN-MIB",
    "riverdelta")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysDescr,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rdnChassis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 1)
)
rdnChassis.setRevisions(
        ("2011-11-09 00:00",
         "2008-08-08 00:00",
         "2006-01-06 00:00",
         "2005-03-01 00:00",
         "2005-02-22 00:00",
         "2004-03-18 00:00",
         "2003-11-04 00:00",
         "2003-04-30 00:00",
         "2003-04-29 00:00",
         "2001-05-08 00:00",
         "2001-01-15 00:00",
         "2000-05-23 00:00",
         "2000-04-04 00:00",
         "2000-04-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChassisNotificationObject_ObjectIdentity = ObjectIdentity
chassisNotificationObject = _ChassisNotificationObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 1, 0)
)


class _ChassisPowerFailureTrapInfo_Type(Integer32):
    """Custom type chassisPowerFailureTrapInfo based on Integer32"""
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
        *(("powerFailureA", 1),
          ("powerFailureB", 2),
          ("powerRestoredA", 3),
          ("powerRestoredB", 4))
    )


_ChassisPowerFailureTrapInfo_Type.__name__ = "Integer32"
_ChassisPowerFailureTrapInfo_Object = MibScalar
chassisPowerFailureTrapInfo = _ChassisPowerFailureTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 0, 1),
    _ChassisPowerFailureTrapInfo_Type()
)
chassisPowerFailureTrapInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    chassisPowerFailureTrapInfo.setStatus("current")


class _ChassisFanFailureTrapInfo_Type(Integer32):
    """Custom type chassisFanFailureTrapInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerFanFailure", 2),
          ("upperFanFailure", 1))
    )


_ChassisFanFailureTrapInfo_Type.__name__ = "Integer32"
_ChassisFanFailureTrapInfo_Object = MibScalar
chassisFanFailureTrapInfo = _ChassisFanFailureTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 0, 3),
    _ChassisFanFailureTrapInfo_Type()
)
chassisFanFailureTrapInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    chassisFanFailureTrapInfo.setStatus("current")


class _RdnRedundancyFailedSlotNumber_Type(Integer32):
    """Custom type rdnRedundancyFailedSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdnRedundancyFailedSlotNumber_Type.__name__ = "Integer32"
_RdnRedundancyFailedSlotNumber_Object = MibScalar
rdnRedundancyFailedSlotNumber = _RdnRedundancyFailedSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 0, 5),
    _RdnRedundancyFailedSlotNumber_Type()
)
rdnRedundancyFailedSlotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnRedundancyFailedSlotNumber.setStatus("current")


class _RdnRedundancyBackupSlotNumber_Type(Integer32):
    """Custom type rdnRedundancyBackupSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdnRedundancyBackupSlotNumber_Type.__name__ = "Integer32"
_RdnRedundancyBackupSlotNumber_Object = MibScalar
rdnRedundancyBackupSlotNumber = _RdnRedundancyBackupSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 0, 6),
    _RdnRedundancyBackupSlotNumber_Type()
)
rdnRedundancyBackupSlotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnRedundancyBackupSlotNumber.setStatus("current")


class _RdnChassisType_Type(Integer32):
    """Custom type rdnChassisType based on Integer32"""
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
        *(("bsr1000", 3),
          ("bsr64000", 2),
          ("osr2000", 4),
          ("unknown", 1))
    )


_RdnChassisType_Type.__name__ = "Integer32"
_RdnChassisType_Object = MibScalar
rdnChassisType = _RdnChassisType_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 1),
    _RdnChassisType_Type()
)
rdnChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnChassisType.setStatus("current")
_RdnChassisVersion_Type = DisplayString
_RdnChassisVersion_Object = MibScalar
rdnChassisVersion = _RdnChassisVersion_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 2),
    _RdnChassisVersion_Type()
)
rdnChassisVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnChassisVersion.setStatus("current")
_RdnChassisId_Type = DisplayString
_RdnChassisId_Object = MibScalar
rdnChassisId = _RdnChassisId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 3),
    _RdnChassisId_Type()
)
rdnChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnChassisId.setStatus("current")
_RdnProcessorRam_Type = Integer32
_RdnProcessorRam_Object = MibScalar
rdnProcessorRam = _RdnProcessorRam_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 4),
    _RdnProcessorRam_Type()
)
rdnProcessorRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnProcessorRam.setStatus("current")
_RdnNvRAMSize_Type = Integer32
_RdnNvRAMSize_Object = MibScalar
rdnNvRAMSize = _RdnNvRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 5),
    _RdnNvRAMSize_Type()
)
rdnNvRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnNvRAMSize.setStatus("current")
_RdnNvRAMUsed_Type = Integer32
_RdnNvRAMUsed_Object = MibScalar
rdnNvRAMUsed = _RdnNvRAMUsed_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 6),
    _RdnNvRAMUsed_Type()
)
rdnNvRAMUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnNvRAMUsed.setStatus("current")
_RdnFlashSize_Type = Integer32
_RdnFlashSize_Object = MibScalar
rdnFlashSize = _RdnFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 7),
    _RdnFlashSize_Type()
)
rdnFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnFlashSize.setStatus("current")
_RdnCardTable_Object = MibTable
rdnCardTable = _RdnCardTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 8)
)
if mibBuilder.loadTexts:
    rdnCardTable.setStatus("current")
_RdnCardEntry_Object = MibTableRow
rdnCardEntry = _RdnCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 8, 1)
)
rdnCardEntry.setIndexNames(
    (0, "RDN-CHASSIS-MIB", "rdnCardIndex"),
)
if mibBuilder.loadTexts:
    rdnCardEntry.setStatus("current")


class _RdnCardIndex_Type(Unsigned32):
    """Custom type rdnCardIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RdnCardIndex_Type.__name__ = "Unsigned32"
_RdnCardIndex_Object = MibTableColumn
rdnCardIndex = _RdnCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 8, 1, 1),
    _RdnCardIndex_Type()
)
rdnCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnCardIndex.setStatus("current")


class _RdnCardType_Type(Integer32):
    """Custom type rdnCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("io", 3),
          ("srm", 2),
          ("unknown", 1))
    )


_RdnCardType_Type.__name__ = "Integer32"
_RdnCardType_Object = MibTableColumn
rdnCardType = _RdnCardType_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 8, 1, 2),
    _RdnCardType_Type()
)
rdnCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardType.setStatus("current")
_RdnCardDescr_Type = DisplayString
_RdnCardDescr_Object = MibTableColumn
rdnCardDescr = _RdnCardDescr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 8, 1, 3),
    _RdnCardDescr_Type()
)
rdnCardDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardDescr.setStatus("current")
_RdnCardSerial_Type = DisplayString
_RdnCardSerial_Object = MibTableColumn
rdnCardSerial = _RdnCardSerial_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 8, 1, 4),
    _RdnCardSerial_Type()
)
rdnCardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardSerial.setStatus("current")
_RdnCardHwVersion_Type = DisplayString
_RdnCardHwVersion_Object = MibTableColumn
rdnCardHwVersion = _RdnCardHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 8, 1, 5),
    _RdnCardHwVersion_Type()
)
rdnCardHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardHwVersion.setStatus("current")
_RdnCardSwVersion_Type = DisplayString
_RdnCardSwVersion_Object = MibTableColumn
rdnCardSwVersion = _RdnCardSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 8, 1, 6),
    _RdnCardSwVersion_Type()
)
rdnCardSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardSwVersion.setStatus("current")
_RdnCardSlotNumber_Type = Integer32
_RdnCardSlotNumber_Object = MibTableColumn
rdnCardSlotNumber = _RdnCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 8, 1, 7),
    _RdnCardSlotNumber_Type()
)
rdnCardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardSlotNumber.setStatus("current")
_RdnCardContainedByIndex_Type = Integer32
_RdnCardContainedByIndex_Object = MibTableColumn
rdnCardContainedByIndex = _RdnCardContainedByIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 8, 1, 8),
    _RdnCardContainedByIndex_Type()
)
rdnCardContainedByIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardContainedByIndex.setStatus("current")


class _RdnCardOperStatus_Type(Integer32):
    """Custom type rdnCardOperStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("boot", 8),
          ("config", 9),
          ("diag", 7),
          ("down", 3),
          ("flash", 6),
          ("not-specified", 1),
          ("rom", 5),
          ("standby", 4),
          ("up", 2))
    )


_RdnCardOperStatus_Type.__name__ = "Integer32"
_RdnCardOperStatus_Object = MibTableColumn
rdnCardOperStatus = _RdnCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 8, 1, 9),
    _RdnCardOperStatus_Type()
)
rdnCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardOperStatus.setStatus("current")
_RdnChassisSlots_Type = Integer32
_RdnChassisSlots_Object = MibScalar
rdnChassisSlots = _RdnChassisSlots_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 9),
    _RdnChassisSlots_Type()
)
rdnChassisSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnChassisSlots.setStatus("current")
_RdnSlotTable_Object = MibTable
rdnSlotTable = _RdnSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10)
)
if mibBuilder.loadTexts:
    rdnSlotTable.setStatus("current")
_RdnSlotEntry_Object = MibTableRow
rdnSlotEntry = _RdnSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1)
)
rdnSlotEntry.setIndexNames(
    (0, "RDN-CHASSIS-MIB", "rdnSlotIndex"),
)
if mibBuilder.loadTexts:
    rdnSlotEntry.setStatus("current")


class _RdnSlotIndex_Type(Integer32):
    """Custom type rdnSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdnSlotIndex_Type.__name__ = "Integer32"
_RdnSlotIndex_Object = MibTableColumn
rdnSlotIndex = _RdnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 1),
    _RdnSlotIndex_Type()
)
rdnSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnSlotIndex.setStatus("current")


class _RdnSlotType_Type(Integer32):
    """Custom type rdnSlotType based on Integer32"""
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
        *(("cmts", 5),
          ("hsim", 4),
          ("io", 3),
          ("srm", 2),
          ("unknown", 1))
    )


_RdnSlotType_Type.__name__ = "Integer32"
_RdnSlotType_Object = MibTableColumn
rdnSlotType = _RdnSlotType_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 2),
    _RdnSlotType_Type()
)
rdnSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSlotType.setStatus("current")


class _RdnSlotNumber_Type(Integer32):
    """Custom type rdnSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_RdnSlotNumber_Type.__name__ = "Integer32"
_RdnSlotNumber_Object = MibTableColumn
rdnSlotNumber = _RdnSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 3),
    _RdnSlotNumber_Type()
)
rdnSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSlotNumber.setStatus("current")


class _RdnSlotOperStatus_Type(Integer32):
    """Custom type rdnSlotOperStatus based on Integer32"""
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
        *(("down", 3),
          ("not-specified", 1),
          ("standby", 4),
          ("up", 2))
    )


_RdnSlotOperStatus_Type.__name__ = "Integer32"
_RdnSlotOperStatus_Object = MibTableColumn
rdnSlotOperStatus = _RdnSlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 4),
    _RdnSlotOperStatus_Type()
)
rdnSlotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSlotOperStatus.setStatus("current")


class _RdnOfflineModemCount_Type(Integer32):
    """Custom type rdnOfflineModemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdnOfflineModemCount_Type.__name__ = "Integer32"
_RdnOfflineModemCount_Object = MibTableColumn
rdnOfflineModemCount = _RdnOfflineModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 5),
    _RdnOfflineModemCount_Type()
)
rdnOfflineModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnOfflineModemCount.setStatus("current")


class _RdnOnlineModemCount_Type(Integer32):
    """Custom type rdnOnlineModemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdnOnlineModemCount_Type.__name__ = "Integer32"
_RdnOnlineModemCount_Object = MibTableColumn
rdnOnlineModemCount = _RdnOnlineModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 6),
    _RdnOnlineModemCount_Type()
)
rdnOnlineModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnOnlineModemCount.setStatus("current")


class _RdnActiveModemCount_Type(Integer32):
    """Custom type rdnActiveModemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdnActiveModemCount_Type.__name__ = "Integer32"
_RdnActiveModemCount_Object = MibTableColumn
rdnActiveModemCount = _RdnActiveModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 7),
    _RdnActiveModemCount_Type()
)
rdnActiveModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnActiveModemCount.setStatus("current")


class _RdnRegisteredModemCount_Type(Integer32):
    """Custom type rdnRegisteredModemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdnRegisteredModemCount_Type.__name__ = "Integer32"
_RdnRegisteredModemCount_Object = MibTableColumn
rdnRegisteredModemCount = _RdnRegisteredModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 8),
    _RdnRegisteredModemCount_Type()
)
rdnRegisteredModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnRegisteredModemCount.setStatus("current")


class _RdnProvisionedModemCount_Type(Integer32):
    """Custom type rdnProvisionedModemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdnProvisionedModemCount_Type.__name__ = "Integer32"
_RdnProvisionedModemCount_Object = MibTableColumn
rdnProvisionedModemCount = _RdnProvisionedModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 9),
    _RdnProvisionedModemCount_Type()
)
rdnProvisionedModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnProvisionedModemCount.setStatus("current")


class _RdnUnregisteredModemCount_Type(Integer32):
    """Custom type rdnUnregisteredModemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdnUnregisteredModemCount_Type.__name__ = "Integer32"
_RdnUnregisteredModemCount_Object = MibTableColumn
rdnUnregisteredModemCount = _RdnUnregisteredModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 10),
    _RdnUnregisteredModemCount_Type()
)
rdnUnregisteredModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnUnregisteredModemCount.setStatus("current")
_RdnResetSlotStats_Type = TruthValue
_RdnResetSlotStats_Object = MibTableColumn
rdnResetSlotStats = _RdnResetSlotStats_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 11),
    _RdnResetSlotStats_Type()
)
rdnResetSlotStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnResetSlotStats.setStatus("current")
_RdnSlotUnerroreds_Type = Counter32
_RdnSlotUnerroreds_Object = MibTableColumn
rdnSlotUnerroreds = _RdnSlotUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 12),
    _RdnSlotUnerroreds_Type()
)
rdnSlotUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSlotUnerroreds.setStatus("current")
_RdnSlotCorrecteds_Type = Counter32
_RdnSlotCorrecteds_Object = MibTableColumn
rdnSlotCorrecteds = _RdnSlotCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 13),
    _RdnSlotCorrecteds_Type()
)
rdnSlotCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSlotCorrecteds.setStatus("current")
_RdnSlotUncorrectables_Type = Counter32
_RdnSlotUncorrectables_Object = MibTableColumn
rdnSlotUncorrectables = _RdnSlotUncorrectables_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 10, 1, 14),
    _RdnSlotUncorrectables_Type()
)
rdnSlotUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSlotUncorrectables.setStatus("current")
_RdnCardIfIndexTable_Object = MibTable
rdnCardIfIndexTable = _RdnCardIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 11)
)
if mibBuilder.loadTexts:
    rdnCardIfIndexTable.setStatus("current")
_RdnCardIfIndexEntry_Object = MibTableRow
rdnCardIfIndexEntry = _RdnCardIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 11, 1)
)
rdnCardIfIndexEntry.setIndexNames(
    (0, "RDN-CHASSIS-MIB", "rdnCardIfIndex"),
)
if mibBuilder.loadTexts:
    rdnCardIfIndexEntry.setStatus("current")
_RdnCardIfIndex_Type = Integer32
_RdnCardIfIndex_Object = MibTableColumn
rdnCardIfIndex = _RdnCardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 11, 1, 1),
    _RdnCardIfIndex_Type()
)
rdnCardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardIfIndex.setStatus("current")
_RdnCardIfSlotNumber_Type = Integer32
_RdnCardIfSlotNumber_Object = MibTableColumn
rdnCardIfSlotNumber = _RdnCardIfSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 11, 1, 2),
    _RdnCardIfSlotNumber_Type()
)
rdnCardIfSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardIfSlotNumber.setStatus("current")
_RdnCardIfPortNumber_Type = Integer32
_RdnCardIfPortNumber_Object = MibTableColumn
rdnCardIfPortNumber = _RdnCardIfPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 11, 1, 3),
    _RdnCardIfPortNumber_Type()
)
rdnCardIfPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardIfPortNumber.setStatus("current")
_RdnCardIfCardIndex_Type = Integer32
_RdnCardIfCardIndex_Object = MibTableColumn
rdnCardIfCardIndex = _RdnCardIfCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 11, 1, 4),
    _RdnCardIfCardIndex_Type()
)
rdnCardIfCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardIfCardIndex.setStatus("current")


class _RdnCardIfConnectorTypeEnabled_Type(Integer32):
    """Custom type rdnCardIfConnectorTypeEnabled based on Integer32"""
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
        *(("db-15", 5),
          ("db-40", 4),
          ("none", 2),
          ("not-specified", 1),
          ("rj-45", 3))
    )


_RdnCardIfConnectorTypeEnabled_Type.__name__ = "Integer32"
_RdnCardIfConnectorTypeEnabled_Object = MibTableColumn
rdnCardIfConnectorTypeEnabled = _RdnCardIfConnectorTypeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 11, 1, 5),
    _RdnCardIfConnectorTypeEnabled_Type()
)
rdnCardIfConnectorTypeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardIfConnectorTypeEnabled.setStatus("current")


class _RdnCardIfLinkUpDownEnable_Type(Integer32):
    """Custom type rdnCardIfLinkUpDownEnable based on Integer32"""
    defaultValue = 2

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


_RdnCardIfLinkUpDownEnable_Type.__name__ = "Integer32"
_RdnCardIfLinkUpDownEnable_Object = MibTableColumn
rdnCardIfLinkUpDownEnable = _RdnCardIfLinkUpDownEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 11, 1, 6),
    _RdnCardIfLinkUpDownEnable_Type()
)
rdnCardIfLinkUpDownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCardIfLinkUpDownEnable.setStatus("current")


class _RdnCardIfPortType_Type(Integer32):
    """Custom type rdnCardIfPortType based on Integer32"""
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
        *(("cmts", 3),
          ("cmts-dn", 4),
          ("cmts-up", 5),
          ("cmts-up-log", 6),
          ("ethernet", 1),
          ("gige", 2),
          ("lag", 8),
          ("pos", 7))
    )


_RdnCardIfPortType_Type.__name__ = "Integer32"
_RdnCardIfPortType_Object = MibTableColumn
rdnCardIfPortType = _RdnCardIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 11, 1, 7),
    _RdnCardIfPortType_Type()
)
rdnCardIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCardIfPortType.setStatus("current")
_RdnSysUpTimeAtLastChassisChange_Type = TimeTicks
_RdnSysUpTimeAtLastChassisChange_Object = MibScalar
rdnSysUpTimeAtLastChassisChange = _RdnSysUpTimeAtLastChassisChange_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 12),
    _RdnSysUpTimeAtLastChassisChange_Type()
)
rdnSysUpTimeAtLastChassisChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSysUpTimeAtLastChassisChange.setStatus("current")
_RdnSysUpTimeAtLastConfigChange_Type = TimeTicks
_RdnSysUpTimeAtLastConfigChange_Object = MibScalar
rdnSysUpTimeAtLastConfigChange = _RdnSysUpTimeAtLastConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 13),
    _RdnSysUpTimeAtLastConfigChange_Type()
)
rdnSysUpTimeAtLastConfigChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnSysUpTimeAtLastConfigChange.setStatus("current")


class _RdnChassisPowerTrapEnable_Type(Integer32):
    """Custom type rdnChassisPowerTrapEnable based on Integer32"""
    defaultValue = 1

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


_RdnChassisPowerTrapEnable_Type.__name__ = "Integer32"
_RdnChassisPowerTrapEnable_Object = MibScalar
rdnChassisPowerTrapEnable = _RdnChassisPowerTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 14),
    _RdnChassisPowerTrapEnable_Type()
)
rdnChassisPowerTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnChassisPowerTrapEnable.setStatus("current")


class _RdnChassisFanTrapEnable_Type(Integer32):
    """Custom type rdnChassisFanTrapEnable based on Integer32"""
    defaultValue = 1

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


_RdnChassisFanTrapEnable_Type.__name__ = "Integer32"
_RdnChassisFanTrapEnable_Object = MibScalar
rdnChassisFanTrapEnable = _RdnChassisFanTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 15),
    _RdnChassisFanTrapEnable_Type()
)
rdnChassisFanTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnChassisFanTrapEnable.setStatus("current")


class _RdnChassisBSRSrmSwitchoverTrapEnable_Type(Integer32):
    """Custom type rdnChassisBSRSrmSwitchoverTrapEnable based on Integer32"""
    defaultValue = 1

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


_RdnChassisBSRSrmSwitchoverTrapEnable_Type.__name__ = "Integer32"
_RdnChassisBSRSrmSwitchoverTrapEnable_Object = MibScalar
rdnChassisBSRSrmSwitchoverTrapEnable = _RdnChassisBSRSrmSwitchoverTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 16),
    _RdnChassisBSRSrmSwitchoverTrapEnable_Type()
)
rdnChassisBSRSrmSwitchoverTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnChassisBSRSrmSwitchoverTrapEnable.setStatus("current")

# Managed Objects groups


# Notification objects

chassisPowerFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 1, 0, 2)
)
chassisPowerFailureTrap.setObjects(
    ("RDN-CHASSIS-MIB", "chassisPowerFailureTrapInfo")
)
if mibBuilder.loadTexts:
    chassisPowerFailureTrap.setStatus(
        "current"
    )

chassisFanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 1, 0, 4)
)
chassisFanFailureTrap.setObjects(
    ("RDN-CHASSIS-MIB", "chassisFanFailureTrapInfo")
)
if mibBuilder.loadTexts:
    chassisFanFailureTrap.setStatus(
        "current"
    )

rdnBSRSrmSwitchoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 1, 0, 7)
)
rdnBSRSrmSwitchoverTrap.setObjects(
      *(("RDN-CHASSIS-MIB", "rdnRedundancyFailedSlotNumber"),
        ("RDN-CHASSIS-MIB", "rdnRedundancyBackupSlotNumber"))
)
if mibBuilder.loadTexts:
    rdnBSRSrmSwitchoverTrap.setStatus(
        "current"
    )

rdnLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 1, 0, 8)
)
rdnLinkUpTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    rdnLinkUpTrap.setStatus(
        "current"
    )

rdnLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 1, 0, 9)
)
rdnLinkDownTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    rdnLinkDownTrap.setStatus(
        "current"
    )

rdnBsrTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 1, 0, 10)
)
rdnBsrTestTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    rdnBsrTestTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-CHASSIS-MIB",
    **{"rdnChassis": rdnChassis,
       "chassisNotificationObject": chassisNotificationObject,
       "chassisPowerFailureTrapInfo": chassisPowerFailureTrapInfo,
       "chassisPowerFailureTrap": chassisPowerFailureTrap,
       "chassisFanFailureTrapInfo": chassisFanFailureTrapInfo,
       "chassisFanFailureTrap": chassisFanFailureTrap,
       "rdnRedundancyFailedSlotNumber": rdnRedundancyFailedSlotNumber,
       "rdnRedundancyBackupSlotNumber": rdnRedundancyBackupSlotNumber,
       "rdnBSRSrmSwitchoverTrap": rdnBSRSrmSwitchoverTrap,
       "rdnLinkUpTrap": rdnLinkUpTrap,
       "rdnLinkDownTrap": rdnLinkDownTrap,
       "rdnBsrTestTrap": rdnBsrTestTrap,
       "rdnChassisType": rdnChassisType,
       "rdnChassisVersion": rdnChassisVersion,
       "rdnChassisId": rdnChassisId,
       "rdnProcessorRam": rdnProcessorRam,
       "rdnNvRAMSize": rdnNvRAMSize,
       "rdnNvRAMUsed": rdnNvRAMUsed,
       "rdnFlashSize": rdnFlashSize,
       "rdnCardTable": rdnCardTable,
       "rdnCardEntry": rdnCardEntry,
       "rdnCardIndex": rdnCardIndex,
       "rdnCardType": rdnCardType,
       "rdnCardDescr": rdnCardDescr,
       "rdnCardSerial": rdnCardSerial,
       "rdnCardHwVersion": rdnCardHwVersion,
       "rdnCardSwVersion": rdnCardSwVersion,
       "rdnCardSlotNumber": rdnCardSlotNumber,
       "rdnCardContainedByIndex": rdnCardContainedByIndex,
       "rdnCardOperStatus": rdnCardOperStatus,
       "rdnChassisSlots": rdnChassisSlots,
       "rdnSlotTable": rdnSlotTable,
       "rdnSlotEntry": rdnSlotEntry,
       "rdnSlotIndex": rdnSlotIndex,
       "rdnSlotType": rdnSlotType,
       "rdnSlotNumber": rdnSlotNumber,
       "rdnSlotOperStatus": rdnSlotOperStatus,
       "rdnOfflineModemCount": rdnOfflineModemCount,
       "rdnOnlineModemCount": rdnOnlineModemCount,
       "rdnActiveModemCount": rdnActiveModemCount,
       "rdnRegisteredModemCount": rdnRegisteredModemCount,
       "rdnProvisionedModemCount": rdnProvisionedModemCount,
       "rdnUnregisteredModemCount": rdnUnregisteredModemCount,
       "rdnResetSlotStats": rdnResetSlotStats,
       "rdnSlotUnerroreds": rdnSlotUnerroreds,
       "rdnSlotCorrecteds": rdnSlotCorrecteds,
       "rdnSlotUncorrectables": rdnSlotUncorrectables,
       "rdnCardIfIndexTable": rdnCardIfIndexTable,
       "rdnCardIfIndexEntry": rdnCardIfIndexEntry,
       "rdnCardIfIndex": rdnCardIfIndex,
       "rdnCardIfSlotNumber": rdnCardIfSlotNumber,
       "rdnCardIfPortNumber": rdnCardIfPortNumber,
       "rdnCardIfCardIndex": rdnCardIfCardIndex,
       "rdnCardIfConnectorTypeEnabled": rdnCardIfConnectorTypeEnabled,
       "rdnCardIfLinkUpDownEnable": rdnCardIfLinkUpDownEnable,
       "rdnCardIfPortType": rdnCardIfPortType,
       "rdnSysUpTimeAtLastChassisChange": rdnSysUpTimeAtLastChassisChange,
       "rdnSysUpTimeAtLastConfigChange": rdnSysUpTimeAtLastConfigChange,
       "rdnChassisPowerTrapEnable": rdnChassisPowerTrapEnable,
       "rdnChassisFanTrapEnable": rdnChassisFanTrapEnable,
       "rdnChassisBSRSrmSwitchoverTrapEnable": rdnChassisBSRSrmSwitchoverTrapEnable}
)
