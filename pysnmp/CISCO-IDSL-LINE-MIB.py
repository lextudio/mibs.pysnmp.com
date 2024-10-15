# SNMP MIB module (CISCO-IDSL-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IDSL-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:20 2024
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

(AdslLineProfileName,
 adslLineConfProfileName) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "AdslLineProfileName",
    "adslLineConfProfileName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

ciscoIdslLineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 154)
)
ciscoIdslLineMIB.setRevisions(
        ("2000-01-20 00:36",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IdslPerfTimeElapsed(Gauge32, TextualConvention):
    status = "current"


class IdslPerfCurrDayCount(Gauge32, TextualConvention):
    status = "current"


class IdslPerfPrevDayCount(Gauge32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoIdslLineMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIdslLineMIBObjects = _CiscoIdslLineMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1)
)
_CIdslLineTable_Object = MibTable
cIdslLineTable = _CIdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 1)
)
if mibBuilder.loadTexts:
    cIdslLineTable.setStatus("current")
_CIdslLineEntry_Object = MibTableRow
cIdslLineEntry = _CIdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 1, 1)
)
cIdslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cIdslLineEntry.setStatus("current")
_CIdslLineSpecific_Type = VariablePointer
_CIdslLineSpecific_Object = MibTableColumn
cIdslLineSpecific = _CIdslLineSpecific_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 1, 1, 1),
    _CIdslLineSpecific_Type()
)
cIdslLineSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslLineSpecific.setStatus("current")
_CIdslLineConfProfile_Type = AdslLineProfileName
_CIdslLineConfProfile_Object = MibTableColumn
cIdslLineConfProfile = _CIdslLineConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 1, 1, 2),
    _CIdslLineConfProfile_Type()
)
cIdslLineConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIdslLineConfProfile.setStatus("current")
_CIdslLineAlarmConfProfile_Type = AdslLineProfileName
_CIdslLineAlarmConfProfile_Object = MibTableColumn
cIdslLineAlarmConfProfile = _CIdslLineAlarmConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 1, 1, 3),
    _CIdslLineAlarmConfProfile_Type()
)
cIdslLineAlarmConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIdslLineAlarmConfProfile.setStatus("current")
_CIdslItucPhysTable_Object = MibTable
cIdslItucPhysTable = _CIdslItucPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 2)
)
if mibBuilder.loadTexts:
    cIdslItucPhysTable.setStatus("current")
_CIdslItucPhysEntry_Object = MibTableRow
cIdslItucPhysEntry = _CIdslItucPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 2, 1)
)
cIdslItucPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cIdslItucPhysEntry.setStatus("current")
_CIdslItucInvSerialNumber_Type = SnmpAdminString
_CIdslItucInvSerialNumber_Object = MibTableColumn
cIdslItucInvSerialNumber = _CIdslItucInvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 2, 1, 1),
    _CIdslItucInvSerialNumber_Type()
)
cIdslItucInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucInvSerialNumber.setStatus("current")
_CIdslItucInvVendorId_Type = SnmpAdminString
_CIdslItucInvVendorId_Object = MibTableColumn
cIdslItucInvVendorId = _CIdslItucInvVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 2, 1, 2),
    _CIdslItucInvVendorId_Type()
)
cIdslItucInvVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucInvVendorId.setStatus("current")
_CIdslItucInvVersionNumber_Type = SnmpAdminString
_CIdslItucInvVersionNumber_Object = MibTableColumn
cIdslItucInvVersionNumber = _CIdslItucInvVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 2, 1, 3),
    _CIdslItucInvVersionNumber_Type()
)
cIdslItucInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucInvVersionNumber.setStatus("current")


class _CIdslItucStatus_Type(Integer32):
    """Custom type cIdslItucStatus based on Integer32"""
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
        *(("dslSync", 2),
          ("loopDown", 1),
          ("loopUp", 3),
          ("loopUpLmiActive", 4))
    )


_CIdslItucStatus_Type.__name__ = "Integer32"
_CIdslItucStatus_Object = MibTableColumn
cIdslItucStatus = _CIdslItucStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 2, 1, 4),
    _CIdslItucStatus_Type()
)
cIdslItucStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucStatus.setStatus("current")
_CIdslItucPerfDataTable_Object = MibTable
cIdslItucPerfDataTable = _CIdslItucPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6)
)
if mibBuilder.loadTexts:
    cIdslItucPerfDataTable.setStatus("current")
_CIdslItucPerfDataEntry_Object = MibTableRow
cIdslItucPerfDataEntry = _CIdslItucPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1)
)
cIdslItucPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cIdslItucPerfDataEntry.setStatus("current")
_CIdslItucPerfCVs_Type = Counter32
_CIdslItucPerfCVs_Object = MibTableColumn
cIdslItucPerfCVs = _CIdslItucPerfCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 1),
    _CIdslItucPerfCVs_Type()
)
cIdslItucPerfCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCVs.setStatus("current")
_CIdslItucPerfESs_Type = Counter32
_CIdslItucPerfESs_Object = MibTableColumn
cIdslItucPerfESs = _CIdslItucPerfESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 2),
    _CIdslItucPerfESs_Type()
)
cIdslItucPerfESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfESs.setStatus("current")
_CIdslItucPerfSESs_Type = Counter32
_CIdslItucPerfSESs_Object = MibTableColumn
cIdslItucPerfSESs = _CIdslItucPerfSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 3),
    _CIdslItucPerfSESs_Type()
)
cIdslItucPerfSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfSESs.setStatus("current")
_CIdslItucPerfHdlcCVs_Type = Counter32
_CIdslItucPerfHdlcCVs_Object = MibTableColumn
cIdslItucPerfHdlcCVs = _CIdslItucPerfHdlcCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 4),
    _CIdslItucPerfHdlcCVs_Type()
)
cIdslItucPerfHdlcCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfHdlcCVs.setStatus("current")
_CIdslItucPerfHdlcAborts_Type = Counter32
_CIdslItucPerfHdlcAborts_Object = MibTableColumn
cIdslItucPerfHdlcAborts = _CIdslItucPerfHdlcAborts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 5),
    _CIdslItucPerfHdlcAborts_Type()
)
cIdslItucPerfHdlcAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfHdlcAborts.setStatus("current")
_CIdslItucPerfHdlcAligns_Type = Counter32
_CIdslItucPerfHdlcAligns_Object = MibTableColumn
cIdslItucPerfHdlcAligns = _CIdslItucPerfHdlcAligns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 6),
    _CIdslItucPerfHdlcAligns_Type()
)
cIdslItucPerfHdlcAligns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfHdlcAligns.setStatus("current")
_CIdslItucPerfHdlcShorts_Type = Counter32
_CIdslItucPerfHdlcShorts_Object = MibTableColumn
cIdslItucPerfHdlcShorts = _CIdslItucPerfHdlcShorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 7),
    _CIdslItucPerfHdlcShorts_Type()
)
cIdslItucPerfHdlcShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfHdlcShorts.setStatus("current")
_CIdslItucPerfHdlcLongs_Type = Counter32
_CIdslItucPerfHdlcLongs_Object = MibTableColumn
cIdslItucPerfHdlcLongs = _CIdslItucPerfHdlcLongs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 8),
    _CIdslItucPerfHdlcLongs_Type()
)
cIdslItucPerfHdlcLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfHdlcLongs.setStatus("current")


class _CIdslItucPerfValidIntervals_Type(Integer32):
    """Custom type cIdslItucPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CIdslItucPerfValidIntervals_Type.__name__ = "Integer32"
_CIdslItucPerfValidIntervals_Object = MibTableColumn
cIdslItucPerfValidIntervals = _CIdslItucPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 9),
    _CIdslItucPerfValidIntervals_Type()
)
cIdslItucPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfValidIntervals.setStatus("current")


class _CIdslItucPerfInvalidIntervals_Type(Integer32):
    """Custom type cIdslItucPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CIdslItucPerfInvalidIntervals_Type.__name__ = "Integer32"
