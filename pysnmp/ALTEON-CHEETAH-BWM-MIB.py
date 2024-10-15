# SNMP MIB module (ALTEON-CHEETAH-BWM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-CHEETAH-BWM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:48 2024
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

(aws_switch,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "aws-switch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

bwm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6)
)
bwm.setRevisions(
        ("2009-08-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BwmConfigs_ObjectIdentity = ObjectIdentity
bwmConfigs = _BwmConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1)
)
_BwmGeneralConfig_ObjectIdentity = ObjectIdentity
bwmGeneralConfig = _BwmGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1)
)


class _BwmCurCfgGenState_Type(Integer32):
    """Custom type bwmCurCfgGenState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_BwmCurCfgGenState_Type.__name__ = "Integer32"
_BwmCurCfgGenState_Object = MibScalar
bwmCurCfgGenState = _BwmCurCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 1),
    _BwmCurCfgGenState_Type()
)
bwmCurCfgGenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenState.setStatus("current")


class _BwmNewCfgGenState_Type(Integer32):
    """Custom type bwmNewCfgGenState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_BwmNewCfgGenState_Type.__name__ = "Integer32"
_BwmNewCfgGenState_Object = MibScalar
bwmNewCfgGenState = _BwmNewCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 2),
    _BwmNewCfgGenState_Type()
)
bwmNewCfgGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenState.setStatus("current")


class _BwmCurCfgGenEnforcePolicy_Type(Integer32):
    """Custom type bwmCurCfgGenEnforcePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmCurCfgGenEnforcePolicy_Type.__name__ = "Integer32"
_BwmCurCfgGenEnforcePolicy_Object = MibScalar
bwmCurCfgGenEnforcePolicy = _BwmCurCfgGenEnforcePolicy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 3),
    _BwmCurCfgGenEnforcePolicy_Type()
)
bwmCurCfgGenEnforcePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenEnforcePolicy.setStatus("current")


class _BwmNewCfgGenEnforcePolicy_Type(Integer32):
    """Custom type bwmNewCfgGenEnforcePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmNewCfgGenEnforcePolicy_Type.__name__ = "Integer32"
_BwmNewCfgGenEnforcePolicy_Object = MibScalar
bwmNewCfgGenEnforcePolicy = _BwmNewCfgGenEnforcePolicy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 4),
    _BwmNewCfgGenEnforcePolicy_Type()
)
bwmNewCfgGenEnforcePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenEnforcePolicy.setStatus("current")


class _BwmCurCfgGenSmtpUser_Type(DisplayString):
    """Custom type bwmCurCfgGenSmtpUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BwmCurCfgGenSmtpUser_Type.__name__ = "DisplayString"
_BwmCurCfgGenSmtpUser_Object = MibScalar
bwmCurCfgGenSmtpUser = _BwmCurCfgGenSmtpUser_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 5),
    _BwmCurCfgGenSmtpUser_Type()
)
bwmCurCfgGenSmtpUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenSmtpUser.setStatus("current")


class _BwmNewCfgGenSmtpUser_Type(DisplayString):
    """Custom type bwmNewCfgGenSmtpUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BwmNewCfgGenSmtpUser_Type.__name__ = "DisplayString"
_BwmNewCfgGenSmtpUser_Object = MibScalar
bwmNewCfgGenSmtpUser = _BwmNewCfgGenSmtpUser_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 6),
    _BwmNewCfgGenSmtpUser_Type()
)
bwmNewCfgGenSmtpUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenSmtpUser.setStatus("current")


class _BwmCurCfgGenEmailFrequency_Type(Integer32):
    """Custom type bwmCurCfgGenEmailFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_BwmCurCfgGenEmailFrequency_Type.__name__ = "Integer32"
_BwmCurCfgGenEmailFrequency_Object = MibScalar
bwmCurCfgGenEmailFrequency = _BwmCurCfgGenEmailFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 7),
    _BwmCurCfgGenEmailFrequency_Type()
)
bwmCurCfgGenEmailFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenEmailFrequency.setStatus("current")


class _BwmNewCfgGenEmailFrequency_Type(Integer32):
    """Custom type bwmNewCfgGenEmailFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_BwmNewCfgGenEmailFrequency_Type.__name__ = "Integer32"
_BwmNewCfgGenEmailFrequency_Object = MibScalar
bwmNewCfgGenEmailFrequency = _BwmNewCfgGenEmailFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 8),
    _BwmNewCfgGenEmailFrequency_Type()
)
bwmNewCfgGenEmailFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenEmailFrequency.setStatus("current")


class _BwmCurCfgGenIPUserLimit_Type(DisplayString):
    """Custom type bwmCurCfgGenIPUserLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BwmCurCfgGenIPUserLimit_Type.__name__ = "DisplayString"
_BwmCurCfgGenIPUserLimit_Object = MibScalar
bwmCurCfgGenIPUserLimit = _BwmCurCfgGenIPUserLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 9),
    _BwmCurCfgGenIPUserLimit_Type()
)
bwmCurCfgGenIPUserLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenIPUserLimit.setStatus("current")


class _BwmNewCfgGenIPUserLimit_Type(DisplayString):
    """Custom type bwmNewCfgGenIPUserLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BwmNewCfgGenIPUserLimit_Type.__name__ = "DisplayString"
_BwmNewCfgGenIPUserLimit_Object = MibScalar
bwmNewCfgGenIPUserLimit = _BwmNewCfgGenIPUserLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 10),
    _BwmNewCfgGenIPUserLimit_Type()
)
bwmNewCfgGenIPUserLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenIPUserLimit.setStatus("current")


class _BwmCurCfgGenEmail_Type(Integer32):
    """Custom type bwmCurCfgGenEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmCurCfgGenEmail_Type.__name__ = "Integer32"
_BwmCurCfgGenEmail_Object = MibScalar
bwmCurCfgGenEmail = _BwmCurCfgGenEmail_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 11),
    _BwmCurCfgGenEmail_Type()
)
bwmCurCfgGenEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenEmail.setStatus("current")


class _BwmNewCfgGenEmail_Type(Integer32):
    """Custom type bwmNewCfgGenEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmNewCfgGenEmail_Type.__name__ = "Integer32"
_BwmNewCfgGenEmail_Object = MibScalar
bwmNewCfgGenEmail = _BwmNewCfgGenEmail_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 12),
    _BwmNewCfgGenEmail_Type()
)
bwmNewCfgGenEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenEmail.setStatus("current")
_BwmCurCfgGenReport_Type = IpAddress
_BwmCurCfgGenReport_Object = MibScalar
bwmCurCfgGenReport = _BwmCurCfgGenReport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 13),
    _BwmCurCfgGenReport_Type()
)
bwmCurCfgGenReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenReport.setStatus("current")
_BwmNewCfgGenReport_Type = IpAddress
_BwmNewCfgGenReport_Object = MibScalar
bwmNewCfgGenReport = _BwmNewCfgGenReport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 14),
    _BwmNewCfgGenReport_Type()
)
bwmNewCfgGenReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenReport.setStatus("current")
_BwmCurCfgGenReportStr_Type = DisplayString
_BwmCurCfgGenReportStr_Object = MibScalar
bwmCurCfgGenReportStr = _BwmCurCfgGenReportStr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 15),
    _BwmCurCfgGenReportStr_Type()
)
bwmCurCfgGenReportStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgGenReportStr.setStatus("current")
_BwmNewCfgGenReportStr_Type = DisplayString
_BwmNewCfgGenReportStr_Object = MibScalar
bwmNewCfgGenReportStr = _BwmNewCfgGenReportStr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 1, 16),
    _BwmNewCfgGenReportStr_Type()
)
bwmNewCfgGenReportStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmNewCfgGenReportStr.setStatus("current")
_BwmPolicyConfig_ObjectIdentity = ObjectIdentity
bwmPolicyConfig = _BwmPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2)
)
_BwmPolicyTableMaxEnt_Type = Integer32
_BwmPolicyTableMaxEnt_Object = MibScalar
bwmPolicyTableMaxEnt = _BwmPolicyTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 1),
    _BwmPolicyTableMaxEnt_Type()
)
bwmPolicyTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmPolicyTableMaxEnt.setStatus("current")
_BwmCurCfgPolicyTable_Object = MibTable
bwmCurCfgPolicyTable = _BwmCurCfgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    bwmCurCfgPolicyTable.setStatus("current")
_BwmCurCfgPolicyTableEntry_Object = MibTableRow
bwmCurCfgPolicyTableEntry = _BwmCurCfgPolicyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 2, 1)
)
bwmCurCfgPolicyTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmCurCfgPolicyIndx"),
)
if mibBuilder.loadTexts:
    bwmCurCfgPolicyTableEntry.setStatus("current")
_BwmCurCfgPolicyIndx_Type = Integer32
_BwmCurCfgPolicyIndx_Object = MibTableColumn
bwmCurCfgPolicyIndx = _BwmCurCfgPolicyIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 2, 1, 1),
    _BwmCurCfgPolicyIndx_Type()
)
bwmCurCfgPolicyIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyIndx.setStatus("current")


class _BwmCurCfgPolicyTosIn_Type(Integer32):
    """Custom type bwmCurCfgPolicyTosIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwmCurCfgPolicyTosIn_Type.__name__ = "Integer32"
_BwmCurCfgPolicyTosIn_Object = MibTableColumn
bwmCurCfgPolicyTosIn = _BwmCurCfgPolicyTosIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 2, 1, 2),
    _BwmCurCfgPolicyTosIn_Type()
)
bwmCurCfgPolicyTosIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyTosIn.setStatus("current")


class _BwmCurCfgPolicyTosOut_Type(Integer32):
    """Custom type bwmCurCfgPolicyTosOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwmCurCfgPolicyTosOut_Type.__name__ = "Integer32"
