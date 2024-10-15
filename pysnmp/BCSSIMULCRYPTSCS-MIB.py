# SNMP MIB module (BCSSIMULCRYPTSCS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BCSSIMULCRYPTSCS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:29 2024
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

(bcs,) = mibBuilder.importSymbols(
    "BCS-IDENT-MIB",
    "bcs")

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

bcsSimulcryptScs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7)
)
bcsSimulcryptScs.setRevisions(
        ("2009-10-01 00:00",
         "2009-05-10 00:00",
         "2006-02-09 00:00",
         "2004-08-09 00:00",
         "2004-01-23 00:00")
)


# Types definitions



class ApplyDataToDeviceTYPE(Integer32):
    """Custom type ApplyDataToDeviceTYPE based on Integer32"""
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
        *(("apply", 2),
          ("applyNotInProgress", 1),
          ("applyNotInProgressInvalidData", 4),
          ("applyNotInProgressValidData", 3))
    )





class ManualSwitchBackTYPE(Integer32):
    """Custom type ManualSwitchBackTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manualSwitchBack", 2),
          ("manualSwitchBackNotInProgress", 1))
    )





class EnableDisableTYPE(Integer32):
    """Custom type EnableDisableTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcsSimScsConfig_ObjectIdentity = ObjectIdentity
bcsSimScsConfig = _BcsSimScsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1)
)
_BcsSimScsConfigGeneral_ObjectIdentity = ObjectIdentity
bcsSimScsConfigGeneral = _BcsSimScsConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1)
)
_BcsSimScsNetworkId_Type = Unsigned32
_BcsSimScsNetworkId_Object = MibScalar
bcsSimScsNetworkId = _BcsSimScsNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 1),
    _BcsSimScsNetworkId_Type()
)
bcsSimScsNetworkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsNetworkId.setStatus("current")
_BcsSimScsMaxNetworkDelay_Type = Unsigned32
_BcsSimScsMaxNetworkDelay_Object = MibScalar
bcsSimScsMaxNetworkDelay = _BcsSimScsMaxNetworkDelay_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 2),
    _BcsSimScsMaxNetworkDelay_Type()
)
bcsSimScsMaxNetworkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsMaxNetworkDelay.setStatus("current")
_BcsSimScsNominalCryptoPeriod_Type = Unsigned32
_BcsSimScsNominalCryptoPeriod_Object = MibScalar
bcsSimScsNominalCryptoPeriod = _BcsSimScsNominalCryptoPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 3),
    _BcsSimScsNominalCryptoPeriod_Type()
)
bcsSimScsNominalCryptoPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsNominalCryptoPeriod.setStatus("current")


