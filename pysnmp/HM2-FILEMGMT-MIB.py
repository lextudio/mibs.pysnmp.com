# SNMP MIB module (HM2-FILEMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-FILEMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:56 2024
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

(HmEnabledStatus,
 HmTimeSeconds1970,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "HmTimeSeconds1970",
    "hm2ConfigurationMibs")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hm2FileMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21)
)
hm2FileMgmtMib.setRevisions(
        ("2011-03-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2FileMgmtNotifications_ObjectIdentity = ObjectIdentity
hm2FileMgmtNotifications = _Hm2FileMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 0)
)
_Hm2FileMgmtMibObjects_ObjectIdentity = ObjectIdentity
hm2FileMgmtMibObjects = _Hm2FileMgmtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1)
)
_Hm2FileMgmtProfileGroup_ObjectIdentity = ObjectIdentity
hm2FileMgmtProfileGroup = _Hm2FileMgmtProfileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1)
)
_Hm2FMProfileTable_Object = MibTable
hm2FMProfileTable = _Hm2FMProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hm2FMProfileTable.setStatus("current")
_Hm2FMProfileEntry_Object = MibTableRow
hm2FMProfileEntry = _Hm2FMProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1)
)
hm2FMProfileEntry.setIndexNames(
    (0, "HM2-FILEMGMT-MIB", "hm2FMProfileStorageType"),
    (0, "HM2-FILEMGMT-MIB", "hm2FMProfileIndex"),
)
if mibBuilder.loadTexts:
    hm2FMProfileEntry.setStatus("current")


class _Hm2FMProfileStorageType_Type(Integer32):
    """Custom type hm2FMProfileStorageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("envm", 2),
          ("nvm", 1))
    )


_Hm2FMProfileStorageType_Type.__name__ = "Integer32"
_Hm2FMProfileStorageType_Object = MibTableColumn
hm2FMProfileStorageType = _Hm2FMProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 1),
    _Hm2FMProfileStorageType_Type()
)
hm2FMProfileStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMProfileStorageType.setStatus("current")


class _Hm2FMProfileIndex_Type(Integer32):
    """Custom type hm2FMProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hm2FMProfileIndex_Type.__name__ = "Integer32"
_Hm2FMProfileIndex_Object = MibTableColumn
hm2FMProfileIndex = _Hm2FMProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 2),
    _Hm2FMProfileIndex_Type()
)
hm2FMProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMProfileIndex.setStatus("current")


class _Hm2FMProfileName_Type(DisplayString):
    """Custom type hm2FMProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2FMProfileName_Type.__name__ = "DisplayString"
_Hm2FMProfileName_Object = MibTableColumn
hm2FMProfileName = _Hm2FMProfileName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 3),
    _Hm2FMProfileName_Type()
)
hm2FMProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMProfileName.setStatus("current")
_Hm2FMProfileDateTime_Type = HmTimeSeconds1970
_Hm2FMProfileDateTime_Object = MibTableColumn
hm2FMProfileDateTime = _Hm2FMProfileDateTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 4),
    _Hm2FMProfileDateTime_Type()
)
hm2FMProfileDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMProfileDateTime.setStatus("current")


class _Hm2FMProfileActive_Type(Integer32):
    """Custom type hm2FMProfileActive based on Integer32"""
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


_Hm2FMProfileActive_Type.__name__ = "Integer32"
_Hm2FMProfileActive_Object = MibTableColumn
hm2FMProfileActive = _Hm2FMProfileActive_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 5),
    _Hm2FMProfileActive_Type()
)
hm2FMProfileActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FMProfileActive.setStatus("current")


class _Hm2FMProfileAction_Type(Integer32):
    """Custom type hm2FMProfileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_Hm2FMProfileAction_Type.__name__ = "Integer32"
