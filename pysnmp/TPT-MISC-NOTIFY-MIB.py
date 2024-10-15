# SNMP MIB module (TPT-MISC-NOTIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-MISC-NOTIFY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:58 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(SslInspectedFlag,) = mibBuilder.importSymbols(
    "TPT-POLICY-MIB",
    "SslInspectedFlag")

(tpt_tpa_eventsV2,
 tpt_tpa_objs,
 tpt_tpa_unkparams) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-eventsV2",
    "tpt-tpa-objs",
    "tpt-tpa-unkparams")


# MODULE-IDENTITY

tpt_misc_notify = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 2)
)
tpt_misc_notify.setRevisions(
        ("2016-05-25 18:54",
         "2016-05-03 17:26",
         "2015-05-28 13:30",
         "2014-11-11 18:43")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LogFileType(Integer32, TextualConvention):
    status = "current"
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
        *(("alert", 2),
          ("audit", 5),
          ("block", 3),
          ("peer", 4),
          ("quarantine", 6),
          ("system", 1))
    )



class DiscoveryDelta(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changed", 1),
          ("unchanged", 2))
    )



class SystemLogSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("alert", 5),
          ("critical", 1),
          ("debug", 8),
          ("emergency", 3),
          ("error", 2),
          ("info", 7),
          ("notice", 6),
          ("warning", 4))
    )



class AddOrRemove(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )



class CongestionThresholdPhase(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continuing", 2),
          ("entering", 1),
          ("exiting", 3))
    )



class AuditLogResult(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("success", 1))
    )



class AuditLogCategory(Integer32, TextualConvention):
    status = "current"
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
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("boot", 9),
          ("cf", 24),
          ("cfg", 12),
          ("connTable", 21),
          ("device", 13),
          ("general", 2),
          ("ha", 18),
          ("host", 11),
          ("hostComm", 22),
          ("ipFilter", 20),
          ("license", 17),
          ("login", 3),
          ("logout", 4),
          ("monitor", 19),
          ("policy", 7),
          ("report", 10),
          ("segment", 16),
          ("server", 15),
          ("sms", 14),
          ("time", 6),
          ("tse", 23),
          ("undefined", 1),
          ("update", 8),
          ("user", 5))
    )



# MIB Managed Objects in the order of their OIDs



class _TptMiscNotifyDeviceID_Type(OctetString):
    """Custom type tptMiscNotifyDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptMiscNotifyDeviceID_Type.__name__ = "OctetString"
_TptMiscNotifyDeviceID_Object = MibScalar
tptMiscNotifyDeviceID = _TptMiscNotifyDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 31),
    _TptMiscNotifyDeviceID_Type()
)
tptMiscNotifyDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptMiscNotifyDeviceID.setStatus("current")
_TptRolloverNotifyFileType_Type = LogFileType
_TptRolloverNotifyFileType_Object = MibScalar
tptRolloverNotifyFileType = _TptRolloverNotifyFileType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 32),
    _TptRolloverNotifyFileType_Type()
)
tptRolloverNotifyFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptRolloverNotifyFileType.setStatus("current")
_TptRolloverNotifyMaxFiles_Type = Unsigned32
_TptRolloverNotifyMaxFiles_Object = MibScalar
tptRolloverNotifyMaxFiles = _TptRolloverNotifyMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 33),
    _TptRolloverNotifyMaxFiles_Type()
)
tptRolloverNotifyMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptRolloverNotifyMaxFiles.setStatus("deprecated")
_TptRolloverNotifyNumFiles_Type = Unsigned32
_TptRolloverNotifyNumFiles_Object = MibScalar
tptRolloverNotifyNumFiles = _TptRolloverNotifyNumFiles_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 34),
    _TptRolloverNotifyNumFiles_Type()
)
tptRolloverNotifyNumFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptRolloverNotifyNumFiles.setStatus("deprecated")
_TptRolloverNotifyTime_Type = Unsigned32
_TptRolloverNotifyTime_Object = MibScalar
tptRolloverNotifyTime = _TptRolloverNotifyTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 35),
    _TptRolloverNotifyTime_Type()
)
tptRolloverNotifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptRolloverNotifyTime.setStatus("current")


class _TptDiscoveryNotifyScanID_Type(OctetString):
    """Custom type tptDiscoveryNotifyScanID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptDiscoveryNotifyScanID_Type.__name__ = "OctetString"
