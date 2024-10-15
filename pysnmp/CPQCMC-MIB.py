# SNMP MIB module (CPQCMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQCMC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:16 2024
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

(compaq,) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysDescr,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysDescr",
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

_CpqCmc_ObjectIdentity = ObjectIdentity
cpqCmc = _CpqCmc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153)
)
_CpqCmcMibRev_ObjectIdentity = ObjectIdentity
cpqCmcMibRev = _CpqCmcMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 1)
)


class _CpqCmcMibRevMajor_Type(Integer32):
    """Custom type cpqCmcMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqCmcMibRevMajor_Type.__name__ = "Integer32"
_CpqCmcMibRevMajor_Object = MibScalar
cpqCmcMibRevMajor = _CpqCmcMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 1, 1),
    _CpqCmcMibRevMajor_Type()
)
cpqCmcMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcMibRevMajor.setStatus("mandatory")


class _CpqCmcMibRevMinor_Type(Integer32):
    """Custom type cpqCmcMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqCmcMibRevMinor_Type.__name__ = "Integer32"
_CpqCmcMibRevMinor_Object = MibScalar
cpqCmcMibRevMinor = _CpqCmcMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 1, 2),
    _CpqCmcMibRevMinor_Type()
)
cpqCmcMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcMibRevMinor.setStatus("mandatory")


class _CpqCmcMibCondition_Type(Integer32):
    """Custom type cpqCmcMibCondition based on Integer32"""
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


_CpqCmcMibCondition_Type.__name__ = "Integer32"
_CpqCmcMibCondition_Object = MibScalar
cpqCmcMibCondition = _CpqCmcMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 1, 3),
    _CpqCmcMibCondition_Type()
)
cpqCmcMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcMibCondition.setStatus("mandatory")
_CpqCmcComponent_ObjectIdentity = ObjectIdentity
cpqCmcComponent = _CpqCmcComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2)
)
_CpqCmcInterface_ObjectIdentity = ObjectIdentity
cpqCmcInterface = _CpqCmcInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 1)
)
_CpqCmcOsCommon_ObjectIdentity = ObjectIdentity
cpqCmcOsCommon = _CpqCmcOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 1, 1)
)


class _CpqCmcOsCommonPollFreq_Type(Integer32):
    """Custom type cpqCmcOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqCmcOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqCmcOsCommonPollFreq_Object = MibScalar
cpqCmcOsCommonPollFreq = _CpqCmcOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 1, 1, 1),
    _CpqCmcOsCommonPollFreq_Type()
)
cpqCmcOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcOsCommonPollFreq.setStatus("mandatory")
_CpqCmcDevice_ObjectIdentity = ObjectIdentity
cpqCmcDevice = _CpqCmcDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2)
)


class _CpqCmcDeviceCondition_Type(Integer32):
    """Custom type cpqCmcDeviceCondition based on Integer32"""
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
        *(("fuseDC", 4),
          ("ok", 2),
          ("other", 1),
          ("overloadDC", 3))
    )


_CpqCmcDeviceCondition_Type.__name__ = "Integer32"
_CpqCmcDeviceCondition_Object = MibScalar
cpqCmcDeviceCondition = _CpqCmcDeviceCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 1),
    _CpqCmcDeviceCondition_Type()
)
cpqCmcDeviceCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcDeviceCondition.setStatus("mandatory")
_CpqCmcSetup_ObjectIdentity = ObjectIdentity
cpqCmcSetup = _CpqCmcSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2)
)
_CpqCmcSetupConfig_ObjectIdentity = ObjectIdentity
cpqCmcSetupConfig = _CpqCmcSetupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1)
)
_CpqCmcSetupGeneral_ObjectIdentity = ObjectIdentity
cpqCmcSetupGeneral = _CpqCmcSetupGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 1)
)


class _CpqCmcsetLanguage_Type(Integer32):
    """Custom type cpqCmcsetLanguage based on Integer32"""
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
        *(("dutch", 7),
          ("english", 2),
          ("french", 3),
          ("german", 5),
          ("italian", 4),
          ("japanese", 8),
          ("other", 1),
          ("spanish", 6))
    )


_CpqCmcsetLanguage_Type.__name__ = "Integer32"
_CpqCmcsetLanguage_Object = MibScalar
cpqCmcsetLanguage = _CpqCmcsetLanguage_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 1, 1),
    _CpqCmcsetLanguage_Type()
)
cpqCmcsetLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcsetLanguage.setStatus("mandatory")


class _CpqCmcsetTempUnit_Type(Integer32):
    """Custom type cpqCmcsetTempUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 2),
          ("fahrenheit", 3),
          ("other", 1))
    )


_CpqCmcsetTempUnit_Type.__name__ = "Integer32"
_CpqCmcsetTempUnit_Object = MibScalar
cpqCmcsetTempUnit = _CpqCmcsetTempUnit_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 1, 2),
    _CpqCmcsetTempUnit_Type()
)
cpqCmcsetTempUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcsetTempUnit.setStatus("mandatory")


class _CpqCmcsetAudibleAlarm_Type(Integer32):
    """Custom type cpqCmcsetAudibleAlarm based on Integer32"""
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
        *(("disableSilence", 3),
          ("enableSilence", 2),
          ("off", 4),
          ("other", 1))
    )


_CpqCmcsetAudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcsetAudibleAlarm_Object = MibScalar
cpqCmcsetAudibleAlarm = _CpqCmcsetAudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 1, 3),
    _CpqCmcsetAudibleAlarm_Type()
)
cpqCmcsetAudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcsetAudibleAlarm.setStatus("mandatory")


class _CpqCmcPassword_Type(DisplayString):
    """Custom type cpqCmcPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CpqCmcPassword_Type.__name__ = "DisplayString"
_CpqCmcPassword_Object = MibScalar
cpqCmcPassword = _CpqCmcPassword_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 1, 4),
    _CpqCmcPassword_Type()
)
cpqCmcPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcPassword.setStatus("mandatory")


class _CpqCmcPasswordOption_Type(Integer32):
    """Custom type cpqCmcPasswordOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcPasswordOption_Type.__name__ = "Integer32"
_CpqCmcPasswordOption_Object = MibScalar
cpqCmcPasswordOption = _CpqCmcPasswordOption_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 1, 5),
    _CpqCmcPasswordOption_Type()
)
cpqCmcPasswordOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcPasswordOption.setStatus("mandatory")


class _CpqCmcquitRelay1_Type(Integer32):
    """Custom type cpqCmcquitRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcquitRelay1_Type.__name__ = "Integer32"
_CpqCmcquitRelay1_Object = MibScalar
cpqCmcquitRelay1 = _CpqCmcquitRelay1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 1, 6),
    _CpqCmcquitRelay1_Type()
)
cpqCmcquitRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcquitRelay1.setStatus("mandatory")


class _CpqCmcquitRelay2_Type(Integer32):
    """Custom type cpqCmcquitRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcquitRelay2_Type.__name__ = "Integer32"
_CpqCmcquitRelay2_Object = MibScalar
cpqCmcquitRelay2 = _CpqCmcquitRelay2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 1, 7),
    _CpqCmcquitRelay2_Type()
)
cpqCmcquitRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcquitRelay2.setStatus("mandatory")


class _CpqCmclogicRelay1_Type(Integer32):
    """Custom type cpqCmclogicRelay1 based on Integer32"""
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
        *(("closeAtAlarm", 2),
          ("closeAtEPO", 4),
          ("openAtAlarm", 3),
          ("other", 1))
    )


_CpqCmclogicRelay1_Type.__name__ = "Integer32"
_CpqCmclogicRelay1_Object = MibScalar
cpqCmclogicRelay1 = _CpqCmclogicRelay1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 1, 8),
    _CpqCmclogicRelay1_Type()
)
cpqCmclogicRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmclogicRelay1.setStatus("mandatory")


class _CpqCmclogicRelay2_Type(Integer32):
    """Custom type cpqCmclogicRelay2 based on Integer32"""
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
        *(("closeAtAlarm", 2),
          ("closeAtEPO", 4),
          ("openAtAlarm", 3),
          ("other", 1))
    )


_CpqCmclogicRelay2_Type.__name__ = "Integer32"
_CpqCmclogicRelay2_Object = MibScalar
cpqCmclogicRelay2 = _CpqCmclogicRelay2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 1, 9),
    _CpqCmclogicRelay2_Type()
)
cpqCmclogicRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmclogicRelay2.setStatus("mandatory")
_CpqCmcSetupEvents_ObjectIdentity = ObjectIdentity
cpqCmcSetupEvents = _CpqCmcSetupEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2)
)
_CpqCmcSetupTemp1_ObjectIdentity = ObjectIdentity
cpqCmcSetupTemp1 = _CpqCmcSetupTemp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 1)
)


class _CpqCmcSetupTemp1Avail_Type(Integer32):
    """Custom type cpqCmcSetupTemp1Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupTemp1Avail_Type.__name__ = "Integer32"
_CpqCmcSetupTemp1Avail_Object = MibScalar
cpqCmcSetupTemp1Avail = _CpqCmcSetupTemp1Avail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 1, 1),
    _CpqCmcSetupTemp1Avail_Type()
)
cpqCmcSetupTemp1Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp1Avail.setStatus("mandatory")


class _CpqCmcSetupTemp1RelaysWarn_Type(Integer32):
    """Custom type cpqCmcSetupTemp1RelaysWarn based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupTemp1RelaysWarn_Type.__name__ = "Integer32"
_CpqCmcSetupTemp1RelaysWarn_Object = MibScalar
cpqCmcSetupTemp1RelaysWarn = _CpqCmcSetupTemp1RelaysWarn_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 1, 2),
    _CpqCmcSetupTemp1RelaysWarn_Type()
)
cpqCmcSetupTemp1RelaysWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp1RelaysWarn.setStatus("mandatory")


class _CpqCmcSetupTemp1RelaysMax_Type(Integer32):
    """Custom type cpqCmcSetupTemp1RelaysMax based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupTemp1RelaysMax_Type.__name__ = "Integer32"
_CpqCmcSetupTemp1RelaysMax_Object = MibScalar
cpqCmcSetupTemp1RelaysMax = _CpqCmcSetupTemp1RelaysMax_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 1, 3),
    _CpqCmcSetupTemp1RelaysMax_Type()
)
cpqCmcSetupTemp1RelaysMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp1RelaysMax.setStatus("mandatory")


class _CpqCmcSetupTemp1RelaysMin_Type(Integer32):
    """Custom type cpqCmcSetupTemp1RelaysMin based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupTemp1RelaysMin_Type.__name__ = "Integer32"
_CpqCmcSetupTemp1RelaysMin_Object = MibScalar
cpqCmcSetupTemp1RelaysMin = _CpqCmcSetupTemp1RelaysMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 1, 4),
    _CpqCmcSetupTemp1RelaysMin_Type()
)
cpqCmcSetupTemp1RelaysMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp1RelaysMin.setStatus("mandatory")


class _CpqCmcSetupTemp1AudibleAlarmWarn_Type(Integer32):
    """Custom type cpqCmcSetupTemp1AudibleAlarmWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupTemp1AudibleAlarmWarn_Type.__name__ = "Integer32"
_CpqCmcSetupTemp1AudibleAlarmWarn_Object = MibScalar
cpqCmcSetupTemp1AudibleAlarmWarn = _CpqCmcSetupTemp1AudibleAlarmWarn_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 1, 5),
    _CpqCmcSetupTemp1AudibleAlarmWarn_Type()
)
cpqCmcSetupTemp1AudibleAlarmWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp1AudibleAlarmWarn.setStatus("mandatory")


class _CpqCmcSetupTemp1AudibleAlarmMax_Type(Integer32):
    """Custom type cpqCmcSetupTemp1AudibleAlarmMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupTemp1AudibleAlarmMax_Type.__name__ = "Integer32"
_CpqCmcSetupTemp1AudibleAlarmMax_Object = MibScalar
cpqCmcSetupTemp1AudibleAlarmMax = _CpqCmcSetupTemp1AudibleAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 1, 6),
    _CpqCmcSetupTemp1AudibleAlarmMax_Type()
)
cpqCmcSetupTemp1AudibleAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp1AudibleAlarmMax.setStatus("mandatory")


class _CpqCmcSetupTemp1AudibleAlarmMin_Type(Integer32):
    """Custom type cpqCmcSetupTemp1AudibleAlarmMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupTemp1AudibleAlarmMin_Type.__name__ = "Integer32"
_CpqCmcSetupTemp1AudibleAlarmMin_Object = MibScalar
cpqCmcSetupTemp1AudibleAlarmMin = _CpqCmcSetupTemp1AudibleAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 1, 7),
    _CpqCmcSetupTemp1AudibleAlarmMin_Type()
)
cpqCmcSetupTemp1AudibleAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp1AudibleAlarmMin.setStatus("mandatory")
_CpqCmcSetupTemp2_ObjectIdentity = ObjectIdentity
cpqCmcSetupTemp2 = _CpqCmcSetupTemp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 2)
)


class _CpqCmcSetupTemp2Avail_Type(Integer32):
    """Custom type cpqCmcSetupTemp2Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupTemp2Avail_Type.__name__ = "Integer32"
_CpqCmcSetupTemp2Avail_Object = MibScalar
cpqCmcSetupTemp2Avail = _CpqCmcSetupTemp2Avail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 2, 1),
    _CpqCmcSetupTemp2Avail_Type()
)
cpqCmcSetupTemp2Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp2Avail.setStatus("mandatory")


class _CpqCmcSetupTemp2RelaysWarn_Type(Integer32):
    """Custom type cpqCmcSetupTemp2RelaysWarn based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupTemp2RelaysWarn_Type.__name__ = "Integer32"
_CpqCmcSetupTemp2RelaysWarn_Object = MibScalar
cpqCmcSetupTemp2RelaysWarn = _CpqCmcSetupTemp2RelaysWarn_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 2, 2),
    _CpqCmcSetupTemp2RelaysWarn_Type()
)
cpqCmcSetupTemp2RelaysWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp2RelaysWarn.setStatus("mandatory")


class _CpqCmcSetupTemp2RelaysMax_Type(Integer32):
    """Custom type cpqCmcSetupTemp2RelaysMax based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupTemp2RelaysMax_Type.__name__ = "Integer32"
_CpqCmcSetupTemp2RelaysMax_Object = MibScalar
cpqCmcSetupTemp2RelaysMax = _CpqCmcSetupTemp2RelaysMax_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 2, 3),
    _CpqCmcSetupTemp2RelaysMax_Type()
)
cpqCmcSetupTemp2RelaysMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp2RelaysMax.setStatus("mandatory")


class _CpqCmcSetupTemp2RelaysMin_Type(Integer32):
    """Custom type cpqCmcSetupTemp2RelaysMin based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupTemp2RelaysMin_Type.__name__ = "Integer32"
_CpqCmcSetupTemp2RelaysMin_Object = MibScalar
cpqCmcSetupTemp2RelaysMin = _CpqCmcSetupTemp2RelaysMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 2, 4),
    _CpqCmcSetupTemp2RelaysMin_Type()
)
cpqCmcSetupTemp2RelaysMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp2RelaysMin.setStatus("mandatory")


class _CpqCmcSetupTemp2AudibleAlarmWarn_Type(Integer32):
    """Custom type cpqCmcSetupTemp2AudibleAlarmWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupTemp2AudibleAlarmWarn_Type.__name__ = "Integer32"
_CpqCmcSetupTemp2AudibleAlarmWarn_Object = MibScalar
cpqCmcSetupTemp2AudibleAlarmWarn = _CpqCmcSetupTemp2AudibleAlarmWarn_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 2, 5),
    _CpqCmcSetupTemp2AudibleAlarmWarn_Type()
)
cpqCmcSetupTemp2AudibleAlarmWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp2AudibleAlarmWarn.setStatus("mandatory")


