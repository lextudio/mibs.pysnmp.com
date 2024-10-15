# SNMP MIB module (NTPv4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTPv4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:48 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(Utf8String,) = mibBuilder.importSymbols(
    "SYSAPPL-MIB",
    "Utf8String")


# MODULE-IDENTITY

ntpSnmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 197)
)
ntpSnmpMIB.setRevisions(
        ("2010-05-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NtpStratum(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class NtpDateTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d:4d:4d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_NtpEntNotifications_ObjectIdentity = ObjectIdentity
ntpEntNotifications = _NtpEntNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 197, 0)
)
_NtpSnmpMIBObjects_ObjectIdentity = ObjectIdentity
ntpSnmpMIBObjects = _NtpSnmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 197, 1)
)
_NtpEntInfo_ObjectIdentity = ObjectIdentity
ntpEntInfo = _NtpEntInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 197, 1, 1)
)
_NtpEntSoftwareName_Type = Utf8String
_NtpEntSoftwareName_Object = MibScalar
ntpEntSoftwareName = _NtpEntSoftwareName_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 1, 1),
    _NtpEntSoftwareName_Type()
)
ntpEntSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntSoftwareName.setStatus("current")
_NtpEntSoftwareVersion_Type = Utf8String
_NtpEntSoftwareVersion_Object = MibScalar
ntpEntSoftwareVersion = _NtpEntSoftwareVersion_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 1, 2),
    _NtpEntSoftwareVersion_Type()
)
ntpEntSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntSoftwareVersion.setStatus("current")
_NtpEntSoftwareVendor_Type = Utf8String
_NtpEntSoftwareVendor_Object = MibScalar
ntpEntSoftwareVendor = _NtpEntSoftwareVendor_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 1, 3),
    _NtpEntSoftwareVendor_Type()
)
ntpEntSoftwareVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntSoftwareVendor.setStatus("current")
_NtpEntSystemType_Type = Utf8String
_NtpEntSystemType_Object = MibScalar
ntpEntSystemType = _NtpEntSystemType_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 1, 4),
    _NtpEntSystemType_Type()
)
ntpEntSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntSystemType.setStatus("current")
_NtpEntTimeResolution_Type = Unsigned32
_NtpEntTimeResolution_Object = MibScalar
ntpEntTimeResolution = _NtpEntTimeResolution_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 1, 5),
    _NtpEntTimeResolution_Type()
)
ntpEntTimeResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntTimeResolution.setStatus("current")
_NtpEntTimePrecision_Type = Integer32
_NtpEntTimePrecision_Object = MibScalar
ntpEntTimePrecision = _NtpEntTimePrecision_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 1, 6),
    _NtpEntTimePrecision_Type()
)
ntpEntTimePrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntTimePrecision.setStatus("current")
_NtpEntTimeDistance_Type = DisplayString
_NtpEntTimeDistance_Object = MibScalar
ntpEntTimeDistance = _NtpEntTimeDistance_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 1, 7),
    _NtpEntTimeDistance_Type()
)
ntpEntTimeDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntTimeDistance.setStatus("current")
_NtpEntStatus_ObjectIdentity = ObjectIdentity
ntpEntStatus = _NtpEntStatus_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 197, 1, 2)
)


class _NtpEntStatusCurrentMode_Type(Integer32):
    """Custom type ntpEntStatusCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("noneConfigured", 3),
          ("notRunning", 1),
          ("notSynchronized", 2),
          ("syncToLocal", 4),
          ("syncToRefclock", 5),
          ("syncToRemoteServer", 6),
          ("unknown", 99))
    )


_NtpEntStatusCurrentMode_Type.__name__ = "Integer32"
_NtpEntStatusCurrentMode_Object = MibScalar
ntpEntStatusCurrentMode = _NtpEntStatusCurrentMode_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 1),
    _NtpEntStatusCurrentMode_Type()
)
ntpEntStatusCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusCurrentMode.setStatus("current")
_NtpEntStatusStratum_Type = NtpStratum
_NtpEntStatusStratum_Object = MibScalar
ntpEntStatusStratum = _NtpEntStatusStratum_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 2),
    _NtpEntStatusStratum_Type()
)
ntpEntStatusStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusStratum.setStatus("current")


class _NtpEntStatusActiveRefSourceId_Type(Unsigned32):
    """Custom type ntpEntStatusActiveRefSourceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NtpEntStatusActiveRefSourceId_Type.__name__ = "Unsigned32"