_TptDiscoveryNotifyScanID_Object = MibScalar
tptDiscoveryNotifyScanID = _TptDiscoveryNotifyScanID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 42),
    _TptDiscoveryNotifyScanID_Type()
)
tptDiscoveryNotifyScanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyScanID.setStatus("obsolete")


class _TptDiscoveryNotifySegmentName_Type(OctetString):
    """Custom type tptDiscoveryNotifySegmentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TptDiscoveryNotifySegmentName_Type.__name__ = "OctetString"
_TptDiscoveryNotifySegmentName_Object = MibScalar
tptDiscoveryNotifySegmentName = _TptDiscoveryNotifySegmentName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 43),
    _TptDiscoveryNotifySegmentName_Type()
)
tptDiscoveryNotifySegmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifySegmentName.setStatus("obsolete")


class _TptDiscoveryNotifyScanRange_Type(OctetString):
    """Custom type tptDiscoveryNotifyScanRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptDiscoveryNotifyScanRange_Type.__name__ = "OctetString"
_TptDiscoveryNotifyScanRange_Object = MibScalar
tptDiscoveryNotifyScanRange = _TptDiscoveryNotifyScanRange_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 44),
    _TptDiscoveryNotifyScanRange_Type()
)
tptDiscoveryNotifyScanRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyScanRange.setStatus("obsolete")
_TptDiscoveryNotifyDelta_Type = DiscoveryDelta
_TptDiscoveryNotifyDelta_Object = MibScalar
tptDiscoveryNotifyDelta = _TptDiscoveryNotifyDelta_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 45),
    _TptDiscoveryNotifyDelta_Type()
)
tptDiscoveryNotifyDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyDelta.setStatus("obsolete")
_TptDiscoveryNotifyNewHosts_Type = Integer32
_TptDiscoveryNotifyNewHosts_Object = MibScalar
tptDiscoveryNotifyNewHosts = _TptDiscoveryNotifyNewHosts_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 46),
    _TptDiscoveryNotifyNewHosts_Type()
)
tptDiscoveryNotifyNewHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyNewHosts.setStatus("obsolete")
_TptDiscoveryNotifyChanged_Type = Integer32
_TptDiscoveryNotifyChanged_Object = MibScalar
tptDiscoveryNotifyChanged = _TptDiscoveryNotifyChanged_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 47),
    _TptDiscoveryNotifyChanged_Type()
)
tptDiscoveryNotifyChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyChanged.setStatus("obsolete")
_TptDiscoveryNotifyUnchanged_Type = Integer32
_TptDiscoveryNotifyUnchanged_Object = MibScalar
tptDiscoveryNotifyUnchanged = _TptDiscoveryNotifyUnchanged_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 48),
    _TptDiscoveryNotifyUnchanged_Type()
)
tptDiscoveryNotifyUnchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyUnchanged.setStatus("obsolete")
_TptDiscoveryNotifyNotFound_Type = Integer32
_TptDiscoveryNotifyNotFound_Object = MibScalar
tptDiscoveryNotifyNotFound = _TptDiscoveryNotifyNotFound_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 49),
    _TptDiscoveryNotifyNotFound_Type()
)
tptDiscoveryNotifyNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyNotFound.setStatus("obsolete")
_TptDiscoveryNotifyUnknown_Type = Integer32
_TptDiscoveryNotifyUnknown_Object = MibScalar
tptDiscoveryNotifyUnknown = _TptDiscoveryNotifyUnknown_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 50),
    _TptDiscoveryNotifyUnknown_Type()
)
tptDiscoveryNotifyUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyUnknown.setStatus("obsolete")
_TptDiscoveryNotifyStartTime_Type = Unsigned32
_TptDiscoveryNotifyStartTime_Object = MibScalar
tptDiscoveryNotifyStartTime = _TptDiscoveryNotifyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 51),
    _TptDiscoveryNotifyStartTime_Type()
)
tptDiscoveryNotifyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyStartTime.setStatus("obsolete")
_TptDiscoveryNotifyStopTime_Type = Unsigned32
_TptDiscoveryNotifyStopTime_Object = MibScalar
tptDiscoveryNotifyStopTime = _TptDiscoveryNotifyStopTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 52),
    _TptDiscoveryNotifyStopTime_Type()
)
tptDiscoveryNotifyStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyStopTime.setStatus("obsolete")