_CIdslItucPerfInvalidIntervals_Object = MibTableColumn
cIdslItucPerfInvalidIntervals = _CIdslItucPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 10),
    _CIdslItucPerfInvalidIntervals_Type()
)
cIdslItucPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfInvalidIntervals.setStatus("current")
_CIdslItucPerfCurr15MinElapsed_Type = IdslPerfTimeElapsed
_CIdslItucPerfCurr15MinElapsed_Object = MibTableColumn
cIdslItucPerfCurr15MinElapsed = _CIdslItucPerfCurr15MinElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 11),
    _CIdslItucPerfCurr15MinElapsed_Type()
)
cIdslItucPerfCurr15MinElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr15MinElapsed.setStatus("current")
_CIdslItucPerfCurr15MinCVs_Type = PerfCurrentCount
_CIdslItucPerfCurr15MinCVs_Object = MibTableColumn
cIdslItucPerfCurr15MinCVs = _CIdslItucPerfCurr15MinCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 12),
    _CIdslItucPerfCurr15MinCVs_Type()
)
cIdslItucPerfCurr15MinCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr15MinCVs.setStatus("current")
_CIdslItucPerfCurr15MinESs_Type = PerfCurrentCount
_CIdslItucPerfCurr15MinESs_Object = MibTableColumn
cIdslItucPerfCurr15MinESs = _CIdslItucPerfCurr15MinESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 13),
    _CIdslItucPerfCurr15MinESs_Type()
)
cIdslItucPerfCurr15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr15MinESs.setStatus("current")
_CIdslItucPerfCurr15MinSESs_Type = PerfCurrentCount
_CIdslItucPerfCurr15MinSESs_Object = MibTableColumn
cIdslItucPerfCurr15MinSESs = _CIdslItucPerfCurr15MinSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 14),
    _CIdslItucPerfCurr15MinSESs_Type()
)
cIdslItucPerfCurr15MinSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr15MinSESs.setStatus("current")
_CIdslItucPerfCurr15MinHdlcCVs_Type = PerfCurrentCount
_CIdslItucPerfCurr15MinHdlcCVs_Object = MibTableColumn
cIdslItucPerfCurr15MinHdlcCVs = _CIdslItucPerfCurr15MinHdlcCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 15),
    _CIdslItucPerfCurr15MinHdlcCVs_Type()
)
cIdslItucPerfCurr15MinHdlcCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr15MinHdlcCVs.setStatus("current")
_CIdslItucPerfCurr15MinHdlcAborts_Type = PerfCurrentCount
_CIdslItucPerfCurr15MinHdlcAborts_Object = MibTableColumn
cIdslItucPerfCurr15MinHdlcAborts = _CIdslItucPerfCurr15MinHdlcAborts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 16),
    _CIdslItucPerfCurr15MinHdlcAborts_Type()
)
cIdslItucPerfCurr15MinHdlcAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr15MinHdlcAborts.setStatus("current")
_CIdslItucPerfCurr15MinHdlcAligns_Type = PerfCurrentCount
_CIdslItucPerfCurr15MinHdlcAligns_Object = MibTableColumn
cIdslItucPerfCurr15MinHdlcAligns = _CIdslItucPerfCurr15MinHdlcAligns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 17),
    _CIdslItucPerfCurr15MinHdlcAligns_Type()
)
cIdslItucPerfCurr15MinHdlcAligns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr15MinHdlcAligns.setStatus("current")
_CIdslItucPerfCurr15MinHdlcShorts_Type = PerfCurrentCount
_CIdslItucPerfCurr15MinHdlcShorts_Object = MibTableColumn
cIdslItucPerfCurr15MinHdlcShorts = _CIdslItucPerfCurr15MinHdlcShorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 18),
    _CIdslItucPerfCurr15MinHdlcShorts_Type()
)
cIdslItucPerfCurr15MinHdlcShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr15MinHdlcShorts.setStatus("current")
_CIdslItucPerfCurr15MinHdlcLongs_Type = PerfCurrentCount
_CIdslItucPerfCurr15MinHdlcLongs_Object = MibTableColumn
cIdslItucPerfCurr15MinHdlcLongs = _CIdslItucPerfCurr15MinHdlcLongs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 19),
    _CIdslItucPerfCurr15MinHdlcLongs_Type()
)
cIdslItucPerfCurr15MinHdlcLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr15MinHdlcLongs.setStatus("current")
_CIdslItucPerfCurr1DayElapsed_Type = IdslPerfTimeElapsed
_CIdslItucPerfCurr1DayElapsed_Object = MibTableColumn
cIdslItucPerfCurr1DayElapsed = _CIdslItucPerfCurr1DayElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 20),
    _CIdslItucPerfCurr1DayElapsed_Type()
)
cIdslItucPerfCurr1DayElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr1DayElapsed.setStatus("current")
_CIdslItucPerfCurr1DayCVs_Type = IdslPerfCurrDayCount
_CIdslItucPerfCurr1DayCVs_Object = MibTableColumn
cIdslItucPerfCurr1DayCVs = _CIdslItucPerfCurr1DayCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 21),
    _CIdslItucPerfCurr1DayCVs_Type()
)
cIdslItucPerfCurr1DayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr1DayCVs.setStatus("current")
_CIdslItucPerfCurr1DayESs_Type = IdslPerfCurrDayCount
_CIdslItucPerfCurr1DayESs_Object = MibTableColumn
cIdslItucPerfCurr1DayESs = _CIdslItucPerfCurr1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 22),
    _CIdslItucPerfCurr1DayESs_Type()
)
cIdslItucPerfCurr1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr1DayESs.setStatus("current")
_CIdslItucPerfCurr1DaySESs_Type = IdslPerfCurrDayCount
_CIdslItucPerfCurr1DaySESs_Object = MibTableColumn
cIdslItucPerfCurr1DaySESs = _CIdslItucPerfCurr1DaySESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 23),
    _CIdslItucPerfCurr1DaySESs_Type()
)
cIdslItucPerfCurr1DaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr1DaySESs.setStatus("current")
_CIdslItucPerfCurr1DayHdlcCVs_Type = IdslPerfCurrDayCount
_CIdslItucPerfCurr1DayHdlcCVs_Object = MibTableColumn
cIdslItucPerfCurr1DayHdlcCVs = _CIdslItucPerfCurr1DayHdlcCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 24),
    _CIdslItucPerfCurr1DayHdlcCVs_Type()
)
cIdslItucPerfCurr1DayHdlcCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr1DayHdlcCVs.setStatus("current")
_CIdslItucPerfCurr1DayHdlcAborts_Type = IdslPerfCurrDayCount
_CIdslItucPerfCurr1DayHdlcAborts_Object = MibTableColumn
cIdslItucPerfCurr1DayHdlcAborts = _CIdslItucPerfCurr1DayHdlcAborts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 25),
    _CIdslItucPerfCurr1DayHdlcAborts_Type()
)
cIdslItucPerfCurr1DayHdlcAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr1DayHdlcAborts.setStatus("current")
_CIdslItucPerfCurr1DayHdlcAligns_Type = IdslPerfCurrDayCount
_CIdslItucPerfCurr1DayHdlcAligns_Object = MibTableColumn
cIdslItucPerfCurr1DayHdlcAligns = _CIdslItucPerfCurr1DayHdlcAligns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 26),
    _CIdslItucPerfCurr1DayHdlcAligns_Type()
)
cIdslItucPerfCurr1DayHdlcAligns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr1DayHdlcAligns.setStatus("current")
_CIdslItucPerfCurr1DayHdlcShorts_Type = IdslPerfCurrDayCount
_CIdslItucPerfCurr1DayHdlcShorts_Object = MibTableColumn
cIdslItucPerfCurr1DayHdlcShorts = _CIdslItucPerfCurr1DayHdlcShorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 27),
    _CIdslItucPerfCurr1DayHdlcShorts_Type()
)
cIdslItucPerfCurr1DayHdlcShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr1DayHdlcShorts.setStatus("current")
_CIdslItucPerfCurr1DayHdlcLongs_Type = IdslPerfCurrDayCount
_CIdslItucPerfCurr1DayHdlcLongs_Object = MibTableColumn
cIdslItucPerfCurr1DayHdlcLongs = _CIdslItucPerfCurr1DayHdlcLongs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 28),
    _CIdslItucPerfCurr1DayHdlcLongs_Type()
)
cIdslItucPerfCurr1DayHdlcLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfCurr1DayHdlcLongs.setStatus("current")