class _CpqCmcSetupTemp2AudibleAlarmMax_Type(Integer32):
    """Custom type cpqCmcSetupTemp2AudibleAlarmMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupTemp2AudibleAlarmMax_Type.__name__ = "Integer32"
_CpqCmcSetupTemp2AudibleAlarmMax_Object = MibScalar
cpqCmcSetupTemp2AudibleAlarmMax = _CpqCmcSetupTemp2AudibleAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 2, 6),
    _CpqCmcSetupTemp2AudibleAlarmMax_Type()
)
cpqCmcSetupTemp2AudibleAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp2AudibleAlarmMax.setStatus("mandatory")


class _CpqCmcSetupTemp2AudibleAlarmMin_Type(Integer32):
    """Custom type cpqCmcSetupTemp2AudibleAlarmMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupTemp2AudibleAlarmMin_Type.__name__ = "Integer32"
_CpqCmcSetupTemp2AudibleAlarmMin_Object = MibScalar
cpqCmcSetupTemp2AudibleAlarmMin = _CpqCmcSetupTemp2AudibleAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 2, 7),
    _CpqCmcSetupTemp2AudibleAlarmMin_Type()
)
cpqCmcSetupTemp2AudibleAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTemp2AudibleAlarmMin.setStatus("mandatory")
_CpqCmcSetupFan1_ObjectIdentity = ObjectIdentity
cpqCmcSetupFan1 = _CpqCmcSetupFan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 3)
)


class _CpqCmcSetupFan1Avail_Type(Integer32):
    """Custom type cpqCmcSetupFan1Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupFan1Avail_Type.__name__ = "Integer32"
_CpqCmcSetupFan1Avail_Object = MibScalar
cpqCmcSetupFan1Avail = _CpqCmcSetupFan1Avail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 3, 1),
    _CpqCmcSetupFan1Avail_Type()
)
cpqCmcSetupFan1Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupFan1Avail.setStatus("mandatory")


class _CpqCmcSetupFan1Relays_Type(Integer32):
    """Custom type cpqCmcSetupFan1Relays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupFan1Relays_Type.__name__ = "Integer32"
_CpqCmcSetupFan1Relays_Object = MibScalar
cpqCmcSetupFan1Relays = _CpqCmcSetupFan1Relays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 3, 2),
    _CpqCmcSetupFan1Relays_Type()
)
cpqCmcSetupFan1Relays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupFan1Relays.setStatus("mandatory")


class _CpqCmcSetupFan1AudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupFan1AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupFan1AudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupFan1AudibleAlarm_Object = MibScalar
cpqCmcSetupFan1AudibleAlarm = _CpqCmcSetupFan1AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 3, 3),
    _CpqCmcSetupFan1AudibleAlarm_Type()
)
cpqCmcSetupFan1AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupFan1AudibleAlarm.setStatus("mandatory")
_CpqCmcSetupFan2_ObjectIdentity = ObjectIdentity
cpqCmcSetupFan2 = _CpqCmcSetupFan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 4)
)


class _CpqCmcSetupFan2Avail_Type(Integer32):
    """Custom type cpqCmcSetupFan2Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupFan2Avail_Type.__name__ = "Integer32"
_CpqCmcSetupFan2Avail_Object = MibScalar
cpqCmcSetupFan2Avail = _CpqCmcSetupFan2Avail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 4, 1),
    _CpqCmcSetupFan2Avail_Type()
)
cpqCmcSetupFan2Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupFan2Avail.setStatus("mandatory")


class _CpqCmcSetupFan2Relays_Type(Integer32):
    """Custom type cpqCmcSetupFan2Relays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupFan2Relays_Type.__name__ = "Integer32"
_CpqCmcSetupFan2Relays_Object = MibScalar
cpqCmcSetupFan2Relays = _CpqCmcSetupFan2Relays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 4, 2),
    _CpqCmcSetupFan2Relays_Type()
)
cpqCmcSetupFan2Relays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupFan2Relays.setStatus("mandatory")


class _CpqCmcSetupFan2AudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupFan2AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupFan2AudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupFan2AudibleAlarm_Object = MibScalar
cpqCmcSetupFan2AudibleAlarm = _CpqCmcSetupFan2AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 4, 3),
    _CpqCmcSetupFan2AudibleAlarm_Type()
)
cpqCmcSetupFan2AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupFan2AudibleAlarm.setStatus("mandatory")
_CpqCmcSetupVoltage_ObjectIdentity = ObjectIdentity
cpqCmcSetupVoltage = _CpqCmcSetupVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 5)
)


class _CpqCmcSetupVoltageAvail_Type(Integer32):
    """Custom type cpqCmcSetupVoltageAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupVoltageAvail_Type.__name__ = "Integer32"
_CpqCmcSetupVoltageAvail_Object = MibScalar
cpqCmcSetupVoltageAvail = _CpqCmcSetupVoltageAvail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 5, 1),
    _CpqCmcSetupVoltageAvail_Type()
)
cpqCmcSetupVoltageAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupVoltageAvail.setStatus("mandatory")


class _CpqCmcSetupVoltageRelaysMax_Type(Integer32):
    """Custom type cpqCmcSetupVoltageRelaysMax based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupVoltageRelaysMax_Type.__name__ = "Integer32"
_CpqCmcSetupVoltageRelaysMax_Object = MibScalar
cpqCmcSetupVoltageRelaysMax = _CpqCmcSetupVoltageRelaysMax_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 5, 2),
    _CpqCmcSetupVoltageRelaysMax_Type()
)
cpqCmcSetupVoltageRelaysMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupVoltageRelaysMax.setStatus("mandatory")


class _CpqCmcSetupVoltageRelaysMin_Type(Integer32):
    """Custom type cpqCmcSetupVoltageRelaysMin based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupVoltageRelaysMin_Type.__name__ = "Integer32"
_CpqCmcSetupVoltageRelaysMin_Object = MibScalar
cpqCmcSetupVoltageRelaysMin = _CpqCmcSetupVoltageRelaysMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 5, 3),
    _CpqCmcSetupVoltageRelaysMin_Type()
)
cpqCmcSetupVoltageRelaysMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupVoltageRelaysMin.setStatus("mandatory")


class _CpqCmcSetupVoltageAudibleAlarmMax_Type(Integer32):
    """Custom type cpqCmcSetupVoltageAudibleAlarmMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupVoltageAudibleAlarmMax_Type.__name__ = "Integer32"
_CpqCmcSetupVoltageAudibleAlarmMax_Object = MibScalar
cpqCmcSetupVoltageAudibleAlarmMax = _CpqCmcSetupVoltageAudibleAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 5, 4),
    _CpqCmcSetupVoltageAudibleAlarmMax_Type()
)
cpqCmcSetupVoltageAudibleAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupVoltageAudibleAlarmMax.setStatus("mandatory")


class _CpqCmcSetupVoltageAudibleAlarmMin_Type(Integer32):
    """Custom type cpqCmcSetupVoltageAudibleAlarmMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupVoltageAudibleAlarmMin_Type.__name__ = "Integer32"
_CpqCmcSetupVoltageAudibleAlarmMin_Object = MibScalar
cpqCmcSetupVoltageAudibleAlarmMin = _CpqCmcSetupVoltageAudibleAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 5, 5),
    _CpqCmcSetupVoltageAudibleAlarmMin_Type()
)
cpqCmcSetupVoltageAudibleAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupVoltageAudibleAlarmMin.setStatus("mandatory")
_CpqCmcSetupHumidity_ObjectIdentity = ObjectIdentity
cpqCmcSetupHumidity = _CpqCmcSetupHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 6)
)


class _CpqCmcSetupHumidityAvail_Type(Integer32):
    """Custom type cpqCmcSetupHumidityAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupHumidityAvail_Type.__name__ = "Integer32"
_CpqCmcSetupHumidityAvail_Object = MibScalar
cpqCmcSetupHumidityAvail = _CpqCmcSetupHumidityAvail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 6, 1),
    _CpqCmcSetupHumidityAvail_Type()
)
cpqCmcSetupHumidityAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupHumidityAvail.setStatus("mandatory")


class _CpqCmcSetupHumidityRelaysMax_Type(Integer32):
    """Custom type cpqCmcSetupHumidityRelaysMax based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupHumidityRelaysMax_Type.__name__ = "Integer32"
_CpqCmcSetupHumidityRelaysMax_Object = MibScalar
cpqCmcSetupHumidityRelaysMax = _CpqCmcSetupHumidityRelaysMax_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 6, 2),
    _CpqCmcSetupHumidityRelaysMax_Type()
)
cpqCmcSetupHumidityRelaysMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupHumidityRelaysMax.setStatus("mandatory")


class _CpqCmcSetupHumidityRelaysMin_Type(Integer32):
    """Custom type cpqCmcSetupHumidityRelaysMin based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupHumidityRelaysMin_Type.__name__ = "Integer32"
_CpqCmcSetupHumidityRelaysMin_Object = MibScalar
cpqCmcSetupHumidityRelaysMin = _CpqCmcSetupHumidityRelaysMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 6, 3),
    _CpqCmcSetupHumidityRelaysMin_Type()
)
cpqCmcSetupHumidityRelaysMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupHumidityRelaysMin.setStatus("mandatory")


class _CpqCmcSetupHumidityAudibleAlarmMax_Type(Integer32):
    """Custom type cpqCmcSetupHumidityAudibleAlarmMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupHumidityAudibleAlarmMax_Type.__name__ = "Integer32"
_CpqCmcSetupHumidityAudibleAlarmMax_Object = MibScalar
cpqCmcSetupHumidityAudibleAlarmMax = _CpqCmcSetupHumidityAudibleAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 6, 4),
    _CpqCmcSetupHumidityAudibleAlarmMax_Type()
)
cpqCmcSetupHumidityAudibleAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupHumidityAudibleAlarmMax.setStatus("mandatory")


class _CpqCmcSetupHumidityAudibleAlarmMin_Type(Integer32):
    """Custom type cpqCmcSetupHumidityAudibleAlarmMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupHumidityAudibleAlarmMin_Type.__name__ = "Integer32"
_CpqCmcSetupHumidityAudibleAlarmMin_Object = MibScalar
cpqCmcSetupHumidityAudibleAlarmMin = _CpqCmcSetupHumidityAudibleAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 6, 5),
    _CpqCmcSetupHumidityAudibleAlarmMin_Type()
)
cpqCmcSetupHumidityAudibleAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupHumidityAudibleAlarmMin.setStatus("mandatory")
_CpqCmcSetupInput1_ObjectIdentity = ObjectIdentity
cpqCmcSetupInput1 = _CpqCmcSetupInput1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 7)
)


class _CpqCmcSetupInput1Avail_Type(Integer32):
    """Custom type cpqCmcSetupInput1Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupInput1Avail_Type.__name__ = "Integer32"
_CpqCmcSetupInput1Avail_Object = MibScalar
cpqCmcSetupInput1Avail = _CpqCmcSetupInput1Avail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 7, 1),
    _CpqCmcSetupInput1Avail_Type()
)
cpqCmcSetupInput1Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput1Avail.setStatus("mandatory")


class _CpqCmcSetupInput1Relays_Type(Integer32):
    """Custom type cpqCmcSetupInput1Relays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupInput1Relays_Type.__name__ = "Integer32"
_CpqCmcSetupInput1Relays_Object = MibScalar
cpqCmcSetupInput1Relays = _CpqCmcSetupInput1Relays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 7, 2),
    _CpqCmcSetupInput1Relays_Type()
)
cpqCmcSetupInput1Relays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput1Relays.setStatus("mandatory")


class _CpqCmcSetupInput1AudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupInput1AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupInput1AudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupInput1AudibleAlarm_Object = MibScalar
cpqCmcSetupInput1AudibleAlarm = _CpqCmcSetupInput1AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 7, 3),
    _CpqCmcSetupInput1AudibleAlarm_Type()
)
cpqCmcSetupInput1AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput1AudibleAlarm.setStatus("mandatory")


class _CpqCmcSetupInput1FansOff_Type(Integer32):
    """Custom type cpqCmcSetupInput1FansOff based on Integer32"""
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
        *(("both", 2),
          ("fan1", 3),
          ("fan2", 4),
          ("noFan", 5),
          ("other", 1))
    )


_CpqCmcSetupInput1FansOff_Type.__name__ = "Integer32"
_CpqCmcSetupInput1FansOff_Object = MibScalar
cpqCmcSetupInput1FansOff = _CpqCmcSetupInput1FansOff_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 7, 4),
    _CpqCmcSetupInput1FansOff_Type()
)
cpqCmcSetupInput1FansOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput1FansOff.setStatus("mandatory")


class _CpqCmcSetupInput1ShockSensor_Type(Integer32):
    """Custom type cpqCmcSetupInput1ShockSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_CpqCmcSetupInput1ShockSensor_Type.__name__ = "Integer32"
_CpqCmcSetupInput1ShockSensor_Object = MibScalar
cpqCmcSetupInput1ShockSensor = _CpqCmcSetupInput1ShockSensor_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 7, 5),
    _CpqCmcSetupInput1ShockSensor_Type()
)
cpqCmcSetupInput1ShockSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput1ShockSensor.setStatus("mandatory")


class _CpqCmcSetupInput1Description_Type(DisplayString):
    """Custom type cpqCmcSetupInput1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_CpqCmcSetupInput1Description_Type.__name__ = "DisplayString"
_CpqCmcSetupInput1Description_Object = MibScalar
cpqCmcSetupInput1Description = _CpqCmcSetupInput1Description_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 7, 6),
    _CpqCmcSetupInput1Description_Type()
)
cpqCmcSetupInput1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput1Description.setStatus("mandatory")


class _CpqCmcSetupInput1Lock_Type(Integer32):
    """Custom type cpqCmcSetupInput1Lock based on Integer32"""
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
        *(("both", 5),
          ("lock1", 3),
          ("lock2", 4),
          ("none", 2),
          ("other", 1))
    )


_CpqCmcSetupInput1Lock_Type.__name__ = "Integer32"
_CpqCmcSetupInput1Lock_Object = MibScalar
cpqCmcSetupInput1Lock = _CpqCmcSetupInput1Lock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 7, 7),
    _CpqCmcSetupInput1Lock_Type()
)
cpqCmcSetupInput1Lock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput1Lock.setStatus("mandatory")
_CpqCmcSetupInput2_ObjectIdentity = ObjectIdentity
cpqCmcSetupInput2 = _CpqCmcSetupInput2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 8)
)


class _CpqCmcSetupInput2Avail_Type(Integer32):
    """Custom type cpqCmcSetupInput2Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupInput2Avail_Type.__name__ = "Integer32"
_CpqCmcSetupInput2Avail_Object = MibScalar
cpqCmcSetupInput2Avail = _CpqCmcSetupInput2Avail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 8, 1),
    _CpqCmcSetupInput2Avail_Type()
)
cpqCmcSetupInput2Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput2Avail.setStatus("mandatory")


class _CpqCmcSetupInput2Relays_Type(Integer32):
    """Custom type cpqCmcSetupInput2Relays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupInput2Relays_Type.__name__ = "Integer32"
_CpqCmcSetupInput2Relays_Object = MibScalar
cpqCmcSetupInput2Relays = _CpqCmcSetupInput2Relays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 8, 2),
    _CpqCmcSetupInput2Relays_Type()
)
cpqCmcSetupInput2Relays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput2Relays.setStatus("mandatory")


class _CpqCmcSetupInput2AudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupInput2AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupInput2AudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupInput2AudibleAlarm_Object = MibScalar
cpqCmcSetupInput2AudibleAlarm = _CpqCmcSetupInput2AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 8, 3),
    _CpqCmcSetupInput2AudibleAlarm_Type()
)
cpqCmcSetupInput2AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput2AudibleAlarm.setStatus("mandatory")


class _CpqCmcSetupInput2FansOff_Type(Integer32):
    """Custom type cpqCmcSetupInput2FansOff based on Integer32"""
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
        *(("both", 2),
          ("fan1", 3),
          ("fan2", 4),
          ("noFan", 5),
          ("other", 1))
    )


_CpqCmcSetupInput2FansOff_Type.__name__ = "Integer32"
_CpqCmcSetupInput2FansOff_Object = MibScalar
cpqCmcSetupInput2FansOff = _CpqCmcSetupInput2FansOff_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 8, 4),
    _CpqCmcSetupInput2FansOff_Type()
)
cpqCmcSetupInput2FansOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput2FansOff.setStatus("mandatory")


