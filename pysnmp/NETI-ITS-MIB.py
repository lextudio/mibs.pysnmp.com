# SNMP MIB module (NETI-ITS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETI-ITS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:35 2024
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

(Dsti,) = mibBuilder.importSymbols(
    "NETI-CHMGR-MIB",
    "Dsti")

(netiExperimentalGeneric,) = mibBuilder.importSymbols(
    "NETI-COMMON-MIB",
    "netiExperimentalGeneric")

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

(DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

netiItsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16)
)
netiItsMIB.setRevisions(
        ("2014-09-11 13:00",
         "2014-02-21 15:00",
         "2013-09-30 07:00",
         "2012-12-03 11:00",
         "2012-09-04 14:00",
         "2012-01-20 16:00",
         "2011-12-01 09:00",
         "2011-10-10 13:00",
         "2011-04-27 09:00",
         "2011-04-27 08:00",
         "2011-02-04 12:00",
         "2011-02-03 09:00",
         "2010-08-19 09:00",
         "2010-01-19 09:00",
         "2009-01-22 15:00",
         "2008-04-17 10:30",
         "2008-01-18 15:00",
         "2007-12-04 16:00",
         "2007-06-29 14:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ItsTtpIndexList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
    )



class ItsProtectionStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("hitlessCapable", 4),
          ("hitlessProtected", 5),
          ("standbyProtected", 3),
          ("unavailable", 1),
          ("unprotected", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ItsObjects_ObjectIdentity = ObjectIdentity
itsObjects = _ItsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1)
)
_ItsIfGroup_ObjectIdentity = ObjectIdentity
itsIfGroup = _ItsIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1)
)
_ItsIfLastChange_Type = TimeStamp
_ItsIfLastChange_Object = MibScalar
itsIfLastChange = _ItsIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 1),
    _ItsIfLastChange_Type()
)
itsIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfLastChange.setStatus("current")
_ItsIfTable_Object = MibTable
itsIfTable = _ItsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2)
)
if mibBuilder.loadTexts:
    itsIfTable.setStatus("current")
_ItsIfEntry_Object = MibTableRow
itsIfEntry = _ItsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1)
)
itsIfEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsIfIndex"),
)
if mibBuilder.loadTexts:
    itsIfEntry.setStatus("current")
_ItsIfIndex_Type = Unsigned32
_ItsIfIndex_Object = MibTableColumn
itsIfIndex = _ItsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 1),
    _ItsIfIndex_Type()
)
itsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    itsIfIndex.setStatus("current")
_ItsIfIfIndex_Type = Integer32
_ItsIfIfIndex_Object = MibTableColumn
itsIfIfIndex = _ItsIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 2),
    _ItsIfIfIndex_Type()
)
itsIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfIfIndex.setStatus("current")
_ItsIfName_Type = SnmpAdminString
_ItsIfName_Object = MibTableColumn
itsIfName = _ItsIfName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 3),
    _ItsIfName_Type()
)
itsIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfName.setStatus("current")
_ItsIfDescr_Type = SnmpAdminString
_ItsIfDescr_Object = MibTableColumn
itsIfDescr = _ItsIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 4),
    _ItsIfDescr_Type()
)
itsIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfDescr.setStatus("current")
_ItsIfSpeed_Type = Gauge32
_ItsIfSpeed_Object = MibTableColumn
itsIfSpeed = _ItsIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 5),
    _ItsIfSpeed_Type()
)
itsIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfSpeed.setStatus("current")


class _ItsIfSuppressAlarm_Type(Integer32):
    """Custom type itsIfSuppressAlarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("none", 1),
          ("notSupported", 0),
          ("warning", 2))
    )


_ItsIfSuppressAlarm_Type.__name__ = "Integer32"
_ItsIfSuppressAlarm_Object = MibTableColumn
itsIfSuppressAlarm = _ItsIfSuppressAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 6),
    _ItsIfSuppressAlarm_Type()
)
itsIfSuppressAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSuppressAlarm.setStatus("current")


class _ItsIfLoopMode_Type(Integer32):
    """Custom type itsIfLoopMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dtm", 3),
          ("line", 2),
          ("none", 1),
          ("notSupported", 0))
    )


_ItsIfLoopMode_Type.__name__ = "Integer32"
_ItsIfLoopMode_Object = MibTableColumn
itsIfLoopMode = _ItsIfLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 7),
    _ItsIfLoopMode_Type()
)
itsIfLoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfLoopMode.setStatus("current")


class _ItsIfLoopTime_Type(Gauge32):
    """Custom type itsIfLoopTime based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ItsIfLoopTime_Type.__name__ = "Gauge32"
_ItsIfLoopTime_Object = MibTableColumn
itsIfLoopTime = _ItsIfLoopTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 8),
    _ItsIfLoopTime_Type()
)
itsIfLoopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfLoopTime.setStatus("deprecated")


class _ItsIfCapabilities_Type(Bits):
    """Custom type itsIfCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("allowProtection", 1),
          ("avrs", 16),
          ("channelPM", 3),
          ("compatible", 31),
          ("dvrs", 25),
          ("fs", 15),
          ("hitps", 23),
          ("interfacePM", 4),
          ("j2kDec", 22),
          ("j2kEnc", 21),
          ("loopd", 8),
          ("loopl", 7),
          ("madi", 19),
          ("mon", 6),
          ("multicast", 0),
          ("psType3", 24),
          ("ref", 20),
          ("requireCapacity", 2),
          ("sdi1483", 9),
          ("sdi1485", 10),
          ("sdi270", 12),
          ("sdi288", 11),
          ("sdi2967", 13),
          ("sdi2970", 14),
          ("ttp", 5))
    )

_ItsIfCapabilities_Type.__name__ = "Bits"
_ItsIfCapabilities_Object = MibTableColumn
itsIfCapabilities = _ItsIfCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 9),
    _ItsIfCapabilities_Type()
)
itsIfCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfCapabilities.setStatus("current")


class _ItsIfProperties_Type(Bits):
    """Custom type itsIfProperties based on Bits"""
    namedValues = NamedValues(
        ("tbd", 0)
    )

_ItsIfProperties_Type.__name__ = "Bits"
_ItsIfProperties_Object = MibTableColumn
itsIfProperties = _ItsIfProperties_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 10),
    _ItsIfProperties_Type()
)
itsIfProperties.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfProperties.setStatus("current")


class _ItsIfDefects_Type(Bits):
    """Custom type itsIfDefects based on Bits"""
    namedValues = NamedValues(
        *(("ais", 2),
          ("lod", 4),
          ("lof", 1),
          ("lol", 6),
          ("lop", 3),
          ("los", 0),
          ("rdi", 5))
    )

_ItsIfDefects_Type.__name__ = "Bits"
_ItsIfDefects_Object = MibTableColumn
itsIfDefects = _ItsIfDefects_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 11),
    _ItsIfDefects_Type()
)
itsIfDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfDefects.setStatus("current")
_ItsIfFailure_Type = SnmpAdminString
_ItsIfFailure_Object = MibTableColumn
itsIfFailure = _ItsIfFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 12),
    _ItsIfFailure_Type()
)
itsIfFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfFailure.setStatus("current")
_ItsIfPMReference_Type = RowPointer
_ItsIfPMReference_Object = MibTableColumn
itsIfPMReference = _ItsIfPMReference_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 13),
    _ItsIfPMReference_Type()
)
itsIfPMReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfPMReference.setStatus("current")


class _ItsIfOperStatus_Type(Integer32):
    """Custom type itsIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("notPresent", 6),
          ("unknown", 4),
          ("up", 1))
    )


_ItsIfOperStatus_Type.__name__ = "Integer32"
_ItsIfOperStatus_Object = MibTableColumn
itsIfOperStatus = _ItsIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 14),
    _ItsIfOperStatus_Type()
)
itsIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfOperStatus.setStatus("current")


class _ItsIfTxMuteOnFault_Type(Integer32):
    """Custom type itsIfTxMuteOnFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("freeze", 3),
          ("notSupported", 0))
    )


