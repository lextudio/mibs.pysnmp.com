# SNMP MIB module (LUMINOUS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LUMINOUS-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:31 2024
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

(LumAdminStatus,
 LumAlarmSeverity,
 LumCardBaseType,
 LumDescr,
 LumName,
 LumOperStatus,
 LumPortNum,
 LumResetCmd,
 LumSignalState,
 LumSimpleIndex,
 LumSlotNum,
 LumVersionString) = mibBuilder.importSymbols(
    "LUMINOUS-TC-MIB",
    "LumAdminStatus",
    "LumAlarmSeverity",
    "LumCardBaseType",
    "LumDescr",
    "LumName",
    "LumOperStatus",
    "LumPortNum",
    "LumResetCmd",
    "LumSignalState",
    "LumSimpleIndex",
    "LumSlotNum",
    "LumVersionString")

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
 ObjectName,
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
    "ObjectName",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lumSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4)
)
lumSystemMIB.setRevisions(
        ("1901-06-27 00:00",
         "1901-05-24 00:00",
         "1900-10-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Luminous_ObjectIdentity = ObjectIdentity
luminous = _Luminous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614)
)
_LumADM_ObjectIdentity = ObjectIdentity
lumADM = _LumADM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1)
)
_LumSoftwareDownload_ObjectIdentity = ObjectIdentity
lumSoftwareDownload = _LumSoftwareDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 1)
)


class _LumDownLoadImageType_Type(LumCardBaseType):
    """Custom type lumDownLoadImageType based on LumCardBaseType"""
    defaultValue = 1


_LumDownLoadImageType_Object = MibScalar
lumDownLoadImageType = _LumDownLoadImageType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 1),
    _LumDownLoadImageType_Type()
)
lumDownLoadImageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumDownLoadImageType.setStatus("current")


class _LumDownLoadHost_Type(DisplayString):
    """Custom type lumDownLoadHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LumDownLoadHost_Type.__name__ = "DisplayString"
_LumDownLoadHost_Object = MibScalar
lumDownLoadHost = _LumDownLoadHost_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 2),
    _LumDownLoadHost_Type()
)
lumDownLoadHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumDownLoadHost.setStatus("current")


class _LumDownLoadUsrName_Type(DisplayString):
    """Custom type lumDownLoadUsrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LumDownLoadUsrName_Type.__name__ = "DisplayString"
_LumDownLoadUsrName_Object = MibScalar
lumDownLoadUsrName = _LumDownLoadUsrName_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 3),
    _LumDownLoadUsrName_Type()
)
lumDownLoadUsrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumDownLoadUsrName.setStatus("current")


class _LumDownLoadPasswd_Type(DisplayString):
    """Custom type lumDownLoadPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LumDownLoadPasswd_Type.__name__ = "DisplayString"
_LumDownLoadPasswd_Object = MibScalar
lumDownLoadPasswd = _LumDownLoadPasswd_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 4),
    _LumDownLoadPasswd_Type()
)
lumDownLoadPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumDownLoadPasswd.setStatus("current")


class _LumDownLoadFilePath_Type(DisplayString):
    """Custom type lumDownLoadFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LumDownLoadFilePath_Type.__name__ = "DisplayString"
_LumDownLoadFilePath_Object = MibScalar
lumDownLoadFilePath = _LumDownLoadFilePath_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 5),
    _LumDownLoadFilePath_Type()
)
lumDownLoadFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumDownLoadFilePath.setStatus("current")
_LumDownLoadVersion_Type = LumVersionString
_LumDownLoadVersion_Object = MibScalar
lumDownLoadVersion = _LumDownLoadVersion_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 6),
    _LumDownLoadVersion_Type()
)
lumDownLoadVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumDownLoadVersion.setStatus("current")
_LumDownLoadSlot_Type = LumSlotNum
_LumDownLoadSlot_Object = MibScalar
lumDownLoadSlot = _LumDownLoadSlot_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 7),
    _LumDownLoadSlot_Type()
)
lumDownLoadSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumDownLoadSlot.setStatus("current")


class _LumDownLoadTimeOut_Type(Integer32):
    """Custom type lumDownLoadTimeOut based on Integer32"""
    defaultValue = 10


