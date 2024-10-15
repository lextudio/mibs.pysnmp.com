# SNMP MIB module (ASCEND-MIBANSWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBANSWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:03 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibanswerProfile_ObjectIdentity = ObjectIdentity
mibanswerProfile = _MibanswerProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 3)
)
_MibanswerProfileTable_Object = MibTable
mibanswerProfileTable = _MibanswerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1)
)
if mibBuilder.loadTexts:
    mibanswerProfileTable.setStatus("mandatory")
_MibanswerProfileEntry_Object = MibTableRow
mibanswerProfileEntry = _MibanswerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1)
)
mibanswerProfileEntry.setIndexNames(
    (0, "ASCEND-MIBANSWER-MIB", "answerProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibanswerProfileEntry.setStatus("mandatory")
_AnswerProfile_Index_o_Type = Integer32
_AnswerProfile_Index_o_Object = MibScalar
answerProfile_Index_o = _AnswerProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 1),
    _AnswerProfile_Index_o_Type()
)
answerProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    answerProfile_Index_o.setStatus("mandatory")


class _AnswerProfile_UseAnswerForAllDefaults_Type(Integer32):
    """Custom type answerProfile_UseAnswerForAllDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_UseAnswerForAllDefaults_Type.__name__ = "Integer32"
_AnswerProfile_UseAnswerForAllDefaults_Object = MibScalar
answerProfile_UseAnswerForAllDefaults = _AnswerProfile_UseAnswerForAllDefaults_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 2),
    _AnswerProfile_UseAnswerForAllDefaults_Type()
)
answerProfile_UseAnswerForAllDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_UseAnswerForAllDefaults.setStatus("mandatory")


class _AnswerProfile_Force56kbps_Type(Integer32):
    """Custom type answerProfile_Force56kbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_Force56kbps_Type.__name__ = "Integer32"
_AnswerProfile_Force56kbps_Object = MibScalar
answerProfile_Force56kbps = _AnswerProfile_Force56kbps_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 3),
    _AnswerProfile_Force56kbps_Type()
)
answerProfile_Force56kbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_Force56kbps.setStatus("mandatory")


class _AnswerProfile_ProfilesRequired_Type(Integer32):
    """Custom type answerProfile_ProfilesRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_ProfilesRequired_Type.__name__ = "Integer32"
_AnswerProfile_ProfilesRequired_Object = MibScalar
answerProfile_ProfilesRequired = _AnswerProfile_ProfilesRequired_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 4),
    _AnswerProfile_ProfilesRequired_Type()
)
answerProfile_ProfilesRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_ProfilesRequired.setStatus("mandatory")


class _AnswerProfile_ClidAuthMode_Type(Integer32):
    """Custom type answerProfile_ClidAuthMode based on Integer32"""
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
        *(("clidFallback", 4),
          ("clidFirst", 7),
          ("clidPrefer", 2),
          ("clidRequire", 3),
          ("dnisFallback", 9),
          ("dnisFirst", 8),
          ("dnisPref", 6),
          ("dnisRequire", 5),
          ("ignore", 1))
    )


_AnswerProfile_ClidAuthMode_Type.__name__ = "Integer32"
_AnswerProfile_ClidAuthMode_Object = MibScalar
answerProfile_ClidAuthMode = _AnswerProfile_ClidAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 5),
    _AnswerProfile_ClidAuthMode_Type()
)
answerProfile_ClidAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_ClidAuthMode.setStatus("mandatory")


class _AnswerProfile_PppAnswer_Enabled_Type(Integer32):
    """Custom type answerProfile_PppAnswer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_PppAnswer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_PppAnswer_Enabled_Object = MibScalar
answerProfile_PppAnswer_Enabled = _AnswerProfile_PppAnswer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 6),
    _AnswerProfile_PppAnswer_Enabled_Type()
)
answerProfile_PppAnswer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_Enabled.setStatus("mandatory")


class _AnswerProfile_PppAnswer_ReceiveAuthMode_Type(Integer32):
    """Custom type answerProfile_PppAnswer_ReceiveAuthMode based on Integer32"""
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
        *(("anyPppAuth", 4),
          ("cacheTokenPppAuth", 8),
          ("chapPppAuth", 3),
          ("desPapPppAuth", 5),
          ("msChapPppAuth", 9),
          ("noPppAuth", 1),
          ("papPppAuth", 2),
          ("papPreferred", 10),
          ("tokenChapPppAuth", 7),
          ("tokenPapPppAuth", 6))
    )


_AnswerProfile_PppAnswer_ReceiveAuthMode_Type.__name__ = "Integer32"
_AnswerProfile_PppAnswer_ReceiveAuthMode_Object = MibScalar
answerProfile_PppAnswer_ReceiveAuthMode = _AnswerProfile_PppAnswer_ReceiveAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 7),
    _AnswerProfile_PppAnswer_ReceiveAuthMode_Type()
)
answerProfile_PppAnswer_ReceiveAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_ReceiveAuthMode.setStatus("mandatory")


class _AnswerProfile_PppAnswer_DisconnectOnAuthTimeout_Type(Integer32):
    """Custom type answerProfile_PppAnswer_DisconnectOnAuthTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_PppAnswer_DisconnectOnAuthTimeout_Type.__name__ = "Integer32"
_AnswerProfile_PppAnswer_DisconnectOnAuthTimeout_Object = MibScalar
answerProfile_PppAnswer_DisconnectOnAuthTimeout = _AnswerProfile_PppAnswer_DisconnectOnAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 8),
    _AnswerProfile_PppAnswer_DisconnectOnAuthTimeout_Type()
)
answerProfile_PppAnswer_DisconnectOnAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_DisconnectOnAuthTimeout.setStatus("mandatory")
_AnswerProfile_PppAnswer_BridgingGroup_Type = Integer32
_AnswerProfile_PppAnswer_BridgingGroup_Object = MibScalar
answerProfile_PppAnswer_BridgingGroup = _AnswerProfile_PppAnswer_BridgingGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 9),
    _AnswerProfile_PppAnswer_BridgingGroup_Type()
)
answerProfile_PppAnswer_BridgingGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_BridgingGroup.setStatus("mandatory")


class _AnswerProfile_PppAnswer_LinkCompression_Type(Integer32):
    """Custom type answerProfile_PppAnswer_LinkCompression based on Integer32"""
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
        *(("mppc", 5),
          ("msStac", 4),
          ("none", 1),
          ("stac", 2),
          ("stac9", 3))
    )


_AnswerProfile_PppAnswer_LinkCompression_Type.__name__ = "Integer32"
_AnswerProfile_PppAnswer_LinkCompression_Object = MibScalar
answerProfile_PppAnswer_LinkCompression = _AnswerProfile_PppAnswer_LinkCompression_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 10),
    _AnswerProfile_PppAnswer_LinkCompression_Type()
)
answerProfile_PppAnswer_LinkCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_LinkCompression.setStatus("mandatory")
_AnswerProfile_PppAnswer_Mru_Type = Integer32
_AnswerProfile_PppAnswer_Mru_Object = MibScalar
answerProfile_PppAnswer_Mru = _AnswerProfile_PppAnswer_Mru_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 11),
    _AnswerProfile_PppAnswer_Mru_Type()
)
answerProfile_PppAnswer_Mru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_Mru.setStatus("mandatory")


class _AnswerProfile_PppAnswer_Lqm_Type(Integer32):
    """Custom type answerProfile_PppAnswer_Lqm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_PppAnswer_Lqm_Type.__name__ = "Integer32"