_NtpEntStatusActiveRefSourceId_Object = MibScalar
ntpEntStatusActiveRefSourceId = _NtpEntStatusActiveRefSourceId_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 3),
    _NtpEntStatusActiveRefSourceId_Type()
)
ntpEntStatusActiveRefSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusActiveRefSourceId.setStatus("current")
_NtpEntStatusActiveRefSourceName_Type = Utf8String
_NtpEntStatusActiveRefSourceName_Object = MibScalar
ntpEntStatusActiveRefSourceName = _NtpEntStatusActiveRefSourceName_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 4),
    _NtpEntStatusActiveRefSourceName_Type()
)
ntpEntStatusActiveRefSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusActiveRefSourceName.setStatus("current")
_NtpEntStatusActiveOffset_Type = DisplayString
_NtpEntStatusActiveOffset_Object = MibScalar
ntpEntStatusActiveOffset = _NtpEntStatusActiveOffset_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 5),
    _NtpEntStatusActiveOffset_Type()
)
ntpEntStatusActiveOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusActiveOffset.setStatus("current")


class _NtpEntStatusNumberOfRefSources_Type(Unsigned32):
    """Custom type ntpEntStatusNumberOfRefSources based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_NtpEntStatusNumberOfRefSources_Type.__name__ = "Unsigned32"
_NtpEntStatusNumberOfRefSources_Object = MibScalar
ntpEntStatusNumberOfRefSources = _NtpEntStatusNumberOfRefSources_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 6),
    _NtpEntStatusNumberOfRefSources_Type()
)
ntpEntStatusNumberOfRefSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusNumberOfRefSources.setStatus("current")
_NtpEntStatusDispersion_Type = DisplayString
_NtpEntStatusDispersion_Object = MibScalar
ntpEntStatusDispersion = _NtpEntStatusDispersion_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 7),
    _NtpEntStatusDispersion_Type()
)
ntpEntStatusDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusDispersion.setStatus("current")
_NtpEntStatusEntityUptime_Type = TimeTicks
_NtpEntStatusEntityUptime_Object = MibScalar
ntpEntStatusEntityUptime = _NtpEntStatusEntityUptime_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 8),
    _NtpEntStatusEntityUptime_Type()
)
ntpEntStatusEntityUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusEntityUptime.setStatus("current")
_NtpEntStatusDateTime_Type = NtpDateTime
_NtpEntStatusDateTime_Object = MibScalar
ntpEntStatusDateTime = _NtpEntStatusDateTime_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 9),
    _NtpEntStatusDateTime_Type()
)
ntpEntStatusDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusDateTime.setStatus("current")
_NtpEntStatusLeapSecond_Type = NtpDateTime
_NtpEntStatusLeapSecond_Object = MibScalar
ntpEntStatusLeapSecond = _NtpEntStatusLeapSecond_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 10),
    _NtpEntStatusLeapSecond_Type()
)
ntpEntStatusLeapSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusLeapSecond.setStatus("current")


class _NtpEntStatusLeapSecDirection_Type(Integer32):
    """Custom type ntpEntStatusLeapSecDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_NtpEntStatusLeapSecDirection_Type.__name__ = "Integer32"
_NtpEntStatusLeapSecDirection_Object = MibScalar
ntpEntStatusLeapSecDirection = _NtpEntStatusLeapSecDirection_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 11),
    _NtpEntStatusLeapSecDirection_Type()
)
ntpEntStatusLeapSecDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusLeapSecDirection.setStatus("current")
_NtpEntStatusInPkts_Type = Counter32
_NtpEntStatusInPkts_Object = MibScalar
ntpEntStatusInPkts = _NtpEntStatusInPkts_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 12),
    _NtpEntStatusInPkts_Type()
)
ntpEntStatusInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusInPkts.setStatus("current")
if mibBuilder.loadTexts:
    ntpEntStatusInPkts.setUnits("packets")