class _TptDiscoveryNotifyErrorText_Type(OctetString):
    """Custom type tptDiscoveryNotifyErrorText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TptDiscoveryNotifyErrorText_Type.__name__ = "OctetString"
_TptDiscoveryNotifyErrorText_Object = MibScalar
tptDiscoveryNotifyErrorText = _TptDiscoveryNotifyErrorText_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 53),
    _TptDiscoveryNotifyErrorText_Type()
)
tptDiscoveryNotifyErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyErrorText.setStatus("obsolete")
_TptDiscoveryNotifyHostNetAddr_Type = IpAddress
_TptDiscoveryNotifyHostNetAddr_Object = MibScalar
tptDiscoveryNotifyHostNetAddr = _TptDiscoveryNotifyHostNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 54),
    _TptDiscoveryNotifyHostNetAddr_Type()
)
tptDiscoveryNotifyHostNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyHostNetAddr.setStatus("obsolete")


class _TptDiscoveryNotifyHostDeviceID_Type(OctetString):
    """Custom type tptDiscoveryNotifyHostDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptDiscoveryNotifyHostDeviceID_Type.__name__ = "OctetString"
_TptDiscoveryNotifyHostDeviceID_Object = MibScalar
tptDiscoveryNotifyHostDeviceID = _TptDiscoveryNotifyHostDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 55),
    _TptDiscoveryNotifyHostDeviceID_Type()
)
tptDiscoveryNotifyHostDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifyHostDeviceID.setStatus("obsolete")


class _TptDiscoveryNotifySchedID_Type(OctetString):
    """Custom type tptDiscoveryNotifySchedID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptDiscoveryNotifySchedID_Type.__name__ = "OctetString"
_TptDiscoveryNotifySchedID_Object = MibScalar
tptDiscoveryNotifySchedID = _TptDiscoveryNotifySchedID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 56),
    _TptDiscoveryNotifySchedID_Type()
)
tptDiscoveryNotifySchedID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptDiscoveryNotifySchedID.setStatus("obsolete")


class _TptSystemLogNotifyText_Type(OctetString):
    """Custom type tptSystemLogNotifyText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_TptSystemLogNotifyText_Type.__name__ = "OctetString"
_TptSystemLogNotifyText_Object = MibScalar
tptSystemLogNotifyText = _TptSystemLogNotifyText_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 92),
    _TptSystemLogNotifyText_Type()
)
tptSystemLogNotifyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptSystemLogNotifyText.setStatus("current")
_TptSystemLogNotifySequence_Type = Counter64
_TptSystemLogNotifySequence_Object = MibScalar
tptSystemLogNotifySequence = _TptSystemLogNotifySequence_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 93),
    _TptSystemLogNotifySequence_Type()
)
tptSystemLogNotifySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptSystemLogNotifySequence.setStatus("current")
_TptSystemLogNotifySeverity_Type = SystemLogSeverity
_TptSystemLogNotifySeverity_Object = MibScalar
tptSystemLogNotifySeverity = _TptSystemLogNotifySeverity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 94),
    _TptSystemLogNotifySeverity_Type()
)
tptSystemLogNotifySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptSystemLogNotifySeverity.setStatus("current")
_TptSystemLogNotifyTimeSec_Type = Unsigned32
_TptSystemLogNotifyTimeSec_Object = MibScalar
tptSystemLogNotifyTimeSec = _TptSystemLogNotifyTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 95),
    _TptSystemLogNotifyTimeSec_Type()
)
tptSystemLogNotifyTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptSystemLogNotifyTimeSec.setStatus("current")
_TptSystemLogNotifyTimeNano_Type = Unsigned32
_TptSystemLogNotifyTimeNano_Object = MibScalar
tptSystemLogNotifyTimeNano = _TptSystemLogNotifyTimeNano_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 96),
    _TptSystemLogNotifyTimeNano_Type()
)
tptSystemLogNotifyTimeNano.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptSystemLogNotifyTimeNano.setStatus("current")
_TptQuarantineNotifyHostNetAddr_Type = IpAddress
_TptQuarantineNotifyHostNetAddr_Object = MibScalar
tptQuarantineNotifyHostNetAddr = _TptQuarantineNotifyHostNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 132),
    _TptQuarantineNotifyHostNetAddr_Type()
)
tptQuarantineNotifyHostNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptQuarantineNotifyHostNetAddr.setStatus("current")