_AnswerProfile_PppAnswer_Lqm_Object = MibScalar
answerProfile_PppAnswer_Lqm = _AnswerProfile_PppAnswer_Lqm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 12),
    _AnswerProfile_PppAnswer_Lqm_Type()
)
answerProfile_PppAnswer_Lqm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_Lqm.setStatus("mandatory")
_AnswerProfile_PppAnswer_LqmMinimumPeriod_Type = Integer32
_AnswerProfile_PppAnswer_LqmMinimumPeriod_Object = MibScalar
answerProfile_PppAnswer_LqmMinimumPeriod = _AnswerProfile_PppAnswer_LqmMinimumPeriod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 13),
    _AnswerProfile_PppAnswer_LqmMinimumPeriod_Type()
)
answerProfile_PppAnswer_LqmMinimumPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_LqmMinimumPeriod.setStatus("mandatory")
_AnswerProfile_PppAnswer_LqmMaximumPeriod_Type = Integer32
_AnswerProfile_PppAnswer_LqmMaximumPeriod_Object = MibScalar
answerProfile_PppAnswer_LqmMaximumPeriod = _AnswerProfile_PppAnswer_LqmMaximumPeriod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 14),
    _AnswerProfile_PppAnswer_LqmMaximumPeriod_Type()
)
answerProfile_PppAnswer_LqmMaximumPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_LqmMaximumPeriod.setStatus("mandatory")


class _AnswerProfile_MpAnswer_Enabled_Type(Integer32):
    """Custom type answerProfile_MpAnswer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_MpAnswer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_MpAnswer_Enabled_Object = MibScalar
answerProfile_MpAnswer_Enabled = _AnswerProfile_MpAnswer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 15),
    _AnswerProfile_MpAnswer_Enabled_Type()
)
answerProfile_MpAnswer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MpAnswer_Enabled.setStatus("mandatory")
_AnswerProfile_MpAnswer_MinimumChannels_Type = Integer32
_AnswerProfile_MpAnswer_MinimumChannels_Object = MibScalar
answerProfile_MpAnswer_MinimumChannels = _AnswerProfile_MpAnswer_MinimumChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 16),
    _AnswerProfile_MpAnswer_MinimumChannels_Type()
)
answerProfile_MpAnswer_MinimumChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MpAnswer_MinimumChannels.setStatus("mandatory")
_AnswerProfile_MpAnswer_MaximumChannels_Type = Integer32
_AnswerProfile_MpAnswer_MaximumChannels_Object = MibScalar
answerProfile_MpAnswer_MaximumChannels = _AnswerProfile_MpAnswer_MaximumChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 17),
    _AnswerProfile_MpAnswer_MaximumChannels_Type()
)
answerProfile_MpAnswer_MaximumChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MpAnswer_MaximumChannels.setStatus("mandatory")


class _AnswerProfile_MpAnswer_BacpEnable_Type(Integer32):
    """Custom type answerProfile_MpAnswer_BacpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_MpAnswer_BacpEnable_Type.__name__ = "Integer32"
_AnswerProfile_MpAnswer_BacpEnable_Object = MibScalar
answerProfile_MpAnswer_BacpEnable = _AnswerProfile_MpAnswer_BacpEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 18),
    _AnswerProfile_MpAnswer_BacpEnable_Type()
)
answerProfile_MpAnswer_BacpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MpAnswer_BacpEnable.setStatus("mandatory")


class _AnswerProfile_MppAnswer_Enabled_Type(Integer32):
    """Custom type answerProfile_MppAnswer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_MppAnswer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_MppAnswer_Enabled_Object = MibScalar
answerProfile_MppAnswer_Enabled = _AnswerProfile_MppAnswer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 19),
    _AnswerProfile_MppAnswer_Enabled_Type()
)
answerProfile_MppAnswer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MppAnswer_Enabled.setStatus("mandatory")


class _AnswerProfile_MppAnswer_DynamicAlgorithm_Type(Integer32):
    """Custom type answerProfile_MppAnswer_DynamicAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("constant", 1),
          ("linear", 2),
          ("quadratic", 3))
    )


_AnswerProfile_MppAnswer_DynamicAlgorithm_Type.__name__ = "Integer32"
_AnswerProfile_MppAnswer_DynamicAlgorithm_Object = MibScalar
answerProfile_MppAnswer_DynamicAlgorithm = _AnswerProfile_MppAnswer_DynamicAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 20),
    _AnswerProfile_MppAnswer_DynamicAlgorithm_Type()
)
answerProfile_MppAnswer_DynamicAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MppAnswer_DynamicAlgorithm.setStatus("mandatory")


class _AnswerProfile_MppAnswer_BandwidthMonitorDirection_Type(Integer32):
    """Custom type answerProfile_MppAnswer_BandwidthMonitorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("transmit", 1),
          ("transmitRecv", 2))
    )


_AnswerProfile_MppAnswer_BandwidthMonitorDirection_Type.__name__ = "Integer32"
_AnswerProfile_MppAnswer_BandwidthMonitorDirection_Object = MibScalar
answerProfile_MppAnswer_BandwidthMonitorDirection = _AnswerProfile_MppAnswer_BandwidthMonitorDirection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 21),
    _AnswerProfile_MppAnswer_BandwidthMonitorDirection_Type()
)
answerProfile_MppAnswer_BandwidthMonitorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MppAnswer_BandwidthMonitorDirection.setStatus("mandatory")
_AnswerProfile_MppAnswer_IncrementChannelCount_Type = Integer32
_AnswerProfile_MppAnswer_IncrementChannelCount_Object = MibScalar
answerProfile_MppAnswer_IncrementChannelCount = _AnswerProfile_MppAnswer_IncrementChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 22),
    _AnswerProfile_MppAnswer_IncrementChannelCount_Type()
)
answerProfile_MppAnswer_IncrementChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MppAnswer_IncrementChannelCount.setStatus("mandatory")
_AnswerProfile_MppAnswer_DecrementChannelCount_Type = Integer32
_AnswerProfile_MppAnswer_DecrementChannelCount_Object = MibScalar
answerProfile_MppAnswer_DecrementChannelCount = _AnswerProfile_MppAnswer_DecrementChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 23),
    _AnswerProfile_MppAnswer_DecrementChannelCount_Type()
)
answerProfile_MppAnswer_DecrementChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MppAnswer_DecrementChannelCount.setStatus("mandatory")
_AnswerProfile_MppAnswer_SecondsHistory_Type = Integer32
_AnswerProfile_MppAnswer_SecondsHistory_Object = MibScalar
answerProfile_MppAnswer_SecondsHistory = _AnswerProfile_MppAnswer_SecondsHistory_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 24),
    _AnswerProfile_MppAnswer_SecondsHistory_Type()
)
answerProfile_MppAnswer_SecondsHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MppAnswer_SecondsHistory.setStatus("mandatory")
_AnswerProfile_MppAnswer_AddPersistence_Type = Integer32
_AnswerProfile_MppAnswer_AddPersistence_Object = MibScalar
answerProfile_MppAnswer_AddPersistence = _AnswerProfile_MppAnswer_AddPersistence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 25),
    _AnswerProfile_MppAnswer_AddPersistence_Type()
)
answerProfile_MppAnswer_AddPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MppAnswer_AddPersistence.setStatus("mandatory")
_AnswerProfile_MppAnswer_SubPersistence_Type = Integer32
_AnswerProfile_MppAnswer_SubPersistence_Object = MibScalar
answerProfile_MppAnswer_SubPersistence = _AnswerProfile_MppAnswer_SubPersistence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 26),
    _AnswerProfile_MppAnswer_SubPersistence_Type()
)
answerProfile_MppAnswer_SubPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MppAnswer_SubPersistence.setStatus("mandatory")
_AnswerProfile_MppAnswer_TargetUtilization_Type = Integer32
_AnswerProfile_MppAnswer_TargetUtilization_Object = MibScalar
answerProfile_MppAnswer_TargetUtilization = _AnswerProfile_MppAnswer_TargetUtilization_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 27),
    _AnswerProfile_MppAnswer_TargetUtilization_Type()
)
answerProfile_MppAnswer_TargetUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_MppAnswer_TargetUtilization.setStatus("mandatory")


class _AnswerProfile_FrAnswer_Enabled_Type(Integer32):
    """Custom type answerProfile_FrAnswer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_FrAnswer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_FrAnswer_Enabled_Object = MibScalar