class _CIdslItucPerfPrev1DayMoniSecs_Type(Integer32):
    """Custom type cIdslItucPerfPrev1DayMoniSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CIdslItucPerfPrev1DayMoniSecs_Type.__name__ = "Integer32"
_CIdslItucPerfPrev1DayMoniSecs_Object = MibTableColumn
cIdslItucPerfPrev1DayMoniSecs = _CIdslItucPerfPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 29),
    _CIdslItucPerfPrev1DayMoniSecs_Type()
)
cIdslItucPerfPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfPrev1DayMoniSecs.setStatus("current")
_CIdslItucPerfPrev1DayCVs_Type = IdslPerfPrevDayCount
_CIdslItucPerfPrev1DayCVs_Object = MibTableColumn
cIdslItucPerfPrev1DayCVs = _CIdslItucPerfPrev1DayCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 30),
    _CIdslItucPerfPrev1DayCVs_Type()
)
cIdslItucPerfPrev1DayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfPrev1DayCVs.setStatus("current")
_CIdslItucPerfPrev1DayESs_Type = IdslPerfPrevDayCount
_CIdslItucPerfPrev1DayESs_Object = MibTableColumn
cIdslItucPerfPrev1DayESs = _CIdslItucPerfPrev1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 31),
    _CIdslItucPerfPrev1DayESs_Type()
)
cIdslItucPerfPrev1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfPrev1DayESs.setStatus("current")
_CIdslItucPerfPrev1DaySESs_Type = IdslPerfPrevDayCount
_CIdslItucPerfPrev1DaySESs_Object = MibTableColumn
cIdslItucPerfPrev1DaySESs = _CIdslItucPerfPrev1DaySESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 32),
    _CIdslItucPerfPrev1DaySESs_Type()
)
cIdslItucPerfPrev1DaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfPrev1DaySESs.setStatus("current")
_CIdslItucPerfPrev1DayHdlcCVs_Type = IdslPerfPrevDayCount
_CIdslItucPerfPrev1DayHdlcCVs_Object = MibTableColumn
cIdslItucPerfPrev1DayHdlcCVs = _CIdslItucPerfPrev1DayHdlcCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 33),
    _CIdslItucPerfPrev1DayHdlcCVs_Type()
)
cIdslItucPerfPrev1DayHdlcCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfPrev1DayHdlcCVs.setStatus("current")
_CIdslItucPerfPrev1DayHdlcAborts_Type = IdslPerfPrevDayCount
_CIdslItucPerfPrev1DayHdlcAborts_Object = MibTableColumn
cIdslItucPerfPrev1DayHdlcAborts = _CIdslItucPerfPrev1DayHdlcAborts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 34),
    _CIdslItucPerfPrev1DayHdlcAborts_Type()
)
cIdslItucPerfPrev1DayHdlcAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfPrev1DayHdlcAborts.setStatus("current")
_CIdslItucPerfPrev1DayHdlcAligns_Type = IdslPerfPrevDayCount
_CIdslItucPerfPrev1DayHdlcAligns_Object = MibTableColumn
cIdslItucPerfPrev1DayHdlcAligns = _CIdslItucPerfPrev1DayHdlcAligns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 35),
    _CIdslItucPerfPrev1DayHdlcAligns_Type()
)
cIdslItucPerfPrev1DayHdlcAligns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfPrev1DayHdlcAligns.setStatus("current")
_CIdslItucPerfPrev1DayHdlcShorts_Type = IdslPerfPrevDayCount
_CIdslItucPerfPrev1DayHdlcShorts_Object = MibTableColumn
cIdslItucPerfPrev1DayHdlcShorts = _CIdslItucPerfPrev1DayHdlcShorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 36),
    _CIdslItucPerfPrev1DayHdlcShorts_Type()
)
cIdslItucPerfPrev1DayHdlcShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfPrev1DayHdlcShorts.setStatus("current")
_CIdslItucPerfPrev1DayHdlcLongs_Type = IdslPerfPrevDayCount
_CIdslItucPerfPrev1DayHdlcLongs_Object = MibTableColumn
cIdslItucPerfPrev1DayHdlcLongs = _CIdslItucPerfPrev1DayHdlcLongs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 6, 1, 37),
    _CIdslItucPerfPrev1DayHdlcLongs_Type()
)
cIdslItucPerfPrev1DayHdlcLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucPerfPrev1DayHdlcLongs.setStatus("current")
_CIdslIturPerfDataTable_Object = MibTable
cIdslIturPerfDataTable = _CIdslIturPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7)
)
if mibBuilder.loadTexts:
    cIdslIturPerfDataTable.setStatus("current")
_CIdslIturPerfDataEntry_Object = MibTableRow
cIdslIturPerfDataEntry = _CIdslIturPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1)
)
cIdslIturPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cIdslIturPerfDataEntry.setStatus("current")
_CIdslIturPerfCVs_Type = Counter32
_CIdslIturPerfCVs_Object = MibTableColumn
cIdslIturPerfCVs = _CIdslIturPerfCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 1),
    _CIdslIturPerfCVs_Type()
)
cIdslIturPerfCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfCVs.setStatus("current")
_CIdslIturPerfESs_Type = Counter32
_CIdslIturPerfESs_Object = MibTableColumn
cIdslIturPerfESs = _CIdslIturPerfESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 2),
    _CIdslIturPerfESs_Type()
)
cIdslIturPerfESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfESs.setStatus("current")
_CIdslIturPerfSESs_Type = Counter32
_CIdslIturPerfSESs_Object = MibTableColumn
cIdslIturPerfSESs = _CIdslIturPerfSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 3),
    _CIdslIturPerfSESs_Type()
)
cIdslIturPerfSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfSESs.setStatus("current")


class _CIdslIturPerfValidIntervals_Type(Integer32):
    """Custom type cIdslIturPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CIdslIturPerfValidIntervals_Type.__name__ = "Integer32"
_CIdslIturPerfValidIntervals_Object = MibTableColumn
cIdslIturPerfValidIntervals = _CIdslIturPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 4),
    _CIdslIturPerfValidIntervals_Type()
)
cIdslIturPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfValidIntervals.setStatus("current")


class _CIdslIturPerfInvalidIntervals_Type(Integer32):
    """Custom type cIdslIturPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CIdslIturPerfInvalidIntervals_Type.__name__ = "Integer32"
_CIdslIturPerfInvalidIntervals_Object = MibTableColumn
cIdslIturPerfInvalidIntervals = _CIdslIturPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 5),
    _CIdslIturPerfInvalidIntervals_Type()
)
cIdslIturPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfInvalidIntervals.setStatus("current")
_CIdslIturPerfCurr15MinElapsed_Type = IdslPerfTimeElapsed
_CIdslIturPerfCurr15MinElapsed_Object = MibTableColumn
cIdslIturPerfCurr15MinElapsed = _CIdslIturPerfCurr15MinElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 6),
    _CIdslIturPerfCurr15MinElapsed_Type()
)
cIdslIturPerfCurr15MinElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfCurr15MinElapsed.setStatus("current")
_CIdslIturPerfCurr15MinCVs_Type = PerfCurrentCount
_CIdslIturPerfCurr15MinCVs_Object = MibTableColumn
cIdslIturPerfCurr15MinCVs = _CIdslIturPerfCurr15MinCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 7),
    _CIdslIturPerfCurr15MinCVs_Type()
)
cIdslIturPerfCurr15MinCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfCurr15MinCVs.setStatus("current")
_CIdslIturPerfCurr15MinESs_Type = PerfCurrentCount
_CIdslIturPerfCurr15MinESs_Object = MibTableColumn
cIdslIturPerfCurr15MinESs = _CIdslIturPerfCurr15MinESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 8),
    _CIdslIturPerfCurr15MinESs_Type()
)
cIdslIturPerfCurr15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfCurr15MinESs.setStatus("current")
_CIdslIturPerfCurr15MinSESs_Type = PerfCurrentCount
_CIdslIturPerfCurr15MinSESs_Object = MibTableColumn
cIdslIturPerfCurr15MinSESs = _CIdslIturPerfCurr15MinSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 9),
    _CIdslIturPerfCurr15MinSESs_Type()
)
cIdslIturPerfCurr15MinSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfCurr15MinSESs.setStatus("current")
_CIdslIturPerfCurr1DayElapsed_Type = IdslPerfTimeElapsed
_CIdslIturPerfCurr1DayElapsed_Object = MibTableColumn
cIdslIturPerfCurr1DayElapsed = _CIdslIturPerfCurr1DayElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 10),
    _CIdslIturPerfCurr1DayElapsed_Type()
)
cIdslIturPerfCurr1DayElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfCurr1DayElapsed.setStatus("current")
_CIdslIturPerfCurr1DayCVs_Type = IdslPerfCurrDayCount
_CIdslIturPerfCurr1DayCVs_Object = MibTableColumn
cIdslIturPerfCurr1DayCVs = _CIdslIturPerfCurr1DayCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 11),
    _CIdslIturPerfCurr1DayCVs_Type()
)
cIdslIturPerfCurr1DayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfCurr1DayCVs.setStatus("current")
_CIdslIturPerfCurr1DayESs_Type = IdslPerfCurrDayCount
_CIdslIturPerfCurr1DayESs_Object = MibTableColumn
cIdslIturPerfCurr1DayESs = _CIdslIturPerfCurr1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 12),
    _CIdslIturPerfCurr1DayESs_Type()
)
cIdslIturPerfCurr1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfCurr1DayESs.setStatus("current")
_CIdslIturPerfCurr1DaySESs_Type = IdslPerfCurrDayCount
_CIdslIturPerfCurr1DaySESs_Object = MibTableColumn
cIdslIturPerfCurr1DaySESs = _CIdslIturPerfCurr1DaySESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 13),
    _CIdslIturPerfCurr1DaySESs_Type()
)
cIdslIturPerfCurr1DaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfCurr1DaySESs.setStatus("current")


class _CIdslIturPerfPrev1DayMoniSecs_Type(Integer32):
    """Custom type cIdslIturPerfPrev1DayMoniSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CIdslIturPerfPrev1DayMoniSecs_Type.__name__ = "Integer32"
_CIdslIturPerfPrev1DayMoniSecs_Object = MibTableColumn
cIdslIturPerfPrev1DayMoniSecs = _CIdslIturPerfPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 14),
    _CIdslIturPerfPrev1DayMoniSecs_Type()
)
cIdslIturPerfPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfPrev1DayMoniSecs.setStatus("current")
_CIdslIturPerfPrev1DayCVs_Type = IdslPerfPrevDayCount
_CIdslIturPerfPrev1DayCVs_Object = MibTableColumn
cIdslIturPerfPrev1DayCVs = _CIdslIturPerfPrev1DayCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 15),
    _CIdslIturPerfPrev1DayCVs_Type()
)
cIdslIturPerfPrev1DayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfPrev1DayCVs.setStatus("current")
_CIdslIturPerfPrev1DayESs_Type = IdslPerfPrevDayCount
_CIdslIturPerfPrev1DayESs_Object = MibTableColumn
cIdslIturPerfPrev1DayESs = _CIdslIturPerfPrev1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 16),
    _CIdslIturPerfPrev1DayESs_Type()
)
cIdslIturPerfPrev1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfPrev1DayESs.setStatus("current")
_CIdslIturPerfPrev1DaySESs_Type = IdslPerfPrevDayCount
_CIdslIturPerfPrev1DaySESs_Object = MibTableColumn
cIdslIturPerfPrev1DaySESs = _CIdslIturPerfPrev1DaySESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 7, 1, 17),
    _CIdslIturPerfPrev1DaySESs_Type()
)
cIdslIturPerfPrev1DaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturPerfPrev1DaySESs.setStatus("current")
_CIdslItucIntervalTable_Object = MibTable
cIdslItucIntervalTable = _CIdslItucIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 8)
)
if mibBuilder.loadTexts:
    cIdslItucIntervalTable.setStatus("current")