class _CpqCmcSetupInput2ShockSensor_Type(Integer32):
    """Custom type cpqCmcSetupInput2ShockSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_CpqCmcSetupInput2ShockSensor_Type.__name__ = "Integer32"
_CpqCmcSetupInput2ShockSensor_Object = MibScalar
cpqCmcSetupInput2ShockSensor = _CpqCmcSetupInput2ShockSensor_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 8, 5),
    _CpqCmcSetupInput2ShockSensor_Type()
)
cpqCmcSetupInput2ShockSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput2ShockSensor.setStatus("mandatory")


class _CpqCmcSetupInput2Description_Type(DisplayString):
    """Custom type cpqCmcSetupInput2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_CpqCmcSetupInput2Description_Type.__name__ = "DisplayString"
_CpqCmcSetupInput2Description_Object = MibScalar
cpqCmcSetupInput2Description = _CpqCmcSetupInput2Description_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 8, 6),
    _CpqCmcSetupInput2Description_Type()
)
cpqCmcSetupInput2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput2Description.setStatus("mandatory")


class _CpqCmcSetupInput2Lock_Type(Integer32):
    """Custom type cpqCmcSetupInput2Lock based on Integer32"""
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
        *(("both", 5),
          ("lock1", 3),
          ("lock2", 4),
          ("none", 2),
          ("other", 1))
    )


_CpqCmcSetupInput2Lock_Type.__name__ = "Integer32"
_CpqCmcSetupInput2Lock_Object = MibScalar
cpqCmcSetupInput2Lock = _CpqCmcSetupInput2Lock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 8, 7),
    _CpqCmcSetupInput2Lock_Type()
)
cpqCmcSetupInput2Lock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput2Lock.setStatus("mandatory")
_CpqCmcSetupInput3_ObjectIdentity = ObjectIdentity
cpqCmcSetupInput3 = _CpqCmcSetupInput3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 9)
)


class _CpqCmcSetupInput3Avail_Type(Integer32):
    """Custom type cpqCmcSetupInput3Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupInput3Avail_Type.__name__ = "Integer32"
_CpqCmcSetupInput3Avail_Object = MibScalar
cpqCmcSetupInput3Avail = _CpqCmcSetupInput3Avail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 9, 1),
    _CpqCmcSetupInput3Avail_Type()
)
cpqCmcSetupInput3Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput3Avail.setStatus("mandatory")


class _CpqCmcSetupInput3Relays_Type(Integer32):
    """Custom type cpqCmcSetupInput3Relays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupInput3Relays_Type.__name__ = "Integer32"
_CpqCmcSetupInput3Relays_Object = MibScalar
cpqCmcSetupInput3Relays = _CpqCmcSetupInput3Relays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 9, 2),
    _CpqCmcSetupInput3Relays_Type()
)
cpqCmcSetupInput3Relays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput3Relays.setStatus("mandatory")


class _CpqCmcSetupInput3AudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupInput3AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupInput3AudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupInput3AudibleAlarm_Object = MibScalar
cpqCmcSetupInput3AudibleAlarm = _CpqCmcSetupInput3AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 9, 3),
    _CpqCmcSetupInput3AudibleAlarm_Type()
)
cpqCmcSetupInput3AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput3AudibleAlarm.setStatus("mandatory")


class _CpqCmcSetupInput3FansOff_Type(Integer32):
    """Custom type cpqCmcSetupInput3FansOff based on Integer32"""
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
        *(("both", 2),
          ("fan1", 3),
          ("fan2", 4),
          ("noFan", 5),
          ("other", 1))
    )


_CpqCmcSetupInput3FansOff_Type.__name__ = "Integer32"
_CpqCmcSetupInput3FansOff_Object = MibScalar
cpqCmcSetupInput3FansOff = _CpqCmcSetupInput3FansOff_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 9, 4),
    _CpqCmcSetupInput3FansOff_Type()
)
cpqCmcSetupInput3FansOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput3FansOff.setStatus("mandatory")


class _CpqCmcSetupInput3ShockSensor_Type(Integer32):
    """Custom type cpqCmcSetupInput3ShockSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_CpqCmcSetupInput3ShockSensor_Type.__name__ = "Integer32"
_CpqCmcSetupInput3ShockSensor_Object = MibScalar
cpqCmcSetupInput3ShockSensor = _CpqCmcSetupInput3ShockSensor_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 9, 5),
    _CpqCmcSetupInput3ShockSensor_Type()
)
cpqCmcSetupInput3ShockSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput3ShockSensor.setStatus("mandatory")


class _CpqCmcSetupInput3Description_Type(DisplayString):
    """Custom type cpqCmcSetupInput3Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_CpqCmcSetupInput3Description_Type.__name__ = "DisplayString"
_CpqCmcSetupInput3Description_Object = MibScalar
cpqCmcSetupInput3Description = _CpqCmcSetupInput3Description_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 9, 6),
    _CpqCmcSetupInput3Description_Type()
)
cpqCmcSetupInput3Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput3Description.setStatus("mandatory")


class _CpqCmcSetupInput3Lock_Type(Integer32):
    """Custom type cpqCmcSetupInput3Lock based on Integer32"""
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
        *(("both", 5),
          ("lock1", 3),
          ("lock2", 4),
          ("none", 2),
          ("other", 1))
    )


_CpqCmcSetupInput3Lock_Type.__name__ = "Integer32"
_CpqCmcSetupInput3Lock_Object = MibScalar
cpqCmcSetupInput3Lock = _CpqCmcSetupInput3Lock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 9, 7),
    _CpqCmcSetupInput3Lock_Type()
)
cpqCmcSetupInput3Lock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput3Lock.setStatus("mandatory")
_CpqCmcSetupInput4_ObjectIdentity = ObjectIdentity
cpqCmcSetupInput4 = _CpqCmcSetupInput4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 10)
)


class _CpqCmcSetupInput4Avail_Type(Integer32):
    """Custom type cpqCmcSetupInput4Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupInput4Avail_Type.__name__ = "Integer32"
_CpqCmcSetupInput4Avail_Object = MibScalar
cpqCmcSetupInput4Avail = _CpqCmcSetupInput4Avail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 10, 1),
    _CpqCmcSetupInput4Avail_Type()
)
cpqCmcSetupInput4Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput4Avail.setStatus("mandatory")


class _CpqCmcSetupInput4Relays_Type(Integer32):
    """Custom type cpqCmcSetupInput4Relays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupInput4Relays_Type.__name__ = "Integer32"
_CpqCmcSetupInput4Relays_Object = MibScalar
cpqCmcSetupInput4Relays = _CpqCmcSetupInput4Relays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 10, 2),
    _CpqCmcSetupInput4Relays_Type()
)
cpqCmcSetupInput4Relays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput4Relays.setStatus("mandatory")


class _CpqCmcSetupInput4AudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupInput4AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupInput4AudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupInput4AudibleAlarm_Object = MibScalar
cpqCmcSetupInput4AudibleAlarm = _CpqCmcSetupInput4AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 10, 3),
    _CpqCmcSetupInput4AudibleAlarm_Type()
)
cpqCmcSetupInput4AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput4AudibleAlarm.setStatus("mandatory")


class _CpqCmcSetupInput4FansOff_Type(Integer32):
    """Custom type cpqCmcSetupInput4FansOff based on Integer32"""
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
        *(("both", 2),
          ("fan1", 3),
          ("fan2", 4),
          ("noFan", 5),
          ("other", 1))
    )


_CpqCmcSetupInput4FansOff_Type.__name__ = "Integer32"
_CpqCmcSetupInput4FansOff_Object = MibScalar
cpqCmcSetupInput4FansOff = _CpqCmcSetupInput4FansOff_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 10, 4),
    _CpqCmcSetupInput4FansOff_Type()
)
cpqCmcSetupInput4FansOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput4FansOff.setStatus("mandatory")


class _CpqCmcSetupInput4ShockSensor_Type(Integer32):
    """Custom type cpqCmcSetupInput4ShockSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_CpqCmcSetupInput4ShockSensor_Type.__name__ = "Integer32"
_CpqCmcSetupInput4ShockSensor_Object = MibScalar
cpqCmcSetupInput4ShockSensor = _CpqCmcSetupInput4ShockSensor_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 10, 5),
    _CpqCmcSetupInput4ShockSensor_Type()
)
cpqCmcSetupInput4ShockSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput4ShockSensor.setStatus("mandatory")


class _CpqCmcSetupInput4Description_Type(DisplayString):
    """Custom type cpqCmcSetupInput4Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_CpqCmcSetupInput4Description_Type.__name__ = "DisplayString"
_CpqCmcSetupInput4Description_Object = MibScalar
cpqCmcSetupInput4Description = _CpqCmcSetupInput4Description_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 10, 6),
    _CpqCmcSetupInput4Description_Type()
)
cpqCmcSetupInput4Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput4Description.setStatus("mandatory")


class _CpqCmcSetupInput4Lock_Type(Integer32):
    """Custom type cpqCmcSetupInput4Lock based on Integer32"""
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
        *(("both", 5),
          ("lock1", 3),
          ("lock2", 4),
          ("none", 2),
          ("other", 1))
    )


_CpqCmcSetupInput4Lock_Type.__name__ = "Integer32"
_CpqCmcSetupInput4Lock_Object = MibScalar
cpqCmcSetupInput4Lock = _CpqCmcSetupInput4Lock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 10, 7),
    _CpqCmcSetupInput4Lock_Type()
)
cpqCmcSetupInput4Lock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupInput4Lock.setStatus("mandatory")
_CpqCmcSetupLock1_ObjectIdentity = ObjectIdentity
cpqCmcSetupLock1 = _CpqCmcSetupLock1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 11)
)


class _CpqCmcSetupLock1Avail_Type(Integer32):
    """Custom type cpqCmcSetupLock1Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupLock1Avail_Type.__name__ = "Integer32"
_CpqCmcSetupLock1Avail_Object = MibScalar
cpqCmcSetupLock1Avail = _CpqCmcSetupLock1Avail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 11, 1),
    _CpqCmcSetupLock1Avail_Type()
)
cpqCmcSetupLock1Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock1Avail.setStatus("mandatory")


class _CpqCmcSetupLock1Relays_Type(Integer32):
    """Custom type cpqCmcSetupLock1Relays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupLock1Relays_Type.__name__ = "Integer32"
_CpqCmcSetupLock1Relays_Object = MibScalar
cpqCmcSetupLock1Relays = _CpqCmcSetupLock1Relays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 11, 2),
    _CpqCmcSetupLock1Relays_Type()
)
cpqCmcSetupLock1Relays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock1Relays.setStatus("mandatory")


class _CpqCmcSetupLock1RelaysDevice_Type(Integer32):
    """Custom type cpqCmcSetupLock1RelaysDevice based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupLock1RelaysDevice_Type.__name__ = "Integer32"
_CpqCmcSetupLock1RelaysDevice_Object = MibScalar
cpqCmcSetupLock1RelaysDevice = _CpqCmcSetupLock1RelaysDevice_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 11, 3),
    _CpqCmcSetupLock1RelaysDevice_Type()
)
cpqCmcSetupLock1RelaysDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock1RelaysDevice.setStatus("mandatory")


class _CpqCmcSetupLock1AudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupLock1AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupLock1AudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupLock1AudibleAlarm_Object = MibScalar
cpqCmcSetupLock1AudibleAlarm = _CpqCmcSetupLock1AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 11, 4),
    _CpqCmcSetupLock1AudibleAlarm_Type()
)
cpqCmcSetupLock1AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock1AudibleAlarm.setStatus("mandatory")


class _CpqCmcSetupLock1AudibleAlarmDevice_Type(Integer32):
    """Custom type cpqCmcSetupLock1AudibleAlarmDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupLock1AudibleAlarmDevice_Type.__name__ = "Integer32"
_CpqCmcSetupLock1AudibleAlarmDevice_Object = MibScalar
cpqCmcSetupLock1AudibleAlarmDevice = _CpqCmcSetupLock1AudibleAlarmDevice_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 11, 5),
    _CpqCmcSetupLock1AudibleAlarmDevice_Type()
)
cpqCmcSetupLock1AudibleAlarmDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock1AudibleAlarmDevice.setStatus("mandatory")


class _CpqCmcSetupLock1Time_Type(Integer32):
    """Custom type cpqCmcSetupLock1Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 600),
    )


_CpqCmcSetupLock1Time_Type.__name__ = "Integer32"
_CpqCmcSetupLock1Time_Object = MibScalar
cpqCmcSetupLock1Time = _CpqCmcSetupLock1Time_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 11, 6),
    _CpqCmcSetupLock1Time_Type()
)
cpqCmcSetupLock1Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock1Time.setStatus("mandatory")


class _CpqCmcSetupLock1PwrFailUnlock_Type(Integer32):
    """Custom type cpqCmcSetupLock1PwrFailUnlock based on Integer32"""
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
        *(("auto", 3),
          ("disabled", 2),
          ("manual", 4),
          ("other", 1))
    )


_CpqCmcSetupLock1PwrFailUnlock_Type.__name__ = "Integer32"
_CpqCmcSetupLock1PwrFailUnlock_Object = MibScalar
cpqCmcSetupLock1PwrFailUnlock = _CpqCmcSetupLock1PwrFailUnlock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 11, 7),
    _CpqCmcSetupLock1PwrFailUnlock_Type()
)
cpqCmcSetupLock1PwrFailUnlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock1PwrFailUnlock.setStatus("mandatory")


class _CpqCmcSetupLock1BattLowUnlock_Type(Integer32):
    """Custom type cpqCmcSetupLock1BattLowUnlock based on Integer32"""
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
        *(("auto", 3),
          ("disabled", 2),
          ("manual", 4),
          ("other", 1))
    )


_CpqCmcSetupLock1BattLowUnlock_Type.__name__ = "Integer32"
_CpqCmcSetupLock1BattLowUnlock_Object = MibScalar
cpqCmcSetupLock1BattLowUnlock = _CpqCmcSetupLock1BattLowUnlock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 11, 8),
    _CpqCmcSetupLock1BattLowUnlock_Type()
)
cpqCmcSetupLock1BattLowUnlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock1BattLowUnlock.setStatus("mandatory")


class _CpqCmcSetupLock1NetFailUnlock_Type(Integer32):
    """Custom type cpqCmcSetupLock1NetFailUnlock based on Integer32"""
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
        *(("auto", 3),
          ("disabled", 2),
          ("manual", 4),
          ("other", 1))
    )


_CpqCmcSetupLock1NetFailUnlock_Type.__name__ = "Integer32"
_CpqCmcSetupLock1NetFailUnlock_Object = MibScalar
cpqCmcSetupLock1NetFailUnlock = _CpqCmcSetupLock1NetFailUnlock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 11, 9),
    _CpqCmcSetupLock1NetFailUnlock_Type()
)
cpqCmcSetupLock1NetFailUnlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock1NetFailUnlock.setStatus("mandatory")


class _CpqCmcSetupLock1LifeFailUnlock_Type(Integer32):
    """Custom type cpqCmcSetupLock1LifeFailUnlock based on Integer32"""
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
        *(("auto", 3),
          ("disabled", 2),
          ("manual", 4),
          ("other", 1))
    )


_CpqCmcSetupLock1LifeFailUnlock_Type.__name__ = "Integer32"
_CpqCmcSetupLock1LifeFailUnlock_Object = MibScalar
cpqCmcSetupLock1LifeFailUnlock = _CpqCmcSetupLock1LifeFailUnlock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 11, 10),
    _CpqCmcSetupLock1LifeFailUnlock_Type()
)
cpqCmcSetupLock1LifeFailUnlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock1LifeFailUnlock.setStatus("mandatory")
_CpqCmcSetupLock2_ObjectIdentity = ObjectIdentity
cpqCmcSetupLock2 = _CpqCmcSetupLock2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 12)
)


class _CpqCmcSetupLock2Avail_Type(Integer32):
    """Custom type cpqCmcSetupLock2Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupLock2Avail_Type.__name__ = "Integer32"