_ItsIfTxMuteOnFault_Type.__name__ = "Integer32"
_ItsIfTxMuteOnFault_Object = MibTableColumn
itsIfTxMuteOnFault = _ItsIfTxMuteOnFault_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 15),
    _ItsIfTxMuteOnFault_Type()
)
itsIfTxMuteOnFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfTxMuteOnFault.setStatus("current")


class _ItsIfPurpose_Type(SnmpAdminString):
    """Custom type itsIfPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_ItsIfPurpose_Object = MibTableColumn
itsIfPurpose = _ItsIfPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 16),
    _ItsIfPurpose_Type()
)
itsIfPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfPurpose.setStatus("current")


class _ItsIfInterfaceType_Type(Integer32):
    """Custom type itsIfInterfaceType based on Integer32"""
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
        *(("aes", 5),
          ("dvb", 4),
          ("mon", 6),
          ("pdh", 1),
          ("sdh", 2),
          ("sdi", 3))
    )


_ItsIfInterfaceType_Type.__name__ = "Integer32"
_ItsIfInterfaceType_Object = MibTableColumn
itsIfInterfaceType = _ItsIfInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 17),
    _ItsIfInterfaceType_Type()
)
itsIfInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfInterfaceType.setStatus("current")
_ItsIfMembersSrc_Type = ItsTtpIndexList
_ItsIfMembersSrc_Object = MibTableColumn
itsIfMembersSrc = _ItsIfMembersSrc_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 18),
    _ItsIfMembersSrc_Type()
)
itsIfMembersSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfMembersSrc.setStatus("current")
_ItsIfMembersSnk_Type = ItsTtpIndexList
_ItsIfMembersSnk_Object = MibTableColumn
itsIfMembersSnk = _ItsIfMembersSnk_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 2, 1, 19),
    _ItsIfMembersSnk_Type()
)
itsIfMembersSnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfMembersSnk.setStatus("current")
_ItsIfPdhTable_Object = MibTable
itsIfPdhTable = _ItsIfPdhTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 3)
)
if mibBuilder.loadTexts:
    itsIfPdhTable.setStatus("current")
_ItsIfPdhEntry_Object = MibTableRow
itsIfPdhEntry = _ItsIfPdhEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 3, 1)
)
itsIfPdhEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsIfIndex"),
)
if mibBuilder.loadTexts:
    itsIfPdhEntry.setStatus("current")


class _ItsIfPdhSignal_Type(Integer32):
    """Custom type itsIfPdhSignal based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3", 2),
          ("e3", 1))
    )


_ItsIfPdhSignal_Type.__name__ = "Integer32"
_ItsIfPdhSignal_Object = MibTableColumn
itsIfPdhSignal = _ItsIfPdhSignal_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 3, 1, 1),
    _ItsIfPdhSignal_Type()
)
itsIfPdhSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfPdhSignal.setStatus("current")


class _ItsIfPdhFraming_Type(Integer32):
    """Custom type itsIfPdhFraming based on Integer32"""
    defaultValue = 1

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
        *(("cbit", 4),
          ("g751", 2),
          ("g832", 3),
          ("m13", 5),
          ("none", 1))
    )


_ItsIfPdhFraming_Type.__name__ = "Integer32"
_ItsIfPdhFraming_Object = MibTableColumn
itsIfPdhFraming = _ItsIfPdhFraming_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 3, 1, 2),
    _ItsIfPdhFraming_Type()
)
itsIfPdhFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfPdhFraming.setStatus("current")
_ItsIfSdhTable_Object = MibTable
itsIfSdhTable = _ItsIfSdhTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 4)
)
if mibBuilder.loadTexts:
    itsIfSdhTable.setStatus("current")
_ItsIfSdhEntry_Object = MibTableRow
itsIfSdhEntry = _ItsIfSdhEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 4, 1)
)
itsIfSdhEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsIfIndex"),
)
if mibBuilder.loadTexts:
    itsIfSdhEntry.setStatus("current")


class _ItsIfSdhTiming_Type(Integer32):
    """Custom type itsIfSdhTiming based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("loop", 1))
    )


_ItsIfSdhTiming_Type.__name__ = "Integer32"
_ItsIfSdhTiming_Object = MibTableColumn
itsIfSdhTiming = _ItsIfSdhTiming_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 4, 1, 1),
    _ItsIfSdhTiming_Type()
)
itsIfSdhTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdhTiming.setStatus("current")


class _ItsIfSdhMode_Type(Integer32):
    """Custom type itsIfSdhMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 1),
          ("sonet", 2))
    )


_ItsIfSdhMode_Type.__name__ = "Integer32"
_ItsIfSdhMode_Object = MibTableColumn
itsIfSdhMode = _ItsIfSdhMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 4, 1, 2),
    _ItsIfSdhMode_Type()
)
itsIfSdhMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdhMode.setStatus("current")


class _ItsIfSdhSs_Type(Unsigned32):
    """Custom type itsIfSdhSs based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ItsIfSdhSs_Type.__name__ = "Unsigned32"
_ItsIfSdhSs_Object = MibTableColumn
itsIfSdhSs = _ItsIfSdhSs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 4, 1, 3),
    _ItsIfSdhSs_Type()
)
itsIfSdhSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdhSs.setStatus("current")


class _ItsIfSdhS1_Type(Unsigned32):
    """Custom type itsIfSdhS1 based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ItsIfSdhS1_Type.__name__ = "Unsigned32"
_ItsIfSdhS1_Object = MibTableColumn
itsIfSdhS1 = _ItsIfSdhS1_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 4, 1, 4),
    _ItsIfSdhS1_Type()
)
itsIfSdhS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdhS1.setStatus("current")
_ItsIfSdhSoh_Type = SnmpAdminString
_ItsIfSdhSoh_Object = MibTableColumn
itsIfSdhSoh = _ItsIfSdhSoh_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 4, 1, 5),
    _ItsIfSdhSoh_Type()
)
itsIfSdhSoh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfSdhSoh.setStatus("current")
_ItsIfSdhPoh_Type = SnmpAdminString
_ItsIfSdhPoh_Object = MibTableColumn
itsIfSdhPoh = _ItsIfSdhPoh_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 4, 1, 6),
    _ItsIfSdhPoh_Type()
)
itsIfSdhPoh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfSdhPoh.setStatus("current")
_ItsIfSdhJc_Type = SnmpAdminString
_ItsIfSdhJc_Object = MibTableColumn
itsIfSdhJc = _ItsIfSdhJc_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 4, 1, 7),
    _ItsIfSdhJc_Type()
)
itsIfSdhJc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfSdhJc.setStatus("current")
_ItsIfDvbTable_Object = MibTable
itsIfDvbTable = _ItsIfDvbTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 5)
)
if mibBuilder.loadTexts:
    itsIfDvbTable.setStatus("current")
_ItsIfDvbEntry_Object = MibTableRow
itsIfDvbEntry = _ItsIfDvbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 5, 1)
)
itsIfDvbEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsIfIndex"),
)
if mibBuilder.loadTexts:
    itsIfDvbEntry.setStatus("current")
_ItsIfDvbFormat_Type = SnmpAdminString
_ItsIfDvbFormat_Object = MibTableColumn
itsIfDvbFormat = _ItsIfDvbFormat_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 5, 1, 1),
    _ItsIfDvbFormat_Type()
)
itsIfDvbFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfDvbFormat.setStatus("current")


class _ItsIfDvbOutputMode_Type(Integer32):
    """Custom type itsIfDvbOutputMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("burst", 2),
          ("spread", 3))
    )


_ItsIfDvbOutputMode_Type.__name__ = "Integer32"
_ItsIfDvbOutputMode_Object = MibTableColumn
itsIfDvbOutputMode = _ItsIfDvbOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 5, 1, 2),
    _ItsIfDvbOutputMode_Type()
)
itsIfDvbOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfDvbOutputMode.setStatus("current")
_ItsIfAesTable_Object = MibTable
itsIfAesTable = _ItsIfAesTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 6)
)
if mibBuilder.loadTexts:
    itsIfAesTable.setStatus("current")
_ItsIfAesEntry_Object = MibTableRow
itsIfAesEntry = _ItsIfAesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 6, 1)
)
itsIfAesEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsIfIndex"),
)
if mibBuilder.loadTexts:
    itsIfAesEntry.setStatus("current")


class _ItsIfAesIsTimingProvider_Type(Integer32):
    """Custom type itsIfAesIsTimingProvider based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("wordClock", 1))
    )


