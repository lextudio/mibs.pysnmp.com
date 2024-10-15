# SNMP MIB module (AISLCSYSCFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISLCSYSCFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:22 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aiSLCSysCfg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 21)
)


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)


class _AislcscSystemPrompt_Type(DisplayString):
    """Custom type aislcscSystemPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcscSystemPrompt_Type.__name__ = "DisplayString"
_AislcscSystemPrompt_Object = MibScalar
aislcscSystemPrompt = _AislcscSystemPrompt_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 1),
    _AislcscSystemPrompt_Type()
)
aislcscSystemPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscSystemPrompt.setStatus("current")


class _AislcscShellMinLogLevel_Type(Integer32):
    """Custom type aislcscShellMinLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AislcscShellMinLogLevel_Type.__name__ = "Integer32"
_AislcscShellMinLogLevel_Object = MibScalar
aislcscShellMinLogLevel = _AislcscShellMinLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 2),
    _AislcscShellMinLogLevel_Type()
)
aislcscShellMinLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscShellMinLogLevel.setStatus("current")


class _AislcscFtpPort_Type(Integer32):
    """Custom type aislcscFtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AislcscFtpPort_Type.__name__ = "Integer32"
_AislcscFtpPort_Object = MibScalar
aislcscFtpPort = _AislcscFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 3),
    _AislcscFtpPort_Type()
)
aislcscFtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscFtpPort.setStatus("current")


class _AislcscTelnetPort_Type(Integer32):
    """Custom type aislcscTelnetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AislcscTelnetPort_Type.__name__ = "Integer32"
_AislcscTelnetPort_Object = MibScalar
aislcscTelnetPort = _AislcscTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 4),
    _AislcscTelnetPort_Type()
)
aislcscTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscTelnetPort.setStatus("current")
_AiSLCSysCfgManagerTable_Object = MibTable
aiSLCSysCfgManagerTable = _AiSLCSysCfgManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 5)
)
if mibBuilder.loadTexts:
    aiSLCSysCfgManagerTable.setStatus("current")
_AiSLCSysCfgManagerEntry_Object = MibTableRow
aiSLCSysCfgManagerEntry = _AiSLCSysCfgManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 5, 1)
)
aiSLCSysCfgManagerEntry.setIndexNames(
    (0, "AISLCSYSCFG-MIB", "aislcscManagerIndex"),
)
if mibBuilder.loadTexts:
    aiSLCSysCfgManagerEntry.setStatus("current")
_AislcscManagerIndex_Type = PositiveInteger
_AislcscManagerIndex_Object = MibTableColumn
aislcscManagerIndex = _AislcscManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 5, 1, 1),
    _AislcscManagerIndex_Type()
)
aislcscManagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcscManagerIndex.setStatus("current")
_AislcscManagerAddress_Type = IpAddress
_AislcscManagerAddress_Object = MibTableColumn
aislcscManagerAddress = _AislcscManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 5, 1, 2),
    _AislcscManagerAddress_Type()
)
aislcscManagerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscManagerAddress.setStatus("current")


class _AislcscManagerTrapPort_Type(Integer32):
    """Custom type aislcscManagerTrapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AislcscManagerTrapPort_Type.__name__ = "Integer32"
_AislcscManagerTrapPort_Object = MibTableColumn
aislcscManagerTrapPort = _AislcscManagerTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 5, 1, 3),
    _AislcscManagerTrapPort_Type()
)
aislcscManagerTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscManagerTrapPort.setStatus("current")


class _AislcscReadCommunity_Type(DisplayString):
    """Custom type aislcscReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AislcscReadCommunity_Type.__name__ = "DisplayString"
_AislcscReadCommunity_Object = MibScalar
aislcscReadCommunity = _AislcscReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 6),
    _AislcscReadCommunity_Type()
)
aislcscReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscReadCommunity.setStatus("current")