_Hm2FMProfileAction_Object = MibTableColumn
hm2FMProfileAction = _Hm2FMProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 6),
    _Hm2FMProfileAction_Type()
)
hm2FMProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FMProfileAction.setStatus("current")
_Hm2FMProfileDeviceType_Type = ObjectIdentifier
_Hm2FMProfileDeviceType_Object = MibTableColumn
hm2FMProfileDeviceType = _Hm2FMProfileDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 7),
    _Hm2FMProfileDeviceType_Type()
)
hm2FMProfileDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMProfileDeviceType.setStatus("current")
_Hm2FMProfileEncryptionActive_Type = TruthValue
_Hm2FMProfileEncryptionActive_Object = MibTableColumn
hm2FMProfileEncryptionActive = _Hm2FMProfileEncryptionActive_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 8),
    _Hm2FMProfileEncryptionActive_Type()
)
hm2FMProfileEncryptionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMProfileEncryptionActive.setStatus("current")
_Hm2FMProfileEncryptionVerified_Type = TruthValue
_Hm2FMProfileEncryptionVerified_Object = MibTableColumn
hm2FMProfileEncryptionVerified = _Hm2FMProfileEncryptionVerified_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 9),
    _Hm2FMProfileEncryptionVerified_Type()
)
hm2FMProfileEncryptionVerified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMProfileEncryptionVerified.setStatus("current")
_Hm2FMProfileSwMajorRelNum_Type = Integer32
_Hm2FMProfileSwMajorRelNum_Object = MibTableColumn
hm2FMProfileSwMajorRelNum = _Hm2FMProfileSwMajorRelNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 10),
    _Hm2FMProfileSwMajorRelNum_Type()
)
hm2FMProfileSwMajorRelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMProfileSwMajorRelNum.setStatus("current")
_Hm2FMProfileSwMinorRelNum_Type = Integer32
_Hm2FMProfileSwMinorRelNum_Object = MibTableColumn
hm2FMProfileSwMinorRelNum = _Hm2FMProfileSwMinorRelNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 11),
    _Hm2FMProfileSwMinorRelNum_Type()
)
hm2FMProfileSwMinorRelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMProfileSwMinorRelNum.setStatus("current")
_Hm2FMProfileSwBugfixRelNum_Type = Integer32
_Hm2FMProfileSwBugfixRelNum_Object = MibTableColumn
hm2FMProfileSwBugfixRelNum = _Hm2FMProfileSwBugfixRelNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 12),
    _Hm2FMProfileSwBugfixRelNum_Type()
)
hm2FMProfileSwBugfixRelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMProfileSwBugfixRelNum.setStatus("current")


class _Hm2FMProfileFingerprint_Type(DisplayString):
    """Custom type hm2FMProfileFingerprint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_Hm2FMProfileFingerprint_Type.__name__ = "DisplayString"
_Hm2FMProfileFingerprint_Object = MibTableColumn
hm2FMProfileFingerprint = _Hm2FMProfileFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 13),
    _Hm2FMProfileFingerprint_Type()
)
hm2FMProfileFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMProfileFingerprint.setStatus("current")
_Hm2FMProfileFingerprintVerified_Type = TruthValue
_Hm2FMProfileFingerprintVerified_Object = MibTableColumn
hm2FMProfileFingerprintVerified = _Hm2FMProfileFingerprintVerified_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 1, 1, 1, 14),
    _Hm2FMProfileFingerprintVerified_Type()
)
hm2FMProfileFingerprintVerified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMProfileFingerprintVerified.setStatus("current")
_Hm2FileMgmtActionGroup_ObjectIdentity = ObjectIdentity
hm2FileMgmtActionGroup = _Hm2FileMgmtActionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2)
)
_Hm2FMActionTable_Object = MibTable
hm2FMActionTable = _Hm2FMActionTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hm2FMActionTable.setStatus("current")
_Hm2FMActionEntry_Object = MibTableRow
hm2FMActionEntry = _Hm2FMActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1, 1)
)
hm2FMActionEntry.setIndexNames(
    (0, "HM2-FILEMGMT-MIB", "hm2FMActionType"),
    (0, "HM2-FILEMGMT-MIB", "hm2FMActionItemType"),
    (0, "HM2-FILEMGMT-MIB", "hm2FMActionSourceType"),
    (0, "HM2-FILEMGMT-MIB", "hm2FMActionDestinationType"),
)
if mibBuilder.loadTexts:
    hm2FMActionEntry.setStatus("current")


class _Hm2FMActionType_Type(Integer32):
    """Custom type hm2FMActionType based on Integer32"""
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
        *(("clear", 3),
          ("copy", 2),
          ("nop", 1),
          ("swap", 4))
    )


_Hm2FMActionType_Type.__name__ = "Integer32"
_Hm2FMActionType_Object = MibTableColumn
hm2FMActionType = _Hm2FMActionType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1, 1, 1),
    _Hm2FMActionType_Type()
)
hm2FMActionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2FMActionType.setStatus("current")


class _Hm2FMActionItemType_Type(Integer32):
    """Custom type hm2FMActionItemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              15,
              20,
              30,
              31,
              40,
              41,
              42,
              50,
              51,
              52,
              53,
              60,
              65,
              70,
              71,
              80,
              81,
              82,
              83,
              84,
              90,
              100)
        )
    )
    namedValues = NamedValues(
        *(("audittrail", 41),
          ("bootcode", 31),
          ("camcert", 80),
          ("camcertPEM", 84),
          ("cliBanner", 52),
          ("config", 10),
          ("edsFile", 90),
          ("eventlog", 40),
          ("filesystem", 15),
          ("firmware", 30),
          ("gsdmlFile", 100),
          ("httpsServerCert", 65),
          ("ldapCacert", 81),
          ("mailCacert", 82),
          ("none", 1),
          ("script", 20),
          ("sfpWhiteList", 51),
          ("sshkey", 60),
          ("sysinfo", 50),
          ("sysinfoall", 53),
          ("syslogCacert", 83),
          ("tcpdumpcap", 70),
          ("tcpdumpfilter", 71),
          ("traplog", 42))
    )