_CIdslItucIntervalEntry_Object = MibTableRow
cIdslItucIntervalEntry = _CIdslItucIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 8, 1)
)
cIdslItucIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IDSL-LINE-MIB", "cIdslItucIntervalNumber"),
)
if mibBuilder.loadTexts:
    cIdslItucIntervalEntry.setStatus("current")


class _CIdslItucIntervalNumber_Type(Integer32):
    """Custom type cIdslItucIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CIdslItucIntervalNumber_Type.__name__ = "Integer32"
_CIdslItucIntervalNumber_Object = MibTableColumn
cIdslItucIntervalNumber = _CIdslItucIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 8, 1, 1),
    _CIdslItucIntervalNumber_Type()
)
cIdslItucIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucIntervalNumber.setStatus("current")
_CIdslItucIntervalValidData_Type = TruthValue
_CIdslItucIntervalValidData_Object = MibTableColumn
cIdslItucIntervalValidData = _CIdslItucIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 8, 1, 2),
    _CIdslItucIntervalValidData_Type()
)
cIdslItucIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucIntervalValidData.setStatus("current")
_CIdslItucIntervalCVs_Type = PerfIntervalCount
_CIdslItucIntervalCVs_Object = MibTableColumn
cIdslItucIntervalCVs = _CIdslItucIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 8, 1, 3),
    _CIdslItucIntervalCVs_Type()
)
cIdslItucIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucIntervalCVs.setStatus("current")
_CIdslItucIntervalESs_Type = PerfIntervalCount
_CIdslItucIntervalESs_Object = MibTableColumn
cIdslItucIntervalESs = _CIdslItucIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 8, 1, 4),
    _CIdslItucIntervalESs_Type()
)
cIdslItucIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucIntervalESs.setStatus("current")
_CIdslItucIntervalSESs_Type = PerfIntervalCount
_CIdslItucIntervalSESs_Object = MibTableColumn
cIdslItucIntervalSESs = _CIdslItucIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 8, 1, 5),
    _CIdslItucIntervalSESs_Type()
)
cIdslItucIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucIntervalSESs.setStatus("current")
_CIdslItucIntervalHdlcCVs_Type = PerfIntervalCount
_CIdslItucIntervalHdlcCVs_Object = MibTableColumn
cIdslItucIntervalHdlcCVs = _CIdslItucIntervalHdlcCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 8, 1, 6),
    _CIdslItucIntervalHdlcCVs_Type()
)
cIdslItucIntervalHdlcCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucIntervalHdlcCVs.setStatus("current")
_CIdslItucIntervalHdlcAborts_Type = PerfIntervalCount
_CIdslItucIntervalHdlcAborts_Object = MibTableColumn
cIdslItucIntervalHdlcAborts = _CIdslItucIntervalHdlcAborts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 8, 1, 7),
    _CIdslItucIntervalHdlcAborts_Type()
)
cIdslItucIntervalHdlcAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucIntervalHdlcAborts.setStatus("current")
_CIdslItucIntervalHdlcAligns_Type = PerfIntervalCount
_CIdslItucIntervalHdlcAligns_Object = MibTableColumn
cIdslItucIntervalHdlcAligns = _CIdslItucIntervalHdlcAligns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 8, 1, 8),
    _CIdslItucIntervalHdlcAligns_Type()
)
cIdslItucIntervalHdlcAligns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucIntervalHdlcAligns.setStatus("current")
_CIdslItucIntervalHdlcShorts_Type = PerfIntervalCount
_CIdslItucIntervalHdlcShorts_Object = MibTableColumn
cIdslItucIntervalHdlcShorts = _CIdslItucIntervalHdlcShorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 8, 1, 9),
    _CIdslItucIntervalHdlcShorts_Type()
)
cIdslItucIntervalHdlcShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucIntervalHdlcShorts.setStatus("current")
_CIdslItucIntervalHdlcLongs_Type = PerfIntervalCount
_CIdslItucIntervalHdlcLongs_Object = MibTableColumn
cIdslItucIntervalHdlcLongs = _CIdslItucIntervalHdlcLongs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 8, 1, 10),
    _CIdslItucIntervalHdlcLongs_Type()
)
cIdslItucIntervalHdlcLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslItucIntervalHdlcLongs.setStatus("current")
_CIdslIturIntervalTable_Object = MibTable
cIdslIturIntervalTable = _CIdslIturIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 9)
)
if mibBuilder.loadTexts:
    cIdslIturIntervalTable.setStatus("current")
_CIdslIturIntervalEntry_Object = MibTableRow
cIdslIturIntervalEntry = _CIdslIturIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 9, 1)
)
cIdslIturIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IDSL-LINE-MIB", "cIdslIturIntervalNumber"),
)
if mibBuilder.loadTexts:
    cIdslIturIntervalEntry.setStatus("current")


class _CIdslIturIntervalNumber_Type(Integer32):
    """Custom type cIdslIturIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CIdslIturIntervalNumber_Type.__name__ = "Integer32"
_CIdslIturIntervalNumber_Object = MibTableColumn
cIdslIturIntervalNumber = _CIdslIturIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 9, 1, 1),
    _CIdslIturIntervalNumber_Type()
)
cIdslIturIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturIntervalNumber.setStatus("current")
_CIdslIturIntervalValidData_Type = TruthValue
_CIdslIturIntervalValidData_Object = MibTableColumn
cIdslIturIntervalValidData = _CIdslIturIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 9, 1, 2),
    _CIdslIturIntervalValidData_Type()
)
cIdslIturIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturIntervalValidData.setStatus("current")
_CIdslIturIntervalCVs_Type = PerfIntervalCount
_CIdslIturIntervalCVs_Object = MibTableColumn
cIdslIturIntervalCVs = _CIdslIturIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 9, 1, 3),
    _CIdslIturIntervalCVs_Type()
)
cIdslIturIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturIntervalCVs.setStatus("current")
_CIdslIturIntervalESs_Type = PerfIntervalCount
_CIdslIturIntervalESs_Object = MibTableColumn
cIdslIturIntervalESs = _CIdslIturIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 9, 1, 4),
    _CIdslIturIntervalESs_Type()
)
cIdslIturIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturIntervalESs.setStatus("current")
_CIdslIturIntervalSESs_Type = PerfIntervalCount
_CIdslIturIntervalSESs_Object = MibTableColumn
cIdslIturIntervalSESs = _CIdslIturIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 9, 1, 5),
    _CIdslIturIntervalSESs_Type()
)
cIdslIturIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslIturIntervalSESs.setStatus("current")
_CIdslLineConfProfileTable_Object = MibTable
cIdslLineConfProfileTable = _CIdslLineConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 14)
)
if mibBuilder.loadTexts:
    cIdslLineConfProfileTable.setStatus("current")
_CIdslLineConfProfileEntry_Object = MibTableRow
cIdslLineConfProfileEntry = _CIdslLineConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 14, 1)
)
cIdslLineConfProfileEntry.setIndexNames(
    (1, "ADSL-LINE-MIB", "adslLineConfProfileName"),
)
if mibBuilder.loadTexts:
    cIdslLineConfProfileEntry.setStatus("current")


class _CIdslLineConfRate_Type(Integer32):
    """Custom type cIdslLineConfRate based on Integer32"""
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
        *(("rate128k", 3),
          ("rate144k", 1),
          ("rate144kIdl", 2),
          ("rate56k", 5),
          ("rate64k", 4))
    )


_CIdslLineConfRate_Type.__name__ = "Integer32"
_CIdslLineConfRate_Object = MibTableColumn
cIdslLineConfRate = _CIdslLineConfRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 14, 1, 1),
    _CIdslLineConfRate_Type()
)
cIdslLineConfRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIdslLineConfRate.setStatus("current")


class _CIdslLineConfProtocol_Type(Integer32):
    """Custom type cIdslLineConfProtocol based on Integer32"""
    defaultValue = 1

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
        *(("frf", 1),
          ("pppLlcIetf", 4),
          ("pppMuxCisco", 2),
          ("pppMuxIetf", 3))
    )


_CIdslLineConfProtocol_Type.__name__ = "Integer32"
_CIdslLineConfProtocol_Object = MibTableColumn
cIdslLineConfProtocol = _CIdslLineConfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 14, 1, 2),
    _CIdslLineConfProtocol_Type()
)
cIdslLineConfProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIdslLineConfProtocol.setStatus("current")


class _CIdslLineConfLmiProtocol_Type(Integer32):
    """Custom type cIdslLineConfLmiProtocol based on Integer32"""
    defaultValue = 1

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
        *(("ansiT1617B", 4),
          ("ansiT1617D", 3),
          ("ansiT1617D1994", 6),
          ("itut933A", 5),
          ("lmiRev1", 2),
          ("noLmiConfigured", 1))
    )


_CIdslLineConfLmiProtocol_Type.__name__ = "Integer32"
_CIdslLineConfLmiProtocol_Object = MibTableColumn
cIdslLineConfLmiProtocol = _CIdslLineConfLmiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 14, 1, 3),
    _CIdslLineConfLmiProtocol_Type()
)
cIdslLineConfLmiProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIdslLineConfLmiProtocol.setStatus("current")


class _CIdslLineConfLmiNetN392_Type(Integer32):
    """Custom type cIdslLineConfLmiNetN392 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CIdslLineConfLmiNetN392_Type.__name__ = "Integer32"
_CIdslLineConfLmiNetN392_Object = MibTableColumn
cIdslLineConfLmiNetN392 = _CIdslLineConfLmiNetN392_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 14, 1, 4),
    _CIdslLineConfLmiNetN392_Type()
)
cIdslLineConfLmiNetN392.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIdslLineConfLmiNetN392.setStatus("current")
if mibBuilder.loadTexts:
    cIdslLineConfLmiNetN392.setUnits("seconds")


class _CIdslLineConfLmiNetN393_Type(Integer32):
    """Custom type cIdslLineConfLmiNetN393 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CIdslLineConfLmiNetN393_Type.__name__ = "Integer32"