class _BcsSimScsAccessCriteriaSource_Type(Integer32):
    """Custom type bcsSimScsAccessCriteriaSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dtviaFixedAc", 1),
          ("noAc", 2),
          ("serviceId", 3))
    )


_BcsSimScsAccessCriteriaSource_Type.__name__ = "Integer32"
_BcsSimScsAccessCriteriaSource_Object = MibScalar
bcsSimScsAccessCriteriaSource = _BcsSimScsAccessCriteriaSource_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 4),
    _BcsSimScsAccessCriteriaSource_Type()
)
bcsSimScsAccessCriteriaSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsAccessCriteriaSource.setStatus("current")
_BcsSimScsEcmgTimeout_Type = Unsigned32
_BcsSimScsEcmgTimeout_Object = MibScalar
bcsSimScsEcmgTimeout = _BcsSimScsEcmgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 5),
    _BcsSimScsEcmgTimeout_Type()
)
bcsSimScsEcmgTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmgTimeout.setStatus("current")
_BcsSimScsEcmIdInitial_Type = Unsigned32
_BcsSimScsEcmIdInitial_Object = MibScalar
bcsSimScsEcmIdInitial = _BcsSimScsEcmIdInitial_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 6),
    _BcsSimScsEcmIdInitial_Type()
)
bcsSimScsEcmIdInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmIdInitial.setStatus("current")
_BcsSimScsEcmChannelTestPeriodicity_Type = Unsigned32
_BcsSimScsEcmChannelTestPeriodicity_Object = MibScalar
bcsSimScsEcmChannelTestPeriodicity = _BcsSimScsEcmChannelTestPeriodicity_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 7),
    _BcsSimScsEcmChannelTestPeriodicity_Type()
)
bcsSimScsEcmChannelTestPeriodicity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmChannelTestPeriodicity.setStatus("current")
_BcsSimScsEcmNetworkDelay_Type = Unsigned32
_BcsSimScsEcmNetworkDelay_Object = MibScalar
bcsSimScsEcmNetworkDelay = _BcsSimScsEcmNetworkDelay_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 8),
    _BcsSimScsEcmNetworkDelay_Type()
)
bcsSimScsEcmNetworkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmNetworkDelay.setStatus("current")
_BcsSimScsEcmReplyTimeout_Type = Unsigned32
_BcsSimScsEcmReplyTimeout_Object = MibScalar
bcsSimScsEcmReplyTimeout = _BcsSimScsEcmReplyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 9),
    _BcsSimScsEcmReplyTimeout_Type()
)
bcsSimScsEcmReplyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmReplyTimeout.setStatus("current")
_BcsSimScsEcmgConnectionTable_Object = MibTable
bcsSimScsEcmgConnectionTable = _BcsSimScsEcmgConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2)
)
if mibBuilder.loadTexts:
    bcsSimScsEcmgConnectionTable.setStatus("current")
_BcsSimScsEcmgConnectionEntry_Object = MibTableRow
bcsSimScsEcmgConnectionEntry = _BcsSimScsEcmgConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1)
)
bcsSimScsEcmgConnectionEntry.setIndexNames(
    (0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsEcmgConnectIndex"),
)
if mibBuilder.loadTexts:
    bcsSimScsEcmgConnectionEntry.setStatus("current")
_BcsSimScsEcmgConnectIndex_Type = Integer32
_BcsSimScsEcmgConnectIndex_Object = MibTableColumn
bcsSimScsEcmgConnectIndex = _BcsSimScsEcmgConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 1),
    _BcsSimScsEcmgConnectIndex_Type()
)
bcsSimScsEcmgConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsSimScsEcmgConnectIndex.setStatus("current")
_BcsSimScsEcmgConnectEnabled_Type = EnableDisableTYPE
_BcsSimScsEcmgConnectEnabled_Object = MibTableColumn
bcsSimScsEcmgConnectEnabled = _BcsSimScsEcmgConnectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 2),
    _BcsSimScsEcmgConnectEnabled_Type()
)
bcsSimScsEcmgConnectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmgConnectEnabled.setStatus("current")
_BcsSimScsEcmgConnectSuperCasId_Type = Unsigned32
_BcsSimScsEcmgConnectSuperCasId_Object = MibTableColumn
bcsSimScsEcmgConnectSuperCasId = _BcsSimScsEcmgConnectSuperCasId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 3),
    _BcsSimScsEcmgConnectSuperCasId_Type()
)
bcsSimScsEcmgConnectSuperCasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmgConnectSuperCasId.setStatus("current")
_BcsSimScsEcmgConnectIpAddr_Type = IpAddress
_BcsSimScsEcmgConnectIpAddr_Object = MibTableColumn
bcsSimScsEcmgConnectIpAddr = _BcsSimScsEcmgConnectIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 4),
    _BcsSimScsEcmgConnectIpAddr_Type()
)
bcsSimScsEcmgConnectIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmgConnectIpAddr.setStatus("current")
_BcsSimScsEcmgConnectPort_Type = Integer32
_BcsSimScsEcmgConnectPort_Object = MibTableColumn
bcsSimScsEcmgConnectPort = _BcsSimScsEcmgConnectPort_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 5),
    _BcsSimScsEcmgConnectPort_Type()
)
bcsSimScsEcmgConnectPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmgConnectPort.setStatus("current")
_BcsSimScsEcmgRedundancyConfigTable_Object = MibTable
bcsSimScsEcmgRedundancyConfigTable = _BcsSimScsEcmgRedundancyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3)
)
if mibBuilder.loadTexts:
    bcsSimScsEcmgRedundancyConfigTable.setStatus("current")
_BcsSimScsEcmgRedundancyConfigEntry_Object = MibTableRow
bcsSimScsEcmgRedundancyConfigEntry = _BcsSimScsEcmgRedundancyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1)
)
bcsSimScsEcmgRedundancyConfigEntry.setIndexNames(
    (0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsEcmgRedundancyConfigIndex"),
)
if mibBuilder.loadTexts:
    bcsSimScsEcmgRedundancyConfigEntry.setStatus("current")


class _BcsSimScsEcmgRedundancyConfigIndex_Type(Integer32):
    """Custom type bcsSimScsEcmgRedundancyConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BcsSimScsEcmgRedundancyConfigIndex_Type.__name__ = "Integer32"