_Hm2FMActionItemType_Type.__name__ = "Integer32"
_Hm2FMActionItemType_Object = MibTableColumn
hm2FMActionItemType = _Hm2FMActionItemType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1, 1, 2),
    _Hm2FMActionItemType_Type()
)
hm2FMActionItemType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2FMActionItemType.setStatus("current")


class _Hm2FMActionSourceType_Type(Integer32):
    """Custom type hm2FMActionSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              10,
              11,
              20)
        )
    )
    namedValues = NamedValues(
        *(("buffered", 6),
          ("envm", 3),
          ("none", 1),
          ("nvm", 2),
          ("persistent", 7),
          ("runningConfig", 10),
          ("server", 20),
          ("system", 11))
    )


_Hm2FMActionSourceType_Type.__name__ = "Integer32"
_Hm2FMActionSourceType_Object = MibTableColumn
hm2FMActionSourceType = _Hm2FMActionSourceType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1, 1, 3),
    _Hm2FMActionSourceType_Type()
)
hm2FMActionSourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2FMActionSourceType.setStatus("current")


class _Hm2FMActionDestinationType_Type(Integer32):
    """Custom type hm2FMActionDestinationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11,
              20)
        )
    )
    namedValues = NamedValues(
        *(("envm", 3),
          ("none", 1),
          ("nvm", 2),
          ("runningConfig", 10),
          ("server", 20),
          ("system", 11))
    )


_Hm2FMActionDestinationType_Type.__name__ = "Integer32"
_Hm2FMActionDestinationType_Object = MibTableColumn
hm2FMActionDestinationType = _Hm2FMActionDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1, 1, 4),
    _Hm2FMActionDestinationType_Type()
)
hm2FMActionDestinationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2FMActionDestinationType.setStatus("current")
_Hm2FMActionActivate_Type = Integer32
_Hm2FMActionActivate_Object = MibTableColumn
hm2FMActionActivate = _Hm2FMActionActivate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 1, 1, 5),
    _Hm2FMActionActivate_Type()
)
hm2FMActionActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FMActionActivate.setStatus("current")


class _Hm2FMActionSourceData_Type(DisplayString):
    """Custom type hm2FMActionSourceData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2FMActionSourceData_Type.__name__ = "DisplayString"
_Hm2FMActionSourceData_Object = MibScalar
hm2FMActionSourceData = _Hm2FMActionSourceData_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 10),
    _Hm2FMActionSourceData_Type()
)
hm2FMActionSourceData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FMActionSourceData.setStatus("current")


class _Hm2FMActionDestinationData_Type(DisplayString):
    """Custom type hm2FMActionDestinationData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2FMActionDestinationData_Type.__name__ = "DisplayString"
_Hm2FMActionDestinationData_Object = MibScalar
hm2FMActionDestinationData = _Hm2FMActionDestinationData_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 11),
    _Hm2FMActionDestinationData_Type()
)
hm2FMActionDestinationData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FMActionDestinationData.setStatus("current")


class _Hm2FMActionActivateResult_Type(Integer32):
    """Custom type hm2FMActionActivateResult based on Integer32"""
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
          ("ok", 1),
          ("paramError", 2))
    )