_CIdslLineConfLmiNetN393_Object = MibTableColumn
cIdslLineConfLmiNetN393 = _CIdslLineConfLmiNetN393_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 14, 1, 5),
    _CIdslLineConfLmiNetN393_Type()
)
cIdslLineConfLmiNetN393.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIdslLineConfLmiNetN393.setStatus("current")


class _CIdslLineConfLmiNetT392_Type(Integer32):
    """Custom type cIdslLineConfLmiNetT392 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_CIdslLineConfLmiNetT392_Type.__name__ = "Integer32"
_CIdslLineConfLmiNetT392_Object = MibTableColumn
cIdslLineConfLmiNetT392 = _CIdslLineConfLmiNetT392_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 14, 1, 6),
    _CIdslLineConfLmiNetT392_Type()
)
cIdslLineConfLmiNetT392.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIdslLineConfLmiNetT392.setStatus("current")
if mibBuilder.loadTexts:
    cIdslLineConfLmiNetT392.setUnits("seconds")


class _CIdslLineConfUpcIntent_Type(Integer32):
    """Custom type cIdslLineConfUpcIntent based on Integer32"""
    defaultValue = 1

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
        *(("drop", 4),
          ("pass", 1),
          ("tag", 3),
          ("tagDrop", 2))
    )


_CIdslLineConfUpcIntent_Type.__name__ = "Integer32"
_CIdslLineConfUpcIntent_Object = MibTableColumn
cIdslLineConfUpcIntent = _CIdslLineConfUpcIntent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 14, 1, 7),
    _CIdslLineConfUpcIntent_Type()
)
cIdslLineConfUpcIntent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIdslLineConfUpcIntent.setStatus("current")


class _CIdslLineConfBcDefault_Type(Integer32):
    """Custom type cIdslLineConfBcDefault based on Integer32"""
    defaultValue = 0


_CIdslLineConfBcDefault_Object = MibTableColumn
cIdslLineConfBcDefault = _CIdslLineConfBcDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 14, 1, 8),
    _CIdslLineConfBcDefault_Type()
)
cIdslLineConfBcDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIdslLineConfBcDefault.setStatus("current")
_CIdslPppoaPerfDataTable_Object = MibTable
cIdslPppoaPerfDataTable = _CIdslPppoaPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16)
)
if mibBuilder.loadTexts:
    cIdslPppoaPerfDataTable.setStatus("current")
_CIdslPppoaPerfDataEntry_Object = MibTableRow
cIdslPppoaPerfDataEntry = _CIdslPppoaPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1)
)
cIdslPppoaPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cIdslPppoaPerfDataEntry.setStatus("current")
_CIdslPppoaPerfRTOs_Type = Counter32
_CIdslPppoaPerfRTOs_Object = MibTableColumn
cIdslPppoaPerfRTOs = _CIdslPppoaPerfRTOs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 1),
    _CIdslPppoaPerfRTOs_Type()
)
cIdslPppoaPerfRTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfRTOs.setStatus("current")
_CIdslPppoaPerfCVs_Type = Counter32
_CIdslPppoaPerfCVs_Object = MibTableColumn
cIdslPppoaPerfCVs = _CIdslPppoaPerfCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 2),
    _CIdslPppoaPerfCVs_Type()
)
cIdslPppoaPerfCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCVs.setStatus("current")
_CIdslPppoaPerfShorts_Type = Counter32
_CIdslPppoaPerfShorts_Object = MibTableColumn
cIdslPppoaPerfShorts = _CIdslPppoaPerfShorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 3),
    _CIdslPppoaPerfShorts_Type()
)
cIdslPppoaPerfShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfShorts.setStatus("current")
_CIdslPppoaPerfLongs_Type = Counter32
_CIdslPppoaPerfLongs_Object = MibTableColumn
cIdslPppoaPerfLongs = _CIdslPppoaPerfLongs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 4),
    _CIdslPppoaPerfLongs_Type()
)
cIdslPppoaPerfLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfLongs.setStatus("current")
_CIdslPppoaPerfDiscards_Type = Counter32
_CIdslPppoaPerfDiscards_Object = MibTableColumn
cIdslPppoaPerfDiscards = _CIdslPppoaPerfDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 5),
    _CIdslPppoaPerfDiscards_Type()
)
cIdslPppoaPerfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfDiscards.setStatus("current")


class _CIdslPppoaPerfValidIntervals_Type(Integer32):
    """Custom type cIdslPppoaPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CIdslPppoaPerfValidIntervals_Type.__name__ = "Integer32"
_CIdslPppoaPerfValidIntervals_Object = MibTableColumn
cIdslPppoaPerfValidIntervals = _CIdslPppoaPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 6),
    _CIdslPppoaPerfValidIntervals_Type()
)
cIdslPppoaPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfValidIntervals.setStatus("current")


class _CIdslPppoaPerfInvalidIntervals_Type(Integer32):
    """Custom type cIdslPppoaPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CIdslPppoaPerfInvalidIntervals_Type.__name__ = "Integer32"
_CIdslPppoaPerfInvalidIntervals_Object = MibTableColumn
cIdslPppoaPerfInvalidIntervals = _CIdslPppoaPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 7),
    _CIdslPppoaPerfInvalidIntervals_Type()
)
cIdslPppoaPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfInvalidIntervals.setStatus("current")
_CIdslPppoaPerfCurr15MinElapsed_Type = IdslPerfTimeElapsed
_CIdslPppoaPerfCurr15MinElapsed_Object = MibTableColumn
cIdslPppoaPerfCurr15MinElapsed = _CIdslPppoaPerfCurr15MinElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 8),
    _CIdslPppoaPerfCurr15MinElapsed_Type()
)
cIdslPppoaPerfCurr15MinElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCurr15MinElapsed.setStatus("current")
_CIdslPppoaPerfCurr15MinRTOs_Type = PerfCurrentCount
_CIdslPppoaPerfCurr15MinRTOs_Object = MibTableColumn
cIdslPppoaPerfCurr15MinRTOs = _CIdslPppoaPerfCurr15MinRTOs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 9),
    _CIdslPppoaPerfCurr15MinRTOs_Type()
)
cIdslPppoaPerfCurr15MinRTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCurr15MinRTOs.setStatus("current")
_CIdslPppoaPerfCurr15MinCVs_Type = PerfCurrentCount
_CIdslPppoaPerfCurr15MinCVs_Object = MibTableColumn
cIdslPppoaPerfCurr15MinCVs = _CIdslPppoaPerfCurr15MinCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 10),
    _CIdslPppoaPerfCurr15MinCVs_Type()
)
cIdslPppoaPerfCurr15MinCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCurr15MinCVs.setStatus("current")
_CIdslPppoaPerfCurr15MinShorts_Type = PerfCurrentCount
_CIdslPppoaPerfCurr15MinShorts_Object = MibTableColumn
cIdslPppoaPerfCurr15MinShorts = _CIdslPppoaPerfCurr15MinShorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 11),
    _CIdslPppoaPerfCurr15MinShorts_Type()
)
cIdslPppoaPerfCurr15MinShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCurr15MinShorts.setStatus("current")
_CIdslPppoaPerfCurr15MinLongs_Type = PerfCurrentCount
_CIdslPppoaPerfCurr15MinLongs_Object = MibTableColumn
cIdslPppoaPerfCurr15MinLongs = _CIdslPppoaPerfCurr15MinLongs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 12),
    _CIdslPppoaPerfCurr15MinLongs_Type()
)
cIdslPppoaPerfCurr15MinLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCurr15MinLongs.setStatus("current")
_CIdslPppoaPerfCurr15MinDiscards_Type = PerfCurrentCount
_CIdslPppoaPerfCurr15MinDiscards_Object = MibTableColumn
cIdslPppoaPerfCurr15MinDiscards = _CIdslPppoaPerfCurr15MinDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 13),
    _CIdslPppoaPerfCurr15MinDiscards_Type()
)
cIdslPppoaPerfCurr15MinDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCurr15MinDiscards.setStatus("current")
_CIdslPppoaPerfCurr1DayElapsed_Type = IdslPerfTimeElapsed
_CIdslPppoaPerfCurr1DayElapsed_Object = MibTableColumn
cIdslPppoaPerfCurr1DayElapsed = _CIdslPppoaPerfCurr1DayElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 14),
    _CIdslPppoaPerfCurr1DayElapsed_Type()
)
cIdslPppoaPerfCurr1DayElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCurr1DayElapsed.setStatus("current")
_CIdslPppoaPerfCurr1DayRTOs_Type = IdslPerfCurrDayCount
_CIdslPppoaPerfCurr1DayRTOs_Object = MibTableColumn
cIdslPppoaPerfCurr1DayRTOs = _CIdslPppoaPerfCurr1DayRTOs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 15),
    _CIdslPppoaPerfCurr1DayRTOs_Type()
)
cIdslPppoaPerfCurr1DayRTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCurr1DayRTOs.setStatus("current")
_CIdslPppoaPerfCurr1DayCVs_Type = IdslPerfCurrDayCount
_CIdslPppoaPerfCurr1DayCVs_Object = MibTableColumn
cIdslPppoaPerfCurr1DayCVs = _CIdslPppoaPerfCurr1DayCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 16),
    _CIdslPppoaPerfCurr1DayCVs_Type()
)
cIdslPppoaPerfCurr1DayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCurr1DayCVs.setStatus("current")
_CIdslPppoaPerfCurr1DayShorts_Type = IdslPerfCurrDayCount
_CIdslPppoaPerfCurr1DayShorts_Object = MibTableColumn
cIdslPppoaPerfCurr1DayShorts = _CIdslPppoaPerfCurr1DayShorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 17),
    _CIdslPppoaPerfCurr1DayShorts_Type()
)
cIdslPppoaPerfCurr1DayShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCurr1DayShorts.setStatus("current")
_CIdslPppoaPerfCurr1DayLongs_Type = IdslPerfCurrDayCount
_CIdslPppoaPerfCurr1DayLongs_Object = MibTableColumn
cIdslPppoaPerfCurr1DayLongs = _CIdslPppoaPerfCurr1DayLongs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 18),
    _CIdslPppoaPerfCurr1DayLongs_Type()
)
cIdslPppoaPerfCurr1DayLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCurr1DayLongs.setStatus("current")
_CIdslPppoaPerfCurr1DayDiscards_Type = IdslPerfCurrDayCount
_CIdslPppoaPerfCurr1DayDiscards_Object = MibTableColumn
cIdslPppoaPerfCurr1DayDiscards = _CIdslPppoaPerfCurr1DayDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 19),
    _CIdslPppoaPerfCurr1DayDiscards_Type()
)
cIdslPppoaPerfCurr1DayDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfCurr1DayDiscards.setStatus("current")


class _CIdslPppoaPerfPrev1DayMoniSecs_Type(Integer32):
    """Custom type cIdslPppoaPerfPrev1DayMoniSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CIdslPppoaPerfPrev1DayMoniSecs_Type.__name__ = "Integer32"