_BwmCurCfgPolicyTosOut_Object = MibTableColumn
bwmCurCfgPolicyTosOut = _BwmCurCfgPolicyTosOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 2, 1, 3),
    _BwmCurCfgPolicyTosOut_Type()
)
bwmCurCfgPolicyTosOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyTosOut.setStatus("current")


class _BwmCurCfgPolicyHard_Type(DisplayString):
    """Custom type bwmCurCfgPolicyHard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmCurCfgPolicyHard_Type.__name__ = "DisplayString"
_BwmCurCfgPolicyHard_Object = MibTableColumn
bwmCurCfgPolicyHard = _BwmCurCfgPolicyHard_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 2, 1, 4),
    _BwmCurCfgPolicyHard_Type()
)
bwmCurCfgPolicyHard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyHard.setStatus("current")


class _BwmCurCfgPolicySoft_Type(DisplayString):
    """Custom type bwmCurCfgPolicySoft based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmCurCfgPolicySoft_Type.__name__ = "DisplayString"
_BwmCurCfgPolicySoft_Object = MibTableColumn
bwmCurCfgPolicySoft = _BwmCurCfgPolicySoft_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 2, 1, 5),
    _BwmCurCfgPolicySoft_Type()
)
bwmCurCfgPolicySoft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicySoft.setStatus("current")


class _BwmCurCfgPolicyResv_Type(DisplayString):
    """Custom type bwmCurCfgPolicyResv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmCurCfgPolicyResv_Type.__name__ = "DisplayString"
_BwmCurCfgPolicyResv_Object = MibTableColumn
bwmCurCfgPolicyResv = _BwmCurCfgPolicyResv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 2, 1, 6),
    _BwmCurCfgPolicyResv_Type()
)
bwmCurCfgPolicyResv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyResv.setStatus("current")


class _BwmCurCfgPolicyBuffer_Type(Integer32):
    """Custom type bwmCurCfgPolicyBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 128000),
    )


_BwmCurCfgPolicyBuffer_Type.__name__ = "Integer32"
_BwmCurCfgPolicyBuffer_Object = MibTableColumn
bwmCurCfgPolicyBuffer = _BwmCurCfgPolicyBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 2, 1, 7),
    _BwmCurCfgPolicyBuffer_Type()
)
bwmCurCfgPolicyBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyBuffer.setStatus("current")


class _BwmCurCfgPolicyUserLimit_Type(DisplayString):
    """Custom type bwmCurCfgPolicyUserLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmCurCfgPolicyUserLimit_Type.__name__ = "DisplayString"
_BwmCurCfgPolicyUserLimit_Object = MibTableColumn
bwmCurCfgPolicyUserLimit = _BwmCurCfgPolicyUserLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 2, 1, 8),
    _BwmCurCfgPolicyUserLimit_Type()
)
bwmCurCfgPolicyUserLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgPolicyUserLimit.setStatus("current")
_BwmNewCfgPolicyTable_Object = MibTable
bwmNewCfgPolicyTable = _BwmNewCfgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    bwmNewCfgPolicyTable.setStatus("current")
_BwmNewCfgPolicyTableEntry_Object = MibTableRow
bwmNewCfgPolicyTableEntry = _BwmNewCfgPolicyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 3, 1)
)
bwmNewCfgPolicyTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmNewCfgPolicyIndx"),
)
if mibBuilder.loadTexts:
    bwmNewCfgPolicyTableEntry.setStatus("current")
_BwmNewCfgPolicyIndx_Type = Integer32
_BwmNewCfgPolicyIndx_Object = MibTableColumn
bwmNewCfgPolicyIndx = _BwmNewCfgPolicyIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 3, 1, 1),
    _BwmNewCfgPolicyIndx_Type()
)
bwmNewCfgPolicyIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyIndx.setStatus("current")


class _BwmNewCfgPolicyTosIn_Type(Integer32):
    """Custom type bwmNewCfgPolicyTosIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwmNewCfgPolicyTosIn_Type.__name__ = "Integer32"
_BwmNewCfgPolicyTosIn_Object = MibTableColumn
bwmNewCfgPolicyTosIn = _BwmNewCfgPolicyTosIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 3, 1, 2),
    _BwmNewCfgPolicyTosIn_Type()
)
bwmNewCfgPolicyTosIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyTosIn.setStatus("current")


class _BwmNewCfgPolicyTosOut_Type(Integer32):
    """Custom type bwmNewCfgPolicyTosOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BwmNewCfgPolicyTosOut_Type.__name__ = "Integer32"
_BwmNewCfgPolicyTosOut_Object = MibTableColumn
bwmNewCfgPolicyTosOut = _BwmNewCfgPolicyTosOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 3, 1, 3),
    _BwmNewCfgPolicyTosOut_Type()
)
bwmNewCfgPolicyTosOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyTosOut.setStatus("current")


class _BwmNewCfgPolicyHard_Type(DisplayString):
    """Custom type bwmNewCfgPolicyHard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmNewCfgPolicyHard_Type.__name__ = "DisplayString"
_BwmNewCfgPolicyHard_Object = MibTableColumn
bwmNewCfgPolicyHard = _BwmNewCfgPolicyHard_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 3, 1, 4),
    _BwmNewCfgPolicyHard_Type()
)
bwmNewCfgPolicyHard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyHard.setStatus("current")


class _BwmNewCfgPolicySoft_Type(DisplayString):
    """Custom type bwmNewCfgPolicySoft based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmNewCfgPolicySoft_Type.__name__ = "DisplayString"
_BwmNewCfgPolicySoft_Object = MibTableColumn
bwmNewCfgPolicySoft = _BwmNewCfgPolicySoft_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 3, 1, 5),
    _BwmNewCfgPolicySoft_Type()
)
bwmNewCfgPolicySoft.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgPolicySoft.setStatus("current")


class _BwmNewCfgPolicyResv_Type(DisplayString):
    """Custom type bwmNewCfgPolicyResv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmNewCfgPolicyResv_Type.__name__ = "DisplayString"
_BwmNewCfgPolicyResv_Object = MibTableColumn
bwmNewCfgPolicyResv = _BwmNewCfgPolicyResv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 3, 1, 6),
    _BwmNewCfgPolicyResv_Type()
)
bwmNewCfgPolicyResv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyResv.setStatus("current")


class _BwmNewCfgPolicyBuffer_Type(Integer32):
    """Custom type bwmNewCfgPolicyBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 128000),
    )


_BwmNewCfgPolicyBuffer_Type.__name__ = "Integer32"
_BwmNewCfgPolicyBuffer_Object = MibTableColumn
bwmNewCfgPolicyBuffer = _BwmNewCfgPolicyBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 3, 1, 7),
    _BwmNewCfgPolicyBuffer_Type()
)
bwmNewCfgPolicyBuffer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyBuffer.setStatus("current")


class _BwmNewCfgPolicyDelete_Type(Integer32):
    """Custom type bwmNewCfgPolicyDelete based on Integer32"""
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


_BwmNewCfgPolicyDelete_Type.__name__ = "Integer32"
_BwmNewCfgPolicyDelete_Object = MibTableColumn
bwmNewCfgPolicyDelete = _BwmNewCfgPolicyDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 3, 1, 8),
    _BwmNewCfgPolicyDelete_Type()
)
bwmNewCfgPolicyDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyDelete.setStatus("current")


class _BwmNewCfgPolicyUserLimit_Type(DisplayString):
    """Custom type bwmNewCfgPolicyUserLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_BwmNewCfgPolicyUserLimit_Type.__name__ = "DisplayString"
_BwmNewCfgPolicyUserLimit_Object = MibTableColumn
bwmNewCfgPolicyUserLimit = _BwmNewCfgPolicyUserLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 2, 3, 1, 9),
    _BwmNewCfgPolicyUserLimit_Type()
)
bwmNewCfgPolicyUserLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgPolicyUserLimit.setStatus("current")
_BwmContractConfig_ObjectIdentity = ObjectIdentity
bwmContractConfig = _BwmContractConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3)
)
_BwmContractTableMaxEnt_Type = Integer32
_BwmContractTableMaxEnt_Object = MibScalar
bwmContractTableMaxEnt = _BwmContractTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 1),
    _BwmContractTableMaxEnt_Type()
)
bwmContractTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmContractTableMaxEnt.setStatus("current")
_BwmCurCfgContractTable_Object = MibTable
bwmCurCfgContractTable = _BwmCurCfgContractTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    bwmCurCfgContractTable.setStatus("current")
_BwmCurCfgContractTableEntry_Object = MibTableRow
bwmCurCfgContractTableEntry = _BwmCurCfgContractTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1)
)
bwmCurCfgContractTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmCurCfgContractIndx"),
)
if mibBuilder.loadTexts:
    bwmCurCfgContractTableEntry.setStatus("current")
_BwmCurCfgContractIndx_Type = Integer32
_BwmCurCfgContractIndx_Object = MibTableColumn
bwmCurCfgContractIndx = _BwmCurCfgContractIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 1),
    _BwmCurCfgContractIndx_Type()
)
bwmCurCfgContractIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractIndx.setStatus("current")


class _BwmCurCfgContractName_Type(DisplayString):
    """Custom type bwmCurCfgContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BwmCurCfgContractName_Type.__name__ = "DisplayString"
_BwmCurCfgContractName_Object = MibTableColumn
bwmCurCfgContractName = _BwmCurCfgContractName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 2),
    _BwmCurCfgContractName_Type()
)
bwmCurCfgContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractName.setStatus("current")


class _BwmCurCfgContractState_Type(Integer32):
    """Custom type bwmCurCfgContractState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmCurCfgContractState_Type.__name__ = "Integer32"