_Hm2FMActionActivateResult_Type.__name__ = "Integer32"
_Hm2FMActionActivateResult_Object = MibScalar
hm2FMActionActivateResult = _Hm2FMActionActivateResult_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 12),
    _Hm2FMActionActivateResult_Type()
)
hm2FMActionActivateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMActionActivateResult.setStatus("current")
_Hm2FMActionActivateResultText_Type = DisplayString
_Hm2FMActionActivateResultText_Object = MibScalar
hm2FMActionActivateResultText = _Hm2FMActionActivateResultText_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 13),
    _Hm2FMActionActivateResultText_Type()
)
hm2FMActionActivateResultText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMActionActivateResultText.setStatus("current")


class _Hm2FMActionStatus_Type(Integer32):
    """Custom type hm2FMActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("running", 2))
    )


_Hm2FMActionStatus_Type.__name__ = "Integer32"
_Hm2FMActionStatus_Object = MibScalar
hm2FMActionStatus = _Hm2FMActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 14),
    _Hm2FMActionStatus_Type()
)
hm2FMActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMActionStatus.setStatus("current")


class _Hm2FMActionPercentReady_Type(Integer32):
    """Custom type hm2FMActionPercentReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hm2FMActionPercentReady_Type.__name__ = "Integer32"
_Hm2FMActionPercentReady_Object = MibScalar
hm2FMActionPercentReady = _Hm2FMActionPercentReady_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 15),
    _Hm2FMActionPercentReady_Type()
)
hm2FMActionPercentReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMActionPercentReady.setStatus("current")


class _Hm2FMActionResult_Type(Integer32):
    """Custom type hm2FMActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("ok", 1))
    )


_Hm2FMActionResult_Type.__name__ = "Integer32"
_Hm2FMActionResult_Object = MibScalar
hm2FMActionResult = _Hm2FMActionResult_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 16),
    _Hm2FMActionResult_Type()
)
hm2FMActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMActionResult.setStatus("current")
_Hm2FMActionResultText_Type = DisplayString
_Hm2FMActionResultText_Object = MibScalar
hm2FMActionResultText = _Hm2FMActionResultText_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 17),
    _Hm2FMActionResultText_Type()
)
hm2FMActionResultText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMActionResultText.setStatus("current")
_Hm2FMActionActivateKey_Type = Integer32
_Hm2FMActionActivateKey_Object = MibScalar
hm2FMActionActivateKey = _Hm2FMActionActivateKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 18),
    _Hm2FMActionActivateKey_Type()
)
hm2FMActionActivateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMActionActivateKey.setStatus("current")


class _Hm2FMActionContainerPassword_Type(DisplayString):
    """Custom type hm2FMActionContainerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_Hm2FMActionContainerPassword_Type.__name__ = "DisplayString"
_Hm2FMActionContainerPassword_Object = MibScalar
hm2FMActionContainerPassword = _Hm2FMActionContainerPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 19),
    _Hm2FMActionContainerPassword_Type()
)
hm2FMActionContainerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FMActionContainerPassword.setStatus("current")


class _Hm2FMActionParameter_Type(Integer32):
    """Custom type hm2FMActionParameter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("none", 1))
    )


_Hm2FMActionParameter_Type.__name__ = "Integer32"
_Hm2FMActionParameter_Object = MibScalar
hm2FMActionParameter = _Hm2FMActionParameter_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 20),
    _Hm2FMActionParameter_Type()
)
hm2FMActionParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FMActionParameter.setStatus("current")


class _Hm2FMActionSourceInterface_Type(InterfaceIndexOrZero):
    """Custom type hm2FMActionSourceInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2FMActionSourceInterface_Object = MibScalar
hm2FMActionSourceInterface = _Hm2FMActionSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 2, 21),
    _Hm2FMActionSourceInterface_Type()
)
hm2FMActionSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FMActionSourceInterface.setStatus("current")
_Hm2FileMgmtStatusGroup_ObjectIdentity = ObjectIdentity
hm2FileMgmtStatusGroup = _Hm2FileMgmtStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 3)
)


class _Hm2FMNvmState_Type(Integer32):
    """Custom type hm2FMNvmState based on Integer32"""
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
          ("ok", 1),
          ("outOfSync", 2))
    )


_Hm2FMNvmState_Type.__name__ = "Integer32"
_Hm2FMNvmState_Object = MibScalar
hm2FMNvmState = _Hm2FMNvmState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 3, 1),
    _Hm2FMNvmState_Type()
)
hm2FMNvmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMNvmState.setStatus("current")