class _TptQuarantineNotifyReason_Type(OctetString):
    """Custom type tptQuarantineNotifyReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptQuarantineNotifyReason_Type.__name__ = "OctetString"
_TptQuarantineNotifyReason_Object = MibScalar
tptQuarantineNotifyReason = _TptQuarantineNotifyReason_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 133),
    _TptQuarantineNotifyReason_Type()
)
tptQuarantineNotifyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptQuarantineNotifyReason.setStatus("current")


class _TptQuarantineNotifySegmentName_Type(OctetString):
    """Custom type tptQuarantineNotifySegmentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TptQuarantineNotifySegmentName_Type.__name__ = "OctetString"
_TptQuarantineNotifySegmentName_Object = MibScalar
tptQuarantineNotifySegmentName = _TptQuarantineNotifySegmentName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 134),
    _TptQuarantineNotifySegmentName_Type()
)
tptQuarantineNotifySegmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptQuarantineNotifySegmentName.setStatus("current")
_TptQuarantineNotifyAction_Type = AddOrRemove
_TptQuarantineNotifyAction_Object = MibScalar
tptQuarantineNotifyAction = _TptQuarantineNotifyAction_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 135),
    _TptQuarantineNotifyAction_Type()
)
tptQuarantineNotifyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptQuarantineNotifyAction.setStatus("current")
_TptQuarantineNotifyHostNetAddrV6_Type = Ipv6Address
_TptQuarantineNotifyHostNetAddrV6_Object = MibScalar
tptQuarantineNotifyHostNetAddrV6 = _TptQuarantineNotifyHostNetAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 136),
    _TptQuarantineNotifyHostNetAddrV6_Type()
)
tptQuarantineNotifyHostNetAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptQuarantineNotifyHostNetAddrV6.setStatus("current")
_TptCongestionPacketLoss_Type = Unsigned32
_TptCongestionPacketLoss_Object = MibScalar
tptCongestionPacketLoss = _TptCongestionPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 153),
    _TptCongestionPacketLoss_Type()
)
tptCongestionPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptCongestionPacketLoss.setStatus("current")
_TptCongestionNotifyPhase_Type = CongestionThresholdPhase
_TptCongestionNotifyPhase_Object = MibScalar
tptCongestionNotifyPhase = _TptCongestionNotifyPhase_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 154),
    _TptCongestionNotifyPhase_Type()
)
tptCongestionNotifyPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptCongestionNotifyPhase.setStatus("current")
_TptCongestionThreshold_Type = Unsigned32
_TptCongestionThreshold_Object = MibScalar
tptCongestionThreshold = _TptCongestionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 155),
    _TptCongestionThreshold_Type()
)
tptCongestionThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptCongestionThreshold.setStatus("current")
_TptTier3CongestionPacketLoss_Type = Unsigned32
_TptTier3CongestionPacketLoss_Object = MibScalar
tptTier3CongestionPacketLoss = _TptTier3CongestionPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 156),
    _TptTier3CongestionPacketLoss_Type()
)
tptTier3CongestionPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptTier3CongestionPacketLoss.setStatus("current")
_TptTier3CongestionNotifyPhase_Type = CongestionThresholdPhase
_TptTier3CongestionNotifyPhase_Object = MibScalar
tptTier3CongestionNotifyPhase = _TptTier3CongestionNotifyPhase_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 157),
    _TptTier3CongestionNotifyPhase_Type()
)
tptTier3CongestionNotifyPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptTier3CongestionNotifyPhase.setStatus("current")
_TptTier3CongestionThreshold_Type = Unsigned32
_TptTier3CongestionThreshold_Object = MibScalar
tptTier3CongestionThreshold = _TptTier3CongestionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 158),
    _TptTier3CongestionThreshold_Type()
)
tptTier3CongestionThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptTier3CongestionThreshold.setStatus("current")
_TptAuditLogNotifyTime_Type = DateAndTime
_TptAuditLogNotifyTime_Object = MibScalar
tptAuditLogNotifyTime = _TptAuditLogNotifyTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 170),
    _TptAuditLogNotifyTime_Type()
)
tptAuditLogNotifyTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptAuditLogNotifyTime.setStatus("current")
_TptAuditLogNotifyAccess_Type = Unsigned32
_TptAuditLogNotifyAccess_Object = MibScalar
tptAuditLogNotifyAccess = _TptAuditLogNotifyAccess_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 171),
    _TptAuditLogNotifyAccess_Type()
)
tptAuditLogNotifyAccess.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptAuditLogNotifyAccess.setStatus("current")