_LumDownLoadTimeOut_Object = MibScalar
lumDownLoadTimeOut = _LumDownLoadTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 8),
    _LumDownLoadTimeOut_Type()
)
lumDownLoadTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumDownLoadTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    lumDownLoadTimeOut.setUnits("minutes")


class _LumDownLoadCmd_Type(Integer32):
    """Custom type lumDownLoadCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("none", 1))
    )


_LumDownLoadCmd_Type.__name__ = "Integer32"
_LumDownLoadCmd_Object = MibScalar
lumDownLoadCmd = _LumDownLoadCmd_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 9),
    _LumDownLoadCmd_Type()
)
lumDownLoadCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumDownLoadCmd.setStatus("current")


class _LumDownLoadStatus_Type(Integer32):
    """Custom type lumDownLoadStatus based on Integer32"""
    defaultValue = 1

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
        *(("download-failed", 4),
          ("download-in-progress", 2),
          ("download-succeeded", 3),
          ("none", 1))
    )


_LumDownLoadStatus_Type.__name__ = "Integer32"
_LumDownLoadStatus_Object = MibScalar
lumDownLoadStatus = _LumDownLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 10),
    _LumDownLoadStatus_Type()
)
lumDownLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumDownLoadStatus.setStatus("current")


class _LumDownLoadAbort_Type(Integer32):
    """Custom type lumDownLoadAbort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abort", 2),
          ("none", 1))
    )


_LumDownLoadAbort_Type.__name__ = "Integer32"
_LumDownLoadAbort_Object = MibScalar
lumDownLoadAbort = _LumDownLoadAbort_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 11),
    _LumDownLoadAbort_Type()
)
lumDownLoadAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumDownLoadAbort.setStatus("current")
_LumSystemReset_ObjectIdentity = ObjectIdentity
lumSystemReset = _LumSystemReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 2)
)
_LumSystemResetCardTable_Object = MibTable
lumSystemResetCardTable = _LumSystemResetCardTable_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    lumSystemResetCardTable.setStatus("deprecated")
_LumSystemResetCardEntry_Object = MibTableRow
lumSystemResetCardEntry = _LumSystemResetCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 1, 1)
)
lumSystemResetCardEntry.setIndexNames(
    (0, "LUMINOUS-SYSTEM-MIB", "lumSystemResetCardIndex"),
)
if mibBuilder.loadTexts:
    lumSystemResetCardEntry.setStatus("deprecated")
_LumSystemResetCardIndex_Type = LumSlotNum
_LumSystemResetCardIndex_Object = MibTableColumn
lumSystemResetCardIndex = _LumSystemResetCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 1, 1, 1),
    _LumSystemResetCardIndex_Type()
)
lumSystemResetCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumSystemResetCardIndex.setStatus("deprecated")
_LumSystemResetCardCmd_Type = LumResetCmd
_LumSystemResetCardCmd_Object = MibTableColumn
lumSystemResetCardCmd = _LumSystemResetCardCmd_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 1, 1, 2),
    _LumSystemResetCardCmd_Type()
)
lumSystemResetCardCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumSystemResetCardCmd.setStatus("deprecated")
_LumSystemResetShelfCmd_Type = LumResetCmd
_LumSystemResetShelfCmd_Object = MibScalar
lumSystemResetShelfCmd = _LumSystemResetShelfCmd_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 2),
    _LumSystemResetShelfCmd_Type()
)
lumSystemResetShelfCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lumSystemResetShelfCmd.setStatus("deprecated")
_LumAlarms_ObjectIdentity = ObjectIdentity
lumAlarms = _LumAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3)
)
_LumAlarmV2Traps_ObjectIdentity = ObjectIdentity
lumAlarmV2Traps = _LumAlarmV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 0)
)
_LumAlarmType_ObjectIdentity = ObjectIdentity
lumAlarmType = _LumAlarmType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1)
)