class _AislcscWriteCommunity_Type(DisplayString):
    """Custom type aislcscWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AislcscWriteCommunity_Type.__name__ = "DisplayString"
_AislcscWriteCommunity_Object = MibScalar
aislcscWriteCommunity = _AislcscWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 7),
    _AislcscWriteCommunity_Type()
)
aislcscWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscWriteCommunity.setStatus("current")


class _Aislcsctl1SourceID_Type(DisplayString):
    """Custom type aislcsctl1SourceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Aislcsctl1SourceID_Type.__name__ = "DisplayString"
_Aislcsctl1SourceID_Object = MibScalar
aislcsctl1SourceID = _Aislcsctl1SourceID_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 8),
    _Aislcsctl1SourceID_Type()
)
aislcsctl1SourceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcsctl1SourceID.setStatus("current")
_Aislcsctl1LogonRequired_Type = TruthValue
_Aislcsctl1LogonRequired_Object = MibScalar
aislcsctl1LogonRequired = _Aislcsctl1LogonRequired_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 9),
    _Aislcsctl1LogonRequired_Type()
)
aislcsctl1LogonRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcsctl1LogonRequired.setStatus("current")
_Aislcsctl1NumBadLogons_Type = PositiveInteger
_Aislcsctl1NumBadLogons_Object = MibScalar
aislcsctl1NumBadLogons = _Aislcsctl1NumBadLogons_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 10),
    _Aislcsctl1NumBadLogons_Type()
)
aislcsctl1NumBadLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcsctl1NumBadLogons.setStatus("current")


class _AislcscExtProbeStatus_Type(Integer32):
    """Custom type aislcscExtProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_AislcscExtProbeStatus_Type.__name__ = "Integer32"
_AislcscExtProbeStatus_Object = MibScalar
aislcscExtProbeStatus = _AislcscExtProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 11),
    _AislcscExtProbeStatus_Type()
)
aislcscExtProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcscExtProbeStatus.setStatus("current")


class _AislcscExtLowThreshCelsius_Type(Integer32):
    """Custom type aislcscExtLowThreshCelsius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-54, 124),
    )


_AislcscExtLowThreshCelsius_Type.__name__ = "Integer32"
_AislcscExtLowThreshCelsius_Object = MibScalar
aislcscExtLowThreshCelsius = _AislcscExtLowThreshCelsius_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 12),
    _AislcscExtLowThreshCelsius_Type()
)
aislcscExtLowThreshCelsius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscExtLowThreshCelsius.setStatus("current")
if mibBuilder.loadTexts:
    aislcscExtLowThreshCelsius.setUnits("degrees Celsius")


class _AislcscExtHighThreshCelsius_Type(Integer32):
    """Custom type aislcscExtHighThreshCelsius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-54, 124),
    )


_AislcscExtHighThreshCelsius_Type.__name__ = "Integer32"
_AislcscExtHighThreshCelsius_Object = MibScalar
aislcscExtHighThreshCelsius = _AislcscExtHighThreshCelsius_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 13),
    _AislcscExtHighThreshCelsius_Type()
)
aislcscExtHighThreshCelsius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscExtHighThreshCelsius.setStatus("current")
if mibBuilder.loadTexts:
    aislcscExtHighThreshCelsius.setUnits("degrees Celsius")


class _AislcscExtTempCelsius_Type(Integer32):
    """Custom type aislcscExtTempCelsius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-55, 125),
    )


_AislcscExtTempCelsius_Type.__name__ = "Integer32"
_AislcscExtTempCelsius_Object = MibScalar
aislcscExtTempCelsius = _AislcscExtTempCelsius_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 14),
    _AislcscExtTempCelsius_Type()
)
aislcscExtTempCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcscExtTempCelsius.setStatus("current")
if mibBuilder.loadTexts:
    aislcscExtTempCelsius.setUnits("degrees Celsius")