class _Hm2FMEnvmState_Type(Integer32):
    """Custom type hm2FMEnvmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 3),
          ("ok", 1),
          ("outOfSync", 2))
    )


_Hm2FMEnvmState_Type.__name__ = "Integer32"
_Hm2FMEnvmState_Object = MibScalar
hm2FMEnvmState = _Hm2FMEnvmState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 3, 2),
    _Hm2FMEnvmState_Type()
)
hm2FMEnvmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMEnvmState.setStatus("current")


class _Hm2FMBootParamState_Type(Integer32):
    """Custom type hm2FMBootParamState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("outOfSync", 2))
    )


_Hm2FMBootParamState_Type.__name__ = "Integer32"
_Hm2FMBootParamState_Object = MibScalar
hm2FMBootParamState = _Hm2FMBootParamState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 3, 3),
    _Hm2FMBootParamState_Type()
)
hm2FMBootParamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FMBootParamState.setStatus("current")
_Hm2FileMgmtConfigGroup_ObjectIdentity = ObjectIdentity
hm2FileMgmtConfigGroup = _Hm2FileMgmtConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4)
)
_Hm2FileMgmtConfigWatchdogControl_ObjectIdentity = ObjectIdentity
hm2FileMgmtConfigWatchdogControl = _Hm2FileMgmtConfigWatchdogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1)
)


class _Hm2ConfigWatchdogAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2ConfigWatchdogAdminStatus based on HmEnabledStatus"""


_Hm2ConfigWatchdogAdminStatus_Object = MibScalar
hm2ConfigWatchdogAdminStatus = _Hm2ConfigWatchdogAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1, 1),
    _Hm2ConfigWatchdogAdminStatus_Type()
)
hm2ConfigWatchdogAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ConfigWatchdogAdminStatus.setStatus("current")
_Hm2ConfigWatchdogOperStatus_Type = HmEnabledStatus
_Hm2ConfigWatchdogOperStatus_Object = MibScalar
hm2ConfigWatchdogOperStatus = _Hm2ConfigWatchdogOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1, 2),
    _Hm2ConfigWatchdogOperStatus_Type()
)
hm2ConfigWatchdogOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ConfigWatchdogOperStatus.setStatus("current")


class _Hm2ConfigWatchdogTimeInterval_Type(Integer32):
    """Custom type hm2ConfigWatchdogTimeInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_Hm2ConfigWatchdogTimeInterval_Type.__name__ = "Integer32"
_Hm2ConfigWatchdogTimeInterval_Object = MibScalar
hm2ConfigWatchdogTimeInterval = _Hm2ConfigWatchdogTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1, 3),
    _Hm2ConfigWatchdogTimeInterval_Type()
)
hm2ConfigWatchdogTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ConfigWatchdogTimeInterval.setStatus("current")
_Hm2ConfigWatchdogTimerValue_Type = Integer32
_Hm2ConfigWatchdogTimerValue_Object = MibScalar
hm2ConfigWatchdogTimerValue = _Hm2ConfigWatchdogTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1, 4),
    _Hm2ConfigWatchdogTimerValue_Type()
)
hm2ConfigWatchdogTimerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ConfigWatchdogTimerValue.setStatus("current")
_Hm2ConfigWatchdogIPAddressType_Type = InetAddressType
_Hm2ConfigWatchdogIPAddressType_Object = MibScalar
hm2ConfigWatchdogIPAddressType = _Hm2ConfigWatchdogIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1, 5),
    _Hm2ConfigWatchdogIPAddressType_Type()
)
hm2ConfigWatchdogIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ConfigWatchdogIPAddressType.setStatus("current")
_Hm2ConfigWatchdogIPAddress_Type = InetAddress
_Hm2ConfigWatchdogIPAddress_Object = MibScalar
hm2ConfigWatchdogIPAddress = _Hm2ConfigWatchdogIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 1, 6),
    _Hm2ConfigWatchdogIPAddress_Type()
)
hm2ConfigWatchdogIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ConfigWatchdogIPAddress.setStatus("current")
_Hm2FileMgmtServerAccessGroup_ObjectIdentity = ObjectIdentity
hm2FileMgmtServerAccessGroup = _Hm2FileMgmtServerAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 2)
)