_BwmCurCfgContractState_Object = MibTableColumn
bwmCurCfgContractState = _BwmCurCfgContractState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 3),
    _BwmCurCfgContractState_Type()
)
bwmCurCfgContractState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractState.setStatus("current")
_BwmCurCfgContractPolicy_Type = Integer32
_BwmCurCfgContractPolicy_Object = MibTableColumn
bwmCurCfgContractPolicy = _BwmCurCfgContractPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 4),
    _BwmCurCfgContractPolicy_Type()
)
bwmCurCfgContractPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractPolicy.setStatus("current")


class _BwmCurCfgContractPrec_Type(Integer32):
    """Custom type bwmCurCfgContractPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BwmCurCfgContractPrec_Type.__name__ = "Integer32"
_BwmCurCfgContractPrec_Object = MibTableColumn
bwmCurCfgContractPrec = _BwmCurCfgContractPrec_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 5),
    _BwmCurCfgContractPrec_Type()
)
bwmCurCfgContractPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractPrec.setStatus("current")


class _BwmCurCfgContractUseTos_Type(Integer32):
    """Custom type bwmCurCfgContractUseTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmCurCfgContractUseTos_Type.__name__ = "Integer32"
_BwmCurCfgContractUseTos_Object = MibTableColumn
bwmCurCfgContractUseTos = _BwmCurCfgContractUseTos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 6),
    _BwmCurCfgContractUseTos_Type()
)
bwmCurCfgContractUseTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractUseTos.setStatus("current")


class _BwmCurCfgContractHistory_Type(Integer32):
    """Custom type bwmCurCfgContractHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmCurCfgContractHistory_Type.__name__ = "Integer32"
_BwmCurCfgContractHistory_Object = MibTableColumn
bwmCurCfgContractHistory = _BwmCurCfgContractHistory_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 7),
    _BwmCurCfgContractHistory_Type()
)
bwmCurCfgContractHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractHistory.setStatus("current")


class _BwmCurCfgContractShaping_Type(Integer32):
    """Custom type bwmCurCfgContractShaping based on Integer32"""
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


_BwmCurCfgContractShaping_Type.__name__ = "Integer32"
_BwmCurCfgContractShaping_Object = MibTableColumn
bwmCurCfgContractShaping = _BwmCurCfgContractShaping_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 8),
    _BwmCurCfgContractShaping_Type()
)
bwmCurCfgContractShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractShaping.setStatus("current")


class _BwmCurCfgContractResizeTcp_Type(Integer32):
    """Custom type bwmCurCfgContractResizeTcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmCurCfgContractResizeTcp_Type.__name__ = "Integer32"
_BwmCurCfgContractResizeTcp_Object = MibTableColumn
bwmCurCfgContractResizeTcp = _BwmCurCfgContractResizeTcp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 9),
    _BwmCurCfgContractResizeTcp_Type()
)
bwmCurCfgContractResizeTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractResizeTcp.setStatus("current")


class _BwmCurCfgContractIpLimit_Type(Integer32):
    """Custom type bwmCurCfgContractIpLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmCurCfgContractIpLimit_Type.__name__ = "Integer32"
_BwmCurCfgContractIpLimit_Object = MibTableColumn
bwmCurCfgContractIpLimit = _BwmCurCfgContractIpLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 10),
    _BwmCurCfgContractIpLimit_Type()
)
bwmCurCfgContractIpLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractIpLimit.setStatus("current")


class _BwmCurCfgContractIpType_Type(Integer32):
    """Custom type bwmCurCfgContractIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dip", 2),
          ("sip", 1))
    )


_BwmCurCfgContractIpType_Type.__name__ = "Integer32"
_BwmCurCfgContractIpType_Object = MibTableColumn
bwmCurCfgContractIpType = _BwmCurCfgContractIpType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 11),
    _BwmCurCfgContractIpType_Type()
)
bwmCurCfgContractIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractIpType.setStatus("current")


class _BwmCurCfgContractMonitorMode_Type(Integer32):
    """Custom type bwmCurCfgContractMonitorMode based on Integer32"""
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


_BwmCurCfgContractMonitorMode_Type.__name__ = "Integer32"
_BwmCurCfgContractMonitorMode_Object = MibTableColumn
bwmCurCfgContractMonitorMode = _BwmCurCfgContractMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 12),
    _BwmCurCfgContractMonitorMode_Type()
)
bwmCurCfgContractMonitorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractMonitorMode.setStatus("current")
_BwmCurCfgContractGroup_Type = Integer32
_BwmCurCfgContractGroup_Object = MibTableColumn
bwmCurCfgContractGroup = _BwmCurCfgContractGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 13),
    _BwmCurCfgContractGroup_Type()
)
bwmCurCfgContractGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractGroup.setStatus("current")


class _BwmCurCfgContractMaxSess_Type(Integer32):
    """Custom type bwmCurCfgContractMaxSess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_BwmCurCfgContractMaxSess_Type.__name__ = "Integer32"
_BwmCurCfgContractMaxSess_Object = MibTableColumn
bwmCurCfgContractMaxSess = _BwmCurCfgContractMaxSess_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 15),
    _BwmCurCfgContractMaxSess_Type()
)
bwmCurCfgContractMaxSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractMaxSess.setStatus("current")


class _BwmCurCfgContractRowType_Type(Integer32):
    """Custom type bwmCurCfgContractRowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("reserved", 2))
    )


_BwmCurCfgContractRowType_Type.__name__ = "Integer32"
_BwmCurCfgContractRowType_Object = MibTableColumn
bwmCurCfgContractRowType = _BwmCurCfgContractRowType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 2, 1, 16),
    _BwmCurCfgContractRowType_Type()
)
bwmCurCfgContractRowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractRowType.setStatus("current")
_BwmNewCfgContractTable_Object = MibTable
bwmNewCfgContractTable = _BwmNewCfgContractTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3)
)
if mibBuilder.loadTexts:
    bwmNewCfgContractTable.setStatus("current")
_BwmNewCfgContractTableEntry_Object = MibTableRow
bwmNewCfgContractTableEntry = _BwmNewCfgContractTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1)
)
bwmNewCfgContractTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmNewCfgContractIndx"),
)
if mibBuilder.loadTexts:
    bwmNewCfgContractTableEntry.setStatus("current")
_BwmNewCfgContractIndx_Type = Integer32
_BwmNewCfgContractIndx_Object = MibTableColumn
bwmNewCfgContractIndx = _BwmNewCfgContractIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 1),
    _BwmNewCfgContractIndx_Type()
)
bwmNewCfgContractIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmNewCfgContractIndx.setStatus("current")


class _BwmNewCfgContractName_Type(DisplayString):
    """Custom type bwmNewCfgContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BwmNewCfgContractName_Type.__name__ = "DisplayString"
_BwmNewCfgContractName_Object = MibTableColumn
bwmNewCfgContractName = _BwmNewCfgContractName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 2),
    _BwmNewCfgContractName_Type()
)
bwmNewCfgContractName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractName.setStatus("current")


class _BwmNewCfgContractState_Type(Integer32):
    """Custom type bwmNewCfgContractState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmNewCfgContractState_Type.__name__ = "Integer32"
_BwmNewCfgContractState_Object = MibTableColumn
bwmNewCfgContractState = _BwmNewCfgContractState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 3),
    _BwmNewCfgContractState_Type()
)
bwmNewCfgContractState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractState.setStatus("current")
_BwmNewCfgContractPolicy_Type = Integer32
_BwmNewCfgContractPolicy_Object = MibTableColumn
bwmNewCfgContractPolicy = _BwmNewCfgContractPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 4),
    _BwmNewCfgContractPolicy_Type()
)
bwmNewCfgContractPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractPolicy.setStatus("current")


class _BwmNewCfgContractDelete_Type(Integer32):
    """Custom type bwmNewCfgContractDelete based on Integer32"""
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


_BwmNewCfgContractDelete_Type.__name__ = "Integer32"
_BwmNewCfgContractDelete_Object = MibTableColumn
bwmNewCfgContractDelete = _BwmNewCfgContractDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 5),
    _BwmNewCfgContractDelete_Type()
)
bwmNewCfgContractDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractDelete.setStatus("current")


class _BwmNewCfgContractPrec_Type(Integer32):
    """Custom type bwmNewCfgContractPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BwmNewCfgContractPrec_Type.__name__ = "Integer32"
_BwmNewCfgContractPrec_Object = MibTableColumn
bwmNewCfgContractPrec = _BwmNewCfgContractPrec_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 6),
    _BwmNewCfgContractPrec_Type()
)
bwmNewCfgContractPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractPrec.setStatus("current")


class _BwmNewCfgContractUseTos_Type(Integer32):
    """Custom type bwmNewCfgContractUseTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmNewCfgContractUseTos_Type.__name__ = "Integer32"
_BwmNewCfgContractUseTos_Object = MibTableColumn
bwmNewCfgContractUseTos = _BwmNewCfgContractUseTos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 7),
    _BwmNewCfgContractUseTos_Type()
)
bwmNewCfgContractUseTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractUseTos.setStatus("current")


class _BwmNewCfgContractHistory_Type(Integer32):
    """Custom type bwmNewCfgContractHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmNewCfgContractHistory_Type.__name__ = "Integer32"
_BwmNewCfgContractHistory_Object = MibTableColumn
bwmNewCfgContractHistory = _BwmNewCfgContractHistory_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 8),
    _BwmNewCfgContractHistory_Type()
)
bwmNewCfgContractHistory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractHistory.setStatus("current")


class _BwmNewCfgContractShaping_Type(Integer32):
    """Custom type bwmNewCfgContractShaping based on Integer32"""
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


_BwmNewCfgContractShaping_Type.__name__ = "Integer32"
_BwmNewCfgContractShaping_Object = MibTableColumn
bwmNewCfgContractShaping = _BwmNewCfgContractShaping_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 9),
    _BwmNewCfgContractShaping_Type()
)
bwmNewCfgContractShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractShaping.setStatus("current")


class _BwmNewCfgContractResizeTcp_Type(Integer32):
    """Custom type bwmNewCfgContractResizeTcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmNewCfgContractResizeTcp_Type.__name__ = "Integer32"