answerProfile_FrAnswer_Enabled = _AnswerProfile_FrAnswer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 28),
    _AnswerProfile_FrAnswer_Enabled_Type()
)
answerProfile_FrAnswer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_FrAnswer_Enabled.setStatus("mandatory")


class _AnswerProfile_TcpClearAnswer_Enabled_Type(Integer32):
    """Custom type answerProfile_TcpClearAnswer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_TcpClearAnswer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_TcpClearAnswer_Enabled_Object = MibScalar
answerProfile_TcpClearAnswer_Enabled = _AnswerProfile_TcpClearAnswer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 29),
    _AnswerProfile_TcpClearAnswer_Enabled_Type()
)
answerProfile_TcpClearAnswer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_TcpClearAnswer_Enabled.setStatus("mandatory")


class _AnswerProfile_AraAnswer_Enabled_Type(Integer32):
    """Custom type answerProfile_AraAnswer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_AraAnswer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_AraAnswer_Enabled_Object = MibScalar
answerProfile_AraAnswer_Enabled = _AnswerProfile_AraAnswer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 30),
    _AnswerProfile_AraAnswer_Enabled_Type()
)
answerProfile_AraAnswer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_AraAnswer_Enabled.setStatus("mandatory")


class _AnswerProfile_V120Answer_Enabled_Type(Integer32):
    """Custom type answerProfile_V120Answer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_V120Answer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_V120Answer_Enabled_Object = MibScalar
answerProfile_V120Answer_Enabled = _AnswerProfile_V120Answer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 31),
    _AnswerProfile_V120Answer_Enabled_Type()
)
answerProfile_V120Answer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_V120Answer_Enabled.setStatus("mandatory")
_AnswerProfile_V120Answer_FrameLength_Type = Integer32
_AnswerProfile_V120Answer_FrameLength_Object = MibScalar
answerProfile_V120Answer_FrameLength = _AnswerProfile_V120Answer_FrameLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 32),
    _AnswerProfile_V120Answer_FrameLength_Type()
)
answerProfile_V120Answer_FrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_V120Answer_FrameLength.setStatus("mandatory")


class _AnswerProfile_X25Answer_Enabled_Type(Integer32):
    """Custom type answerProfile_X25Answer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_X25Answer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_X25Answer_Enabled_Object = MibScalar
answerProfile_X25Answer_Enabled = _AnswerProfile_X25Answer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 33),
    _AnswerProfile_X25Answer_Enabled_Type()
)
answerProfile_X25Answer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_X25Answer_Enabled.setStatus("mandatory")
_AnswerProfile_X25Answer_X25Profile_Type = DisplayString
_AnswerProfile_X25Answer_X25Profile_Object = MibScalar
answerProfile_X25Answer_X25Profile = _AnswerProfile_X25Answer_X25Profile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 34),
    _AnswerProfile_X25Answer_X25Profile_Type()
)
answerProfile_X25Answer_X25Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_X25Answer_X25Profile.setStatus("mandatory")


class _AnswerProfile_X25Answer_X3Profile_Type(Integer32):
    """Custom type answerProfile_X25Answer_X3Profile based on Integer32"""
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
        *(("ccSspProfile", 5),
          ("ccTspProfile", 6),
          ("crtProfile", 1),
          ("customProfile", 11),
          ("defaultProfile", 3),
          ("hardcopyProfile", 7),
          ("hdxProfile", 8),
          ("infonetProfile", 2),
          ("nullProfile", 10),
          ("posProfile", 12),
          ("scenProfile", 4),
          ("sharkProfile", 9))
    )


_AnswerProfile_X25Answer_X3Profile_Type.__name__ = "Integer32"
_AnswerProfile_X25Answer_X3Profile_Object = MibScalar
answerProfile_X25Answer_X3Profile = _AnswerProfile_X25Answer_X3Profile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 35),
    _AnswerProfile_X25Answer_X3Profile_Type()
)
answerProfile_X25Answer_X3Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_X25Answer_X3Profile.setStatus("mandatory")
_AnswerProfile_X25Answer_MaxCalls_Type = Integer32
_AnswerProfile_X25Answer_MaxCalls_Object = MibScalar
answerProfile_X25Answer_MaxCalls = _AnswerProfile_X25Answer_MaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 36),
    _AnswerProfile_X25Answer_MaxCalls_Type()
)
answerProfile_X25Answer_MaxCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_X25Answer_MaxCalls.setStatus("mandatory")


class _AnswerProfile_X25Answer_VcTimerEnable_Type(Integer32):
    """Custom type answerProfile_X25Answer_VcTimerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_X25Answer_VcTimerEnable_Type.__name__ = "Integer32"
_AnswerProfile_X25Answer_VcTimerEnable_Object = MibScalar
answerProfile_X25Answer_VcTimerEnable = _AnswerProfile_X25Answer_VcTimerEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 37),
    _AnswerProfile_X25Answer_VcTimerEnable_Type()
)
answerProfile_X25Answer_VcTimerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_X25Answer_VcTimerEnable.setStatus("mandatory")
_AnswerProfile_X25Answer_AutoCallX121Address_Type = DisplayString
_AnswerProfile_X25Answer_AutoCallX121Address_Object = MibScalar
answerProfile_X25Answer_AutoCallX121Address = _AnswerProfile_X25Answer_AutoCallX121Address_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 38),
    _AnswerProfile_X25Answer_AutoCallX121Address_Type()
)
answerProfile_X25Answer_AutoCallX121Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    answerProfile_X25Answer_AutoCallX121Address.setStatus("mandatory")


class _AnswerProfile_X25Answer_ReverseCharge_Type(Integer32):
    """Custom type answerProfile_X25Answer_ReverseCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_X25Answer_ReverseCharge_Type.__name__ = "Integer32"
_AnswerProfile_X25Answer_ReverseCharge_Object = MibScalar
answerProfile_X25Answer_ReverseCharge = _AnswerProfile_X25Answer_ReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 39),
    _AnswerProfile_X25Answer_ReverseCharge_Type()
)
answerProfile_X25Answer_ReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_X25Answer_ReverseCharge.setStatus("mandatory")
_AnswerProfile_X25Answer_X3CustomProf_Type = DisplayString
_AnswerProfile_X25Answer_X3CustomProf_Object = MibScalar
answerProfile_X25Answer_X3CustomProf = _AnswerProfile_X25Answer_X3CustomProf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 40),
    _AnswerProfile_X25Answer_X3CustomProf_Type()
)
answerProfile_X25Answer_X3CustomProf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    answerProfile_X25Answer_X3CustomProf.setStatus("mandatory")