class _Hm2FMServerUserName_Type(DisplayString):
    """Custom type hm2FMServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2FMServerUserName_Type.__name__ = "DisplayString"
_Hm2FMServerUserName_Object = MibScalar
hm2FMServerUserName = _Hm2FMServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 2, 1),
    _Hm2FMServerUserName_Type()
)
hm2FMServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FMServerUserName.setStatus("current")


class _Hm2FMServerPassword_Type(DisplayString):
    """Custom type hm2FMServerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2FMServerPassword_Type.__name__ = "DisplayString"
_Hm2FMServerPassword_Object = MibScalar
hm2FMServerPassword = _Hm2FMServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 2, 2),
    _Hm2FMServerPassword_Type()
)
hm2FMServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FMServerPassword.setStatus("current")
_Hm2FileMgmtSecurityGroup_ObjectIdentity = ObjectIdentity
hm2FileMgmtSecurityGroup = _Hm2FileMgmtSecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 4)
)


class _Hm2FileMgmtConfigPasswordStatus_Type(TruthValue):
    """Custom type hm2FileMgmtConfigPasswordStatus based on TruthValue"""


_Hm2FileMgmtConfigPasswordStatus_Object = MibScalar
hm2FileMgmtConfigPasswordStatus = _Hm2FileMgmtConfigPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 4, 1),
    _Hm2FileMgmtConfigPasswordStatus_Type()
)
hm2FileMgmtConfigPasswordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FileMgmtConfigPasswordStatus.setStatus("current")


class _Hm2FileMgmtConfigPasswordChange_Type(DisplayString):
    """Custom type hm2FileMgmtConfigPasswordChange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2FileMgmtConfigPasswordChange_Type.__name__ = "DisplayString"
_Hm2FileMgmtConfigPasswordChange_Object = MibScalar
hm2FileMgmtConfigPasswordChange = _Hm2FileMgmtConfigPasswordChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 4, 2),
    _Hm2FileMgmtConfigPasswordChange_Type()
)
hm2FileMgmtConfigPasswordChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FileMgmtConfigPasswordChange.setStatus("current")


class _Hm2FileMgmtGlobalSourceInterface_Type(InterfaceIndexOrZero):
    """Custom type hm2FileMgmtGlobalSourceInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2FileMgmtGlobalSourceInterface_Object = MibScalar
hm2FileMgmtGlobalSourceInterface = _Hm2FileMgmtGlobalSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 9),
    _Hm2FileMgmtGlobalSourceInterface_Type()
)
hm2FileMgmtGlobalSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FileMgmtGlobalSourceInterface.setStatus("current")