_ItsIfAesIsTimingProvider_Type.__name__ = "Integer32"
_ItsIfAesIsTimingProvider_Object = MibTableColumn
itsIfAesIsTimingProvider = _ItsIfAesIsTimingProvider_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 6, 1, 1),
    _ItsIfAesIsTimingProvider_Type()
)
itsIfAesIsTimingProvider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfAesIsTimingProvider.setStatus("current")
_ItsIfAesReference_Type = Integer32
_ItsIfAesReference_Object = MibTableColumn
itsIfAesReference = _ItsIfAesReference_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 6, 1, 2),
    _ItsIfAesReference_Type()
)
itsIfAesReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfAesReference.setStatus("current")
_ItsIfSdiTable_Object = MibTable
itsIfSdiTable = _ItsIfSdiTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 7)
)
if mibBuilder.loadTexts:
    itsIfSdiTable.setStatus("current")
_ItsIfSdiEntry_Object = MibTableRow
itsIfSdiEntry = _ItsIfSdiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 7, 1)
)
itsIfSdiEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsIfIndex"),
)
if mibBuilder.loadTexts:
    itsIfSdiEntry.setStatus("current")
_ItsIfSdiFormat_Type = SnmpAdminString
_ItsIfSdiFormat_Object = MibTableColumn
itsIfSdiFormat = _ItsIfSdiFormat_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 7, 1, 1),
    _ItsIfSdiFormat_Type()
)
itsIfSdiFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfSdiFormat.setStatus("current")


class _ItsIfSdiAutoSense_Type(Integer32):
    """Custom type itsIfSdiAutoSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupported", 0))
    )


_ItsIfSdiAutoSense_Type.__name__ = "Integer32"
_ItsIfSdiAutoSense_Object = MibTableColumn
itsIfSdiAutoSense = _ItsIfSdiAutoSense_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 7, 1, 2),
    _ItsIfSdiAutoSense_Type()
)
itsIfSdiAutoSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdiAutoSense.setStatus("current")


class _ItsIfSdiIsTimingProvider_Type(Integer32):
    """Custom type itsIfSdiIsTimingProvider based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog", 1),
          ("digital", 2),
          ("no", 0))
    )


_ItsIfSdiIsTimingProvider_Type.__name__ = "Integer32"
_ItsIfSdiIsTimingProvider_Object = MibTableColumn
itsIfSdiIsTimingProvider = _ItsIfSdiIsTimingProvider_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 7, 1, 3),
    _ItsIfSdiIsTimingProvider_Type()
)
itsIfSdiIsTimingProvider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdiIsTimingProvider.setStatus("current")
_ItsIfSdiReference_Type = Integer32
_ItsIfSdiReference_Object = MibTableColumn
itsIfSdiReference = _ItsIfSdiReference_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 7, 1, 4),
    _ItsIfSdiReference_Type()
)
itsIfSdiReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdiReference.setStatus("current")


class _ItsIfSdiFsVDelay_Type(Integer32):
    """Custom type itsIfSdiFsVDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 1124),
    )


_ItsIfSdiFsVDelay_Type.__name__ = "Integer32"
_ItsIfSdiFsVDelay_Object = MibTableColumn
itsIfSdiFsVDelay = _ItsIfSdiFsVDelay_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 7, 1, 5),
    _ItsIfSdiFsVDelay_Type()
)
itsIfSdiFsVDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdiFsVDelay.setStatus("obsolete")


class _ItsIfSdiFsHDelay_Type(Integer32):
    """Custom type itsIfSdiFsHDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3865, 259),
    )


_ItsIfSdiFsHDelay_Type.__name__ = "Integer32"
_ItsIfSdiFsHDelay_Object = MibTableColumn
itsIfSdiFsHDelay = _ItsIfSdiFsHDelay_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 7, 1, 6),
    _ItsIfSdiFsHDelay_Type()
)
itsIfSdiFsHDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdiFsHDelay.setStatus("obsolete")


class _ItsIfSdiFsDelay_Type(Integer32):
    """Custom type itsIfSdiFsDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20854167, 20854167),
    )


_ItsIfSdiFsDelay_Type.__name__ = "Integer32"
_ItsIfSdiFsDelay_Object = MibTableColumn
itsIfSdiFsDelay = _ItsIfSdiFsDelay_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 7, 1, 7),
    _ItsIfSdiFsDelay_Type()
)
itsIfSdiFsDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdiFsDelay.setStatus("current")
_ItsIfMonTable_Object = MibTable
itsIfMonTable = _ItsIfMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 9)
)
if mibBuilder.loadTexts:
    itsIfMonTable.setStatus("current")
_ItsIfMonEntry_Object = MibTableRow
itsIfMonEntry = _ItsIfMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 9, 1)
)
itsIfMonEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsIfIndex"),
)
if mibBuilder.loadTexts:
    itsIfMonEntry.setStatus("current")


class _ItsIfMonMonitoredInterface_Type(Integer32):
    """Custom type itsIfMonMonitoredInterface based on Integer32"""
    defaultValue = 0


_ItsIfMonMonitoredInterface_Object = MibTableColumn
itsIfMonMonitoredInterface = _ItsIfMonMonitoredInterface_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 9, 1, 1),
    _ItsIfMonMonitoredInterface_Type()
)
itsIfMonMonitoredInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfMonMonitoredInterface.setStatus("current")


class _ItsIfMonDirection_Type(Integer32):
    """Custom type itsIfMonDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_ItsIfMonDirection_Type.__name__ = "Integer32"
_ItsIfMonDirection_Object = MibTableColumn
itsIfMonDirection = _ItsIfMonDirection_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 9, 1, 2),
    _ItsIfMonDirection_Type()
)
itsIfMonDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfMonDirection.setStatus("current")


class _ItsIfEnableButton_Type(TruthValue):
    """Custom type itsIfEnableButton based on TruthValue"""


_ItsIfEnableButton_Object = MibTableColumn
itsIfEnableButton = _ItsIfEnableButton_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 9, 1, 3),
    _ItsIfEnableButton_Type()
)
itsIfEnableButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfEnableButton.setStatus("current")
_ItsIfJ2kTable_Object = MibTable
itsIfJ2kTable = _ItsIfJ2kTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 10)
)
if mibBuilder.loadTexts:
    itsIfJ2kTable.setStatus("current")
_ItsIfJ2kEntry_Object = MibTableRow
itsIfJ2kEntry = _ItsIfJ2kEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 10, 1)
)
itsIfJ2kEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsIfIndex"),
)
if mibBuilder.loadTexts:
    itsIfJ2kEntry.setStatus("current")


class _ItsIfJ2kEncoderEnable_Type(TruthValue):
    """Custom type itsIfJ2kEncoderEnable based on TruthValue"""


_ItsIfJ2kEncoderEnable_Object = MibTableColumn
itsIfJ2kEncoderEnable = _ItsIfJ2kEncoderEnable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 10, 1, 1),
    _ItsIfJ2kEncoderEnable_Type()
)
itsIfJ2kEncoderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfJ2kEncoderEnable.setStatus("current")
_ItsIfJ2kDecoderActive_Type = TruthValue
_ItsIfJ2kDecoderActive_Object = MibTableColumn
itsIfJ2kDecoderActive = _ItsIfJ2kDecoderActive_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 10, 1, 2),
    _ItsIfJ2kDecoderActive_Type()
)
itsIfJ2kDecoderActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfJ2kDecoderActive.setStatus("current")