class _AnswerProfile_EuAnswer_EurawEnabled_Type(Integer32):
    """Custom type answerProfile_EuAnswer_EurawEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_EuAnswer_EurawEnabled_Type.__name__ = "Integer32"
_AnswerProfile_EuAnswer_EurawEnabled_Object = MibScalar
answerProfile_EuAnswer_EurawEnabled = _AnswerProfile_EuAnswer_EurawEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 45),
    _AnswerProfile_EuAnswer_EurawEnabled_Type()
)
answerProfile_EuAnswer_EurawEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_EuAnswer_EurawEnabled.setStatus("mandatory")


class _AnswerProfile_EuAnswer_EuuiEnabled_Type(Integer32):
    """Custom type answerProfile_EuAnswer_EuuiEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_EuAnswer_EuuiEnabled_Type.__name__ = "Integer32"
_AnswerProfile_EuAnswer_EuuiEnabled_Object = MibScalar
answerProfile_EuAnswer_EuuiEnabled = _AnswerProfile_EuAnswer_EuuiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 46),
    _AnswerProfile_EuAnswer_EuuiEnabled_Type()
)
answerProfile_EuAnswer_EuuiEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_EuAnswer_EuuiEnabled.setStatus("mandatory")
_AnswerProfile_EuAnswer_DceAddr_Type = Integer32
_AnswerProfile_EuAnswer_DceAddr_Object = MibScalar
answerProfile_EuAnswer_DceAddr = _AnswerProfile_EuAnswer_DceAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 47),
    _AnswerProfile_EuAnswer_DceAddr_Type()
)
answerProfile_EuAnswer_DceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_EuAnswer_DceAddr.setStatus("mandatory")
_AnswerProfile_EuAnswer_DteAddr_Type = Integer32
_AnswerProfile_EuAnswer_DteAddr_Object = MibScalar
answerProfile_EuAnswer_DteAddr = _AnswerProfile_EuAnswer_DteAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 48),
    _AnswerProfile_EuAnswer_DteAddr_Type()
)
answerProfile_EuAnswer_DteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_EuAnswer_DteAddr.setStatus("mandatory")
_AnswerProfile_EuAnswer_Mru_Type = Integer32
_AnswerProfile_EuAnswer_Mru_Object = MibScalar
answerProfile_EuAnswer_Mru = _AnswerProfile_EuAnswer_Mru_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 49),
    _AnswerProfile_EuAnswer_Mru_Type()
)
answerProfile_EuAnswer_Mru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_EuAnswer_Mru.setStatus("mandatory")


class _AnswerProfile_IpAnswer_Enabled_Type(Integer32):
    """Custom type answerProfile_IpAnswer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_IpAnswer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_IpAnswer_Enabled_Object = MibScalar
answerProfile_IpAnswer_Enabled = _AnswerProfile_IpAnswer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 50),
    _AnswerProfile_IpAnswer_Enabled_Type()
)
answerProfile_IpAnswer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_IpAnswer_Enabled.setStatus("mandatory")


class _AnswerProfile_IpAnswer_VjHeaderPrediction_Type(Integer32):
    """Custom type answerProfile_IpAnswer_VjHeaderPrediction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_IpAnswer_VjHeaderPrediction_Type.__name__ = "Integer32"
_AnswerProfile_IpAnswer_VjHeaderPrediction_Object = MibScalar
answerProfile_IpAnswer_VjHeaderPrediction = _AnswerProfile_IpAnswer_VjHeaderPrediction_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 51),
    _AnswerProfile_IpAnswer_VjHeaderPrediction_Type()
)
answerProfile_IpAnswer_VjHeaderPrediction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_IpAnswer_VjHeaderPrediction.setStatus("mandatory")


class _AnswerProfile_IpAnswer_AssignAddress_Type(Integer32):
    """Custom type answerProfile_IpAnswer_AssignAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_IpAnswer_AssignAddress_Type.__name__ = "Integer32"
_AnswerProfile_IpAnswer_AssignAddress_Object = MibScalar
answerProfile_IpAnswer_AssignAddress = _AnswerProfile_IpAnswer_AssignAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 52),
    _AnswerProfile_IpAnswer_AssignAddress_Type()
)
answerProfile_IpAnswer_AssignAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_IpAnswer_AssignAddress.setStatus("mandatory")
_AnswerProfile_IpAnswer_RoutingMetric_Type = Integer32
_AnswerProfile_IpAnswer_RoutingMetric_Object = MibScalar
answerProfile_IpAnswer_RoutingMetric = _AnswerProfile_IpAnswer_RoutingMetric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 53),
    _AnswerProfile_IpAnswer_RoutingMetric_Type()
)
answerProfile_IpAnswer_RoutingMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_IpAnswer_RoutingMetric.setStatus("mandatory")


class _AnswerProfile_IpxAnswer_Enabled_Type(Integer32):
    """Custom type answerProfile_IpxAnswer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_IpxAnswer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_IpxAnswer_Enabled_Object = MibScalar
answerProfile_IpxAnswer_Enabled = _AnswerProfile_IpxAnswer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 54),
    _AnswerProfile_IpxAnswer_Enabled_Type()
)
answerProfile_IpxAnswer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_IpxAnswer_Enabled.setStatus("mandatory")


class _AnswerProfile_IpxAnswer_PeerMode_Type(Integer32):
    """Custom type answerProfile_IpxAnswer_PeerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dialinPeer", 2),
          ("routerPeer", 1))
    )


_AnswerProfile_IpxAnswer_PeerMode_Type.__name__ = "Integer32"
_AnswerProfile_IpxAnswer_PeerMode_Object = MibScalar
answerProfile_IpxAnswer_PeerMode = _AnswerProfile_IpxAnswer_PeerMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 55),
    _AnswerProfile_IpxAnswer_PeerMode_Type()
)
answerProfile_IpxAnswer_PeerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_IpxAnswer_PeerMode.setStatus("mandatory")
_AnswerProfile_SessionInfo_CallFilter_Type = DisplayString
_AnswerProfile_SessionInfo_CallFilter_Object = MibScalar
answerProfile_SessionInfo_CallFilter = _AnswerProfile_SessionInfo_CallFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 56),
    _AnswerProfile_SessionInfo_CallFilter_Type()
)
answerProfile_SessionInfo_CallFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_SessionInfo_CallFilter.setStatus("mandatory")
_AnswerProfile_SessionInfo_DataFilter_Type = DisplayString
_AnswerProfile_SessionInfo_DataFilter_Object = MibScalar
answerProfile_SessionInfo_DataFilter = _AnswerProfile_SessionInfo_DataFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 57),
    _AnswerProfile_SessionInfo_DataFilter_Type()
)
answerProfile_SessionInfo_DataFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_SessionInfo_DataFilter.setStatus("mandatory")


class _AnswerProfile_SessionInfo_FilterPersistence_Type(Integer32):
    """Custom type answerProfile_SessionInfo_FilterPersistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_SessionInfo_FilterPersistence_Type.__name__ = "Integer32"