_CpqCmcSetupLock2Avail_Object = MibScalar
cpqCmcSetupLock2Avail = _CpqCmcSetupLock2Avail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 12, 1),
    _CpqCmcSetupLock2Avail_Type()
)
cpqCmcSetupLock2Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock2Avail.setStatus("mandatory")


class _CpqCmcSetupLock2Relays_Type(Integer32):
    """Custom type cpqCmcSetupLock2Relays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupLock2Relays_Type.__name__ = "Integer32"
_CpqCmcSetupLock2Relays_Object = MibScalar
cpqCmcSetupLock2Relays = _CpqCmcSetupLock2Relays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 12, 2),
    _CpqCmcSetupLock2Relays_Type()
)
cpqCmcSetupLock2Relays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock2Relays.setStatus("mandatory")


class _CpqCmcSetupLock2RelaysDevice_Type(Integer32):
    """Custom type cpqCmcSetupLock2RelaysDevice based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupLock2RelaysDevice_Type.__name__ = "Integer32"
_CpqCmcSetupLock2RelaysDevice_Object = MibScalar
cpqCmcSetupLock2RelaysDevice = _CpqCmcSetupLock2RelaysDevice_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 12, 3),
    _CpqCmcSetupLock2RelaysDevice_Type()
)
cpqCmcSetupLock2RelaysDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock2RelaysDevice.setStatus("mandatory")


class _CpqCmcSetupLock2AudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupLock2AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupLock2AudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupLock2AudibleAlarm_Object = MibScalar
cpqCmcSetupLock2AudibleAlarm = _CpqCmcSetupLock2AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 12, 4),
    _CpqCmcSetupLock2AudibleAlarm_Type()
)
cpqCmcSetupLock2AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock2AudibleAlarm.setStatus("mandatory")


class _CpqCmcSetupLock2AudibleAlarmDevice_Type(Integer32):
    """Custom type cpqCmcSetupLock2AudibleAlarmDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupLock2AudibleAlarmDevice_Type.__name__ = "Integer32"
_CpqCmcSetupLock2AudibleAlarmDevice_Object = MibScalar
cpqCmcSetupLock2AudibleAlarmDevice = _CpqCmcSetupLock2AudibleAlarmDevice_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 12, 5),
    _CpqCmcSetupLock2AudibleAlarmDevice_Type()
)
cpqCmcSetupLock2AudibleAlarmDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock2AudibleAlarmDevice.setStatus("mandatory")


class _CpqCmcSetupLock2Time_Type(Integer32):
    """Custom type cpqCmcSetupLock2Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 600),
    )


_CpqCmcSetupLock2Time_Type.__name__ = "Integer32"
_CpqCmcSetupLock2Time_Object = MibScalar
cpqCmcSetupLock2Time = _CpqCmcSetupLock2Time_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 12, 6),
    _CpqCmcSetupLock2Time_Type()
)
cpqCmcSetupLock2Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock2Time.setStatus("mandatory")


class _CpqCmcSetupLock2PwrFailUnlock_Type(Integer32):
    """Custom type cpqCmcSetupLock2PwrFailUnlock based on Integer32"""
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
        *(("auto", 3),
          ("disabled", 2),
          ("manual", 4),
          ("other", 1))
    )


_CpqCmcSetupLock2PwrFailUnlock_Type.__name__ = "Integer32"
_CpqCmcSetupLock2PwrFailUnlock_Object = MibScalar
cpqCmcSetupLock2PwrFailUnlock = _CpqCmcSetupLock2PwrFailUnlock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 12, 7),
    _CpqCmcSetupLock2PwrFailUnlock_Type()
)
cpqCmcSetupLock2PwrFailUnlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock2PwrFailUnlock.setStatus("mandatory")


class _CpqCmcSetupLock2BattLowUnlock_Type(Integer32):
    """Custom type cpqCmcSetupLock2BattLowUnlock based on Integer32"""
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
        *(("auto", 3),
          ("disabled", 2),
          ("manual", 4),
          ("other", 1))
    )


_CpqCmcSetupLock2BattLowUnlock_Type.__name__ = "Integer32"
_CpqCmcSetupLock2BattLowUnlock_Object = MibScalar
cpqCmcSetupLock2BattLowUnlock = _CpqCmcSetupLock2BattLowUnlock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 12, 8),
    _CpqCmcSetupLock2BattLowUnlock_Type()
)
cpqCmcSetupLock2BattLowUnlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock2BattLowUnlock.setStatus("mandatory")


class _CpqCmcSetupLock2NetFailUnlock_Type(Integer32):
    """Custom type cpqCmcSetupLock2NetFailUnlock based on Integer32"""
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
        *(("auto", 3),
          ("disabled", 2),
          ("manual", 4),
          ("other", 1))
    )


_CpqCmcSetupLock2NetFailUnlock_Type.__name__ = "Integer32"
_CpqCmcSetupLock2NetFailUnlock_Object = MibScalar
cpqCmcSetupLock2NetFailUnlock = _CpqCmcSetupLock2NetFailUnlock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 12, 9),
    _CpqCmcSetupLock2NetFailUnlock_Type()
)
cpqCmcSetupLock2NetFailUnlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock2NetFailUnlock.setStatus("mandatory")


class _CpqCmcSetupLock2LifeFailUnlock_Type(Integer32):
    """Custom type cpqCmcSetupLock2LifeFailUnlock based on Integer32"""
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
        *(("auto", 3),
          ("disabled", 2),
          ("manual", 4),
          ("other", 1))
    )


_CpqCmcSetupLock2LifeFailUnlock_Type.__name__ = "Integer32"
_CpqCmcSetupLock2LifeFailUnlock_Object = MibScalar
cpqCmcSetupLock2LifeFailUnlock = _CpqCmcSetupLock2LifeFailUnlock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 12, 10),
    _CpqCmcSetupLock2LifeFailUnlock_Type()
)
cpqCmcSetupLock2LifeFailUnlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupLock2LifeFailUnlock.setStatus("mandatory")
_CpqCmcSetupSmoke_ObjectIdentity = ObjectIdentity
cpqCmcSetupSmoke = _CpqCmcSetupSmoke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 13)
)


class _CpqCmcSetupSmokeAvail_Type(Integer32):
    """Custom type cpqCmcSetupSmokeAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupSmokeAvail_Type.__name__ = "Integer32"
_CpqCmcSetupSmokeAvail_Object = MibScalar
cpqCmcSetupSmokeAvail = _CpqCmcSetupSmokeAvail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 13, 1),
    _CpqCmcSetupSmokeAvail_Type()
)
cpqCmcSetupSmokeAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupSmokeAvail.setStatus("mandatory")


class _CpqCmcSetupSmokeRelays_Type(Integer32):
    """Custom type cpqCmcSetupSmokeRelays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupSmokeRelays_Type.__name__ = "Integer32"
_CpqCmcSetupSmokeRelays_Object = MibScalar
cpqCmcSetupSmokeRelays = _CpqCmcSetupSmokeRelays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 13, 2),
    _CpqCmcSetupSmokeRelays_Type()
)
cpqCmcSetupSmokeRelays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupSmokeRelays.setStatus("mandatory")


class _CpqCmcSetupSmokeAudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupSmokeAudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupSmokeAudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupSmokeAudibleAlarm_Object = MibScalar
cpqCmcSetupSmokeAudibleAlarm = _CpqCmcSetupSmokeAudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 13, 3),
    _CpqCmcSetupSmokeAudibleAlarm_Type()
)
cpqCmcSetupSmokeAudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupSmokeAudibleAlarm.setStatus("mandatory")


class _CpqCmcSetupSmokeFansOff_Type(Integer32):
    """Custom type cpqCmcSetupSmokeFansOff based on Integer32"""
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
        *(("both", 2),
          ("fan1", 3),
          ("fan2", 4),
          ("noFan", 5),
          ("other", 1))
    )


_CpqCmcSetupSmokeFansOff_Type.__name__ = "Integer32"
_CpqCmcSetupSmokeFansOff_Object = MibScalar
cpqCmcSetupSmokeFansOff = _CpqCmcSetupSmokeFansOff_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 13, 4),
    _CpqCmcSetupSmokeFansOff_Type()
)
cpqCmcSetupSmokeFansOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupSmokeFansOff.setStatus("mandatory")


class _CpqCmcSetupSmokeUnlock_Type(Integer32):
    """Custom type cpqCmcSetupSmokeUnlock based on Integer32"""
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
        *(("both", 2),
          ("lock1", 3),
          ("lock2", 4),
          ("noLock", 5),
          ("other", 1))
    )


_CpqCmcSetupSmokeUnlock_Type.__name__ = "Integer32"
_CpqCmcSetupSmokeUnlock_Object = MibScalar
cpqCmcSetupSmokeUnlock = _CpqCmcSetupSmokeUnlock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 13, 5),
    _CpqCmcSetupSmokeUnlock_Type()
)
cpqCmcSetupSmokeUnlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupSmokeUnlock.setStatus("mandatory")
_CpqCmcSetupShock_ObjectIdentity = ObjectIdentity
cpqCmcSetupShock = _CpqCmcSetupShock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 14)
)


class _CpqCmcSetupShockAvail_Type(Integer32):
    """Custom type cpqCmcSetupShockAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupShockAvail_Type.__name__ = "Integer32"
_CpqCmcSetupShockAvail_Object = MibScalar
cpqCmcSetupShockAvail = _CpqCmcSetupShockAvail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 14, 1),
    _CpqCmcSetupShockAvail_Type()
)
cpqCmcSetupShockAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupShockAvail.setStatus("mandatory")


class _CpqCmcSetupShockRelays_Type(Integer32):
    """Custom type cpqCmcSetupShockRelays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupShockRelays_Type.__name__ = "Integer32"
_CpqCmcSetupShockRelays_Object = MibScalar
cpqCmcSetupShockRelays = _CpqCmcSetupShockRelays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 14, 2),
    _CpqCmcSetupShockRelays_Type()
)
cpqCmcSetupShockRelays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupShockRelays.setStatus("mandatory")


class _CpqCmcSetupShockAudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupShockAudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupShockAudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupShockAudibleAlarm_Object = MibScalar
cpqCmcSetupShockAudibleAlarm = _CpqCmcSetupShockAudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 14, 3),
    _CpqCmcSetupShockAudibleAlarm_Type()
)
cpqCmcSetupShockAudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupShockAudibleAlarm.setStatus("mandatory")


class _CpqCmcSetupShockSensitivity_Type(Integer32):
    """Custom type cpqCmcSetupShockSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CpqCmcSetupShockSensitivity_Type.__name__ = "Integer32"
_CpqCmcSetupShockSensitivity_Object = MibScalar
cpqCmcSetupShockSensitivity = _CpqCmcSetupShockSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 14, 4),
    _CpqCmcSetupShockSensitivity_Type()
)
cpqCmcSetupShockSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupShockSensitivity.setStatus("mandatory")
_CpqCmcSetupAux1_ObjectIdentity = ObjectIdentity
cpqCmcSetupAux1 = _CpqCmcSetupAux1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 15)
)


class _CpqCmcSetupAux1Avail_Type(Integer32):
    """Custom type cpqCmcSetupAux1Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupAux1Avail_Type.__name__ = "Integer32"
_CpqCmcSetupAux1Avail_Object = MibScalar
cpqCmcSetupAux1Avail = _CpqCmcSetupAux1Avail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 15, 1),
    _CpqCmcSetupAux1Avail_Type()
)
cpqCmcSetupAux1Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAux1Avail.setStatus("mandatory")


class _CpqCmcSetupAux1Relays_Type(Integer32):
    """Custom type cpqCmcSetupAux1Relays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupAux1Relays_Type.__name__ = "Integer32"
_CpqCmcSetupAux1Relays_Object = MibScalar
cpqCmcSetupAux1Relays = _CpqCmcSetupAux1Relays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 15, 2),
    _CpqCmcSetupAux1Relays_Type()
)
cpqCmcSetupAux1Relays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAux1Relays.setStatus("mandatory")


class _CpqCmcSetupAux1AudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupAux1AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupAux1AudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupAux1AudibleAlarm_Object = MibScalar
cpqCmcSetupAux1AudibleAlarm = _CpqCmcSetupAux1AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 15, 3),
    _CpqCmcSetupAux1AudibleAlarm_Type()
)
cpqCmcSetupAux1AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAux1AudibleAlarm.setStatus("mandatory")


class _CpqCmcSetupAux1InputType_Type(Integer32):
    """Custom type cpqCmcSetupAux1InputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normClosed", 3),
          ("normOpen", 2),
          ("other", 1))
    )


_CpqCmcSetupAux1InputType_Type.__name__ = "Integer32"
_CpqCmcSetupAux1InputType_Object = MibScalar
cpqCmcSetupAux1InputType = _CpqCmcSetupAux1InputType_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 15, 4),
    _CpqCmcSetupAux1InputType_Type()
)
cpqCmcSetupAux1InputType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAux1InputType.setStatus("mandatory")


class _CpqCmcSetupAux1Description_Type(DisplayString):
    """Custom type cpqCmcSetupAux1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_CpqCmcSetupAux1Description_Type.__name__ = "DisplayString"
_CpqCmcSetupAux1Description_Object = MibScalar
cpqCmcSetupAux1Description = _CpqCmcSetupAux1Description_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 15, 5),
    _CpqCmcSetupAux1Description_Type()
)
cpqCmcSetupAux1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAux1Description.setStatus("mandatory")


class _CpqCmcSetupAux1Unlock_Type(Integer32):
    """Custom type cpqCmcSetupAux1Unlock based on Integer32"""
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
        *(("both", 5),
          ("lock1", 3),
          ("lock2", 4),
          ("noLock", 2),
          ("other", 1))
    )


_CpqCmcSetupAux1Unlock_Type.__name__ = "Integer32"
_CpqCmcSetupAux1Unlock_Object = MibScalar
cpqCmcSetupAux1Unlock = _CpqCmcSetupAux1Unlock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 15, 6),
    _CpqCmcSetupAux1Unlock_Type()
)
cpqCmcSetupAux1Unlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAux1Unlock.setStatus("mandatory")
_CpqCmcSetupAux2_ObjectIdentity = ObjectIdentity
cpqCmcSetupAux2 = _CpqCmcSetupAux2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 16)
)


class _CpqCmcSetupAux2Avail_Type(Integer32):
    """Custom type cpqCmcSetupAux2Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 3),
          ("other", 1))
    )


_CpqCmcSetupAux2Avail_Type.__name__ = "Integer32"
_CpqCmcSetupAux2Avail_Object = MibScalar
cpqCmcSetupAux2Avail = _CpqCmcSetupAux2Avail_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 16, 1),
    _CpqCmcSetupAux2Avail_Type()
)
cpqCmcSetupAux2Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAux2Avail.setStatus("mandatory")


class _CpqCmcSetupAux2Relays_Type(Integer32):
    """Custom type cpqCmcSetupAux2Relays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupAux2Relays_Type.__name__ = "Integer32"
_CpqCmcSetupAux2Relays_Object = MibScalar
cpqCmcSetupAux2Relays = _CpqCmcSetupAux2Relays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 16, 2),
    _CpqCmcSetupAux2Relays_Type()
)
cpqCmcSetupAux2Relays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAux2Relays.setStatus("mandatory")


class _CpqCmcSetupAux2AudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupAux2AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupAux2AudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupAux2AudibleAlarm_Object = MibScalar
cpqCmcSetupAux2AudibleAlarm = _CpqCmcSetupAux2AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 16, 3),
    _CpqCmcSetupAux2AudibleAlarm_Type()
)
cpqCmcSetupAux2AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAux2AudibleAlarm.setStatus("mandatory")


class _CpqCmcSetupAux2InputType_Type(Integer32):
    """Custom type cpqCmcSetupAux2InputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normClosed", 3),
          ("normOpen", 2),
          ("other", 1))
    )


_CpqCmcSetupAux2InputType_Type.__name__ = "Integer32"
_CpqCmcSetupAux2InputType_Object = MibScalar
cpqCmcSetupAux2InputType = _CpqCmcSetupAux2InputType_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 16, 4),
    _CpqCmcSetupAux2InputType_Type()
)
cpqCmcSetupAux2InputType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAux2InputType.setStatus("mandatory")


