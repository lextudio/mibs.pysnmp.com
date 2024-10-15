# SNMP MIB module (FRI-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FRI-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:25 2024
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

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PPCTFRIPortTable_Object = MibTable
cdx6500PPCTFRIPortTable = _Cdx6500PPCTFRIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31)
)
if mibBuilder.loadTexts:
    cdx6500PPCTFRIPortTable.setStatus("mandatory")
_Cdx6500PPCTFRIPortEntry_Object = MibTableRow
cdx6500PPCTFRIPortEntry = _Cdx6500PPCTFRIPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1)
)
cdx6500PPCTFRIPortEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friPCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTFRIPortEntry.setStatus("mandatory")


class _FriPCfgPortNumber_Type(Integer32):
    """Custom type friPCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriPCfgPortNumber_Type.__name__ = "Integer32"
_FriPCfgPortNumber_Object = MibTableColumn
friPCfgPortNumber = _FriPCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 1),
    _FriPCfgPortNumber_Type()
)
friPCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPCfgPortNumber.setStatus("mandatory")


class _FriPCfgPortType_Type(Integer32):
    """Custom type friPCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            18
        )
    )
    namedValues = NamedValues(
        ("fri", 18)
    )


_FriPCfgPortType_Type.__name__ = "Integer32"
_FriPCfgPortType_Object = MibTableColumn
friPCfgPortType = _FriPCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 2),
    _FriPCfgPortType_Type()
)
friPCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPCfgPortType.setStatus("mandatory")


class _FriPCfgConnectionType_Type(Integer32):
    """Custom type friPCfgConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              21,
              100)
        )
    )
    namedValues = NamedValues(
        *(("dtr", 2),
          ("nc", 100),
          ("simp", 1),
          ("simpb", 21))
    )


_FriPCfgConnectionType_Type.__name__ = "Integer32"
_FriPCfgConnectionType_Object = MibTableColumn
friPCfgConnectionType = _FriPCfgConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 3),
    _FriPCfgConnectionType_Type()
)
friPCfgConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgConnectionType.setStatus("mandatory")


class _FriPCfgClockSource_Type(Integer32):
    """Custom type friPCfgClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ext", 2),
          ("extint", 3),
          ("extlp", 4),
          ("int", 1),
          ("nc", 100))
    )


_FriPCfgClockSource_Type.__name__ = "Integer32"
_FriPCfgClockSource_Object = MibTableColumn
friPCfgClockSource = _FriPCfgClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 4),
    _FriPCfgClockSource_Type()
)
friPCfgClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgClockSource.setStatus("mandatory")


class _FriPCfgClockSpeed_Type(Integer32):
    """Custom type friPCfgClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 2048000),
    )


_FriPCfgClockSpeed_Type.__name__ = "Integer32"
_FriPCfgClockSpeed_Object = MibTableColumn
friPCfgClockSpeed = _FriPCfgClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 5),
    _FriPCfgClockSpeed_Type()
)
friPCfgClockSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgClockSpeed.setStatus("mandatory")


class _FriPCfgHighestStnNumber_Type(Integer32):
    """Custom type friPCfgHighestStnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FriPCfgHighestStnNumber_Type.__name__ = "Integer32"
_FriPCfgHighestStnNumber_Object = MibTableColumn
friPCfgHighestStnNumber = _FriPCfgHighestStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 6),
    _FriPCfgHighestStnNumber_Type()
)
friPCfgHighestStnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPCfgHighestStnNumber.setStatus("deprecated")


class _FriPCfgFrameSeqCounting_Type(Integer32):
    """Custom type friPCfgFrameSeqCounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("nc", 100),
          ("normal", 1))
    )


_FriPCfgFrameSeqCounting_Type.__name__ = "Integer32"
_FriPCfgFrameSeqCounting_Object = MibTableColumn
friPCfgFrameSeqCounting = _FriPCfgFrameSeqCounting_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 7),
    _FriPCfgFrameSeqCounting_Type()
)
friPCfgFrameSeqCounting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPCfgFrameSeqCounting.setStatus("mandatory")


class _FriPCfgPktSeqCounting_Type(Integer32):
    """Custom type friPCfgPktSeqCounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("nc", 100),
          ("normal", 1))
    )


_FriPCfgPktSeqCounting_Type.__name__ = "Integer32"
_FriPCfgPktSeqCounting_Object = MibTableColumn
friPCfgPktSeqCounting = _FriPCfgPktSeqCounting_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 8),
    _FriPCfgPktSeqCounting_Type()
)
friPCfgPktSeqCounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgPktSeqCounting.setStatus("mandatory")


class _FriPCfgCntrlProtocolSupport_Type(Integer32):
    """Custom type friPCfgCntrlProtocolSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 4),
          ("annexD", 1),
          ("auto", 5),
          ("lmi", 3),
          ("nc", 100),
          ("none", 2))
    )


_FriPCfgCntrlProtocolSupport_Type.__name__ = "Integer32"
_FriPCfgCntrlProtocolSupport_Object = MibTableColumn
friPCfgCntrlProtocolSupport = _FriPCfgCntrlProtocolSupport_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 9),
    _FriPCfgCntrlProtocolSupport_Type()
)
friPCfgCntrlProtocolSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgCntrlProtocolSupport.setStatus("mandatory")


class _FriPCfgHighPriorityStn_Type(Integer32):
    """Custom type friPCfgHighPriorityStn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FriPCfgHighPriorityStn_Type.__name__ = "Integer32"
_FriPCfgHighPriorityStn_Object = MibTableColumn
friPCfgHighPriorityStn = _FriPCfgHighPriorityStn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 10),
    _FriPCfgHighPriorityStn_Type()
)
friPCfgHighPriorityStn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgHighPriorityStn.setStatus("mandatory")


class _FriPCfgMaxVoiceBWBitsPerSec_Type(Integer32):
    """Custom type friPCfgMaxVoiceBWBitsPerSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_FriPCfgMaxVoiceBWBitsPerSec_Type.__name__ = "Integer32"
_FriPCfgMaxVoiceBWBitsPerSec_Object = MibTableColumn
friPCfgMaxVoiceBWBitsPerSec = _FriPCfgMaxVoiceBWBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 11),
    _FriPCfgMaxVoiceBWBitsPerSec_Type()
)
friPCfgMaxVoiceBWBitsPerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgMaxVoiceBWBitsPerSec.setStatus("mandatory")


class _FriPCfgSegSizeVoicePresent_Type(Integer32):
    """Custom type friPCfgSegSizeVoicePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(33,
              65,
              100,
              129,
              257,
              513,
              1025)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("segSize1024", 1025),
          ("segSize128", 129),
          ("segSize256", 257),
          ("segSize32", 33),
          ("segSize512", 513),
          ("segSize64", 65))
    )


_FriPCfgSegSizeVoicePresent_Type.__name__ = "Integer32"
_FriPCfgSegSizeVoicePresent_Object = MibTableColumn
friPCfgSegSizeVoicePresent = _FriPCfgSegSizeVoicePresent_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 12),
    _FriPCfgSegSizeVoicePresent_Type()
)
friPCfgSegSizeVoicePresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgSegSizeVoicePresent.setStatus("mandatory")


class _FriPCfgSegSizeVoiceNotPresent_Type(Integer32):
    """Custom type friPCfgSegSizeVoiceNotPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(33,
              65,
              100,
              129,
              257,
              513,
              1025,
              2049,
              4097,
              32000)
        )
    )
    namedValues = NamedValues(
        *(("disable", 32000),
          ("nc", 100),
          ("segSize1024", 1025),
          ("segSize128", 129),
          ("segSize2048", 2049),
          ("segSize256", 257),
          ("segSize32", 33),
          ("segSize4096", 4097),
          ("segSize512", 513),
          ("segSize64", 65))
    )


_FriPCfgSegSizeVoiceNotPresent_Type.__name__ = "Integer32"
_FriPCfgSegSizeVoiceNotPresent_Object = MibTableColumn
friPCfgSegSizeVoiceNotPresent = _FriPCfgSegSizeVoiceNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 13),
    _FriPCfgSegSizeVoiceNotPresent_Type()
)
friPCfgSegSizeVoiceNotPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgSegSizeVoiceNotPresent.setStatus("mandatory")


class _FriPCfgT391Timer_Type(Integer32):
    """Custom type friPCfgT391Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FriPCfgT391Timer_Type.__name__ = "Integer32"
_FriPCfgT391Timer_Object = MibTableColumn
friPCfgT391Timer = _FriPCfgT391Timer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 14),
    _FriPCfgT391Timer_Type()
)
friPCfgT391Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgT391Timer.setStatus("mandatory")


class _FriPCfgT392Timer_Type(Integer32):
    """Custom type friPCfgT392Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FriPCfgT392Timer_Type.__name__ = "Integer32"
_FriPCfgT392Timer_Object = MibTableColumn
friPCfgT392Timer = _FriPCfgT392Timer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 15),
    _FriPCfgT392Timer_Type()
)
friPCfgT392Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgT392Timer.setStatus("mandatory")
_FriPCfgN391PollCycle_Type = Integer32
_FriPCfgN391PollCycle_Object = MibTableColumn
friPCfgN391PollCycle = _FriPCfgN391PollCycle_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 16),
    _FriPCfgN391PollCycle_Type()
)
friPCfgN391PollCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgN391PollCycle.setStatus("mandatory")
_FriPCfgN392ErrsDuringMonitoredEvents_Type = Integer32
_FriPCfgN392ErrsDuringMonitoredEvents_Object = MibTableColumn
friPCfgN392ErrsDuringMonitoredEvents = _FriPCfgN392ErrsDuringMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 17),
    _FriPCfgN392ErrsDuringMonitoredEvents_Type()
)
friPCfgN392ErrsDuringMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgN392ErrsDuringMonitoredEvents.setStatus("mandatory")
_FriPCfgN393MonitoredEvents_Type = Integer32
_FriPCfgN393MonitoredEvents_Object = MibTableColumn
friPCfgN393MonitoredEvents = _FriPCfgN393MonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 18),
    _FriPCfgN393MonitoredEvents_Type()
)
friPCfgN393MonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgN393MonitoredEvents.setStatus("mandatory")


class _FriPCfgNT1PollTimer_Type(Integer32):
    """Custom type friPCfgNT1PollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FriPCfgNT1PollTimer_Type.__name__ = "Integer32"
_FriPCfgNT1PollTimer_Object = MibTableColumn
friPCfgNT1PollTimer = _FriPCfgNT1PollTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 19),
    _FriPCfgNT1PollTimer_Type()
)
friPCfgNT1PollTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPCfgNT1PollTimer.setStatus("mandatory")


class _FriPCfgNT2VerificationTimer_Type(Integer32):
    """Custom type friPCfgNT2VerificationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FriPCfgNT2VerificationTimer_Type.__name__ = "Integer32"
_FriPCfgNT2VerificationTimer_Object = MibTableColumn
friPCfgNT2VerificationTimer = _FriPCfgNT2VerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 20),
    _FriPCfgNT2VerificationTimer_Type()
)
friPCfgNT2VerificationTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPCfgNT2VerificationTimer.setStatus("mandatory")
_FriPCfgNN1StatusPollingCycle_Type = Integer32
_FriPCfgNN1StatusPollingCycle_Object = MibTableColumn
friPCfgNN1StatusPollingCycle = _FriPCfgNN1StatusPollingCycle_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 21),
    _FriPCfgNN1StatusPollingCycle_Type()
)
friPCfgNN1StatusPollingCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPCfgNN1StatusPollingCycle.setStatus("mandatory")
_FriPCfgNN2ErrsDuringMonitoredEvents_Type = Integer32
_FriPCfgNN2ErrsDuringMonitoredEvents_Object = MibTableColumn
friPCfgNN2ErrsDuringMonitoredEvents = _FriPCfgNN2ErrsDuringMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 22),
    _FriPCfgNN2ErrsDuringMonitoredEvents_Type()
)
friPCfgNN2ErrsDuringMonitoredEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPCfgNN2ErrsDuringMonitoredEvents.setStatus("mandatory")
_FriPCfgNN3MonitoredEvents_Type = Integer32
_FriPCfgNN3MonitoredEvents_Object = MibTableColumn
friPCfgNN3MonitoredEvents = _FriPCfgNN3MonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 23),
    _FriPCfgNN3MonitoredEvents_Type()
)
friPCfgNN3MonitoredEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPCfgNN3MonitoredEvents.setStatus("mandatory")


class _FriPCfgInvertTXClock_Type(Integer32):
    """Custom type friPCfgInvertTXClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("no", 1),
          ("yes", 2))
    )


_FriPCfgInvertTXClock_Type.__name__ = "Integer32"
_FriPCfgInvertTXClock_Object = MibTableColumn
friPCfgInvertTXClock = _FriPCfgInvertTXClock_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 24),
    _FriPCfgInvertTXClock_Type()
)
friPCfgInvertTXClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgInvertTXClock.setStatus("mandatory")


class _FriPCfgControlProtocolOptions_Type(DisplayString):
    """Custom type friPCfgControlProtocolOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_FriPCfgControlProtocolOptions_Type.__name__ = "DisplayString"
_FriPCfgControlProtocolOptions_Object = MibTableColumn
friPCfgControlProtocolOptions = _FriPCfgControlProtocolOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 25),
    _FriPCfgControlProtocolOptions_Type()
)
friPCfgControlProtocolOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgControlProtocolOptions.setStatus("mandatory")


class _FriPCfgDiscardControlOptions_Type(Integer32):
    """Custom type friPCfgDiscardControlOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("debit", 2),
          ("none", 1))
    )


_FriPCfgDiscardControlOptions_Type.__name__ = "Integer32"
_FriPCfgDiscardControlOptions_Object = MibTableColumn
friPCfgDiscardControlOptions = _FriPCfgDiscardControlOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 26),
    _FriPCfgDiscardControlOptions_Type()
)
friPCfgDiscardControlOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgDiscardControlOptions.setStatus("mandatory")
_FriPCfgStartSvcDlci_Type = Integer32
_FriPCfgStartSvcDlci_Object = MibTableColumn
friPCfgStartSvcDlci = _FriPCfgStartSvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 27),
    _FriPCfgStartSvcDlci_Type()
)
friPCfgStartSvcDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgStartSvcDlci.setStatus("mandatory")


class _FriPCfgSubscriberNumber_Type(OctetString):
    """Custom type friPCfgSubscriberNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 19),
    )


_FriPCfgSubscriberNumber_Type.__name__ = "OctetString"
_FriPCfgSubscriberNumber_Object = MibTableColumn
friPCfgSubscriberNumber = _FriPCfgSubscriberNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 28),
    _FriPCfgSubscriberNumber_Type()
)
friPCfgSubscriberNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgSubscriberNumber.setStatus("mandatory")


class _FriPCfgMaxFmif_Type(Integer32):
    """Custom type friPCfgMaxFmif based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(262, 4096),
    )


_FriPCfgMaxFmif_Type.__name__ = "Integer32"
_FriPCfgMaxFmif_Object = MibTableColumn
friPCfgMaxFmif = _FriPCfgMaxFmif_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 29),
    _FriPCfgMaxFmif_Type()
)
friPCfgMaxFmif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgMaxFmif.setStatus("mandatory")


class _FriPCfgT200_Type(Integer32):
    """Custom type friPCfgT200 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriPCfgT200_Type.__name__ = "Integer32"
_FriPCfgT200_Object = MibTableColumn
friPCfgT200 = _FriPCfgT200_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 30),
    _FriPCfgT200_Type()
)
friPCfgT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgT200.setStatus("mandatory")


class _FriPCfgN200_Type(Integer32):
    """Custom type friPCfgN200 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_FriPCfgN200_Type.__name__ = "Integer32"
_FriPCfgN200_Object = MibTableColumn
friPCfgN200 = _FriPCfgN200_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 31),
    _FriPCfgN200_Type()
)
friPCfgN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgN200.setStatus("mandatory")


class _FriPCfgWindowK_Type(Integer32):
    """Custom type friPCfgWindowK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FriPCfgWindowK_Type.__name__ = "Integer32"
_FriPCfgWindowK_Object = MibTableColumn
friPCfgWindowK = _FriPCfgWindowK_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 32),
    _FriPCfgWindowK_Type()
)
friPCfgWindowK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgWindowK.setStatus("mandatory")


class _FriPCfgT203_Type(Integer32):
    """Custom type friPCfgT203 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriPCfgT203_Type.__name__ = "Integer32"
_FriPCfgT203_Object = MibTableColumn
friPCfgT203 = _FriPCfgT203_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 33),
    _FriPCfgT203_Type()
)
friPCfgT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgT203.setStatus("mandatory")


class _FriPCfgT303_Type(Integer32):
    """Custom type friPCfgT303 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_FriPCfgT303_Type.__name__ = "Integer32"
_FriPCfgT303_Object = MibTableColumn
friPCfgT303 = _FriPCfgT303_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 34),
    _FriPCfgT303_Type()
)
friPCfgT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgT303.setStatus("mandatory")


class _FriPCfgT305_Type(Integer32):
    """Custom type friPCfgT305 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriPCfgT305_Type.__name__ = "Integer32"
_FriPCfgT305_Object = MibTableColumn
friPCfgT305 = _FriPCfgT305_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 35),
    _FriPCfgT305_Type()
)
friPCfgT305.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgT305.setStatus("mandatory")


class _FriPCfgT308_Type(Integer32):
    """Custom type friPCfgT308 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_FriPCfgT308_Type.__name__ = "Integer32"
_FriPCfgT308_Object = MibTableColumn
friPCfgT308 = _FriPCfgT308_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 36),
    _FriPCfgT308_Type()
)
friPCfgT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgT308.setStatus("mandatory")


class _FriPCfgT310_Type(Integer32):
    """Custom type friPCfgT310 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriPCfgT310_Type.__name__ = "Integer32"
_FriPCfgT310_Object = MibTableColumn
friPCfgT310 = _FriPCfgT310_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 37),
    _FriPCfgT310_Type()
)
friPCfgT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgT310.setStatus("mandatory")