_AnswerProfile_SessionInfo_FilterPersistence_Object = MibScalar
answerProfile_SessionInfo_FilterPersistence = _AnswerProfile_SessionInfo_FilterPersistence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 58),
    _AnswerProfile_SessionInfo_FilterPersistence_Type()
)
answerProfile_SessionInfo_FilterPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_SessionInfo_FilterPersistence.setStatus("mandatory")
_AnswerProfile_SessionInfo_IdleTimer_Type = Integer32
_AnswerProfile_SessionInfo_IdleTimer_Object = MibScalar
answerProfile_SessionInfo_IdleTimer = _AnswerProfile_SessionInfo_IdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 59),
    _AnswerProfile_SessionInfo_IdleTimer_Type()
)
answerProfile_SessionInfo_IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_SessionInfo_IdleTimer.setStatus("mandatory")


class _AnswerProfile_SessionInfo_TsIdleMode_Type(Integer32):
    """Custom type answerProfile_SessionInfo_TsIdleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inputOnlyIdle", 2),
          ("inputOutputIdle", 3),
          ("noIdle", 1))
    )


_AnswerProfile_SessionInfo_TsIdleMode_Type.__name__ = "Integer32"
_AnswerProfile_SessionInfo_TsIdleMode_Object = MibScalar
answerProfile_SessionInfo_TsIdleMode = _AnswerProfile_SessionInfo_TsIdleMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 60),
    _AnswerProfile_SessionInfo_TsIdleMode_Type()
)
answerProfile_SessionInfo_TsIdleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_SessionInfo_TsIdleMode.setStatus("mandatory")
_AnswerProfile_SessionInfo_TsIdleTimer_Type = Integer32
_AnswerProfile_SessionInfo_TsIdleTimer_Object = MibScalar
answerProfile_SessionInfo_TsIdleTimer = _AnswerProfile_SessionInfo_TsIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 61),
    _AnswerProfile_SessionInfo_TsIdleTimer_Type()
)
answerProfile_SessionInfo_TsIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_SessionInfo_TsIdleTimer.setStatus("mandatory")
_AnswerProfile_SessionInfo_MaxCallDuration_Type = Integer32
_AnswerProfile_SessionInfo_MaxCallDuration_Object = MibScalar
answerProfile_SessionInfo_MaxCallDuration = _AnswerProfile_SessionInfo_MaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 62),
    _AnswerProfile_SessionInfo_MaxCallDuration_Type()
)
answerProfile_SessionInfo_MaxCallDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_SessionInfo_MaxCallDuration.setStatus("mandatory")


class _AnswerProfile_X75Answer_Enabled_Type(Integer32):
    """Custom type answerProfile_X75Answer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_X75Answer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_X75Answer_Enabled_Object = MibScalar
answerProfile_X75Answer_Enabled = _AnswerProfile_X75Answer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 63),
    _AnswerProfile_X75Answer_Enabled_Type()
)
answerProfile_X75Answer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_X75Answer_Enabled.setStatus("mandatory")
_AnswerProfile_X75Answer_KFramesOutstanding_Type = Integer32
_AnswerProfile_X75Answer_KFramesOutstanding_Object = MibScalar
answerProfile_X75Answer_KFramesOutstanding = _AnswerProfile_X75Answer_KFramesOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 64),
    _AnswerProfile_X75Answer_KFramesOutstanding_Type()
)
answerProfile_X75Answer_KFramesOutstanding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_X75Answer_KFramesOutstanding.setStatus("mandatory")
_AnswerProfile_X75Answer_N2Retransmissions_Type = Integer32
_AnswerProfile_X75Answer_N2Retransmissions_Object = MibScalar
answerProfile_X75Answer_N2Retransmissions = _AnswerProfile_X75Answer_N2Retransmissions_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 65),
    _AnswerProfile_X75Answer_N2Retransmissions_Type()
)
answerProfile_X75Answer_N2Retransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_X75Answer_N2Retransmissions.setStatus("mandatory")
_AnswerProfile_X75Answer_T1RetranTimer_Type = Integer32
_AnswerProfile_X75Answer_T1RetranTimer_Object = MibScalar
answerProfile_X75Answer_T1RetranTimer = _AnswerProfile_X75Answer_T1RetranTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 66),
    _AnswerProfile_X75Answer_T1RetranTimer_Type()
)
answerProfile_X75Answer_T1RetranTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_X75Answer_T1RetranTimer.setStatus("mandatory")
_AnswerProfile_X75Answer_FrameLength_Type = Integer32
_AnswerProfile_X75Answer_FrameLength_Object = MibScalar
answerProfile_X75Answer_FrameLength = _AnswerProfile_X75Answer_FrameLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 67),
    _AnswerProfile_X75Answer_FrameLength_Type()
)
answerProfile_X75Answer_FrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_X75Answer_FrameLength.setStatus("mandatory")


class _AnswerProfile_FramedOnly_Type(Integer32):
    """Custom type answerProfile_FramedOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_FramedOnly_Type.__name__ = "Integer32"
_AnswerProfile_FramedOnly_Object = MibScalar
answerProfile_FramedOnly = _AnswerProfile_FramedOnly_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 68),
    _AnswerProfile_FramedOnly_Type()
)
answerProfile_FramedOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_FramedOnly.setStatus("mandatory")


class _AnswerProfile_Action_o_Type(Integer32):
    """Custom type answerProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_AnswerProfile_Action_o_Type.__name__ = "Integer32"
_AnswerProfile_Action_o_Object = MibScalar
answerProfile_Action_o = _AnswerProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 69),
    _AnswerProfile_Action_o_Type()
)
answerProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_Action_o.setStatus("mandatory")


class _AnswerProfile_PppAnswer_CbcpEnabled_Type(Integer32):
    """Custom type answerProfile_PppAnswer_CbcpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_PppAnswer_CbcpEnabled_Type.__name__ = "Integer32"
_AnswerProfile_PppAnswer_CbcpEnabled_Object = MibScalar
answerProfile_PppAnswer_CbcpEnabled = _AnswerProfile_PppAnswer_CbcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 70),
    _AnswerProfile_PppAnswer_CbcpEnabled_Type()
)
answerProfile_PppAnswer_CbcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_CbcpEnabled.setStatus("mandatory")


class _AnswerProfile_HdlcNrmAnswer_Enabled_Type(Integer32):
    """Custom type answerProfile_HdlcNrmAnswer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_HdlcNrmAnswer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_HdlcNrmAnswer_Enabled_Object = MibScalar
answerProfile_HdlcNrmAnswer_Enabled = _AnswerProfile_HdlcNrmAnswer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 71),
    _AnswerProfile_HdlcNrmAnswer_Enabled_Type()
)
answerProfile_HdlcNrmAnswer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_HdlcNrmAnswer_Enabled.setStatus("mandatory")


