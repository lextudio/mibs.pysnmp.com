# SNMP MIB module (SSPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SSPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:49 2024
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

(AppLocalIndex,) = mibBuilder.importSymbols(
    "APM-MIB",
    "AppLocalIndex")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(OwnerString,
 rmon) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
    "rmon")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(Utf8String,) = mibBuilder.importSymbols(
    "SYSAPPL-MIB",
    "Utf8String")


# MODULE-IDENTITY

sspmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 28)
)
sspmMIB.setRevisions(
        ("2005-07-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SspmMicroSeconds(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class SspmClockSource(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class SspmClockMaxSkew(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_SspmMIBObjects_ObjectIdentity = ObjectIdentity
sspmMIBObjects = _SspmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 28, 1)
)
_SspmGeneral_ObjectIdentity = ObjectIdentity
sspmGeneral = _SspmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 1)
)
_SspmGeneralClockResolution_Type = SspmMicroSeconds
_SspmGeneralClockResolution_Object = MibScalar
sspmGeneralClockResolution = _SspmGeneralClockResolution_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 1),
    _SspmGeneralClockResolution_Type()
)
sspmGeneralClockResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspmGeneralClockResolution.setStatus("current")
_SspmGeneralClockMaxSkew_Type = SspmClockMaxSkew
_SspmGeneralClockMaxSkew_Object = MibScalar
sspmGeneralClockMaxSkew = _SspmGeneralClockMaxSkew_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 2),
    _SspmGeneralClockMaxSkew_Type()
)
sspmGeneralClockMaxSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspmGeneralClockMaxSkew.setStatus("current")
_SspmGeneralClockSource_Type = SspmClockSource
_SspmGeneralClockSource_Object = MibScalar
sspmGeneralClockSource = _SspmGeneralClockSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 3),
    _SspmGeneralClockSource_Type()
)
sspmGeneralClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspmGeneralClockSource.setStatus("current")
_SspmGeneralMinFrequency_Type = SspmMicroSeconds
_SspmGeneralMinFrequency_Object = MibScalar
sspmGeneralMinFrequency = _SspmGeneralMinFrequency_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 4),
    _SspmGeneralMinFrequency_Type()
)
sspmGeneralMinFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspmGeneralMinFrequency.setStatus("current")
_SspmCapabilitiesTable_Object = MibTable
sspmCapabilitiesTable = _SspmCapabilitiesTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sspmCapabilitiesTable.setStatus("current")
_SspmCapabilitiesEntry_Object = MibTableRow
sspmCapabilitiesEntry = _SspmCapabilitiesEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 5, 1)
)
sspmCapabilitiesEntry.setIndexNames(
    (0, "SSPM-MIB", "sspmCapabilitiesInstance"),
)
if mibBuilder.loadTexts:
    sspmCapabilitiesEntry.setStatus("current")
_SspmCapabilitiesInstance_Type = AppLocalIndex
_SspmCapabilitiesInstance_Object = MibTableColumn
sspmCapabilitiesInstance = _SspmCapabilitiesInstance_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 5, 1, 1),
    _SspmCapabilitiesInstance_Type()
)
sspmCapabilitiesInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspmCapabilitiesInstance.setStatus("current")
_SspmSource_ObjectIdentity = ObjectIdentity
sspmSource = _SspmSource_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2)
)
_SspmSourceProfileTable_Object = MibTable
sspmSourceProfileTable = _SspmSourceProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sspmSourceProfileTable.setStatus("current")
_SspmSourceProfileEntry_Object = MibTableRow
sspmSourceProfileEntry = _SspmSourceProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1)
)
sspmSourceProfileEntry.setIndexNames(
    (0, "SSPM-MIB", "sspmSourceProfileInstance"),
)
if mibBuilder.loadTexts:
    sspmSourceProfileEntry.setStatus("current")