class _LumProvisionAlarmType_Type(Integer32):
    """Custom type lumProvisionAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("provCardFailedNoBackup", 1),
          ("provCardFailedWithBackup", 2))
    )


_LumProvisionAlarmType_Type.__name__ = "Integer32"
_LumProvisionAlarmType_Object = MibScalar
lumProvisionAlarmType = _LumProvisionAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 1),
    _LumProvisionAlarmType_Type()
)
lumProvisionAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumProvisionAlarmType.setStatus("current")


class _LumAlarmCardAlarmType_Type(Integer32):
    """Custom type lumAlarmCardAlarmType based on Integer32"""
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
        *(("alarmCardFailedNoBackup", 9),
          ("alarmCardFailedWithBackup", 10),
          ("card-lost", 11),
          ("input0", 1),
          ("input1", 2),
          ("input2", 3),
          ("input3", 4),
          ("input4", 5),
          ("input5", 6),
          ("input6", 7),
          ("input7", 8))
    )


_LumAlarmCardAlarmType_Type.__name__ = "Integer32"
_LumAlarmCardAlarmType_Object = MibScalar
lumAlarmCardAlarmType = _LumAlarmCardAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 2),
    _LumAlarmCardAlarmType_Type()
)
lumAlarmCardAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumAlarmCardAlarmType.setStatus("current")


class _LumSysconAlarmType_Type(Integer32):
    """Custom type lumSysconAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cmmlf", 1),
          ("redundancy-lost", 2))
    )


_LumSysconAlarmType_Type.__name__ = "Integer32"
_LumSysconAlarmType_Object = MibScalar
lumSysconAlarmType = _LumSysconAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 3),
    _LumSysconAlarmType_Type()
)
lumSysconAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumSysconAlarmType.setStatus("current")


class _LumT1AlarmType_Type(Integer32):
    """Custom type lumT1AlarmType based on Integer32"""
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
        *(("ais", 4),
          ("bpv", 1),
          ("lof", 2),
          ("los", 3),
          ("ovrfl", 6),
          ("rai", 5),
          ("sf-ber", 7),
          ("sf-es", 8),
          ("sf-ses", 9),
          ("tcfl", 10))
    )


_LumT1AlarmType_Type.__name__ = "Integer32"
_LumT1AlarmType_Object = MibScalar
lumT1AlarmType = _LumT1AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 4),
    _LumT1AlarmType_Type()
)
lumT1AlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumT1AlarmType.setStatus("current")


class _LumTEN100AlarmType_Type(Integer32):
    """Custom type lumTEN100AlarmType based on Integer32"""
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
        *(("aler", 6),
          ("an-fail", 1),
          ("fcserr", 7),
          ("frlex", 5),
          ("los", 2),
          ("rxer", 4),
          ("symer", 3))
    )


_LumTEN100AlarmType_Type.__name__ = "Integer32"
_LumTEN100AlarmType_Object = MibScalar
lumTEN100AlarmType = _LumTEN100AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 5),
    _LumTEN100AlarmType_Type()
)
lumTEN100AlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumTEN100AlarmType.setStatus("current")


class _LumSonetAlarmType_Type(Integer32):
    """Custom type lumSonetAlarmType based on Integer32"""
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
        *(("ais-l", 7),
          ("ais-p", 11),
          ("aps-failed", 21),
          ("aps-far-end", 19),
          ("aps-k1", 16),
          ("aps-k2", 17),
          ("aps-mode", 18),
          ("aps-success", 20),
          ("laser-bias", 2),
          ("laser-loop", 1),
          ("laser-pwr", 3),
          ("lof-s", 6),
          ("lop-p", 13),
          ("los-s", 5),
          ("loss-of-sync", 4),
          ("plm-p", 15),
          ("rfi-l", 8),
          ("rfi-p", 12),
          ("sd-ber", 10),
          ("sf-ber", 9),
          ("uneq-p", 14))
    )


_LumSonetAlarmType_Type.__name__ = "Integer32"
_LumSonetAlarmType_Object = MibScalar
lumSonetAlarmType = _LumSonetAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 6),
    _LumSonetAlarmType_Type()
)
lumSonetAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumSonetAlarmType.setStatus("current")