_BwmNewCfgContractResizeTcp_Object = MibTableColumn
bwmNewCfgContractResizeTcp = _BwmNewCfgContractResizeTcp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 10),
    _BwmNewCfgContractResizeTcp_Type()
)
bwmNewCfgContractResizeTcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractResizeTcp.setStatus("current")


class _BwmNewCfgContractIpLimit_Type(Integer32):
    """Custom type bwmNewCfgContractIpLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_BwmNewCfgContractIpLimit_Type.__name__ = "Integer32"
_BwmNewCfgContractIpLimit_Object = MibTableColumn
bwmNewCfgContractIpLimit = _BwmNewCfgContractIpLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 11),
    _BwmNewCfgContractIpLimit_Type()
)
bwmNewCfgContractIpLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractIpLimit.setStatus("current")


class _BwmNewCfgContractIpType_Type(Integer32):
    """Custom type bwmNewCfgContractIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dip", 2),
          ("sip", 1))
    )


_BwmNewCfgContractIpType_Type.__name__ = "Integer32"
_BwmNewCfgContractIpType_Object = MibTableColumn
bwmNewCfgContractIpType = _BwmNewCfgContractIpType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 12),
    _BwmNewCfgContractIpType_Type()
)
bwmNewCfgContractIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractIpType.setStatus("current")


class _BwmNewCfgContractMonitorMode_Type(Integer32):
    """Custom type bwmNewCfgContractMonitorMode based on Integer32"""
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


_BwmNewCfgContractMonitorMode_Type.__name__ = "Integer32"
_BwmNewCfgContractMonitorMode_Object = MibTableColumn
bwmNewCfgContractMonitorMode = _BwmNewCfgContractMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 13),
    _BwmNewCfgContractMonitorMode_Type()
)
bwmNewCfgContractMonitorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractMonitorMode.setStatus("current")
_BwmNewCfgContractGroup_Type = Integer32
_BwmNewCfgContractGroup_Object = MibTableColumn
bwmNewCfgContractGroup = _BwmNewCfgContractGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 14),
    _BwmNewCfgContractGroup_Type()
)
bwmNewCfgContractGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmNewCfgContractGroup.setStatus("current")


class _BwmNewCfgContractMaxSess_Type(Integer32):
    """Custom type bwmNewCfgContractMaxSess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_BwmNewCfgContractMaxSess_Type.__name__ = "Integer32"
_BwmNewCfgContractMaxSess_Object = MibTableColumn
bwmNewCfgContractMaxSess = _BwmNewCfgContractMaxSess_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 16),
    _BwmNewCfgContractMaxSess_Type()
)
bwmNewCfgContractMaxSess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractMaxSess.setStatus("current")


class _BwmNewCfgContractRowType_Type(Integer32):
    """Custom type bwmNewCfgContractRowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("reserved", 2))
    )


_BwmNewCfgContractRowType_Type.__name__ = "Integer32"
_BwmNewCfgContractRowType_Object = MibTableColumn
bwmNewCfgContractRowType = _BwmNewCfgContractRowType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 3, 1, 17),
    _BwmNewCfgContractRowType_Type()
)
bwmNewCfgContractRowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmNewCfgContractRowType.setStatus("current")
_BwmAvailableContractsTable_Object = MibTable
bwmAvailableContractsTable = _BwmAvailableContractsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 4)
)
if mibBuilder.loadTexts:
    bwmAvailableContractsTable.setStatus("current")
_BwmAvailableContractsTableEntry_Object = MibTableRow
bwmAvailableContractsTableEntry = _BwmAvailableContractsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 4, 1)
)
bwmAvailableContractsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmContractIndx"),
)
if mibBuilder.loadTexts:
    bwmAvailableContractsTableEntry.setStatus("current")
_BwmContractIndx_Type = Integer32
_BwmContractIndx_Object = MibTableColumn
bwmContractIndx = _BwmContractIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 4, 1, 1),
    _BwmContractIndx_Type()
)
bwmContractIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmContractIndx.setStatus("current")


class _BwmContractName_Type(DisplayString):
    """Custom type bwmContractName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BwmContractName_Type.__name__ = "DisplayString"
_BwmContractName_Object = MibTableColumn
bwmContractName = _BwmContractName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 3, 4, 1, 2),
    _BwmContractName_Type()
)
bwmContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmContractName.setStatus("current")
_BwmContTimePolicyConfig_ObjectIdentity = ObjectIdentity
bwmContTimePolicyConfig = _BwmContTimePolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4)
)
_BwmContTimePolicyTableMaxEnt_Type = Integer32
_BwmContTimePolicyTableMaxEnt_Object = MibScalar
bwmContTimePolicyTableMaxEnt = _BwmContTimePolicyTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 1),
    _BwmContTimePolicyTableMaxEnt_Type()
)
bwmContTimePolicyTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmContTimePolicyTableMaxEnt.setStatus("current")
_BwmCurCfgContTimePolicyTable_Object = MibTable
bwmCurCfgContTimePolicyTable = _BwmCurCfgContTimePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    bwmCurCfgContTimePolicyTable.setStatus("current")
_BwmCurCfgContTimePolicyTableEntry_Object = MibTableRow
bwmCurCfgContTimePolicyTableEntry = _BwmCurCfgContTimePolicyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 2, 1)
)
bwmCurCfgContTimePolicyTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmCurCfgContTimePolicyContIndx"),
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmCurCfgContTimePolicyIndx"),
)
if mibBuilder.loadTexts:
    bwmCurCfgContTimePolicyTableEntry.setStatus("current")
_BwmCurCfgContTimePolicyContIndx_Type = Integer32
_BwmCurCfgContTimePolicyContIndx_Object = MibTableColumn
bwmCurCfgContTimePolicyContIndx = _BwmCurCfgContTimePolicyContIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 2, 1, 1),
    _BwmCurCfgContTimePolicyContIndx_Type()
)
bwmCurCfgContTimePolicyContIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContTimePolicyContIndx.setStatus("current")
_BwmCurCfgContTimePolicyIndx_Type = Integer32
_BwmCurCfgContTimePolicyIndx_Object = MibTableColumn
bwmCurCfgContTimePolicyIndx = _BwmCurCfgContTimePolicyIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 2, 1, 2),
    _BwmCurCfgContTimePolicyIndx_Type()
)
bwmCurCfgContTimePolicyIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContTimePolicyIndx.setStatus("current")


class _BwmCurCfgContTimePolicyDay_Type(Integer32):
    """Custom type bwmCurCfgContTimePolicyDay based on Integer32"""
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
        *(("everyday", 10),
          ("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4),
          ("weekday", 8),
          ("weekend", 9))
    )


_BwmCurCfgContTimePolicyDay_Type.__name__ = "Integer32"
_BwmCurCfgContTimePolicyDay_Object = MibTableColumn
bwmCurCfgContTimePolicyDay = _BwmCurCfgContTimePolicyDay_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 2, 1, 3),
    _BwmCurCfgContTimePolicyDay_Type()
)
bwmCurCfgContTimePolicyDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContTimePolicyDay.setStatus("current")


class _BwmCurCfgContTimePolicyFrom_Type(Integer32):
    """Custom type bwmCurCfgContTimePolicyFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_BwmCurCfgContTimePolicyFrom_Type.__name__ = "Integer32"
_BwmCurCfgContTimePolicyFrom_Object = MibTableColumn
bwmCurCfgContTimePolicyFrom = _BwmCurCfgContTimePolicyFrom_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 2, 1, 4),
    _BwmCurCfgContTimePolicyFrom_Type()
)
bwmCurCfgContTimePolicyFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContTimePolicyFrom.setStatus("current")