class _TptAuditLogNotifyType_Type(SnmpAdminString):
    """Custom type tptAuditLogNotifyType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptAuditLogNotifyType_Type.__name__ = "SnmpAdminString"
_TptAuditLogNotifyType_Object = MibScalar
tptAuditLogNotifyType = _TptAuditLogNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 172),
    _TptAuditLogNotifyType_Type()
)
tptAuditLogNotifyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptAuditLogNotifyType.setStatus("current")
_TptAuditLogNotifyIpAddrType_Type = InetAddressType
_TptAuditLogNotifyIpAddrType_Object = MibScalar
tptAuditLogNotifyIpAddrType = _TptAuditLogNotifyIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 173),
    _TptAuditLogNotifyIpAddrType_Type()
)
tptAuditLogNotifyIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptAuditLogNotifyIpAddrType.setStatus("current")
_TptAuditLogNotifyIpAddr_Type = InetAddress
_TptAuditLogNotifyIpAddr_Object = MibScalar
tptAuditLogNotifyIpAddr = _TptAuditLogNotifyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 174),
    _TptAuditLogNotifyIpAddr_Type()
)
tptAuditLogNotifyIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptAuditLogNotifyIpAddr.setStatus("current")
_TptAuditLogNotifyCategory_Type = AuditLogCategory
_TptAuditLogNotifyCategory_Object = MibScalar
tptAuditLogNotifyCategory = _TptAuditLogNotifyCategory_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 175),
    _TptAuditLogNotifyCategory_Type()
)
tptAuditLogNotifyCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptAuditLogNotifyCategory.setStatus("current")
_TptAuditLogNotifyResult_Type = AuditLogResult
_TptAuditLogNotifyResult_Object = MibScalar
tptAuditLogNotifyResult = _TptAuditLogNotifyResult_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 176),
    _TptAuditLogNotifyResult_Type()
)
tptAuditLogNotifyResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptAuditLogNotifyResult.setStatus("current")


class _TptAuditLogNotifyUser_Type(SnmpAdminString):
    """Custom type tptAuditLogNotifyUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TptAuditLogNotifyUser_Type.__name__ = "SnmpAdminString"
_TptAuditLogNotifyUser_Object = MibScalar
tptAuditLogNotifyUser = _TptAuditLogNotifyUser_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 177),
    _TptAuditLogNotifyUser_Type()
)
tptAuditLogNotifyUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptAuditLogNotifyUser.setStatus("current")