class _FriPCfgControlProtocol_Type(Integer32):
    """Custom type friPCfgControlProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_FriPCfgControlProtocol_Type.__name__ = "Integer32"
_FriPCfgControlProtocol_Object = MibTableColumn
friPCfgControlProtocol = _FriPCfgControlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 38),
    _FriPCfgControlProtocol_Type()
)
friPCfgControlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgControlProtocol.setStatus("mandatory")


class _FriPCfguniState_Type(Integer32):
    """Custom type friPCfguniState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FriPCfguniState_Type.__name__ = "Integer32"
_FriPCfguniState_Object = MibTableColumn
friPCfguniState = _FriPCfguniState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 39),
    _FriPCfguniState_Type()
)
friPCfguniState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfguniState.setStatus("mandatory")


class _FriPCfguniSSVP_Type(Integer32):
    """Custom type friPCfguniSSVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65,
              129,
              257,
              513,
              1025)
        )
    )
    namedValues = NamedValues(
        *(("segSize1024", 1025),
          ("segSize128", 129),
          ("segSize256", 257),
          ("segSize512", 513),
          ("segSize64", 65))
    )


_FriPCfguniSSVP_Type.__name__ = "Integer32"
_FriPCfguniSSVP_Object = MibTableColumn
friPCfguniSSVP = _FriPCfguniSSVP_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 40),
    _FriPCfguniSSVP_Type()
)
friPCfguniSSVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPCfguniSSVP.setStatus("mandatory")


class _FriPCfguniSSVNP_Type(Integer32):
    """Custom type friPCfguniSSVNP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65,
              129,
              257,
              513,
              1025,
              2049,
              4097,
              32000)
        )
    )
    namedValues = NamedValues(
        *(("disable", 32000),
          ("segSize1024", 1025),
          ("segSize128", 129),
          ("segSize2048", 2049),
          ("segSize256", 257),
          ("segSize4096", 4097),
          ("segSize512", 513),
          ("segSize64", 65))
    )


_FriPCfguniSSVNP_Type.__name__ = "Integer32"
_FriPCfguniSSVNP_Object = MibTableColumn
friPCfguniSSVNP = _FriPCfguniSSVNP_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 41),
    _FriPCfguniSSVNP_Type()
)
friPCfguniSSVNP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfguniSSVNP.setStatus("mandatory")


class _FriPCfguniSegDelay_Type(Integer32):
    """Custom type friPCfguniSegDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FriPCfguniSegDelay_Type.__name__ = "Integer32"
_FriPCfguniSegDelay_Object = MibTableColumn
friPCfguniSegDelay = _FriPCfguniSegDelay_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 42),
    _FriPCfguniSegDelay_Type()
)
friPCfguniSegDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfguniSegDelay.setStatus("mandatory")


class _FriPCfguniCheckPckSize_Type(Integer32):
    """Custom type friPCfguniCheckPckSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FriPCfguniCheckPckSize_Type.__name__ = "Integer32"
_FriPCfguniCheckPckSize_Object = MibTableColumn
friPCfguniCheckPckSize = _FriPCfguniCheckPckSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 43),
    _FriPCfguniCheckPckSize_Type()
)
friPCfguniCheckPckSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfguniCheckPckSize.setStatus("mandatory")


class _FriPCfgElectricalInterfaceType_Type(Integer32):
    """Custom type friPCfgElectricalInterfaceType based on Integer32"""
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
        *(("none", 5),
          ("v24", 1),
          ("v35", 2),
          ("v36", 3),
          ("x21", 4))
    )


_FriPCfgElectricalInterfaceType_Type.__name__ = "Integer32"
_FriPCfgElectricalInterfaceType_Object = MibTableColumn
friPCfgElectricalInterfaceType = _FriPCfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 44),
    _FriPCfgElectricalInterfaceType_Type()
)
friPCfgElectricalInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgElectricalInterfaceType.setStatus("mandatory")


class _FriPCfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type friPCfgV24ElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ri", 1),
          ("tm", 2))
    )


_FriPCfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_FriPCfgV24ElectricalInterfaceOption_Object = MibTableColumn
friPCfgV24ElectricalInterfaceOption = _FriPCfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 45),
    _FriPCfgV24ElectricalInterfaceOption_Type()
)
friPCfgV24ElectricalInterfaceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _FriPCfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type friPCfgHighSpeedElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("xover", 2))
    )


_FriPCfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_FriPCfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
friPCfgHighSpeedElectricalInterfaceOption = _FriPCfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 31, 1, 46),
    _FriPCfgHighSpeedElectricalInterfaceOption_Type()
)
friPCfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friPCfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTStationProtocolGroup = _Cdx6500PCTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3)
)
_Cdx6500SPCTFRIStationTable_Object = MibTable
cdx6500SPCTFRIStationTable = _Cdx6500SPCTFRIStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9)
)
if mibBuilder.loadTexts:
    cdx6500SPCTFRIStationTable.setStatus("mandatory")
_Cdx6500SPCTFRIStationEntry_Object = MibTableRow
cdx6500SPCTFRIStationEntry = _Cdx6500SPCTFRIStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1)
)
cdx6500SPCTFRIStationEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friSCfgPortNumber"),
    (0, "FRI-OPT-MIB", "friSCfgStnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500SPCTFRIStationEntry.setStatus("mandatory")


class _FriSCfgPortNumber_Type(Integer32):
    """Custom type friSCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriSCfgPortNumber_Type.__name__ = "Integer32"
_FriSCfgPortNumber_Object = MibTableColumn
friSCfgPortNumber = _FriSCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 1),
    _FriSCfgPortNumber_Type()
)
friSCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSCfgPortNumber.setStatus("mandatory")


class _FriSCfgStnNumber_Type(Integer32):
    """Custom type friSCfgStnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FriSCfgStnNumber_Type.__name__ = "Integer32"
_FriSCfgStnNumber_Object = MibTableColumn
friSCfgStnNumber = _FriSCfgStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 2),
    _FriSCfgStnNumber_Type()
)
friSCfgStnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSCfgStnNumber.setStatus("mandatory")


class _FriSCfgStnType_Type(Integer32):
    """Custom type friSCfgStnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annexG", 1),
          ("bypass", 2),
          ("voiceRelay", 3))
    )


_FriSCfgStnType_Type.__name__ = "Integer32"
_FriSCfgStnType_Object = MibTableColumn
friSCfgStnType = _FriSCfgStnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 3),
    _FriSCfgStnType_Type()
)
friSCfgStnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgStnType.setStatus("mandatory")
_FriSCfgDLCI_Type = Integer32
_FriSCfgDLCI_Object = MibTableColumn
friSCfgDLCI = _FriSCfgDLCI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 4),
    _FriSCfgDLCI_Type()
)
friSCfgDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgDLCI.setStatus("mandatory")


class _FriSCfgCommInfoRate_Type(Integer32):
    """Custom type friSCfgCommInfoRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_FriSCfgCommInfoRate_Type.__name__ = "Integer32"
_FriSCfgCommInfoRate_Object = MibTableColumn
friSCfgCommInfoRate = _FriSCfgCommInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 5),
    _FriSCfgCommInfoRate_Type()
)
friSCfgCommInfoRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgCommInfoRate.setStatus("mandatory")


class _FriSCfgCommBurstSize_Type(Integer32):
    """Custom type friSCfgCommBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 768000),
    )


_FriSCfgCommBurstSize_Type.__name__ = "Integer32"
_FriSCfgCommBurstSize_Object = MibTableColumn
friSCfgCommBurstSize = _FriSCfgCommBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 6),
    _FriSCfgCommBurstSize_Type()
)
friSCfgCommBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgCommBurstSize.setStatus("mandatory")


class _FriSCfgTransDelay_Type(Integer32):
    """Custom type friSCfgTransDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FriSCfgTransDelay_Type.__name__ = "Integer32"
_FriSCfgTransDelay_Object = MibTableColumn
friSCfgTransDelay = _FriSCfgTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 7),
    _FriSCfgTransDelay_Type()
)
friSCfgTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgTransDelay.setStatus("mandatory")


class _FriSCfgCongControlMode_Type(Integer32):
    """Custom type friSCfgCongControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("congested", 3),
          ("disable", 2),
          ("limit", 4),
          ("nc", 100),
          ("normal", 1))
    )


_FriSCfgCongControlMode_Type.__name__ = "Integer32"
_FriSCfgCongControlMode_Object = MibTableColumn
friSCfgCongControlMode = _FriSCfgCongControlMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 8),
    _FriSCfgCongControlMode_Type()
)
friSCfgCongControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgCongControlMode.setStatus("mandatory")


class _FriSCfgLinkAddress_Type(Integer32):
    """Custom type friSCfgLinkAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1),
          ("nc", 100))
    )


_FriSCfgLinkAddress_Type.__name__ = "Integer32"
_FriSCfgLinkAddress_Object = MibTableColumn
friSCfgLinkAddress = _FriSCfgLinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 9),
    _FriSCfgLinkAddress_Type()
)
friSCfgLinkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgLinkAddress.setStatus("mandatory")


class _FriSCfgPVCChannels_Type(Integer32):
    """Custom type friSCfgPVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FriSCfgPVCChannels_Type.__name__ = "Integer32"
_FriSCfgPVCChannels_Object = MibTableColumn
friSCfgPVCChannels = _FriSCfgPVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 10),
    _FriSCfgPVCChannels_Type()
)
friSCfgPVCChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgPVCChannels.setStatus("mandatory")


class _FriSCfgStartingPVC_Type(Integer32):
    """Custom type friSCfgStartingPVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FriSCfgStartingPVC_Type.__name__ = "Integer32"
_FriSCfgStartingPVC_Object = MibTableColumn
friSCfgStartingPVC = _FriSCfgStartingPVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 11),
    _FriSCfgStartingPVC_Type()
)
friSCfgStartingPVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgStartingPVC.setStatus("mandatory")


class _FriSCfgSVCChannels_Type(Integer32):
    """Custom type friSCfgSVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_FriSCfgSVCChannels_Type.__name__ = "Integer32"
_FriSCfgSVCChannels_Object = MibTableColumn
friSCfgSVCChannels = _FriSCfgSVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 12),
    _FriSCfgSVCChannels_Type()
)
friSCfgSVCChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgSVCChannels.setStatus("mandatory")


class _FriSCfgStartingSVC_Type(Integer32):
    """Custom type friSCfgStartingSVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_FriSCfgStartingSVC_Type.__name__ = "Integer32"
_FriSCfgStartingSVC_Object = MibTableColumn
friSCfgStartingSVC = _FriSCfgStartingSVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 13),
    _FriSCfgStartingSVC_Type()
)
friSCfgStartingSVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgStartingSVC.setStatus("mandatory")


class _FriSCfgVoiceSVCChannels_Type(Integer32):
    """Custom type friSCfgVoiceSVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FriSCfgVoiceSVCChannels_Type.__name__ = "Integer32"
_FriSCfgVoiceSVCChannels_Object = MibTableColumn
friSCfgVoiceSVCChannels = _FriSCfgVoiceSVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 14),
    _FriSCfgVoiceSVCChannels_Type()
)
friSCfgVoiceSVCChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgVoiceSVCChannels.setStatus("mandatory")


class _FriSCfgInitialFrame_Type(Integer32):
    """Custom type friSCfgInitialFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disc", 2),
          ("nc", 100),
          ("none", 3),
          ("sabm", 1))
    )


_FriSCfgInitialFrame_Type.__name__ = "Integer32"
_FriSCfgInitialFrame_Object = MibTableColumn
friSCfgInitialFrame = _FriSCfgInitialFrame_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 15),
    _FriSCfgInitialFrame_Type()
)
friSCfgInitialFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgInitialFrame.setStatus("mandatory")


class _FriSCfgT1RetryTimer_Type(Integer32):
    """Custom type friSCfgT1RetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FriSCfgT1RetryTimer_Type.__name__ = "Integer32"
_FriSCfgT1RetryTimer_Object = MibTableColumn
friSCfgT1RetryTimer = _FriSCfgT1RetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 16),
    _FriSCfgT1RetryTimer_Type()
)
friSCfgT1RetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgT1RetryTimer.setStatus("mandatory")


class _FriSCfgT4PollTimer_Type(Integer32):
    """Custom type friSCfgT4PollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_FriSCfgT4PollTimer_Type.__name__ = "Integer32"
_FriSCfgT4PollTimer_Object = MibTableColumn
friSCfgT4PollTimer = _FriSCfgT4PollTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 17),
    _FriSCfgT4PollTimer_Type()
)
friSCfgT4PollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgT4PollTimer.setStatus("mandatory")


class _FriSCfgN2TransmissionTries_Type(Integer32):
    """Custom type friSCfgN2TransmissionTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_FriSCfgN2TransmissionTries_Type.__name__ = "Integer32"
_FriSCfgN2TransmissionTries_Object = MibTableColumn
friSCfgN2TransmissionTries = _FriSCfgN2TransmissionTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 18),
    _FriSCfgN2TransmissionTries_Type()
)
friSCfgN2TransmissionTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgN2TransmissionTries.setStatus("mandatory")


class _FriSCfgKFrameWindow_Type(Integer32):
    """Custom type friSCfgKFrameWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_FriSCfgKFrameWindow_Type.__name__ = "Integer32"
_FriSCfgKFrameWindow_Object = MibTableColumn
friSCfgKFrameWindow = _FriSCfgKFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 19),
    _FriSCfgKFrameWindow_Type()
)
friSCfgKFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgKFrameWindow.setStatus("mandatory")


class _FriSCfgWPacketWindow_Type(Integer32):
    """Custom type friSCfgWPacketWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_FriSCfgWPacketWindow_Type.__name__ = "Integer32"
_FriSCfgWPacketWindow_Object = MibTableColumn
friSCfgWPacketWindow = _FriSCfgWPacketWindow_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 20),
    _FriSCfgWPacketWindow_Type()
)
friSCfgWPacketWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgWPacketWindow.setStatus("mandatory")


class _FriSCfgPPacketSize_Type(Integer32):
    """Custom type friSCfgPPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9,
              10,
              11,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("psize1024", 11),
          ("psize128", 8),
          ("psize256", 9),
          ("psize32", 6),
          ("psize512", 10),
          ("psize64", 7))
    )


_FriSCfgPPacketSize_Type.__name__ = "Integer32"
_FriSCfgPPacketSize_Object = MibTableColumn
friSCfgPPacketSize = _FriSCfgPPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 21),
    _FriSCfgPPacketSize_Type()
)
friSCfgPPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgPPacketSize.setStatus("mandatory")


class _FriSCfgDataQUpperThreshold_Type(Integer32):
    """Custom type friSCfgDataQUpperThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FriSCfgDataQUpperThreshold_Type.__name__ = "Integer32"
_FriSCfgDataQUpperThreshold_Object = MibTableColumn
friSCfgDataQUpperThreshold = _FriSCfgDataQUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 22),
    _FriSCfgDataQUpperThreshold_Type()
)
friSCfgDataQUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgDataQUpperThreshold.setStatus("mandatory")


class _FriSCfgDataQLowerThreshold_Type(Integer32):
    """Custom type friSCfgDataQLowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FriSCfgDataQLowerThreshold_Type.__name__ = "Integer32"
_FriSCfgDataQLowerThreshold_Object = MibTableColumn
friSCfgDataQLowerThreshold = _FriSCfgDataQLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 23),
    _FriSCfgDataQLowerThreshold_Type()
)
friSCfgDataQLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgDataQLowerThreshold.setStatus("mandatory")


class _FriSCfgRestartTimer_Type(Integer32):
    """Custom type friSCfgRestartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_FriSCfgRestartTimer_Type.__name__ = "Integer32"
_FriSCfgRestartTimer_Object = MibTableColumn
friSCfgRestartTimer = _FriSCfgRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 24),
    _FriSCfgRestartTimer_Type()
)
friSCfgRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgRestartTimer.setStatus("mandatory")


class _FriSCfgResetTimer_Type(Integer32):
    """Custom type friSCfgResetTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_FriSCfgResetTimer_Type.__name__ = "Integer32"
_FriSCfgResetTimer_Object = MibTableColumn
friSCfgResetTimer = _FriSCfgResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 25),
    _FriSCfgResetTimer_Type()
)
friSCfgResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgResetTimer.setStatus("mandatory")


class _FriSCfgCallTimer_Type(Integer32):
    """Custom type friSCfgCallTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_FriSCfgCallTimer_Type.__name__ = "Integer32"
_FriSCfgCallTimer_Object = MibTableColumn
friSCfgCallTimer = _FriSCfgCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 26),
    _FriSCfgCallTimer_Type()
)
friSCfgCallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgCallTimer.setStatus("mandatory")


class _FriSCfgClearTimer_Type(Integer32):
    """Custom type friSCfgClearTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_FriSCfgClearTimer_Type.__name__ = "Integer32"
_FriSCfgClearTimer_Object = MibTableColumn
friSCfgClearTimer = _FriSCfgClearTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 27),
    _FriSCfgClearTimer_Type()
)
friSCfgClearTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgClearTimer.setStatus("mandatory")


class _FriSCfgX25Options_Type(DisplayString):
    """Custom type friSCfgX25Options based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_FriSCfgX25Options_Type.__name__ = "DisplayString"
_FriSCfgX25Options_Object = MibTableColumn
friSCfgX25Options = _FriSCfgX25Options_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 28),
    _FriSCfgX25Options_Type()
)
friSCfgX25Options.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgX25Options.setStatus("mandatory")


class _FriSCfgRestrictedConnDest_Type(DisplayString):
    """Custom type friSCfgRestrictedConnDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FriSCfgRestrictedConnDest_Type.__name__ = "DisplayString"
_FriSCfgRestrictedConnDest_Object = MibTableColumn
friSCfgRestrictedConnDest = _FriSCfgRestrictedConnDest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 29),
    _FriSCfgRestrictedConnDest_Type()
)
friSCfgRestrictedConnDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgRestrictedConnDest.setStatus("mandatory")


class _FriSCfgCUGMembership_Type(DisplayString):
    """Custom type friSCfgCUGMembership based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_FriSCfgCUGMembership_Type.__name__ = "DisplayString"
_FriSCfgCUGMembership_Object = MibTableColumn
friSCfgCUGMembership = _FriSCfgCUGMembership_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 30),
    _FriSCfgCUGMembership_Type()
)
friSCfgCUGMembership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgCUGMembership.setStatus("mandatory")


class _FriSCfgBillingRecords_Type(Integer32):
    """Custom type friSCfgBillingRecords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("off", 1),
          ("on", 2))
    )