class _SspmSourceProfileInstance_Type(Unsigned32):
    """Custom type sspmSourceProfileInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SspmSourceProfileInstance_Type.__name__ = "Unsigned32"
_SspmSourceProfileInstance_Object = MibTableColumn
sspmSourceProfileInstance = _SspmSourceProfileInstance_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 1),
    _SspmSourceProfileInstance_Type()
)
sspmSourceProfileInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sspmSourceProfileInstance.setStatus("current")
_SspmSourceProfileType_Type = AppLocalIndex
_SspmSourceProfileType_Object = MibTableColumn
sspmSourceProfileType = _SspmSourceProfileType_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 2),
    _SspmSourceProfileType_Type()
)
sspmSourceProfileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfileType.setStatus("current")
_SspmSourceProfilePacketSize_Type = Unsigned32
_SspmSourceProfilePacketSize_Object = MibTableColumn
sspmSourceProfilePacketSize = _SspmSourceProfilePacketSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 3),
    _SspmSourceProfilePacketSize_Type()
)
sspmSourceProfilePacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfilePacketSize.setStatus("current")


class _SspmSourceProfilePacketFillType_Type(Integer32):
    """Custom type sspmSourceProfilePacketFillType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pattern", 2),
          ("random", 1),
          ("url", 3))
    )


_SspmSourceProfilePacketFillType_Type.__name__ = "Integer32"
_SspmSourceProfilePacketFillType_Object = MibTableColumn
sspmSourceProfilePacketFillType = _SspmSourceProfilePacketFillType_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 4),
    _SspmSourceProfilePacketFillType_Type()
)
sspmSourceProfilePacketFillType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfilePacketFillType.setStatus("current")


class _SspmSourceProfilePacketFillValue_Type(OctetString):
    """Custom type sspmSourceProfilePacketFillValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SspmSourceProfilePacketFillValue_Type.__name__ = "OctetString"
_SspmSourceProfilePacketFillValue_Object = MibTableColumn
sspmSourceProfilePacketFillValue = _SspmSourceProfilePacketFillValue_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 5),
    _SspmSourceProfilePacketFillValue_Type()
)
sspmSourceProfilePacketFillValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfilePacketFillValue.setStatus("current")


class _SspmSourceProfileTOS_Type(Integer32):
    """Custom type sspmSourceProfileTOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SspmSourceProfileTOS_Type.__name__ = "Integer32"
_SspmSourceProfileTOS_Object = MibTableColumn
sspmSourceProfileTOS = _SspmSourceProfileTOS_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 6),
    _SspmSourceProfileTOS_Type()
)
sspmSourceProfileTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfileTOS.setStatus("current")


class _SspmSourceProfileFlowLabel_Type(Integer32):
    """Custom type sspmSourceProfileFlowLabel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_SspmSourceProfileFlowLabel_Type.__name__ = "Integer32"
_SspmSourceProfileFlowLabel_Object = MibTableColumn
sspmSourceProfileFlowLabel = _SspmSourceProfileFlowLabel_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 7),
    _SspmSourceProfileFlowLabel_Type()
)
sspmSourceProfileFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfileFlowLabel.setStatus("current")


class _SspmSourceProfileLooseSrcRteFill_Type(OctetString):
    """Custom type sspmSourceProfileLooseSrcRteFill based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_SspmSourceProfileLooseSrcRteFill_Type.__name__ = "OctetString"
_SspmSourceProfileLooseSrcRteFill_Object = MibTableColumn
sspmSourceProfileLooseSrcRteFill = _SspmSourceProfileLooseSrcRteFill_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 8),
    _SspmSourceProfileLooseSrcRteFill_Type()
)
sspmSourceProfileLooseSrcRteFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfileLooseSrcRteFill.setStatus("current")