class _CpqCmcSetupAux2Description_Type(DisplayString):
    """Custom type cpqCmcSetupAux2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_CpqCmcSetupAux2Description_Type.__name__ = "DisplayString"
_CpqCmcSetupAux2Description_Object = MibScalar
cpqCmcSetupAux2Description = _CpqCmcSetupAux2Description_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 16, 5),
    _CpqCmcSetupAux2Description_Type()
)
cpqCmcSetupAux2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAux2Description.setStatus("mandatory")


class _CpqCmcSetupAux2Unlock_Type(Integer32):
    """Custom type cpqCmcSetupAux2Unlock based on Integer32"""
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
        *(("both", 5),
          ("lock1", 3),
          ("lock2", 4),
          ("noLock", 2),
          ("other", 1))
    )


_CpqCmcSetupAux2Unlock_Type.__name__ = "Integer32"
_CpqCmcSetupAux2Unlock_Object = MibScalar
cpqCmcSetupAux2Unlock = _CpqCmcSetupAux2Unlock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 16, 6),
    _CpqCmcSetupAux2Unlock_Type()
)
cpqCmcSetupAux2Unlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAux2Unlock.setStatus("mandatory")
_CpqCmcSetupAlarm1_ObjectIdentity = ObjectIdentity
cpqCmcSetupAlarm1 = _CpqCmcSetupAlarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 17)
)


class _CpqCmcSetupAlarm1Relays_Type(Integer32):
    """Custom type cpqCmcSetupAlarm1Relays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupAlarm1Relays_Type.__name__ = "Integer32"
_CpqCmcSetupAlarm1Relays_Object = MibScalar
cpqCmcSetupAlarm1Relays = _CpqCmcSetupAlarm1Relays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 17, 1),
    _CpqCmcSetupAlarm1Relays_Type()
)
cpqCmcSetupAlarm1Relays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAlarm1Relays.setStatus("mandatory")


class _CpqCmcSetupAlarm1AudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupAlarm1AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupAlarm1AudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupAlarm1AudibleAlarm_Object = MibScalar
cpqCmcSetupAlarm1AudibleAlarm = _CpqCmcSetupAlarm1AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 17, 2),
    _CpqCmcSetupAlarm1AudibleAlarm_Type()
)
cpqCmcSetupAlarm1AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAlarm1AudibleAlarm.setStatus("mandatory")


class _CpqCmcSetupAlarm1Description_Type(DisplayString):
    """Custom type cpqCmcSetupAlarm1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_CpqCmcSetupAlarm1Description_Type.__name__ = "DisplayString"
_CpqCmcSetupAlarm1Description_Object = MibScalar
cpqCmcSetupAlarm1Description = _CpqCmcSetupAlarm1Description_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 17, 3),
    _CpqCmcSetupAlarm1Description_Type()
)
cpqCmcSetupAlarm1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAlarm1Description.setStatus("mandatory")
_CpqCmcSetupAlarm2_ObjectIdentity = ObjectIdentity
cpqCmcSetupAlarm2 = _CpqCmcSetupAlarm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 18)
)


class _CpqCmcSetupAlarm2Relays_Type(Integer32):
    """Custom type cpqCmcSetupAlarm2Relays based on Integer32"""
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
        *(("both", 5),
          ("off", 2),
          ("other", 1),
          ("relay1", 3),
          ("relay2", 4))
    )


_CpqCmcSetupAlarm2Relays_Type.__name__ = "Integer32"
_CpqCmcSetupAlarm2Relays_Object = MibScalar
cpqCmcSetupAlarm2Relays = _CpqCmcSetupAlarm2Relays_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 18, 1),
    _CpqCmcSetupAlarm2Relays_Type()
)
cpqCmcSetupAlarm2Relays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAlarm2Relays.setStatus("mandatory")


class _CpqCmcSetupAlarm2AudibleAlarm_Type(Integer32):
    """Custom type cpqCmcSetupAlarm2AudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcSetupAlarm2AudibleAlarm_Type.__name__ = "Integer32"
_CpqCmcSetupAlarm2AudibleAlarm_Object = MibScalar
cpqCmcSetupAlarm2AudibleAlarm = _CpqCmcSetupAlarm2AudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 18, 2),
    _CpqCmcSetupAlarm2AudibleAlarm_Type()
)
cpqCmcSetupAlarm2AudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAlarm2AudibleAlarm.setStatus("mandatory")


class _CpqCmcSetupAlarm2Description_Type(DisplayString):
    """Custom type cpqCmcSetupAlarm2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_CpqCmcSetupAlarm2Description_Type.__name__ = "DisplayString"
_CpqCmcSetupAlarm2Description_Object = MibScalar
cpqCmcSetupAlarm2Description = _CpqCmcSetupAlarm2Description_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 2, 18, 3),
    _CpqCmcSetupAlarm2Description_Type()
)
cpqCmcSetupAlarm2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupAlarm2Description.setStatus("mandatory")
_CpqCmcSetupClock_ObjectIdentity = ObjectIdentity
cpqCmcSetupClock = _CpqCmcSetupClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 3)
)


class _CpqCmcSetupDate_Type(DisplayString):
    """Custom type cpqCmcSetupDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CpqCmcSetupDate_Type.__name__ = "DisplayString"
_CpqCmcSetupDate_Object = MibScalar
cpqCmcSetupDate = _CpqCmcSetupDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 3, 1),
    _CpqCmcSetupDate_Type()
)
cpqCmcSetupDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupDate.setStatus("mandatory")


class _CpqCmcSetupTime_Type(DisplayString):
    """Custom type cpqCmcSetupTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqCmcSetupTime_Type.__name__ = "DisplayString"
_CpqCmcSetupTime_Object = MibScalar
cpqCmcSetupTime = _CpqCmcSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 1, 3, 2),
    _CpqCmcSetupTime_Type()
)
cpqCmcSetupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetupTime.setStatus("mandatory")
_CpqCmcSetupThreshold_ObjectIdentity = ObjectIdentity
cpqCmcSetupThreshold = _CpqCmcSetupThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2)
)


class _CpqCmcThresholdMaxTemp1_Type(Integer32):
    """Custom type cpqCmcThresholdMaxTemp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CpqCmcThresholdMaxTemp1_Type.__name__ = "Integer32"
_CpqCmcThresholdMaxTemp1_Object = MibScalar
cpqCmcThresholdMaxTemp1 = _CpqCmcThresholdMaxTemp1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 1),
    _CpqCmcThresholdMaxTemp1_Type()
)
cpqCmcThresholdMaxTemp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdMaxTemp1.setStatus("mandatory")


class _CpqCmcThresholdWarningTemp1_Type(Integer32):
    """Custom type cpqCmcThresholdWarningTemp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CpqCmcThresholdWarningTemp1_Type.__name__ = "Integer32"
_CpqCmcThresholdWarningTemp1_Object = MibScalar
cpqCmcThresholdWarningTemp1 = _CpqCmcThresholdWarningTemp1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 2),
    _CpqCmcThresholdWarningTemp1_Type()
)
cpqCmcThresholdWarningTemp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdWarningTemp1.setStatus("mandatory")


class _CpqCmcThresholdMinTemp1_Type(Integer32):
    """Custom type cpqCmcThresholdMinTemp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpqCmcThresholdMinTemp1_Type.__name__ = "Integer32"
_CpqCmcThresholdMinTemp1_Object = MibScalar
cpqCmcThresholdMinTemp1 = _CpqCmcThresholdMinTemp1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 3),
    _CpqCmcThresholdMinTemp1_Type()
)
cpqCmcThresholdMinTemp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdMinTemp1.setStatus("mandatory")


class _CpqCmcThresholdMaxTemp2_Type(Integer32):
    """Custom type cpqCmcThresholdMaxTemp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CpqCmcThresholdMaxTemp2_Type.__name__ = "Integer32"
_CpqCmcThresholdMaxTemp2_Object = MibScalar
cpqCmcThresholdMaxTemp2 = _CpqCmcThresholdMaxTemp2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 4),
    _CpqCmcThresholdMaxTemp2_Type()
)
cpqCmcThresholdMaxTemp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdMaxTemp2.setStatus("mandatory")


class _CpqCmcThresholdWarningTemp2_Type(Integer32):
    """Custom type cpqCmcThresholdWarningTemp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CpqCmcThresholdWarningTemp2_Type.__name__ = "Integer32"
_CpqCmcThresholdWarningTemp2_Object = MibScalar
cpqCmcThresholdWarningTemp2 = _CpqCmcThresholdWarningTemp2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 5),
    _CpqCmcThresholdWarningTemp2_Type()
)
cpqCmcThresholdWarningTemp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdWarningTemp2.setStatus("mandatory")


class _CpqCmcThresholdMinTemp2_Type(Integer32):
    """Custom type cpqCmcThresholdMinTemp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpqCmcThresholdMinTemp2_Type.__name__ = "Integer32"
_CpqCmcThresholdMinTemp2_Object = MibScalar
cpqCmcThresholdMinTemp2 = _CpqCmcThresholdMinTemp2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 6),
    _CpqCmcThresholdMinTemp2_Type()
)
cpqCmcThresholdMinTemp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdMinTemp2.setStatus("mandatory")


class _CpqCmcThresholdFan1_Type(Integer32):
    """Custom type cpqCmcThresholdFan1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CpqCmcThresholdFan1_Type.__name__ = "Integer32"
_CpqCmcThresholdFan1_Object = MibScalar
cpqCmcThresholdFan1 = _CpqCmcThresholdFan1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 7),
    _CpqCmcThresholdFan1_Type()
)
cpqCmcThresholdFan1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdFan1.setStatus("mandatory")


class _CpqCmcThresholdFan1Hysteresis_Type(Integer32):
    """Custom type cpqCmcThresholdFan1Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CpqCmcThresholdFan1Hysteresis_Type.__name__ = "Integer32"
_CpqCmcThresholdFan1Hysteresis_Object = MibScalar
cpqCmcThresholdFan1Hysteresis = _CpqCmcThresholdFan1Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 8),
    _CpqCmcThresholdFan1Hysteresis_Type()
)
cpqCmcThresholdFan1Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdFan1Hysteresis.setStatus("mandatory")


class _CpqCmcThresholdFan2_Type(Integer32):
    """Custom type cpqCmcThresholdFan2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CpqCmcThresholdFan2_Type.__name__ = "Integer32"
_CpqCmcThresholdFan2_Object = MibScalar
cpqCmcThresholdFan2 = _CpqCmcThresholdFan2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 9),
    _CpqCmcThresholdFan2_Type()
)
cpqCmcThresholdFan2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdFan2.setStatus("mandatory")


class _CpqCmcThresholdFan2Hysteresis_Type(Integer32):
    """Custom type cpqCmcThresholdFan2Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CpqCmcThresholdFan2Hysteresis_Type.__name__ = "Integer32"
_CpqCmcThresholdFan2Hysteresis_Object = MibScalar
cpqCmcThresholdFan2Hysteresis = _CpqCmcThresholdFan2Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 10),
    _CpqCmcThresholdFan2Hysteresis_Type()
)
cpqCmcThresholdFan2Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdFan2Hysteresis.setStatus("mandatory")


class _CpqCmcThresholdMaxVoltage_Type(Integer32):
    """Custom type cpqCmcThresholdMaxVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCmcThresholdMaxVoltage_Type.__name__ = "Integer32"
_CpqCmcThresholdMaxVoltage_Object = MibScalar
cpqCmcThresholdMaxVoltage = _CpqCmcThresholdMaxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 11),
    _CpqCmcThresholdMaxVoltage_Type()
)
cpqCmcThresholdMaxVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdMaxVoltage.setStatus("mandatory")


class _CpqCmcThresholdMinVoltage_Type(Integer32):
    """Custom type cpqCmcThresholdMinVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqCmcThresholdMinVoltage_Type.__name__ = "Integer32"
_CpqCmcThresholdMinVoltage_Object = MibScalar
cpqCmcThresholdMinVoltage = _CpqCmcThresholdMinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 12),
    _CpqCmcThresholdMinVoltage_Type()
)
cpqCmcThresholdMinVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdMinVoltage.setStatus("mandatory")


class _CpqCmcThresholdMaxHumidity_Type(Integer32):
    """Custom type cpqCmcThresholdMaxHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpqCmcThresholdMaxHumidity_Type.__name__ = "Integer32"
_CpqCmcThresholdMaxHumidity_Object = MibScalar
cpqCmcThresholdMaxHumidity = _CpqCmcThresholdMaxHumidity_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 13),
    _CpqCmcThresholdMaxHumidity_Type()
)
cpqCmcThresholdMaxHumidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdMaxHumidity.setStatus("mandatory")


class _CpqCmcThresholdMinHumidity_Type(Integer32):
    """Custom type cpqCmcThresholdMinHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpqCmcThresholdMinHumidity_Type.__name__ = "Integer32"
_CpqCmcThresholdMinHumidity_Object = MibScalar
cpqCmcThresholdMinHumidity = _CpqCmcThresholdMinHumidity_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 2, 14),
    _CpqCmcThresholdMinHumidity_Type()
)
cpqCmcThresholdMinHumidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcThresholdMinHumidity.setStatus("mandatory")
_CpqCmcTraps_ObjectIdentity = ObjectIdentity
cpqCmcTraps = _CpqCmcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 3)
)
_CpqCmcTrapTableNumber_Type = Integer32
_CpqCmcTrapTableNumber_Object = MibScalar
cpqCmcTrapTableNumber = _CpqCmcTrapTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 3, 1),
    _CpqCmcTrapTableNumber_Type()
)
cpqCmcTrapTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcTrapTableNumber.setStatus("mandatory")
_CpqCmcTrapTable_Object = MibTable
cpqCmcTrapTable = _CpqCmcTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cpqCmcTrapTable.setStatus("mandatory")
_CpqCmcTrapEntry_Object = MibTableRow
cpqCmcTrapEntry = _CpqCmcTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 3, 2, 1)
)
cpqCmcTrapEntry.setIndexNames(
    (0, "CPQCMC-MIB", "cpqCmcTrapIndex"),
)
if mibBuilder.loadTexts:
    cpqCmcTrapEntry.setStatus("mandatory")


class _CpqCmcTrapIndex_Type(Integer32):
    """Custom type cpqCmcTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CpqCmcTrapIndex_Type.__name__ = "Integer32"
_CpqCmcTrapIndex_Object = MibTableColumn
cpqCmcTrapIndex = _CpqCmcTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 3, 2, 1, 1),
    _CpqCmcTrapIndex_Type()
)
cpqCmcTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcTrapIndex.setStatus("mandatory")


class _CpqCmcTrapStatus_Type(Integer32):
    """Custom type cpqCmcTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_CpqCmcTrapStatus_Type.__name__ = "Integer32"
_CpqCmcTrapStatus_Object = MibTableColumn
cpqCmcTrapStatus = _CpqCmcTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 3, 2, 1, 2),
    _CpqCmcTrapStatus_Type()
)
cpqCmcTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcTrapStatus.setStatus("mandatory")


class _CpqCmcTrapIPaddress_Type(DisplayString):
    """Custom type cpqCmcTrapIPaddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqCmcTrapIPaddress_Type.__name__ = "DisplayString"