class _AnswerProfile_Visa2Answer_Enabled_Type(Integer32):
    """Custom type answerProfile_Visa2Answer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_Visa2Answer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_Visa2Answer_Enabled_Object = MibScalar
answerProfile_Visa2Answer_Enabled = _AnswerProfile_Visa2Answer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 72),
    _AnswerProfile_Visa2Answer_Enabled_Type()
)
answerProfile_Visa2Answer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_Visa2Answer_Enabled.setStatus("mandatory")


class _AnswerProfile_ClidSelection_Type(Integer32):
    """Custom type answerProfile_ClidSelection based on Integer32"""
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
        *(("first", 1),
          ("securePrefer", 2),
          ("secureRequire", 3),
          ("userPrefer", 4),
          ("userRequire", 5))
    )


_AnswerProfile_ClidSelection_Type.__name__ = "Integer32"
_AnswerProfile_ClidSelection_Object = MibScalar
answerProfile_ClidSelection = _AnswerProfile_ClidSelection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 73),
    _AnswerProfile_ClidSelection_Type()
)
answerProfile_ClidSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_ClidSelection.setStatus("mandatory")


class _AnswerProfile_PppAnswer_IpxHeaderCompression_Type(Integer32):
    """Custom type answerProfile_PppAnswer_IpxHeaderCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_PppAnswer_IpxHeaderCompression_Type.__name__ = "Integer32"
_AnswerProfile_PppAnswer_IpxHeaderCompression_Object = MibScalar
answerProfile_PppAnswer_IpxHeaderCompression = _AnswerProfile_PppAnswer_IpxHeaderCompression_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 74),
    _AnswerProfile_PppAnswer_IpxHeaderCompression_Type()
)
answerProfile_PppAnswer_IpxHeaderCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_IpxHeaderCompression.setStatus("mandatory")
_AnswerProfile_PppAnswer_Mtu_Type = Integer32
_AnswerProfile_PppAnswer_Mtu_Object = MibScalar
answerProfile_PppAnswer_Mtu = _AnswerProfile_PppAnswer_Mtu_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 75),
    _AnswerProfile_PppAnswer_Mtu_Type()
)
answerProfile_PppAnswer_Mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_Mtu.setStatus("mandatory")


class _AnswerProfile_IpAnswer_PrivateRouteProfileRequired_Type(Integer32):
    """Custom type answerProfile_IpAnswer_PrivateRouteProfileRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_IpAnswer_PrivateRouteProfileRequired_Type.__name__ = "Integer32"
_AnswerProfile_IpAnswer_PrivateRouteProfileRequired_Object = MibScalar
answerProfile_IpAnswer_PrivateRouteProfileRequired = _AnswerProfile_IpAnswer_PrivateRouteProfileRequired_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 76),
    _AnswerProfile_IpAnswer_PrivateRouteProfileRequired_Type()
)
answerProfile_IpAnswer_PrivateRouteProfileRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_IpAnswer_PrivateRouteProfileRequired.setStatus("mandatory")


class _AnswerProfile_SessionInfo_FilterRequired_Type(Integer32):
    """Custom type answerProfile_SessionInfo_FilterRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_SessionInfo_FilterRequired_Type.__name__ = "Integer32"
_AnswerProfile_SessionInfo_FilterRequired_Object = MibScalar
answerProfile_SessionInfo_FilterRequired = _AnswerProfile_SessionInfo_FilterRequired_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 77),
    _AnswerProfile_SessionInfo_FilterRequired_Type()
)
answerProfile_SessionInfo_FilterRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_SessionInfo_FilterRequired.setStatus("mandatory")


class _AnswerProfile_AtmAnswer_SvcEnabled_Type(Integer32):
    """Custom type answerProfile_AtmAnswer_SvcEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_AtmAnswer_SvcEnabled_Type.__name__ = "Integer32"
_AnswerProfile_AtmAnswer_SvcEnabled_Object = MibScalar
answerProfile_AtmAnswer_SvcEnabled = _AnswerProfile_AtmAnswer_SvcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 78),
    _AnswerProfile_AtmAnswer_SvcEnabled_Type()
)
answerProfile_AtmAnswer_SvcEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_AtmAnswer_SvcEnabled.setStatus("mandatory")


class _AnswerProfile_PppAnswer_BiDirectionalAuth_Type(Integer32):
    """Custom type answerProfile_PppAnswer_BiDirectionalAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 2),
          ("none", 1),
          ("required", 3))
    )


_AnswerProfile_PppAnswer_BiDirectionalAuth_Type.__name__ = "Integer32"
_AnswerProfile_PppAnswer_BiDirectionalAuth_Object = MibScalar
answerProfile_PppAnswer_BiDirectionalAuth = _AnswerProfile_PppAnswer_BiDirectionalAuth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 79),
    _AnswerProfile_PppAnswer_BiDirectionalAuth_Type()
)
answerProfile_PppAnswer_BiDirectionalAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_BiDirectionalAuth.setStatus("mandatory")
_AnswerProfile_PppAnswer_SubstituteSendName_Type = DisplayString
_AnswerProfile_PppAnswer_SubstituteSendName_Object = MibScalar
answerProfile_PppAnswer_SubstituteSendName = _AnswerProfile_PppAnswer_SubstituteSendName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 80),
    _AnswerProfile_PppAnswer_SubstituteSendName_Type()
)
answerProfile_PppAnswer_SubstituteSendName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_SubstituteSendName.setStatus("mandatory")


class _AnswerProfile_PppAnswer_AuthForAsyncFramedUsers_Type(Integer32):
    """Custom type answerProfile_PppAnswer_AuthForAsyncFramedUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRequired", 1),
          ("required", 2))
    )


_AnswerProfile_PppAnswer_AuthForAsyncFramedUsers_Type.__name__ = "Integer32"
_AnswerProfile_PppAnswer_AuthForAsyncFramedUsers_Object = MibScalar
answerProfile_PppAnswer_AuthForAsyncFramedUsers = _AnswerProfile_PppAnswer_AuthForAsyncFramedUsers_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 81),
    _AnswerProfile_PppAnswer_AuthForAsyncFramedUsers_Type()
)
answerProfile_PppAnswer_AuthForAsyncFramedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_AuthForAsyncFramedUsers.setStatus("mandatory")
_AnswerProfile_PppAnswer_MaxPapAuthRetry_Type = Integer32
_AnswerProfile_PppAnswer_MaxPapAuthRetry_Object = MibScalar
answerProfile_PppAnswer_MaxPapAuthRetry = _AnswerProfile_PppAnswer_MaxPapAuthRetry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 82),
    _AnswerProfile_PppAnswer_MaxPapAuthRetry_Type()
)
answerProfile_PppAnswer_MaxPapAuthRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_MaxPapAuthRetry.setStatus("mandatory")
_AnswerProfile_IpAnswer_PoolForAsyncFramedUser_Type = Integer32
_AnswerProfile_IpAnswer_PoolForAsyncFramedUser_Object = MibScalar
answerProfile_IpAnswer_PoolForAsyncFramedUser = _AnswerProfile_IpAnswer_PoolForAsyncFramedUser_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 83),
    _AnswerProfile_IpAnswer_PoolForAsyncFramedUser_Type()
)
answerProfile_IpAnswer_PoolForAsyncFramedUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_IpAnswer_PoolForAsyncFramedUser.setStatus("mandatory")
_AnswerProfile_CallbackClidPrefix_Type = DisplayString
_AnswerProfile_CallbackClidPrefix_Object = MibScalar
answerProfile_CallbackClidPrefix = _AnswerProfile_CallbackClidPrefix_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 85),
    _AnswerProfile_CallbackClidPrefix_Type()
)
answerProfile_CallbackClidPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_CallbackClidPrefix.setStatus("mandatory")


class _AnswerProfile_PriorityAnswer_PacketClassification_Type(Integer32):
    """Custom type answerProfile_PriorityAnswer_PacketClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qosTag", 2),
          ("udpPortRange", 3))
    )