_BcsSimScsEcmgRedundancyConfigIndex_Object = MibTableColumn
bcsSimScsEcmgRedundancyConfigIndex = _BcsSimScsEcmgRedundancyConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1, 1),
    _BcsSimScsEcmgRedundancyConfigIndex_Type()
)
bcsSimScsEcmgRedundancyConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsSimScsEcmgRedundancyConfigIndex.setStatus("current")
_BcsSimScsEcmgRedundancyConfigAutoSwitchBack_Type = EnableDisableTYPE
_BcsSimScsEcmgRedundancyConfigAutoSwitchBack_Object = MibTableColumn
bcsSimScsEcmgRedundancyConfigAutoSwitchBack = _BcsSimScsEcmgRedundancyConfigAutoSwitchBack_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1, 2),
    _BcsSimScsEcmgRedundancyConfigAutoSwitchBack_Type()
)
bcsSimScsEcmgRedundancyConfigAutoSwitchBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmgRedundancyConfigAutoSwitchBack.setStatus("current")
_BcsSimScsEcmgRedundancyConfigManualSwitchBack_Type = ManualSwitchBackTYPE
_BcsSimScsEcmgRedundancyConfigManualSwitchBack_Object = MibTableColumn
bcsSimScsEcmgRedundancyConfigManualSwitchBack = _BcsSimScsEcmgRedundancyConfigManualSwitchBack_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1, 3),
    _BcsSimScsEcmgRedundancyConfigManualSwitchBack_Type()
)
bcsSimScsEcmgRedundancyConfigManualSwitchBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmgRedundancyConfigManualSwitchBack.setStatus("current")


class _BcsSimScsEcmgRedundancyConfigMaxStreams_Type(Integer32):
    """Custom type bcsSimScsEcmgRedundancyConfigMaxStreams based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_BcsSimScsEcmgRedundancyConfigMaxStreams_Type.__name__ = "Integer32"
_BcsSimScsEcmgRedundancyConfigMaxStreams_Object = MibTableColumn
bcsSimScsEcmgRedundancyConfigMaxStreams = _BcsSimScsEcmgRedundancyConfigMaxStreams_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1, 4),
    _BcsSimScsEcmgRedundancyConfigMaxStreams_Type()
)
bcsSimScsEcmgRedundancyConfigMaxStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmgRedundancyConfigMaxStreams.setStatus("current")
_BcsSimScsEcmgRedundancyConfigApplyTable_Object = MibTable
bcsSimScsEcmgRedundancyConfigApplyTable = _BcsSimScsEcmgRedundancyConfigApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 4)
)
if mibBuilder.loadTexts:
    bcsSimScsEcmgRedundancyConfigApplyTable.setStatus("current")
_BcsSimScsEcmgRedundancyConfigApplyEntry_Object = MibTableRow
bcsSimScsEcmgRedundancyConfigApplyEntry = _BcsSimScsEcmgRedundancyConfigApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 4, 1)
)
bcsSimScsEcmgRedundancyConfigApplyEntry.setIndexNames(
    (0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsEcmgRedundancyConfigApplyIndex"),
)
if mibBuilder.loadTexts:
    bcsSimScsEcmgRedundancyConfigApplyEntry.setStatus("current")


class _BcsSimScsEcmgRedundancyConfigApplyIndex_Type(Integer32):
    """Custom type bcsSimScsEcmgRedundancyConfigApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BcsSimScsEcmgRedundancyConfigApplyIndex_Type.__name__ = "Integer32"