_CpqCmcTrapIPaddress_Object = MibTableColumn
cpqCmcTrapIPaddress = _CpqCmcTrapIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 2, 3, 2, 1, 3),
    _CpqCmcTrapIPaddress_Type()
)
cpqCmcTrapIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcTrapIPaddress.setStatus("mandatory")
_CpqCmcValues_ObjectIdentity = ObjectIdentity
cpqCmcValues = _CpqCmcValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 3)
)
_CpqCmcValueTemp1_Type = Integer32
_CpqCmcValueTemp1_Object = MibScalar
cpqCmcValueTemp1 = _CpqCmcValueTemp1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 3, 1),
    _CpqCmcValueTemp1_Type()
)
cpqCmcValueTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcValueTemp1.setStatus("mandatory")
_CpqCmcValueTemp2_Type = Integer32
_CpqCmcValueTemp2_Object = MibScalar
cpqCmcValueTemp2 = _CpqCmcValueTemp2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 3, 2),
    _CpqCmcValueTemp2_Type()
)
cpqCmcValueTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcValueTemp2.setStatus("mandatory")
_CpqCmcValueVoltage_Type = Integer32
_CpqCmcValueVoltage_Object = MibScalar
cpqCmcValueVoltage = _CpqCmcValueVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 3, 3),
    _CpqCmcValueVoltage_Type()
)
cpqCmcValueVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcValueVoltage.setStatus("mandatory")
_CpqCmcValueHumidity_Type = Integer32
_CpqCmcValueHumidity_Object = MibScalar
cpqCmcValueHumidity = _CpqCmcValueHumidity_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 3, 4),
    _CpqCmcValueHumidity_Type()
)
cpqCmcValueHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcValueHumidity.setStatus("mandatory")


class _CpqCmcValueOperatingTime_Type(DisplayString):
    """Custom type cpqCmcValueOperatingTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CpqCmcValueOperatingTime_Type.__name__ = "DisplayString"
_CpqCmcValueOperatingTime_Object = MibScalar
cpqCmcValueOperatingTime = _CpqCmcValueOperatingTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 3, 5),
    _CpqCmcValueOperatingTime_Type()
)
cpqCmcValueOperatingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcValueOperatingTime.setStatus("mandatory")
_CpqCmcStatus_ObjectIdentity = ObjectIdentity
cpqCmcStatus = _CpqCmcStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4)
)


class _CpqCmcStatusTemp1_Type(Integer32):
    """Custom type cpqCmcStatusTemp1 based on Integer32"""
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
        *(("error", 7),
          ("noSensor", 6),
          ("normal", 2),
          ("other", 1),
          ("overMax", 4),
          ("underMin", 5),
          ("warning", 3))
    )


_CpqCmcStatusTemp1_Type.__name__ = "Integer32"
_CpqCmcStatusTemp1_Object = MibScalar
cpqCmcStatusTemp1 = _CpqCmcStatusTemp1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 1),
    _CpqCmcStatusTemp1_Type()
)
cpqCmcStatusTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusTemp1.setStatus("mandatory")


class _CpqCmcStatusTemp2_Type(Integer32):
    """Custom type cpqCmcStatusTemp2 based on Integer32"""
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
        *(("error", 7),
          ("noSensor", 6),
          ("normal", 2),
          ("other", 1),
          ("overMax", 4),
          ("underMin", 5),
          ("warning", 3))
    )


_CpqCmcStatusTemp2_Type.__name__ = "Integer32"
_CpqCmcStatusTemp2_Object = MibScalar
cpqCmcStatusTemp2 = _CpqCmcStatusTemp2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 2),
    _CpqCmcStatusTemp2_Type()
)
cpqCmcStatusTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusTemp2.setStatus("mandatory")


class _CpqCmcStatusFan1_Type(Integer32):
    """Custom type cpqCmcStatusFan1 based on Integer32"""
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
        *(("autoOff", 2),
          ("autoOn", 3),
          ("doorOff", 7),
          ("error", 9),
          ("manualOff", 4),
          ("manualOn", 5),
          ("noFan", 8),
          ("other", 1),
          ("smokeOff", 6))
    )


_CpqCmcStatusFan1_Type.__name__ = "Integer32"
_CpqCmcStatusFan1_Object = MibScalar
cpqCmcStatusFan1 = _CpqCmcStatusFan1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 3),
    _CpqCmcStatusFan1_Type()
)
cpqCmcStatusFan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusFan1.setStatus("mandatory")


class _CpqCmcStatusFan2_Type(Integer32):
    """Custom type cpqCmcStatusFan2 based on Integer32"""
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
        *(("autoOff", 2),
          ("autoOn", 3),
          ("doorOff", 7),
          ("error", 9),
          ("manualOff", 4),
          ("manualOn", 5),
          ("noFan", 8),
          ("other", 1),
          ("smokeOff", 6))
    )


_CpqCmcStatusFan2_Type.__name__ = "Integer32"
_CpqCmcStatusFan2_Object = MibScalar
cpqCmcStatusFan2 = _CpqCmcStatusFan2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 4),
    _CpqCmcStatusFan2_Type()
)
cpqCmcStatusFan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusFan2.setStatus("mandatory")


class _CpqCmcStatusVoltage_Type(Integer32):
    """Custom type cpqCmcStatusVoltage based on Integer32"""
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
        *(("noVoltage", 5),
          ("normal", 2),
          ("other", 1),
          ("overMax", 3),
          ("underMin", 4))
    )


_CpqCmcStatusVoltage_Type.__name__ = "Integer32"
_CpqCmcStatusVoltage_Object = MibScalar
cpqCmcStatusVoltage = _CpqCmcStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 5),
    _CpqCmcStatusVoltage_Type()
)
cpqCmcStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusVoltage.setStatus("mandatory")


class _CpqCmcStatusHumidity_Type(Integer32):
    """Custom type cpqCmcStatusHumidity based on Integer32"""
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
        *(("error", 6),
          ("noSensor", 5),
          ("normal", 2),
          ("other", 1),
          ("overMax", 3),
          ("underMin", 4))
    )


_CpqCmcStatusHumidity_Type.__name__ = "Integer32"
_CpqCmcStatusHumidity_Object = MibScalar
cpqCmcStatusHumidity = _CpqCmcStatusHumidity_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 6),
    _CpqCmcStatusHumidity_Type()
)
cpqCmcStatusHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusHumidity.setStatus("mandatory")


class _CpqCmcStatusInput1_Type(Integer32):
    """Custom type cpqCmcStatusInput1 based on Integer32"""
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
        *(("closed", 2),
          ("noSensor", 4),
          ("open", 3),
          ("other", 1))
    )


_CpqCmcStatusInput1_Type.__name__ = "Integer32"
_CpqCmcStatusInput1_Object = MibScalar
cpqCmcStatusInput1 = _CpqCmcStatusInput1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 7),
    _CpqCmcStatusInput1_Type()
)
cpqCmcStatusInput1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusInput1.setStatus("mandatory")


class _CpqCmcStatusInput2_Type(Integer32):
    """Custom type cpqCmcStatusInput2 based on Integer32"""
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
        *(("closed", 2),
          ("noSensor", 4),
          ("open", 3),
          ("other", 1))
    )


_CpqCmcStatusInput2_Type.__name__ = "Integer32"
_CpqCmcStatusInput2_Object = MibScalar
cpqCmcStatusInput2 = _CpqCmcStatusInput2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 8),
    _CpqCmcStatusInput2_Type()
)
cpqCmcStatusInput2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusInput2.setStatus("mandatory")


class _CpqCmcStatusInput3_Type(Integer32):
    """Custom type cpqCmcStatusInput3 based on Integer32"""
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
        *(("closed", 2),
          ("noSensor", 4),
          ("open", 3),
          ("other", 1))
    )


_CpqCmcStatusInput3_Type.__name__ = "Integer32"
_CpqCmcStatusInput3_Object = MibScalar
cpqCmcStatusInput3 = _CpqCmcStatusInput3_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 9),
    _CpqCmcStatusInput3_Type()
)
cpqCmcStatusInput3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusInput3.setStatus("mandatory")


class _CpqCmcStatusInput4_Type(Integer32):
    """Custom type cpqCmcStatusInput4 based on Integer32"""
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
        *(("closed", 2),
          ("noSensor", 4),
          ("open", 3),
          ("other", 1))
    )


_CpqCmcStatusInput4_Type.__name__ = "Integer32"
_CpqCmcStatusInput4_Object = MibScalar
cpqCmcStatusInput4 = _CpqCmcStatusInput4_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 10),
    _CpqCmcStatusInput4_Type()
)
cpqCmcStatusInput4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusInput4.setStatus("mandatory")


class _CpqCmcStatusLock1Lock_Type(Integer32):
    """Custom type cpqCmcStatusLock1Lock based on Integer32"""
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
        *(("alarm", 12),
          ("configError", 13),
          ("locked", 2),
          ("notAvail", 14),
          ("other", 1),
          ("readyToLock", 11),
          ("unlockedAuto", 3),
          ("unlockedBattLow", 8),
          ("unlockedConnFail", 10),
          ("unlockedKey", 6),
          ("unlockedNetFail", 9),
          ("unlockedPwrFail", 7),
          ("unlockedSmoke", 5),
          ("unlockedTime", 4))
    )


_CpqCmcStatusLock1Lock_Type.__name__ = "Integer32"
_CpqCmcStatusLock1Lock_Object = MibScalar
cpqCmcStatusLock1Lock = _CpqCmcStatusLock1Lock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 11),
    _CpqCmcStatusLock1Lock_Type()
)
cpqCmcStatusLock1Lock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusLock1Lock.setStatus("mandatory")


class _CpqCmcStatusLock2Lock_Type(Integer32):
    """Custom type cpqCmcStatusLock2Lock based on Integer32"""
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
        *(("alarm", 12),
          ("configError", 13),
          ("locked", 2),
          ("notAvail", 14),
          ("other", 1),
          ("readyToLock", 11),
          ("unlockedAuto", 3),
          ("unlockedBattLow", 8),
          ("unlockedConnFail", 10),
          ("unlockedKey", 6),
          ("unlockedNetFail", 9),
          ("unlockedPwrFail", 7),
          ("unlockedSmoke", 5),
          ("unlockedTime", 4))
    )


_CpqCmcStatusLock2Lock_Type.__name__ = "Integer32"
_CpqCmcStatusLock2Lock_Object = MibScalar
cpqCmcStatusLock2Lock = _CpqCmcStatusLock2Lock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 12),
    _CpqCmcStatusLock2Lock_Type()
)
cpqCmcStatusLock2Lock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusLock2Lock.setStatus("mandatory")


class _CpqCmcStatusSmoke_Type(Integer32):
    """Custom type cpqCmcStatusSmoke based on Integer32"""
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
        *(("cleared", 2),
          ("noSensor", 4),
          ("other", 1),
          ("present", 3))
    )


_CpqCmcStatusSmoke_Type.__name__ = "Integer32"
_CpqCmcStatusSmoke_Object = MibScalar
cpqCmcStatusSmoke = _CpqCmcStatusSmoke_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 13),
    _CpqCmcStatusSmoke_Type()
)
cpqCmcStatusSmoke.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusSmoke.setStatus("mandatory")


class _CpqCmcStatusShock_Type(Integer32):
    """Custom type cpqCmcStatusShock based on Integer32"""
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
        *(("cleared", 2),
          ("noSensor", 4),
          ("other", 1),
          ("present", 3))
    )


_CpqCmcStatusShock_Type.__name__ = "Integer32"
_CpqCmcStatusShock_Object = MibScalar
cpqCmcStatusShock = _CpqCmcStatusShock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 14),
    _CpqCmcStatusShock_Type()
)
cpqCmcStatusShock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusShock.setStatus("mandatory")


class _CpqCmcStatusAux1_Type(Integer32):
    """Custom type cpqCmcStatusAux1 based on Integer32"""
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
        *(("alarm", 3),
          ("noSensor", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCmcStatusAux1_Type.__name__ = "Integer32"
_CpqCmcStatusAux1_Object = MibScalar
cpqCmcStatusAux1 = _CpqCmcStatusAux1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 15),
    _CpqCmcStatusAux1_Type()
)
cpqCmcStatusAux1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusAux1.setStatus("mandatory")


class _CpqCmcStatusAux2_Type(Integer32):
    """Custom type cpqCmcStatusAux2 based on Integer32"""
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
        *(("alarm", 3),
          ("noSensor", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqCmcStatusAux2_Type.__name__ = "Integer32"
_CpqCmcStatusAux2_Object = MibScalar
cpqCmcStatusAux2 = _CpqCmcStatusAux2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 16),
    _CpqCmcStatusAux2_Type()
)
cpqCmcStatusAux2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusAux2.setStatus("mandatory")


class _CpqCmcStatusAlarm1_Type(Integer32):
    """Custom type cpqCmcStatusAlarm1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqCmcStatusAlarm1_Type.__name__ = "Integer32"
_CpqCmcStatusAlarm1_Object = MibScalar
cpqCmcStatusAlarm1 = _CpqCmcStatusAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 17),
    _CpqCmcStatusAlarm1_Type()
)
cpqCmcStatusAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusAlarm1.setStatus("mandatory")


class _CpqCmcStatusAlarm2_Type(Integer32):
    """Custom type cpqCmcStatusAlarm2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqCmcStatusAlarm2_Type.__name__ = "Integer32"
_CpqCmcStatusAlarm2_Object = MibScalar
cpqCmcStatusAlarm2 = _CpqCmcStatusAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 18),
    _CpqCmcStatusAlarm2_Type()
)
cpqCmcStatusAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusAlarm2.setStatus("mandatory")


class _CpqCmcStatusLock1Dev_Type(Integer32):
    """Custom type cpqCmcStatusLock1Dev based on Integer32"""
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
        *(("lowBattery", 4),
          ("missingBatt", 6),
          ("noConnect", 7),
          ("notAvail", 8),
          ("ok", 2),
          ("other", 1),
          ("powerFail", 3),
          ("replaceBatt", 5))
    )


_CpqCmcStatusLock1Dev_Type.__name__ = "Integer32"
_CpqCmcStatusLock1Dev_Object = MibScalar
cpqCmcStatusLock1Dev = _CpqCmcStatusLock1Dev_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 19),
    _CpqCmcStatusLock1Dev_Type()
)
cpqCmcStatusLock1Dev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusLock1Dev.setStatus("mandatory")


class _CpqCmcStatusLock2Dev_Type(Integer32):
    """Custom type cpqCmcStatusLock2Dev based on Integer32"""
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
        *(("lowBattery", 4),
          ("missingBatt", 6),
          ("noConnect", 7),
          ("notAvail", 8),
          ("ok", 2),
          ("other", 1),
          ("powerFail", 3),
          ("replaceBatt", 5))
    )


_CpqCmcStatusLock2Dev_Type.__name__ = "Integer32"
_CpqCmcStatusLock2Dev_Object = MibScalar
cpqCmcStatusLock2Dev = _CpqCmcStatusLock2Dev_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 4, 20),
    _CpqCmcStatusLock2Dev_Type()
)
cpqCmcStatusLock2Dev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcStatusLock2Dev.setStatus("mandatory")
_CpqCmcControl_ObjectIdentity = ObjectIdentity
cpqCmcControl = _CpqCmcControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5)
)


class _CpqCmcStatusAccess_Type(DisplayString):
    """Custom type cpqCmcStatusAccess based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CpqCmcStatusAccess_Type.__name__ = "DisplayString"
_CpqCmcStatusAccess_Object = MibScalar
cpqCmcStatusAccess = _CpqCmcStatusAccess_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5, 1),
    _CpqCmcStatusAccess_Type()
)
cpqCmcStatusAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcStatusAccess.setStatus("mandatory")


class _CpqCmcSetLock1Lock_Type(Integer32):
    """Custom type cpqCmcSetLock1Lock based on Integer32"""
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
        *(("lockDoor", 2),
          ("openDoor", 4),
          ("openDoorTime", 3),
          ("other", 1))
    )


_CpqCmcSetLock1Lock_Type.__name__ = "Integer32"
_CpqCmcSetLock1Lock_Object = MibScalar
cpqCmcSetLock1Lock = _CpqCmcSetLock1Lock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5, 2),
    _CpqCmcSetLock1Lock_Type()
)
cpqCmcSetLock1Lock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetLock1Lock.setStatus("mandatory")


class _CpqCmcSetLock1Key_Type(Integer32):
    """Custom type cpqCmcSetLock1Key based on Integer32"""
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
        *(("disable", 2),
          ("enableBoth", 3),
          ("enableKeypad", 4),
          ("enableRemoteInput", 5),
          ("other", 1))
    )


_CpqCmcSetLock1Key_Type.__name__ = "Integer32"
_CpqCmcSetLock1Key_Object = MibScalar
cpqCmcSetLock1Key = _CpqCmcSetLock1Key_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5, 3),
    _CpqCmcSetLock1Key_Type()
)
cpqCmcSetLock1Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetLock1Key.setStatus("mandatory")