class _AislcscIntProbeStatus_Type(Integer32):
    """Custom type aislcscIntProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_AislcscIntProbeStatus_Type.__name__ = "Integer32"
_AislcscIntProbeStatus_Object = MibScalar
aislcscIntProbeStatus = _AislcscIntProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 15),
    _AislcscIntProbeStatus_Type()
)
aislcscIntProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcscIntProbeStatus.setStatus("current")


class _AislcscIntLowThreshCelsius_Type(Integer32):
    """Custom type aislcscIntLowThreshCelsius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-54, 124),
    )


_AislcscIntLowThreshCelsius_Type.__name__ = "Integer32"
_AislcscIntLowThreshCelsius_Object = MibScalar
aislcscIntLowThreshCelsius = _AislcscIntLowThreshCelsius_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 16),
    _AislcscIntLowThreshCelsius_Type()
)
aislcscIntLowThreshCelsius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscIntLowThreshCelsius.setStatus("current")
if mibBuilder.loadTexts:
    aislcscIntLowThreshCelsius.setUnits("degrees Celsius")


class _AislcscIntHighThreshCelsius_Type(Integer32):
    """Custom type aislcscIntHighThreshCelsius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-54, 124),
    )


_AislcscIntHighThreshCelsius_Type.__name__ = "Integer32"
_AislcscIntHighThreshCelsius_Object = MibScalar
aislcscIntHighThreshCelsius = _AislcscIntHighThreshCelsius_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 17),
    _AislcscIntHighThreshCelsius_Type()
)
aislcscIntHighThreshCelsius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscIntHighThreshCelsius.setStatus("current")
if mibBuilder.loadTexts:
    aislcscIntHighThreshCelsius.setUnits("degrees Celsius")


class _AislcscIntTempCelsius_Type(Integer32):
    """Custom type aislcscIntTempCelsius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-55, 125),
    )


_AislcscIntTempCelsius_Type.__name__ = "Integer32"
_AislcscIntTempCelsius_Object = MibScalar
aislcscIntTempCelsius = _AislcscIntTempCelsius_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 18),
    _AislcscIntTempCelsius_Type()
)
aislcscIntTempCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcscIntTempCelsius.setStatus("current")
if mibBuilder.loadTexts:
    aislcscIntTempCelsius.setUnits("degrees Celsius")


class _AislcscExceededThresholdValue_Type(Integer32):
    """Custom type aislcscExceededThresholdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-55, 125),
    )


_AislcscExceededThresholdValue_Type.__name__ = "Integer32"
_AislcscExceededThresholdValue_Object = MibScalar
aislcscExceededThresholdValue = _AislcscExceededThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 19),
    _AislcscExceededThresholdValue_Type()
)
aislcscExceededThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcscExceededThresholdValue.setStatus("current")
if mibBuilder.loadTexts:
    aislcscExceededThresholdValue.setUnits("degrees Celsius")
_AiSLCSysCfgKeepAliveTable_Object = MibTable
aiSLCSysCfgKeepAliveTable = _AiSLCSysCfgKeepAliveTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 20)
)
if mibBuilder.loadTexts:
    aiSLCSysCfgKeepAliveTable.setStatus("current")
_AiSLCSysCfgKeepAliveEntry_Object = MibTableRow
aiSLCSysCfgKeepAliveEntry = _AiSLCSysCfgKeepAliveEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 20, 1)
)
aiSLCSysCfgKeepAliveEntry.setIndexNames(
    (0, "AISLCSYSCFG-MIB", "aislcscKeepAliveIndex"),
)
if mibBuilder.loadTexts:
    aiSLCSysCfgKeepAliveEntry.setStatus("current")
_AislcscKeepAliveIndex_Type = PositiveInteger
_AislcscKeepAliveIndex_Object = MibTableColumn
aislcscKeepAliveIndex = _AislcscKeepAliveIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 20, 1, 1),
    _AislcscKeepAliveIndex_Type()
)
aislcscKeepAliveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcscKeepAliveIndex.setStatus("current")
_AislcscKeepAliveAddress_Type = IpAddress
_AislcscKeepAliveAddress_Object = MibTableColumn
aislcscKeepAliveAddress = _AislcscKeepAliveAddress_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 20, 1, 2),
    _AislcscKeepAliveAddress_Type()
)
aislcscKeepAliveAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscKeepAliveAddress.setStatus("current")


class _AislcscKeepAliveInterval_Type(Integer32):
    """Custom type aislcscKeepAliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_AislcscKeepAliveInterval_Type.__name__ = "Integer32"