_FriSCfgBillingRecords_Type.__name__ = "Integer32"
_FriSCfgBillingRecords_Object = MibTableColumn
friSCfgBillingRecords = _FriSCfgBillingRecords_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 31),
    _FriSCfgBillingRecords_Type()
)
friSCfgBillingRecords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgBillingRecords.setStatus("mandatory")


class _FriSCfgFrameSegmenter_Type(Integer32):
    """Custom type friSCfgFrameSegmenter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("nc", 100))
    )


_FriSCfgFrameSegmenter_Type.__name__ = "Integer32"
_FriSCfgFrameSegmenter_Object = MibTableColumn
friSCfgFrameSegmenter = _FriSCfgFrameSegmenter_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 32),
    _FriSCfgFrameSegmenter_Type()
)
friSCfgFrameSegmenter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgFrameSegmenter.setStatus("mandatory")


class _FriSCfgVoiceCongCtrlMode_Type(Integer32):
    """Custom type friSCfgVoiceCongCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("nc", 100))
    )


_FriSCfgVoiceCongCtrlMode_Type.__name__ = "Integer32"
_FriSCfgVoiceCongCtrlMode_Object = MibTableColumn
friSCfgVoiceCongCtrlMode = _FriSCfgVoiceCongCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 33),
    _FriSCfgVoiceCongCtrlMode_Type()
)
friSCfgVoiceCongCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgVoiceCongCtrlMode.setStatus("mandatory")


class _FriSCfgPeakUtilization_Type(Integer32):
    """Custom type friSCfgPeakUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_FriSCfgPeakUtilization_Type.__name__ = "Integer32"
_FriSCfgPeakUtilization_Object = MibTableColumn
friSCfgPeakUtilization = _FriSCfgPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 34),
    _FriSCfgPeakUtilization_Type()
)
friSCfgPeakUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgPeakUtilization.setStatus("mandatory")


class _FriSCfgMaxInboundQueue_Type(Integer32):
    """Custom type friSCfgMaxInboundQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2500),
    )


_FriSCfgMaxInboundQueue_Type.__name__ = "Integer32"
_FriSCfgMaxInboundQueue_Object = MibTableColumn
friSCfgMaxInboundQueue = _FriSCfgMaxInboundQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 35),
    _FriSCfgMaxInboundQueue_Type()
)
friSCfgMaxInboundQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgMaxInboundQueue.setStatus("mandatory")


class _FriSCfgAnnexGRateReduction_Type(Integer32):
    """Custom type friSCfgAnnexGRateReduction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("nc", 100))
    )


_FriSCfgAnnexGRateReduction_Type.__name__ = "Integer32"
_FriSCfgAnnexGRateReduction_Object = MibTableColumn
friSCfgAnnexGRateReduction = _FriSCfgAnnexGRateReduction_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 36),
    _FriSCfgAnnexGRateReduction_Type()
)
friSCfgAnnexGRateReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgAnnexGRateReduction.setStatus("mandatory")


class _FriSCfgCctType_Type(Integer32):
    """Custom type friSCfgCctType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_FriSCfgCctType_Type.__name__ = "Integer32"
_FriSCfgCctType_Object = MibTableColumn
friSCfgCctType = _FriSCfgCctType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 37),
    _FriSCfgCctType_Type()
)
friSCfgCctType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgCctType.setStatus("mandatory")


class _FriSCfgCallControl_Type(Integer32):
    """Custom type friSCfgCallControl based on Integer32"""
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
        *(("autd", 2),
          ("auto", 1),
          ("cnorm", 4),
          ("recv", 3))
    )


_FriSCfgCallControl_Type.__name__ = "Integer32"
_FriSCfgCallControl_Object = MibTableColumn
friSCfgCallControl = _FriSCfgCallControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 38),
    _FriSCfgCallControl_Type()
)
friSCfgCallControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgCallControl.setStatus("mandatory")


class _FriSCfgRetryInterval_Type(Integer32):
    """Custom type friSCfgRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriSCfgRetryInterval_Type.__name__ = "Integer32"
_FriSCfgRetryInterval_Object = MibTableColumn
friSCfgRetryInterval = _FriSCfgRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 39),
    _FriSCfgRetryInterval_Type()
)
friSCfgRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgRetryInterval.setStatus("mandatory")


class _FriSCfgCallAttempts_Type(Integer32):
    """Custom type friSCfgCallAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FriSCfgCallAttempts_Type.__name__ = "Integer32"
_FriSCfgCallAttempts_Object = MibTableColumn
friSCfgCallAttempts = _FriSCfgCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 40),
    _FriSCfgCallAttempts_Type()
)
friSCfgCallAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgCallAttempts.setStatus("mandatory")


class _FriSCfgIdleInterval_Type(Integer32):
    """Custom type friSCfgIdleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_FriSCfgIdleInterval_Type.__name__ = "Integer32"
_FriSCfgIdleInterval_Object = MibTableColumn
friSCfgIdleInterval = _FriSCfgIdleInterval_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 41),
    _FriSCfgIdleInterval_Type()
)
friSCfgIdleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgIdleInterval.setStatus("mandatory")
_FriSCfgIeNegotiation_Type = DisplayString
_FriSCfgIeNegotiation_Object = MibTableColumn
friSCfgIeNegotiation = _FriSCfgIeNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 42),
    _FriSCfgIeNegotiation_Type()
)
friSCfgIeNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgIeNegotiation.setStatus("mandatory")


class _FriSCfgSubaddress_Type(OctetString):
    """Custom type friSCfgSubaddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 6),
    )


_FriSCfgSubaddress_Type.__name__ = "OctetString"
_FriSCfgSubaddress_Object = MibTableColumn
friSCfgSubaddress = _FriSCfgSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 43),
    _FriSCfgSubaddress_Type()
)
friSCfgSubaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgSubaddress.setStatus("mandatory")


class _FriSCfgCalledNumber_Type(OctetString):
    """Custom type friSCfgCalledNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 19),
    )


_FriSCfgCalledNumber_Type.__name__ = "OctetString"
_FriSCfgCalledNumber_Object = MibTableColumn
friSCfgCalledNumber = _FriSCfgCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 44),
    _FriSCfgCalledNumber_Type()
)
friSCfgCalledNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgCalledNumber.setStatus("mandatory")


class _FriSCfgCalledSubaddress_Type(OctetString):
    """Custom type friSCfgCalledSubaddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 6),
    )


_FriSCfgCalledSubaddress_Type.__name__ = "OctetString"
_FriSCfgCalledSubaddress_Object = MibTableColumn
friSCfgCalledSubaddress = _FriSCfgCalledSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 45),
    _FriSCfgCalledSubaddress_Type()
)
friSCfgCalledSubaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgCalledSubaddress.setStatus("mandatory")


class _FriSCfgMinCir_Type(Integer32):
    """Custom type friSCfgMinCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_FriSCfgMinCir_Type.__name__ = "Integer32"
_FriSCfgMinCir_Object = MibTableColumn
friSCfgMinCir = _FriSCfgMinCir_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 46),
    _FriSCfgMinCir_Type()
)
friSCfgMinCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgMinCir.setStatus("mandatory")


class _FriSCfgBurstExcess_Type(Integer32):
    """Custom type friSCfgBurstExcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096000),
    )


_FriSCfgBurstExcess_Type.__name__ = "Integer32"
_FriSCfgBurstExcess_Object = MibTableColumn
friSCfgBurstExcess = _FriSCfgBurstExcess_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 47),
    _FriSCfgBurstExcess_Type()
)
friSCfgBurstExcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgBurstExcess.setStatus("mandatory")


class _FriSCfgE2EEnabled_Type(Integer32):
    """Custom type friSCfgE2EEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FriSCfgE2EEnabled_Type.__name__ = "Integer32"
_FriSCfgE2EEnabled_Object = MibTableColumn
friSCfgE2EEnabled = _FriSCfgE2EEnabled_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 48),
    _FriSCfgE2EEnabled_Type()
)
friSCfgE2EEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgE2EEnabled.setStatus("mandatory")


class _FriSCfgE2EType_Type(Integer32):
    """Custom type friSCfgE2EType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frf12", 2),
          ("motorola", 1))
    )


_FriSCfgE2EType_Type.__name__ = "Integer32"
_FriSCfgE2EType_Object = MibTableColumn
friSCfgE2EType = _FriSCfgE2EType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 49),
    _FriSCfgE2EType_Type()
)
friSCfgE2EType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgE2EType.setStatus("mandatory")


class _FriSCfgE2ESSVP_Type(Integer32):
    """Custom type friSCfgE2ESSVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65,
              129,
              257,
              513,
              1025)
        )
    )
    namedValues = NamedValues(
        *(("segSize1024", 1025),
          ("segSize128", 129),
          ("segSize256", 257),
          ("segSize512", 513),
          ("segSize64", 65))
    )


_FriSCfgE2ESSVP_Type.__name__ = "Integer32"
_FriSCfgE2ESSVP_Object = MibTableColumn
friSCfgE2ESSVP = _FriSCfgE2ESSVP_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 50),
    _FriSCfgE2ESSVP_Type()
)
friSCfgE2ESSVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSCfgE2ESSVP.setStatus("mandatory")


class _FriSCfgE2ESSVNP_Type(Integer32):
    """Custom type friSCfgE2ESSVNP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65,
              129,
              257,
              513,
              1025,
              2049,
              4097,
              32000)
        )
    )
    namedValues = NamedValues(
        *(("disable", 32000),
          ("segSize1024", 1025),
          ("segSize128", 129),
          ("segSize2048", 2049),
          ("segSize256", 257),
          ("segSize4096", 4097),
          ("segSize512", 513),
          ("segSize64", 65))
    )


_FriSCfgE2ESSVNP_Type.__name__ = "Integer32"
_FriSCfgE2ESSVNP_Object = MibTableColumn
friSCfgE2ESSVNP = _FriSCfgE2ESSVNP_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 51),
    _FriSCfgE2ESSVNP_Type()
)
friSCfgE2ESSVNP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgE2ESSVNP.setStatus("mandatory")


class _FriSCfgE2ESegDelayEnabled_Type(Integer32):
    """Custom type friSCfgE2ESegDelayEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FriSCfgE2ESegDelayEnabled_Type.__name__ = "Integer32"
_FriSCfgE2ESegDelayEnabled_Object = MibTableColumn
friSCfgE2ESegDelayEnabled = _FriSCfgE2ESegDelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 52),
    _FriSCfgE2ESegDelayEnabled_Type()
)
friSCfgE2ESegDelayEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgE2ESegDelayEnabled.setStatus("mandatory")


class _FriSCfgE2ECheckPckSize_Type(Integer32):
    """Custom type friSCfgE2ECheckPckSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FriSCfgE2ECheckPckSize_Type.__name__ = "Integer32"
_FriSCfgE2ECheckPckSize_Object = MibTableColumn
friSCfgE2ECheckPckSize = _FriSCfgE2ECheckPckSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 53),
    _FriSCfgE2ECheckPckSize_Type()
)
friSCfgE2ECheckPckSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgE2ECheckPckSize.setStatus("mandatory")


class _FriSCfgvoice_header_Type(Integer32):
    """Custom type friSCfgvoice_header based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FriSCfgvoice_header_Type.__name__ = "Integer32"
_FriSCfgvoice_header_Object = MibScalar
friSCfgvoice_header = _FriSCfgvoice_header_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 9, 1, 54),
    _FriSCfgvoice_header_Type()
)
friSCfgvoice_header.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friSCfgvoice_header.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PPSTFRIPStatsTable_ObjectIdentity = ObjectIdentity
cdx6500PPSTFRIPStatsTable = _Cdx6500PPSTFRIPStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32)
)
_Cdx6500PPSTFRIPortTable_Object = MibTable
cdx6500PPSTFRIPortTable = _Cdx6500PPSTFRIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPSTFRIPortTable.setStatus("mandatory")
_Cdx6500PPSTFRIPortEntry_Object = MibTableRow
cdx6500PPSTFRIPortEntry = _Cdx6500PPSTFRIPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 1, 1)
)
cdx6500PPSTFRIPortEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friPStatsPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTFRIPortEntry.setStatus("mandatory")


class _FriPStatsPortNumber_Type(Integer32):
    """Custom type friPStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriPStatsPortNumber_Type.__name__ = "Integer32"
_FriPStatsPortNumber_Object = MibTableColumn
friPStatsPortNumber = _FriPStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 1, 1, 1),
    _FriPStatsPortNumber_Type()
)
friPStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsPortNumber.setStatus("mandatory")


class _FriPStatsPortType_Type(Integer32):
    """Custom type friPStatsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            17
        )
    )
    namedValues = NamedValues(
        ("fri", 17)
    )


_FriPStatsPortType_Type.__name__ = "Integer32"
_FriPStatsPortType_Object = MibTableColumn
friPStatsPortType = _FriPStatsPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 1, 1, 2),
    _FriPStatsPortType_Type()
)
friPStatsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsPortType.setStatus("mandatory")


class _FriPStatsPortStatus_Type(Integer32):
    """Custom type friPStatsPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 3),
          ("disabled", 1),
          ("down", 5),
          ("enabled", 2),
          ("na", 100),
          ("up", 4))
    )


_FriPStatsPortStatus_Type.__name__ = "Integer32"
_FriPStatsPortStatus_Object = MibTableColumn
friPStatsPortStatus = _FriPStatsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 1, 1, 3),
    _FriPStatsPortStatus_Type()
)
friPStatsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsPortStatus.setStatus("mandatory")
_FriPStatsConfiguredStns_Type = DisplayString
_FriPStatsConfiguredStns_Object = MibTableColumn
friPStatsConfiguredStns = _FriPStatsConfiguredStns_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 1, 1, 4),
    _FriPStatsConfiguredStns_Type()
)
friPStatsConfiguredStns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsConfiguredStns.setStatus("mandatory")
_FriPStatsPortSpeed_Type = Integer32
_FriPStatsPortSpeed_Object = MibTableColumn
friPStatsPortSpeed = _FriPStatsPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 1, 1, 5),
    _FriPStatsPortSpeed_Type()
)
friPStatsPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsPortSpeed.setStatus("mandatory")
_FriPStatsOpCntrlProtocol_Type = DisplayString
_FriPStatsOpCntrlProtocol_Object = MibTableColumn
friPStatsOpCntrlProtocol = _FriPStatsOpCntrlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 1, 1, 6),
    _FriPStatsOpCntrlProtocol_Type()
)
friPStatsOpCntrlProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsOpCntrlProtocol.setStatus("mandatory")
_FriPStatsSPBackup_Type = DisplayString
_FriPStatsSPBackup_Object = MibTableColumn
friPStatsSPBackup = _FriPStatsSPBackup_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 1, 1, 7),
    _FriPStatsSPBackup_Type()
)
friPStatsSPBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsSPBackup.setStatus("mandatory")
_FriPStatsPriorityStn_Type = Integer32
_FriPStatsPriorityStn_Object = MibTableColumn
friPStatsPriorityStn = _FriPStatsPriorityStn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 1, 1, 8),
    _FriPStatsPriorityStn_Type()
)
friPStatsPriorityStn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsPriorityStn.setStatus("mandatory")
_FriPStatsLastStatsReset_Type = DisplayString
_FriPStatsLastStatsReset_Object = MibTableColumn
friPStatsLastStatsReset = _FriPStatsLastStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 1, 1, 9),
    _FriPStatsLastStatsReset_Type()
)
friPStatsLastStatsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsLastStatsReset.setStatus("mandatory")
_Cdx6500PPSTFRIDataSummaryTable_Object = MibTable
cdx6500PPSTFRIDataSummaryTable = _Cdx6500PPSTFRIDataSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2)
)
if mibBuilder.loadTexts:
    cdx6500PPSTFRIDataSummaryTable.setStatus("mandatory")
_Cdx6500PPSTFRIDataSummaryEntry_Object = MibTableRow
cdx6500PPSTFRIDataSummaryEntry = _Cdx6500PPSTFRIDataSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1)
)
cdx6500PPSTFRIDataSummaryEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friDataSummPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTFRIDataSummaryEntry.setStatus("mandatory")