_CIdslPppoaPerfPrev1DayMoniSecs_Object = MibTableColumn
cIdslPppoaPerfPrev1DayMoniSecs = _CIdslPppoaPerfPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 20),
    _CIdslPppoaPerfPrev1DayMoniSecs_Type()
)
cIdslPppoaPerfPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfPrev1DayMoniSecs.setStatus("current")
_CIdslPppoaPerfPrev1DayRTOs_Type = IdslPerfPrevDayCount
_CIdslPppoaPerfPrev1DayRTOs_Object = MibTableColumn
cIdslPppoaPerfPrev1DayRTOs = _CIdslPppoaPerfPrev1DayRTOs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 21),
    _CIdslPppoaPerfPrev1DayRTOs_Type()
)
cIdslPppoaPerfPrev1DayRTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfPrev1DayRTOs.setStatus("current")
_CIdslPppoaPerfPrev1DayCVs_Type = IdslPerfPrevDayCount
_CIdslPppoaPerfPrev1DayCVs_Object = MibTableColumn
cIdslPppoaPerfPrev1DayCVs = _CIdslPppoaPerfPrev1DayCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 22),
    _CIdslPppoaPerfPrev1DayCVs_Type()
)
cIdslPppoaPerfPrev1DayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfPrev1DayCVs.setStatus("current")
_CIdslPppoaPerfPrev1DayShorts_Type = IdslPerfPrevDayCount
_CIdslPppoaPerfPrev1DayShorts_Object = MibTableColumn
cIdslPppoaPerfPrev1DayShorts = _CIdslPppoaPerfPrev1DayShorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 23),
    _CIdslPppoaPerfPrev1DayShorts_Type()
)
cIdslPppoaPerfPrev1DayShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfPrev1DayShorts.setStatus("current")
_CIdslPppoaPerfPrev1DayLongs_Type = IdslPerfPrevDayCount
_CIdslPppoaPerfPrev1DayLongs_Object = MibTableColumn
cIdslPppoaPerfPrev1DayLongs = _CIdslPppoaPerfPrev1DayLongs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 24),
    _CIdslPppoaPerfPrev1DayLongs_Type()
)
cIdslPppoaPerfPrev1DayLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfPrev1DayLongs.setStatus("current")
_CIdslPppoaPerfPrev1DayDiscards_Type = IdslPerfPrevDayCount
_CIdslPppoaPerfPrev1DayDiscards_Object = MibTableColumn
cIdslPppoaPerfPrev1DayDiscards = _CIdslPppoaPerfPrev1DayDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 16, 1, 25),
    _CIdslPppoaPerfPrev1DayDiscards_Type()
)
cIdslPppoaPerfPrev1DayDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaPerfPrev1DayDiscards.setStatus("current")
_CIdslPppoaIntervalTable_Object = MibTable
cIdslPppoaIntervalTable = _CIdslPppoaIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 17)
)
if mibBuilder.loadTexts:
    cIdslPppoaIntervalTable.setStatus("current")
_CIdslPppoaIntervalEntry_Object = MibTableRow
cIdslPppoaIntervalEntry = _CIdslPppoaIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 17, 1)
)
cIdslPppoaIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IDSL-LINE-MIB", "cIdslPppoaIntervalNumber"),
)
if mibBuilder.loadTexts:
    cIdslPppoaIntervalEntry.setStatus("current")


class _CIdslPppoaIntervalNumber_Type(Integer32):
    """Custom type cIdslPppoaIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CIdslPppoaIntervalNumber_Type.__name__ = "Integer32"
_CIdslPppoaIntervalNumber_Object = MibTableColumn
cIdslPppoaIntervalNumber = _CIdslPppoaIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 17, 1, 1),
    _CIdslPppoaIntervalNumber_Type()
)
cIdslPppoaIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaIntervalNumber.setStatus("current")
_CIdslPppoaIntervalValidData_Type = TruthValue
_CIdslPppoaIntervalValidData_Object = MibTableColumn
cIdslPppoaIntervalValidData = _CIdslPppoaIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 17, 1, 2),
    _CIdslPppoaIntervalValidData_Type()
)
cIdslPppoaIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaIntervalValidData.setStatus("current")
_CIdslPppoaIntervalRTOs_Type = PerfIntervalCount
_CIdslPppoaIntervalRTOs_Object = MibTableColumn
cIdslPppoaIntervalRTOs = _CIdslPppoaIntervalRTOs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 17, 1, 3),
    _CIdslPppoaIntervalRTOs_Type()
)
cIdslPppoaIntervalRTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaIntervalRTOs.setStatus("current")
_CIdslPppoaIntervalCVs_Type = PerfIntervalCount
_CIdslPppoaIntervalCVs_Object = MibTableColumn
cIdslPppoaIntervalCVs = _CIdslPppoaIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 17, 1, 4),
    _CIdslPppoaIntervalCVs_Type()
)
cIdslPppoaIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaIntervalCVs.setStatus("current")
_CIdslPppoaIntervalShorts_Type = PerfIntervalCount
_CIdslPppoaIntervalShorts_Object = MibTableColumn
cIdslPppoaIntervalShorts = _CIdslPppoaIntervalShorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 17, 1, 5),
    _CIdslPppoaIntervalShorts_Type()
)
cIdslPppoaIntervalShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaIntervalShorts.setStatus("current")
_CIdslPppoaIntervalLongs_Type = PerfIntervalCount
_CIdslPppoaIntervalLongs_Object = MibTableColumn
cIdslPppoaIntervalLongs = _CIdslPppoaIntervalLongs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 17, 1, 6),
    _CIdslPppoaIntervalLongs_Type()
)
cIdslPppoaIntervalLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaIntervalLongs.setStatus("current")
_CIdslPppoaIntervalDiscards_Type = PerfIntervalCount
_CIdslPppoaIntervalDiscards_Object = MibTableColumn
cIdslPppoaIntervalDiscards = _CIdslPppoaIntervalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 17, 1, 7),
    _CIdslPppoaIntervalDiscards_Type()
)
cIdslPppoaIntervalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaIntervalDiscards.setStatus("current")
_CIdslPppoaMapTable_Object = MibTable
cIdslPppoaMapTable = _CIdslPppoaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 18)
)
if mibBuilder.loadTexts:
    cIdslPppoaMapTable.setStatus("current")
_CIdslPppoaMapEntry_Object = MibTableRow
cIdslPppoaMapEntry = _CIdslPppoaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 18, 1)
)
cIdslPppoaMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cIdslPppoaMapEntry.setStatus("current")
_CIdslPppoaMapIfIndex_Type = InterfaceIndex
_CIdslPppoaMapIfIndex_Object = MibTableColumn
cIdslPppoaMapIfIndex = _CIdslPppoaMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 18, 1, 1),
    _CIdslPppoaMapIfIndex_Type()
)
cIdslPppoaMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIdslPppoaMapIfIndex.setStatus("current")


class _CIdslPppoaMapVpi_Type(Integer32):
    """Custom type cIdslPppoaMapVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CIdslPppoaMapVpi_Type.__name__ = "Integer32"
_CIdslPppoaMapVpi_Object = MibTableColumn
cIdslPppoaMapVpi = _CIdslPppoaMapVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 18, 1, 2),
    _CIdslPppoaMapVpi_Type()
)
cIdslPppoaMapVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIdslPppoaMapVpi.setStatus("current")