_AislcscKeepAliveInterval_Object = MibTableColumn
aislcscKeepAliveInterval = _AislcscKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 20, 1, 3),
    _AislcscKeepAliveInterval_Type()
)
aislcscKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    aislcscKeepAliveInterval.setUnits("seconds")


class _AislcscKeepAliveWarningText_Type(DisplayString):
    """Custom type aislcscKeepAliveWarningText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AislcscKeepAliveWarningText_Type.__name__ = "DisplayString"
_AislcscKeepAliveWarningText_Object = MibTableColumn
aislcscKeepAliveWarningText = _AislcscKeepAliveWarningText_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 20, 1, 4),
    _AislcscKeepAliveWarningText_Type()
)
aislcscKeepAliveWarningText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscKeepAliveWarningText.setStatus("current")


class _AislcscKeepAliveOKText_Type(DisplayString):
    """Custom type aislcscKeepAliveOKText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AislcscKeepAliveOKText_Type.__name__ = "DisplayString"
_AislcscKeepAliveOKText_Object = MibTableColumn
aislcscKeepAliveOKText = _AislcscKeepAliveOKText_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 20, 1, 5),
    _AislcscKeepAliveOKText_Type()
)
aislcscKeepAliveOKText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscKeepAliveOKText.setStatus("current")


class _AislcscKeepAliveCommStat_Type(Integer32):
    """Custom type aislcscKeepAliveCommStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("lost", 3),
          ("ok", 2))
    )


_AislcscKeepAliveCommStat_Type.__name__ = "Integer32"
_AislcscKeepAliveCommStat_Object = MibTableColumn
aislcscKeepAliveCommStat = _AislcscKeepAliveCommStat_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 20, 1, 6),
    _AislcscKeepAliveCommStat_Type()
)
aislcscKeepAliveCommStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcscKeepAliveCommStat.setStatus("current")


class _AislcscActiveConfigName_Type(DisplayString):
    """Custom type aislcscActiveConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AislcscActiveConfigName_Type.__name__ = "DisplayString"
_AislcscActiveConfigName_Object = MibScalar
aislcscActiveConfigName = _AislcscActiveConfigName_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 21),
    _AislcscActiveConfigName_Type()
)
aislcscActiveConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscActiveConfigName.setStatus("current")


class _AislcscActiveConfigCRC_Type(Integer32):
    """Custom type aislcscActiveConfigCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AislcscActiveConfigCRC_Type.__name__ = "Integer32"
_AislcscActiveConfigCRC_Object = MibScalar
aislcscActiveConfigCRC = _AislcscActiveConfigCRC_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 22),
    _AislcscActiveConfigCRC_Type()
)
aislcscActiveConfigCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcscActiveConfigCRC.setStatus("current")


class _AislcscSoftwareUpdateName_Type(DisplayString):
    """Custom type aislcscSoftwareUpdateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AislcscSoftwareUpdateName_Type.__name__ = "DisplayString"
_AislcscSoftwareUpdateName_Object = MibScalar
aislcscSoftwareUpdateName = _AislcscSoftwareUpdateName_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 23),
    _AislcscSoftwareUpdateName_Type()
)
aislcscSoftwareUpdateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscSoftwareUpdateName.setStatus("current")


class _AislcscSoftwareUpdateStatus_Type(Integer32):
    """Custom type aislcscSoftwareUpdateStatus based on Integer32"""
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
        *(("error", 4),
          ("inProgress", 2),
          ("ok", 3),
          ("ready", 1))
    )