class _FriDataSummPortNumber_Type(Integer32):
    """Custom type friDataSummPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriDataSummPortNumber_Type.__name__ = "Integer32"
_FriDataSummPortNumber_Object = MibTableColumn
friDataSummPortNumber = _FriDataSummPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 1),
    _FriDataSummPortNumber_Type()
)
friDataSummPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friDataSummPortNumber.setStatus("mandatory")
_FriPStatsCharInTotal_Type = Counter32
_FriPStatsCharInTotal_Object = MibTableColumn
friPStatsCharInTotal = _FriPStatsCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 2),
    _FriPStatsCharInTotal_Type()
)
friPStatsCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsCharInTotal.setStatus("mandatory")
_FriPStatsCharOutTotal_Type = Counter32
_FriPStatsCharOutTotal_Object = MibTableColumn
friPStatsCharOutTotal = _FriPStatsCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 3),
    _FriPStatsCharOutTotal_Type()
)
friPStatsCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsCharOutTotal.setStatus("mandatory")
_FriPStatsCharInPerSec_Type = Integer32
_FriPStatsCharInPerSec_Object = MibTableColumn
friPStatsCharInPerSec = _FriPStatsCharInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 4),
    _FriPStatsCharInPerSec_Type()
)
friPStatsCharInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsCharInPerSec.setStatus("mandatory")
_FriPStatsCharOutPerSec_Type = Integer32
_FriPStatsCharOutPerSec_Object = MibTableColumn
friPStatsCharOutPerSec = _FriPStatsCharOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 5),
    _FriPStatsCharOutPerSec_Type()
)
friPStatsCharOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsCharOutPerSec.setStatus("mandatory")
_FriPStatsFramesInTotal_Type = Counter32
_FriPStatsFramesInTotal_Object = MibTableColumn
friPStatsFramesInTotal = _FriPStatsFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 6),
    _FriPStatsFramesInTotal_Type()
)
friPStatsFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsFramesInTotal.setStatus("mandatory")
_FriPStatsFramesOutTotal_Type = Counter32
_FriPStatsFramesOutTotal_Object = MibTableColumn
friPStatsFramesOutTotal = _FriPStatsFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 7),
    _FriPStatsFramesOutTotal_Type()
)
friPStatsFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsFramesOutTotal.setStatus("mandatory")
_FriPStatsFramesInPerSec_Type = Integer32
_FriPStatsFramesInPerSec_Object = MibTableColumn
friPStatsFramesInPerSec = _FriPStatsFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 8),
    _FriPStatsFramesInPerSec_Type()
)
friPStatsFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsFramesInPerSec.setStatus("mandatory")
_FriPStatsFramesOutPerSec_Type = Integer32
_FriPStatsFramesOutPerSec_Object = MibTableColumn
friPStatsFramesOutPerSec = _FriPStatsFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 9),
    _FriPStatsFramesOutPerSec_Type()
)
friPStatsFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsFramesOutPerSec.setStatus("mandatory")
_FriPStatsAvFrameSizeIn_Type = Integer32
_FriPStatsAvFrameSizeIn_Object = MibTableColumn
friPStatsAvFrameSizeIn = _FriPStatsAvFrameSizeIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 10),
    _FriPStatsAvFrameSizeIn_Type()
)
friPStatsAvFrameSizeIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsAvFrameSizeIn.setStatus("mandatory")
_FriPStatsAvFrameSizeOut_Type = Integer32
_FriPStatsAvFrameSizeOut_Object = MibTableColumn
friPStatsAvFrameSizeOut = _FriPStatsAvFrameSizeOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 11),
    _FriPStatsAvFrameSizeOut_Type()
)
friPStatsAvFrameSizeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsAvFrameSizeOut.setStatus("mandatory")
_FriPStatsUtilIn_Type = Integer32
_FriPStatsUtilIn_Object = MibTableColumn
friPStatsUtilIn = _FriPStatsUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 12),
    _FriPStatsUtilIn_Type()
)
friPStatsUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsUtilIn.setStatus("mandatory")
_FriPStatsUtilOut_Type = Integer32
_FriPStatsUtilOut_Object = MibTableColumn
friPStatsUtilOut = _FriPStatsUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 2, 1, 13),
    _FriPStatsUtilOut_Type()
)
friPStatsUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsUtilOut.setStatus("mandatory")
_Cdx6500PPSTFRISummaryTable_Object = MibTable
cdx6500PPSTFRISummaryTable = _Cdx6500PPSTFRISummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3)
)
if mibBuilder.loadTexts:
    cdx6500PPSTFRISummaryTable.setStatus("mandatory")
_Cdx6500PPSTFRISummaryEntry_Object = MibTableRow
cdx6500PPSTFRISummaryEntry = _Cdx6500PPSTFRISummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1)
)
cdx6500PPSTFRISummaryEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friSummPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTFRISummaryEntry.setStatus("mandatory")


class _FriSummPortNumber_Type(Integer32):
    """Custom type friSummPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriSummPortNumber_Type.__name__ = "Integer32"
_FriSummPortNumber_Object = MibTableColumn
friSummPortNumber = _FriSummPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 1),
    _FriSummPortNumber_Type()
)
friSummPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSummPortNumber.setStatus("mandatory")
_FriPStatsCRCErrors_Type = Counter32
_FriPStatsCRCErrors_Object = MibTableColumn
friPStatsCRCErrors = _FriPStatsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 2),
    _FriPStatsCRCErrors_Type()
)
friPStatsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsCRCErrors.setStatus("mandatory")
_FriPStatsOverrunErrors_Type = Counter32
_FriPStatsOverrunErrors_Object = MibTableColumn
friPStatsOverrunErrors = _FriPStatsOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 3),
    _FriPStatsOverrunErrors_Type()
)
friPStatsOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsOverrunErrors.setStatus("mandatory")
_FriPStatsFrameLengthErrors_Type = Counter32
_FriPStatsFrameLengthErrors_Object = MibTableColumn
friPStatsFrameLengthErrors = _FriPStatsFrameLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 4),
    _FriPStatsFrameLengthErrors_Type()
)
friPStatsFrameLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsFrameLengthErrors.setStatus("mandatory")
_FriPStatsUnderrunErrors_Type = Counter32
_FriPStatsUnderrunErrors_Object = MibTableColumn
friPStatsUnderrunErrors = _FriPStatsUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 5),
    _FriPStatsUnderrunErrors_Type()
)
friPStatsUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsUnderrunErrors.setStatus("mandatory")
_FriPStatsUnknownDLCICount_Type = Counter32
_FriPStatsUnknownDLCICount_Object = MibTableColumn
friPStatsUnknownDLCICount = _FriPStatsUnknownDLCICount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 6),
    _FriPStatsUnknownDLCICount_Type()
)
friPStatsUnknownDLCICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsUnknownDLCICount.setStatus("mandatory")
_FriPStatsLastUnknownDLCI_Type = Integer32
_FriPStatsLastUnknownDLCI_Object = MibTableColumn
friPStatsLastUnknownDLCI = _FriPStatsLastUnknownDLCI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 7),
    _FriPStatsLastUnknownDLCI_Type()
)
friPStatsLastUnknownDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsLastUnknownDLCI.setStatus("mandatory")
_FriPStatsSplittingRatio_Type = Integer32
_FriPStatsSplittingRatio_Object = MibTableColumn
friPStatsSplittingRatio = _FriPStatsSplittingRatio_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 8),
    _FriPStatsSplittingRatio_Type()
)
friPStatsSplittingRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsSplittingRatio.setStatus("mandatory")
_FriPStatsTotalSegmentsLost_Type = Integer32
_FriPStatsTotalSegmentsLost_Object = MibTableColumn
friPStatsTotalSegmentsLost = _FriPStatsTotalSegmentsLost_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 9),
    _FriPStatsTotalSegmentsLost_Type()
)
friPStatsTotalSegmentsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsTotalSegmentsLost.setStatus("mandatory")
_FriPStatsMaxContiguousSegmentsLost_Type = Integer32
_FriPStatsMaxContiguousSegmentsLost_Object = MibTableColumn
friPStatsMaxContiguousSegmentsLost = _FriPStatsMaxContiguousSegmentsLost_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 10),
    _FriPStatsMaxContiguousSegmentsLost_Type()
)
friPStatsMaxContiguousSegmentsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsMaxContiguousSegmentsLost.setStatus("mandatory")
_FriPStatsVoiceBWOnPort_Type = Integer32
_FriPStatsVoiceBWOnPort_Object = MibTableColumn
friPStatsVoiceBWOnPort = _FriPStatsVoiceBWOnPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 11),
    _FriPStatsVoiceBWOnPort_Type()
)
friPStatsVoiceBWOnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsVoiceBWOnPort.setStatus("mandatory")
_FriPStatsFrameSegmenterSyncLost_Type = Integer32
_FriPStatsFrameSegmenterSyncLost_Object = MibTableColumn
friPStatsFrameSegmenterSyncLost = _FriPStatsFrameSegmenterSyncLost_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 12),
    _FriPStatsFrameSegmenterSyncLost_Type()
)
friPStatsFrameSegmenterSyncLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsFrameSegmenterSyncLost.setStatus("mandatory")
_FriPStatsStatusEnqSentFull_Type = Integer32
_FriPStatsStatusEnqSentFull_Object = MibTableColumn
friPStatsStatusEnqSentFull = _FriPStatsStatusEnqSentFull_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 13),
    _FriPStatsStatusEnqSentFull_Type()
)
friPStatsStatusEnqSentFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsStatusEnqSentFull.setStatus("mandatory")
_FriPStatsFullStatusRecd_Type = Integer32
_FriPStatsFullStatusRecd_Object = MibTableColumn
friPStatsFullStatusRecd = _FriPStatsFullStatusRecd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 14),
    _FriPStatsFullStatusRecd_Type()
)
friPStatsFullStatusRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsFullStatusRecd.setStatus("mandatory")
_FriPStatsStatusEnqSentLIV_Type = Integer32
_FriPStatsStatusEnqSentLIV_Object = MibTableColumn
friPStatsStatusEnqSentLIV = _FriPStatsStatusEnqSentLIV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 15),
    _FriPStatsStatusEnqSentLIV_Type()
)
friPStatsStatusEnqSentLIV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsStatusEnqSentLIV.setStatus("mandatory")
_FriPStatsLIVStatusRecd_Type = Integer32
_FriPStatsLIVStatusRecd_Object = MibTableColumn
friPStatsLIVStatusRecd = _FriPStatsLIVStatusRecd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 16),
    _FriPStatsLIVStatusRecd_Type()
)
friPStatsLIVStatusRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsLIVStatusRecd.setStatus("mandatory")
_FriPStatsStatusEnqRecdFull_Type = Integer32
_FriPStatsStatusEnqRecdFull_Object = MibTableColumn
friPStatsStatusEnqRecdFull = _FriPStatsStatusEnqRecdFull_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 17),
    _FriPStatsStatusEnqRecdFull_Type()
)
friPStatsStatusEnqRecdFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsStatusEnqRecdFull.setStatus("mandatory")
_FriPStatsStatusEnqRecdLIV_Type = Integer32
_FriPStatsStatusEnqRecdLIV_Object = MibTableColumn
friPStatsStatusEnqRecdLIV = _FriPStatsStatusEnqRecdLIV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 18),
    _FriPStatsStatusEnqRecdLIV_Type()
)
friPStatsStatusEnqRecdLIV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsStatusEnqRecdLIV.setStatus("mandatory")
_FriPStatsAsyncUpdateRecd_Type = Integer32
_FriPStatsAsyncUpdateRecd_Object = MibTableColumn
friPStatsAsyncUpdateRecd = _FriPStatsAsyncUpdateRecd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 19),
    _FriPStatsAsyncUpdateRecd_Type()
)
friPStatsAsyncUpdateRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsAsyncUpdateRecd.setStatus("mandatory")
_FriPStatsSeqNumMismatch_Type = Integer32
_FriPStatsSeqNumMismatch_Object = MibTableColumn
friPStatsSeqNumMismatch = _FriPStatsSeqNumMismatch_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 20),
    _FriPStatsSeqNumMismatch_Type()
)
friPStatsSeqNumMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsSeqNumMismatch.setStatus("mandatory")
_FriPStatsTimeouts_Type = Integer32
_FriPStatsTimeouts_Object = MibTableColumn
friPStatsTimeouts = _FriPStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 3, 1, 21),
    _FriPStatsTimeouts_Type()
)
friPStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsTimeouts.setStatus("mandatory")
_Cdx6500PPSTFRIISDNCallStatusTable_Object = MibTable
cdx6500PPSTFRIISDNCallStatusTable = _Cdx6500PPSTFRIISDNCallStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4)
)
if mibBuilder.loadTexts:
    cdx6500PPSTFRIISDNCallStatusTable.setStatus("mandatory")
_Cdx6500PPSTFRIISDNCallStatusEntry_Object = MibTableRow
cdx6500PPSTFRIISDNCallStatusEntry = _Cdx6500PPSTFRIISDNCallStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1)
)
cdx6500PPSTFRIISDNCallStatusEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friISDNCallStatusPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTFRIISDNCallStatusEntry.setStatus("mandatory")


class _FriISDNCallStatusPortNumber_Type(Integer32):
    """Custom type friISDNCallStatusPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriISDNCallStatusPortNumber_Type.__name__ = "Integer32"
_FriISDNCallStatusPortNumber_Object = MibTableColumn
friISDNCallStatusPortNumber = _FriISDNCallStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 1),
    _FriISDNCallStatusPortNumber_Type()
)
friISDNCallStatusPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friISDNCallStatusPortNumber.setStatus("mandatory")
_FriPStatsNumRxCallsSinceLastReset_Type = Integer32
_FriPStatsNumRxCallsSinceLastReset_Object = MibTableColumn
friPStatsNumRxCallsSinceLastReset = _FriPStatsNumRxCallsSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 2),
    _FriPStatsNumRxCallsSinceLastReset_Type()
)
friPStatsNumRxCallsSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsNumRxCallsSinceLastReset.setStatus("mandatory")
_FriPStatsNumRxCallsRejected_Type = Integer32
_FriPStatsNumRxCallsRejected_Object = MibTableColumn
friPStatsNumRxCallsRejected = _FriPStatsNumRxCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 3),
    _FriPStatsNumRxCallsRejected_Type()
)
friPStatsNumRxCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsNumRxCallsRejected.setStatus("mandatory")


class _FriPStatsRxLastCallFailureCause_Type(Integer32):
    """Custom type friPStatsRxLastCallFailureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("callCollision", 200),
          ("callRejected", 197),
          ("failureNotSupported", 203),
          ("invalidConfiguration", 202),
          ("invalidPhoneNumber", 198),
          ("na", 100),
          ("noAvailableVirtualPort", 194),
          ("noFailureReported", 193),
          ("noResourcesAvailable", 196),
          ("outgoingCallRequestTimeout", 199),
          ("securityViolation", 195),
          ("virtualPortNotAvailable", 201))
    )


_FriPStatsRxLastCallFailureCause_Type.__name__ = "Integer32"
_FriPStatsRxLastCallFailureCause_Object = MibTableColumn
friPStatsRxLastCallFailureCause = _FriPStatsRxLastCallFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 4),
    _FriPStatsRxLastCallFailureCause_Type()
)
friPStatsRxLastCallFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsRxLastCallFailureCause.setStatus("mandatory")
_FriPStatsRxLastCalledNumber_Type = DisplayString
_FriPStatsRxLastCalledNumber_Object = MibTableColumn
friPStatsRxLastCalledNumber = _FriPStatsRxLastCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 5),
    _FriPStatsRxLastCalledNumber_Type()
)
friPStatsRxLastCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsRxLastCalledNumber.setStatus("mandatory")
_FriPStatsRxLastCallingNumber_Type = DisplayString
_FriPStatsRxLastCallingNumber_Object = MibTableColumn
friPStatsRxLastCallingNumber = _FriPStatsRxLastCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 6),
    _FriPStatsRxLastCallingNumber_Type()
)
friPStatsRxLastCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsRxLastCallingNumber.setStatus("mandatory")
_FriPStatsRxMinCallDuration_Type = DisplayString
_FriPStatsRxMinCallDuration_Object = MibTableColumn
friPStatsRxMinCallDuration = _FriPStatsRxMinCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 7),
    _FriPStatsRxMinCallDuration_Type()
)
friPStatsRxMinCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsRxMinCallDuration.setStatus("mandatory")
_FriPStatsRxMaxCallDuration_Type = DisplayString
_FriPStatsRxMaxCallDuration_Object = MibTableColumn
friPStatsRxMaxCallDuration = _FriPStatsRxMaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 8),
    _FriPStatsRxMaxCallDuration_Type()
)
friPStatsRxMaxCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsRxMaxCallDuration.setStatus("mandatory")
_FriPStatsRxAvgCallDuration_Type = DisplayString
_FriPStatsRxAvgCallDuration_Object = MibTableColumn
friPStatsRxAvgCallDuration = _FriPStatsRxAvgCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 9),
    _FriPStatsRxAvgCallDuration_Type()
)
friPStatsRxAvgCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsRxAvgCallDuration.setStatus("mandatory")
_FriPStatsNumTxCallsSinceLastReset_Type = Integer32
_FriPStatsNumTxCallsSinceLastReset_Object = MibTableColumn
friPStatsNumTxCallsSinceLastReset = _FriPStatsNumTxCallsSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 10),
    _FriPStatsNumTxCallsSinceLastReset_Type()
)
friPStatsNumTxCallsSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsNumTxCallsSinceLastReset.setStatus("mandatory")
_FriPStatsNumTxCallsRejected_Type = Integer32
_FriPStatsNumTxCallsRejected_Object = MibTableColumn
friPStatsNumTxCallsRejected = _FriPStatsNumTxCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 11),
    _FriPStatsNumTxCallsRejected_Type()
)
friPStatsNumTxCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsNumTxCallsRejected.setStatus("mandatory")


class _FriPStatsTxLastCallFailureCause_Type(Integer32):
    """Custom type friPStatsTxLastCallFailureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("callCollision", 200),
          ("callRejected", 197),
          ("failureNotSupported", 203),
          ("invalidConfiguration", 202),
          ("invalidPhoneNumber", 198),
          ("na", 100),
          ("noAvailableVirtualPort", 194),
          ("noFailureReported", 193),
          ("noResourcesAvailable", 196),
          ("outgoingCallRequestTimeout", 199),
          ("securityViolation", 195),
          ("virtualPortNotAvailable", 201))
    )


_FriPStatsTxLastCallFailureCause_Type.__name__ = "Integer32"
_FriPStatsTxLastCallFailureCause_Object = MibTableColumn
friPStatsTxLastCallFailureCause = _FriPStatsTxLastCallFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 12),
    _FriPStatsTxLastCallFailureCause_Type()
)
friPStatsTxLastCallFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsTxLastCallFailureCause.setStatus("mandatory")
_FriPStatsTxLastCalledNumber_Type = DisplayString
_FriPStatsTxLastCalledNumber_Object = MibTableColumn
friPStatsTxLastCalledNumber = _FriPStatsTxLastCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 13),
    _FriPStatsTxLastCalledNumber_Type()
)
friPStatsTxLastCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsTxLastCalledNumber.setStatus("mandatory")
_FriPStatsTxLastCallingNumber_Type = DisplayString
_FriPStatsTxLastCallingNumber_Object = MibTableColumn
friPStatsTxLastCallingNumber = _FriPStatsTxLastCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 14),
    _FriPStatsTxLastCallingNumber_Type()
)
friPStatsTxLastCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsTxLastCallingNumber.setStatus("mandatory")
_FriPStatsTxMinCallDuration_Type = DisplayString
_FriPStatsTxMinCallDuration_Object = MibTableColumn
friPStatsTxMinCallDuration = _FriPStatsTxMinCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 15),
    _FriPStatsTxMinCallDuration_Type()
)
friPStatsTxMinCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsTxMinCallDuration.setStatus("mandatory")
_FriPStatsTxMaxCallDuration_Type = DisplayString
_FriPStatsTxMaxCallDuration_Object = MibTableColumn
friPStatsTxMaxCallDuration = _FriPStatsTxMaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 16),
    _FriPStatsTxMaxCallDuration_Type()
)
friPStatsTxMaxCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsTxMaxCallDuration.setStatus("mandatory")
_FriPStatsTxAvgCallDuration_Type = DisplayString
_FriPStatsTxAvgCallDuration_Object = MibTableColumn
friPStatsTxAvgCallDuration = _FriPStatsTxAvgCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 17),
    _FriPStatsTxAvgCallDuration_Type()
)
friPStatsTxAvgCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsTxAvgCallDuration.setStatus("mandatory")


class _FriPStatsSignalingState_Type(Integer32):
    """Custom type friPStatsSignalingState based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("congested", 4),
          ("connected", 3),
          ("dChannelDown", 6),
          ("disabled", 5),
          ("disabledDChannelDown", 7),
          ("disconnecting", 8),
          ("idle", 1),
          ("na", 100),
          ("ringing", 2))
    )