class _Hm2FileMgmtConfigCompatibilityMode_Type(Integer32):
    """Custom type hm2FileMgmtConfigCompatibilityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("hiosV1V2", 2))
    )


_Hm2FileMgmtConfigCompatibilityMode_Type.__name__ = "Integer32"
_Hm2FileMgmtConfigCompatibilityMode_Object = MibScalar
hm2FileMgmtConfigCompatibilityMode = _Hm2FileMgmtConfigCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 1, 4, 10),
    _Hm2FileMgmtConfigCompatibilityMode_Type()
)
hm2FileMgmtConfigCompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FileMgmtConfigCompatibilityMode.setStatus("current")
_Hm2FileMgmtSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2FileMgmtSNMPExtensionGroup = _Hm2FileMgmtSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 3)
)
_Hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn_ObjectIdentity = ObjectIdentity
hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn = _Hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 1)
)
if mibBuilder.loadTexts:
    hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn.setStatus("current")
_Hm2FileMgmtSESCfgActivateErrorReturn_ObjectIdentity = ObjectIdentity
hm2FileMgmtSESCfgActivateErrorReturn = _Hm2FileMgmtSESCfgActivateErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 2)
)
if mibBuilder.loadTexts:
    hm2FileMgmtSESCfgActivateErrorReturn.setStatus("current")
_Hm2FileMgmtSESCfgActivateIncomlpeteReturn_ObjectIdentity = ObjectIdentity
hm2FileMgmtSESCfgActivateIncomlpeteReturn = _Hm2FileMgmtSESCfgActivateIncomlpeteReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 3)
)
if mibBuilder.loadTexts:
    hm2FileMgmtSESCfgActivateIncomlpeteReturn.setStatus("current")
_Hm2FileMgmtSESCfgMgrCopyCommandErrorReturn_ObjectIdentity = ObjectIdentity
hm2FileMgmtSESCfgMgrCopyCommandErrorReturn = _Hm2FileMgmtSESCfgMgrCopyCommandErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 4)
)
if mibBuilder.loadTexts:
    hm2FileMgmtSESCfgMgrCopyCommandErrorReturn.setStatus("current")
_Hm2FileMgmtSESCfgMgrClearCommandErrorReturn_ObjectIdentity = ObjectIdentity
hm2FileMgmtSESCfgMgrClearCommandErrorReturn = _Hm2FileMgmtSESCfgMgrClearCommandErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 5)
)
if mibBuilder.loadTexts:
    hm2FileMgmtSESCfgMgrClearCommandErrorReturn.setStatus("current")
_Hm2FileMgmtSESCfgMgrSwapCommandErrorReturn_ObjectIdentity = ObjectIdentity
hm2FileMgmtSESCfgMgrSwapCommandErrorReturn = _Hm2FileMgmtSESCfgMgrSwapCommandErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 6)
)
if mibBuilder.loadTexts:
    hm2FileMgmtSESCfgMgrSwapCommandErrorReturn.setStatus("current")
_Hm2FileMgmtSESCfgErrorReturn_ObjectIdentity = ObjectIdentity
hm2FileMgmtSESCfgErrorReturn = _Hm2FileMgmtSESCfgErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 7)
)
if mibBuilder.loadTexts:
    hm2FileMgmtSESCfgErrorReturn.setStatus("current")
_Hm2FileMgmtSESCfgMgrCommandActivateErrorReturn_ObjectIdentity = ObjectIdentity
hm2FileMgmtSESCfgMgrCommandActivateErrorReturn = _Hm2FileMgmtSESCfgMgrCommandActivateErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 3, 8)
)
if mibBuilder.loadTexts:
    hm2FileMgmtSESCfgMgrCommandActivateErrorReturn.setStatus("current")

# Managed Objects groups


# Notification objects

hm2ConfigurationSavedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 0, 1)
)
hm2ConfigurationSavedTrap.setObjects(
      *(("HM2-FILEMGMT-MIB", "hm2FMNvmState"),
        ("HM2-FILEMGMT-MIB", "hm2FMEnvmState"))
)
if mibBuilder.loadTexts:
    hm2ConfigurationSavedTrap.setStatus(
        "current"
    )

hm2ConfigurationChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 21, 0, 2)
)
hm2ConfigurationChangedTrap.setObjects(
    ("HM2-FILEMGMT-MIB", "hm2FMNvmState")
)
if mibBuilder.loadTexts:
    hm2ConfigurationChangedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-FILEMGMT-MIB",
    **{"hm2FileMgmtMib": hm2FileMgmtMib,
       "hm2FileMgmtNotifications": hm2FileMgmtNotifications,
       "hm2ConfigurationSavedTrap": hm2ConfigurationSavedTrap,
       "hm2ConfigurationChangedTrap": hm2ConfigurationChangedTrap,
       "hm2FileMgmtMibObjects": hm2FileMgmtMibObjects,
       "hm2FileMgmtProfileGroup": hm2FileMgmtProfileGroup,
       "hm2FMProfileTable": hm2FMProfileTable,
       "hm2FMProfileEntry": hm2FMProfileEntry,
       "hm2FMProfileStorageType": hm2FMProfileStorageType,
       "hm2FMProfileIndex": hm2FMProfileIndex,
       "hm2FMProfileName": hm2FMProfileName,
       "hm2FMProfileDateTime": hm2FMProfileDateTime,
       "hm2FMProfileActive": hm2FMProfileActive,
       "hm2FMProfileAction": hm2FMProfileAction,
       "hm2FMProfileDeviceType": hm2FMProfileDeviceType,
       "hm2FMProfileEncryptionActive": hm2FMProfileEncryptionActive,
       "hm2FMProfileEncryptionVerified": hm2FMProfileEncryptionVerified,
       "hm2FMProfileSwMajorRelNum": hm2FMProfileSwMajorRelNum,
       "hm2FMProfileSwMinorRelNum": hm2FMProfileSwMinorRelNum,
       "hm2FMProfileSwBugfixRelNum": hm2FMProfileSwBugfixRelNum,
       "hm2FMProfileFingerprint": hm2FMProfileFingerprint,
       "hm2FMProfileFingerprintVerified": hm2FMProfileFingerprintVerified,
       "hm2FileMgmtActionGroup": hm2FileMgmtActionGroup,
       "hm2FMActionTable": hm2FMActionTable,
       "hm2FMActionEntry": hm2FMActionEntry,
       "hm2FMActionType": hm2FMActionType,
       "hm2FMActionItemType": hm2FMActionItemType,
       "hm2FMActionSourceType": hm2FMActionSourceType,
       "hm2FMActionDestinationType": hm2FMActionDestinationType,
       "hm2FMActionActivate": hm2FMActionActivate,
       "hm2FMActionSourceData": hm2FMActionSourceData,
       "hm2FMActionDestinationData": hm2FMActionDestinationData,
       "hm2FMActionActivateResult": hm2FMActionActivateResult,
       "hm2FMActionActivateResultText": hm2FMActionActivateResultText,
       "hm2FMActionStatus": hm2FMActionStatus,
       "hm2FMActionPercentReady": hm2FMActionPercentReady,
       "hm2FMActionResult": hm2FMActionResult,
       "hm2FMActionResultText": hm2FMActionResultText,
       "hm2FMActionActivateKey": hm2FMActionActivateKey,
       "hm2FMActionContainerPassword": hm2FMActionContainerPassword,
       "hm2FMActionParameter": hm2FMActionParameter,
       "hm2FMActionSourceInterface": hm2FMActionSourceInterface,
       "hm2FileMgmtStatusGroup": hm2FileMgmtStatusGroup,
       "hm2FMNvmState": hm2FMNvmState,
       "hm2FMEnvmState": hm2FMEnvmState,
       "hm2FMBootParamState": hm2FMBootParamState,
       "hm2FileMgmtConfigGroup": hm2FileMgmtConfigGroup,
       "hm2FileMgmtConfigWatchdogControl": hm2FileMgmtConfigWatchdogControl,
       "hm2ConfigWatchdogAdminStatus": hm2ConfigWatchdogAdminStatus,
       "hm2ConfigWatchdogOperStatus": hm2ConfigWatchdogOperStatus,
       "hm2ConfigWatchdogTimeInterval": hm2ConfigWatchdogTimeInterval,
       "hm2ConfigWatchdogTimerValue": hm2ConfigWatchdogTimerValue,
       "hm2ConfigWatchdogIPAddressType": hm2ConfigWatchdogIPAddressType,
       "hm2ConfigWatchdogIPAddress": hm2ConfigWatchdogIPAddress,
       "hm2FileMgmtServerAccessGroup": hm2FileMgmtServerAccessGroup,
       "hm2FMServerUserName": hm2FMServerUserName,
       "hm2FMServerPassword": hm2FMServerPassword,
       "hm2FileMgmtSecurityGroup": hm2FileMgmtSecurityGroup,
       "hm2FileMgmtConfigPasswordStatus": hm2FileMgmtConfigPasswordStatus,
       "hm2FileMgmtConfigPasswordChange": hm2FileMgmtConfigPasswordChange,
       "hm2FileMgmtGlobalSourceInterface": hm2FileMgmtGlobalSourceInterface,
       "hm2FileMgmtConfigCompatibilityMode": hm2FileMgmtConfigCompatibilityMode,
       "hm2FileMgmtSNMPExtensionGroup": hm2FileMgmtSNMPExtensionGroup,
       "hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn": hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn,
       "hm2FileMgmtSESCfgActivateErrorReturn": hm2FileMgmtSESCfgActivateErrorReturn,
       "hm2FileMgmtSESCfgActivateIncomlpeteReturn": hm2FileMgmtSESCfgActivateIncomlpeteReturn,
       "hm2FileMgmtSESCfgMgrCopyCommandErrorReturn": hm2FileMgmtSESCfgMgrCopyCommandErrorReturn,
       "hm2FileMgmtSESCfgMgrClearCommandErrorReturn": hm2FileMgmtSESCfgMgrClearCommandErrorReturn,
       "hm2FileMgmtSESCfgMgrSwapCommandErrorReturn": hm2FileMgmtSESCfgMgrSwapCommandErrorReturn,
       "hm2FileMgmtSESCfgErrorReturn": hm2FileMgmtSESCfgErrorReturn,
       "hm2FileMgmtSESCfgMgrCommandActivateErrorReturn": hm2FileMgmtSESCfgMgrCommandActivateErrorReturn}
)