_AislcscSoftwareUpdateStatus_Type.__name__ = "Integer32"
_AislcscSoftwareUpdateStatus_Object = MibScalar
aislcscSoftwareUpdateStatus = _AislcscSoftwareUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 24),
    _AislcscSoftwareUpdateStatus_Type()
)
aislcscSoftwareUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscSoftwareUpdateStatus.setStatus("current")


class _AislcscResetSystem_Type(Integer32):
    """Custom type aislcscResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coldStart", 2),
          ("none", 1))
    )


_AislcscResetSystem_Type.__name__ = "Integer32"
_AislcscResetSystem_Object = MibScalar
aislcscResetSystem = _AislcscResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 25),
    _AislcscResetSystem_Type()
)
aislcscResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscResetSystem.setStatus("current")


class _AislcscDiscPowerSupplyStatus_Type(Integer32):
    """Custom type aislcscDiscPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("okay", 1),
          ("trouble", 2))
    )


_AislcscDiscPowerSupplyStatus_Type.__name__ = "Integer32"
_AislcscDiscPowerSupplyStatus_Object = MibScalar
aislcscDiscPowerSupplyStatus = _AislcscDiscPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 26),
    _AislcscDiscPowerSupplyStatus_Type()
)
aislcscDiscPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcscDiscPowerSupplyStatus.setStatus("current")


class _Aislcsc48VSupplyAStatus_Type(Integer32):
    """Custom type aislcsc48VSupplyAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("okay", 1),
          ("overVoltage", 3),
          ("underVoltage", 2))
    )


_Aislcsc48VSupplyAStatus_Type.__name__ = "Integer32"
_Aislcsc48VSupplyAStatus_Object = MibScalar
aislcsc48VSupplyAStatus = _Aislcsc48VSupplyAStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 27),
    _Aislcsc48VSupplyAStatus_Type()
)
aislcsc48VSupplyAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcsc48VSupplyAStatus.setStatus("current")


class _Aislcsc48VSupplyBStatus_Type(Integer32):
    """Custom type aislcsc48VSupplyBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("okay", 1),
          ("overVoltage", 3),
          ("underVoltage", 2))
    )


_Aislcsc48VSupplyBStatus_Type.__name__ = "Integer32"
_Aislcsc48VSupplyBStatus_Object = MibScalar
aislcsc48VSupplyBStatus = _Aislcsc48VSupplyBStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 28),
    _Aislcsc48VSupplyBStatus_Type()
)
aislcsc48VSupplyBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcsc48VSupplyBStatus.setStatus("current")


class _AislcscFanStatus_Type(Integer32):
    """Custom type aislcscFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("okay", 1))
    )


_AislcscFanStatus_Type.__name__ = "Integer32"
_AislcscFanStatus_Object = MibScalar
aislcscFanStatus = _AislcscFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 29),
    _AislcscFanStatus_Type()
)
aislcscFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcscFanStatus.setStatus("current")


class _AislcscMib2ReadCommunity_Type(DisplayString):
    """Custom type aislcscMib2ReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AislcscMib2ReadCommunity_Type.__name__ = "DisplayString"
_AislcscMib2ReadCommunity_Object = MibScalar
aislcscMib2ReadCommunity = _AislcscMib2ReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 30),
    _AislcscMib2ReadCommunity_Type()
)
aislcscMib2ReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscMib2ReadCommunity.setStatus("current")


class _AislcscOverallAlarmSeverity_Type(Integer32):
    """Custom type aislcscOverallAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AislcscOverallAlarmSeverity_Type.__name__ = "Integer32"
_AislcscOverallAlarmSeverity_Object = MibScalar
aislcscOverallAlarmSeverity = _AislcscOverallAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 31),
    _AislcscOverallAlarmSeverity_Type()
)
aislcscOverallAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscOverallAlarmSeverity.setStatus("current")
_AislcSysCfgTime_ObjectIdentity = ObjectIdentity
aislcSysCfgTime = _AislcSysCfgTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 21, 32)
)


class _AislcscTimeZone_Type(DisplayString):
    """Custom type aislcscTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 6),
    )