class _CIdslPppoaMapVci_Type(Integer32):
    """Custom type cIdslPppoaMapVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CIdslPppoaMapVci_Type.__name__ = "Integer32"
_CIdslPppoaMapVci_Object = MibTableColumn
cIdslPppoaMapVci = _CIdslPppoaMapVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 1, 18, 1, 3),
    _CIdslPppoaMapVci_Type()
)
cIdslPppoaMapVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIdslPppoaMapVci.setStatus("current")
_CiscoIdslLineMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoIdslLineMIBNotificationsPrefix = _CiscoIdslLineMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 2)
)
_CiscoIdslLineMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoIdslLineMIBNotifications = _CiscoIdslLineMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 2, 0)
)
_CiscoIdslLineMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIdslLineMIBConformance = _CiscoIdslLineMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 3)
)
_CiscoIdslLineMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIdslLineMIBCompliances = _CiscoIdslLineMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 3, 1)
)
_CiscoIdslLineMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIdslLineMIBGroups = _CiscoIdslLineMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 3, 2)
)

# Managed Objects groups

cIdslBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 3, 2, 1)
)
cIdslBasicGroup.setObjects(
      *(("CISCO-IDSL-LINE-MIB", "cIdslLineSpecific"),
        ("CISCO-IDSL-LINE-MIB", "cIdslLineConfProfile"),
        ("CISCO-IDSL-LINE-MIB", "cIdslLineAlarmConfProfile"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucInvSerialNumber"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucInvVendorId"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucInvVersionNumber"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucStatus"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfSESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfHdlcCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfHdlcAborts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfHdlcAligns"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfHdlcShorts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfHdlcLongs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfSESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslLineConfRate"),
        ("CISCO-IDSL-LINE-MIB", "cIdslLineConfProtocol"),
        ("CISCO-IDSL-LINE-MIB", "cIdslLineConfLmiProtocol"),
        ("CISCO-IDSL-LINE-MIB", "cIdslLineConfLmiNetN392"),
        ("CISCO-IDSL-LINE-MIB", "cIdslLineConfLmiNetN393"),
        ("CISCO-IDSL-LINE-MIB", "cIdslLineConfLmiNetT392"),
        ("CISCO-IDSL-LINE-MIB", "cIdslLineConfUpcIntent"),
        ("CISCO-IDSL-LINE-MIB", "cIdslLineConfBcDefault"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfRTOs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfShorts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfLongs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfDiscards"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaMapIfIndex"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaMapVpi"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaMapVci"))
)
if mibBuilder.loadTexts:
    cIdslBasicGroup.setStatus("current")

cIdslPM15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 3, 2, 2)
)
cIdslPM15MinIntervalGroup.setObjects(
      *(("CISCO-IDSL-LINE-MIB", "cIdslItucPerfValidIntervals"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfInvalidIntervals"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr15MinElapsed"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr15MinCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr15MinESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr15MinSESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr15MinHdlcCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr15MinHdlcAborts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr15MinHdlcAligns"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr15MinHdlcShorts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr15MinHdlcLongs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr1DayElapsed"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr1DayCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr1DayESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr1DaySESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr1DayHdlcCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr1DayHdlcAborts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr1DayHdlcAligns"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr1DayHdlcShorts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfCurr1DayHdlcLongs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfPrev1DayMoniSecs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfPrev1DayCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfPrev1DayESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfPrev1DaySESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfPrev1DayHdlcCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfPrev1DayHdlcAborts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfPrev1DayHdlcAligns"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfPrev1DayHdlcShorts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucPerfPrev1DayHdlcLongs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfValidIntervals"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfInvalidIntervals"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfCurr15MinElapsed"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfCurr15MinCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfCurr15MinESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfCurr15MinSESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfCurr1DayElapsed"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfCurr1DayCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfCurr1DayESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfCurr1DaySESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfPrev1DayMoniSecs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfPrev1DayCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfPrev1DayESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturPerfPrev1DaySESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucIntervalNumber"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucIntervalValidData"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucIntervalCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucIntervalESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucIntervalSESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucIntervalHdlcCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucIntervalHdlcAborts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucIntervalHdlcAligns"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucIntervalHdlcShorts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslItucIntervalHdlcLongs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturIntervalNumber"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturIntervalValidData"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturIntervalCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturIntervalESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslIturIntervalSESs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfValidIntervals"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfInvalidIntervals"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCurr15MinElapsed"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCurr15MinRTOs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCurr15MinCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCurr15MinShorts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCurr15MinLongs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCurr15MinDiscards"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCurr1DayElapsed"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCurr1DayRTOs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCurr1DayCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCurr1DayShorts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCurr1DayLongs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfCurr1DayDiscards"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfPrev1DayMoniSecs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfPrev1DayRTOs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfPrev1DayCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfPrev1DayShorts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfPrev1DayLongs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaPerfPrev1DayDiscards"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaIntervalNumber"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaIntervalValidData"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaIntervalRTOs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaIntervalCVs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaIntervalShorts"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaIntervalLongs"),
        ("CISCO-IDSL-LINE-MIB", "cIdslPppoaIntervalDiscards"))
)
if mibBuilder.loadTexts:
    cIdslPM15MinIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIdslLineMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 154, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIdslLineMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IDSL-LINE-MIB",
    **{"IdslPerfTimeElapsed": IdslPerfTimeElapsed,
       "IdslPerfCurrDayCount": IdslPerfCurrDayCount,
       "IdslPerfPrevDayCount": IdslPerfPrevDayCount,
       "ciscoIdslLineMIB": ciscoIdslLineMIB,
       "ciscoIdslLineMIBObjects": ciscoIdslLineMIBObjects,
       "cIdslLineTable": cIdslLineTable,
       "cIdslLineEntry": cIdslLineEntry,
       "cIdslLineSpecific": cIdslLineSpecific,
       "cIdslLineConfProfile": cIdslLineConfProfile,
       "cIdslLineAlarmConfProfile": cIdslLineAlarmConfProfile,
       "cIdslItucPhysTable": cIdslItucPhysTable,
       "cIdslItucPhysEntry": cIdslItucPhysEntry,
       "cIdslItucInvSerialNumber": cIdslItucInvSerialNumber,
       "cIdslItucInvVendorId": cIdslItucInvVendorId,
       "cIdslItucInvVersionNumber": cIdslItucInvVersionNumber,
       "cIdslItucStatus": cIdslItucStatus,
       "cIdslItucPerfDataTable": cIdslItucPerfDataTable,
       "cIdslItucPerfDataEntry": cIdslItucPerfDataEntry,
       "cIdslItucPerfCVs": cIdslItucPerfCVs,
       "cIdslItucPerfESs": cIdslItucPerfESs,
       "cIdslItucPerfSESs": cIdslItucPerfSESs,
       "cIdslItucPerfHdlcCVs": cIdslItucPerfHdlcCVs,
       "cIdslItucPerfHdlcAborts": cIdslItucPerfHdlcAborts,
       "cIdslItucPerfHdlcAligns": cIdslItucPerfHdlcAligns,
       "cIdslItucPerfHdlcShorts": cIdslItucPerfHdlcShorts,
       "cIdslItucPerfHdlcLongs": cIdslItucPerfHdlcLongs,
       "cIdslItucPerfValidIntervals": cIdslItucPerfValidIntervals,
       "cIdslItucPerfInvalidIntervals": cIdslItucPerfInvalidIntervals,
       "cIdslItucPerfCurr15MinElapsed": cIdslItucPerfCurr15MinElapsed,
       "cIdslItucPerfCurr15MinCVs": cIdslItucPerfCurr15MinCVs,
       "cIdslItucPerfCurr15MinESs": cIdslItucPerfCurr15MinESs,
       "cIdslItucPerfCurr15MinSESs": cIdslItucPerfCurr15MinSESs,
       "cIdslItucPerfCurr15MinHdlcCVs": cIdslItucPerfCurr15MinHdlcCVs,
       "cIdslItucPerfCurr15MinHdlcAborts": cIdslItucPerfCurr15MinHdlcAborts,
       "cIdslItucPerfCurr15MinHdlcAligns": cIdslItucPerfCurr15MinHdlcAligns,
       "cIdslItucPerfCurr15MinHdlcShorts": cIdslItucPerfCurr15MinHdlcShorts,
       "cIdslItucPerfCurr15MinHdlcLongs": cIdslItucPerfCurr15MinHdlcLongs,
       "cIdslItucPerfCurr1DayElapsed": cIdslItucPerfCurr1DayElapsed,
       "cIdslItucPerfCurr1DayCVs": cIdslItucPerfCurr1DayCVs,
       "cIdslItucPerfCurr1DayESs": cIdslItucPerfCurr1DayESs,
       "cIdslItucPerfCurr1DaySESs": cIdslItucPerfCurr1DaySESs,
       "cIdslItucPerfCurr1DayHdlcCVs": cIdslItucPerfCurr1DayHdlcCVs,
       "cIdslItucPerfCurr1DayHdlcAborts": cIdslItucPerfCurr1DayHdlcAborts,
       "cIdslItucPerfCurr1DayHdlcAligns": cIdslItucPerfCurr1DayHdlcAligns,
       "cIdslItucPerfCurr1DayHdlcShorts": cIdslItucPerfCurr1DayHdlcShorts,
       "cIdslItucPerfCurr1DayHdlcLongs": cIdslItucPerfCurr1DayHdlcLongs,
       "cIdslItucPerfPrev1DayMoniSecs": cIdslItucPerfPrev1DayMoniSecs,
       "cIdslItucPerfPrev1DayCVs": cIdslItucPerfPrev1DayCVs,
       "cIdslItucPerfPrev1DayESs": cIdslItucPerfPrev1DayESs,
       "cIdslItucPerfPrev1DaySESs": cIdslItucPerfPrev1DaySESs,
       "cIdslItucPerfPrev1DayHdlcCVs": cIdslItucPerfPrev1DayHdlcCVs,
       "cIdslItucPerfPrev1DayHdlcAborts": cIdslItucPerfPrev1DayHdlcAborts,
       "cIdslItucPerfPrev1DayHdlcAligns": cIdslItucPerfPrev1DayHdlcAligns,
       "cIdslItucPerfPrev1DayHdlcShorts": cIdslItucPerfPrev1DayHdlcShorts,
       "cIdslItucPerfPrev1DayHdlcLongs": cIdslItucPerfPrev1DayHdlcLongs,
       "cIdslIturPerfDataTable": cIdslIturPerfDataTable,
       "cIdslIturPerfDataEntry": cIdslIturPerfDataEntry,
       "cIdslIturPerfCVs": cIdslIturPerfCVs,
       "cIdslIturPerfESs": cIdslIturPerfESs,
       "cIdslIturPerfSESs": cIdslIturPerfSESs,
       "cIdslIturPerfValidIntervals": cIdslIturPerfValidIntervals,
       "cIdslIturPerfInvalidIntervals": cIdslIturPerfInvalidIntervals,
       "cIdslIturPerfCurr15MinElapsed": cIdslIturPerfCurr15MinElapsed,
       "cIdslIturPerfCurr15MinCVs": cIdslIturPerfCurr15MinCVs,
       "cIdslIturPerfCurr15MinESs": cIdslIturPerfCurr15MinESs,
       "cIdslIturPerfCurr15MinSESs": cIdslIturPerfCurr15MinSESs,
       "cIdslIturPerfCurr1DayElapsed": cIdslIturPerfCurr1DayElapsed,
       "cIdslIturPerfCurr1DayCVs": cIdslIturPerfCurr1DayCVs,
       "cIdslIturPerfCurr1DayESs": cIdslIturPerfCurr1DayESs,
       "cIdslIturPerfCurr1DaySESs": cIdslIturPerfCurr1DaySESs,
       "cIdslIturPerfPrev1DayMoniSecs": cIdslIturPerfPrev1DayMoniSecs,
       "cIdslIturPerfPrev1DayCVs": cIdslIturPerfPrev1DayCVs,
       "cIdslIturPerfPrev1DayESs": cIdslIturPerfPrev1DayESs,
       "cIdslIturPerfPrev1DaySESs": cIdslIturPerfPrev1DaySESs,
       "cIdslItucIntervalTable": cIdslItucIntervalTable,
       "cIdslItucIntervalEntry": cIdslItucIntervalEntry,
       "cIdslItucIntervalNumber": cIdslItucIntervalNumber,
       "cIdslItucIntervalValidData": cIdslItucIntervalValidData,
       "cIdslItucIntervalCVs": cIdslItucIntervalCVs,
       "cIdslItucIntervalESs": cIdslItucIntervalESs,
       "cIdslItucIntervalSESs": cIdslItucIntervalSESs,
       "cIdslItucIntervalHdlcCVs": cIdslItucIntervalHdlcCVs,
       "cIdslItucIntervalHdlcAborts": cIdslItucIntervalHdlcAborts,
       "cIdslItucIntervalHdlcAligns": cIdslItucIntervalHdlcAligns,
       "cIdslItucIntervalHdlcShorts": cIdslItucIntervalHdlcShorts,
       "cIdslItucIntervalHdlcLongs": cIdslItucIntervalHdlcLongs,
       "cIdslIturIntervalTable": cIdslIturIntervalTable,
       "cIdslIturIntervalEntry": cIdslIturIntervalEntry,
       "cIdslIturIntervalNumber": cIdslIturIntervalNumber,
       "cIdslIturIntervalValidData": cIdslIturIntervalValidData,
       "cIdslIturIntervalCVs": cIdslIturIntervalCVs,
       "cIdslIturIntervalESs": cIdslIturIntervalESs,
       "cIdslIturIntervalSESs": cIdslIturIntervalSESs,
       "cIdslLineConfProfileTable": cIdslLineConfProfileTable,
       "cIdslLineConfProfileEntry": cIdslLineConfProfileEntry,
       "cIdslLineConfRate": cIdslLineConfRate,
       "cIdslLineConfProtocol": cIdslLineConfProtocol,
       "cIdslLineConfLmiProtocol": cIdslLineConfLmiProtocol,
       "cIdslLineConfLmiNetN392": cIdslLineConfLmiNetN392,
       "cIdslLineConfLmiNetN393": cIdslLineConfLmiNetN393,
       "cIdslLineConfLmiNetT392": cIdslLineConfLmiNetT392,
       "cIdslLineConfUpcIntent": cIdslLineConfUpcIntent,
       "cIdslLineConfBcDefault": cIdslLineConfBcDefault,
       "cIdslPppoaPerfDataTable": cIdslPppoaPerfDataTable,
       "cIdslPppoaPerfDataEntry": cIdslPppoaPerfDataEntry,
       "cIdslPppoaPerfRTOs": cIdslPppoaPerfRTOs,
       "cIdslPppoaPerfCVs": cIdslPppoaPerfCVs,
       "cIdslPppoaPerfShorts": cIdslPppoaPerfShorts,
       "cIdslPppoaPerfLongs": cIdslPppoaPerfLongs,
       "cIdslPppoaPerfDiscards": cIdslPppoaPerfDiscards,
       "cIdslPppoaPerfValidIntervals": cIdslPppoaPerfValidIntervals,
       "cIdslPppoaPerfInvalidIntervals": cIdslPppoaPerfInvalidIntervals,
       "cIdslPppoaPerfCurr15MinElapsed": cIdslPppoaPerfCurr15MinElapsed,
       "cIdslPppoaPerfCurr15MinRTOs": cIdslPppoaPerfCurr15MinRTOs,
       "cIdslPppoaPerfCurr15MinCVs": cIdslPppoaPerfCurr15MinCVs,
       "cIdslPppoaPerfCurr15MinShorts": cIdslPppoaPerfCurr15MinShorts,
       "cIdslPppoaPerfCurr15MinLongs": cIdslPppoaPerfCurr15MinLongs,
       "cIdslPppoaPerfCurr15MinDiscards": cIdslPppoaPerfCurr15MinDiscards,
       "cIdslPppoaPerfCurr1DayElapsed": cIdslPppoaPerfCurr1DayElapsed,
       "cIdslPppoaPerfCurr1DayRTOs": cIdslPppoaPerfCurr1DayRTOs,
       "cIdslPppoaPerfCurr1DayCVs": cIdslPppoaPerfCurr1DayCVs,
       "cIdslPppoaPerfCurr1DayShorts": cIdslPppoaPerfCurr1DayShorts,
       "cIdslPppoaPerfCurr1DayLongs": cIdslPppoaPerfCurr1DayLongs,
       "cIdslPppoaPerfCurr1DayDiscards": cIdslPppoaPerfCurr1DayDiscards,
       "cIdslPppoaPerfPrev1DayMoniSecs": cIdslPppoaPerfPrev1DayMoniSecs,
       "cIdslPppoaPerfPrev1DayRTOs": cIdslPppoaPerfPrev1DayRTOs,
       "cIdslPppoaPerfPrev1DayCVs": cIdslPppoaPerfPrev1DayCVs,
       "cIdslPppoaPerfPrev1DayShorts": cIdslPppoaPerfPrev1DayShorts,
       "cIdslPppoaPerfPrev1DayLongs": cIdslPppoaPerfPrev1DayLongs,
       "cIdslPppoaPerfPrev1DayDiscards": cIdslPppoaPerfPrev1DayDiscards,
       "cIdslPppoaIntervalTable": cIdslPppoaIntervalTable,
       "cIdslPppoaIntervalEntry": cIdslPppoaIntervalEntry,
       "cIdslPppoaIntervalNumber": cIdslPppoaIntervalNumber,
       "cIdslPppoaIntervalValidData": cIdslPppoaIntervalValidData,
       "cIdslPppoaIntervalRTOs": cIdslPppoaIntervalRTOs,
       "cIdslPppoaIntervalCVs": cIdslPppoaIntervalCVs,
       "cIdslPppoaIntervalShorts": cIdslPppoaIntervalShorts,
       "cIdslPppoaIntervalLongs": cIdslPppoaIntervalLongs,
       "cIdslPppoaIntervalDiscards": cIdslPppoaIntervalDiscards,
       "cIdslPppoaMapTable": cIdslPppoaMapTable,
       "cIdslPppoaMapEntry": cIdslPppoaMapEntry,
       "cIdslPppoaMapIfIndex": cIdslPppoaMapIfIndex,
       "cIdslPppoaMapVpi": cIdslPppoaMapVpi,
       "cIdslPppoaMapVci": cIdslPppoaMapVci,
       "ciscoIdslLineMIBNotificationsPrefix": ciscoIdslLineMIBNotificationsPrefix,
       "ciscoIdslLineMIBNotifications": ciscoIdslLineMIBNotifications,
       "ciscoIdslLineMIBConformance": ciscoIdslLineMIBConformance,
       "ciscoIdslLineMIBCompliances": ciscoIdslLineMIBCompliances,
       "ciscoIdslLineMIBCompliance": ciscoIdslLineMIBCompliance,
       "ciscoIdslLineMIBGroups": ciscoIdslLineMIBGroups,
       "cIdslBasicGroup": cIdslBasicGroup,
       "cIdslPM15MinIntervalGroup": cIdslPM15MinIntervalGroup}
)