class _ItsIfJ2kSignalFormat_Type(Integer32):
    """Custom type itsIfJ2kSignalFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("hd3gSdiEu", 5),
          ("hd3gSdiUs", 6),
          ("hdSdiEu", 3),
          ("hdSdiUs", 4),
          ("notApplicable", 0),
          ("sdSdi", 1))
    )


_ItsIfJ2kSignalFormat_Type.__name__ = "Integer32"
_ItsIfJ2kSignalFormat_Object = MibTableColumn
itsIfJ2kSignalFormat = _ItsIfJ2kSignalFormat_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 10, 1, 3),
    _ItsIfJ2kSignalFormat_Type()
)
itsIfJ2kSignalFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfJ2kSignalFormat.setStatus("current")
_ItsIfJ2kRateVideo_Type = Unsigned32
_ItsIfJ2kRateVideo_Object = MibTableColumn
itsIfJ2kRateVideo = _ItsIfJ2kRateVideo_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 10, 1, 4),
    _ItsIfJ2kRateVideo_Type()
)
itsIfJ2kRateVideo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfJ2kRateVideo.setStatus("current")
_ItsIfJ2kRateVideoMax_Type = Unsigned32
_ItsIfJ2kRateVideoMax_Object = MibTableColumn
itsIfJ2kRateVideoMax = _ItsIfJ2kRateVideoMax_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 10, 1, 5),
    _ItsIfJ2kRateVideoMax_Type()
)
itsIfJ2kRateVideoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfJ2kRateVideoMax.setStatus("current")
_ItsIfJ2kRateVbi_Type = Unsigned32
_ItsIfJ2kRateVbi_Object = MibTableColumn
itsIfJ2kRateVbi = _ItsIfJ2kRateVbi_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 10, 1, 6),
    _ItsIfJ2kRateVbi_Type()
)
itsIfJ2kRateVbi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfJ2kRateVbi.setStatus("current")
_ItsIfJ2kRateAnc_Type = Unsigned32
_ItsIfJ2kRateAnc_Object = MibTableColumn
itsIfJ2kRateAnc = _ItsIfJ2kRateAnc_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 10, 1, 7),
    _ItsIfJ2kRateAnc_Type()
)
itsIfJ2kRateAnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfJ2kRateAnc.setStatus("current")
_ItsIfJ2kRateAudio_Type = Unsigned32
_ItsIfJ2kRateAudio_Object = MibTableColumn
itsIfJ2kRateAudio = _ItsIfJ2kRateAudio_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 10, 1, 8),
    _ItsIfJ2kRateAudio_Type()
)
itsIfJ2kRateAudio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfJ2kRateAudio.setStatus("current")


class _ItsIfJ2kAudioSampleSize_Type(Unsigned32):
    """Custom type itsIfJ2kAudioSampleSize based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(24, 24),
    )


_ItsIfJ2kAudioSampleSize_Type.__name__ = "Unsigned32"
_ItsIfJ2kAudioSampleSize_Object = MibTableColumn
itsIfJ2kAudioSampleSize = _ItsIfJ2kAudioSampleSize_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 10, 1, 9),
    _ItsIfJ2kAudioSampleSize_Type()
)
itsIfJ2kAudioSampleSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfJ2kAudioSampleSize.setStatus("current")


class _ItsIfJ2kReduceAudioTransportBitrate_Type(TruthValue):
    """Custom type itsIfJ2kReduceAudioTransportBitrate based on TruthValue"""


_ItsIfJ2kReduceAudioTransportBitrate_Object = MibTableColumn
itsIfJ2kReduceAudioTransportBitrate = _ItsIfJ2kReduceAudioTransportBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 10, 1, 10),
    _ItsIfJ2kReduceAudioTransportBitrate_Type()
)
itsIfJ2kReduceAudioTransportBitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfJ2kReduceAudioTransportBitrate.setStatus("current")
_ItsIfSdiAudioTable_Object = MibTable
itsIfSdiAudioTable = _ItsIfSdiAudioTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 11)
)
if mibBuilder.loadTexts:
    itsIfSdiAudioTable.setStatus("current")
_ItsIfSdiAudioEntry_Object = MibTableRow
itsIfSdiAudioEntry = _ItsIfSdiAudioEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 11, 1)
)
itsIfSdiAudioEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsIfIndex"),
    (0, "NETI-ITS-MIB", "itsIfSdiAudioIndex"),
)
if mibBuilder.loadTexts:
    itsIfSdiAudioEntry.setStatus("current")


class _ItsIfSdiAudioIndex_Type(Unsigned32):
    """Custom type itsIfSdiAudioIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ItsIfSdiAudioIndex_Type.__name__ = "Unsigned32"
_ItsIfSdiAudioIndex_Object = MibTableColumn
itsIfSdiAudioIndex = _ItsIfSdiAudioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 11, 1, 1),
    _ItsIfSdiAudioIndex_Type()
)
itsIfSdiAudioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    itsIfSdiAudioIndex.setStatus("current")


class _ItsIfSdiAudioForward_Type(TruthValue):
    """Custom type itsIfSdiAudioForward based on TruthValue"""


_ItsIfSdiAudioForward_Object = MibTableColumn
itsIfSdiAudioForward = _ItsIfSdiAudioForward_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 11, 1, 2),
    _ItsIfSdiAudioForward_Type()
)
itsIfSdiAudioForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdiAudioForward.setStatus("current")
_ItsIfSdiVbiTable_Object = MibTable
itsIfSdiVbiTable = _ItsIfSdiVbiTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 12)
)
if mibBuilder.loadTexts:
    itsIfSdiVbiTable.setStatus("current")
_ItsIfSdiVbiEntry_Object = MibTableRow
itsIfSdiVbiEntry = _ItsIfSdiVbiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 12, 1)
)
itsIfSdiVbiEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsIfIndex"),
    (0, "NETI-ITS-MIB", "itsIfSdiVbiIndex"),
)
if mibBuilder.loadTexts:
    itsIfSdiVbiEntry.setStatus("current")


class _ItsIfSdiVbiIndex_Type(Integer32):
    """Custom type itsIfSdiVbiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 46),
    )


_ItsIfSdiVbiIndex_Type.__name__ = "Integer32"
_ItsIfSdiVbiIndex_Object = MibTableColumn
itsIfSdiVbiIndex = _ItsIfSdiVbiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 12, 1, 1),
    _ItsIfSdiVbiIndex_Type()
)
itsIfSdiVbiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    itsIfSdiVbiIndex.setStatus("current")
_ItsIfSdiVbiLineNumber_Type = Integer32
_ItsIfSdiVbiLineNumber_Object = MibTableColumn
itsIfSdiVbiLineNumber = _ItsIfSdiVbiLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 12, 1, 2),
    _ItsIfSdiVbiLineNumber_Type()
)
itsIfSdiVbiLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfSdiVbiLineNumber.setStatus("current")


class _ItsIfSdiVbiForward_Type(Integer32):
    """Custom type itsIfSdiVbiForward based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("notApplicable", 0),
          ("yes", 1))
    )


_ItsIfSdiVbiForward_Type.__name__ = "Integer32"
_ItsIfSdiVbiForward_Object = MibTableColumn
itsIfSdiVbiForward = _ItsIfSdiVbiForward_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 12, 1, 3),
    _ItsIfSdiVbiForward_Type()
)
itsIfSdiVbiForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdiVbiForward.setStatus("current")
_ItsIfSdiAncTable_Object = MibTable
itsIfSdiAncTable = _ItsIfSdiAncTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 13)
)
if mibBuilder.loadTexts:
    itsIfSdiAncTable.setStatus("current")
_ItsIfSdiAncEntry_Object = MibTableRow
itsIfSdiAncEntry = _ItsIfSdiAncEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 13, 1)
)
itsIfSdiAncEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsIfIndex"),
    (0, "NETI-ITS-MIB", "itsIfSdiAncIndex"),
)
if mibBuilder.loadTexts:
    itsIfSdiAncEntry.setStatus("current")


class _ItsIfSdiAncIndex_Type(Integer32):
    """Custom type itsIfSdiAncIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ItsIfSdiAncIndex_Type.__name__ = "Integer32"