class _LumRingCardAlarmType_Type(Integer32):
    """Custom type lumRingCardAlarmType based on Integer32"""
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
        *(("io-card-lost", 9),
          ("io-east-lost", 8),
          ("io-west-lost", 7),
          ("los", 1),
          ("losynch", 2),
          ("pri-los", 5),
          ("sd-ber", 4),
          ("sec-los", 6),
          ("sf-ber", 3),
          ("switch-fabric-lost", 10),
          ("switch-fabric-redundancy-lost", 11))
    )


_LumRingCardAlarmType_Type.__name__ = "Integer32"
_LumRingCardAlarmType_Object = MibScalar
lumRingCardAlarmType = _LumRingCardAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 7),
    _LumRingCardAlarmType_Type()
)
lumRingCardAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumRingCardAlarmType.setStatus("current")


class _LumUtilityAlarmType_Type(Integer32):
    """Custom type lumUtilityAlarmType based on Integer32"""
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
        *(("card-lost", 5),
          ("hitmp", 2),
          ("pwra", 3),
          ("pwrb", 4),
          ("vltg", 1))
    )


_LumUtilityAlarmType_Type.__name__ = "Integer32"
_LumUtilityAlarmType_Object = MibScalar
lumUtilityAlarmType = _LumUtilityAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 8),
    _LumUtilityAlarmType_Type()
)
lumUtilityAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumUtilityAlarmType.setStatus("current")


class _LumEquipmentAlarmType_Type(Integer32):
    """Custom type lumEquipmentAlarmType based on Integer32"""
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
        *(("boot", 3),
          ("fncrt", 1),
          ("fnmjr", 2),
          ("hitmp", 5),
          ("hwfl", 4),
          ("io-card-lost", 12),
          ("io-card-mismatched", 14),
          ("mea", 10),
          ("prov-io-card-lost", 11),
          ("prov-io-card-mismatched", 13),
          ("sgeo", 8),
          ("trans-mea", 7),
          ("ueq", 9),
          ("vltg", 6))
    )


_LumEquipmentAlarmType_Type.__name__ = "Integer32"
_LumEquipmentAlarmType_Object = MibScalar
lumEquipmentAlarmType = _LumEquipmentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 9),
    _LumEquipmentAlarmType_Type()
)
lumEquipmentAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumEquipmentAlarmType.setStatus("current")


class _LumDataFlowAlarmType_Type(Integer32):
    """Custom type lumDataFlowAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sf-bfc", 3),
          ("sf-dfc", 1),
          ("sf-ifc", 2))
    )


_LumDataFlowAlarmType_Type.__name__ = "Integer32"
_LumDataFlowAlarmType_Object = MibScalar
lumDataFlowAlarmType = _LumDataFlowAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 10),
    _LumDataFlowAlarmType_Type()
)
lumDataFlowAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumDataFlowAlarmType.setStatus("current")


class _LumDataBaseAlarmType_Type(Integer32):
    """Custom type lumDataBaseAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restoreFailed", 2),
          ("saveFailed", 1))
    )


_LumDataBaseAlarmType_Type.__name__ = "Integer32"
_LumDataBaseAlarmType_Object = MibScalar
lumDataBaseAlarmType = _LumDataBaseAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 11),
    _LumDataBaseAlarmType_Type()
)
lumDataBaseAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumDataBaseAlarmType.setStatus("current")


class _LumPPPAlarmType_Type(Integer32):
    """Custom type lumPPPAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("linkDown", 1)
    )


_LumPPPAlarmType_Type.__name__ = "Integer32"
_LumPPPAlarmType_Object = MibScalar
lumPPPAlarmType = _LumPPPAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 12),
    _LumPPPAlarmType_Type()
)
lumPPPAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumPPPAlarmType.setStatus("current")
_LumAlarmSource_ObjectIdentity = ObjectIdentity
lumAlarmSource = _LumAlarmSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 2)
)
_LumAlarmSlotId_Type = LumSlotNum
_LumAlarmSlotId_Object = MibScalar
lumAlarmSlotId = _LumAlarmSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 2, 1),
    _LumAlarmSlotId_Type()
)
lumAlarmSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumAlarmSlotId.setStatus("current")
_LumAlarmPortId_Type = LumPortNum
_LumAlarmPortId_Object = MibScalar
lumAlarmPortId = _LumAlarmPortId_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 2, 2),
    _LumAlarmPortId_Type()
)
lumAlarmPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumAlarmPortId.setStatus("current")


class _LumAlarmStatus_Type(Integer32):
    """Custom type lumAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarmClear", 1),
          ("alarmMasked", 3),
          ("alarmSet", 2))
    )