class _CpqCmcSetLock2Lock_Type(Integer32):
    """Custom type cpqCmcSetLock2Lock based on Integer32"""
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
        *(("lockDoor", 2),
          ("openDoor", 4),
          ("openDoorTime", 3),
          ("other", 1))
    )


_CpqCmcSetLock2Lock_Type.__name__ = "Integer32"
_CpqCmcSetLock2Lock_Object = MibScalar
cpqCmcSetLock2Lock = _CpqCmcSetLock2Lock_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5, 4),
    _CpqCmcSetLock2Lock_Type()
)
cpqCmcSetLock2Lock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetLock2Lock.setStatus("mandatory")


class _CpqCmcSetLock2Key_Type(Integer32):
    """Custom type cpqCmcSetLock2Key based on Integer32"""
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
        *(("disable", 2),
          ("enableBoth", 3),
          ("enableKeypad", 4),
          ("enableRemoteInput", 5),
          ("other", 1))
    )


_CpqCmcSetLock2Key_Type.__name__ = "Integer32"
_CpqCmcSetLock2Key_Object = MibScalar
cpqCmcSetLock2Key = _CpqCmcSetLock2Key_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5, 5),
    _CpqCmcSetLock2Key_Type()
)
cpqCmcSetLock2Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetLock2Key.setStatus("mandatory")


class _CpqCmcSetMessage_Type(DisplayString):
    """Custom type cpqCmcSetMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CpqCmcSetMessage_Type.__name__ = "DisplayString"
_CpqCmcSetMessage_Object = MibScalar
cpqCmcSetMessage = _CpqCmcSetMessage_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5, 6),
    _CpqCmcSetMessage_Type()
)
cpqCmcSetMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetMessage.setStatus("mandatory")


class _CpqCmcSetAlarm1_Type(Integer32):
    """Custom type cpqCmcSetAlarm1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearAlarm", 2),
          ("other", 1),
          ("setAlarm", 3))
    )


_CpqCmcSetAlarm1_Type.__name__ = "Integer32"
_CpqCmcSetAlarm1_Object = MibScalar
cpqCmcSetAlarm1 = _CpqCmcSetAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5, 7),
    _CpqCmcSetAlarm1_Type()
)
cpqCmcSetAlarm1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetAlarm1.setStatus("mandatory")


class _CpqCmcSetAlarm2_Type(Integer32):
    """Custom type cpqCmcSetAlarm2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearAlarm", 2),
          ("other", 1),
          ("setAlarm", 3))
    )


_CpqCmcSetAlarm2_Type.__name__ = "Integer32"
_CpqCmcSetAlarm2_Object = MibScalar
cpqCmcSetAlarm2 = _CpqCmcSetAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5, 8),
    _CpqCmcSetAlarm2_Type()
)
cpqCmcSetAlarm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetAlarm2.setStatus("mandatory")


class _CpqCmcSetFan1_Type(Integer32):
    """Custom type cpqCmcSetFan1 based on Integer32"""
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
          ("off", 4),
          ("on", 3),
          ("other", 1))
    )


_CpqCmcSetFan1_Type.__name__ = "Integer32"
_CpqCmcSetFan1_Object = MibScalar
cpqCmcSetFan1 = _CpqCmcSetFan1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5, 9),
    _CpqCmcSetFan1_Type()
)
cpqCmcSetFan1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetFan1.setStatus("mandatory")


class _CpqCmcSetFan2_Type(Integer32):
    """Custom type cpqCmcSetFan2 based on Integer32"""
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
          ("off", 4),
          ("on", 3),
          ("other", 1))
    )


_CpqCmcSetFan2_Type.__name__ = "Integer32"
_CpqCmcSetFan2_Object = MibScalar
cpqCmcSetFan2 = _CpqCmcSetFan2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5, 10),
    _CpqCmcSetFan2_Type()
)
cpqCmcSetFan2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetFan2.setStatus("mandatory")


class _CpqCmcSetQuitRelay1_Type(Integer32):
    """Custom type cpqCmcSetQuitRelay1 based on Integer32"""
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
        *(("notSwitched", 3),
          ("other", 1),
          ("quit", 4),
          ("switched", 2))
    )


_CpqCmcSetQuitRelay1_Type.__name__ = "Integer32"
_CpqCmcSetQuitRelay1_Object = MibScalar
cpqCmcSetQuitRelay1 = _CpqCmcSetQuitRelay1_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5, 11),
    _CpqCmcSetQuitRelay1_Type()
)
cpqCmcSetQuitRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetQuitRelay1.setStatus("mandatory")


class _CpqCmcSetQuitRelay2_Type(Integer32):
    """Custom type cpqCmcSetQuitRelay2 based on Integer32"""
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
        *(("notSwitched", 3),
          ("other", 1),
          ("quit", 4),
          ("switched", 2))
    )


_CpqCmcSetQuitRelay2_Type.__name__ = "Integer32"
_CpqCmcSetQuitRelay2_Object = MibScalar
cpqCmcSetQuitRelay2 = _CpqCmcSetQuitRelay2_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 5, 12),
    _CpqCmcSetQuitRelay2_Type()
)
cpqCmcSetQuitRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqCmcSetQuitRelay2.setStatus("mandatory")
_CpqCmcLog_ObjectIdentity = ObjectIdentity
cpqCmcLog = _CpqCmcLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 6)
)


class _CpqCmcLogsNumber_Type(Integer32):
    """Custom type cpqCmcLogsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpqCmcLogsNumber_Type.__name__ = "Integer32"
_CpqCmcLogsNumber_Object = MibScalar
cpqCmcLogsNumber = _CpqCmcLogsNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 6, 1),
    _CpqCmcLogsNumber_Type()
)
cpqCmcLogsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcLogsNumber.setStatus("mandatory")
_CpqCmcLogTable_Object = MibTable
cpqCmcLogTable = _CpqCmcLogTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 6, 2)
)
if mibBuilder.loadTexts:
    cpqCmcLogTable.setStatus("mandatory")
_CpqCmcLogEntry_Object = MibTableRow
cpqCmcLogEntry = _CpqCmcLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 6, 2, 1)
)
cpqCmcLogEntry.setIndexNames(
    (0, "CPQCMC-MIB", "cpqCmcLogIndex"),
)
if mibBuilder.loadTexts:
    cpqCmcLogEntry.setStatus("mandatory")


class _CpqCmcLogIndex_Type(Integer32):
    """Custom type cpqCmcLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpqCmcLogIndex_Type.__name__ = "Integer32"
_CpqCmcLogIndex_Object = MibTableColumn
cpqCmcLogIndex = _CpqCmcLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 6, 2, 1, 1),
    _CpqCmcLogIndex_Type()
)
cpqCmcLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcLogIndex.setStatus("mandatory")


class _CpqCmcLogDate_Type(DisplayString):
    """Custom type cpqCmcLogDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_CpqCmcLogDate_Type.__name__ = "DisplayString"
_CpqCmcLogDate_Object = MibTableColumn
cpqCmcLogDate = _CpqCmcLogDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 6, 2, 1, 2),
    _CpqCmcLogDate_Type()
)
cpqCmcLogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcLogDate.setStatus("mandatory")


class _CpqCmcLogTime_Type(DisplayString):
    """Custom type cpqCmcLogTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_CpqCmcLogTime_Type.__name__ = "DisplayString"
_CpqCmcLogTime_Object = MibTableColumn
cpqCmcLogTime = _CpqCmcLogTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 6, 2, 1, 3),
    _CpqCmcLogTime_Type()
)
cpqCmcLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcLogTime.setStatus("mandatory")


class _CpqCmcLogText_Type(DisplayString):
    """Custom type cpqCmcLogText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CpqCmcLogText_Type.__name__ = "DisplayString"
_CpqCmcLogText_Object = MibTableColumn
cpqCmcLogText = _CpqCmcLogText_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 6, 2, 1, 4),
    _CpqCmcLogText_Type()
)
cpqCmcLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcLogText.setStatus("mandatory")