class _BwmCurCfgContTimePolicyTo_Type(Integer32):
    """Custom type bwmCurCfgContTimePolicyTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_BwmCurCfgContTimePolicyTo_Type.__name__ = "Integer32"
_BwmCurCfgContTimePolicyTo_Object = MibTableColumn
bwmCurCfgContTimePolicyTo = _BwmCurCfgContTimePolicyTo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 2, 1, 5),
    _BwmCurCfgContTimePolicyTo_Type()
)
bwmCurCfgContTimePolicyTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContTimePolicyTo.setStatus("current")
_BwmCurCfgContTimePolicyPol_Type = Integer32
_BwmCurCfgContTimePolicyPol_Object = MibTableColumn
bwmCurCfgContTimePolicyPol = _BwmCurCfgContTimePolicyPol_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 2, 1, 6),
    _BwmCurCfgContTimePolicyPol_Type()
)
bwmCurCfgContTimePolicyPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContTimePolicyPol.setStatus("current")


class _BwmCurCfgContTimePolicyState_Type(Integer32):
    """Custom type bwmCurCfgContTimePolicyState based on Integer32"""
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


_BwmCurCfgContTimePolicyState_Type.__name__ = "Integer32"
_BwmCurCfgContTimePolicyState_Object = MibTableColumn
bwmCurCfgContTimePolicyState = _BwmCurCfgContTimePolicyState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 2, 1, 7),
    _BwmCurCfgContTimePolicyState_Type()
)
bwmCurCfgContTimePolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContTimePolicyState.setStatus("current")
_BwmNewCfgContTimePolicyTable_Object = MibTable
bwmNewCfgContTimePolicyTable = _BwmNewCfgContTimePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 3)
)
if mibBuilder.loadTexts:
    bwmNewCfgContTimePolicyTable.setStatus("current")
_BwmNewCfgContTimePolicyTableEntry_Object = MibTableRow
bwmNewCfgContTimePolicyTableEntry = _BwmNewCfgContTimePolicyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 3, 1)
)
bwmNewCfgContTimePolicyTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmNewCfgContTimePolicyContIndx"),
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmNewCfgContTimePolicyIndx"),
)
if mibBuilder.loadTexts:
    bwmNewCfgContTimePolicyTableEntry.setStatus("current")
_BwmNewCfgContTimePolicyContIndx_Type = Integer32
_BwmNewCfgContTimePolicyContIndx_Object = MibTableColumn
bwmNewCfgContTimePolicyContIndx = _BwmNewCfgContTimePolicyContIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 3, 1, 1),
    _BwmNewCfgContTimePolicyContIndx_Type()
)
bwmNewCfgContTimePolicyContIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmNewCfgContTimePolicyContIndx.setStatus("current")
_BwmNewCfgContTimePolicyIndx_Type = Integer32
_BwmNewCfgContTimePolicyIndx_Object = MibTableColumn
bwmNewCfgContTimePolicyIndx = _BwmNewCfgContTimePolicyIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 3, 1, 2),
    _BwmNewCfgContTimePolicyIndx_Type()
)
bwmNewCfgContTimePolicyIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmNewCfgContTimePolicyIndx.setStatus("current")


class _BwmNewCfgContTimePolicyDay_Type(Integer32):
    """Custom type bwmNewCfgContTimePolicyDay based on Integer32"""
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
        *(("everyday", 10),
          ("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4),
          ("weekday", 8),
          ("weekend", 9))
    )


_BwmNewCfgContTimePolicyDay_Type.__name__ = "Integer32"
_BwmNewCfgContTimePolicyDay_Object = MibTableColumn
bwmNewCfgContTimePolicyDay = _BwmNewCfgContTimePolicyDay_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 3, 1, 3),
    _BwmNewCfgContTimePolicyDay_Type()
)
bwmNewCfgContTimePolicyDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContTimePolicyDay.setStatus("current")


class _BwmNewCfgContTimePolicyFrom_Type(Integer32):
    """Custom type bwmNewCfgContTimePolicyFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_BwmNewCfgContTimePolicyFrom_Type.__name__ = "Integer32"
_BwmNewCfgContTimePolicyFrom_Object = MibTableColumn
bwmNewCfgContTimePolicyFrom = _BwmNewCfgContTimePolicyFrom_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 3, 1, 4),
    _BwmNewCfgContTimePolicyFrom_Type()
)
bwmNewCfgContTimePolicyFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContTimePolicyFrom.setStatus("current")


class _BwmNewCfgContTimePolicyTo_Type(Integer32):
    """Custom type bwmNewCfgContTimePolicyTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_BwmNewCfgContTimePolicyTo_Type.__name__ = "Integer32"
_BwmNewCfgContTimePolicyTo_Object = MibTableColumn
bwmNewCfgContTimePolicyTo = _BwmNewCfgContTimePolicyTo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 3, 1, 5),
    _BwmNewCfgContTimePolicyTo_Type()
)
bwmNewCfgContTimePolicyTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContTimePolicyTo.setStatus("current")
_BwmNewCfgContTimePolicyPol_Type = Integer32
_BwmNewCfgContTimePolicyPol_Object = MibTableColumn
bwmNewCfgContTimePolicyPol = _BwmNewCfgContTimePolicyPol_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 3, 1, 6),
    _BwmNewCfgContTimePolicyPol_Type()
)
bwmNewCfgContTimePolicyPol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContTimePolicyPol.setStatus("current")


class _BwmNewCfgContTimePolicyState_Type(Integer32):
    """Custom type bwmNewCfgContTimePolicyState based on Integer32"""
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


_BwmNewCfgContTimePolicyState_Type.__name__ = "Integer32"
_BwmNewCfgContTimePolicyState_Object = MibTableColumn
bwmNewCfgContTimePolicyState = _BwmNewCfgContTimePolicyState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 3, 1, 7),
    _BwmNewCfgContTimePolicyState_Type()
)
bwmNewCfgContTimePolicyState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContTimePolicyState.setStatus("current")


class _BwmNewCfgContTimePolicyDelete_Type(Integer32):
    """Custom type bwmNewCfgContTimePolicyDelete based on Integer32"""
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


_BwmNewCfgContTimePolicyDelete_Type.__name__ = "Integer32"
_BwmNewCfgContTimePolicyDelete_Object = MibTableColumn
bwmNewCfgContTimePolicyDelete = _BwmNewCfgContTimePolicyDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 4, 3, 1, 8),
    _BwmNewCfgContTimePolicyDelete_Type()
)
bwmNewCfgContTimePolicyDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContTimePolicyDelete.setStatus("current")
_BwmContractGroupConfig_ObjectIdentity = ObjectIdentity
bwmContractGroupConfig = _BwmContractGroupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5)
)
_BwmContractGroupTableMaxEnt_Type = Integer32
_BwmContractGroupTableMaxEnt_Object = MibScalar
bwmContractGroupTableMaxEnt = _BwmContractGroupTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 1),
    _BwmContractGroupTableMaxEnt_Type()
)
bwmContractGroupTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmContractGroupTableMaxEnt.setStatus("current")
_BwmCurCfgContractGroupTable_Object = MibTable
bwmCurCfgContractGroupTable = _BwmCurCfgContractGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 2)
)
if mibBuilder.loadTexts:
    bwmCurCfgContractGroupTable.setStatus("current")
_BwmCurCfgContractGroupTableEntry_Object = MibTableRow
bwmCurCfgContractGroupTableEntry = _BwmCurCfgContractGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 2, 1)
)
bwmCurCfgContractGroupTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmCurCfgContractGroupIndx"),
)
if mibBuilder.loadTexts:
    bwmCurCfgContractGroupTableEntry.setStatus("current")
_BwmCurCfgContractGroupIndx_Type = Integer32
_BwmCurCfgContractGroupIndx_Object = MibTableColumn
bwmCurCfgContractGroupIndx = _BwmCurCfgContractGroupIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 2, 1, 1),
    _BwmCurCfgContractGroupIndx_Type()
)
bwmCurCfgContractGroupIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractGroupIndx.setStatus("current")
_BwmCurCfgContractGroupContracts_Type = OctetString
_BwmCurCfgContractGroupContracts_Object = MibTableColumn
bwmCurCfgContractGroupContracts = _BwmCurCfgContractGroupContracts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 2, 1, 2),
    _BwmCurCfgContractGroupContracts_Type()
)
bwmCurCfgContractGroupContracts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractGroupContracts.setStatus("current")


class _BwmCurCfgContractGroupName_Type(DisplayString):
    """Custom type bwmCurCfgContractGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BwmCurCfgContractGroupName_Type.__name__ = "DisplayString"
_BwmCurCfgContractGroupName_Object = MibTableColumn
bwmCurCfgContractGroupName = _BwmCurCfgContractGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 2, 1, 3),
    _BwmCurCfgContractGroupName_Type()
)
bwmCurCfgContractGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmCurCfgContractGroupName.setStatus("current")
_BwmNewCfgContractGroupTable_Object = MibTable
bwmNewCfgContractGroupTable = _BwmNewCfgContractGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 3)
)
if mibBuilder.loadTexts:
    bwmNewCfgContractGroupTable.setStatus("current")
_BwmNewCfgContractGroupTableEntry_Object = MibTableRow
bwmNewCfgContractGroupTableEntry = _BwmNewCfgContractGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 3, 1)
)
bwmNewCfgContractGroupTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmNewCfgContractGroupIndx"),
)
if mibBuilder.loadTexts:
    bwmNewCfgContractGroupTableEntry.setStatus("current")
_BwmNewCfgContractGroupIndx_Type = Integer32
_BwmNewCfgContractGroupIndx_Object = MibTableColumn
bwmNewCfgContractGroupIndx = _BwmNewCfgContractGroupIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 3, 1, 1),
    _BwmNewCfgContractGroupIndx_Type()
)
bwmNewCfgContractGroupIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmNewCfgContractGroupIndx.setStatus("current")
_BwmNewCfgContractGroupContracts_Type = OctetString
_BwmNewCfgContractGroupContracts_Object = MibTableColumn
bwmNewCfgContractGroupContracts = _BwmNewCfgContractGroupContracts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 3, 1, 2),
    _BwmNewCfgContractGroupContracts_Type()
)
bwmNewCfgContractGroupContracts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmNewCfgContractGroupContracts.setStatus("current")
_BwmNewCfgContractGroupAddCont_Type = Integer32
_BwmNewCfgContractGroupAddCont_Object = MibTableColumn
bwmNewCfgContractGroupAddCont = _BwmNewCfgContractGroupAddCont_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 3, 1, 3),
    _BwmNewCfgContractGroupAddCont_Type()
)
bwmNewCfgContractGroupAddCont.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractGroupAddCont.setStatus("current")
_BwmNewCfgContractGroupRemCont_Type = Integer32
_BwmNewCfgContractGroupRemCont_Object = MibTableColumn
bwmNewCfgContractGroupRemCont = _BwmNewCfgContractGroupRemCont_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 3, 1, 4),
    _BwmNewCfgContractGroupRemCont_Type()
)
bwmNewCfgContractGroupRemCont.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractGroupRemCont.setStatus("current")


class _BwmNewCfgContractGroupDelete_Type(Integer32):
    """Custom type bwmNewCfgContractGroupDelete based on Integer32"""
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


_BwmNewCfgContractGroupDelete_Type.__name__ = "Integer32"
_BwmNewCfgContractGroupDelete_Object = MibTableColumn
bwmNewCfgContractGroupDelete = _BwmNewCfgContractGroupDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 3, 1, 5),
    _BwmNewCfgContractGroupDelete_Type()
)
bwmNewCfgContractGroupDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractGroupDelete.setStatus("current")