_LumAlarmStatus_Type.__name__ = "Integer32"
_LumAlarmStatus_Object = MibScalar
lumAlarmStatus = _LumAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 3),
    _LumAlarmStatus_Type()
)
lumAlarmStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lumAlarmStatus.setStatus("current")
_LumAlarmLog_ObjectIdentity = ObjectIdentity
lumAlarmLog = _LumAlarmLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4)
)
_LumAlarmActiveTable_Object = MibTable
lumAlarmActiveTable = _LumAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1)
)
if mibBuilder.loadTexts:
    lumAlarmActiveTable.setStatus("current")
_LumAlarmActiveEntry_Object = MibTableRow
lumAlarmActiveEntry = _LumAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1)
)
lumAlarmActiveEntry.setIndexNames(
    (0, "LUMINOUS-SYSTEM-MIB", "lumAlarmActiveIndex"),
)
if mibBuilder.loadTexts:
    lumAlarmActiveEntry.setStatus("current")
_LumAlarmActiveIndex_Type = Integer32
_LumAlarmActiveIndex_Object = MibTableColumn
lumAlarmActiveIndex = _LumAlarmActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 1),
    _LumAlarmActiveIndex_Type()
)
lumAlarmActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmActiveIndex.setStatus("current")


class _LumAlarmActiveType_Type(Integer32):
    """Custom type lumAlarmActiveType based on Integer32"""
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
        *(("alarmCard", 2),
          ("dataBase", 11),
          ("dataFlow", 10),
          ("equipment", 9),
          ("provision", 1),
          ("ringCard", 7),
          ("sonet", 6),
          ("syscon", 3),
          ("t1", 4),
          ("tEN100", 5),
          ("utility", 8))
    )


_LumAlarmActiveType_Type.__name__ = "Integer32"
_LumAlarmActiveType_Object = MibTableColumn
lumAlarmActiveType = _LumAlarmActiveType_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 2),
    _LumAlarmActiveType_Type()
)
lumAlarmActiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmActiveType.setStatus("current")
_LumAlarmActiveValue_Type = Integer32
_LumAlarmActiveValue_Object = MibTableColumn
lumAlarmActiveValue = _LumAlarmActiveValue_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 3),
    _LumAlarmActiveValue_Type()
)
lumAlarmActiveValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmActiveValue.setStatus("current")


class _LumAlarmActiveStatus_Type(Integer32):
    """Custom type lumAlarmActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarmClear", 1),
          ("alarmMasked", 3),
          ("alarmSet", 2))
    )


_LumAlarmActiveStatus_Type.__name__ = "Integer32"
_LumAlarmActiveStatus_Object = MibTableColumn
lumAlarmActiveStatus = _LumAlarmActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 4),
    _LumAlarmActiveStatus_Type()
)
lumAlarmActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmActiveStatus.setStatus("current")
_LumAlarmActiveTimeStamp_Type = DateAndTime
_LumAlarmActiveTimeStamp_Object = MibTableColumn
lumAlarmActiveTimeStamp = _LumAlarmActiveTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 5),
    _LumAlarmActiveTimeStamp_Type()
)
lumAlarmActiveTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmActiveTimeStamp.setStatus("current")
_LumAlarmActiveSlotId_Type = LumSlotNum
_LumAlarmActiveSlotId_Object = MibTableColumn
lumAlarmActiveSlotId = _LumAlarmActiveSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 6),
    _LumAlarmActiveSlotId_Type()
)
lumAlarmActiveSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmActiveSlotId.setStatus("current")
_LumAlarmActivePortId_Type = LumPortNum
_LumAlarmActivePortId_Object = MibTableColumn
lumAlarmActivePortId = _LumAlarmActivePortId_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 7),
    _LumAlarmActivePortId_Type()
)
lumAlarmActivePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmActivePortId.setStatus("current")
_LumAlarmHistoryTable_Object = MibTable
lumAlarmHistoryTable = _LumAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 2)
)
if mibBuilder.loadTexts:
    lumAlarmHistoryTable.setStatus("current")
_LumAlarmHistoryEntry_Object = MibTableRow
lumAlarmHistoryEntry = _LumAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 2, 1)
)
lumAlarmHistoryEntry.setIndexNames(
    (0, "LUMINOUS-SYSTEM-MIB", "lumAlarmHistoryIndex"),
)
if mibBuilder.loadTexts:
    lumAlarmHistoryEntry.setStatus("current")
_LumAlarmHistoryIndex_Type = Integer32
_LumAlarmHistoryIndex_Object = MibTableColumn
lumAlarmHistoryIndex = _LumAlarmHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 2, 1, 1),
    _LumAlarmHistoryIndex_Type()
)
lumAlarmHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmHistoryIndex.setStatus("current")


class _LumAlarmHistoryData_Type(DisplayString):
    """Custom type lumAlarmHistoryData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LumAlarmHistoryData_Type.__name__ = "DisplayString"