_AislcscTimeZone_Type.__name__ = "DisplayString"
_AislcscTimeZone_Object = MibScalar
aislcscTimeZone = _AislcscTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 32, 1),
    _AislcscTimeZone_Type()
)
aislcscTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscTimeZone.setStatus("current")


class _AislcscDayLightSaving_Type(Integer32):
    """Custom type aislcscDayLightSaving based on Integer32"""
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


_AislcscDayLightSaving_Type.__name__ = "Integer32"
_AislcscDayLightSaving_Object = MibScalar
aislcscDayLightSaving = _AislcscDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 32, 2),
    _AislcscDayLightSaving_Type()
)
aislcscDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscDayLightSaving.setStatus("current")


class _AislcscSntpPoll_Type(Integer32):
    """Custom type aislcscSntpPoll based on Integer32"""
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


_AislcscSntpPoll_Type.__name__ = "Integer32"
_AislcscSntpPoll_Object = MibScalar
aislcscSntpPoll = _AislcscSntpPoll_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 32, 3),
    _AislcscSntpPoll_Type()
)
aislcscSntpPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscSntpPoll.setStatus("current")
_AislcscNtpServerAddr1_Type = IpAddress
_AislcscNtpServerAddr1_Object = MibScalar
aislcscNtpServerAddr1 = _AislcscNtpServerAddr1_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 32, 4),
    _AislcscNtpServerAddr1_Type()
)
aislcscNtpServerAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscNtpServerAddr1.setStatus("current")
_AislcscNtpServerAddr2_Type = IpAddress
_AislcscNtpServerAddr2_Object = MibScalar
aislcscNtpServerAddr2 = _AislcscNtpServerAddr2_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 32, 5),
    _AislcscNtpServerAddr2_Type()
)
aislcscNtpServerAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscNtpServerAddr2.setStatus("current")


class _AislcscSntpPollInterval_Type(Integer32):
    """Custom type aislcscSntpPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_AislcscSntpPollInterval_Type.__name__ = "Integer32"
_AislcscSntpPollInterval_Object = MibScalar
aislcscSntpPollInterval = _AislcscSntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 32, 6),
    _AislcscSntpPollInterval_Type()
)
aislcscSntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscSntpPollInterval.setStatus("current")


class _AislcscStandaloneStatus_Type(Integer32):
    """Custom type aislcscStandaloneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonStandalone", 2),
          ("standalone", 1))
    )


_AislcscStandaloneStatus_Type.__name__ = "Integer32"
_AislcscStandaloneStatus_Object = MibScalar
aislcscStandaloneStatus = _AislcscStandaloneStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 33),
    _AislcscStandaloneStatus_Type()
)
aislcscStandaloneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcscStandaloneStatus.setStatus("current")


class _AislcscShellPromptTimeout_Type(Integer32):
    """Custom type aislcscShellPromptTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AislcscShellPromptTimeout_Type.__name__ = "Integer32"
_AislcscShellPromptTimeout_Object = MibScalar
aislcscShellPromptTimeout = _AislcscShellPromptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 34),
    _AislcscShellPromptTimeout_Type()
)
aislcscShellPromptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscShellPromptTimeout.setStatus("current")
if mibBuilder.loadTexts:
    aislcscShellPromptTimeout.setUnits("minutes")


class _AislcscDestMenuBreakSeq_Type(DisplayString):
    """Custom type aislcscDestMenuBreakSeq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcscDestMenuBreakSeq_Type.__name__ = "DisplayString"