_BcsSimScsEcmgRedundancyConfigApplyIndex_Object = MibTableColumn
bcsSimScsEcmgRedundancyConfigApplyIndex = _BcsSimScsEcmgRedundancyConfigApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 4, 1, 1),
    _BcsSimScsEcmgRedundancyConfigApplyIndex_Type()
)
bcsSimScsEcmgRedundancyConfigApplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsSimScsEcmgRedundancyConfigApplyIndex.setStatus("current")
_BcsSimScsEcmgRedundancyConfigApplyChange_Type = ApplyDataToDeviceTYPE
_BcsSimScsEcmgRedundancyConfigApplyChange_Object = MibTableColumn
bcsSimScsEcmgRedundancyConfigApplyChange = _BcsSimScsEcmgRedundancyConfigApplyChange_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 4, 1, 2),
    _BcsSimScsEcmgRedundancyConfigApplyChange_Type()
)
bcsSimScsEcmgRedundancyConfigApplyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcsSimScsEcmgRedundancyConfigApplyChange.setStatus("current")
_BcsSimScsStatus_ObjectIdentity = ObjectIdentity
bcsSimScsStatus = _BcsSimScsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2)
)
_BcsSimScsStatusGeneral_ObjectIdentity = ObjectIdentity
bcsSimScsStatusGeneral = _BcsSimScsStatusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1)
)


class _BcsSimScsMibSupportStatus_Type(Integer32):
    """Custom type bcsSimScsMibSupportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("capable", 2),
          ("enabled", 3),
          ("notCapable", 1))
    )


_BcsSimScsMibSupportStatus_Type.__name__ = "Integer32"
_BcsSimScsMibSupportStatus_Object = MibScalar
bcsSimScsMibSupportStatus = _BcsSimScsMibSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 1),
    _BcsSimScsMibSupportStatus_Type()
)
bcsSimScsMibSupportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsMibSupportStatus.setStatus("current")
_BcsSimScsMaxEcmg_Type = Unsigned32
_BcsSimScsMaxEcmg_Object = MibScalar
bcsSimScsMaxEcmg = _BcsSimScsMaxEcmg_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 2),
    _BcsSimScsMaxEcmg_Type()
)
bcsSimScsMaxEcmg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsMaxEcmg.setStatus("current")
_BcsSimScsMaxPrograms_Type = Unsigned32
_BcsSimScsMaxPrograms_Object = MibScalar
bcsSimScsMaxPrograms = _BcsSimScsMaxPrograms_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 3),
    _BcsSimScsMaxPrograms_Type()
)
bcsSimScsMaxPrograms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsMaxPrograms.setStatus("current")
_BcsSimScsMaxProgramEcmg_Type = Unsigned32
_BcsSimScsMaxProgramEcmg_Object = MibScalar
bcsSimScsMaxProgramEcmg = _BcsSimScsMaxProgramEcmg_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 4),
    _BcsSimScsMaxProgramEcmg_Type()
)
bcsSimScsMaxProgramEcmg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsMaxProgramEcmg.setStatus("current")


class _BcsSimScsEcmgRedundancyConfigInvalidApplyText_Type(DisplayString):
    """Custom type bcsSimScsEcmgRedundancyConfigInvalidApplyText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BcsSimScsEcmgRedundancyConfigInvalidApplyText_Type.__name__ = "DisplayString"
_BcsSimScsEcmgRedundancyConfigInvalidApplyText_Object = MibScalar
bcsSimScsEcmgRedundancyConfigInvalidApplyText = _BcsSimScsEcmgRedundancyConfigInvalidApplyText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 5),
    _BcsSimScsEcmgRedundancyConfigInvalidApplyText_Type()
)
bcsSimScsEcmgRedundancyConfigInvalidApplyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsEcmgRedundancyConfigInvalidApplyText.setStatus("current")
_BcsSimScsEcmgStatusTable_Object = MibTable
bcsSimScsEcmgStatusTable = _BcsSimScsEcmgStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2)
)
if mibBuilder.loadTexts:
    bcsSimScsEcmgStatusTable.setStatus("current")