_AnswerProfile_PriorityAnswer_PacketClassification_Type.__name__ = "Integer32"
_AnswerProfile_PriorityAnswer_PacketClassification_Object = MibScalar
answerProfile_PriorityAnswer_PacketClassification = _AnswerProfile_PriorityAnswer_PacketClassification_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 87),
    _AnswerProfile_PriorityAnswer_PacketClassification_Type()
)
answerProfile_PriorityAnswer_PacketClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PriorityAnswer_PacketClassification.setStatus("mandatory")
_AnswerProfile_PriorityAnswer_MaxRtpPacketDelay_Type = Integer32
_AnswerProfile_PriorityAnswer_MaxRtpPacketDelay_Object = MibScalar
answerProfile_PriorityAnswer_MaxRtpPacketDelay = _AnswerProfile_PriorityAnswer_MaxRtpPacketDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 88),
    _AnswerProfile_PriorityAnswer_MaxRtpPacketDelay_Type()
)
answerProfile_PriorityAnswer_MaxRtpPacketDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PriorityAnswer_MaxRtpPacketDelay.setStatus("mandatory")
_AnswerProfile_PriorityAnswer_MinimumRtpPort_Type = Integer32
_AnswerProfile_PriorityAnswer_MinimumRtpPort_Object = MibScalar
answerProfile_PriorityAnswer_MinimumRtpPort = _AnswerProfile_PriorityAnswer_MinimumRtpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 89),
    _AnswerProfile_PriorityAnswer_MinimumRtpPort_Type()
)
answerProfile_PriorityAnswer_MinimumRtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PriorityAnswer_MinimumRtpPort.setStatus("mandatory")
_AnswerProfile_PriorityAnswer_MaximumRtpPort_Type = Integer32
_AnswerProfile_PriorityAnswer_MaximumRtpPort_Object = MibScalar
answerProfile_PriorityAnswer_MaximumRtpPort = _AnswerProfile_PriorityAnswer_MaximumRtpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 90),
    _AnswerProfile_PriorityAnswer_MaximumRtpPort_Type()
)
answerProfile_PriorityAnswer_MaximumRtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PriorityAnswer_MaximumRtpPort.setStatus("mandatory")
_AnswerProfile_PriorityAnswer_NoHighPrioPktDuration_Type = Integer32
_AnswerProfile_PriorityAnswer_NoHighPrioPktDuration_Object = MibScalar
answerProfile_PriorityAnswer_NoHighPrioPktDuration = _AnswerProfile_PriorityAnswer_NoHighPrioPktDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 91),
    _AnswerProfile_PriorityAnswer_NoHighPrioPktDuration_Type()
)
answerProfile_PriorityAnswer_NoHighPrioPktDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PriorityAnswer_NoHighPrioPktDuration.setStatus("mandatory")
_AnswerProfile_PppAnswer_MaxPppConfigureRetry_Type = Integer32
_AnswerProfile_PppAnswer_MaxPppConfigureRetry_Object = MibScalar
answerProfile_PppAnswer_MaxPppConfigureRetry = _AnswerProfile_PppAnswer_MaxPppConfigureRetry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 92),
    _AnswerProfile_PppAnswer_MaxPppConfigureRetry_Type()
)
answerProfile_PppAnswer_MaxPppConfigureRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_MaxPppConfigureRetry.setStatus("mandatory")
_AnswerProfile_PppAnswer_PppRestartTimer_Type = Integer32
_AnswerProfile_PppAnswer_PppRestartTimer_Object = MibScalar
answerProfile_PppAnswer_PppRestartTimer = _AnswerProfile_PppAnswer_PppRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 93),
    _AnswerProfile_PppAnswer_PppRestartTimer_Type()
)
answerProfile_PppAnswer_PppRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_PppRestartTimer.setStatus("mandatory")
_AnswerProfile_PppAnswer_MaxPppRestartTimer_Type = Integer32
_AnswerProfile_PppAnswer_MaxPppRestartTimer_Object = MibScalar
answerProfile_PppAnswer_MaxPppRestartTimer = _AnswerProfile_PppAnswer_MaxPppRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 94),
    _AnswerProfile_PppAnswer_MaxPppRestartTimer_Type()
)
answerProfile_PppAnswer_MaxPppRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PppAnswer_MaxPppRestartTimer.setStatus("mandatory")