_AislcscDestMenuBreakSeq_Object = MibScalar
aislcscDestMenuBreakSeq = _AislcscDestMenuBreakSeq_Object(
    (1, 3, 6, 1, 4, 1, 539, 21, 35),
    _AislcscDestMenuBreakSeq_Type()
)
aislcscDestMenuBreakSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcscDestMenuBreakSeq.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISLCSYSCFG-MIB",
    **{"PositiveInteger": PositiveInteger,
       "aii": aii,
       "aiSLCSysCfg": aiSLCSysCfg,
       "aislcscSystemPrompt": aislcscSystemPrompt,
       "aislcscShellMinLogLevel": aislcscShellMinLogLevel,
       "aislcscFtpPort": aislcscFtpPort,
       "aislcscTelnetPort": aislcscTelnetPort,
       "aiSLCSysCfgManagerTable": aiSLCSysCfgManagerTable,
       "aiSLCSysCfgManagerEntry": aiSLCSysCfgManagerEntry,
       "aislcscManagerIndex": aislcscManagerIndex,
       "aislcscManagerAddress": aislcscManagerAddress,
       "aislcscManagerTrapPort": aislcscManagerTrapPort,
       "aislcscReadCommunity": aislcscReadCommunity,
       "aislcscWriteCommunity": aislcscWriteCommunity,
       "aislcsctl1SourceID": aislcsctl1SourceID,
       "aislcsctl1LogonRequired": aislcsctl1LogonRequired,
       "aislcsctl1NumBadLogons": aislcsctl1NumBadLogons,
       "aislcscExtProbeStatus": aislcscExtProbeStatus,
       "aislcscExtLowThreshCelsius": aislcscExtLowThreshCelsius,
       "aislcscExtHighThreshCelsius": aislcscExtHighThreshCelsius,
       "aislcscExtTempCelsius": aislcscExtTempCelsius,
       "aislcscIntProbeStatus": aislcscIntProbeStatus,
       "aislcscIntLowThreshCelsius": aislcscIntLowThreshCelsius,
       "aislcscIntHighThreshCelsius": aislcscIntHighThreshCelsius,
       "aislcscIntTempCelsius": aislcscIntTempCelsius,
       "aislcscExceededThresholdValue": aislcscExceededThresholdValue,
       "aiSLCSysCfgKeepAliveTable": aiSLCSysCfgKeepAliveTable,
       "aiSLCSysCfgKeepAliveEntry": aiSLCSysCfgKeepAliveEntry,
       "aislcscKeepAliveIndex": aislcscKeepAliveIndex,
       "aislcscKeepAliveAddress": aislcscKeepAliveAddress,
       "aislcscKeepAliveInterval": aislcscKeepAliveInterval,
       "aislcscKeepAliveWarningText": aislcscKeepAliveWarningText,
       "aislcscKeepAliveOKText": aislcscKeepAliveOKText,
       "aislcscKeepAliveCommStat": aislcscKeepAliveCommStat,
       "aislcscActiveConfigName": aislcscActiveConfigName,
       "aislcscActiveConfigCRC": aislcscActiveConfigCRC,
       "aislcscSoftwareUpdateName": aislcscSoftwareUpdateName,
       "aislcscSoftwareUpdateStatus": aislcscSoftwareUpdateStatus,
       "aislcscResetSystem": aislcscResetSystem,
       "aislcscDiscPowerSupplyStatus": aislcscDiscPowerSupplyStatus,
       "aislcsc48VSupplyAStatus": aislcsc48VSupplyAStatus,
       "aislcsc48VSupplyBStatus": aislcsc48VSupplyBStatus,
       "aislcscFanStatus": aislcscFanStatus,
       "aislcscMib2ReadCommunity": aislcscMib2ReadCommunity,
       "aislcscOverallAlarmSeverity": aislcscOverallAlarmSeverity,
       "aislcSysCfgTime": aislcSysCfgTime,
       "aislcscTimeZone": aislcscTimeZone,
       "aislcscDayLightSaving": aislcscDayLightSaving,
       "aislcscSntpPoll": aislcscSntpPoll,
       "aislcscNtpServerAddr1": aislcscNtpServerAddr1,
       "aislcscNtpServerAddr2": aislcscNtpServerAddr2,
       "aislcscSntpPollInterval": aislcscSntpPollInterval,
       "aislcscStandaloneStatus": aislcscStandaloneStatus,
       "aislcscShellPromptTimeout": aislcscShellPromptTimeout,
       "aislcscDestMenuBreakSeq": aislcscDestMenuBreakSeq}
)