_ItsIfSdiAncIndex_Object = MibTableColumn
itsIfSdiAncIndex = _ItsIfSdiAncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 13, 1, 1),
    _ItsIfSdiAncIndex_Type()
)
itsIfSdiAncIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    itsIfSdiAncIndex.setStatus("current")
_ItsIfSdiAncDescription_Type = SnmpAdminString
_ItsIfSdiAncDescription_Object = MibTableColumn
itsIfSdiAncDescription = _ItsIfSdiAncDescription_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 13, 1, 2),
    _ItsIfSdiAncDescription_Type()
)
itsIfSdiAncDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfSdiAncDescription.setStatus("current")
_ItsIfSdiAncDid_Type = Unsigned32
_ItsIfSdiAncDid_Object = MibTableColumn
itsIfSdiAncDid = _ItsIfSdiAncDid_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 13, 1, 3),
    _ItsIfSdiAncDid_Type()
)
itsIfSdiAncDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfSdiAncDid.setStatus("current")
_ItsIfSdiAncSdid_Type = Unsigned32
_ItsIfSdiAncSdid_Object = MibTableColumn
itsIfSdiAncSdid = _ItsIfSdiAncSdid_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 13, 1, 4),
    _ItsIfSdiAncSdid_Type()
)
itsIfSdiAncSdid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfSdiAncSdid.setStatus("current")


class _ItsIfSdiAncForward_Type(Integer32):
    """Custom type itsIfSdiAncForward based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("notApplicable", 0),
          ("yes", 1))
    )


_ItsIfSdiAncForward_Type.__name__ = "Integer32"
_ItsIfSdiAncForward_Object = MibTableColumn
itsIfSdiAncForward = _ItsIfSdiAncForward_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 13, 1, 5),
    _ItsIfSdiAncForward_Type()
)
itsIfSdiAncForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfSdiAncForward.setStatus("current")
_ItsIfPs3Table_Object = MibTable
itsIfPs3Table = _ItsIfPs3Table_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 14)
)
if mibBuilder.loadTexts:
    itsIfPs3Table.setStatus("current")
_ItsIfPs3Entry_Object = MibTableRow
itsIfPs3Entry = _ItsIfPs3Entry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 14, 1)
)
itsIfPs3Entry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsIfIndex"),
)
if mibBuilder.loadTexts:
    itsIfPs3Entry.setStatus("current")
_ItsIfPs3DifferentialDelay_Type = Unsigned32
_ItsIfPs3DifferentialDelay_Object = MibTableColumn
itsIfPs3DifferentialDelay = _ItsIfPs3DifferentialDelay_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 14, 1, 1),
    _ItsIfPs3DifferentialDelay_Type()
)
itsIfPs3DifferentialDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfPs3DifferentialDelay.setStatus("current")
_ItsIfPs3DifferentialDelayValid_Type = TruthValue
_ItsIfPs3DifferentialDelayValid_Object = MibTableColumn
itsIfPs3DifferentialDelayValid = _ItsIfPs3DifferentialDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 14, 1, 2),
    _ItsIfPs3DifferentialDelayValid_Type()
)
itsIfPs3DifferentialDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfPs3DifferentialDelayValid.setStatus("current")
_ItsIfPs3AheadInterface_Type = Integer32
_ItsIfPs3AheadInterface_Object = MibTableColumn
itsIfPs3AheadInterface = _ItsIfPs3AheadInterface_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 14, 1, 3),
    _ItsIfPs3AheadInterface_Type()
)
itsIfPs3AheadInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfPs3AheadInterface.setStatus("current")
_ItsIfPs3HitlessProtection_Type = TruthValue
_ItsIfPs3HitlessProtection_Object = MibTableColumn
itsIfPs3HitlessProtection = _ItsIfPs3HitlessProtection_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 14, 1, 4),
    _ItsIfPs3HitlessProtection_Type()
)
itsIfPs3HitlessProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfPs3HitlessProtection.setStatus("current")
_ItsIfPs3ProtectionStatus_Type = ItsProtectionStatus
_ItsIfPs3ProtectionStatus_Object = MibTableColumn
itsIfPs3ProtectionStatus = _ItsIfPs3ProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 14, 1, 5),
    _ItsIfPs3ProtectionStatus_Type()
)
itsIfPs3ProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsIfPs3ProtectionStatus.setStatus("current")


class _ItsIfPs3ExpectedProtectionStatus_Type(ItsProtectionStatus):
    """Custom type itsIfPs3ExpectedProtectionStatus based on ItsProtectionStatus"""


_ItsIfPs3ExpectedProtectionStatus_Object = MibTableColumn
itsIfPs3ExpectedProtectionStatus = _ItsIfPs3ExpectedProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 14, 1, 6),
    _ItsIfPs3ExpectedProtectionStatus_Type()
)
itsIfPs3ExpectedProtectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfPs3ExpectedProtectionStatus.setStatus("current")


class _ItsIfPs3ForceHit_Type(Unsigned32):
    """Custom type itsIfPs3ForceHit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_ItsIfPs3ForceHit_Type.__name__ = "Unsigned32"
_ItsIfPs3ForceHit_Object = MibTableColumn
itsIfPs3ForceHit = _ItsIfPs3ForceHit_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 14, 1, 7),
    _ItsIfPs3ForceHit_Type()
)
itsIfPs3ForceHit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfPs3ForceHit.setStatus("current")
_ItsIfPs3ActiveInterface_Type = Integer32
_ItsIfPs3ActiveInterface_Object = MibTableColumn
itsIfPs3ActiveInterface = _ItsIfPs3ActiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 14, 1, 8),
    _ItsIfPs3ActiveInterface_Type()
)
itsIfPs3ActiveInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfPs3ActiveInterface.setStatus("current")
_ItsIfPs3MaxExpDifferentialDelay_Type = Unsigned32
_ItsIfPs3MaxExpDifferentialDelay_Object = MibTableColumn
itsIfPs3MaxExpDifferentialDelay = _ItsIfPs3MaxExpDifferentialDelay_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 1, 14, 1, 9),
    _ItsIfPs3MaxExpDifferentialDelay_Type()
)
itsIfPs3MaxExpDifferentialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsIfPs3MaxExpDifferentialDelay.setStatus("current")
_ItsSourceGroup_ObjectIdentity = ObjectIdentity
itsSourceGroup = _ItsSourceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2)
)
_ItsSrcTtpLastChange_Type = TimeStamp
_ItsSrcTtpLastChange_Object = MibScalar
itsSrcTtpLastChange = _ItsSrcTtpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 1),
    _ItsSrcTtpLastChange_Type()
)
itsSrcTtpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSrcTtpLastChange.setStatus("current")
_ItsSrcTtpNextIndex_Type = Unsigned32
_ItsSrcTtpNextIndex_Object = MibScalar
itsSrcTtpNextIndex = _ItsSrcTtpNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 2),
    _ItsSrcTtpNextIndex_Type()
)
itsSrcTtpNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSrcTtpNextIndex.setStatus("current")
_ItsSrcTtpTable_Object = MibTable
itsSrcTtpTable = _ItsSrcTtpTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3)
)
if mibBuilder.loadTexts:
    itsSrcTtpTable.setStatus("current")
_ItsSrcTtpEntry_Object = MibTableRow
itsSrcTtpEntry = _ItsSrcTtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1)
)
itsSrcTtpEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsSrcTtpIndex"),
)
if mibBuilder.loadTexts:
    itsSrcTtpEntry.setStatus("current")
_ItsSrcTtpIndex_Type = Unsigned32
_ItsSrcTtpIndex_Object = MibTableColumn
itsSrcTtpIndex = _ItsSrcTtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 1),
    _ItsSrcTtpIndex_Type()
)
itsSrcTtpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    itsSrcTtpIndex.setStatus("current")
_ItsSrcTtpName_Type = SnmpAdminString
_ItsSrcTtpName_Object = MibTableColumn
itsSrcTtpName = _ItsSrcTtpName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 2),
    _ItsSrcTtpName_Type()
)
itsSrcTtpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSrcTtpName.setStatus("current")


class _ItsSrcTtpCustomerId_Type(Unsigned32):
    """Custom type itsSrcTtpCustomerId based on Unsigned32"""
    defaultValue = 0


_ItsSrcTtpCustomerId_Object = MibTableColumn
itsSrcTtpCustomerId = _ItsSrcTtpCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 3),
    _ItsSrcTtpCustomerId_Type()
)
itsSrcTtpCustomerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSrcTtpCustomerId.setStatus("current")