class _BwmNewCfgContractGroupName_Type(DisplayString):
    """Custom type bwmNewCfgContractGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BwmNewCfgContractGroupName_Type.__name__ = "DisplayString"
_BwmNewCfgContractGroupName_Object = MibTableColumn
bwmNewCfgContractGroupName = _BwmNewCfgContractGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 3, 1, 6),
    _BwmNewCfgContractGroupName_Type()
)
bwmNewCfgContractGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bwmNewCfgContractGroupName.setStatus("current")
_BwmContractGroupTableMaxCont_Type = Integer32
_BwmContractGroupTableMaxCont_Object = MibScalar
bwmContractGroupTableMaxCont = _BwmContractGroupTableMaxCont_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 1, 5, 4),
    _BwmContractGroupTableMaxCont_Type()
)
bwmContractGroupTableMaxCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmContractGroupTableMaxCont.setStatus("current")
_BwmStats_ObjectIdentity = ObjectIdentity
bwmStats = _BwmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2)
)
_BwmStatTcTable_Object = MibTable
bwmStatTcTable = _BwmStatTcTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 1)
)
if mibBuilder.loadTexts:
    bwmStatTcTable.setStatus("current")
_BwmStatTcEntry_Object = MibTableRow
bwmStatTcEntry = _BwmStatTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 1, 1)
)
bwmStatTcEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmStatTcContractIndex"),
)
if mibBuilder.loadTexts:
    bwmStatTcEntry.setStatus("current")
_BwmStatTcContractIndex_Type = Integer32
_BwmStatTcContractIndex_Object = MibTableColumn
bwmStatTcContractIndex = _BwmStatTcContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 1, 1, 1),
    _BwmStatTcContractIndex_Type()
)
bwmStatTcContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcContractIndex.setStatus("current")


class _BwmStatTcName_Type(DisplayString):
    """Custom type bwmStatTcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwmStatTcName_Type.__name__ = "DisplayString"
_BwmStatTcName_Object = MibTableColumn
bwmStatTcName = _BwmStatTcName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 1, 1, 2),
    _BwmStatTcName_Type()
)
bwmStatTcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcName.setStatus("current")
_BwmStatTcOutoct_Type = Counter32
_BwmStatTcOutoct_Object = MibTableColumn
bwmStatTcOutoct = _BwmStatTcOutoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 1, 1, 3),
    _BwmStatTcOutoct_Type()
)
bwmStatTcOutoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcOutoct.setStatus("current")
_BwmStatTcOutdisoct_Type = Counter32
_BwmStatTcOutdisoct_Object = MibTableColumn
bwmStatTcOutdisoct = _BwmStatTcOutdisoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 1, 1, 4),
    _BwmStatTcOutdisoct_Type()
)
bwmStatTcOutdisoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcOutdisoct.setStatus("current")
_BwmStatTcBufferUsed_Type = Integer32
_BwmStatTcBufferUsed_Object = MibTableColumn
bwmStatTcBufferUsed = _BwmStatTcBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 1, 1, 5),
    _BwmStatTcBufferUsed_Type()
)
bwmStatTcBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcBufferUsed.setStatus("current")
_BwmStatTcBufferMax_Type = Counter32
_BwmStatTcBufferMax_Object = MibTableColumn
bwmStatTcBufferMax = _BwmStatTcBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 1, 1, 6),
    _BwmStatTcBufferMax_Type()
)
bwmStatTcBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcBufferMax.setStatus("current")
_BwmStatTcTotalPackets_Type = Counter32
_BwmStatTcTotalPackets_Object = MibTableColumn
bwmStatTcTotalPackets = _BwmStatTcTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 1, 1, 7),
    _BwmStatTcTotalPackets_Type()
)
bwmStatTcTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcTotalPackets.setStatus("current")
_BwmStatTcSessRejected_Type = Counter32
_BwmStatTcSessRejected_Object = MibTableColumn
bwmStatTcSessRejected = _BwmStatTcSessRejected_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 1, 1, 8),
    _BwmStatTcSessRejected_Type()
)
bwmStatTcSessRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcSessRejected.setStatus("current")
_BwmStatTcrTable_Object = MibTable
bwmStatTcrTable = _BwmStatTcrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 2)
)
if mibBuilder.loadTexts:
    bwmStatTcrTable.setStatus("current")
_BwmStatTcrEntry_Object = MibTableRow
bwmStatTcrEntry = _BwmStatTcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 2, 1)
)
bwmStatTcrEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmStatTcrContractIndex"),
)
if mibBuilder.loadTexts:
    bwmStatTcrEntry.setStatus("current")
_BwmStatTcrContractIndex_Type = Integer32
_BwmStatTcrContractIndex_Object = MibTableColumn
bwmStatTcrContractIndex = _BwmStatTcrContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 2, 1, 1),
    _BwmStatTcrContractIndex_Type()
)
bwmStatTcrContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrContractIndex.setStatus("current")


class _BwmStatTcrName_Type(DisplayString):
    """Custom type bwmStatTcrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwmStatTcrName_Type.__name__ = "DisplayString"
_BwmStatTcrName_Object = MibTableColumn
bwmStatTcrName = _BwmStatTcrName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 2, 1, 2),
    _BwmStatTcrName_Type()
)
bwmStatTcrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrName.setStatus("current")
_BwmStatTcrRate_Type = Integer32
_BwmStatTcrRate_Object = MibTableColumn
bwmStatTcrRate = _BwmStatTcrRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 2, 1, 3),
    _BwmStatTcrRate_Type()
)
bwmStatTcrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrRate.setStatus("current")
_BwmStatTcrOutoct_Type = Counter32
_BwmStatTcrOutoct_Object = MibTableColumn
bwmStatTcrOutoct = _BwmStatTcrOutoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 2, 1, 4),
    _BwmStatTcrOutoct_Type()
)
bwmStatTcrOutoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrOutoct.setStatus("current")
_BwmStatTcrOutdisoct_Type = Counter32
_BwmStatTcrOutdisoct_Object = MibTableColumn
bwmStatTcrOutdisoct = _BwmStatTcrOutdisoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 2, 1, 5),
    _BwmStatTcrOutdisoct_Type()
)
bwmStatTcrOutdisoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrOutdisoct.setStatus("current")
_BwmStatTcrBufferUsed_Type = Integer32
_BwmStatTcrBufferUsed_Object = MibTableColumn
bwmStatTcrBufferUsed = _BwmStatTcrBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 2, 1, 6),
    _BwmStatTcrBufferUsed_Type()
)
bwmStatTcrBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrBufferUsed.setStatus("current")
_BwmStatTcrBufferMax_Type = Counter32
_BwmStatTcrBufferMax_Object = MibTableColumn
bwmStatTcrBufferMax = _BwmStatTcrBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 2, 1, 7),
    _BwmStatTcrBufferMax_Type()
)
bwmStatTcrBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrBufferMax.setStatus("current")
_BwmStatTcrTotalPackets_Type = Counter32
_BwmStatTcrTotalPackets_Object = MibTableColumn
bwmStatTcrTotalPackets = _BwmStatTcrTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 2, 1, 8),
    _BwmStatTcrTotalPackets_Type()
)
bwmStatTcrTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatTcrTotalPackets.setStatus("current")
_BwmStatPortTcTable_Object = MibTable
bwmStatPortTcTable = _BwmStatPortTcTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 3)
)
if mibBuilder.loadTexts:
    bwmStatPortTcTable.setStatus("current")
_BwmStatPortTcEntry_Object = MibTableRow
bwmStatPortTcEntry = _BwmStatPortTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 3, 1)
)
bwmStatPortTcEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmStatPortTcPortIndex"),
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmStatPortTcContractIndex"),
)
if mibBuilder.loadTexts:
    bwmStatPortTcEntry.setStatus("current")
_BwmStatPortTcPortIndex_Type = Integer32
_BwmStatPortTcPortIndex_Object = MibTableColumn
bwmStatPortTcPortIndex = _BwmStatPortTcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 3, 1, 1),
    _BwmStatPortTcPortIndex_Type()
)
bwmStatPortTcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcPortIndex.setStatus("current")
_BwmStatPortTcContractIndex_Type = Integer32
_BwmStatPortTcContractIndex_Object = MibTableColumn
bwmStatPortTcContractIndex = _BwmStatPortTcContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 3, 1, 2),
    _BwmStatPortTcContractIndex_Type()
)
bwmStatPortTcContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcContractIndex.setStatus("current")


class _BwmStatPortTcName_Type(DisplayString):
    """Custom type bwmStatPortTcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwmStatPortTcName_Type.__name__ = "DisplayString"
_BwmStatPortTcName_Object = MibTableColumn
bwmStatPortTcName = _BwmStatPortTcName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 3, 1, 3),
    _BwmStatPortTcName_Type()
)
bwmStatPortTcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcName.setStatus("current")
_BwmStatPortTcOutoct_Type = Counter32
_BwmStatPortTcOutoct_Object = MibTableColumn
bwmStatPortTcOutoct = _BwmStatPortTcOutoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 3, 1, 4),
    _BwmStatPortTcOutoct_Type()
)
bwmStatPortTcOutoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcOutoct.setStatus("current")
_BwmStatPortTcOutdisoct_Type = Counter32
_BwmStatPortTcOutdisoct_Object = MibTableColumn
bwmStatPortTcOutdisoct = _BwmStatPortTcOutdisoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 3, 1, 5),
    _BwmStatPortTcOutdisoct_Type()
)
bwmStatPortTcOutdisoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcOutdisoct.setStatus("current")
_BwmStatPortTcBufferUsed_Type = Integer32
_BwmStatPortTcBufferUsed_Object = MibTableColumn
bwmStatPortTcBufferUsed = _BwmStatPortTcBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 3, 1, 6),
    _BwmStatPortTcBufferUsed_Type()
)
bwmStatPortTcBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcBufferUsed.setStatus("current")
_BwmStatPortTcBufferMax_Type = Counter32
_BwmStatPortTcBufferMax_Object = MibTableColumn
bwmStatPortTcBufferMax = _BwmStatPortTcBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 3, 1, 7),
    _BwmStatPortTcBufferMax_Type()
)
bwmStatPortTcBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcBufferMax.setStatus("current")
_BwmStatPortTcTotalPackets_Type = Counter32
_BwmStatPortTcTotalPackets_Object = MibTableColumn
bwmStatPortTcTotalPackets = _BwmStatPortTcTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 3, 1, 8),
    _BwmStatPortTcTotalPackets_Type()
)
bwmStatPortTcTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcTotalPackets.setStatus("current")
_BwmStatPortTcrTable_Object = MibTable
bwmStatPortTcrTable = _BwmStatPortTcrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 4)
)
if mibBuilder.loadTexts:
    bwmStatPortTcrTable.setStatus("current")