_NtpEntStatusOutPkts_Type = Counter32
_NtpEntStatusOutPkts_Object = MibScalar
ntpEntStatusOutPkts = _NtpEntStatusOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 13),
    _NtpEntStatusOutPkts_Type()
)
ntpEntStatusOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    ntpEntStatusOutPkts.setUnits("packets")
_NtpEntStatusBadVersion_Type = Counter32
_NtpEntStatusBadVersion_Object = MibScalar
ntpEntStatusBadVersion = _NtpEntStatusBadVersion_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 14),
    _NtpEntStatusBadVersion_Type()
)
ntpEntStatusBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusBadVersion.setStatus("current")
if mibBuilder.loadTexts:
    ntpEntStatusBadVersion.setUnits("packets")
_NtpEntStatusProtocolError_Type = Counter32
_NtpEntStatusProtocolError_Object = MibScalar
ntpEntStatusProtocolError = _NtpEntStatusProtocolError_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 15),
    _NtpEntStatusProtocolError_Type()
)
ntpEntStatusProtocolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusProtocolError.setStatus("current")
if mibBuilder.loadTexts:
    ntpEntStatusProtocolError.setUnits("packets")
_NtpEntStatusNotifications_Type = Counter32
_NtpEntStatusNotifications_Object = MibScalar
ntpEntStatusNotifications = _NtpEntStatusNotifications_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 16),
    _NtpEntStatusNotifications_Type()
)
ntpEntStatusNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatusNotifications.setStatus("current")
if mibBuilder.loadTexts:
    ntpEntStatusNotifications.setUnits("notifications")
_NtpEntStatPktModeTable_Object = MibTable
ntpEntStatPktModeTable = _NtpEntStatPktModeTable_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 17)
)
if mibBuilder.loadTexts:
    ntpEntStatPktModeTable.setStatus("current")
_NtpEntStatPktModeEntry_Object = MibTableRow
ntpEntStatPktModeEntry = _NtpEntStatPktModeEntry_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 17, 1)
)
ntpEntStatPktModeEntry.setIndexNames(
    (0, "NTPv4-MIB", "ntpEntStatPktMode"),
)
if mibBuilder.loadTexts:
    ntpEntStatPktModeEntry.setStatus("current")


class _NtpEntStatPktMode_Type(Integer32):
    """Custom type ntpEntStatPktMode based on Integer32"""
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
        *(("broadcastclient", 6),
          ("broadcastserver", 5),
          ("client", 3),
          ("server", 4),
          ("symetricactive", 1),
          ("symetricpassive", 2))
    )


_NtpEntStatPktMode_Type.__name__ = "Integer32"
_NtpEntStatPktMode_Object = MibTableColumn
ntpEntStatPktMode = _NtpEntStatPktMode_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 17, 1, 1),
    _NtpEntStatPktMode_Type()
)
ntpEntStatPktMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpEntStatPktMode.setStatus("current")
_NtpEntStatPktSent_Type = Counter32
_NtpEntStatPktSent_Object = MibTableColumn
ntpEntStatPktSent = _NtpEntStatPktSent_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 17, 1, 2),
    _NtpEntStatPktSent_Type()
)
ntpEntStatPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatPktSent.setStatus("current")
if mibBuilder.loadTexts:
    ntpEntStatPktSent.setUnits("packets")
_NtpEntStatPktReceived_Type = Counter32
_NtpEntStatPktReceived_Object = MibTableColumn
ntpEntStatPktReceived = _NtpEntStatPktReceived_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 2, 17, 1, 3),
    _NtpEntStatPktReceived_Type()
)
ntpEntStatPktReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEntStatPktReceived.setStatus("current")
if mibBuilder.loadTexts:
    ntpEntStatPktReceived.setUnits("packets")
_NtpAssociation_ObjectIdentity = ObjectIdentity
ntpAssociation = _NtpAssociation_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 197, 1, 3)
)
_NtpAssociationTable_Object = MibTable
ntpAssociationTable = _NtpAssociationTable_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ntpAssociationTable.setStatus("current")
_NtpAssociationEntry_Object = MibTableRow
ntpAssociationEntry = _NtpAssociationEntry_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 1, 1)
)
ntpAssociationEntry.setIndexNames(
    (0, "NTPv4-MIB", "ntpAssocId"),
)
if mibBuilder.loadTexts:
    ntpAssociationEntry.setStatus("current")