class _CpqCmcLogClass_Type(DisplayString):
    """Custom type cpqCmcLogClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CpqCmcLogClass_Type.__name__ = "DisplayString"
_CpqCmcLogClass_Object = MibTableColumn
cpqCmcLogClass = _CpqCmcLogClass_Object(
    (1, 3, 6, 1, 4, 1, 232, 153, 2, 2, 6, 2, 1, 5),
    _CpqCmcLogClass_Type()
)
cpqCmcLogClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqCmcLogClass.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqCmcalarmTemp1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153001)
)
cpqCmcalarmTemp1.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusTemp1"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmTemp1.setStatus(
        ""
    )

cpqCmcalarmTemp2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153002)
)
cpqCmcalarmTemp2.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusTemp2"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmTemp2.setStatus(
        ""
    )

cpqCmcalarmFan1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153003)
)
cpqCmcalarmFan1.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusFan1"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmFan1.setStatus(
        ""
    )

cpqCmcalarmFan2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153004)
)
cpqCmcalarmFan2.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusFan2"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmFan2.setStatus(
        ""
    )

cpqCmcalarmVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153005)
)
cpqCmcalarmVoltage.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusVoltage"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmVoltage.setStatus(
        ""
    )

cpqCmcalarmHumidity = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153006)
)
cpqCmcalarmHumidity.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusHumidity"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmHumidity.setStatus(
        ""
    )

cpqCmcalarmInput1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153007)
)
cpqCmcalarmInput1.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusInput1"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmInput1.setStatus(
        ""
    )

cpqCmcalarmInput2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153008)
)
cpqCmcalarmInput2.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusInput2"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmInput2.setStatus(
        ""
    )

cpqCmcalarmInput3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153009)
)
cpqCmcalarmInput3.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusInput3"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmInput3.setStatus(
        ""
    )

cpqCmcalarmInput4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153010)
)
cpqCmcalarmInput4.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusInput4"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmInput4.setStatus(
        ""
    )

cpqCmcalarmLock1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153011)
)
cpqCmcalarmLock1.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusLock1Lock"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmLock1.setStatus(
        ""
    )

cpqCmcalarmLock2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153012)
)
cpqCmcalarmLock2.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusLock2Lock"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmLock2.setStatus(
        ""
    )

cpqCmcalarmSmoke = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153013)
)
cpqCmcalarmSmoke.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusSmoke"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmSmoke.setStatus(
        ""
    )

cpqCmcalarmShock = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153014)
)
cpqCmcalarmShock.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusShock"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmShock.setStatus(
        ""
    )

cpqCmcalarmAux1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153015)
)
cpqCmcalarmAux1.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusAux1"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmAux1.setStatus(
        ""
    )

cpqCmcalarmAux2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153016)
)
cpqCmcalarmAux2.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusAux2"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmAux2.setStatus(
        ""
    )

cpqCmcalarm1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153017)
)
cpqCmcalarm1.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusAlarm1"))
)
if mibBuilder.loadTexts:
    cpqCmcalarm1.setStatus(
        ""
    )

cpqCmcalarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153018)
)
cpqCmcalarm2.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusAlarm2"))
)
if mibBuilder.loadTexts:
    cpqCmcalarm2.setStatus(
        ""
    )

cpqCmcalarmLock1Dev = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153019)
)
cpqCmcalarmLock1Dev.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusLock1Dev"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmLock1Dev.setStatus(
        ""
    )

cpqCmcalarmLock2Dev = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153020)
)
cpqCmcalarmLock2Dev.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQCMC-MIB", "cpqCmcStatusLock2Dev"))
)
if mibBuilder.loadTexts:
    cpqCmcalarmLock2Dev.setStatus(
        ""
    )

cpqCmcSetupChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 153, 0, 153100)
)
cpqCmcSetupChanged.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    cpqCmcSetupChanged.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQCMC-MIB",
    **{"cpqCmc": cpqCmc,
       "cpqCmcalarmTemp1": cpqCmcalarmTemp1,
       "cpqCmcalarmTemp2": cpqCmcalarmTemp2,
       "cpqCmcalarmFan1": cpqCmcalarmFan1,
       "cpqCmcalarmFan2": cpqCmcalarmFan2,
       "cpqCmcalarmVoltage": cpqCmcalarmVoltage,
       "cpqCmcalarmHumidity": cpqCmcalarmHumidity,
       "cpqCmcalarmInput1": cpqCmcalarmInput1,
       "cpqCmcalarmInput2": cpqCmcalarmInput2,
       "cpqCmcalarmInput3": cpqCmcalarmInput3,
       "cpqCmcalarmInput4": cpqCmcalarmInput4,
       "cpqCmcalarmLock1": cpqCmcalarmLock1,
       "cpqCmcalarmLock2": cpqCmcalarmLock2,
       "cpqCmcalarmSmoke": cpqCmcalarmSmoke,
       "cpqCmcalarmShock": cpqCmcalarmShock,
       "cpqCmcalarmAux1": cpqCmcalarmAux1,
       "cpqCmcalarmAux2": cpqCmcalarmAux2,
       "cpqCmcalarm1": cpqCmcalarm1,
       "cpqCmcalarm2": cpqCmcalarm2,
       "cpqCmcalarmLock1Dev": cpqCmcalarmLock1Dev,
       "cpqCmcalarmLock2Dev": cpqCmcalarmLock2Dev,
       "cpqCmcSetupChanged": cpqCmcSetupChanged,
       "cpqCmcMibRev": cpqCmcMibRev,
       "cpqCmcMibRevMajor": cpqCmcMibRevMajor,
       "cpqCmcMibRevMinor": cpqCmcMibRevMinor,
       "cpqCmcMibCondition": cpqCmcMibCondition,
       "cpqCmcComponent": cpqCmcComponent,
       "cpqCmcInterface": cpqCmcInterface,
       "cpqCmcOsCommon": cpqCmcOsCommon,
       "cpqCmcOsCommonPollFreq": cpqCmcOsCommonPollFreq,
       "cpqCmcDevice": cpqCmcDevice,
       "cpqCmcDeviceCondition": cpqCmcDeviceCondition,
       "cpqCmcSetup": cpqCmcSetup,
       "cpqCmcSetupConfig": cpqCmcSetupConfig,
       "cpqCmcSetupGeneral": cpqCmcSetupGeneral,
       "cpqCmcsetLanguage": cpqCmcsetLanguage,
       "cpqCmcsetTempUnit": cpqCmcsetTempUnit,
       "cpqCmcsetAudibleAlarm": cpqCmcsetAudibleAlarm,
       "cpqCmcPassword": cpqCmcPassword,
       "cpqCmcPasswordOption": cpqCmcPasswordOption,
       "cpqCmcquitRelay1": cpqCmcquitRelay1,
       "cpqCmcquitRelay2": cpqCmcquitRelay2,
       "cpqCmclogicRelay1": cpqCmclogicRelay1,
       "cpqCmclogicRelay2": cpqCmclogicRelay2,
       "cpqCmcSetupEvents": cpqCmcSetupEvents,
       "cpqCmcSetupTemp1": cpqCmcSetupTemp1,
       "cpqCmcSetupTemp1Avail": cpqCmcSetupTemp1Avail,
       "cpqCmcSetupTemp1RelaysWarn": cpqCmcSetupTemp1RelaysWarn,
       "cpqCmcSetupTemp1RelaysMax": cpqCmcSetupTemp1RelaysMax,
       "cpqCmcSetupTemp1RelaysMin": cpqCmcSetupTemp1RelaysMin,
       "cpqCmcSetupTemp1AudibleAlarmWarn": cpqCmcSetupTemp1AudibleAlarmWarn,
       "cpqCmcSetupTemp1AudibleAlarmMax": cpqCmcSetupTemp1AudibleAlarmMax,
       "cpqCmcSetupTemp1AudibleAlarmMin": cpqCmcSetupTemp1AudibleAlarmMin,
       "cpqCmcSetupTemp2": cpqCmcSetupTemp2,
       "cpqCmcSetupTemp2Avail": cpqCmcSetupTemp2Avail,
       "cpqCmcSetupTemp2RelaysWarn": cpqCmcSetupTemp2RelaysWarn,
       "cpqCmcSetupTemp2RelaysMax": cpqCmcSetupTemp2RelaysMax,
       "cpqCmcSetupTemp2RelaysMin": cpqCmcSetupTemp2RelaysMin,
       "cpqCmcSetupTemp2AudibleAlarmWarn": cpqCmcSetupTemp2AudibleAlarmWarn,
       "cpqCmcSetupTemp2AudibleAlarmMax": cpqCmcSetupTemp2AudibleAlarmMax,
       "cpqCmcSetupTemp2AudibleAlarmMin": cpqCmcSetupTemp2AudibleAlarmMin,
       "cpqCmcSetupFan1": cpqCmcSetupFan1,
       "cpqCmcSetupFan1Avail": cpqCmcSetupFan1Avail,
       "cpqCmcSetupFan1Relays": cpqCmcSetupFan1Relays,
       "cpqCmcSetupFan1AudibleAlarm": cpqCmcSetupFan1AudibleAlarm,
       "cpqCmcSetupFan2": cpqCmcSetupFan2,
       "cpqCmcSetupFan2Avail": cpqCmcSetupFan2Avail,
       "cpqCmcSetupFan2Relays": cpqCmcSetupFan2Relays,
       "cpqCmcSetupFan2AudibleAlarm": cpqCmcSetupFan2AudibleAlarm,
       "cpqCmcSetupVoltage": cpqCmcSetupVoltage,
       "cpqCmcSetupVoltageAvail": cpqCmcSetupVoltageAvail,
       "cpqCmcSetupVoltageRelaysMax": cpqCmcSetupVoltageRelaysMax,
       "cpqCmcSetupVoltageRelaysMin": cpqCmcSetupVoltageRelaysMin,
       "cpqCmcSetupVoltageAudibleAlarmMax": cpqCmcSetupVoltageAudibleAlarmMax,
       "cpqCmcSetupVoltageAudibleAlarmMin": cpqCmcSetupVoltageAudibleAlarmMin,
       "cpqCmcSetupHumidity": cpqCmcSetupHumidity,
       "cpqCmcSetupHumidityAvail": cpqCmcSetupHumidityAvail,
       "cpqCmcSetupHumidityRelaysMax": cpqCmcSetupHumidityRelaysMax,
       "cpqCmcSetupHumidityRelaysMin": cpqCmcSetupHumidityRelaysMin,
       "cpqCmcSetupHumidityAudibleAlarmMax": cpqCmcSetupHumidityAudibleAlarmMax,
       "cpqCmcSetupHumidityAudibleAlarmMin": cpqCmcSetupHumidityAudibleAlarmMin,
       "cpqCmcSetupInput1": cpqCmcSetupInput1,
       "cpqCmcSetupInput1Avail": cpqCmcSetupInput1Avail,
       "cpqCmcSetupInput1Relays": cpqCmcSetupInput1Relays,
       "cpqCmcSetupInput1AudibleAlarm": cpqCmcSetupInput1AudibleAlarm,
       "cpqCmcSetupInput1FansOff": cpqCmcSetupInput1FansOff,
       "cpqCmcSetupInput1ShockSensor": cpqCmcSetupInput1ShockSensor,
       "cpqCmcSetupInput1Description": cpqCmcSetupInput1Description,
       "cpqCmcSetupInput1Lock": cpqCmcSetupInput1Lock,
       "cpqCmcSetupInput2": cpqCmcSetupInput2,
       "cpqCmcSetupInput2Avail": cpqCmcSetupInput2Avail,
       "cpqCmcSetupInput2Relays": cpqCmcSetupInput2Relays,
       "cpqCmcSetupInput2AudibleAlarm": cpqCmcSetupInput2AudibleAlarm,
       "cpqCmcSetupInput2FansOff": cpqCmcSetupInput2FansOff,
       "cpqCmcSetupInput2ShockSensor": cpqCmcSetupInput2ShockSensor,
       "cpqCmcSetupInput2Description": cpqCmcSetupInput2Description,
       "cpqCmcSetupInput2Lock": cpqCmcSetupInput2Lock,
       "cpqCmcSetupInput3": cpqCmcSetupInput3,
       "cpqCmcSetupInput3Avail": cpqCmcSetupInput3Avail,
       "cpqCmcSetupInput3Relays": cpqCmcSetupInput3Relays,
       "cpqCmcSetupInput3AudibleAlarm": cpqCmcSetupInput3AudibleAlarm,
       "cpqCmcSetupInput3FansOff": cpqCmcSetupInput3FansOff,
       "cpqCmcSetupInput3ShockSensor": cpqCmcSetupInput3ShockSensor,
       "cpqCmcSetupInput3Description": cpqCmcSetupInput3Description,
       "cpqCmcSetupInput3Lock": cpqCmcSetupInput3Lock,
       "cpqCmcSetupInput4": cpqCmcSetupInput4,
       "cpqCmcSetupInput4Avail": cpqCmcSetupInput4Avail,
       "cpqCmcSetupInput4Relays": cpqCmcSetupInput4Relays,
       "cpqCmcSetupInput4AudibleAlarm": cpqCmcSetupInput4AudibleAlarm,
       "cpqCmcSetupInput4FansOff": cpqCmcSetupInput4FansOff,
       "cpqCmcSetupInput4ShockSensor": cpqCmcSetupInput4ShockSensor,
       "cpqCmcSetupInput4Description": cpqCmcSetupInput4Description,
       "cpqCmcSetupInput4Lock": cpqCmcSetupInput4Lock,
       "cpqCmcSetupLock1": cpqCmcSetupLock1,
       "cpqCmcSetupLock1Avail": cpqCmcSetupLock1Avail,
       "cpqCmcSetupLock1Relays": cpqCmcSetupLock1Relays,
       "cpqCmcSetupLock1RelaysDevice": cpqCmcSetupLock1RelaysDevice,
       "cpqCmcSetupLock1AudibleAlarm": cpqCmcSetupLock1AudibleAlarm,
       "cpqCmcSetupLock1AudibleAlarmDevice": cpqCmcSetupLock1AudibleAlarmDevice,
       "cpqCmcSetupLock1Time": cpqCmcSetupLock1Time,
       "cpqCmcSetupLock1PwrFailUnlock": cpqCmcSetupLock1PwrFailUnlock,
       "cpqCmcSetupLock1BattLowUnlock": cpqCmcSetupLock1BattLowUnlock,
       "cpqCmcSetupLock1NetFailUnlock": cpqCmcSetupLock1NetFailUnlock,
       "cpqCmcSetupLock1LifeFailUnlock": cpqCmcSetupLock1LifeFailUnlock,
       "cpqCmcSetupLock2": cpqCmcSetupLock2,
       "cpqCmcSetupLock2Avail": cpqCmcSetupLock2Avail,
       "cpqCmcSetupLock2Relays": cpqCmcSetupLock2Relays,
       "cpqCmcSetupLock2RelaysDevice": cpqCmcSetupLock2RelaysDevice,
       "cpqCmcSetupLock2AudibleAlarm": cpqCmcSetupLock2AudibleAlarm,
       "cpqCmcSetupLock2AudibleAlarmDevice": cpqCmcSetupLock2AudibleAlarmDevice,
       "cpqCmcSetupLock2Time": cpqCmcSetupLock2Time,
       "cpqCmcSetupLock2PwrFailUnlock": cpqCmcSetupLock2PwrFailUnlock,
       "cpqCmcSetupLock2BattLowUnlock": cpqCmcSetupLock2BattLowUnlock,
       "cpqCmcSetupLock2NetFailUnlock": cpqCmcSetupLock2NetFailUnlock,
       "cpqCmcSetupLock2LifeFailUnlock": cpqCmcSetupLock2LifeFailUnlock,
       "cpqCmcSetupSmoke": cpqCmcSetupSmoke,
       "cpqCmcSetupSmokeAvail": cpqCmcSetupSmokeAvail,
       "cpqCmcSetupSmokeRelays": cpqCmcSetupSmokeRelays,
       "cpqCmcSetupSmokeAudibleAlarm": cpqCmcSetupSmokeAudibleAlarm,
       "cpqCmcSetupSmokeFansOff": cpqCmcSetupSmokeFansOff,
       "cpqCmcSetupSmokeUnlock": cpqCmcSetupSmokeUnlock,
       "cpqCmcSetupShock": cpqCmcSetupShock,
       "cpqCmcSetupShockAvail": cpqCmcSetupShockAvail,
       "cpqCmcSetupShockRelays": cpqCmcSetupShockRelays,
       "cpqCmcSetupShockAudibleAlarm": cpqCmcSetupShockAudibleAlarm,
       "cpqCmcSetupShockSensitivity": cpqCmcSetupShockSensitivity,
       "cpqCmcSetupAux1": cpqCmcSetupAux1,
       "cpqCmcSetupAux1Avail": cpqCmcSetupAux1Avail,
       "cpqCmcSetupAux1Relays": cpqCmcSetupAux1Relays,
       "cpqCmcSetupAux1AudibleAlarm": cpqCmcSetupAux1AudibleAlarm,
       "cpqCmcSetupAux1InputType": cpqCmcSetupAux1InputType,
       "cpqCmcSetupAux1Description": cpqCmcSetupAux1Description,
       "cpqCmcSetupAux1Unlock": cpqCmcSetupAux1Unlock,
       "cpqCmcSetupAux2": cpqCmcSetupAux2,
       "cpqCmcSetupAux2Avail": cpqCmcSetupAux2Avail,
       "cpqCmcSetupAux2Relays": cpqCmcSetupAux2Relays,
       "cpqCmcSetupAux2AudibleAlarm": cpqCmcSetupAux2AudibleAlarm,
       "cpqCmcSetupAux2InputType": cpqCmcSetupAux2InputType,
       "cpqCmcSetupAux2Description": cpqCmcSetupAux2Description,
       "cpqCmcSetupAux2Unlock": cpqCmcSetupAux2Unlock,
       "cpqCmcSetupAlarm1": cpqCmcSetupAlarm1,
       "cpqCmcSetupAlarm1Relays": cpqCmcSetupAlarm1Relays,
       "cpqCmcSetupAlarm1AudibleAlarm": cpqCmcSetupAlarm1AudibleAlarm,
       "cpqCmcSetupAlarm1Description": cpqCmcSetupAlarm1Description,
       "cpqCmcSetupAlarm2": cpqCmcSetupAlarm2,
       "cpqCmcSetupAlarm2Relays": cpqCmcSetupAlarm2Relays,
       "cpqCmcSetupAlarm2AudibleAlarm": cpqCmcSetupAlarm2AudibleAlarm,
       "cpqCmcSetupAlarm2Description": cpqCmcSetupAlarm2Description,
       "cpqCmcSetupClock": cpqCmcSetupClock,
       "cpqCmcSetupDate": cpqCmcSetupDate,
       "cpqCmcSetupTime": cpqCmcSetupTime,
       "cpqCmcSetupThreshold": cpqCmcSetupThreshold,
       "cpqCmcThresholdMaxTemp1": cpqCmcThresholdMaxTemp1,
       "cpqCmcThresholdWarningTemp1": cpqCmcThresholdWarningTemp1,
       "cpqCmcThresholdMinTemp1": cpqCmcThresholdMinTemp1,
       "cpqCmcThresholdMaxTemp2": cpqCmcThresholdMaxTemp2,
       "cpqCmcThresholdWarningTemp2": cpqCmcThresholdWarningTemp2,
       "cpqCmcThresholdMinTemp2": cpqCmcThresholdMinTemp2,
       "cpqCmcThresholdFan1": cpqCmcThresholdFan1,
       "cpqCmcThresholdFan1Hysteresis": cpqCmcThresholdFan1Hysteresis,
       "cpqCmcThresholdFan2": cpqCmcThresholdFan2,
       "cpqCmcThresholdFan2Hysteresis": cpqCmcThresholdFan2Hysteresis,
       "cpqCmcThresholdMaxVoltage": cpqCmcThresholdMaxVoltage,
       "cpqCmcThresholdMinVoltage": cpqCmcThresholdMinVoltage,
       "cpqCmcThresholdMaxHumidity": cpqCmcThresholdMaxHumidity,
       "cpqCmcThresholdMinHumidity": cpqCmcThresholdMinHumidity,
       "cpqCmcTraps": cpqCmcTraps,
       "cpqCmcTrapTableNumber": cpqCmcTrapTableNumber,
       "cpqCmcTrapTable": cpqCmcTrapTable,
       "cpqCmcTrapEntry": cpqCmcTrapEntry,
       "cpqCmcTrapIndex": cpqCmcTrapIndex,
       "cpqCmcTrapStatus": cpqCmcTrapStatus,
       "cpqCmcTrapIPaddress": cpqCmcTrapIPaddress,
       "cpqCmcValues": cpqCmcValues,
       "cpqCmcValueTemp1": cpqCmcValueTemp1,
       "cpqCmcValueTemp2": cpqCmcValueTemp2,
       "cpqCmcValueVoltage": cpqCmcValueVoltage,
       "cpqCmcValueHumidity": cpqCmcValueHumidity,
       "cpqCmcValueOperatingTime": cpqCmcValueOperatingTime,
       "cpqCmcStatus": cpqCmcStatus,
       "cpqCmcStatusTemp1": cpqCmcStatusTemp1,
       "cpqCmcStatusTemp2": cpqCmcStatusTemp2,
       "cpqCmcStatusFan1": cpqCmcStatusFan1,
       "cpqCmcStatusFan2": cpqCmcStatusFan2,
       "cpqCmcStatusVoltage": cpqCmcStatusVoltage,
       "cpqCmcStatusHumidity": cpqCmcStatusHumidity,
       "cpqCmcStatusInput1": cpqCmcStatusInput1,
       "cpqCmcStatusInput2": cpqCmcStatusInput2,
       "cpqCmcStatusInput3": cpqCmcStatusInput3,
       "cpqCmcStatusInput4": cpqCmcStatusInput4,
       "cpqCmcStatusLock1Lock": cpqCmcStatusLock1Lock,
       "cpqCmcStatusLock2Lock": cpqCmcStatusLock2Lock,
       "cpqCmcStatusSmoke": cpqCmcStatusSmoke,
       "cpqCmcStatusShock": cpqCmcStatusShock,
       "cpqCmcStatusAux1": cpqCmcStatusAux1,
       "cpqCmcStatusAux2": cpqCmcStatusAux2,
       "cpqCmcStatusAlarm1": cpqCmcStatusAlarm1,
       "cpqCmcStatusAlarm2": cpqCmcStatusAlarm2,
       "cpqCmcStatusLock1Dev": cpqCmcStatusLock1Dev,
       "cpqCmcStatusLock2Dev": cpqCmcStatusLock2Dev,
       "cpqCmcControl": cpqCmcControl,
       "cpqCmcStatusAccess": cpqCmcStatusAccess,
       "cpqCmcSetLock1Lock": cpqCmcSetLock1Lock,
       "cpqCmcSetLock1Key": cpqCmcSetLock1Key,
       "cpqCmcSetLock2Lock": cpqCmcSetLock2Lock,
       "cpqCmcSetLock2Key": cpqCmcSetLock2Key,
       "cpqCmcSetMessage": cpqCmcSetMessage,
       "cpqCmcSetAlarm1": cpqCmcSetAlarm1,
       "cpqCmcSetAlarm2": cpqCmcSetAlarm2,
       "cpqCmcSetFan1": cpqCmcSetFan1,
       "cpqCmcSetFan2": cpqCmcSetFan2,
       "cpqCmcSetQuitRelay1": cpqCmcSetQuitRelay1,
       "cpqCmcSetQuitRelay2": cpqCmcSetQuitRelay2,
       "cpqCmcLog": cpqCmcLog,
       "cpqCmcLogsNumber": cpqCmcLogsNumber,
       "cpqCmcLogTable": cpqCmcLogTable,
       "cpqCmcLogEntry": cpqCmcLogEntry,
       "cpqCmcLogIndex": cpqCmcLogIndex,
       "cpqCmcLogDate": cpqCmcLogDate,
       "cpqCmcLogTime": cpqCmcLogTime,
       "cpqCmcLogText": cpqCmcLogText,
       "cpqCmcLogClass": cpqCmcLogClass}
)