_FriPStatsSignalingState_Type.__name__ = "Integer32"
_FriPStatsSignalingState_Object = MibTableColumn
friPStatsSignalingState = _FriPStatsSignalingState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 32, 4, 1, 18),
    _FriPStatsSignalingState_Type()
)
friPStatsSignalingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friPStatsSignalingState.setStatus("mandatory")
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500SPSTFRISStatsTable_ObjectIdentity = ObjectIdentity
cdx6500SPSTFRISStatsTable = _Cdx6500SPSTFRISStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10)
)
_FriSGenStatsTable_Object = MibTable
friSGenStatsTable = _FriSGenStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1)
)
if mibBuilder.loadTexts:
    friSGenStatsTable.setStatus("mandatory")
_Cdx6500friSGenStatsEntry_Object = MibTableRow
cdx6500friSGenStatsEntry = _Cdx6500friSGenStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1)
)
cdx6500friSGenStatsEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friSGenStatsPortNumber"),
    (0, "FRI-OPT-MIB", "friSGenStatsStnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500friSGenStatsEntry.setStatus("mandatory")


class _FriSGenStatsPortNumber_Type(Integer32):
    """Custom type friSGenStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriSGenStatsPortNumber_Type.__name__ = "Integer32"
_FriSGenStatsPortNumber_Object = MibTableColumn
friSGenStatsPortNumber = _FriSGenStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 1),
    _FriSGenStatsPortNumber_Type()
)
friSGenStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSGenStatsPortNumber.setStatus("mandatory")


class _FriSGenStatsStnNumber_Type(Integer32):
    """Custom type friSGenStatsStnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FriSGenStatsStnNumber_Type.__name__ = "Integer32"
_FriSGenStatsStnNumber_Object = MibTableColumn
friSGenStatsStnNumber = _FriSGenStatsStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 2),
    _FriSGenStatsStnNumber_Type()
)
friSGenStatsStnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSGenStatsStnNumber.setStatus("mandatory")


class _FriSStatsStnType_Type(Integer32):
    """Custom type friSStatsStnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annexG", 1),
          ("bypass", 2),
          ("voice", 3))
    )


_FriSStatsStnType_Type.__name__ = "Integer32"
_FriSStatsStnType_Object = MibTableColumn
friSStatsStnType = _FriSStatsStnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 3),
    _FriSStatsStnType_Type()
)
friSStatsStnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsStnType.setStatus("mandatory")
_FriSStatsStnStatus_Type = DisplayString
_FriSStatsStnStatus_Object = MibTableColumn
friSStatsStnStatus = _FriSStatsStnStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 4),
    _FriSStatsStnStatus_Type()
)
friSStatsStnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsStnStatus.setStatus("mandatory")
_FriSStatsDLCI_Type = Integer32
_FriSStatsDLCI_Object = MibTableColumn
friSStatsDLCI = _FriSStatsDLCI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 5),
    _FriSStatsDLCI_Type()
)
friSStatsDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsDLCI.setStatus("mandatory")
_FriSStatsStnState_Type = DisplayString
_FriSStatsStnState_Object = MibTableColumn
friSStatsStnState = _FriSStatsStnState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 6),
    _FriSStatsStnState_Type()
)
friSStatsStnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsStnState.setStatus("mandatory")
_FriSStatsConfiguredCIR_Type = Integer32
_FriSStatsConfiguredCIR_Object = MibTableColumn
friSStatsConfiguredCIR = _FriSStatsConfiguredCIR_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 7),
    _FriSStatsConfiguredCIR_Type()
)
friSStatsConfiguredCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsConfiguredCIR.setStatus("mandatory")
_FriSStatsAllowedInfoRate_Type = Integer32
_FriSStatsAllowedInfoRate_Object = MibTableColumn
friSStatsAllowedInfoRate = _FriSStatsAllowedInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 8),
    _FriSStatsAllowedInfoRate_Type()
)
friSStatsAllowedInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsAllowedInfoRate.setStatus("mandatory")
_FriSStatsImpCongDetect_Type = Integer32
_FriSStatsImpCongDetect_Object = MibTableColumn
friSStatsImpCongDetect = _FriSStatsImpCongDetect_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 9),
    _FriSStatsImpCongDetect_Type()
)
friSStatsImpCongDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsImpCongDetect.setStatus("mandatory")
_FriSStatsExpCongDetect_Type = Integer32
_FriSStatsExpCongDetect_Object = MibTableColumn
friSStatsExpCongDetect = _FriSStatsExpCongDetect_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 10),
    _FriSStatsExpCongDetect_Type()
)
friSStatsExpCongDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsExpCongDetect.setStatus("mandatory")


class _FriSStatsLMIFlowCntrl_Type(Integer32):
    """Custom type friSStatsLMIFlowCntrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("na", 100),
          ("off", 1),
          ("on", 2))
    )


_FriSStatsLMIFlowCntrl_Type.__name__ = "Integer32"
_FriSStatsLMIFlowCntrl_Object = MibTableColumn
friSStatsLMIFlowCntrl = _FriSStatsLMIFlowCntrl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 11),
    _FriSStatsLMIFlowCntrl_Type()
)
friSStatsLMIFlowCntrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsLMIFlowCntrl.setStatus("mandatory")
_FriSStatsMaxSVCCount_Type = Integer32
_FriSStatsMaxSVCCount_Object = MibTableColumn
friSStatsMaxSVCCount = _FriSStatsMaxSVCCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 12),
    _FriSStatsMaxSVCCount_Type()
)
friSStatsMaxSVCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsMaxSVCCount.setStatus("mandatory")
_FriSStatsCurrSVCCount_Type = Integer32
_FriSStatsCurrSVCCount_Object = MibTableColumn
friSStatsCurrSVCCount = _FriSStatsCurrSVCCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 13),
    _FriSStatsCurrSVCCount_Type()
)
friSStatsCurrSVCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsCurrSVCCount.setStatus("mandatory")
_FriSStatsMaxPVCCount_Type = Integer32
_FriSStatsMaxPVCCount_Object = MibTableColumn
friSStatsMaxPVCCount = _FriSStatsMaxPVCCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 14),
    _FriSStatsMaxPVCCount_Type()
)
friSStatsMaxPVCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsMaxPVCCount.setStatus("mandatory")
_FriSStatsCurrPVCCount_Type = Integer32
_FriSStatsCurrPVCCount_Object = MibTableColumn
friSStatsCurrPVCCount = _FriSStatsCurrPVCCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 15),
    _FriSStatsCurrPVCCount_Type()
)
friSStatsCurrPVCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsCurrPVCCount.setStatus("mandatory")
_FriSStatsLastStatsReset_Type = DisplayString
_FriSStatsLastStatsReset_Object = MibTableColumn
friSStatsLastStatsReset = _FriSStatsLastStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 16),
    _FriSStatsLastStatsReset_Type()
)
friSStatsLastStatsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsLastStatsReset.setStatus("mandatory")
_FriSStatsFrameSegState_Type = DisplayString
_FriSStatsFrameSegState_Object = MibTableColumn
friSStatsFrameSegState = _FriSStatsFrameSegState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 17),
    _FriSStatsFrameSegState_Type()
)
friSStatsFrameSegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsFrameSegState.setStatus("mandatory")
_FriSStatsFrameSegSyncLost_Type = Integer32
_FriSStatsFrameSegSyncLost_Object = MibTableColumn
friSStatsFrameSegSyncLost = _FriSStatsFrameSegSyncLost_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 18),
    _FriSStatsFrameSegSyncLost_Type()
)
friSStatsFrameSegSyncLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsFrameSegSyncLost.setStatus("mandatory")
_FriSStatsPVCState_Type = DisplayString
_FriSStatsPVCState_Object = MibTableColumn
friSStatsPVCState = _FriSStatsPVCState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 19),
    _FriSStatsPVCState_Type()
)
friSStatsPVCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsPVCState.setStatus("mandatory")
_FriSStatsVoiceCongDetect_Type = Integer32
_FriSStatsVoiceCongDetect_Object = MibTableColumn
friSStatsVoiceCongDetect = _FriSStatsVoiceCongDetect_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 20),
    _FriSStatsVoiceCongDetect_Type()
)
friSStatsVoiceCongDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsVoiceCongDetect.setStatus("mandatory")
_FriSStatsMaxVSVCCount_Type = Integer32
_FriSStatsMaxVSVCCount_Object = MibTableColumn
friSStatsMaxVSVCCount = _FriSStatsMaxVSVCCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 21),
    _FriSStatsMaxVSVCCount_Type()
)
friSStatsMaxVSVCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsMaxVSVCCount.setStatus("mandatory")
_FriSStatsCurrVSVCCount_Type = Integer32
_FriSStatsCurrVSVCCount_Object = MibTableColumn
friSStatsCurrVSVCCount = _FriSStatsCurrVSVCCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 1, 1, 22),
    _FriSStatsCurrVSVCCount_Type()
)
friSStatsCurrVSVCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsCurrVSVCCount.setStatus("mandatory")
_FriSDataSummaryStatsTable_Object = MibTable
friSDataSummaryStatsTable = _FriSDataSummaryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2)
)
if mibBuilder.loadTexts:
    friSDataSummaryStatsTable.setStatus("mandatory")
_Cdx6500friSDataSummaryStatsEntry_Object = MibTableRow
cdx6500friSDataSummaryStatsEntry = _Cdx6500friSDataSummaryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1)
)
cdx6500friSDataSummaryStatsEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friSDataSummStatsPortNumber"),
    (0, "FRI-OPT-MIB", "friSDataSummStatsStnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500friSDataSummaryStatsEntry.setStatus("mandatory")


class _FriSDataSummStatsPortNumber_Type(Integer32):
    """Custom type friSDataSummStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriSDataSummStatsPortNumber_Type.__name__ = "Integer32"
_FriSDataSummStatsPortNumber_Object = MibTableColumn
friSDataSummStatsPortNumber = _FriSDataSummStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 1),
    _FriSDataSummStatsPortNumber_Type()
)
friSDataSummStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSDataSummStatsPortNumber.setStatus("mandatory")


class _FriSDataSummStatsStnNumber_Type(Integer32):
    """Custom type friSDataSummStatsStnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FriSDataSummStatsStnNumber_Type.__name__ = "Integer32"
_FriSDataSummStatsStnNumber_Object = MibTableColumn
friSDataSummStatsStnNumber = _FriSDataSummStatsStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 2),
    _FriSDataSummStatsStnNumber_Type()
)
friSDataSummStatsStnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSDataSummStatsStnNumber.setStatus("mandatory")
_FriSStatsCharInTotal_Type = Counter32
_FriSStatsCharInTotal_Object = MibTableColumn
friSStatsCharInTotal = _FriSStatsCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 3),
    _FriSStatsCharInTotal_Type()
)
friSStatsCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsCharInTotal.setStatus("mandatory")
_FriSStatsCharOutTotal_Type = Counter32
_FriSStatsCharOutTotal_Object = MibTableColumn
friSStatsCharOutTotal = _FriSStatsCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 4),
    _FriSStatsCharOutTotal_Type()
)
friSStatsCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsCharOutTotal.setStatus("mandatory")
_FriSStatsCharInPerSec_Type = Integer32
_FriSStatsCharInPerSec_Object = MibTableColumn
friSStatsCharInPerSec = _FriSStatsCharInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 5),
    _FriSStatsCharInPerSec_Type()
)
friSStatsCharInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsCharInPerSec.setStatus("mandatory")
_FriSStatsCharOutPerSec_Type = Integer32
_FriSStatsCharOutPerSec_Object = MibTableColumn
friSStatsCharOutPerSec = _FriSStatsCharOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 6),
    _FriSStatsCharOutPerSec_Type()
)
friSStatsCharOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsCharOutPerSec.setStatus("mandatory")
_FriSStatsPktInTotal_Type = Counter32
_FriSStatsPktInTotal_Object = MibTableColumn
friSStatsPktInTotal = _FriSStatsPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 7),
    _FriSStatsPktInTotal_Type()
)
friSStatsPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsPktInTotal.setStatus("mandatory")
_FriSStatsPktOutTotal_Type = Counter32
_FriSStatsPktOutTotal_Object = MibTableColumn
friSStatsPktOutTotal = _FriSStatsPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 8),
    _FriSStatsPktOutTotal_Type()
)
friSStatsPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsPktOutTotal.setStatus("mandatory")
_FriSStatsPktInPerSec_Type = Integer32
_FriSStatsPktInPerSec_Object = MibTableColumn
friSStatsPktInPerSec = _FriSStatsPktInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 9),
    _FriSStatsPktInPerSec_Type()
)
friSStatsPktInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsPktInPerSec.setStatus("mandatory")
_FriSStatsPktOutPerSec_Type = Integer32
_FriSStatsPktOutPerSec_Object = MibTableColumn
friSStatsPktOutPerSec = _FriSStatsPktOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 10),
    _FriSStatsPktOutPerSec_Type()
)
friSStatsPktOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsPktOutPerSec.setStatus("mandatory")
_FriSStatsFrameInTotal_Type = Counter32
_FriSStatsFrameInTotal_Object = MibTableColumn
friSStatsFrameInTotal = _FriSStatsFrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 11),
    _FriSStatsFrameInTotal_Type()
)
friSStatsFrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsFrameInTotal.setStatus("mandatory")
_FriSStatsFrameOutTotal_Type = Counter32
_FriSStatsFrameOutTotal_Object = MibTableColumn
friSStatsFrameOutTotal = _FriSStatsFrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 12),
    _FriSStatsFrameOutTotal_Type()
)
friSStatsFrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsFrameOutTotal.setStatus("mandatory")
_FriSStatsFrameInPerSec_Type = Integer32
_FriSStatsFrameInPerSec_Object = MibTableColumn
friSStatsFrameInPerSec = _FriSStatsFrameInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 13),
    _FriSStatsFrameInPerSec_Type()
)
friSStatsFrameInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsFrameInPerSec.setStatus("mandatory")
_FriSStatsFrameOutPerSec_Type = Integer32
_FriSStatsFrameOutPerSec_Object = MibTableColumn
friSStatsFrameOutPerSec = _FriSStatsFrameOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 14),
    _FriSStatsFrameOutPerSec_Type()
)
friSStatsFrameOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsFrameOutPerSec.setStatus("mandatory")
_FriSStatsUtilIn_Type = Integer32
_FriSStatsUtilIn_Object = MibTableColumn
friSStatsUtilIn = _FriSStatsUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 15),
    _FriSStatsUtilIn_Type()
)
friSStatsUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsUtilIn.setStatus("mandatory")
_FriSStatsUtilOut_Type = Integer32
_FriSStatsUtilOut_Object = MibTableColumn
friSStatsUtilOut = _FriSStatsUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 16),
    _FriSStatsUtilOut_Type()
)
friSStatsUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsUtilOut.setStatus("mandatory")
_FriSStatsNumPktsQueued_Type = Integer32
_FriSStatsNumPktsQueued_Object = MibTableColumn
friSStatsNumPktsQueued = _FriSStatsNumPktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 17),
    _FriSStatsNumPktsQueued_Type()
)
friSStatsNumPktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsNumPktsQueued.setStatus("mandatory")
_FriSStatsPktsDiscardIn_Type = Integer32
_FriSStatsPktsDiscardIn_Object = MibTableColumn
friSStatsPktsDiscardIn = _FriSStatsPktsDiscardIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 18),
    _FriSStatsPktsDiscardIn_Type()
)
friSStatsPktsDiscardIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsPktsDiscardIn.setStatus("mandatory")
_FriSStatsPktsDiscardOut_Type = Integer32
_FriSStatsPktsDiscardOut_Object = MibTableColumn
friSStatsPktsDiscardOut = _FriSStatsPktsDiscardOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 19),
    _FriSStatsPktsDiscardOut_Type()
)
friSStatsPktsDiscardOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsPktsDiscardOut.setStatus("mandatory")
_FriSStatsPktsQueuedIn_Type = Integer32
_FriSStatsPktsQueuedIn_Object = MibTableColumn
friSStatsPktsQueuedIn = _FriSStatsPktsQueuedIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 20),
    _FriSStatsPktsQueuedIn_Type()
)
friSStatsPktsQueuedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsPktsQueuedIn.setStatus("mandatory")
_FriSStatsPktsQueuedOut_Type = Integer32
_FriSStatsPktsQueuedOut_Object = MibTableColumn
friSStatsPktsQueuedOut = _FriSStatsPktsQueuedOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 2, 1, 21),
    _FriSStatsPktsQueuedOut_Type()
)
friSStatsPktsQueuedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsPktsQueuedOut.setStatus("mandatory")
_FriSVoiceSummaryStatsTable_Object = MibTable
friSVoiceSummaryStatsTable = _FriSVoiceSummaryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 3)
)
if mibBuilder.loadTexts:
    friSVoiceSummaryStatsTable.setStatus("mandatory")