_LumAlarmHistoryData_Object = MibTableColumn
lumAlarmHistoryData = _LumAlarmHistoryData_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 2, 1, 2),
    _LumAlarmHistoryData_Type()
)
lumAlarmHistoryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmHistoryData.setStatus("current")
_LumAlarmSummary_ObjectIdentity = ObjectIdentity
lumAlarmSummary = _LumAlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5)
)
_LumAlarmSummaryGroup_ObjectIdentity = ObjectIdentity
lumAlarmSummaryGroup = _LumAlarmSummaryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1)
)
_LumAlarmSummaryState_Type = LumAlarmSeverity
_LumAlarmSummaryState_Object = MibScalar
lumAlarmSummaryState = _LumAlarmSummaryState_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1, 1),
    _LumAlarmSummaryState_Type()
)
lumAlarmSummaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmSummaryState.setStatus("current")
_LumAlarmSummaryCriticalStatus_Type = LumSignalState
_LumAlarmSummaryCriticalStatus_Object = MibScalar
lumAlarmSummaryCriticalStatus = _LumAlarmSummaryCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1, 2),
    _LumAlarmSummaryCriticalStatus_Type()
)
lumAlarmSummaryCriticalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmSummaryCriticalStatus.setStatus("current")
_LumAlarmSummaryMajorStatus_Type = LumSignalState
_LumAlarmSummaryMajorStatus_Object = MibScalar
lumAlarmSummaryMajorStatus = _LumAlarmSummaryMajorStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1, 3),
    _LumAlarmSummaryMajorStatus_Type()
)
lumAlarmSummaryMajorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmSummaryMajorStatus.setStatus("current")
_LumAlarmSummaryMinorStatus_Type = LumSignalState
_LumAlarmSummaryMinorStatus_Object = MibScalar
lumAlarmSummaryMinorStatus = _LumAlarmSummaryMinorStatus_Object(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1, 4),
    _LumAlarmSummaryMinorStatus_Type()
)
lumAlarmSummaryMinorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumAlarmSummaryMinorStatus.setStatus("current")
_LumAlarmTraps_ObjectIdentity = ObjectIdentity
lumAlarmTraps = _LumAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 10)
)

# Managed Objects groups


# Notification objects

lumAlarmSummaryChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 0, 1)
)
lumAlarmSummaryChangeTrap.setObjects(
      *(("LUMINOUS-SYSTEM-MIB", "lumAlarmSummaryState"),
        ("LUMINOUS-SYSTEM-MIB", "lumAlarmSummaryCriticalStatus"),
        ("LUMINOUS-SYSTEM-MIB", "lumAlarmSummaryMajorStatus"),
        ("LUMINOUS-SYSTEM-MIB", "lumAlarmSummaryMinorStatus"))
)
if mibBuilder.loadTexts:
    lumAlarmSummaryChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUMINOUS-SYSTEM-MIB",
    **{"luminous": luminous,
       "lumADM": lumADM,
       "lumSystemMIB": lumSystemMIB,
       "lumSoftwareDownload": lumSoftwareDownload,
       "lumDownLoadImageType": lumDownLoadImageType,
       "lumDownLoadHost": lumDownLoadHost,
       "lumDownLoadUsrName": lumDownLoadUsrName,
       "lumDownLoadPasswd": lumDownLoadPasswd,
       "lumDownLoadFilePath": lumDownLoadFilePath,
       "lumDownLoadVersion": lumDownLoadVersion,
       "lumDownLoadSlot": lumDownLoadSlot,
       "lumDownLoadTimeOut": lumDownLoadTimeOut,
       "lumDownLoadCmd": lumDownLoadCmd,
       "lumDownLoadStatus": lumDownLoadStatus,
       "lumDownLoadAbort": lumDownLoadAbort,
       "lumSystemReset": lumSystemReset,
       "lumSystemResetCardTable": lumSystemResetCardTable,
       "lumSystemResetCardEntry": lumSystemResetCardEntry,
       "lumSystemResetCardIndex": lumSystemResetCardIndex,
       "lumSystemResetCardCmd": lumSystemResetCardCmd,
       "lumSystemResetShelfCmd": lumSystemResetShelfCmd,
       "lumAlarms": lumAlarms,
       "lumAlarmV2Traps": lumAlarmV2Traps,
       "lumAlarmSummaryChangeTrap": lumAlarmSummaryChangeTrap,
       "lumAlarmType": lumAlarmType,
       "lumProvisionAlarmType": lumProvisionAlarmType,
       "lumAlarmCardAlarmType": lumAlarmCardAlarmType,
       "lumSysconAlarmType": lumSysconAlarmType,
       "lumT1AlarmType": lumT1AlarmType,
       "lumTEN100AlarmType": lumTEN100AlarmType,
       "lumSonetAlarmType": lumSonetAlarmType,
       "lumRingCardAlarmType": lumRingCardAlarmType,
       "lumUtilityAlarmType": lumUtilityAlarmType,
       "lumEquipmentAlarmType": lumEquipmentAlarmType,
       "lumDataFlowAlarmType": lumDataFlowAlarmType,
       "lumDataBaseAlarmType": lumDataBaseAlarmType,
       "lumPPPAlarmType": lumPPPAlarmType,
       "lumAlarmSource": lumAlarmSource,
       "lumAlarmSlotId": lumAlarmSlotId,
       "lumAlarmPortId": lumAlarmPortId,
       "lumAlarmStatus": lumAlarmStatus,
       "lumAlarmLog": lumAlarmLog,
       "lumAlarmActiveTable": lumAlarmActiveTable,
       "lumAlarmActiveEntry": lumAlarmActiveEntry,
       "lumAlarmActiveIndex": lumAlarmActiveIndex,
       "lumAlarmActiveType": lumAlarmActiveType,
       "lumAlarmActiveValue": lumAlarmActiveValue,
       "lumAlarmActiveStatus": lumAlarmActiveStatus,
       "lumAlarmActiveTimeStamp": lumAlarmActiveTimeStamp,
       "lumAlarmActiveSlotId": lumAlarmActiveSlotId,
       "lumAlarmActivePortId": lumAlarmActivePortId,
       "lumAlarmHistoryTable": lumAlarmHistoryTable,
       "lumAlarmHistoryEntry": lumAlarmHistoryEntry,
       "lumAlarmHistoryIndex": lumAlarmHistoryIndex,
       "lumAlarmHistoryData": lumAlarmHistoryData,
       "lumAlarmSummary": lumAlarmSummary,
       "lumAlarmSummaryGroup": lumAlarmSummaryGroup,
       "lumAlarmSummaryState": lumAlarmSummaryState,
       "lumAlarmSummaryCriticalStatus": lumAlarmSummaryCriticalStatus,
       "lumAlarmSummaryMajorStatus": lumAlarmSummaryMajorStatus,
       "lumAlarmSummaryMinorStatus": lumAlarmSummaryMinorStatus,
       "lumAlarmTraps": lumAlarmTraps}
)