class _NtpAssocId_Type(Unsigned32):
    """Custom type ntpAssocId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_NtpAssocId_Type.__name__ = "Unsigned32"
_NtpAssocId_Object = MibTableColumn
ntpAssocId = _NtpAssocId_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 1, 1, 1),
    _NtpAssocId_Type()
)
ntpAssocId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpAssocId.setStatus("current")
_NtpAssocName_Type = Utf8String
_NtpAssocName_Object = MibTableColumn
ntpAssocName = _NtpAssocName_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 1, 1, 2),
    _NtpAssocName_Type()
)
ntpAssocName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocName.setStatus("current")
_NtpAssocRefId_Type = DisplayString
_NtpAssocRefId_Object = MibTableColumn
ntpAssocRefId = _NtpAssocRefId_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 1, 1, 3),
    _NtpAssocRefId_Type()
)
ntpAssocRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocRefId.setStatus("current")
_NtpAssocAddressType_Type = InetAddressType
_NtpAssocAddressType_Object = MibTableColumn
ntpAssocAddressType = _NtpAssocAddressType_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 1, 1, 4),
    _NtpAssocAddressType_Type()
)
ntpAssocAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocAddressType.setStatus("current")


class _NtpAssocAddress_Type(InetAddress):
    """Custom type ntpAssocAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_NtpAssocAddress_Type.__name__ = "InetAddress"
_NtpAssocAddress_Object = MibTableColumn
ntpAssocAddress = _NtpAssocAddress_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 1, 1, 5),
    _NtpAssocAddress_Type()
)
ntpAssocAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocAddress.setStatus("current")
_NtpAssocOffset_Type = DisplayString
_NtpAssocOffset_Object = MibTableColumn
ntpAssocOffset = _NtpAssocOffset_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 1, 1, 6),
    _NtpAssocOffset_Type()
)
ntpAssocOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocOffset.setStatus("current")
_NtpAssocStratum_Type = NtpStratum
_NtpAssocStratum_Object = MibTableColumn
ntpAssocStratum = _NtpAssocStratum_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 1, 1, 7),
    _NtpAssocStratum_Type()
)
ntpAssocStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocStratum.setStatus("current")
_NtpAssocStatusJitter_Type = DisplayString
_NtpAssocStatusJitter_Object = MibTableColumn
ntpAssocStatusJitter = _NtpAssocStatusJitter_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 1, 1, 8),
    _NtpAssocStatusJitter_Type()
)
ntpAssocStatusJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocStatusJitter.setStatus("current")
_NtpAssocStatusDelay_Type = DisplayString
_NtpAssocStatusDelay_Object = MibTableColumn
ntpAssocStatusDelay = _NtpAssocStatusDelay_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 1, 1, 9),
    _NtpAssocStatusDelay_Type()
)
ntpAssocStatusDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocStatusDelay.setStatus("current")
_NtpAssocStatusDispersion_Type = DisplayString
_NtpAssocStatusDispersion_Object = MibTableColumn
ntpAssocStatusDispersion = _NtpAssocStatusDispersion_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 1, 1, 10),
    _NtpAssocStatusDispersion_Type()
)
ntpAssocStatusDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocStatusDispersion.setStatus("current")
_NtpAssociationStatisticsTable_Object = MibTable
ntpAssociationStatisticsTable = _NtpAssociationStatisticsTable_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ntpAssociationStatisticsTable.setStatus("current")
_NtpAssociationStatisticsEntry_Object = MibTableRow
ntpAssociationStatisticsEntry = _NtpAssociationStatisticsEntry_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 2, 1)
)
ntpAssociationStatisticsEntry.setIndexNames(
    (0, "NTPv4-MIB", "ntpAssocId"),
)
if mibBuilder.loadTexts:
    ntpAssociationStatisticsEntry.setStatus("current")
_NtpAssocStatInPkts_Type = Counter32
_NtpAssocStatInPkts_Object = MibTableColumn
ntpAssocStatInPkts = _NtpAssocStatInPkts_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 2, 1, 1),
    _NtpAssocStatInPkts_Type()
)
ntpAssocStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocStatInPkts.setStatus("current")
if mibBuilder.loadTexts:
    ntpAssocStatInPkts.setUnits("packets")