_BwmStatPortTcrEntry_Object = MibTableRow
bwmStatPortTcrEntry = _BwmStatPortTcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 4, 1)
)
bwmStatPortTcrEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmStatPortTcrPortIndex"),
    (0, "ALTEON-CHEETAH-BWM-MIB", "bwmStatPortTcrContractIndex"),
)
if mibBuilder.loadTexts:
    bwmStatPortTcrEntry.setStatus("current")
_BwmStatPortTcrPortIndex_Type = Integer32
_BwmStatPortTcrPortIndex_Object = MibTableColumn
bwmStatPortTcrPortIndex = _BwmStatPortTcrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 4, 1, 1),
    _BwmStatPortTcrPortIndex_Type()
)
bwmStatPortTcrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcrPortIndex.setStatus("current")
_BwmStatPortTcrContractIndex_Type = Integer32
_BwmStatPortTcrContractIndex_Object = MibTableColumn
bwmStatPortTcrContractIndex = _BwmStatPortTcrContractIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 4, 1, 2),
    _BwmStatPortTcrContractIndex_Type()
)
bwmStatPortTcrContractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcrContractIndex.setStatus("current")


class _BwmStatPortTcrName_Type(DisplayString):
    """Custom type bwmStatPortTcrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BwmStatPortTcrName_Type.__name__ = "DisplayString"
_BwmStatPortTcrName_Object = MibTableColumn
bwmStatPortTcrName = _BwmStatPortTcrName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 4, 1, 3),
    _BwmStatPortTcrName_Type()
)
bwmStatPortTcrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcrName.setStatus("current")
_BwmStatPortTcrRate_Type = Integer32
_BwmStatPortTcrRate_Object = MibTableColumn
bwmStatPortTcrRate = _BwmStatPortTcrRate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 4, 1, 4),
    _BwmStatPortTcrRate_Type()
)
bwmStatPortTcrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcrRate.setStatus("current")
_BwmStatPortTcrOutoct_Type = Counter32
_BwmStatPortTcrOutoct_Object = MibTableColumn
bwmStatPortTcrOutoct = _BwmStatPortTcrOutoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 4, 1, 5),
    _BwmStatPortTcrOutoct_Type()
)
bwmStatPortTcrOutoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcrOutoct.setStatus("current")
_BwmStatPortTcrOutdisoct_Type = Counter32
_BwmStatPortTcrOutdisoct_Object = MibTableColumn
bwmStatPortTcrOutdisoct = _BwmStatPortTcrOutdisoct_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 4, 1, 6),
    _BwmStatPortTcrOutdisoct_Type()
)
bwmStatPortTcrOutdisoct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcrOutdisoct.setStatus("current")
_BwmStatPortTcrBufferUsed_Type = Integer32
_BwmStatPortTcrBufferUsed_Object = MibTableColumn
bwmStatPortTcrBufferUsed = _BwmStatPortTcrBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 4, 1, 7),
    _BwmStatPortTcrBufferUsed_Type()
)
bwmStatPortTcrBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcrBufferUsed.setStatus("current")
_BwmStatPortTcrBufferMax_Type = Counter32
_BwmStatPortTcrBufferMax_Object = MibTableColumn
bwmStatPortTcrBufferMax = _BwmStatPortTcrBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 4, 1, 8),
    _BwmStatPortTcrBufferMax_Type()
)
bwmStatPortTcrBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcrBufferMax.setStatus("current")
_BwmStatPortTcrTotalPackets_Type = Counter32
_BwmStatPortTcrTotalPackets_Object = MibTableColumn
bwmStatPortTcrTotalPackets = _BwmStatPortTcrTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 4, 1, 9),
    _BwmStatPortTcrTotalPackets_Type()
)
bwmStatPortTcrTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwmStatPortTcrTotalPackets.setStatus("current")


class _BwmStatsClear_Type(Integer32):
    """Custom type bwmStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_BwmStatsClear_Type.__name__ = "Integer32"
_BwmStatsClear_Object = MibScalar
bwmStatsClear = _BwmStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 2, 5),
    _BwmStatsClear_Type()
)
bwmStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmStatsClear.setStatus("current")
_BwmOpers_ObjectIdentity = ObjectIdentity
bwmOpers = _BwmOpers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 3)
)


class _BwmOperSendSMTP_Type(Integer32):
    """Custom type bwmOperSendSMTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("send", 2))
    )


_BwmOperSendSMTP_Type.__name__ = "Integer32"
_BwmOperSendSMTP_Object = MibScalar
bwmOperSendSMTP = _BwmOperSendSMTP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 3, 1),
    _BwmOperSendSMTP_Type()
)
bwmOperSendSMTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmOperSendSMTP.setStatus("current")


class _BwmOperClearUsrEntry_Type(Integer32):
    """Custom type bwmOperClearUsrEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_BwmOperClearUsrEntry_Type.__name__ = "Integer32"