class _SspmSourceProfileLooseSrcRteLen_Type(Integer32):
    """Custom type sspmSourceProfileLooseSrcRteLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_SspmSourceProfileLooseSrcRteLen_Type.__name__ = "Integer32"
_SspmSourceProfileLooseSrcRteLen_Object = MibTableColumn
sspmSourceProfileLooseSrcRteLen = _SspmSourceProfileLooseSrcRteLen_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 9),
    _SspmSourceProfileLooseSrcRteLen_Type()
)
sspmSourceProfileLooseSrcRteLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfileLooseSrcRteLen.setStatus("current")


class _SspmSourceProfileTTL_Type(Integer32):
    """Custom type sspmSourceProfileTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SspmSourceProfileTTL_Type.__name__ = "Integer32"
_SspmSourceProfileTTL_Object = MibTableColumn
sspmSourceProfileTTL = _SspmSourceProfileTTL_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 10),
    _SspmSourceProfileTTL_Type()
)
sspmSourceProfileTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfileTTL.setStatus("current")
_SspmSourceProfileNoFrag_Type = TruthValue
_SspmSourceProfileNoFrag_Object = MibTableColumn
sspmSourceProfileNoFrag = _SspmSourceProfileNoFrag_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 11),
    _SspmSourceProfileNoFrag_Type()
)
sspmSourceProfileNoFrag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfileNoFrag.setStatus("current")


class _SspmSourceProfile8021Tagging_Type(Integer32):
    """Custom type sspmSourceProfile8021Tagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_SspmSourceProfile8021Tagging_Type.__name__ = "Integer32"
_SspmSourceProfile8021Tagging_Object = MibTableColumn
sspmSourceProfile8021Tagging = _SspmSourceProfile8021Tagging_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 12),
    _SspmSourceProfile8021Tagging_Type()
)
sspmSourceProfile8021Tagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfile8021Tagging.setStatus("current")
_SspmSourceProfileUsername_Type = Utf8String
_SspmSourceProfileUsername_Object = MibTableColumn
sspmSourceProfileUsername = _SspmSourceProfileUsername_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 13),
    _SspmSourceProfileUsername_Type()
)
sspmSourceProfileUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfileUsername.setStatus("current")
_SspmSourceProfilePassword_Type = Utf8String
_SspmSourceProfilePassword_Object = MibTableColumn
sspmSourceProfilePassword = _SspmSourceProfilePassword_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 14),
    _SspmSourceProfilePassword_Type()
)
sspmSourceProfilePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfilePassword.setStatus("current")


class _SspmSourceProfileParameter_Type(OctetString):
    """Custom type sspmSourceProfileParameter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_SspmSourceProfileParameter_Type.__name__ = "OctetString"
_SspmSourceProfileParameter_Object = MibTableColumn
sspmSourceProfileParameter = _SspmSourceProfileParameter_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 15),
    _SspmSourceProfileParameter_Type()
)
sspmSourceProfileParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfileParameter.setStatus("current")
_SspmSourceProfileOwner_Type = OwnerString
_SspmSourceProfileOwner_Object = MibTableColumn
sspmSourceProfileOwner = _SspmSourceProfileOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 16),
    _SspmSourceProfileOwner_Type()
)
sspmSourceProfileOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfileOwner.setStatus("current")
_SspmSourceProfileStorageType_Type = StorageType
_SspmSourceProfileStorageType_Object = MibTableColumn
sspmSourceProfileStorageType = _SspmSourceProfileStorageType_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 17),
    _SspmSourceProfileStorageType_Type()
)
sspmSourceProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfileStorageType.setStatus("current")
_SspmSourceProfileStatus_Type = RowStatus
_SspmSourceProfileStatus_Object = MibTableColumn
sspmSourceProfileStatus = _SspmSourceProfileStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 18),
    _SspmSourceProfileStatus_Type()
)
sspmSourceProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceProfileStatus.setStatus("current")
_SspmSourceControlTable_Object = MibTable
sspmSourceControlTable = _SspmSourceControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sspmSourceControlTable.setStatus("current")
_SspmSourceControlEntry_Object = MibTableRow
sspmSourceControlEntry = _SspmSourceControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1)
)
sspmSourceControlEntry.setIndexNames(
    (0, "SSPM-MIB", "sspmSourceControlInstance"),
)
if mibBuilder.loadTexts:
    sspmSourceControlEntry.setStatus("current")