class _AnswerProfile_PriorityAnswer_Enabled_Type(Integer32):
    """Custom type answerProfile_PriorityAnswer_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AnswerProfile_PriorityAnswer_Enabled_Type.__name__ = "Integer32"
_AnswerProfile_PriorityAnswer_Enabled_Object = MibScalar
answerProfile_PriorityAnswer_Enabled = _AnswerProfile_PriorityAnswer_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 3, 1, 1, 95),
    _AnswerProfile_PriorityAnswer_Enabled_Type()
)
answerProfile_PriorityAnswer_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerProfile_PriorityAnswer_Enabled.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBANSWER-MIB",
    **{"DisplayString": DisplayString,
       "mibanswerProfile": mibanswerProfile,
       "mibanswerProfileTable": mibanswerProfileTable,
       "mibanswerProfileEntry": mibanswerProfileEntry,
       "answerProfile-Index-o": answerProfile_Index_o,
       "answerProfile-UseAnswerForAllDefaults": answerProfile_UseAnswerForAllDefaults,
       "answerProfile-Force56kbps": answerProfile_Force56kbps,
       "answerProfile-ProfilesRequired": answerProfile_ProfilesRequired,
       "answerProfile-ClidAuthMode": answerProfile_ClidAuthMode,
       "answerProfile-PppAnswer-Enabled": answerProfile_PppAnswer_Enabled,
       "answerProfile-PppAnswer-ReceiveAuthMode": answerProfile_PppAnswer_ReceiveAuthMode,
       "answerProfile-PppAnswer-DisconnectOnAuthTimeout": answerProfile_PppAnswer_DisconnectOnAuthTimeout,
       "answerProfile-PppAnswer-BridgingGroup": answerProfile_PppAnswer_BridgingGroup,
       "answerProfile-PppAnswer-LinkCompression": answerProfile_PppAnswer_LinkCompression,
       "answerProfile-PppAnswer-Mru": answerProfile_PppAnswer_Mru,
       "answerProfile-PppAnswer-Lqm": answerProfile_PppAnswer_Lqm,
       "answerProfile-PppAnswer-LqmMinimumPeriod": answerProfile_PppAnswer_LqmMinimumPeriod,
       "answerProfile-PppAnswer-LqmMaximumPeriod": answerProfile_PppAnswer_LqmMaximumPeriod,
       "answerProfile-MpAnswer-Enabled": answerProfile_MpAnswer_Enabled,
       "answerProfile-MpAnswer-MinimumChannels": answerProfile_MpAnswer_MinimumChannels,
       "answerProfile-MpAnswer-MaximumChannels": answerProfile_MpAnswer_MaximumChannels,
       "answerProfile-MpAnswer-BacpEnable": answerProfile_MpAnswer_BacpEnable,
       "answerProfile-MppAnswer-Enabled": answerProfile_MppAnswer_Enabled,
       "answerProfile-MppAnswer-DynamicAlgorithm": answerProfile_MppAnswer_DynamicAlgorithm,
       "answerProfile-MppAnswer-BandwidthMonitorDirection": answerProfile_MppAnswer_BandwidthMonitorDirection,
       "answerProfile-MppAnswer-IncrementChannelCount": answerProfile_MppAnswer_IncrementChannelCount,
       "answerProfile-MppAnswer-DecrementChannelCount": answerProfile_MppAnswer_DecrementChannelCount,
       "answerProfile-MppAnswer-SecondsHistory": answerProfile_MppAnswer_SecondsHistory,
       "answerProfile-MppAnswer-AddPersistence": answerProfile_MppAnswer_AddPersistence,
       "answerProfile-MppAnswer-SubPersistence": answerProfile_MppAnswer_SubPersistence,
       "answerProfile-MppAnswer-TargetUtilization": answerProfile_MppAnswer_TargetUtilization,
       "answerProfile-FrAnswer-Enabled": answerProfile_FrAnswer_Enabled,
       "answerProfile-TcpClearAnswer-Enabled": answerProfile_TcpClearAnswer_Enabled,
       "answerProfile-AraAnswer-Enabled": answerProfile_AraAnswer_Enabled,
       "answerProfile-V120Answer-Enabled": answerProfile_V120Answer_Enabled,
       "answerProfile-V120Answer-FrameLength": answerProfile_V120Answer_FrameLength,
       "answerProfile-X25Answer-Enabled": answerProfile_X25Answer_Enabled,
       "answerProfile-X25Answer-X25Profile": answerProfile_X25Answer_X25Profile,
       "answerProfile-X25Answer-X3Profile": answerProfile_X25Answer_X3Profile,
       "answerProfile-X25Answer-MaxCalls": answerProfile_X25Answer_MaxCalls,
       "answerProfile-X25Answer-VcTimerEnable": answerProfile_X25Answer_VcTimerEnable,
       "answerProfile-X25Answer-AutoCallX121Address": answerProfile_X25Answer_AutoCallX121Address,
       "answerProfile-X25Answer-ReverseCharge": answerProfile_X25Answer_ReverseCharge,
       "answerProfile-X25Answer-X3CustomProf": answerProfile_X25Answer_X3CustomProf,
       "answerProfile-EuAnswer-EurawEnabled": answerProfile_EuAnswer_EurawEnabled,
       "answerProfile-EuAnswer-EuuiEnabled": answerProfile_EuAnswer_EuuiEnabled,
       "answerProfile-EuAnswer-DceAddr": answerProfile_EuAnswer_DceAddr,
       "answerProfile-EuAnswer-DteAddr": answerProfile_EuAnswer_DteAddr,
       "answerProfile-EuAnswer-Mru": answerProfile_EuAnswer_Mru,
       "answerProfile-IpAnswer-Enabled": answerProfile_IpAnswer_Enabled,
       "answerProfile-IpAnswer-VjHeaderPrediction": answerProfile_IpAnswer_VjHeaderPrediction,
       "answerProfile-IpAnswer-AssignAddress": answerProfile_IpAnswer_AssignAddress,
       "answerProfile-IpAnswer-RoutingMetric": answerProfile_IpAnswer_RoutingMetric,
       "answerProfile-IpxAnswer-Enabled": answerProfile_IpxAnswer_Enabled,
       "answerProfile-IpxAnswer-PeerMode": answerProfile_IpxAnswer_PeerMode,
       "answerProfile-SessionInfo-CallFilter": answerProfile_SessionInfo_CallFilter,
       "answerProfile-SessionInfo-DataFilter": answerProfile_SessionInfo_DataFilter,
       "answerProfile-SessionInfo-FilterPersistence": answerProfile_SessionInfo_FilterPersistence,
       "answerProfile-SessionInfo-IdleTimer": answerProfile_SessionInfo_IdleTimer,
       "answerProfile-SessionInfo-TsIdleMode": answerProfile_SessionInfo_TsIdleMode,
       "answerProfile-SessionInfo-TsIdleTimer": answerProfile_SessionInfo_TsIdleTimer,
       "answerProfile-SessionInfo-MaxCallDuration": answerProfile_SessionInfo_MaxCallDuration,
       "answerProfile-X75Answer-Enabled": answerProfile_X75Answer_Enabled,
       "answerProfile-X75Answer-KFramesOutstanding": answerProfile_X75Answer_KFramesOutstanding,
       "answerProfile-X75Answer-N2Retransmissions": answerProfile_X75Answer_N2Retransmissions,
       "answerProfile-X75Answer-T1RetranTimer": answerProfile_X75Answer_T1RetranTimer,
       "answerProfile-X75Answer-FrameLength": answerProfile_X75Answer_FrameLength,
       "answerProfile-FramedOnly": answerProfile_FramedOnly,
       "answerProfile-Action-o": answerProfile_Action_o,
       "answerProfile-PppAnswer-CbcpEnabled": answerProfile_PppAnswer_CbcpEnabled,
       "answerProfile-HdlcNrmAnswer-Enabled": answerProfile_HdlcNrmAnswer_Enabled,
       "answerProfile-Visa2Answer-Enabled": answerProfile_Visa2Answer_Enabled,
       "answerProfile-ClidSelection": answerProfile_ClidSelection,
       "answerProfile-PppAnswer-IpxHeaderCompression": answerProfile_PppAnswer_IpxHeaderCompression,
       "answerProfile-PppAnswer-Mtu": answerProfile_PppAnswer_Mtu,
       "answerProfile-IpAnswer-PrivateRouteProfileRequired": answerProfile_IpAnswer_PrivateRouteProfileRequired,
       "answerProfile-SessionInfo-FilterRequired": answerProfile_SessionInfo_FilterRequired,
       "answerProfile-AtmAnswer-SvcEnabled": answerProfile_AtmAnswer_SvcEnabled,
       "answerProfile-PppAnswer-BiDirectionalAuth": answerProfile_PppAnswer_BiDirectionalAuth,
       "answerProfile-PppAnswer-SubstituteSendName": answerProfile_PppAnswer_SubstituteSendName,
       "answerProfile-PppAnswer-AuthForAsyncFramedUsers": answerProfile_PppAnswer_AuthForAsyncFramedUsers,
       "answerProfile-PppAnswer-MaxPapAuthRetry": answerProfile_PppAnswer_MaxPapAuthRetry,
       "answerProfile-IpAnswer-PoolForAsyncFramedUser": answerProfile_IpAnswer_PoolForAsyncFramedUser,
       "answerProfile-CallbackClidPrefix": answerProfile_CallbackClidPrefix,
       "answerProfile-PriorityAnswer-PacketClassification": answerProfile_PriorityAnswer_PacketClassification,
       "answerProfile-PriorityAnswer-MaxRtpPacketDelay": answerProfile_PriorityAnswer_MaxRtpPacketDelay,
       "answerProfile-PriorityAnswer-MinimumRtpPort": answerProfile_PriorityAnswer_MinimumRtpPort,
       "answerProfile-PriorityAnswer-MaximumRtpPort": answerProfile_PriorityAnswer_MaximumRtpPort,
       "answerProfile-PriorityAnswer-NoHighPrioPktDuration": answerProfile_PriorityAnswer_NoHighPrioPktDuration,
       "answerProfile-PppAnswer-MaxPppConfigureRetry": answerProfile_PppAnswer_MaxPppConfigureRetry,
       "answerProfile-PppAnswer-PppRestartTimer": answerProfile_PppAnswer_PppRestartTimer,
       "answerProfile-PppAnswer-MaxPppRestartTimer": answerProfile_PppAnswer_MaxPppRestartTimer,
       "answerProfile-PriorityAnswer-Enabled": answerProfile_PriorityAnswer_Enabled}
)