class _TptAuditLogNotifyMessage_Type(OctetString):
    """Custom type tptAuditLogNotifyMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_TptAuditLogNotifyMessage_Type.__name__ = "OctetString"
_TptAuditLogNotifyMessage_Object = MibScalar
tptAuditLogNotifyMessage = _TptAuditLogNotifyMessage_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 178),
    _TptAuditLogNotifyMessage_Type()
)
tptAuditLogNotifyMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptAuditLogNotifyMessage.setStatus("current")
_TptQuarantineNotifySslInspected_Type = SslInspectedFlag
_TptQuarantineNotifySslInspected_Object = MibScalar
tptQuarantineNotifySslInspected = _TptQuarantineNotifySslInspected_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 181),
    _TptQuarantineNotifySslInspected_Type()
)
tptQuarantineNotifySslInspected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptQuarantineNotifySslInspected.setStatus("current")
_TptAuditLogCapacityNotifyPercent_Type = Unsigned32
_TptAuditLogCapacityNotifyPercent_Object = MibScalar
tptAuditLogCapacityNotifyPercent = _TptAuditLogCapacityNotifyPercent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 201),
    _TptAuditLogCapacityNotifyPercent_Type()
)
tptAuditLogCapacityNotifyPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptAuditLogCapacityNotifyPercent.setStatus("current")
_TptAuditLogCapacityOrFailureNotifyTime_Type = Unsigned32
_TptAuditLogCapacityOrFailureNotifyTime_Object = MibScalar
tptAuditLogCapacityOrFailureNotifyTime = _TptAuditLogCapacityOrFailureNotifyTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 202),
    _TptAuditLogCapacityOrFailureNotifyTime_Type()
)
tptAuditLogCapacityOrFailureNotifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptAuditLogCapacityOrFailureNotifyTime.setStatus("current")

# Managed Objects groups


# Notification objects

tptManagedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 9)
)
tptManagedNotify.setObjects(
    ("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID")
)
if mibBuilder.loadTexts:
    tptManagedNotify.setStatus(
        "current"
    )

tptUnmanagedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 10)
)
tptUnmanagedNotify.setObjects(
    ("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID")
)
if mibBuilder.loadTexts:
    tptUnmanagedNotify.setStatus(
        "current"
    )

tptRolloverNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 11)
)
tptRolloverNotify.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-MISC-NOTIFY-MIB", "tptRolloverNotifyFileType"),
        ("TPT-MISC-NOTIFY-MIB", "tptRolloverNotifyTime"))
)
if mibBuilder.loadTexts:
    tptRolloverNotify.setStatus(
        "current"
    )

tptDiscoveryNotifyStartStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 12)
)
tptDiscoveryNotifyStartStop.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyScanID"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifySegmentName"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyScanRange"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyDelta"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyNewHosts"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyChanged"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyUnchanged"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyNotFound"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyUnknown"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyStartTime"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyStopTime"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyErrorText"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifySchedID"))
)
if mibBuilder.loadTexts:
    tptDiscoveryNotifyStartStop.setStatus(
        "obsolete"
    )

tptDiscoveryNotifyNewHost = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 13)
)
tptDiscoveryNotifyNewHost.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyHostNetAddr"),
        ("TPT-MISC-NOTIFY-MIB", "tptDiscoveryNotifyHostDeviceID"))
)
if mibBuilder.loadTexts:
    tptDiscoveryNotifyNewHost.setStatus(
        "obsolete"
    )

tptSystemLogNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 16)
)
tptSystemLogNotify.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-MISC-NOTIFY-MIB", "tptSystemLogNotifyText"),
        ("TPT-MISC-NOTIFY-MIB", "tptSystemLogNotifySequence"),
        ("TPT-MISC-NOTIFY-MIB", "tptSystemLogNotifySeverity"),
        ("TPT-MISC-NOTIFY-MIB", "tptSystemLogNotifyTimeSec"),
        ("TPT-MISC-NOTIFY-MIB", "tptSystemLogNotifyTimeNano"))
)
if mibBuilder.loadTexts:
    tptSystemLogNotify.setStatus(
        "current"
    )

tptQuarantineNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 20)
)
tptQuarantineNotify.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-MISC-NOTIFY-MIB", "tptQuarantineNotifyHostNetAddr"),
        ("TPT-MISC-NOTIFY-MIB", "tptQuarantineNotifyReason"),
        ("TPT-MISC-NOTIFY-MIB", "tptQuarantineNotifySegmentName"),
        ("TPT-MISC-NOTIFY-MIB", "tptQuarantineNotifyAction"),
        ("TPT-MISC-NOTIFY-MIB", "tptQuarantineNotifyHostNetAddrV6"),
        ("TPT-MISC-NOTIFY-MIB", "tptQuarantineNotifySslInspected"))
)
if mibBuilder.loadTexts:
    tptQuarantineNotify.setStatus(
        "current"
    )

tptCongestionThresholdNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 25)
)
tptCongestionThresholdNotify.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-MISC-NOTIFY-MIB", "tptCongestionNotifyPhase"),
        ("TPT-MISC-NOTIFY-MIB", "tptCongestionPacketLoss"),
        ("TPT-MISC-NOTIFY-MIB", "tptCongestionThreshold"))
)
if mibBuilder.loadTexts:
    tptCongestionThresholdNotify.setStatus(
        "current"
    )

tptiTier3CongestionThresholdNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 26)
)
tptiTier3CongestionThresholdNotify.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-MISC-NOTIFY-MIB", "tptTier3CongestionNotifyPhase"),
        ("TPT-MISC-NOTIFY-MIB", "tptTier3CongestionPacketLoss"),
        ("TPT-MISC-NOTIFY-MIB", "tptTier3CongestionThreshold"))
)
if mibBuilder.loadTexts:
    tptiTier3CongestionThresholdNotify.setStatus(
        "current"
    )

tptAuditLogNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 60)
)
tptAuditLogNotify.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyTime"),
        ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyAccess"),
        ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyType"),
        ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyIpAddrType"),
        ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyIpAddr"),
        ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyCategory"),
        ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyResult"),
        ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyUser"),
        ("TPT-MISC-NOTIFY-MIB", "tptAuditLogNotifyMessage"))
)
if mibBuilder.loadTexts:
    tptAuditLogNotify.setStatus(
        "current"
    )

tptAuditLogCapacityNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 61)
)
tptAuditLogCapacityNotify.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-MISC-NOTIFY-MIB", "tptAuditLogCapacityNotifyPercent"),
        ("TPT-MISC-NOTIFY-MIB", "tptRolloverNotifyTime"))
)
if mibBuilder.loadTexts:
    tptAuditLogCapacityNotify.setStatus(
        "current"
    )

tptLoggingFailureNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 62)
)
tptLoggingFailureNotify.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-MISC-NOTIFY-MIB", "tptRolloverNotifyTime"))
)
if mibBuilder.loadTexts:
    tptLoggingFailureNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-MISC-NOTIFY-MIB",
    **{"LogFileType": LogFileType,
       "DiscoveryDelta": DiscoveryDelta,
       "SystemLogSeverity": SystemLogSeverity,
       "AddOrRemove": AddOrRemove,
       "CongestionThresholdPhase": CongestionThresholdPhase,
       "AuditLogResult": AuditLogResult,
       "AuditLogCategory": AuditLogCategory,
       "tpt-misc-notify": tpt_misc_notify,
       "tptManagedNotify": tptManagedNotify,
       "tptUnmanagedNotify": tptUnmanagedNotify,
       "tptRolloverNotify": tptRolloverNotify,
       "tptDiscoveryNotifyStartStop": tptDiscoveryNotifyStartStop,
       "tptDiscoveryNotifyNewHost": tptDiscoveryNotifyNewHost,
       "tptSystemLogNotify": tptSystemLogNotify,
       "tptQuarantineNotify": tptQuarantineNotify,
       "tptCongestionThresholdNotify": tptCongestionThresholdNotify,
       "tptiTier3CongestionThresholdNotify": tptiTier3CongestionThresholdNotify,
       "tptAuditLogNotify": tptAuditLogNotify,
       "tptAuditLogCapacityNotify": tptAuditLogCapacityNotify,
       "tptLoggingFailureNotify": tptLoggingFailureNotify,
       "tptMiscNotifyDeviceID": tptMiscNotifyDeviceID,
       "tptRolloverNotifyFileType": tptRolloverNotifyFileType,
       "tptRolloverNotifyMaxFiles": tptRolloverNotifyMaxFiles,
       "tptRolloverNotifyNumFiles": tptRolloverNotifyNumFiles,
       "tptRolloverNotifyTime": tptRolloverNotifyTime,
       "tptDiscoveryNotifyScanID": tptDiscoveryNotifyScanID,
       "tptDiscoveryNotifySegmentName": tptDiscoveryNotifySegmentName,
       "tptDiscoveryNotifyScanRange": tptDiscoveryNotifyScanRange,
       "tptDiscoveryNotifyDelta": tptDiscoveryNotifyDelta,
       "tptDiscoveryNotifyNewHosts": tptDiscoveryNotifyNewHosts,
       "tptDiscoveryNotifyChanged": tptDiscoveryNotifyChanged,
       "tptDiscoveryNotifyUnchanged": tptDiscoveryNotifyUnchanged,
       "tptDiscoveryNotifyNotFound": tptDiscoveryNotifyNotFound,
       "tptDiscoveryNotifyUnknown": tptDiscoveryNotifyUnknown,
       "tptDiscoveryNotifyStartTime": tptDiscoveryNotifyStartTime,
       "tptDiscoveryNotifyStopTime": tptDiscoveryNotifyStopTime,
       "tptDiscoveryNotifyErrorText": tptDiscoveryNotifyErrorText,
       "tptDiscoveryNotifyHostNetAddr": tptDiscoveryNotifyHostNetAddr,
       "tptDiscoveryNotifyHostDeviceID": tptDiscoveryNotifyHostDeviceID,
       "tptDiscoveryNotifySchedID": tptDiscoveryNotifySchedID,
       "tptSystemLogNotifyText": tptSystemLogNotifyText,
       "tptSystemLogNotifySequence": tptSystemLogNotifySequence,
       "tptSystemLogNotifySeverity": tptSystemLogNotifySeverity,
       "tptSystemLogNotifyTimeSec": tptSystemLogNotifyTimeSec,
       "tptSystemLogNotifyTimeNano": tptSystemLogNotifyTimeNano,
       "tptQuarantineNotifyHostNetAddr": tptQuarantineNotifyHostNetAddr,
       "tptQuarantineNotifyReason": tptQuarantineNotifyReason,
       "tptQuarantineNotifySegmentName": tptQuarantineNotifySegmentName,
       "tptQuarantineNotifyAction": tptQuarantineNotifyAction,
       "tptQuarantineNotifyHostNetAddrV6": tptQuarantineNotifyHostNetAddrV6,
       "tptCongestionPacketLoss": tptCongestionPacketLoss,
       "tptCongestionNotifyPhase": tptCongestionNotifyPhase,
       "tptCongestionThreshold": tptCongestionThreshold,
       "tptTier3CongestionPacketLoss": tptTier3CongestionPacketLoss,
       "tptTier3CongestionNotifyPhase": tptTier3CongestionNotifyPhase,
       "tptTier3CongestionThreshold": tptTier3CongestionThreshold,
       "tptAuditLogNotifyTime": tptAuditLogNotifyTime,
       "tptAuditLogNotifyAccess": tptAuditLogNotifyAccess,
       "tptAuditLogNotifyType": tptAuditLogNotifyType,
       "tptAuditLogNotifyIpAddrType": tptAuditLogNotifyIpAddrType,
       "tptAuditLogNotifyIpAddr": tptAuditLogNotifyIpAddr,
       "tptAuditLogNotifyCategory": tptAuditLogNotifyCategory,
       "tptAuditLogNotifyResult": tptAuditLogNotifyResult,
       "tptAuditLogNotifyUser": tptAuditLogNotifyUser,
       "tptAuditLogNotifyMessage": tptAuditLogNotifyMessage,
       "tptQuarantineNotifySslInspected": tptQuarantineNotifySslInspected,
       "tptAuditLogCapacityNotifyPercent": tptAuditLogCapacityNotifyPercent,
       "tptAuditLogCapacityOrFailureNotifyTime": tptAuditLogCapacityOrFailureNotifyTime}
)