class _SspmSourceControlInstance_Type(Unsigned32):
    """Custom type sspmSourceControlInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SspmSourceControlInstance_Type.__name__ = "Unsigned32"
_SspmSourceControlInstance_Object = MibTableColumn
sspmSourceControlInstance = _SspmSourceControlInstance_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 1),
    _SspmSourceControlInstance_Type()
)
sspmSourceControlInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sspmSourceControlInstance.setStatus("current")


class _SspmSourceControlProfile_Type(Integer32):
    """Custom type sspmSourceControlProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SspmSourceControlProfile_Type.__name__ = "Integer32"
_SspmSourceControlProfile_Object = MibTableColumn
sspmSourceControlProfile = _SspmSourceControlProfile_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 2),
    _SspmSourceControlProfile_Type()
)
sspmSourceControlProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceControlProfile.setStatus("current")
_SspmSourceControlSrc_Type = InterfaceIndexOrZero
_SspmSourceControlSrc_Object = MibTableColumn
sspmSourceControlSrc = _SspmSourceControlSrc_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 3),
    _SspmSourceControlSrc_Type()
)
sspmSourceControlSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceControlSrc.setStatus("current")
_SspmSourceControlDestAddrType_Type = InetAddressType
_SspmSourceControlDestAddrType_Object = MibTableColumn
sspmSourceControlDestAddrType = _SspmSourceControlDestAddrType_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 4),
    _SspmSourceControlDestAddrType_Type()
)
sspmSourceControlDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceControlDestAddrType.setStatus("current")
_SspmSourceControlDestAddr_Type = InetAddress
_SspmSourceControlDestAddr_Object = MibTableColumn
sspmSourceControlDestAddr = _SspmSourceControlDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 5),
    _SspmSourceControlDestAddr_Type()
)
sspmSourceControlDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceControlDestAddr.setStatus("current")
_SspmSourceControlEnabled_Type = TruthValue
_SspmSourceControlEnabled_Object = MibTableColumn
sspmSourceControlEnabled = _SspmSourceControlEnabled_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 6),
    _SspmSourceControlEnabled_Type()
)
sspmSourceControlEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceControlEnabled.setStatus("current")
_SspmSourceControlTimeOut_Type = SspmMicroSeconds
_SspmSourceControlTimeOut_Object = MibTableColumn
sspmSourceControlTimeOut = _SspmSourceControlTimeOut_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 7),
    _SspmSourceControlTimeOut_Type()
)
sspmSourceControlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceControlTimeOut.setStatus("current")