class _ItsSrcTtpPurpose_Type(SnmpAdminString):
    """Custom type itsSrcTtpPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_ItsSrcTtpPurpose_Object = MibTableColumn
itsSrcTtpPurpose = _ItsSrcTtpPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 4),
    _ItsSrcTtpPurpose_Type()
)
itsSrcTtpPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSrcTtpPurpose.setStatus("current")
_ItsSrcTtpLocalIf_Type = Unsigned32
_ItsSrcTtpLocalIf_Object = MibTableColumn
itsSrcTtpLocalIf = _ItsSrcTtpLocalIf_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 5),
    _ItsSrcTtpLocalIf_Type()
)
itsSrcTtpLocalIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSrcTtpLocalIf.setStatus("current")
_ItsSrcTtpLocalDsti_Type = Dsti
_ItsSrcTtpLocalDsti_Object = MibTableColumn
itsSrcTtpLocalDsti = _ItsSrcTtpLocalDsti_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 6),
    _ItsSrcTtpLocalDsti_Type()
)
itsSrcTtpLocalDsti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSrcTtpLocalDsti.setStatus("current")


class _ItsSrcTtpMode_Type(Integer32):
    """Custom type itsSrcTtpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 3),
          ("multicast", 2),
          ("unicast", 1))
    )


_ItsSrcTtpMode_Type.__name__ = "Integer32"
_ItsSrcTtpMode_Object = MibTableColumn
itsSrcTtpMode = _ItsSrcTtpMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 7),
    _ItsSrcTtpMode_Type()
)
itsSrcTtpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    itsSrcTtpMode.setStatus("current")


class _ItsSrcTtpODescription_Type(Unsigned32):
    """Custom type itsSrcTtpODescription based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ItsSrcTtpODescription_Type.__name__ = "Unsigned32"
_ItsSrcTtpODescription_Object = MibTableColumn
itsSrcTtpODescription = _ItsSrcTtpODescription_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 8),
    _ItsSrcTtpODescription_Type()
)
itsSrcTtpODescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSrcTtpODescription.setStatus("current")
_ItsSrcTtpOConnection_Type = Unsigned32
_ItsSrcTtpOConnection_Object = MibTableColumn
itsSrcTtpOConnection = _ItsSrcTtpOConnection_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 9),
    _ItsSrcTtpOConnection_Type()
)
itsSrcTtpOConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSrcTtpOConnection.setStatus("current")
_ItsSrcTtpFailure_Type = SnmpAdminString
_ItsSrcTtpFailure_Object = MibTableColumn
itsSrcTtpFailure = _ItsSrcTtpFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 10),
    _ItsSrcTtpFailure_Type()
)
itsSrcTtpFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSrcTtpFailure.setStatus("current")


class _ItsSrcTtpAdminStatus_Type(Integer32):
    """Custom type itsSrcTtpAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ItsSrcTtpAdminStatus_Type.__name__ = "Integer32"
_ItsSrcTtpAdminStatus_Object = MibTableColumn
itsSrcTtpAdminStatus = _ItsSrcTtpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 11),
    _ItsSrcTtpAdminStatus_Type()
)
itsSrcTtpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSrcTtpAdminStatus.setStatus("current")


class _ItsSrcTtpOperStatus_Type(Integer32):
    """Custom type itsSrcTtpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("partial", 9),
          ("unknown", 4),
          ("up", 1))
    )


_ItsSrcTtpOperStatus_Type.__name__ = "Integer32"
_ItsSrcTtpOperStatus_Object = MibTableColumn
itsSrcTtpOperStatus = _ItsSrcTtpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 12),
    _ItsSrcTtpOperStatus_Type()
)
itsSrcTtpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSrcTtpOperStatus.setStatus("current")
_ItsSrcTtpRowStatus_Type = RowStatus
_ItsSrcTtpRowStatus_Object = MibTableColumn
itsSrcTtpRowStatus = _ItsSrcTtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 3, 1, 13),
    _ItsSrcTtpRowStatus_Type()
)
itsSrcTtpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    itsSrcTtpRowStatus.setStatus("current")
_ItsSrcIndexLookupTable_Object = MibTable
itsSrcIndexLookupTable = _ItsSrcIndexLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 4)
)
if mibBuilder.loadTexts:
    itsSrcIndexLookupTable.setStatus("current")
_ItsSrcIndexLookupEntry_Object = MibTableRow
itsSrcIndexLookupEntry = _ItsSrcIndexLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 4, 1)
)
itsSrcIndexLookupEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsSrcTtpLocalDsti"),
)
if mibBuilder.loadTexts:
    itsSrcIndexLookupEntry.setStatus("current")
_ItsSrcIndexLookupIndex_Type = Unsigned32
_ItsSrcIndexLookupIndex_Object = MibTableColumn
itsSrcIndexLookupIndex = _ItsSrcIndexLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 2, 4, 1, 1),
    _ItsSrcIndexLookupIndex_Type()
)
itsSrcIndexLookupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSrcIndexLookupIndex.setStatus("current")
_ItsSinkGroup_ObjectIdentity = ObjectIdentity
itsSinkGroup = _ItsSinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3)
)
_ItsSnkTtpLastChange_Type = TimeStamp
_ItsSnkTtpLastChange_Object = MibScalar
itsSnkTtpLastChange = _ItsSnkTtpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 1),
    _ItsSnkTtpLastChange_Type()
)
itsSnkTtpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSnkTtpLastChange.setStatus("current")
_ItsSnkTtpNextIndex_Type = Unsigned32
_ItsSnkTtpNextIndex_Object = MibScalar
itsSnkTtpNextIndex = _ItsSnkTtpNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 2),
    _ItsSnkTtpNextIndex_Type()
)
itsSnkTtpNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSnkTtpNextIndex.setStatus("current")
_ItsSnkTtpTable_Object = MibTable
itsSnkTtpTable = _ItsSnkTtpTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3)
)
if mibBuilder.loadTexts:
    itsSnkTtpTable.setStatus("current")
_ItsSnkTtpEntry_Object = MibTableRow
itsSnkTtpEntry = _ItsSnkTtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1)
)
itsSnkTtpEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsSnkTtpIndex"),
)
if mibBuilder.loadTexts:
    itsSnkTtpEntry.setStatus("current")
_ItsSnkTtpIndex_Type = Unsigned32
_ItsSnkTtpIndex_Object = MibTableColumn
itsSnkTtpIndex = _ItsSnkTtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 1),
    _ItsSnkTtpIndex_Type()
)
itsSnkTtpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    itsSnkTtpIndex.setStatus("current")
_ItsSnkTtpName_Type = SnmpAdminString
_ItsSnkTtpName_Object = MibTableColumn
itsSnkTtpName = _ItsSnkTtpName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 2),
    _ItsSnkTtpName_Type()
)
itsSnkTtpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSnkTtpName.setStatus("current")


class _ItsSnkTtpCustomerId_Type(Unsigned32):
    """Custom type itsSnkTtpCustomerId based on Unsigned32"""
    defaultValue = 0


_ItsSnkTtpCustomerId_Object = MibTableColumn
itsSnkTtpCustomerId = _ItsSnkTtpCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 3),
    _ItsSnkTtpCustomerId_Type()
)
itsSnkTtpCustomerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSnkTtpCustomerId.setStatus("current")


class _ItsSnkTtpPurpose_Type(SnmpAdminString):
    """Custom type itsSnkTtpPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_ItsSnkTtpPurpose_Object = MibTableColumn
itsSnkTtpPurpose = _ItsSnkTtpPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 4),
    _ItsSnkTtpPurpose_Type()
)
itsSnkTtpPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSnkTtpPurpose.setStatus("current")
_ItsSnkTtpLocalIf_Type = Unsigned32
_ItsSnkTtpLocalIf_Object = MibTableColumn
itsSnkTtpLocalIf = _ItsSnkTtpLocalIf_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 5),
    _ItsSnkTtpLocalIf_Type()
)
itsSnkTtpLocalIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSnkTtpLocalIf.setStatus("current")
_ItsSnkTtpLocalDsti_Type = Dsti
_ItsSnkTtpLocalDsti_Object = MibTableColumn
itsSnkTtpLocalDsti = _ItsSnkTtpLocalDsti_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 6),
    _ItsSnkTtpLocalDsti_Type()
)
itsSnkTtpLocalDsti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSnkTtpLocalDsti.setStatus("current")