_BwmOperClearUsrEntry_Object = MibScalar
bwmOperClearUsrEntry = _BwmOperClearUsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 6, 3, 2),
    _BwmOperClearUsrEntry_Type()
)
bwmOperClearUsrEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwmOperClearUsrEntry.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-CHEETAH-BWM-MIB",
    **{"bwm": bwm,
       "bwmConfigs": bwmConfigs,
       "bwmGeneralConfig": bwmGeneralConfig,
       "bwmCurCfgGenState": bwmCurCfgGenState,
       "bwmNewCfgGenState": bwmNewCfgGenState,
       "bwmCurCfgGenEnforcePolicy": bwmCurCfgGenEnforcePolicy,
       "bwmNewCfgGenEnforcePolicy": bwmNewCfgGenEnforcePolicy,
       "bwmCurCfgGenSmtpUser": bwmCurCfgGenSmtpUser,
       "bwmNewCfgGenSmtpUser": bwmNewCfgGenSmtpUser,
       "bwmCurCfgGenEmailFrequency": bwmCurCfgGenEmailFrequency,
       "bwmNewCfgGenEmailFrequency": bwmNewCfgGenEmailFrequency,
       "bwmCurCfgGenIPUserLimit": bwmCurCfgGenIPUserLimit,
       "bwmNewCfgGenIPUserLimit": bwmNewCfgGenIPUserLimit,
       "bwmCurCfgGenEmail": bwmCurCfgGenEmail,
       "bwmNewCfgGenEmail": bwmNewCfgGenEmail,
       "bwmCurCfgGenReport": bwmCurCfgGenReport,
       "bwmNewCfgGenReport": bwmNewCfgGenReport,
       "bwmCurCfgGenReportStr": bwmCurCfgGenReportStr,
       "bwmNewCfgGenReportStr": bwmNewCfgGenReportStr,
       "bwmPolicyConfig": bwmPolicyConfig,
       "bwmPolicyTableMaxEnt": bwmPolicyTableMaxEnt,
       "bwmCurCfgPolicyTable": bwmCurCfgPolicyTable,
       "bwmCurCfgPolicyTableEntry": bwmCurCfgPolicyTableEntry,
       "bwmCurCfgPolicyIndx": bwmCurCfgPolicyIndx,
       "bwmCurCfgPolicyTosIn": bwmCurCfgPolicyTosIn,
       "bwmCurCfgPolicyTosOut": bwmCurCfgPolicyTosOut,
       "bwmCurCfgPolicyHard": bwmCurCfgPolicyHard,
       "bwmCurCfgPolicySoft": bwmCurCfgPolicySoft,
       "bwmCurCfgPolicyResv": bwmCurCfgPolicyResv,
       "bwmCurCfgPolicyBuffer": bwmCurCfgPolicyBuffer,
       "bwmCurCfgPolicyUserLimit": bwmCurCfgPolicyUserLimit,
       "bwmNewCfgPolicyTable": bwmNewCfgPolicyTable,
       "bwmNewCfgPolicyTableEntry": bwmNewCfgPolicyTableEntry,
       "bwmNewCfgPolicyIndx": bwmNewCfgPolicyIndx,
       "bwmNewCfgPolicyTosIn": bwmNewCfgPolicyTosIn,
       "bwmNewCfgPolicyTosOut": bwmNewCfgPolicyTosOut,
       "bwmNewCfgPolicyHard": bwmNewCfgPolicyHard,
       "bwmNewCfgPolicySoft": bwmNewCfgPolicySoft,
       "bwmNewCfgPolicyResv": bwmNewCfgPolicyResv,
       "bwmNewCfgPolicyBuffer": bwmNewCfgPolicyBuffer,
       "bwmNewCfgPolicyDelete": bwmNewCfgPolicyDelete,
       "bwmNewCfgPolicyUserLimit": bwmNewCfgPolicyUserLimit,
       "bwmContractConfig": bwmContractConfig,
       "bwmContractTableMaxEnt": bwmContractTableMaxEnt,
       "bwmCurCfgContractTable": bwmCurCfgContractTable,
       "bwmCurCfgContractTableEntry": bwmCurCfgContractTableEntry,
       "bwmCurCfgContractIndx": bwmCurCfgContractIndx,
       "bwmCurCfgContractName": bwmCurCfgContractName,
       "bwmCurCfgContractState": bwmCurCfgContractState,
       "bwmCurCfgContractPolicy": bwmCurCfgContractPolicy,
       "bwmCurCfgContractPrec": bwmCurCfgContractPrec,
       "bwmCurCfgContractUseTos": bwmCurCfgContractUseTos,
       "bwmCurCfgContractHistory": bwmCurCfgContractHistory,
       "bwmCurCfgContractShaping": bwmCurCfgContractShaping,
       "bwmCurCfgContractResizeTcp": bwmCurCfgContractResizeTcp,
       "bwmCurCfgContractIpLimit": bwmCurCfgContractIpLimit,
       "bwmCurCfgContractIpType": bwmCurCfgContractIpType,
       "bwmCurCfgContractMonitorMode": bwmCurCfgContractMonitorMode,
       "bwmCurCfgContractGroup": bwmCurCfgContractGroup,
       "bwmCurCfgContractMaxSess": bwmCurCfgContractMaxSess,
       "bwmCurCfgContractRowType": bwmCurCfgContractRowType,
       "bwmNewCfgContractTable": bwmNewCfgContractTable,
       "bwmNewCfgContractTableEntry": bwmNewCfgContractTableEntry,
       "bwmNewCfgContractIndx": bwmNewCfgContractIndx,
       "bwmNewCfgContractName": bwmNewCfgContractName,
       "bwmNewCfgContractState": bwmNewCfgContractState,
       "bwmNewCfgContractPolicy": bwmNewCfgContractPolicy,
       "bwmNewCfgContractDelete": bwmNewCfgContractDelete,
       "bwmNewCfgContractPrec": bwmNewCfgContractPrec,
       "bwmNewCfgContractUseTos": bwmNewCfgContractUseTos,
       "bwmNewCfgContractHistory": bwmNewCfgContractHistory,
       "bwmNewCfgContractShaping": bwmNewCfgContractShaping,
       "bwmNewCfgContractResizeTcp": bwmNewCfgContractResizeTcp,
       "bwmNewCfgContractIpLimit": bwmNewCfgContractIpLimit,
       "bwmNewCfgContractIpType": bwmNewCfgContractIpType,
       "bwmNewCfgContractMonitorMode": bwmNewCfgContractMonitorMode,
       "bwmNewCfgContractGroup": bwmNewCfgContractGroup,
       "bwmNewCfgContractMaxSess": bwmNewCfgContractMaxSess,
       "bwmNewCfgContractRowType": bwmNewCfgContractRowType,
       "bwmAvailableContractsTable": bwmAvailableContractsTable,
       "bwmAvailableContractsTableEntry": bwmAvailableContractsTableEntry,
       "bwmContractIndx": bwmContractIndx,
       "bwmContractName": bwmContractName,
       "bwmContTimePolicyConfig": bwmContTimePolicyConfig,
       "bwmContTimePolicyTableMaxEnt": bwmContTimePolicyTableMaxEnt,
       "bwmCurCfgContTimePolicyTable": bwmCurCfgContTimePolicyTable,
       "bwmCurCfgContTimePolicyTableEntry": bwmCurCfgContTimePolicyTableEntry,
       "bwmCurCfgContTimePolicyContIndx": bwmCurCfgContTimePolicyContIndx,
       "bwmCurCfgContTimePolicyIndx": bwmCurCfgContTimePolicyIndx,
       "bwmCurCfgContTimePolicyDay": bwmCurCfgContTimePolicyDay,
       "bwmCurCfgContTimePolicyFrom": bwmCurCfgContTimePolicyFrom,
       "bwmCurCfgContTimePolicyTo": bwmCurCfgContTimePolicyTo,
       "bwmCurCfgContTimePolicyPol": bwmCurCfgContTimePolicyPol,
       "bwmCurCfgContTimePolicyState": bwmCurCfgContTimePolicyState,
       "bwmNewCfgContTimePolicyTable": bwmNewCfgContTimePolicyTable,
       "bwmNewCfgContTimePolicyTableEntry": bwmNewCfgContTimePolicyTableEntry,
       "bwmNewCfgContTimePolicyContIndx": bwmNewCfgContTimePolicyContIndx,
       "bwmNewCfgContTimePolicyIndx": bwmNewCfgContTimePolicyIndx,
       "bwmNewCfgContTimePolicyDay": bwmNewCfgContTimePolicyDay,
       "bwmNewCfgContTimePolicyFrom": bwmNewCfgContTimePolicyFrom,
       "bwmNewCfgContTimePolicyTo": bwmNewCfgContTimePolicyTo,
       "bwmNewCfgContTimePolicyPol": bwmNewCfgContTimePolicyPol,
       "bwmNewCfgContTimePolicyState": bwmNewCfgContTimePolicyState,
       "bwmNewCfgContTimePolicyDelete": bwmNewCfgContTimePolicyDelete,
       "bwmContractGroupConfig": bwmContractGroupConfig,
       "bwmContractGroupTableMaxEnt": bwmContractGroupTableMaxEnt,
       "bwmCurCfgContractGroupTable": bwmCurCfgContractGroupTable,
       "bwmCurCfgContractGroupTableEntry": bwmCurCfgContractGroupTableEntry,
       "bwmCurCfgContractGroupIndx": bwmCurCfgContractGroupIndx,
       "bwmCurCfgContractGroupContracts": bwmCurCfgContractGroupContracts,
       "bwmCurCfgContractGroupName": bwmCurCfgContractGroupName,
       "bwmNewCfgContractGroupTable": bwmNewCfgContractGroupTable,
       "bwmNewCfgContractGroupTableEntry": bwmNewCfgContractGroupTableEntry,
       "bwmNewCfgContractGroupIndx": bwmNewCfgContractGroupIndx,
       "bwmNewCfgContractGroupContracts": bwmNewCfgContractGroupContracts,
       "bwmNewCfgContractGroupAddCont": bwmNewCfgContractGroupAddCont,
       "bwmNewCfgContractGroupRemCont": bwmNewCfgContractGroupRemCont,
       "bwmNewCfgContractGroupDelete": bwmNewCfgContractGroupDelete,
       "bwmNewCfgContractGroupName": bwmNewCfgContractGroupName,
       "bwmContractGroupTableMaxCont": bwmContractGroupTableMaxCont,
       "bwmStats": bwmStats,
       "bwmStatTcTable": bwmStatTcTable,
       "bwmStatTcEntry": bwmStatTcEntry,
       "bwmStatTcContractIndex": bwmStatTcContractIndex,
       "bwmStatTcName": bwmStatTcName,
       "bwmStatTcOutoct": bwmStatTcOutoct,
       "bwmStatTcOutdisoct": bwmStatTcOutdisoct,
       "bwmStatTcBufferUsed": bwmStatTcBufferUsed,
       "bwmStatTcBufferMax": bwmStatTcBufferMax,
       "bwmStatTcTotalPackets": bwmStatTcTotalPackets,
       "bwmStatTcSessRejected": bwmStatTcSessRejected,
       "bwmStatTcrTable": bwmStatTcrTable,
       "bwmStatTcrEntry": bwmStatTcrEntry,
       "bwmStatTcrContractIndex": bwmStatTcrContractIndex,
       "bwmStatTcrName": bwmStatTcrName,
       "bwmStatTcrRate": bwmStatTcrRate,
       "bwmStatTcrOutoct": bwmStatTcrOutoct,
       "bwmStatTcrOutdisoct": bwmStatTcrOutdisoct,
       "bwmStatTcrBufferUsed": bwmStatTcrBufferUsed,
       "bwmStatTcrBufferMax": bwmStatTcrBufferMax,
       "bwmStatTcrTotalPackets": bwmStatTcrTotalPackets,
       "bwmStatPortTcTable": bwmStatPortTcTable,
       "bwmStatPortTcEntry": bwmStatPortTcEntry,
       "bwmStatPortTcPortIndex": bwmStatPortTcPortIndex,
       "bwmStatPortTcContractIndex": bwmStatPortTcContractIndex,
       "bwmStatPortTcName": bwmStatPortTcName,
       "bwmStatPortTcOutoct": bwmStatPortTcOutoct,
       "bwmStatPortTcOutdisoct": bwmStatPortTcOutdisoct,
       "bwmStatPortTcBufferUsed": bwmStatPortTcBufferUsed,
       "bwmStatPortTcBufferMax": bwmStatPortTcBufferMax,
       "bwmStatPortTcTotalPackets": bwmStatPortTcTotalPackets,
       "bwmStatPortTcrTable": bwmStatPortTcrTable,
       "bwmStatPortTcrEntry": bwmStatPortTcrEntry,
       "bwmStatPortTcrPortIndex": bwmStatPortTcrPortIndex,
       "bwmStatPortTcrContractIndex": bwmStatPortTcrContractIndex,
       "bwmStatPortTcrName": bwmStatPortTcrName,
       "bwmStatPortTcrRate": bwmStatPortTcrRate,
       "bwmStatPortTcrOutoct": bwmStatPortTcrOutoct,
       "bwmStatPortTcrOutdisoct": bwmStatPortTcrOutdisoct,
       "bwmStatPortTcrBufferUsed": bwmStatPortTcrBufferUsed,
       "bwmStatPortTcrBufferMax": bwmStatPortTcrBufferMax,
       "bwmStatPortTcrTotalPackets": bwmStatPortTcrTotalPackets,
       "bwmStatsClear": bwmStatsClear,
       "bwmOpers": bwmOpers,
       "bwmOperSendSMTP": bwmOperSendSMTP,
       "bwmOperClearUsrEntry": bwmOperClearUsrEntry}
)