_NtpAssocStatOutPkts_Type = Counter32
_NtpAssocStatOutPkts_Object = MibTableColumn
ntpAssocStatOutPkts = _NtpAssocStatOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 2, 1, 2),
    _NtpAssocStatOutPkts_Type()
)
ntpAssocStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocStatOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    ntpAssocStatOutPkts.setUnits("packets")
_NtpAssocStatProtocolError_Type = Counter32
_NtpAssocStatProtocolError_Object = MibTableColumn
ntpAssocStatProtocolError = _NtpAssocStatProtocolError_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 3, 2, 1, 3),
    _NtpAssocStatProtocolError_Type()
)
ntpAssocStatProtocolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocStatProtocolError.setStatus("current")
if mibBuilder.loadTexts:
    ntpAssocStatProtocolError.setUnits("packets")
_NtpEntControl_ObjectIdentity = ObjectIdentity
ntpEntControl = _NtpEntControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 197, 1, 4)
)


class _NtpEntHeartbeatInterval_Type(Unsigned32):
    """Custom type ntpEntHeartbeatInterval based on Unsigned32"""
    defaultValue = 60


_NtpEntHeartbeatInterval_Object = MibScalar
ntpEntHeartbeatInterval = _NtpEntHeartbeatInterval_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 4, 1),
    _NtpEntHeartbeatInterval_Type()
)
ntpEntHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpEntHeartbeatInterval.setStatus("current")
if mibBuilder.loadTexts:
    ntpEntHeartbeatInterval.setUnits("seconds")


class _NtpEntNotifBits_Type(Bits):
    """Custom type ntpEntNotifBits based on Bits"""
    namedValues = NamedValues(
        *(("entNotifAddAssociation", 4),
          ("entNotifConfigChanged", 6),
          ("entNotifHeartbeat", 8),
          ("entNotifLeapSecondAnnounced", 7),
          ("entNotifModeChange", 1),
          ("entNotifRemoveAssociation", 5),
          ("entNotifStratumChange", 2),
          ("entNotifSyspeerChanged", 3),
          ("notUsed", 0))
    )

_NtpEntNotifBits_Type.__name__ = "Bits"
_NtpEntNotifBits_Object = MibScalar
ntpEntNotifBits = _NtpEntNotifBits_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 4, 2),
    _NtpEntNotifBits_Type()
)
ntpEntNotifBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpEntNotifBits.setStatus("current")
_NtpEntNotifObjects_ObjectIdentity = ObjectIdentity
ntpEntNotifObjects = _NtpEntNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 197, 1, 5)
)


class _NtpEntNotifMessage_Type(Utf8String):
    """Custom type ntpEntNotifMessage based on Utf8String"""
    defaultValue = OctetString("no event")


_NtpEntNotifMessage_Object = MibScalar
ntpEntNotifMessage = _NtpEntNotifMessage_Object(
    (1, 3, 6, 1, 2, 1, 197, 1, 5, 1),
    _NtpEntNotifMessage_Type()
)
ntpEntNotifMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntpEntNotifMessage.setStatus("current")
_NtpEntConformance_ObjectIdentity = ObjectIdentity
ntpEntConformance = _NtpEntConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 197, 2)
)
_NtpEntCompliances_ObjectIdentity = ObjectIdentity
ntpEntCompliances = _NtpEntCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 197, 2, 1)
)
_NtpEntGroups_ObjectIdentity = ObjectIdentity
ntpEntGroups = _NtpEntGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 197, 2, 2)
)

# Managed Objects groups

ntpEntObjectsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 197, 2, 2, 1)
)
ntpEntObjectsGroup1.setObjects(
      *(("NTPv4-MIB", "ntpEntSoftwareName"),
        ("NTPv4-MIB", "ntpEntSoftwareVersion"),
        ("NTPv4-MIB", "ntpEntSoftwareVendor"),
        ("NTPv4-MIB", "ntpEntSystemType"),
        ("NTPv4-MIB", "ntpEntStatusEntityUptime"),
        ("NTPv4-MIB", "ntpEntStatusDateTime"),
        ("NTPv4-MIB", "ntpAssocName"),
        ("NTPv4-MIB", "ntpAssocRefId"),
        ("NTPv4-MIB", "ntpAssocAddressType"),
        ("NTPv4-MIB", "ntpAssocAddress"))
)
if mibBuilder.loadTexts:
    ntpEntObjectsGroup1.setStatus("current")

ntpEntObjectsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 197, 2, 2, 2)
)
ntpEntObjectsGroup2.setObjects(
      *(("NTPv4-MIB", "ntpEntTimeResolution"),
        ("NTPv4-MIB", "ntpEntTimePrecision"),
        ("NTPv4-MIB", "ntpEntTimeDistance"),
        ("NTPv4-MIB", "ntpEntStatusCurrentMode"),
        ("NTPv4-MIB", "ntpEntStatusStratum"),
        ("NTPv4-MIB", "ntpEntStatusActiveRefSourceId"),
        ("NTPv4-MIB", "ntpEntStatusActiveRefSourceName"),
        ("NTPv4-MIB", "ntpEntStatusActiveOffset"),
        ("NTPv4-MIB", "ntpEntStatusNumberOfRefSources"),
        ("NTPv4-MIB", "ntpEntStatusDispersion"),
        ("NTPv4-MIB", "ntpEntStatusLeapSecond"),
        ("NTPv4-MIB", "ntpEntStatusLeapSecDirection"),
        ("NTPv4-MIB", "ntpEntStatusInPkts"),
        ("NTPv4-MIB", "ntpEntStatusOutPkts"),
        ("NTPv4-MIB", "ntpEntStatusBadVersion"),
        ("NTPv4-MIB", "ntpEntStatusProtocolError"),
        ("NTPv4-MIB", "ntpEntStatusNotifications"),
        ("NTPv4-MIB", "ntpEntStatPktSent"),
        ("NTPv4-MIB", "ntpEntStatPktReceived"),
        ("NTPv4-MIB", "ntpAssocOffset"),
        ("NTPv4-MIB", "ntpAssocStratum"),
        ("NTPv4-MIB", "ntpAssocStatusJitter"),
        ("NTPv4-MIB", "ntpAssocStatusDelay"),
        ("NTPv4-MIB", "ntpAssocStatusDispersion"),
        ("NTPv4-MIB", "ntpAssocStatInPkts"),
        ("NTPv4-MIB", "ntpAssocStatOutPkts"),
        ("NTPv4-MIB", "ntpAssocStatProtocolError"),
        ("NTPv4-MIB", "ntpEntHeartbeatInterval"),
        ("NTPv4-MIB", "ntpEntNotifBits"),
        ("NTPv4-MIB", "ntpEntNotifMessage"))
)
if mibBuilder.loadTexts:
    ntpEntObjectsGroup2.setStatus("current")


# Notification objects

ntpEntNotifModeChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 197, 0, 1)
)
ntpEntNotifModeChange.setObjects(
    ("NTPv4-MIB", "ntpEntStatusCurrentMode")
)
if mibBuilder.loadTexts:
    ntpEntNotifModeChange.setStatus(
        "current"
    )

ntpEntNotifStratumChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 197, 0, 2)
)
ntpEntNotifStratumChange.setObjects(
      *(("NTPv4-MIB", "ntpEntStatusDateTime"),
        ("NTPv4-MIB", "ntpEntStatusStratum"),
        ("NTPv4-MIB", "ntpEntNotifMessage"))
)
if mibBuilder.loadTexts:
    ntpEntNotifStratumChange.setStatus(
        "current"
    )

ntpEntNotifSyspeerChanged = NotificationType(
    (1, 3, 6, 1, 2, 1, 197, 0, 3)
)
ntpEntNotifSyspeerChanged.setObjects(
      *(("NTPv4-MIB", "ntpEntStatusDateTime"),
        ("NTPv4-MIB", "ntpEntStatusActiveRefSourceId"),
        ("NTPv4-MIB", "ntpEntNotifMessage"))
)
if mibBuilder.loadTexts:
    ntpEntNotifSyspeerChanged.setStatus(
        "current"
    )

ntpEntNotifAddAssociation = NotificationType(
    (1, 3, 6, 1, 2, 1, 197, 0, 4)
)
ntpEntNotifAddAssociation.setObjects(
      *(("NTPv4-MIB", "ntpEntStatusDateTime"),
        ("NTPv4-MIB", "ntpAssocName"),
        ("NTPv4-MIB", "ntpEntNotifMessage"))
)
if mibBuilder.loadTexts:
    ntpEntNotifAddAssociation.setStatus(
        "current"
    )