class _ItsSnkTtpPSActiveChannel_Type(Integer32):
    """Custom type itsSnkTtpPSActiveChannel based on Integer32"""
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
          ("primary", 1),
          ("secondary", 2))
    )


_ItsSnkTtpPSActiveChannel_Type.__name__ = "Integer32"
_ItsSnkTtpPSActiveChannel_Object = MibTableColumn
itsSnkTtpPSActiveChannel = _ItsSnkTtpPSActiveChannel_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 7),
    _ItsSnkTtpPSActiveChannel_Type()
)
itsSnkTtpPSActiveChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSnkTtpPSActiveChannel.setStatus("current")


class _ItsSnkTtpSuppressAlarm_Type(Integer32):
    """Custom type itsSnkTtpSuppressAlarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("none", 1),
          ("notSupported", 0),
          ("warning", 2))
    )


_ItsSnkTtpSuppressAlarm_Type.__name__ = "Integer32"
_ItsSnkTtpSuppressAlarm_Object = MibTableColumn
itsSnkTtpSuppressAlarm = _ItsSnkTtpSuppressAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 8),
    _ItsSnkTtpSuppressAlarm_Type()
)
itsSnkTtpSuppressAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSnkTtpSuppressAlarm.setStatus("current")
_ItsSnkTtpTConnection_Type = Unsigned32
_ItsSnkTtpTConnection_Object = MibTableColumn
itsSnkTtpTConnection = _ItsSnkTtpTConnection_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 9),
    _ItsSnkTtpTConnection_Type()
)
itsSnkTtpTConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSnkTtpTConnection.setStatus("current")


class _ItsSnkTtpDefects_Type(Bits):
    """Custom type itsSnkTtpDefects based on Bits"""
    namedValues = NamedValues(
        *(("ais", 2),
          ("lof", 1),
          ("lop", 3),
          ("los", 0))
    )

_ItsSnkTtpDefects_Type.__name__ = "Bits"
_ItsSnkTtpDefects_Object = MibTableColumn
itsSnkTtpDefects = _ItsSnkTtpDefects_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 10),
    _ItsSnkTtpDefects_Type()
)
itsSnkTtpDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSnkTtpDefects.setStatus("current")
_ItsSnkTtpFailure_Type = SnmpAdminString
_ItsSnkTtpFailure_Object = MibTableColumn
itsSnkTtpFailure = _ItsSnkTtpFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 11),
    _ItsSnkTtpFailure_Type()
)
itsSnkTtpFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSnkTtpFailure.setStatus("current")
_ItsSnkTtpPMReference_Type = RowPointer
_ItsSnkTtpPMReference_Object = MibTableColumn
itsSnkTtpPMReference = _ItsSnkTtpPMReference_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 12),
    _ItsSnkTtpPMReference_Type()
)
itsSnkTtpPMReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSnkTtpPMReference.setStatus("current")


class _ItsSnkTtpAdminStatus_Type(Integer32):
    """Custom type itsSnkTtpAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ItsSnkTtpAdminStatus_Type.__name__ = "Integer32"
_ItsSnkTtpAdminStatus_Object = MibTableColumn
itsSnkTtpAdminStatus = _ItsSnkTtpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 13),
    _ItsSnkTtpAdminStatus_Type()
)
itsSnkTtpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSnkTtpAdminStatus.setStatus("current")


class _ItsSnkTtpOperStatus_Type(Integer32):
    """Custom type itsSnkTtpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("up", 1))
    )


_ItsSnkTtpOperStatus_Type.__name__ = "Integer32"
_ItsSnkTtpOperStatus_Object = MibTableColumn
itsSnkTtpOperStatus = _ItsSnkTtpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 14),
    _ItsSnkTtpOperStatus_Type()
)
itsSnkTtpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSnkTtpOperStatus.setStatus("current")
_ItsSnkTtpRowStatus_Type = RowStatus
_ItsSnkTtpRowStatus_Object = MibTableColumn
itsSnkTtpRowStatus = _ItsSnkTtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 15),
    _ItsSnkTtpRowStatus_Type()
)
itsSnkTtpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    itsSnkTtpRowStatus.setStatus("current")


class _ItsSnkTtpTConnection2_Type(Integer32):
    """Custom type itsSnkTtpTConnection2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_ItsSnkTtpTConnection2_Type.__name__ = "Integer32"
_ItsSnkTtpTConnection2_Object = MibTableColumn
itsSnkTtpTConnection2 = _ItsSnkTtpTConnection2_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 16),
    _ItsSnkTtpTConnection2_Type()
)
itsSnkTtpTConnection2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSnkTtpTConnection2.setStatus("current")


class _ItsSnkTtpPSAllow_Type(TruthValue):
    """Custom type itsSnkTtpPSAllow based on TruthValue"""


_ItsSnkTtpPSAllow_Object = MibTableColumn
itsSnkTtpPSAllow = _ItsSnkTtpPSAllow_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 3, 1, 17),
    _ItsSnkTtpPSAllow_Type()
)
itsSnkTtpPSAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsSnkTtpPSAllow.setStatus("current")
_ItsSnkIndexLookupTable_Object = MibTable
itsSnkIndexLookupTable = _ItsSnkIndexLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 4)
)
if mibBuilder.loadTexts:
    itsSnkIndexLookupTable.setStatus("current")
_ItsSnkIndexLookupEntry_Object = MibTableRow
itsSnkIndexLookupEntry = _ItsSnkIndexLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 4, 1)
)
itsSnkIndexLookupEntry.setIndexNames(
    (0, "NETI-ITS-MIB", "itsSnkTtpLocalDsti"),
)
if mibBuilder.loadTexts:
    itsSnkIndexLookupEntry.setStatus("current")