_Cdx6500friSVoiceSummaryStatsEntry_Object = MibTableRow
cdx6500friSVoiceSummaryStatsEntry = _Cdx6500friSVoiceSummaryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 3, 1)
)
cdx6500friSVoiceSummaryStatsEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friSVoiceSummStatsPortNumber"),
    (0, "FRI-OPT-MIB", "friSVoiceSummStatsStnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500friSVoiceSummaryStatsEntry.setStatus("mandatory")


class _FriSVoiceSummStatsPortNumber_Type(Integer32):
    """Custom type friSVoiceSummStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriSVoiceSummStatsPortNumber_Type.__name__ = "Integer32"
_FriSVoiceSummStatsPortNumber_Object = MibTableColumn
friSVoiceSummStatsPortNumber = _FriSVoiceSummStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 3, 1, 1),
    _FriSVoiceSummStatsPortNumber_Type()
)
friSVoiceSummStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSVoiceSummStatsPortNumber.setStatus("mandatory")


class _FriSVoiceSummStatsStnNumber_Type(Integer32):
    """Custom type friSVoiceSummStatsStnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FriSVoiceSummStatsStnNumber_Type.__name__ = "Integer32"
_FriSVoiceSummStatsStnNumber_Object = MibTableColumn
friSVoiceSummStatsStnNumber = _FriSVoiceSummStatsStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 3, 1, 2),
    _FriSVoiceSummStatsStnNumber_Type()
)
friSVoiceSummStatsStnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSVoiceSummStatsStnNumber.setStatus("mandatory")
_FriSStatsVoiceCharInTotal_Type = Counter32
_FriSStatsVoiceCharInTotal_Object = MibTableColumn
friSStatsVoiceCharInTotal = _FriSStatsVoiceCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 3, 1, 3),
    _FriSStatsVoiceCharInTotal_Type()
)
friSStatsVoiceCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsVoiceCharInTotal.setStatus("mandatory")
_FriSStatsVoiceCharOutTotal_Type = Counter32
_FriSStatsVoiceCharOutTotal_Object = MibTableColumn
friSStatsVoiceCharOutTotal = _FriSStatsVoiceCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 3, 1, 4),
    _FriSStatsVoiceCharOutTotal_Type()
)
friSStatsVoiceCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsVoiceCharOutTotal.setStatus("mandatory")
_FriSStatsVoiceCharInPerSec_Type = Integer32
_FriSStatsVoiceCharInPerSec_Object = MibTableColumn
friSStatsVoiceCharInPerSec = _FriSStatsVoiceCharInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 3, 1, 5),
    _FriSStatsVoiceCharInPerSec_Type()
)
friSStatsVoiceCharInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsVoiceCharInPerSec.setStatus("mandatory")
_FriSStatsVoiceCharOutPerSec_Type = Integer32
_FriSStatsVoiceCharOutPerSec_Object = MibTableColumn
friSStatsVoiceCharOutPerSec = _FriSStatsVoiceCharOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 3, 1, 6),
    _FriSStatsVoiceCharOutPerSec_Type()
)
friSStatsVoiceCharOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsVoiceCharOutPerSec.setStatus("mandatory")
_FriSStatsVoicePktInTotal_Type = Counter32
_FriSStatsVoicePktInTotal_Object = MibTableColumn
friSStatsVoicePktInTotal = _FriSStatsVoicePktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 3, 1, 7),
    _FriSStatsVoicePktInTotal_Type()
)
friSStatsVoicePktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsVoicePktInTotal.setStatus("mandatory")
_FriSStatsVoicePktOutTotal_Type = Counter32
_FriSStatsVoicePktOutTotal_Object = MibTableColumn
friSStatsVoicePktOutTotal = _FriSStatsVoicePktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 3, 1, 8),
    _FriSStatsVoicePktOutTotal_Type()
)
friSStatsVoicePktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsVoicePktOutTotal.setStatus("mandatory")
_FriSStatsVoicePktInPerSec_Type = Integer32
_FriSStatsVoicePktInPerSec_Object = MibTableColumn
friSStatsVoicePktInPerSec = _FriSStatsVoicePktInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 3, 1, 9),
    _FriSStatsVoicePktInPerSec_Type()
)
friSStatsVoicePktInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsVoicePktInPerSec.setStatus("mandatory")
_FriSStatsVoicePktOutPerSec_Type = Integer32
_FriSStatsVoicePktOutPerSec_Object = MibTableColumn
friSStatsVoicePktOutPerSec = _FriSStatsVoicePktOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 3, 1, 10),
    _FriSStatsVoicePktOutPerSec_Type()
)
friSStatsVoicePktOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsVoicePktOutPerSec.setStatus("mandatory")
_FriSFrameSummaryStatsTable_Object = MibTable
friSFrameSummaryStatsTable = _FriSFrameSummaryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4)
)
if mibBuilder.loadTexts:
    friSFrameSummaryStatsTable.setStatus("mandatory")
_Cdx6500friSFrameSummaryStatsEntry_Object = MibTableRow
cdx6500friSFrameSummaryStatsEntry = _Cdx6500friSFrameSummaryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1)
)
cdx6500friSFrameSummaryStatsEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friSFrameSummStatsPortNumber"),
    (0, "FRI-OPT-MIB", "friSFrameSummStatsStnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500friSFrameSummaryStatsEntry.setStatus("mandatory")


class _FriSFrameSummStatsPortNumber_Type(Integer32):
    """Custom type friSFrameSummStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriSFrameSummStatsPortNumber_Type.__name__ = "Integer32"
_FriSFrameSummStatsPortNumber_Object = MibTableColumn
friSFrameSummStatsPortNumber = _FriSFrameSummStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 1),
    _FriSFrameSummStatsPortNumber_Type()
)
friSFrameSummStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSFrameSummStatsPortNumber.setStatus("mandatory")


class _FriSFrameSummStatsStnNumber_Type(Integer32):
    """Custom type friSFrameSummStatsStnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FriSFrameSummStatsStnNumber_Type.__name__ = "Integer32"
_FriSFrameSummStatsStnNumber_Object = MibTableColumn
friSFrameSummStatsStnNumber = _FriSFrameSummStatsStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 2),
    _FriSFrameSummStatsStnNumber_Type()
)
friSFrameSummStatsStnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSFrameSummStatsStnNumber.setStatus("mandatory")
_FriSStatsInfoFramesInTotal_Type = Counter32
_FriSStatsInfoFramesInTotal_Object = MibTableColumn
friSStatsInfoFramesInTotal = _FriSStatsInfoFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 3),
    _FriSStatsInfoFramesInTotal_Type()
)
friSStatsInfoFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsInfoFramesInTotal.setStatus("mandatory")
_FriSStatsInfoFramesOutTotal_Type = Counter32
_FriSStatsInfoFramesOutTotal_Object = MibTableColumn
friSStatsInfoFramesOutTotal = _FriSStatsInfoFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 4),
    _FriSStatsInfoFramesOutTotal_Type()
)
friSStatsInfoFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsInfoFramesOutTotal.setStatus("mandatory")
_FriSStatsRRFramesInTotal_Type = Counter32
_FriSStatsRRFramesInTotal_Object = MibTableColumn
friSStatsRRFramesInTotal = _FriSStatsRRFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 5),
    _FriSStatsRRFramesInTotal_Type()
)
friSStatsRRFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsRRFramesInTotal.setStatus("mandatory")
_FriSStatsRRFramesOutTotal_Type = Counter32
_FriSStatsRRFramesOutTotal_Object = MibTableColumn
friSStatsRRFramesOutTotal = _FriSStatsRRFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 6),
    _FriSStatsRRFramesOutTotal_Type()
)
friSStatsRRFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsRRFramesOutTotal.setStatus("mandatory")
_FriSStatsRNRFramesInTotal_Type = Counter32
_FriSStatsRNRFramesInTotal_Object = MibTableColumn
friSStatsRNRFramesInTotal = _FriSStatsRNRFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 7),
    _FriSStatsRNRFramesInTotal_Type()
)
friSStatsRNRFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsRNRFramesInTotal.setStatus("mandatory")
_FriSStatsRNRFramesOutTotal_Type = Counter32
_FriSStatsRNRFramesOutTotal_Object = MibTableColumn
friSStatsRNRFramesOutTotal = _FriSStatsRNRFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 8),
    _FriSStatsRNRFramesOutTotal_Type()
)
friSStatsRNRFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsRNRFramesOutTotal.setStatus("mandatory")
_FriSStatsREJFramesInTotal_Type = Counter32
_FriSStatsREJFramesInTotal_Object = MibTableColumn
friSStatsREJFramesInTotal = _FriSStatsREJFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 9),
    _FriSStatsREJFramesInTotal_Type()
)
friSStatsREJFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsREJFramesInTotal.setStatus("mandatory")
_FriSStatsREJFramesOutTotal_Type = Counter32
_FriSStatsREJFramesOutTotal_Object = MibTableColumn
friSStatsREJFramesOutTotal = _FriSStatsREJFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 10),
    _FriSStatsREJFramesOutTotal_Type()
)
friSStatsREJFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsREJFramesOutTotal.setStatus("mandatory")
_FriSStatsSABMFramesInTotal_Type = Counter32
_FriSStatsSABMFramesInTotal_Object = MibTableColumn
friSStatsSABMFramesInTotal = _FriSStatsSABMFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 11),
    _FriSStatsSABMFramesInTotal_Type()
)
friSStatsSABMFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsSABMFramesInTotal.setStatus("mandatory")
_FriSStatsSABMFramesOutTotal_Type = Counter32
_FriSStatsSABMFramesOutTotal_Object = MibTableColumn
friSStatsSABMFramesOutTotal = _FriSStatsSABMFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 12),
    _FriSStatsSABMFramesOutTotal_Type()
)
friSStatsSABMFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsSABMFramesOutTotal.setStatus("mandatory")
_FriSStatsDISCFramesInTotal_Type = Counter32
_FriSStatsDISCFramesInTotal_Object = MibTableColumn
friSStatsDISCFramesInTotal = _FriSStatsDISCFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 13),
    _FriSStatsDISCFramesInTotal_Type()
)
friSStatsDISCFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsDISCFramesInTotal.setStatus("mandatory")
_FriSStatsDISCFramesOutTotal_Type = Counter32
_FriSStatsDISCFramesOutTotal_Object = MibTableColumn
friSStatsDISCFramesOutTotal = _FriSStatsDISCFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 14),
    _FriSStatsDISCFramesOutTotal_Type()
)
friSStatsDISCFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsDISCFramesOutTotal.setStatus("mandatory")
_FriSStatsDMFramesInTotal_Type = Counter32
_FriSStatsDMFramesInTotal_Object = MibTableColumn
friSStatsDMFramesInTotal = _FriSStatsDMFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 15),
    _FriSStatsDMFramesInTotal_Type()
)
friSStatsDMFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsDMFramesInTotal.setStatus("mandatory")
_FriSStatsDMFramesOutTotal_Type = Counter32
_FriSStatsDMFramesOutTotal_Object = MibTableColumn
friSStatsDMFramesOutTotal = _FriSStatsDMFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 16),
    _FriSStatsDMFramesOutTotal_Type()
)
friSStatsDMFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsDMFramesOutTotal.setStatus("mandatory")
_FriSStatsUAFramesInTotal_Type = Counter32
_FriSStatsUAFramesInTotal_Object = MibTableColumn
friSStatsUAFramesInTotal = _FriSStatsUAFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 17),
    _FriSStatsUAFramesInTotal_Type()
)
friSStatsUAFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsUAFramesInTotal.setStatus("mandatory")
_FriSStatsUAFramesOutTotal_Type = Counter32
_FriSStatsUAFramesOutTotal_Object = MibTableColumn
friSStatsUAFramesOutTotal = _FriSStatsUAFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 18),
    _FriSStatsUAFramesOutTotal_Type()
)
friSStatsUAFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsUAFramesOutTotal.setStatus("mandatory")
_FriSStatsFRMRFramesInTotal_Type = Counter32
_FriSStatsFRMRFramesInTotal_Object = MibTableColumn
friSStatsFRMRFramesInTotal = _FriSStatsFRMRFramesInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 19),
    _FriSStatsFRMRFramesInTotal_Type()
)
friSStatsFRMRFramesInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsFRMRFramesInTotal.setStatus("mandatory")
_FriSStatsFRMRFramesOutTotal_Type = Counter32
_FriSStatsFRMRFramesOutTotal_Object = MibTableColumn
friSStatsFRMRFramesOutTotal = _FriSStatsFRMRFramesOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 4, 1, 20),
    _FriSStatsFRMRFramesOutTotal_Type()
)
friSStatsFRMRFramesOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsFRMRFramesOutTotal.setStatus("mandatory")
_FriSPacketSummaryStatsTable_Object = MibTable
friSPacketSummaryStatsTable = _FriSPacketSummaryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5)
)
if mibBuilder.loadTexts:
    friSPacketSummaryStatsTable.setStatus("mandatory")
_Cdx6500friSPacketSummaryStatsEntry_Object = MibTableRow
cdx6500friSPacketSummaryStatsEntry = _Cdx6500friSPacketSummaryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1)
)
cdx6500friSPacketSummaryStatsEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friSPktSummStatsPortNumber"),
    (0, "FRI-OPT-MIB", "friSPktSummStatsStnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500friSPacketSummaryStatsEntry.setStatus("mandatory")


class _FriSPktSummStatsPortNumber_Type(Integer32):
    """Custom type friSPktSummStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriSPktSummStatsPortNumber_Type.__name__ = "Integer32"
_FriSPktSummStatsPortNumber_Object = MibTableColumn
friSPktSummStatsPortNumber = _FriSPktSummStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 1),
    _FriSPktSummStatsPortNumber_Type()
)
friSPktSummStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSPktSummStatsPortNumber.setStatus("mandatory")


class _FriSPktSummStatsStnNumber_Type(Integer32):
    """Custom type friSPktSummStatsStnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FriSPktSummStatsStnNumber_Type.__name__ = "Integer32"
_FriSPktSummStatsStnNumber_Object = MibTableColumn
friSPktSummStatsStnNumber = _FriSPktSummStatsStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 2),
    _FriSPktSummStatsStnNumber_Type()
)
friSPktSummStatsStnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSPktSummStatsStnNumber.setStatus("mandatory")
_FriSStatsDataPktInTotal_Type = Counter32
_FriSStatsDataPktInTotal_Object = MibTableColumn
friSStatsDataPktInTotal = _FriSStatsDataPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 3),
    _FriSStatsDataPktInTotal_Type()
)
friSStatsDataPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsDataPktInTotal.setStatus("mandatory")
_FriSStatsDataPktOutTotal_Type = Counter32
_FriSStatsDataPktOutTotal_Object = MibTableColumn
friSStatsDataPktOutTotal = _FriSStatsDataPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 4),
    _FriSStatsDataPktOutTotal_Type()
)
friSStatsDataPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsDataPktOutTotal.setStatus("mandatory")
_FriSStatsRRPktInTotal_Type = Counter32
_FriSStatsRRPktInTotal_Object = MibTableColumn
friSStatsRRPktInTotal = _FriSStatsRRPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 5),
    _FriSStatsRRPktInTotal_Type()
)
friSStatsRRPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsRRPktInTotal.setStatus("mandatory")
_FriSStatsRRPktOutTotal_Type = Counter32
_FriSStatsRRPktOutTotal_Object = MibTableColumn
friSStatsRRPktOutTotal = _FriSStatsRRPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 6),
    _FriSStatsRRPktOutTotal_Type()
)
friSStatsRRPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsRRPktOutTotal.setStatus("mandatory")
_FriSStatsRNRPktInTotal_Type = Counter32
_FriSStatsRNRPktInTotal_Object = MibTableColumn
friSStatsRNRPktInTotal = _FriSStatsRNRPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 7),
    _FriSStatsRNRPktInTotal_Type()
)
friSStatsRNRPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsRNRPktInTotal.setStatus("mandatory")
_FriSStatsRNRPktOutTotal_Type = Counter32
_FriSStatsRNRPktOutTotal_Object = MibTableColumn
friSStatsRNRPktOutTotal = _FriSStatsRNRPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 8),
    _FriSStatsRNRPktOutTotal_Type()
)
friSStatsRNRPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsRNRPktOutTotal.setStatus("mandatory")
_FriSStatsREJPktInTotal_Type = Counter32
_FriSStatsREJPktInTotal_Object = MibTableColumn
friSStatsREJPktInTotal = _FriSStatsREJPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 9),
    _FriSStatsREJPktInTotal_Type()
)
friSStatsREJPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsREJPktInTotal.setStatus("mandatory")
_FriSStatsREJPktOutTotal_Type = Counter32
_FriSStatsREJPktOutTotal_Object = MibTableColumn
friSStatsREJPktOutTotal = _FriSStatsREJPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 10),
    _FriSStatsREJPktOutTotal_Type()
)
friSStatsREJPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsREJPktOutTotal.setStatus("mandatory")
_FriSStatsCallReqPktInTotal_Type = Counter32
_FriSStatsCallReqPktInTotal_Object = MibTableColumn
friSStatsCallReqPktInTotal = _FriSStatsCallReqPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 11),
    _FriSStatsCallReqPktInTotal_Type()
)
friSStatsCallReqPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsCallReqPktInTotal.setStatus("mandatory")
_FriSStatsCallReqPktOutTotal_Type = Counter32
_FriSStatsCallReqPktOutTotal_Object = MibTableColumn
friSStatsCallReqPktOutTotal = _FriSStatsCallReqPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 12),
    _FriSStatsCallReqPktOutTotal_Type()
)
friSStatsCallReqPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsCallReqPktOutTotal.setStatus("mandatory")
_FriSStatsCallAccPktInTotal_Type = Counter32
_FriSStatsCallAccPktInTotal_Object = MibTableColumn
friSStatsCallAccPktInTotal = _FriSStatsCallAccPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 13),
    _FriSStatsCallAccPktInTotal_Type()
)
friSStatsCallAccPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsCallAccPktInTotal.setStatus("mandatory")
_FriSStatsCallAccPktOutTotal_Type = Counter32
_FriSStatsCallAccPktOutTotal_Object = MibTableColumn
friSStatsCallAccPktOutTotal = _FriSStatsCallAccPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 14),
    _FriSStatsCallAccPktOutTotal_Type()
)
friSStatsCallAccPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsCallAccPktOutTotal.setStatus("mandatory")
_FriSStatsClrReqPktInTotal_Type = Counter32
_FriSStatsClrReqPktInTotal_Object = MibTableColumn
friSStatsClrReqPktInTotal = _FriSStatsClrReqPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 15),
    _FriSStatsClrReqPktInTotal_Type()
)
friSStatsClrReqPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsClrReqPktInTotal.setStatus("mandatory")
_FriSStatsClrReqPktOutTotal_Type = Counter32
_FriSStatsClrReqPktOutTotal_Object = MibTableColumn
friSStatsClrReqPktOutTotal = _FriSStatsClrReqPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 16),
    _FriSStatsClrReqPktOutTotal_Type()
)
friSStatsClrReqPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsClrReqPktOutTotal.setStatus("mandatory")
_FriSStatsClrConfPktInTotal_Type = Counter32
_FriSStatsClrConfPktInTotal_Object = MibTableColumn
friSStatsClrConfPktInTotal = _FriSStatsClrConfPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 17),
    _FriSStatsClrConfPktInTotal_Type()
)
friSStatsClrConfPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsClrConfPktInTotal.setStatus("mandatory")
_FriSStatsClrConfPktOutTotal_Type = Counter32
_FriSStatsClrConfPktOutTotal_Object = MibTableColumn
friSStatsClrConfPktOutTotal = _FriSStatsClrConfPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 18),
    _FriSStatsClrConfPktOutTotal_Type()
)
friSStatsClrConfPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsClrConfPktOutTotal.setStatus("mandatory")
_FriSStatsIntrReqPktInTotal_Type = Counter32
_FriSStatsIntrReqPktInTotal_Object = MibTableColumn
friSStatsIntrReqPktInTotal = _FriSStatsIntrReqPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 19),
    _FriSStatsIntrReqPktInTotal_Type()
)
friSStatsIntrReqPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsIntrReqPktInTotal.setStatus("mandatory")
_FriSStatsIntrReqPktOutTotal_Type = Counter32
_FriSStatsIntrReqPktOutTotal_Object = MibTableColumn
friSStatsIntrReqPktOutTotal = _FriSStatsIntrReqPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 20),
    _FriSStatsIntrReqPktOutTotal_Type()
)
friSStatsIntrReqPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsIntrReqPktOutTotal.setStatus("mandatory")
_FriSStatsIntrConfPktInTotal_Type = Counter32
_FriSStatsIntrConfPktInTotal_Object = MibTableColumn
friSStatsIntrConfPktInTotal = _FriSStatsIntrConfPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 21),
    _FriSStatsIntrConfPktInTotal_Type()
)
friSStatsIntrConfPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsIntrConfPktInTotal.setStatus("mandatory")
_FriSStatsIntrConfPktOutTotal_Type = Counter32
_FriSStatsIntrConfPktOutTotal_Object = MibTableColumn
friSStatsIntrConfPktOutTotal = _FriSStatsIntrConfPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 22),
    _FriSStatsIntrConfPktOutTotal_Type()
)
friSStatsIntrConfPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsIntrConfPktOutTotal.setStatus("mandatory")
_FriSStatsResetReqPktInTotal_Type = Counter32
_FriSStatsResetReqPktInTotal_Object = MibTableColumn
friSStatsResetReqPktInTotal = _FriSStatsResetReqPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 23),
    _FriSStatsResetReqPktInTotal_Type()
)
friSStatsResetReqPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsResetReqPktInTotal.setStatus("mandatory")
_FriSStatsResetReqPktOutTotal_Type = Counter32
_FriSStatsResetReqPktOutTotal_Object = MibTableColumn
friSStatsResetReqPktOutTotal = _FriSStatsResetReqPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 24),
    _FriSStatsResetReqPktOutTotal_Type()
)
friSStatsResetReqPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsResetReqPktOutTotal.setStatus("mandatory")
_FriSStatsResetConfPktInTotal_Type = Counter32
_FriSStatsResetConfPktInTotal_Object = MibTableColumn
friSStatsResetConfPktInTotal = _FriSStatsResetConfPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 25),
    _FriSStatsResetConfPktInTotal_Type()
)
friSStatsResetConfPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsResetConfPktInTotal.setStatus("mandatory")
_FriSStatsResetConfPktOutTotal_Type = Counter32
_FriSStatsResetConfPktOutTotal_Object = MibTableColumn
friSStatsResetConfPktOutTotal = _FriSStatsResetConfPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 26),
    _FriSStatsResetConfPktOutTotal_Type()
)
friSStatsResetConfPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsResetConfPktOutTotal.setStatus("mandatory")
_FriSStatsRestartReqPktInTotal_Type = Counter32
_FriSStatsRestartReqPktInTotal_Object = MibTableColumn
friSStatsRestartReqPktInTotal = _FriSStatsRestartReqPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 27),
    _FriSStatsRestartReqPktInTotal_Type()
)
friSStatsRestartReqPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsRestartReqPktInTotal.setStatus("mandatory")
_FriSStatsRestartReqPktOutTotal_Type = Counter32
_FriSStatsRestartReqPktOutTotal_Object = MibTableColumn
friSStatsRestartReqPktOutTotal = _FriSStatsRestartReqPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 28),
    _FriSStatsRestartReqPktOutTotal_Type()
)
friSStatsRestartReqPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsRestartReqPktOutTotal.setStatus("mandatory")
_FriSStatsRestartConfPktInTotal_Type = Counter32
_FriSStatsRestartConfPktInTotal_Object = MibTableColumn
friSStatsRestartConfPktInTotal = _FriSStatsRestartConfPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 29),
    _FriSStatsRestartConfPktInTotal_Type()
)
friSStatsRestartConfPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsRestartConfPktInTotal.setStatus("mandatory")
_FriSStatsRestartConfPktOutTotal_Type = Counter32
_FriSStatsRestartConfPktOutTotal_Object = MibTableColumn
friSStatsRestartConfPktOutTotal = _FriSStatsRestartConfPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 5, 1, 30),
    _FriSStatsRestartConfPktOutTotal_Type()
)
friSStatsRestartConfPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsRestartConfPktOutTotal.setStatus("mandatory")
_FriSFRISummaryStatsTable_Object = MibTable
friSFRISummaryStatsTable = _FriSFRISummaryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 6)
)
if mibBuilder.loadTexts:
    friSFRISummaryStatsTable.setStatus("mandatory")