_BcsSimScsEcmgStatusEntry_Object = MibTableRow
bcsSimScsEcmgStatusEntry = _BcsSimScsEcmgStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1)
)
bcsSimScsEcmgStatusEntry.setIndexNames(
    (0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsEcmgStatusIndex"),
)
if mibBuilder.loadTexts:
    bcsSimScsEcmgStatusEntry.setStatus("current")
_BcsSimScsEcmgStatusIndex_Type = Integer32
_BcsSimScsEcmgStatusIndex_Object = MibTableColumn
bcsSimScsEcmgStatusIndex = _BcsSimScsEcmgStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 1),
    _BcsSimScsEcmgStatusIndex_Type()
)
bcsSimScsEcmgStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsSimScsEcmgStatusIndex.setStatus("current")


class _BcsSimScsEcmgTcpState_Type(Integer32):
    """Custom type bcsSimScsEcmgTcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("error", 3),
          ("open", 1))
    )


_BcsSimScsEcmgTcpState_Type.__name__ = "Integer32"
_BcsSimScsEcmgTcpState_Object = MibTableColumn
bcsSimScsEcmgTcpState = _BcsSimScsEcmgTcpState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 2),
    _BcsSimScsEcmgTcpState_Type()
)
bcsSimScsEcmgTcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsEcmgTcpState.setStatus("current")
_BcsSimScsEcmgChannelId_Type = Unsigned32
_BcsSimScsEcmgChannelId_Object = MibTableColumn
bcsSimScsEcmgChannelId = _BcsSimScsEcmgChannelId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 3),
    _BcsSimScsEcmgChannelId_Type()
)
bcsSimScsEcmgChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsEcmgChannelId.setStatus("current")


class _BcsSimScsEcmgChannelState_Type(Integer32):
    """Custom type bcsSimScsEcmgChannelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("notOpen", 2),
          ("open", 1))
    )


_BcsSimScsEcmgChannelState_Type.__name__ = "Integer32"
_BcsSimScsEcmgChannelState_Object = MibTableColumn
bcsSimScsEcmgChannelState = _BcsSimScsEcmgChannelState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 4),
    _BcsSimScsEcmgChannelState_Type()
)
bcsSimScsEcmgChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsEcmgChannelState.setStatus("current")
_BcsSimScsEcmgSuperCasId_Type = Unsigned32
_BcsSimScsEcmgSuperCasId_Object = MibTableColumn
bcsSimScsEcmgSuperCasId = _BcsSimScsEcmgSuperCasId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 5),
    _BcsSimScsEcmgSuperCasId_Type()
)
bcsSimScsEcmgSuperCasId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsEcmgSuperCasId.setStatus("current")
_BcsSimScsProgramTable_Object = MibTable
bcsSimScsProgramTable = _BcsSimScsProgramTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3)
)
if mibBuilder.loadTexts:
    bcsSimScsProgramTable.setStatus("current")
_BcsSimScsProgramEntry_Object = MibTableRow
bcsSimScsProgramEntry = _BcsSimScsProgramEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1)
)
bcsSimScsProgramEntry.setIndexNames(
    (0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsProgramIndex"),
    (0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsProgramEcmgIndex"),
)
if mibBuilder.loadTexts:
    bcsSimScsProgramEntry.setStatus("current")
_BcsSimScsProgramIndex_Type = Integer32
_BcsSimScsProgramIndex_Object = MibTableColumn
bcsSimScsProgramIndex = _BcsSimScsProgramIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 1),
    _BcsSimScsProgramIndex_Type()
)
bcsSimScsProgramIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsSimScsProgramIndex.setStatus("current")
_BcsSimScsProgramEcmgIndex_Type = Integer32
_BcsSimScsProgramEcmgIndex_Object = MibTableColumn
bcsSimScsProgramEcmgIndex = _BcsSimScsProgramEcmgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 2),
    _BcsSimScsProgramEcmgIndex_Type()
)
bcsSimScsProgramEcmgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcsSimScsProgramEcmgIndex.setStatus("current")