_ItsSnkIndexLookupIndex_Type = Unsigned32
_ItsSnkIndexLookupIndex_Object = MibTableColumn
itsSnkIndexLookupIndex = _ItsSnkIndexLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 16, 1, 3, 4, 1, 1),
    _ItsSnkIndexLookupIndex_Type()
)
itsSnkIndexLookupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsSnkIndexLookupIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETI-ITS-MIB",
    **{"ItsTtpIndexList": ItsTtpIndexList,
       "ItsProtectionStatus": ItsProtectionStatus,
       "netiItsMIB": netiItsMIB,
       "itsObjects": itsObjects,
       "itsIfGroup": itsIfGroup,
       "itsIfLastChange": itsIfLastChange,
       "itsIfTable": itsIfTable,
       "itsIfEntry": itsIfEntry,
       "itsIfIndex": itsIfIndex,
       "itsIfIfIndex": itsIfIfIndex,
       "itsIfName": itsIfName,
       "itsIfDescr": itsIfDescr,
       "itsIfSpeed": itsIfSpeed,
       "itsIfSuppressAlarm": itsIfSuppressAlarm,
       "itsIfLoopMode": itsIfLoopMode,
       "itsIfLoopTime": itsIfLoopTime,
       "itsIfCapabilities": itsIfCapabilities,
       "itsIfProperties": itsIfProperties,
       "itsIfDefects": itsIfDefects,
       "itsIfFailure": itsIfFailure,
       "itsIfPMReference": itsIfPMReference,
       "itsIfOperStatus": itsIfOperStatus,
       "itsIfTxMuteOnFault": itsIfTxMuteOnFault,
       "itsIfPurpose": itsIfPurpose,
       "itsIfInterfaceType": itsIfInterfaceType,
       "itsIfMembersSrc": itsIfMembersSrc,
       "itsIfMembersSnk": itsIfMembersSnk,
       "itsIfPdhTable": itsIfPdhTable,
       "itsIfPdhEntry": itsIfPdhEntry,
       "itsIfPdhSignal": itsIfPdhSignal,
       "itsIfPdhFraming": itsIfPdhFraming,
       "itsIfSdhTable": itsIfSdhTable,
       "itsIfSdhEntry": itsIfSdhEntry,
       "itsIfSdhTiming": itsIfSdhTiming,
       "itsIfSdhMode": itsIfSdhMode,
       "itsIfSdhSs": itsIfSdhSs,
       "itsIfSdhS1": itsIfSdhS1,
       "itsIfSdhSoh": itsIfSdhSoh,
       "itsIfSdhPoh": itsIfSdhPoh,
       "itsIfSdhJc": itsIfSdhJc,
       "itsIfDvbTable": itsIfDvbTable,
       "itsIfDvbEntry": itsIfDvbEntry,
       "itsIfDvbFormat": itsIfDvbFormat,
       "itsIfDvbOutputMode": itsIfDvbOutputMode,
       "itsIfAesTable": itsIfAesTable,
       "itsIfAesEntry": itsIfAesEntry,
       "itsIfAesIsTimingProvider": itsIfAesIsTimingProvider,
       "itsIfAesReference": itsIfAesReference,
       "itsIfSdiTable": itsIfSdiTable,
       "itsIfSdiEntry": itsIfSdiEntry,
       "itsIfSdiFormat": itsIfSdiFormat,
       "itsIfSdiAutoSense": itsIfSdiAutoSense,
       "itsIfSdiIsTimingProvider": itsIfSdiIsTimingProvider,
       "itsIfSdiReference": itsIfSdiReference,
       "itsIfSdiFsVDelay": itsIfSdiFsVDelay,
       "itsIfSdiFsHDelay": itsIfSdiFsHDelay,
       "itsIfSdiFsDelay": itsIfSdiFsDelay,
       "itsIfMonTable": itsIfMonTable,
       "itsIfMonEntry": itsIfMonEntry,
       "itsIfMonMonitoredInterface": itsIfMonMonitoredInterface,
       "itsIfMonDirection": itsIfMonDirection,
       "itsIfEnableButton": itsIfEnableButton,
       "itsIfJ2kTable": itsIfJ2kTable,
       "itsIfJ2kEntry": itsIfJ2kEntry,
       "itsIfJ2kEncoderEnable": itsIfJ2kEncoderEnable,
       "itsIfJ2kDecoderActive": itsIfJ2kDecoderActive,
       "itsIfJ2kSignalFormat": itsIfJ2kSignalFormat,
       "itsIfJ2kRateVideo": itsIfJ2kRateVideo,
       "itsIfJ2kRateVideoMax": itsIfJ2kRateVideoMax,
       "itsIfJ2kRateVbi": itsIfJ2kRateVbi,
       "itsIfJ2kRateAnc": itsIfJ2kRateAnc,
       "itsIfJ2kRateAudio": itsIfJ2kRateAudio,
       "itsIfJ2kAudioSampleSize": itsIfJ2kAudioSampleSize,
       "itsIfJ2kReduceAudioTransportBitrate": itsIfJ2kReduceAudioTransportBitrate,
       "itsIfSdiAudioTable": itsIfSdiAudioTable,
       "itsIfSdiAudioEntry": itsIfSdiAudioEntry,
       "itsIfSdiAudioIndex": itsIfSdiAudioIndex,
       "itsIfSdiAudioForward": itsIfSdiAudioForward,
       "itsIfSdiVbiTable": itsIfSdiVbiTable,
       "itsIfSdiVbiEntry": itsIfSdiVbiEntry,
       "itsIfSdiVbiIndex": itsIfSdiVbiIndex,
       "itsIfSdiVbiLineNumber": itsIfSdiVbiLineNumber,
       "itsIfSdiVbiForward": itsIfSdiVbiForward,
       "itsIfSdiAncTable": itsIfSdiAncTable,
       "itsIfSdiAncEntry": itsIfSdiAncEntry,
       "itsIfSdiAncIndex": itsIfSdiAncIndex,
       "itsIfSdiAncDescription": itsIfSdiAncDescription,
       "itsIfSdiAncDid": itsIfSdiAncDid,
       "itsIfSdiAncSdid": itsIfSdiAncSdid,
       "itsIfSdiAncForward": itsIfSdiAncForward,
       "itsIfPs3Table": itsIfPs3Table,
       "itsIfPs3Entry": itsIfPs3Entry,
       "itsIfPs3DifferentialDelay": itsIfPs3DifferentialDelay,
       "itsIfPs3DifferentialDelayValid": itsIfPs3DifferentialDelayValid,
       "itsIfPs3AheadInterface": itsIfPs3AheadInterface,
       "itsIfPs3HitlessProtection": itsIfPs3HitlessProtection,
       "itsIfPs3ProtectionStatus": itsIfPs3ProtectionStatus,
       "itsIfPs3ExpectedProtectionStatus": itsIfPs3ExpectedProtectionStatus,
       "itsIfPs3ForceHit": itsIfPs3ForceHit,
       "itsIfPs3ActiveInterface": itsIfPs3ActiveInterface,
       "itsIfPs3MaxExpDifferentialDelay": itsIfPs3MaxExpDifferentialDelay,
       "itsSourceGroup": itsSourceGroup,
       "itsSrcTtpLastChange": itsSrcTtpLastChange,
       "itsSrcTtpNextIndex": itsSrcTtpNextIndex,
       "itsSrcTtpTable": itsSrcTtpTable,
       "itsSrcTtpEntry": itsSrcTtpEntry,
       "itsSrcTtpIndex": itsSrcTtpIndex,
       "itsSrcTtpName": itsSrcTtpName,
       "itsSrcTtpCustomerId": itsSrcTtpCustomerId,
       "itsSrcTtpPurpose": itsSrcTtpPurpose,
       "itsSrcTtpLocalIf": itsSrcTtpLocalIf,
       "itsSrcTtpLocalDsti": itsSrcTtpLocalDsti,
       "itsSrcTtpMode": itsSrcTtpMode,
       "itsSrcTtpODescription": itsSrcTtpODescription,
       "itsSrcTtpOConnection": itsSrcTtpOConnection,
       "itsSrcTtpFailure": itsSrcTtpFailure,
       "itsSrcTtpAdminStatus": itsSrcTtpAdminStatus,
       "itsSrcTtpOperStatus": itsSrcTtpOperStatus,
       "itsSrcTtpRowStatus": itsSrcTtpRowStatus,
       "itsSrcIndexLookupTable": itsSrcIndexLookupTable,
       "itsSrcIndexLookupEntry": itsSrcIndexLookupEntry,
       "itsSrcIndexLookupIndex": itsSrcIndexLookupIndex,
       "itsSinkGroup": itsSinkGroup,
       "itsSnkTtpLastChange": itsSnkTtpLastChange,
       "itsSnkTtpNextIndex": itsSnkTtpNextIndex,
       "itsSnkTtpTable": itsSnkTtpTable,
       "itsSnkTtpEntry": itsSnkTtpEntry,
       "itsSnkTtpIndex": itsSnkTtpIndex,
       "itsSnkTtpName": itsSnkTtpName,
       "itsSnkTtpCustomerId": itsSnkTtpCustomerId,
       "itsSnkTtpPurpose": itsSnkTtpPurpose,
       "itsSnkTtpLocalIf": itsSnkTtpLocalIf,
       "itsSnkTtpLocalDsti": itsSnkTtpLocalDsti,
       "itsSnkTtpPSActiveChannel": itsSnkTtpPSActiveChannel,
       "itsSnkTtpSuppressAlarm": itsSnkTtpSuppressAlarm,
       "itsSnkTtpTConnection": itsSnkTtpTConnection,
       "itsSnkTtpDefects": itsSnkTtpDefects,
       "itsSnkTtpFailure": itsSnkTtpFailure,
       "itsSnkTtpPMReference": itsSnkTtpPMReference,
       "itsSnkTtpAdminStatus": itsSnkTtpAdminStatus,
       "itsSnkTtpOperStatus": itsSnkTtpOperStatus,
       "itsSnkTtpRowStatus": itsSnkTtpRowStatus,
       "itsSnkTtpTConnection2": itsSnkTtpTConnection2,
       "itsSnkTtpPSAllow": itsSnkTtpPSAllow,
       "itsSnkIndexLookupTable": itsSnkIndexLookupTable,
       "itsSnkIndexLookupEntry": itsSnkIndexLookupEntry,
       "itsSnkIndexLookupIndex": itsSnkIndexLookupIndex}
)