_Cdx6500friSFRISummaryStatsEntry_Object = MibTableRow
cdx6500friSFRISummaryStatsEntry = _Cdx6500friSFRISummaryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 6, 1)
)
cdx6500friSFRISummaryStatsEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friSFRISummStatsPortNumber"),
    (0, "FRI-OPT-MIB", "friSFRISummStatsStnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500friSFRISummaryStatsEntry.setStatus("mandatory")


class _FriSFRISummStatsPortNumber_Type(Integer32):
    """Custom type friSFRISummStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriSFRISummStatsPortNumber_Type.__name__ = "Integer32"
_FriSFRISummStatsPortNumber_Object = MibTableColumn
friSFRISummStatsPortNumber = _FriSFRISummStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 6, 1, 1),
    _FriSFRISummStatsPortNumber_Type()
)
friSFRISummStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSFRISummStatsPortNumber.setStatus("mandatory")


class _FriSFRISummStatsStnNumber_Type(Integer32):
    """Custom type friSFRISummStatsStnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FriSFRISummStatsStnNumber_Type.__name__ = "Integer32"
_FriSFRISummStatsStnNumber_Object = MibTableColumn
friSFRISummStatsStnNumber = _FriSFRISummStatsStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 6, 1, 2),
    _FriSFRISummStatsStnNumber_Type()
)
friSFRISummStatsStnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSFRISummStatsStnNumber.setStatus("mandatory")
_FriSStatsFECNInTotal_Type = Counter32
_FriSStatsFECNInTotal_Object = MibTableColumn
friSStatsFECNInTotal = _FriSStatsFECNInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 6, 1, 3),
    _FriSStatsFECNInTotal_Type()
)
friSStatsFECNInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsFECNInTotal.setStatus("mandatory")
_FriSStatsFECNOutTotal_Type = Counter32
_FriSStatsFECNOutTotal_Object = MibTableColumn
friSStatsFECNOutTotal = _FriSStatsFECNOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 6, 1, 4),
    _FriSStatsFECNOutTotal_Type()
)
friSStatsFECNOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsFECNOutTotal.setStatus("mandatory")
_FriSStatsBECNInTotal_Type = Counter32
_FriSStatsBECNInTotal_Object = MibTableColumn
friSStatsBECNInTotal = _FriSStatsBECNInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 6, 1, 5),
    _FriSStatsBECNInTotal_Type()
)
friSStatsBECNInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsBECNInTotal.setStatus("mandatory")
_FriSStatsBECNOutTotal_Type = Counter32
_FriSStatsBECNOutTotal_Object = MibTableColumn
friSStatsBECNOutTotal = _FriSStatsBECNOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 6, 1, 6),
    _FriSStatsBECNOutTotal_Type()
)
friSStatsBECNOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsBECNOutTotal.setStatus("mandatory")
_FriSStatsDEInTotal_Type = Counter32
_FriSStatsDEInTotal_Object = MibTableColumn
friSStatsDEInTotal = _FriSStatsDEInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 6, 1, 7),
    _FriSStatsDEInTotal_Type()
)
friSStatsDEInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsDEInTotal.setStatus("mandatory")
_FriSStatsDEOutTotal_Type = Counter32
_FriSStatsDEOutTotal_Object = MibTableColumn
friSStatsDEOutTotal = _FriSStatsDEOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 10, 6, 1, 8),
    _FriSStatsDEOutTotal_Type()
)
friSStatsDEOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friSStatsDEOutTotal.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContFRITable_ObjectIdentity = ObjectIdentity
cdx6500ContFRITable = _Cdx6500ContFRITable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 14)
)
_Cdx6500FRIPContTable_Object = MibTable
cdx6500FRIPContTable = _Cdx6500FRIPContTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 14, 1)
)
if mibBuilder.loadTexts:
    cdx6500FRIPContTable.setStatus("mandatory")
_Cdx6500FRIPContEntry_Object = MibTableRow
cdx6500FRIPContEntry = _Cdx6500FRIPContEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 14, 1, 1)
)
cdx6500FRIPContEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friPContPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500FRIPContEntry.setStatus("mandatory")


class _FriPContPortNumber_Type(Integer32):
    """Custom type friPContPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriPContPortNumber_Type.__name__ = "Integer32"
_FriPContPortNumber_Object = MibTableColumn
friPContPortNumber = _FriPContPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 14, 1, 1, 1),
    _FriPContPortNumber_Type()
)
friPContPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friPContPortNumber.setStatus("mandatory")


class _FriPContPortControl_Type(Integer32):
    """Custom type friPContPortControl based on Integer32"""
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
        *(("boot", 1),
          ("disable", 3),
          ("enable", 2),
          ("resetstats", 4))
    )


_FriPContPortControl_Type.__name__ = "Integer32"
_FriPContPortControl_Object = MibTableColumn
friPContPortControl = _FriPContPortControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 14, 1, 1, 2),
    _FriPContPortControl_Type()
)
friPContPortControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    friPContPortControl.setStatus("mandatory")
_Cdx6500FRISContTable_Object = MibTable
cdx6500FRISContTable = _Cdx6500FRISContTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 14, 2)
)
if mibBuilder.loadTexts:
    cdx6500FRISContTable.setStatus("mandatory")
_Cdx6500FRISContEntry_Object = MibTableRow
cdx6500FRISContEntry = _Cdx6500FRISContEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 14, 2, 1)
)
cdx6500FRISContEntry.setIndexNames(
    (0, "FRI-OPT-MIB", "friSContPortNumber"),
    (0, "FRI-OPT-MIB", "friSContStnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500FRISContEntry.setStatus("mandatory")


class _FriSContPortNumber_Type(Integer32):
    """Custom type friSContPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FriSContPortNumber_Type.__name__ = "Integer32"
_FriSContPortNumber_Object = MibTableColumn
friSContPortNumber = _FriSContPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 14, 2, 1, 1),
    _FriSContPortNumber_Type()
)
friSContPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friSContPortNumber.setStatus("mandatory")