class _BcsSimScsProgramState_Type(Integer32):
    """Custom type bcsSimScsProgramState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eventRunning", 2),
          ("noEventRunning", 1),
          ("notConfigured", 3))
    )


_BcsSimScsProgramState_Type.__name__ = "Integer32"
_BcsSimScsProgramState_Object = MibTableColumn
bcsSimScsProgramState = _BcsSimScsProgramState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 3),
    _BcsSimScsProgramState_Type()
)
bcsSimScsProgramState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsProgramState.setStatus("current")
_BcsSimScsProgramCryptoPeriod_Type = Unsigned32
_BcsSimScsProgramCryptoPeriod_Object = MibTableColumn
bcsSimScsProgramCryptoPeriod = _BcsSimScsProgramCryptoPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 4),
    _BcsSimScsProgramCryptoPeriod_Type()
)
bcsSimScsProgramCryptoPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsProgramCryptoPeriod.setStatus("current")
_BcsSimScsProgramChannelId_Type = Unsigned32
_BcsSimScsProgramChannelId_Object = MibTableColumn
bcsSimScsProgramChannelId = _BcsSimScsProgramChannelId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 5),
    _BcsSimScsProgramChannelId_Type()
)
bcsSimScsProgramChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsProgramChannelId.setStatus("current")
_BcsSimScsProgramEcmgSuperCasId_Type = Unsigned32
_BcsSimScsProgramEcmgSuperCasId_Object = MibTableColumn
bcsSimScsProgramEcmgSuperCasId = _BcsSimScsProgramEcmgSuperCasId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 6),
    _BcsSimScsProgramEcmgSuperCasId_Type()
)
bcsSimScsProgramEcmgSuperCasId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsProgramEcmgSuperCasId.setStatus("current")


class _BcsSimScsProgramEcmgStreamState_Type(Integer32):
    """Custom type bcsSimScsProgramEcmgStreamState based on Integer32"""
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
        *(("closed", 2),
          ("ecmTimeout", 6),
          ("error", 3),
          ("invalidCasId", 5),
          ("notConfigured", 4),
          ("open", 1))
    )


_BcsSimScsProgramEcmgStreamState_Type.__name__ = "Integer32"
_BcsSimScsProgramEcmgStreamState_Object = MibTableColumn
bcsSimScsProgramEcmgStreamState = _BcsSimScsProgramEcmgStreamState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 7),
    _BcsSimScsProgramEcmgStreamState_Type()
)
bcsSimScsProgramEcmgStreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcsSimScsProgramEcmgStreamState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCSSIMULCRYPTSCS-MIB",
    **{"ApplyDataToDeviceTYPE": ApplyDataToDeviceTYPE,
       "ManualSwitchBackTYPE": ManualSwitchBackTYPE,
       "EnableDisableTYPE": EnableDisableTYPE,
       "bcsSimulcryptScs": bcsSimulcryptScs,
       "bcsSimScsConfig": bcsSimScsConfig,
       "bcsSimScsConfigGeneral": bcsSimScsConfigGeneral,
       "bcsSimScsNetworkId": bcsSimScsNetworkId,
       "bcsSimScsMaxNetworkDelay": bcsSimScsMaxNetworkDelay,
       "bcsSimScsNominalCryptoPeriod": bcsSimScsNominalCryptoPeriod,
       "bcsSimScsAccessCriteriaSource": bcsSimScsAccessCriteriaSource,
       "bcsSimScsEcmgTimeout": bcsSimScsEcmgTimeout,
       "bcsSimScsEcmIdInitial": bcsSimScsEcmIdInitial,
       "bcsSimScsEcmChannelTestPeriodicity": bcsSimScsEcmChannelTestPeriodicity,
       "bcsSimScsEcmNetworkDelay": bcsSimScsEcmNetworkDelay,
       "bcsSimScsEcmReplyTimeout": bcsSimScsEcmReplyTimeout,
       "bcsSimScsEcmgConnectionTable": bcsSimScsEcmgConnectionTable,
       "bcsSimScsEcmgConnectionEntry": bcsSimScsEcmgConnectionEntry,
       "bcsSimScsEcmgConnectIndex": bcsSimScsEcmgConnectIndex,
       "bcsSimScsEcmgConnectEnabled": bcsSimScsEcmgConnectEnabled,
       "bcsSimScsEcmgConnectSuperCasId": bcsSimScsEcmgConnectSuperCasId,
       "bcsSimScsEcmgConnectIpAddr": bcsSimScsEcmgConnectIpAddr,
       "bcsSimScsEcmgConnectPort": bcsSimScsEcmgConnectPort,
       "bcsSimScsEcmgRedundancyConfigTable": bcsSimScsEcmgRedundancyConfigTable,
       "bcsSimScsEcmgRedundancyConfigEntry": bcsSimScsEcmgRedundancyConfigEntry,
       "bcsSimScsEcmgRedundancyConfigIndex": bcsSimScsEcmgRedundancyConfigIndex,
       "bcsSimScsEcmgRedundancyConfigAutoSwitchBack": bcsSimScsEcmgRedundancyConfigAutoSwitchBack,
       "bcsSimScsEcmgRedundancyConfigManualSwitchBack": bcsSimScsEcmgRedundancyConfigManualSwitchBack,
       "bcsSimScsEcmgRedundancyConfigMaxStreams": bcsSimScsEcmgRedundancyConfigMaxStreams,
       "bcsSimScsEcmgRedundancyConfigApplyTable": bcsSimScsEcmgRedundancyConfigApplyTable,
       "bcsSimScsEcmgRedundancyConfigApplyEntry": bcsSimScsEcmgRedundancyConfigApplyEntry,
       "bcsSimScsEcmgRedundancyConfigApplyIndex": bcsSimScsEcmgRedundancyConfigApplyIndex,
       "bcsSimScsEcmgRedundancyConfigApplyChange": bcsSimScsEcmgRedundancyConfigApplyChange,
       "bcsSimScsStatus": bcsSimScsStatus,
       "bcsSimScsStatusGeneral": bcsSimScsStatusGeneral,
       "bcsSimScsMibSupportStatus": bcsSimScsMibSupportStatus,
       "bcsSimScsMaxEcmg": bcsSimScsMaxEcmg,
       "bcsSimScsMaxPrograms": bcsSimScsMaxPrograms,
       "bcsSimScsMaxProgramEcmg": bcsSimScsMaxProgramEcmg,
       "bcsSimScsEcmgRedundancyConfigInvalidApplyText": bcsSimScsEcmgRedundancyConfigInvalidApplyText,
       "bcsSimScsEcmgStatusTable": bcsSimScsEcmgStatusTable,
       "bcsSimScsEcmgStatusEntry": bcsSimScsEcmgStatusEntry,
       "bcsSimScsEcmgStatusIndex": bcsSimScsEcmgStatusIndex,
       "bcsSimScsEcmgTcpState": bcsSimScsEcmgTcpState,
       "bcsSimScsEcmgChannelId": bcsSimScsEcmgChannelId,
       "bcsSimScsEcmgChannelState": bcsSimScsEcmgChannelState,
       "bcsSimScsEcmgSuperCasId": bcsSimScsEcmgSuperCasId,
       "bcsSimScsProgramTable": bcsSimScsProgramTable,
       "bcsSimScsProgramEntry": bcsSimScsProgramEntry,
       "bcsSimScsProgramIndex": bcsSimScsProgramIndex,
       "bcsSimScsProgramEcmgIndex": bcsSimScsProgramEcmgIndex,
       "bcsSimScsProgramState": bcsSimScsProgramState,
       "bcsSimScsProgramCryptoPeriod": bcsSimScsProgramCryptoPeriod,
       "bcsSimScsProgramChannelId": bcsSimScsProgramChannelId,
       "bcsSimScsProgramEcmgSuperCasId": bcsSimScsProgramEcmgSuperCasId,
       "bcsSimScsProgramEcmgStreamState": bcsSimScsProgramEcmgStreamState}
)