ntpEntNotifRemoveAssociation = NotificationType(
    (1, 3, 6, 1, 2, 1, 197, 0, 5)
)
ntpEntNotifRemoveAssociation.setObjects(
      *(("NTPv4-MIB", "ntpEntStatusDateTime"),
        ("NTPv4-MIB", "ntpAssocName"),
        ("NTPv4-MIB", "ntpEntNotifMessage"))
)
if mibBuilder.loadTexts:
    ntpEntNotifRemoveAssociation.setStatus(
        "current"
    )

ntpEntNotifConfigChanged = NotificationType(
    (1, 3, 6, 1, 2, 1, 197, 0, 6)
)
ntpEntNotifConfigChanged.setObjects(
      *(("NTPv4-MIB", "ntpEntStatusDateTime"),
        ("NTPv4-MIB", "ntpEntNotifMessage"))
)
if mibBuilder.loadTexts:
    ntpEntNotifConfigChanged.setStatus(
        "current"
    )

ntpEntNotifLeapSecondAnnounced = NotificationType(
    (1, 3, 6, 1, 2, 1, 197, 0, 7)
)
ntpEntNotifLeapSecondAnnounced.setObjects(
      *(("NTPv4-MIB", "ntpEntStatusDateTime"),
        ("NTPv4-MIB", "ntpEntNotifMessage"))
)
if mibBuilder.loadTexts:
    ntpEntNotifLeapSecondAnnounced.setStatus(
        "current"
    )

ntpEntNotifHeartbeat = NotificationType(
    (1, 3, 6, 1, 2, 1, 197, 0, 8)
)
ntpEntNotifHeartbeat.setObjects(
      *(("NTPv4-MIB", "ntpEntStatusDateTime"),
        ("NTPv4-MIB", "ntpEntStatusCurrentMode"),
        ("NTPv4-MIB", "ntpEntHeartbeatInterval"),
        ("NTPv4-MIB", "ntpEntNotifMessage"))
)
if mibBuilder.loadTexts:
    ntpEntNotifHeartbeat.setStatus(
        "current"
    )


# Notifications groups

ntpEntNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 197, 2, 2, 3)
)
ntpEntNotifGroup.setObjects(
      *(("NTPv4-MIB", "ntpEntNotifModeChange"),
        ("NTPv4-MIB", "ntpEntNotifStratumChange"),
        ("NTPv4-MIB", "ntpEntNotifSyspeerChanged"),
        ("NTPv4-MIB", "ntpEntNotifAddAssociation"),
        ("NTPv4-MIB", "ntpEntNotifRemoveAssociation"),
        ("NTPv4-MIB", "ntpEntNotifConfigChanged"),
        ("NTPv4-MIB", "ntpEntNotifLeapSecondAnnounced"),
        ("NTPv4-MIB", "ntpEntNotifHeartbeat"))
)
if mibBuilder.loadTexts:
    ntpEntNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ntpEntNTPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 197, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntpEntNTPCompliance.setStatus(
        "current"
    )

ntpEntSNTPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 197, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ntpEntSNTPCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTPv4-MIB",
    **{"NtpStratum": NtpStratum,
       "NtpDateTime": NtpDateTime,
       "ntpSnmpMIB": ntpSnmpMIB,
       "ntpEntNotifications": ntpEntNotifications,
       "ntpEntNotifModeChange": ntpEntNotifModeChange,
       "ntpEntNotifStratumChange": ntpEntNotifStratumChange,
       "ntpEntNotifSyspeerChanged": ntpEntNotifSyspeerChanged,
       "ntpEntNotifAddAssociation": ntpEntNotifAddAssociation,
       "ntpEntNotifRemoveAssociation": ntpEntNotifRemoveAssociation,
       "ntpEntNotifConfigChanged": ntpEntNotifConfigChanged,
       "ntpEntNotifLeapSecondAnnounced": ntpEntNotifLeapSecondAnnounced,
       "ntpEntNotifHeartbeat": ntpEntNotifHeartbeat,
       "ntpSnmpMIBObjects": ntpSnmpMIBObjects,
       "ntpEntInfo": ntpEntInfo,
       "ntpEntSoftwareName": ntpEntSoftwareName,
       "ntpEntSoftwareVersion": ntpEntSoftwareVersion,
       "ntpEntSoftwareVendor": ntpEntSoftwareVendor,
       "ntpEntSystemType": ntpEntSystemType,
       "ntpEntTimeResolution": ntpEntTimeResolution,
       "ntpEntTimePrecision": ntpEntTimePrecision,
       "ntpEntTimeDistance": ntpEntTimeDistance,
       "ntpEntStatus": ntpEntStatus,
       "ntpEntStatusCurrentMode": ntpEntStatusCurrentMode,
       "ntpEntStatusStratum": ntpEntStatusStratum,
       "ntpEntStatusActiveRefSourceId": ntpEntStatusActiveRefSourceId,
       "ntpEntStatusActiveRefSourceName": ntpEntStatusActiveRefSourceName,
       "ntpEntStatusActiveOffset": ntpEntStatusActiveOffset,
       "ntpEntStatusNumberOfRefSources": ntpEntStatusNumberOfRefSources,
       "ntpEntStatusDispersion": ntpEntStatusDispersion,
       "ntpEntStatusEntityUptime": ntpEntStatusEntityUptime,
       "ntpEntStatusDateTime": ntpEntStatusDateTime,
       "ntpEntStatusLeapSecond": ntpEntStatusLeapSecond,
       "ntpEntStatusLeapSecDirection": ntpEntStatusLeapSecDirection,
       "ntpEntStatusInPkts": ntpEntStatusInPkts,
       "ntpEntStatusOutPkts": ntpEntStatusOutPkts,
       "ntpEntStatusBadVersion": ntpEntStatusBadVersion,
       "ntpEntStatusProtocolError": ntpEntStatusProtocolError,
       "ntpEntStatusNotifications": ntpEntStatusNotifications,
       "ntpEntStatPktModeTable": ntpEntStatPktModeTable,
       "ntpEntStatPktModeEntry": ntpEntStatPktModeEntry,
       "ntpEntStatPktMode": ntpEntStatPktMode,
       "ntpEntStatPktSent": ntpEntStatPktSent,
       "ntpEntStatPktReceived": ntpEntStatPktReceived,
       "ntpAssociation": ntpAssociation,
       "ntpAssociationTable": ntpAssociationTable,
       "ntpAssociationEntry": ntpAssociationEntry,
       "ntpAssocId": ntpAssocId,
       "ntpAssocName": ntpAssocName,
       "ntpAssocRefId": ntpAssocRefId,
       "ntpAssocAddressType": ntpAssocAddressType,
       "ntpAssocAddress": ntpAssocAddress,
       "ntpAssocOffset": ntpAssocOffset,
       "ntpAssocStratum": ntpAssocStratum,
       "ntpAssocStatusJitter": ntpAssocStatusJitter,
       "ntpAssocStatusDelay": ntpAssocStatusDelay,
       "ntpAssocStatusDispersion": ntpAssocStatusDispersion,
       "ntpAssociationStatisticsTable": ntpAssociationStatisticsTable,
       "ntpAssociationStatisticsEntry": ntpAssociationStatisticsEntry,
       "ntpAssocStatInPkts": ntpAssocStatInPkts,
       "ntpAssocStatOutPkts": ntpAssocStatOutPkts,
       "ntpAssocStatProtocolError": ntpAssocStatProtocolError,
       "ntpEntControl": ntpEntControl,
       "ntpEntHeartbeatInterval": ntpEntHeartbeatInterval,
       "ntpEntNotifBits": ntpEntNotifBits,
       "ntpEntNotifObjects": ntpEntNotifObjects,
       "ntpEntNotifMessage": ntpEntNotifMessage,
       "ntpEntConformance": ntpEntConformance,
       "ntpEntCompliances": ntpEntCompliances,
       "ntpEntNTPCompliance": ntpEntNTPCompliance,
       "ntpEntSNTPCompliance": ntpEntSNTPCompliance,
       "ntpEntGroups": ntpEntGroups,
       "ntpEntObjectsGroup1": ntpEntObjectsGroup1,
       "ntpEntObjectsGroup2": ntpEntObjectsGroup2,
       "ntpEntNotifGroup": ntpEntNotifGroup}
)