class _SspmSourceControlSamplingDist_Type(Integer32):
    """Custom type sspmSourceControlSamplingDist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deterministic", 1),
          ("poisson", 2))
    )


_SspmSourceControlSamplingDist_Type.__name__ = "Integer32"
_SspmSourceControlSamplingDist_Object = MibTableColumn
sspmSourceControlSamplingDist = _SspmSourceControlSamplingDist_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 8),
    _SspmSourceControlSamplingDist_Type()
)
sspmSourceControlSamplingDist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceControlSamplingDist.setStatus("current")
_SspmSourceControlFrequency_Type = SspmMicroSeconds
_SspmSourceControlFrequency_Object = MibTableColumn
sspmSourceControlFrequency = _SspmSourceControlFrequency_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 9),
    _SspmSourceControlFrequency_Type()
)
sspmSourceControlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceControlFrequency.setStatus("current")
_SspmSourceControlFirstSeqNum_Type = Unsigned32
_SspmSourceControlFirstSeqNum_Object = MibTableColumn
sspmSourceControlFirstSeqNum = _SspmSourceControlFirstSeqNum_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 10),
    _SspmSourceControlFirstSeqNum_Type()
)
sspmSourceControlFirstSeqNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceControlFirstSeqNum.setStatus("current")
_SspmSourceControlLastSeqNum_Type = Unsigned32
_SspmSourceControlLastSeqNum_Object = MibTableColumn
sspmSourceControlLastSeqNum = _SspmSourceControlLastSeqNum_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 11),
    _SspmSourceControlLastSeqNum_Type()
)
sspmSourceControlLastSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspmSourceControlLastSeqNum.setStatus("current")
_SspmSourceControlOwner_Type = OwnerString
_SspmSourceControlOwner_Object = MibTableColumn
sspmSourceControlOwner = _SspmSourceControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 12),
    _SspmSourceControlOwner_Type()
)
sspmSourceControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceControlOwner.setStatus("current")
_SspmSourceControlStorageType_Type = StorageType
_SspmSourceControlStorageType_Object = MibTableColumn
sspmSourceControlStorageType = _SspmSourceControlStorageType_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 13),
    _SspmSourceControlStorageType_Type()
)
sspmSourceControlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceControlStorageType.setStatus("current")
_SspmSourceControlStatus_Type = RowStatus
_SspmSourceControlStatus_Object = MibTableColumn
sspmSourceControlStatus = _SspmSourceControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 14),
    _SspmSourceControlStatus_Type()
)
sspmSourceControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSourceControlStatus.setStatus("current")
_SspmSink_ObjectIdentity = ObjectIdentity
sspmSink = _SspmSink_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5)
)
_SspmSinkTable_Object = MibTable
sspmSinkTable = _SspmSinkTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sspmSinkTable.setStatus("current")
_SspmSinkEntry_Object = MibTableRow
sspmSinkEntry = _SspmSinkEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1)
)
sspmSinkEntry.setIndexNames(
    (0, "SSPM-MIB", "sspmSinkInstance"),
)
if mibBuilder.loadTexts:
    sspmSinkEntry.setStatus("current")


class _SspmSinkInstance_Type(Unsigned32):
    """Custom type sspmSinkInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SspmSinkInstance_Type.__name__ = "Unsigned32"