class _FriSContStnNumber_Type(Integer32):
    """Custom type friSContStnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FriSContStnNumber_Type.__name__ = "Integer32"
_FriSContStnNumber_Object = MibTableColumn
friSContStnNumber = _FriSContStnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 14, 2, 1, 2),
    _FriSContStnNumber_Type()
)
friSContStnNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    friSContStnNumber.setStatus("mandatory")


class _FriSContStnControl_Type(Integer32):
    """Custom type friSContStnControl based on Integer32"""
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
        *(("boot", 1),
          ("disable", 3),
          ("enable", 2),
          ("resetstats", 4))
    )


_FriSContStnControl_Type.__name__ = "Integer32"
_FriSContStnControl_Object = MibTableColumn
friSContStnControl = _FriSContStnControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 14, 2, 1, 3),
    _FriSContStnControl_Type()
)
friSContStnControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    friSContStnControl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FRI-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTFRIPortTable": cdx6500PPCTFRIPortTable,
       "cdx6500PPCTFRIPortEntry": cdx6500PPCTFRIPortEntry,
       "friPCfgPortNumber": friPCfgPortNumber,
       "friPCfgPortType": friPCfgPortType,
       "friPCfgConnectionType": friPCfgConnectionType,
       "friPCfgClockSource": friPCfgClockSource,
       "friPCfgClockSpeed": friPCfgClockSpeed,
       "friPCfgHighestStnNumber": friPCfgHighestStnNumber,
       "friPCfgFrameSeqCounting": friPCfgFrameSeqCounting,
       "friPCfgPktSeqCounting": friPCfgPktSeqCounting,
       "friPCfgCntrlProtocolSupport": friPCfgCntrlProtocolSupport,
       "friPCfgHighPriorityStn": friPCfgHighPriorityStn,
       "friPCfgMaxVoiceBWBitsPerSec": friPCfgMaxVoiceBWBitsPerSec,
       "friPCfgSegSizeVoicePresent": friPCfgSegSizeVoicePresent,
       "friPCfgSegSizeVoiceNotPresent": friPCfgSegSizeVoiceNotPresent,
       "friPCfgT391Timer": friPCfgT391Timer,
       "friPCfgT392Timer": friPCfgT392Timer,
       "friPCfgN391PollCycle": friPCfgN391PollCycle,
       "friPCfgN392ErrsDuringMonitoredEvents": friPCfgN392ErrsDuringMonitoredEvents,
       "friPCfgN393MonitoredEvents": friPCfgN393MonitoredEvents,
       "friPCfgNT1PollTimer": friPCfgNT1PollTimer,
       "friPCfgNT2VerificationTimer": friPCfgNT2VerificationTimer,
       "friPCfgNN1StatusPollingCycle": friPCfgNN1StatusPollingCycle,
       "friPCfgNN2ErrsDuringMonitoredEvents": friPCfgNN2ErrsDuringMonitoredEvents,
       "friPCfgNN3MonitoredEvents": friPCfgNN3MonitoredEvents,
       "friPCfgInvertTXClock": friPCfgInvertTXClock,
       "friPCfgControlProtocolOptions": friPCfgControlProtocolOptions,
       "friPCfgDiscardControlOptions": friPCfgDiscardControlOptions,
       "friPCfgStartSvcDlci": friPCfgStartSvcDlci,
       "friPCfgSubscriberNumber": friPCfgSubscriberNumber,
       "friPCfgMaxFmif": friPCfgMaxFmif,
       "friPCfgT200": friPCfgT200,
       "friPCfgN200": friPCfgN200,
       "friPCfgWindowK": friPCfgWindowK,
       "friPCfgT203": friPCfgT203,
       "friPCfgT303": friPCfgT303,
       "friPCfgT305": friPCfgT305,
       "friPCfgT308": friPCfgT308,
       "friPCfgT310": friPCfgT310,
       "friPCfgControlProtocol": friPCfgControlProtocol,
       "friPCfguniState": friPCfguniState,
       "friPCfguniSSVP": friPCfguniSSVP,
       "friPCfguniSSVNP": friPCfguniSSVNP,
       "friPCfguniSegDelay": friPCfguniSegDelay,
       "friPCfguniCheckPckSize": friPCfguniCheckPckSize,
       "friPCfgElectricalInterfaceType": friPCfgElectricalInterfaceType,
       "friPCfgV24ElectricalInterfaceOption": friPCfgV24ElectricalInterfaceOption,
       "friPCfgHighSpeedElectricalInterfaceOption": friPCfgHighSpeedElectricalInterfaceOption,
       "cdx6500PCTStationProtocolGroup": cdx6500PCTStationProtocolGroup,
       "cdx6500SPCTFRIStationTable": cdx6500SPCTFRIStationTable,
       "cdx6500SPCTFRIStationEntry": cdx6500SPCTFRIStationEntry,
       "friSCfgPortNumber": friSCfgPortNumber,
       "friSCfgStnNumber": friSCfgStnNumber,
       "friSCfgStnType": friSCfgStnType,
       "friSCfgDLCI": friSCfgDLCI,
       "friSCfgCommInfoRate": friSCfgCommInfoRate,
       "friSCfgCommBurstSize": friSCfgCommBurstSize,
       "friSCfgTransDelay": friSCfgTransDelay,
       "friSCfgCongControlMode": friSCfgCongControlMode,
       "friSCfgLinkAddress": friSCfgLinkAddress,
       "friSCfgPVCChannels": friSCfgPVCChannels,
       "friSCfgStartingPVC": friSCfgStartingPVC,
       "friSCfgSVCChannels": friSCfgSVCChannels,
       "friSCfgStartingSVC": friSCfgStartingSVC,
       "friSCfgVoiceSVCChannels": friSCfgVoiceSVCChannels,
       "friSCfgInitialFrame": friSCfgInitialFrame,
       "friSCfgT1RetryTimer": friSCfgT1RetryTimer,
       "friSCfgT4PollTimer": friSCfgT4PollTimer,
       "friSCfgN2TransmissionTries": friSCfgN2TransmissionTries,
       "friSCfgKFrameWindow": friSCfgKFrameWindow,
       "friSCfgWPacketWindow": friSCfgWPacketWindow,
       "friSCfgPPacketSize": friSCfgPPacketSize,
       "friSCfgDataQUpperThreshold": friSCfgDataQUpperThreshold,
       "friSCfgDataQLowerThreshold": friSCfgDataQLowerThreshold,
       "friSCfgRestartTimer": friSCfgRestartTimer,
       "friSCfgResetTimer": friSCfgResetTimer,
       "friSCfgCallTimer": friSCfgCallTimer,
       "friSCfgClearTimer": friSCfgClearTimer,
       "friSCfgX25Options": friSCfgX25Options,
       "friSCfgRestrictedConnDest": friSCfgRestrictedConnDest,
       "friSCfgCUGMembership": friSCfgCUGMembership,
       "friSCfgBillingRecords": friSCfgBillingRecords,
       "friSCfgFrameSegmenter": friSCfgFrameSegmenter,
       "friSCfgVoiceCongCtrlMode": friSCfgVoiceCongCtrlMode,
       "friSCfgPeakUtilization": friSCfgPeakUtilization,
       "friSCfgMaxInboundQueue": friSCfgMaxInboundQueue,
       "friSCfgAnnexGRateReduction": friSCfgAnnexGRateReduction,
       "friSCfgCctType": friSCfgCctType,
       "friSCfgCallControl": friSCfgCallControl,
       "friSCfgRetryInterval": friSCfgRetryInterval,
       "friSCfgCallAttempts": friSCfgCallAttempts,
       "friSCfgIdleInterval": friSCfgIdleInterval,
       "friSCfgIeNegotiation": friSCfgIeNegotiation,
       "friSCfgSubaddress": friSCfgSubaddress,
       "friSCfgCalledNumber": friSCfgCalledNumber,
       "friSCfgCalledSubaddress": friSCfgCalledSubaddress,
       "friSCfgMinCir": friSCfgMinCir,
       "friSCfgBurstExcess": friSCfgBurstExcess,
       "friSCfgE2EEnabled": friSCfgE2EEnabled,
       "friSCfgE2EType": friSCfgE2EType,
       "friSCfgE2ESSVP": friSCfgE2ESSVP,
       "friSCfgE2ESSVNP": friSCfgE2ESSVNP,
       "friSCfgE2ESegDelayEnabled": friSCfgE2ESegDelayEnabled,
       "friSCfgE2ECheckPckSize": friSCfgE2ECheckPckSize,
       "friSCfgvoice-header": friSCfgvoice_header,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTFRIPStatsTable": cdx6500PPSTFRIPStatsTable,
       "cdx6500PPSTFRIPortTable": cdx6500PPSTFRIPortTable,
       "cdx6500PPSTFRIPortEntry": cdx6500PPSTFRIPortEntry,
       "friPStatsPortNumber": friPStatsPortNumber,
       "friPStatsPortType": friPStatsPortType,
       "friPStatsPortStatus": friPStatsPortStatus,
       "friPStatsConfiguredStns": friPStatsConfiguredStns,
       "friPStatsPortSpeed": friPStatsPortSpeed,
       "friPStatsOpCntrlProtocol": friPStatsOpCntrlProtocol,
       "friPStatsSPBackup": friPStatsSPBackup,
       "friPStatsPriorityStn": friPStatsPriorityStn,
       "friPStatsLastStatsReset": friPStatsLastStatsReset,
       "cdx6500PPSTFRIDataSummaryTable": cdx6500PPSTFRIDataSummaryTable,
       "cdx6500PPSTFRIDataSummaryEntry": cdx6500PPSTFRIDataSummaryEntry,
       "friDataSummPortNumber": friDataSummPortNumber,
       "friPStatsCharInTotal": friPStatsCharInTotal,
       "friPStatsCharOutTotal": friPStatsCharOutTotal,
       "friPStatsCharInPerSec": friPStatsCharInPerSec,
       "friPStatsCharOutPerSec": friPStatsCharOutPerSec,
       "friPStatsFramesInTotal": friPStatsFramesInTotal,
       "friPStatsFramesOutTotal": friPStatsFramesOutTotal,
       "friPStatsFramesInPerSec": friPStatsFramesInPerSec,
       "friPStatsFramesOutPerSec": friPStatsFramesOutPerSec,
       "friPStatsAvFrameSizeIn": friPStatsAvFrameSizeIn,
       "friPStatsAvFrameSizeOut": friPStatsAvFrameSizeOut,
       "friPStatsUtilIn": friPStatsUtilIn,
       "friPStatsUtilOut": friPStatsUtilOut,
       "cdx6500PPSTFRISummaryTable": cdx6500PPSTFRISummaryTable,
       "cdx6500PPSTFRISummaryEntry": cdx6500PPSTFRISummaryEntry,
       "friSummPortNumber": friSummPortNumber,
       "friPStatsCRCErrors": friPStatsCRCErrors,
       "friPStatsOverrunErrors": friPStatsOverrunErrors,
       "friPStatsFrameLengthErrors": friPStatsFrameLengthErrors,
       "friPStatsUnderrunErrors": friPStatsUnderrunErrors,
       "friPStatsUnknownDLCICount": friPStatsUnknownDLCICount,
       "friPStatsLastUnknownDLCI": friPStatsLastUnknownDLCI,
       "friPStatsSplittingRatio": friPStatsSplittingRatio,
       "friPStatsTotalSegmentsLost": friPStatsTotalSegmentsLost,
       "friPStatsMaxContiguousSegmentsLost": friPStatsMaxContiguousSegmentsLost,
       "friPStatsVoiceBWOnPort": friPStatsVoiceBWOnPort,
       "friPStatsFrameSegmenterSyncLost": friPStatsFrameSegmenterSyncLost,
       "friPStatsStatusEnqSentFull": friPStatsStatusEnqSentFull,
       "friPStatsFullStatusRecd": friPStatsFullStatusRecd,
       "friPStatsStatusEnqSentLIV": friPStatsStatusEnqSentLIV,
       "friPStatsLIVStatusRecd": friPStatsLIVStatusRecd,
       "friPStatsStatusEnqRecdFull": friPStatsStatusEnqRecdFull,
       "friPStatsStatusEnqRecdLIV": friPStatsStatusEnqRecdLIV,
       "friPStatsAsyncUpdateRecd": friPStatsAsyncUpdateRecd,
       "friPStatsSeqNumMismatch": friPStatsSeqNumMismatch,
       "friPStatsTimeouts": friPStatsTimeouts,
       "cdx6500PPSTFRIISDNCallStatusTable": cdx6500PPSTFRIISDNCallStatusTable,
       "cdx6500PPSTFRIISDNCallStatusEntry": cdx6500PPSTFRIISDNCallStatusEntry,
       "friISDNCallStatusPortNumber": friISDNCallStatusPortNumber,
       "friPStatsNumRxCallsSinceLastReset": friPStatsNumRxCallsSinceLastReset,
       "friPStatsNumRxCallsRejected": friPStatsNumRxCallsRejected,
       "friPStatsRxLastCallFailureCause": friPStatsRxLastCallFailureCause,
       "friPStatsRxLastCalledNumber": friPStatsRxLastCalledNumber,
       "friPStatsRxLastCallingNumber": friPStatsRxLastCallingNumber,
       "friPStatsRxMinCallDuration": friPStatsRxMinCallDuration,
       "friPStatsRxMaxCallDuration": friPStatsRxMaxCallDuration,
       "friPStatsRxAvgCallDuration": friPStatsRxAvgCallDuration,
       "friPStatsNumTxCallsSinceLastReset": friPStatsNumTxCallsSinceLastReset,
       "friPStatsNumTxCallsRejected": friPStatsNumTxCallsRejected,
       "friPStatsTxLastCallFailureCause": friPStatsTxLastCallFailureCause,
       "friPStatsTxLastCalledNumber": friPStatsTxLastCalledNumber,
       "friPStatsTxLastCallingNumber": friPStatsTxLastCallingNumber,
       "friPStatsTxMinCallDuration": friPStatsTxMinCallDuration,
       "friPStatsTxMaxCallDuration": friPStatsTxMaxCallDuration,
       "friPStatsTxAvgCallDuration": friPStatsTxAvgCallDuration,
       "friPStatsSignalingState": friPStatsSignalingState,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500SPSTFRISStatsTable": cdx6500SPSTFRISStatsTable,
       "friSGenStatsTable": friSGenStatsTable,
       "cdx6500friSGenStatsEntry": cdx6500friSGenStatsEntry,
       "friSGenStatsPortNumber": friSGenStatsPortNumber,
       "friSGenStatsStnNumber": friSGenStatsStnNumber,
       "friSStatsStnType": friSStatsStnType,
       "friSStatsStnStatus": friSStatsStnStatus,
       "friSStatsDLCI": friSStatsDLCI,
       "friSStatsStnState": friSStatsStnState,
       "friSStatsConfiguredCIR": friSStatsConfiguredCIR,
       "friSStatsAllowedInfoRate": friSStatsAllowedInfoRate,
       "friSStatsImpCongDetect": friSStatsImpCongDetect,
       "friSStatsExpCongDetect": friSStatsExpCongDetect,
       "friSStatsLMIFlowCntrl": friSStatsLMIFlowCntrl,
       "friSStatsMaxSVCCount": friSStatsMaxSVCCount,
       "friSStatsCurrSVCCount": friSStatsCurrSVCCount,
       "friSStatsMaxPVCCount": friSStatsMaxPVCCount,
       "friSStatsCurrPVCCount": friSStatsCurrPVCCount,
       "friSStatsLastStatsReset": friSStatsLastStatsReset,
       "friSStatsFrameSegState": friSStatsFrameSegState,
       "friSStatsFrameSegSyncLost": friSStatsFrameSegSyncLost,
       "friSStatsPVCState": friSStatsPVCState,
       "friSStatsVoiceCongDetect": friSStatsVoiceCongDetect,
       "friSStatsMaxVSVCCount": friSStatsMaxVSVCCount,
       "friSStatsCurrVSVCCount": friSStatsCurrVSVCCount,
       "friSDataSummaryStatsTable": friSDataSummaryStatsTable,
       "cdx6500friSDataSummaryStatsEntry": cdx6500friSDataSummaryStatsEntry,
       "friSDataSummStatsPortNumber": friSDataSummStatsPortNumber,
       "friSDataSummStatsStnNumber": friSDataSummStatsStnNumber,
       "friSStatsCharInTotal": friSStatsCharInTotal,
       "friSStatsCharOutTotal": friSStatsCharOutTotal,
       "friSStatsCharInPerSec": friSStatsCharInPerSec,
       "friSStatsCharOutPerSec": friSStatsCharOutPerSec,
       "friSStatsPktInTotal": friSStatsPktInTotal,
       "friSStatsPktOutTotal": friSStatsPktOutTotal,
       "friSStatsPktInPerSec": friSStatsPktInPerSec,
       "friSStatsPktOutPerSec": friSStatsPktOutPerSec,
       "friSStatsFrameInTotal": friSStatsFrameInTotal,
       "friSStatsFrameOutTotal": friSStatsFrameOutTotal,
       "friSStatsFrameInPerSec": friSStatsFrameInPerSec,
       "friSStatsFrameOutPerSec": friSStatsFrameOutPerSec,
       "friSStatsUtilIn": friSStatsUtilIn,
       "friSStatsUtilOut": friSStatsUtilOut,
       "friSStatsNumPktsQueued": friSStatsNumPktsQueued,
       "friSStatsPktsDiscardIn": friSStatsPktsDiscardIn,
       "friSStatsPktsDiscardOut": friSStatsPktsDiscardOut,
       "friSStatsPktsQueuedIn": friSStatsPktsQueuedIn,
       "friSStatsPktsQueuedOut": friSStatsPktsQueuedOut,
       "friSVoiceSummaryStatsTable": friSVoiceSummaryStatsTable,
       "cdx6500friSVoiceSummaryStatsEntry": cdx6500friSVoiceSummaryStatsEntry,
       "friSVoiceSummStatsPortNumber": friSVoiceSummStatsPortNumber,
       "friSVoiceSummStatsStnNumber": friSVoiceSummStatsStnNumber,
       "friSStatsVoiceCharInTotal": friSStatsVoiceCharInTotal,
       "friSStatsVoiceCharOutTotal": friSStatsVoiceCharOutTotal,
       "friSStatsVoiceCharInPerSec": friSStatsVoiceCharInPerSec,
       "friSStatsVoiceCharOutPerSec": friSStatsVoiceCharOutPerSec,
       "friSStatsVoicePktInTotal": friSStatsVoicePktInTotal,
       "friSStatsVoicePktOutTotal": friSStatsVoicePktOutTotal,
       "friSStatsVoicePktInPerSec": friSStatsVoicePktInPerSec,
       "friSStatsVoicePktOutPerSec": friSStatsVoicePktOutPerSec,
       "friSFrameSummaryStatsTable": friSFrameSummaryStatsTable,
       "cdx6500friSFrameSummaryStatsEntry": cdx6500friSFrameSummaryStatsEntry,
       "friSFrameSummStatsPortNumber": friSFrameSummStatsPortNumber,
       "friSFrameSummStatsStnNumber": friSFrameSummStatsStnNumber,
       "friSStatsInfoFramesInTotal": friSStatsInfoFramesInTotal,
       "friSStatsInfoFramesOutTotal": friSStatsInfoFramesOutTotal,
       "friSStatsRRFramesInTotal": friSStatsRRFramesInTotal,
       "friSStatsRRFramesOutTotal": friSStatsRRFramesOutTotal,
       "friSStatsRNRFramesInTotal": friSStatsRNRFramesInTotal,
       "friSStatsRNRFramesOutTotal": friSStatsRNRFramesOutTotal,
       "friSStatsREJFramesInTotal": friSStatsREJFramesInTotal,
       "friSStatsREJFramesOutTotal": friSStatsREJFramesOutTotal,
       "friSStatsSABMFramesInTotal": friSStatsSABMFramesInTotal,
       "friSStatsSABMFramesOutTotal": friSStatsSABMFramesOutTotal,
       "friSStatsDISCFramesInTotal": friSStatsDISCFramesInTotal,
       "friSStatsDISCFramesOutTotal": friSStatsDISCFramesOutTotal,
       "friSStatsDMFramesInTotal": friSStatsDMFramesInTotal,
       "friSStatsDMFramesOutTotal": friSStatsDMFramesOutTotal,
       "friSStatsUAFramesInTotal": friSStatsUAFramesInTotal,
       "friSStatsUAFramesOutTotal": friSStatsUAFramesOutTotal,
       "friSStatsFRMRFramesInTotal": friSStatsFRMRFramesInTotal,
       "friSStatsFRMRFramesOutTotal": friSStatsFRMRFramesOutTotal,
       "friSPacketSummaryStatsTable": friSPacketSummaryStatsTable,
       "cdx6500friSPacketSummaryStatsEntry": cdx6500friSPacketSummaryStatsEntry,
       "friSPktSummStatsPortNumber": friSPktSummStatsPortNumber,
       "friSPktSummStatsStnNumber": friSPktSummStatsStnNumber,
       "friSStatsDataPktInTotal": friSStatsDataPktInTotal,
       "friSStatsDataPktOutTotal": friSStatsDataPktOutTotal,
       "friSStatsRRPktInTotal": friSStatsRRPktInTotal,
       "friSStatsRRPktOutTotal": friSStatsRRPktOutTotal,
       "friSStatsRNRPktInTotal": friSStatsRNRPktInTotal,
       "friSStatsRNRPktOutTotal": friSStatsRNRPktOutTotal,
       "friSStatsREJPktInTotal": friSStatsREJPktInTotal,
       "friSStatsREJPktOutTotal": friSStatsREJPktOutTotal,
       "friSStatsCallReqPktInTotal": friSStatsCallReqPktInTotal,
       "friSStatsCallReqPktOutTotal": friSStatsCallReqPktOutTotal,
       "friSStatsCallAccPktInTotal": friSStatsCallAccPktInTotal,
       "friSStatsCallAccPktOutTotal": friSStatsCallAccPktOutTotal,
       "friSStatsClrReqPktInTotal": friSStatsClrReqPktInTotal,
       "friSStatsClrReqPktOutTotal": friSStatsClrReqPktOutTotal,
       "friSStatsClrConfPktInTotal": friSStatsClrConfPktInTotal,
       "friSStatsClrConfPktOutTotal": friSStatsClrConfPktOutTotal,
       "friSStatsIntrReqPktInTotal": friSStatsIntrReqPktInTotal,
       "friSStatsIntrReqPktOutTotal": friSStatsIntrReqPktOutTotal,
       "friSStatsIntrConfPktInTotal": friSStatsIntrConfPktInTotal,
       "friSStatsIntrConfPktOutTotal": friSStatsIntrConfPktOutTotal,
       "friSStatsResetReqPktInTotal": friSStatsResetReqPktInTotal,
       "friSStatsResetReqPktOutTotal": friSStatsResetReqPktOutTotal,
       "friSStatsResetConfPktInTotal": friSStatsResetConfPktInTotal,
       "friSStatsResetConfPktOutTotal": friSStatsResetConfPktOutTotal,
       "friSStatsRestartReqPktInTotal": friSStatsRestartReqPktInTotal,
       "friSStatsRestartReqPktOutTotal": friSStatsRestartReqPktOutTotal,
       "friSStatsRestartConfPktInTotal": friSStatsRestartConfPktInTotal,
       "friSStatsRestartConfPktOutTotal": friSStatsRestartConfPktOutTotal,
       "friSFRISummaryStatsTable": friSFRISummaryStatsTable,
       "cdx6500friSFRISummaryStatsEntry": cdx6500friSFRISummaryStatsEntry,
       "friSFRISummStatsPortNumber": friSFRISummStatsPortNumber,
       "friSFRISummStatsStnNumber": friSFRISummStatsStnNumber,
       "friSStatsFECNInTotal": friSStatsFECNInTotal,
       "friSStatsFECNOutTotal": friSStatsFECNOutTotal,
       "friSStatsBECNInTotal": friSStatsBECNInTotal,
       "friSStatsBECNOutTotal": friSStatsBECNOutTotal,
       "friSStatsDEInTotal": friSStatsDEInTotal,
       "friSStatsDEOutTotal": friSStatsDEOutTotal,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContFRITable": cdx6500ContFRITable,
       "cdx6500FRIPContTable": cdx6500FRIPContTable,
       "cdx6500FRIPContEntry": cdx6500FRIPContEntry,
       "friPContPortNumber": friPContPortNumber,
       "friPContPortControl": friPContPortControl,
       "cdx6500FRISContTable": cdx6500FRISContTable,
       "cdx6500FRISContEntry": cdx6500FRISContEntry,
       "friSContPortNumber": friSContPortNumber,
       "friSContStnNumber": friSContStnNumber,
       "friSContStnControl": friSContStnControl}
)