_SspmSinkInstance_Object = MibTableColumn
sspmSinkInstance = _SspmSinkInstance_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 1),
    _SspmSinkInstance_Type()
)
sspmSinkInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sspmSinkInstance.setStatus("current")
_SspmSinkType_Type = AppLocalIndex
_SspmSinkType_Object = MibTableColumn
sspmSinkType = _SspmSinkType_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 2),
    _SspmSinkType_Type()
)
sspmSinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSinkType.setStatus("current")
_SspmSinkSourceAddressType_Type = InetAddressType
_SspmSinkSourceAddressType_Object = MibTableColumn
sspmSinkSourceAddressType = _SspmSinkSourceAddressType_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 3),
    _SspmSinkSourceAddressType_Type()
)
sspmSinkSourceAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSinkSourceAddressType.setStatus("current")
_SspmSinkSourceAddress_Type = InetAddress
_SspmSinkSourceAddress_Object = MibTableColumn
sspmSinkSourceAddress = _SspmSinkSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 4),
    _SspmSinkSourceAddress_Type()
)
sspmSinkSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSinkSourceAddress.setStatus("current")
_SspmSinkExpectedRate_Type = SspmMicroSeconds
_SspmSinkExpectedRate_Object = MibTableColumn
sspmSinkExpectedRate = _SspmSinkExpectedRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 5),
    _SspmSinkExpectedRate_Type()
)
sspmSinkExpectedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSinkExpectedRate.setStatus("current")
_SspmSinkEnable_Type = TruthValue
_SspmSinkEnable_Object = MibTableColumn
sspmSinkEnable = _SspmSinkEnable_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 6),
    _SspmSinkEnable_Type()
)
sspmSinkEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSinkEnable.setStatus("current")
_SspmSinkExpectedFirstSequenceNum_Type = Unsigned32
_SspmSinkExpectedFirstSequenceNum_Object = MibTableColumn
sspmSinkExpectedFirstSequenceNum = _SspmSinkExpectedFirstSequenceNum_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 7),
    _SspmSinkExpectedFirstSequenceNum_Type()
)
sspmSinkExpectedFirstSequenceNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSinkExpectedFirstSequenceNum.setStatus("current")
_SspmSinkLastSequenceNumber_Type = Unsigned32
_SspmSinkLastSequenceNumber_Object = MibTableColumn
sspmSinkLastSequenceNumber = _SspmSinkLastSequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 8),
    _SspmSinkLastSequenceNumber_Type()
)
sspmSinkLastSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspmSinkLastSequenceNumber.setStatus("current")
_SspmSinkLastSequenceInvalid_Type = Counter32
_SspmSinkLastSequenceInvalid_Object = MibTableColumn
sspmSinkLastSequenceInvalid = _SspmSinkLastSequenceInvalid_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 9),
    _SspmSinkLastSequenceInvalid_Type()
)
sspmSinkLastSequenceInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspmSinkLastSequenceInvalid.setStatus("current")
_SspmSinkStorageType_Type = StorageType
_SspmSinkStorageType_Object = MibTableColumn
sspmSinkStorageType = _SspmSinkStorageType_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 10),
    _SspmSinkStorageType_Type()
)
sspmSinkStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSinkStorageType.setStatus("current")
_SspmSinkStatus_Type = RowStatus
_SspmSinkStatus_Object = MibTableColumn
sspmSinkStatus = _SspmSinkStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 11),
    _SspmSinkStatus_Type()
)
sspmSinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sspmSinkStatus.setStatus("current")
_SspmMIBNotifications_ObjectIdentity = ObjectIdentity
sspmMIBNotifications = _SspmMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 28, 2)
)
_SspmMIBConformance_ObjectIdentity = ObjectIdentity
sspmMIBConformance = _SspmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 28, 3)
)
_SspmCompliances_ObjectIdentity = ObjectIdentity
sspmCompliances = _SspmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 28, 3, 1)
)
_SspmGroups_ObjectIdentity = ObjectIdentity
sspmGroups = _SspmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 28, 3, 2)
)

# Managed Objects groups

sspmGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 28, 3, 2, 1)
)
sspmGeneralGroup.setObjects(
      *(("SSPM-MIB", "sspmGeneralClockResolution"),
        ("SSPM-MIB", "sspmGeneralClockMaxSkew"),
        ("SSPM-MIB", "sspmGeneralClockSource"),
        ("SSPM-MIB", "sspmGeneralMinFrequency"),
        ("SSPM-MIB", "sspmCapabilitiesInstance"))
)
if mibBuilder.loadTexts:
    sspmGeneralGroup.setStatus("current")

sspmSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 28, 3, 2, 2)
)
sspmSourceGroup.setObjects(
      *(("SSPM-MIB", "sspmSourceProfileType"),
        ("SSPM-MIB", "sspmSourceProfilePacketSize"),
        ("SSPM-MIB", "sspmSourceProfilePacketFillType"),
        ("SSPM-MIB", "sspmSourceProfilePacketFillValue"),
        ("SSPM-MIB", "sspmSourceProfileTOS"),
        ("SSPM-MIB", "sspmSourceProfileFlowLabel"),
        ("SSPM-MIB", "sspmSourceProfileLooseSrcRteFill"),
        ("SSPM-MIB", "sspmSourceProfileLooseSrcRteLen"),
        ("SSPM-MIB", "sspmSourceProfileTTL"),
        ("SSPM-MIB", "sspmSourceProfileNoFrag"),
        ("SSPM-MIB", "sspmSourceProfile8021Tagging"),
        ("SSPM-MIB", "sspmSourceProfileUsername"),
        ("SSPM-MIB", "sspmSourceProfilePassword"),
        ("SSPM-MIB", "sspmSourceProfileParameter"),
        ("SSPM-MIB", "sspmSourceProfileOwner"),
        ("SSPM-MIB", "sspmSourceProfileStorageType"),
        ("SSPM-MIB", "sspmSourceProfileStatus"),
        ("SSPM-MIB", "sspmSourceControlProfile"),
        ("SSPM-MIB", "sspmSourceControlSrc"),
        ("SSPM-MIB", "sspmSourceControlDestAddrType"),
        ("SSPM-MIB", "sspmSourceControlDestAddr"),
        ("SSPM-MIB", "sspmSourceControlEnabled"),
        ("SSPM-MIB", "sspmSourceControlTimeOut"),
        ("SSPM-MIB", "sspmSourceControlSamplingDist"),
        ("SSPM-MIB", "sspmSourceControlFrequency"),
        ("SSPM-MIB", "sspmSourceControlFirstSeqNum"),
        ("SSPM-MIB", "sspmSourceControlLastSeqNum"),
        ("SSPM-MIB", "sspmSourceControlOwner"),
        ("SSPM-MIB", "sspmSourceControlStorageType"),
        ("SSPM-MIB", "sspmSourceControlStatus"))
)
if mibBuilder.loadTexts:
    sspmSourceGroup.setStatus("current")

sspmUserPassGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 28, 3, 2, 3)
)
sspmUserPassGroup.setObjects(
      *(("SSPM-MIB", "sspmSourceProfileUsername"),
        ("SSPM-MIB", "sspmSourceProfilePassword"))
)
if mibBuilder.loadTexts:
    sspmUserPassGroup.setStatus("current")

sspmSinkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 28, 3, 2, 4)
)
sspmSinkGroup.setObjects(
      *(("SSPM-MIB", "sspmSinkType"),
        ("SSPM-MIB", "sspmSinkSourceAddressType"),
        ("SSPM-MIB", "sspmSinkSourceAddress"),
        ("SSPM-MIB", "sspmSinkExpectedRate"),
        ("SSPM-MIB", "sspmSinkEnable"),
        ("SSPM-MIB", "sspmSinkExpectedFirstSequenceNum"),
        ("SSPM-MIB", "sspmSinkLastSequenceNumber"),
        ("SSPM-MIB", "sspmSinkLastSequenceInvalid"),
        ("SSPM-MIB", "sspmSinkStorageType"),
        ("SSPM-MIB", "sspmSinkStatus"))
)
if mibBuilder.loadTexts:
    sspmSinkGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sspmGeneralCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 28, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sspmGeneralCompliance.setStatus(
        "current"
    )

sspmSourceFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 28, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sspmSourceFullCompliance.setStatus(
        "current"
    )

sspmSinkFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 28, 3, 1, 3)
)
if mibBuilder.loadTexts:
    sspmSinkFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SSPM-MIB",
    **{"SspmMicroSeconds": SspmMicroSeconds,
       "SspmClockSource": SspmClockSource,
       "SspmClockMaxSkew": SspmClockMaxSkew,
       "sspmMIB": sspmMIB,
       "sspmMIBObjects": sspmMIBObjects,
       "sspmGeneral": sspmGeneral,
       "sspmGeneralClockResolution": sspmGeneralClockResolution,
       "sspmGeneralClockMaxSkew": sspmGeneralClockMaxSkew,
       "sspmGeneralClockSource": sspmGeneralClockSource,
       "sspmGeneralMinFrequency": sspmGeneralMinFrequency,
       "sspmCapabilitiesTable": sspmCapabilitiesTable,
       "sspmCapabilitiesEntry": sspmCapabilitiesEntry,
       "sspmCapabilitiesInstance": sspmCapabilitiesInstance,
       "sspmSource": sspmSource,
       "sspmSourceProfileTable": sspmSourceProfileTable,
       "sspmSourceProfileEntry": sspmSourceProfileEntry,
       "sspmSourceProfileInstance": sspmSourceProfileInstance,
       "sspmSourceProfileType": sspmSourceProfileType,
       "sspmSourceProfilePacketSize": sspmSourceProfilePacketSize,
       "sspmSourceProfilePacketFillType": sspmSourceProfilePacketFillType,
       "sspmSourceProfilePacketFillValue": sspmSourceProfilePacketFillValue,
       "sspmSourceProfileTOS": sspmSourceProfileTOS,
       "sspmSourceProfileFlowLabel": sspmSourceProfileFlowLabel,
       "sspmSourceProfileLooseSrcRteFill": sspmSourceProfileLooseSrcRteFill,
       "sspmSourceProfileLooseSrcRteLen": sspmSourceProfileLooseSrcRteLen,
       "sspmSourceProfileTTL": sspmSourceProfileTTL,
       "sspmSourceProfileNoFrag": sspmSourceProfileNoFrag,
       "sspmSourceProfile8021Tagging": sspmSourceProfile8021Tagging,
       "sspmSourceProfileUsername": sspmSourceProfileUsername,
       "sspmSourceProfilePassword": sspmSourceProfilePassword,
       "sspmSourceProfileParameter": sspmSourceProfileParameter,
       "sspmSourceProfileOwner": sspmSourceProfileOwner,
       "sspmSourceProfileStorageType": sspmSourceProfileStorageType,
       "sspmSourceProfileStatus": sspmSourceProfileStatus,
       "sspmSourceControlTable": sspmSourceControlTable,
       "sspmSourceControlEntry": sspmSourceControlEntry,
       "sspmSourceControlInstance": sspmSourceControlInstance,
       "sspmSourceControlProfile": sspmSourceControlProfile,
       "sspmSourceControlSrc": sspmSourceControlSrc,
       "sspmSourceControlDestAddrType": sspmSourceControlDestAddrType,
       "sspmSourceControlDestAddr": sspmSourceControlDestAddr,
       "sspmSourceControlEnabled": sspmSourceControlEnabled,
       "sspmSourceControlTimeOut": sspmSourceControlTimeOut,
       "sspmSourceControlSamplingDist": sspmSourceControlSamplingDist,
       "sspmSourceControlFrequency": sspmSourceControlFrequency,
       "sspmSourceControlFirstSeqNum": sspmSourceControlFirstSeqNum,
       "sspmSourceControlLastSeqNum": sspmSourceControlLastSeqNum,
       "sspmSourceControlOwner": sspmSourceControlOwner,
       "sspmSourceControlStorageType": sspmSourceControlStorageType,
       "sspmSourceControlStatus": sspmSourceControlStatus,
       "sspmSink": sspmSink,
       "sspmSinkTable": sspmSinkTable,
       "sspmSinkEntry": sspmSinkEntry,
       "sspmSinkInstance": sspmSinkInstance,
       "sspmSinkType": sspmSinkType,
       "sspmSinkSourceAddressType": sspmSinkSourceAddressType,
       "sspmSinkSourceAddress": sspmSinkSourceAddress,
       "sspmSinkExpectedRate": sspmSinkExpectedRate,
       "sspmSinkEnable": sspmSinkEnable,
       "sspmSinkExpectedFirstSequenceNum": sspmSinkExpectedFirstSequenceNum,
       "sspmSinkLastSequenceNumber": sspmSinkLastSequenceNumber,
       "sspmSinkLastSequenceInvalid": sspmSinkLastSequenceInvalid,
       "sspmSinkStorageType": sspmSinkStorageType,
       "sspmSinkStatus": sspmSinkStatus,
       "sspmMIBNotifications": sspmMIBNotifications,
       "sspmMIBConformance": sspmMIBConformance,
       "sspmCompliances": sspmCompliances,
       "sspmGeneralCompliance": sspmGeneralCompliance,
       "sspmSourceFullCompliance": sspmSourceFullCompliance,
       "sspmSinkFullCompliance": sspmSinkFullCompliance,
       "sspmGroups": sspmGroups,
       "sspmGeneralGroup": sspmGeneralGroup,
       "sspmSourceGroup": sspmSourceGroup,
       "sspmUserPassGroup": sspmUserPassGroup,
       "sspmSinkGroup": sspmSinkGroup}
)
