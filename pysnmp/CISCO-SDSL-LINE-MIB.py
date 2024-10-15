# SNMP MIB module (CISCO-SDSL-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SDSL-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:01 2024
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
 adslLineAlarmConfProfileName,
 adslLineConfProfileName) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "AdslLineProfileName",
    "adslLineAlarmConfProfileName",
    "adslLineConfProfileName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

ciscoSdslLineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 155)
)
ciscoSdslLineMIB.setRevisions(
        ("2001-08-20 10:00",
         "2001-04-09 10:13",
         "2001-01-30 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SdslPerfTimeElapsed(Gauge32, TextualConvention):
    status = "current"


class SdslPerfCurrDayCount(Gauge32, TextualConvention):
    status = "current"


class SdslPerfPrevDayCount(Gauge32, TextualConvention):
    status = "current"


class SdslStuxDefect(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoSdslLineMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSdslLineMIBObjects = _CiscoSdslLineMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1)
)
_CSdslLineTable_Object = MibTable
cSdslLineTable = _CSdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 1)
)
if mibBuilder.loadTexts:
    cSdslLineTable.setStatus("current")
_CSdslLineEntry_Object = MibTableRow
cSdslLineEntry = _CSdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 1, 1)
)
cSdslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cSdslLineEntry.setStatus("current")


class _CSdslLineCoding_Type(Integer32):
    """Custom type cSdslLineCoding based on Integer32"""
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
        *(("base2b1q", 2),
          ("cap", 5),
          ("optis", 4),
          ("other", 1),
          ("tcPam", 3))
    )


_CSdslLineCoding_Type.__name__ = "Integer32"
_CSdslLineCoding_Object = MibTableColumn
cSdslLineCoding = _CSdslLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 1, 1, 1),
    _CSdslLineCoding_Type()
)
cSdslLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslLineCoding.setStatus("current")


class _CSdslLineFraming_Type(Integer32):
    """Custom type cSdslLineFraming based on Integer32"""
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
        *(("ds1", 6),
          ("gShdsl", 4),
          ("hdsl", 3),
          ("hdsl2", 5),
          ("none", 1),
          ("other", 2))
    )


_CSdslLineFraming_Type.__name__ = "Integer32"
_CSdslLineFraming_Object = MibTableColumn
cSdslLineFraming = _CSdslLineFraming_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 1, 1, 2),
    _CSdslLineFraming_Type()
)
cSdslLineFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslLineFraming.setStatus("current")
_CSdslLineSpecific_Type = VariablePointer
_CSdslLineSpecific_Object = MibTableColumn
cSdslLineSpecific = _CSdslLineSpecific_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 1, 1, 3),
    _CSdslLineSpecific_Type()
)
cSdslLineSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslLineSpecific.setStatus("current")
_CSdslLineConfProfile_Type = AdslLineProfileName
_CSdslLineConfProfile_Object = MibTableColumn
cSdslLineConfProfile = _CSdslLineConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 1, 1, 4),
    _CSdslLineConfProfile_Type()
)
cSdslLineConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSdslLineConfProfile.setStatus("current")
_CSdslLineAlarmConfProfile_Type = AdslLineProfileName
_CSdslLineAlarmConfProfile_Object = MibTableColumn
cSdslLineAlarmConfProfile = _CSdslLineAlarmConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 1, 1, 5),
    _CSdslLineAlarmConfProfile_Type()
)
cSdslLineAlarmConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSdslLineAlarmConfProfile.setStatus("current")
_CSdslStucPhysTable_Object = MibTable
cSdslStucPhysTable = _CSdslStucPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2)
)
if mibBuilder.loadTexts:
    cSdslStucPhysTable.setStatus("current")
_CSdslStucPhysEntry_Object = MibTableRow
cSdslStucPhysEntry = _CSdslStucPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2, 1)
)
cSdslStucPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cSdslStucPhysEntry.setStatus("current")


class _CSdslStucInvSerialNumber_Type(SnmpAdminString):
    """Custom type cSdslStucInvSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CSdslStucInvSerialNumber_Type.__name__ = "SnmpAdminString"
_CSdslStucInvSerialNumber_Object = MibTableColumn
cSdslStucInvSerialNumber = _CSdslStucInvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2, 1, 1),
    _CSdslStucInvSerialNumber_Type()
)
cSdslStucInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucInvSerialNumber.setStatus("current")


class _CSdslStucInvVendorId_Type(SnmpAdminString):
    """Custom type cSdslStucInvVendorId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CSdslStucInvVendorId_Type.__name__ = "SnmpAdminString"
_CSdslStucInvVendorId_Object = MibTableColumn
cSdslStucInvVendorId = _CSdslStucInvVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2, 1, 2),
    _CSdslStucInvVendorId_Type()
)
cSdslStucInvVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucInvVendorId.setStatus("current")


class _CSdslStucInvVersionNumber_Type(SnmpAdminString):
    """Custom type cSdslStucInvVersionNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CSdslStucInvVersionNumber_Type.__name__ = "SnmpAdminString"
_CSdslStucInvVersionNumber_Object = MibTableColumn
cSdslStucInvVersionNumber = _CSdslStucInvVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2, 1, 3),
    _CSdslStucInvVersionNumber_Type()
)
cSdslStucInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucInvVersionNumber.setStatus("current")


class _CSdslStucState_Type(Integer32):
    """Custom type cSdslStucState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("downloadFailed", 7),
          ("downloading", 6),
          ("idle", 2),
          ("other", 1),
          ("steadyState", 4),
          ("testing", 5),
          ("training", 3))
    )


_CSdslStucState_Type.__name__ = "Integer32"
_CSdslStucState_Object = MibTableColumn
cSdslStucState = _CSdslStucState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2, 1, 4),
    _CSdslStucState_Type()
)
cSdslStucState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucState.setStatus("current")
_CSdslStucDefect_Type = SdslStuxDefect
_CSdslStucDefect_Object = MibTableColumn
cSdslStucDefect = _CSdslStucDefect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2, 1, 5),
    _CSdslStucDefect_Type()
)
cSdslStucDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucDefect.setStatus("current")


class _CSdslStucCurrRate_Type(Integer32):
    """Custom type cSdslStucCurrRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2320000),
    )


_CSdslStucCurrRate_Type.__name__ = "Integer32"
_CSdslStucCurrRate_Object = MibTableColumn
cSdslStucCurrRate = _CSdslStucCurrRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2, 1, 6),
    _CSdslStucCurrRate_Type()
)
cSdslStucCurrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucCurrRate.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucCurrRate.setUnits("bps")
_CSdslStucCurrSnrMgn_Type = Gauge32
_CSdslStucCurrSnrMgn_Object = MibTableColumn
cSdslStucCurrSnrMgn = _CSdslStucCurrSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2, 1, 7),
    _CSdslStucCurrSnrMgn_Type()
)
cSdslStucCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucCurrSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucCurrSnrMgn.setUnits("tenth dB")


class _CSdslStucCurrGain_Type(Integer32):
    """Custom type cSdslStucCurrGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_CSdslStucCurrGain_Type.__name__ = "Integer32"
_CSdslStucCurrGain_Object = MibTableColumn
cSdslStucCurrGain = _CSdslStucCurrGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2, 1, 8),
    _CSdslStucCurrGain_Type()
)
cSdslStucCurrGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucCurrGain.setStatus("deprecated")
if mibBuilder.loadTexts:
    cSdslStucCurrGain.setUnits("tenth dB")
_CSdslStucCurrOutputPwr_Type = Gauge32
_CSdslStucCurrOutputPwr_Object = MibTableColumn
cSdslStucCurrOutputPwr = _CSdslStucCurrOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2, 1, 9),
    _CSdslStucCurrOutputPwr_Type()
)
cSdslStucCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucCurrOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucCurrOutputPwr.setUnits("tenth dBm")
_CSdslStucCurrAtn_Type = Gauge32
_CSdslStucCurrAtn_Object = MibTableColumn
cSdslStucCurrAtn = _CSdslStucCurrAtn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2, 1, 10),
    _CSdslStucCurrAtn_Type()
)
cSdslStucCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucCurrAtn.setUnits("tenth dBm")
_CSdslStucCurrGainRev_Type = Integer32
_CSdslStucCurrGainRev_Object = MibTableColumn
cSdslStucCurrGainRev = _CSdslStucCurrGainRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 2, 1, 11),
    _CSdslStucCurrGainRev_Type()
)
cSdslStucCurrGainRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucCurrGainRev.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucCurrGainRev.setUnits("tenth dB")
_CSdslSturPhysTable_Object = MibTable
cSdslSturPhysTable = _CSdslSturPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3)
)
if mibBuilder.loadTexts:
    cSdslSturPhysTable.setStatus("current")
_CSdslSturPhysEntry_Object = MibTableRow
cSdslSturPhysEntry = _CSdslSturPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3, 1)
)
cSdslSturPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cSdslSturPhysEntry.setStatus("current")


class _CSdslSturInvSerialNumber_Type(SnmpAdminString):
    """Custom type cSdslSturInvSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CSdslSturInvSerialNumber_Type.__name__ = "SnmpAdminString"
_CSdslSturInvSerialNumber_Object = MibTableColumn
cSdslSturInvSerialNumber = _CSdslSturInvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3, 1, 1),
    _CSdslSturInvSerialNumber_Type()
)
cSdslSturInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturInvSerialNumber.setStatus("current")


class _CSdslSturInvVendorId_Type(SnmpAdminString):
    """Custom type cSdslSturInvVendorId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CSdslSturInvVendorId_Type.__name__ = "SnmpAdminString"
_CSdslSturInvVendorId_Object = MibTableColumn
cSdslSturInvVendorId = _CSdslSturInvVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3, 1, 2),
    _CSdslSturInvVendorId_Type()
)
cSdslSturInvVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturInvVendorId.setStatus("current")


class _CSdslSturInvVersionNumber_Type(SnmpAdminString):
    """Custom type cSdslSturInvVersionNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CSdslSturInvVersionNumber_Type.__name__ = "SnmpAdminString"
_CSdslSturInvVersionNumber_Object = MibTableColumn
cSdslSturInvVersionNumber = _CSdslSturInvVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3, 1, 3),
    _CSdslSturInvVersionNumber_Type()
)
cSdslSturInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturInvVersionNumber.setStatus("current")


class _CSdslSturState_Type(Integer32):
    """Custom type cSdslSturState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("steadyState", 3),
          ("training", 2))
    )


_CSdslSturState_Type.__name__ = "Integer32"
_CSdslSturState_Object = MibTableColumn
cSdslSturState = _CSdslSturState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3, 1, 4),
    _CSdslSturState_Type()
)
cSdslSturState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturState.setStatus("current")
_CSdslSturDefect_Type = SdslStuxDefect
_CSdslSturDefect_Object = MibTableColumn
cSdslSturDefect = _CSdslSturDefect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3, 1, 5),
    _CSdslSturDefect_Type()
)
cSdslSturDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturDefect.setStatus("current")


class _CSdslSturCurrRate_Type(Integer32):
    """Custom type cSdslSturCurrRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2320000),
    )


_CSdslSturCurrRate_Type.__name__ = "Integer32"
_CSdslSturCurrRate_Object = MibTableColumn
cSdslSturCurrRate = _CSdslSturCurrRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3, 1, 6),
    _CSdslSturCurrRate_Type()
)
cSdslSturCurrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturCurrRate.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturCurrRate.setUnits("bps")
_CSdslSturCurrSnrMgn_Type = Gauge32
_CSdslSturCurrSnrMgn_Object = MibTableColumn
cSdslSturCurrSnrMgn = _CSdslSturCurrSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3, 1, 7),
    _CSdslSturCurrSnrMgn_Type()
)
cSdslSturCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturCurrSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturCurrSnrMgn.setUnits("tenth dB")


class _CSdslSturCurrGain_Type(Integer32):
    """Custom type cSdslSturCurrGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_CSdslSturCurrGain_Type.__name__ = "Integer32"
_CSdslSturCurrGain_Object = MibTableColumn
cSdslSturCurrGain = _CSdslSturCurrGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3, 1, 8),
    _CSdslSturCurrGain_Type()
)
cSdslSturCurrGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturCurrGain.setStatus("deprecated")
if mibBuilder.loadTexts:
    cSdslSturCurrGain.setUnits("tenth dB")
_CSdslSturCurrOutputPwr_Type = Gauge32
_CSdslSturCurrOutputPwr_Object = MibTableColumn
cSdslSturCurrOutputPwr = _CSdslSturCurrOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3, 1, 9),
    _CSdslSturCurrOutputPwr_Type()
)
cSdslSturCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturCurrOutputPwr.setStatus("current")
_CSdslSturCurrAtn_Type = Gauge32
_CSdslSturCurrAtn_Object = MibTableColumn
cSdslSturCurrAtn = _CSdslSturCurrAtn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3, 1, 10),
    _CSdslSturCurrAtn_Type()
)
cSdslSturCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturCurrAtn.setUnits("tenth dBm")
_CSdslSturCurrGainRev_Type = Integer32
_CSdslSturCurrGainRev_Object = MibTableColumn
cSdslSturCurrGainRev = _CSdslSturCurrGainRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 3, 1, 11),
    _CSdslSturCurrGainRev_Type()
)
cSdslSturCurrGainRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturCurrGainRev.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturCurrGainRev.setUnits("tenth dB")
_CSdslStucPerfDataTable_Object = MibTable
cSdslStucPerfDataTable = _CSdslStucPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6)
)
if mibBuilder.loadTexts:
    cSdslStucPerfDataTable.setStatus("current")
_CSdslStucPerfDataEntry_Object = MibTableRow
cSdslStucPerfDataEntry = _CSdslStucPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1)
)
cSdslStucPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cSdslStucPerfDataEntry.setStatus("current")
_CSdslStucPerfLOSs_Type = Counter32
_CSdslStucPerfLOSs_Object = MibTableColumn
cSdslStucPerfLOSs = _CSdslStucPerfLOSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 1),
    _CSdslStucPerfLOSs_Type()
)
cSdslStucPerfLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfLOSs.setStatus("current")
_CSdslStucPerfLOSQs_Type = Counter32
_CSdslStucPerfLOSQs_Object = MibTableColumn
cSdslStucPerfLOSQs = _CSdslStucPerfLOSQs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 2),
    _CSdslStucPerfLOSQs_Type()
)
cSdslStucPerfLOSQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfLOSQs.setStatus("current")
_CSdslStucPerfCVs_Type = Counter32
_CSdslStucPerfCVs_Object = MibTableColumn
cSdslStucPerfCVs = _CSdslStucPerfCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 3),
    _CSdslStucPerfCVs_Type()
)
cSdslStucPerfCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCVs.setStatus("current")
_CSdslStucPerfESs_Type = Counter32
_CSdslStucPerfESs_Object = MibTableColumn
cSdslStucPerfESs = _CSdslStucPerfESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 4),
    _CSdslStucPerfESs_Type()
)
cSdslStucPerfESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfESs.setUnits("seconds")
_CSdslStucPerfSESs_Type = Counter32
_CSdslStucPerfSESs_Object = MibTableColumn
cSdslStucPerfSESs = _CSdslStucPerfSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 5),
    _CSdslStucPerfSESs_Type()
)
cSdslStucPerfSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfSESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfSESs.setUnits("seconds")
_CSdslStucPerfUASs_Type = Counter32
_CSdslStucPerfUASs_Object = MibTableColumn
cSdslStucPerfUASs = _CSdslStucPerfUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 6),
    _CSdslStucPerfUASs_Type()
)
cSdslStucPerfUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfUASs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfUASs.setUnits("seconds")
_CSdslStucPerfInits_Type = Counter32
_CSdslStucPerfInits_Object = MibTableColumn
cSdslStucPerfInits = _CSdslStucPerfInits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 7),
    _CSdslStucPerfInits_Type()
)
cSdslStucPerfInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfInits.setStatus("current")
_CSdslStucUnavailRsrcs_Type = Counter32
_CSdslStucUnavailRsrcs_Object = MibTableColumn
cSdslStucUnavailRsrcs = _CSdslStucUnavailRsrcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 8),
    _CSdslStucUnavailRsrcs_Type()
)
cSdslStucUnavailRsrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucUnavailRsrcs.setStatus("current")


class _CSdslStucPerfValidIntervals_Type(Integer32):
    """Custom type cSdslStucPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CSdslStucPerfValidIntervals_Type.__name__ = "Integer32"
_CSdslStucPerfValidIntervals_Object = MibTableColumn
cSdslStucPerfValidIntervals = _CSdslStucPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 9),
    _CSdslStucPerfValidIntervals_Type()
)
cSdslStucPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfValidIntervals.setStatus("current")


class _CSdslStucPerfInvalidIntervals_Type(Integer32):
    """Custom type cSdslStucPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CSdslStucPerfInvalidIntervals_Type.__name__ = "Integer32"
_CSdslStucPerfInvalidIntervals_Object = MibTableColumn
cSdslStucPerfInvalidIntervals = _CSdslStucPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 10),
    _CSdslStucPerfInvalidIntervals_Type()
)
cSdslStucPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfInvalidIntervals.setStatus("current")


class _CSdslStucPerfCurr15MinTimeElapse_Type(SdslPerfTimeElapsed):
    """Custom type cSdslStucPerfCurr15MinTimeElapse based on SdslPerfTimeElapsed"""
    subtypeSpec = SdslPerfTimeElapsed.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_CSdslStucPerfCurr15MinTimeElapse_Type.__name__ = "SdslPerfTimeElapsed"
_CSdslStucPerfCurr15MinTimeElapse_Object = MibTableColumn
cSdslStucPerfCurr15MinTimeElapse = _CSdslStucPerfCurr15MinTimeElapse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 11),
    _CSdslStucPerfCurr15MinTimeElapse_Type()
)
cSdslStucPerfCurr15MinTimeElapse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinTimeElapse.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinTimeElapse.setUnits("seconds")
_CSdslStucPerfCurr15MinLOSs_Type = PerfCurrentCount
_CSdslStucPerfCurr15MinLOSs_Object = MibTableColumn
cSdslStucPerfCurr15MinLOSs = _CSdslStucPerfCurr15MinLOSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 12),
    _CSdslStucPerfCurr15MinLOSs_Type()
)
cSdslStucPerfCurr15MinLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinLOSs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinLOSs.setUnits("seconds")
_CSdslStucPerfCurr15MinLOSQs_Type = PerfCurrentCount
_CSdslStucPerfCurr15MinLOSQs_Object = MibTableColumn
cSdslStucPerfCurr15MinLOSQs = _CSdslStucPerfCurr15MinLOSQs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 13),
    _CSdslStucPerfCurr15MinLOSQs_Type()
)
cSdslStucPerfCurr15MinLOSQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinLOSQs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinLOSQs.setUnits("seconds")
_CSdslStucPerfCurr15MinCVs_Type = PerfCurrentCount
_CSdslStucPerfCurr15MinCVs_Object = MibTableColumn
cSdslStucPerfCurr15MinCVs = _CSdslStucPerfCurr15MinCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 14),
    _CSdslStucPerfCurr15MinCVs_Type()
)
cSdslStucPerfCurr15MinCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinCVs.setStatus("current")
_CSdslStucPerfCurr15MinESs_Type = PerfCurrentCount
_CSdslStucPerfCurr15MinESs_Object = MibTableColumn
cSdslStucPerfCurr15MinESs = _CSdslStucPerfCurr15MinESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 15),
    _CSdslStucPerfCurr15MinESs_Type()
)
cSdslStucPerfCurr15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinESs.setUnits("seconds")
_CSdslStucPerfCurr15MinSESs_Type = PerfCurrentCount
_CSdslStucPerfCurr15MinSESs_Object = MibTableColumn
cSdslStucPerfCurr15MinSESs = _CSdslStucPerfCurr15MinSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 16),
    _CSdslStucPerfCurr15MinSESs_Type()
)
cSdslStucPerfCurr15MinSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinSESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinSESs.setUnits("seconds")
_CSdslStucPerfCurr15MinUASs_Type = PerfCurrentCount
_CSdslStucPerfCurr15MinUASs_Object = MibTableColumn
cSdslStucPerfCurr15MinUASs = _CSdslStucPerfCurr15MinUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 17),
    _CSdslStucPerfCurr15MinUASs_Type()
)
cSdslStucPerfCurr15MinUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinUASs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinUASs.setUnits("seconds")
_CSdslStucPerfCurr15MinInits_Type = PerfCurrentCount
_CSdslStucPerfCurr15MinInits_Object = MibTableColumn
cSdslStucPerfCurr15MinInits = _CSdslStucPerfCurr15MinInits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 18),
    _CSdslStucPerfCurr15MinInits_Type()
)
cSdslStucPerfCurr15MinInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinInits.setStatus("current")
_CSdslStucPerfCurr15MinUnavlRsrcs_Type = PerfCurrentCount
_CSdslStucPerfCurr15MinUnavlRsrcs_Object = MibTableColumn
cSdslStucPerfCurr15MinUnavlRsrcs = _CSdslStucPerfCurr15MinUnavlRsrcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 19),
    _CSdslStucPerfCurr15MinUnavlRsrcs_Type()
)
cSdslStucPerfCurr15MinUnavlRsrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr15MinUnavlRsrcs.setStatus("current")


class _CSdslStucPerfCurr1DayTimeElapsed_Type(SdslPerfTimeElapsed):
    """Custom type cSdslStucPerfCurr1DayTimeElapsed based on SdslPerfTimeElapsed"""
    subtypeSpec = SdslPerfTimeElapsed.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_CSdslStucPerfCurr1DayTimeElapsed_Type.__name__ = "SdslPerfTimeElapsed"
_CSdslStucPerfCurr1DayTimeElapsed_Object = MibTableColumn
cSdslStucPerfCurr1DayTimeElapsed = _CSdslStucPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 20),
    _CSdslStucPerfCurr1DayTimeElapsed_Type()
)
cSdslStucPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayTimeElapsed.setUnits("seconds")
_CSdslStucPerfCurr1DayLOSs_Type = SdslPerfCurrDayCount
_CSdslStucPerfCurr1DayLOSs_Object = MibTableColumn
cSdslStucPerfCurr1DayLOSs = _CSdslStucPerfCurr1DayLOSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 21),
    _CSdslStucPerfCurr1DayLOSs_Type()
)
cSdslStucPerfCurr1DayLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayLOSs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayLOSs.setUnits("seconds")
_CSdslStucPerfCurr1DayLOSQs_Type = SdslPerfCurrDayCount
_CSdslStucPerfCurr1DayLOSQs_Object = MibTableColumn
cSdslStucPerfCurr1DayLOSQs = _CSdslStucPerfCurr1DayLOSQs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 22),
    _CSdslStucPerfCurr1DayLOSQs_Type()
)
cSdslStucPerfCurr1DayLOSQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayLOSQs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayLOSQs.setUnits("seconds")
_CSdslStucPerfCurr1DayCVs_Type = SdslPerfCurrDayCount
_CSdslStucPerfCurr1DayCVs_Object = MibTableColumn
cSdslStucPerfCurr1DayCVs = _CSdslStucPerfCurr1DayCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 23),
    _CSdslStucPerfCurr1DayCVs_Type()
)
cSdslStucPerfCurr1DayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayCVs.setStatus("current")
_CSdslStucPerfCurr1DayESs_Type = SdslPerfCurrDayCount
_CSdslStucPerfCurr1DayESs_Object = MibTableColumn
cSdslStucPerfCurr1DayESs = _CSdslStucPerfCurr1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 24),
    _CSdslStucPerfCurr1DayESs_Type()
)
cSdslStucPerfCurr1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayESs.setUnits("seconds")
_CSdslStucPerfCurr1DaySESs_Type = SdslPerfCurrDayCount
_CSdslStucPerfCurr1DaySESs_Object = MibTableColumn
cSdslStucPerfCurr1DaySESs = _CSdslStucPerfCurr1DaySESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 25),
    _CSdslStucPerfCurr1DaySESs_Type()
)
cSdslStucPerfCurr1DaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DaySESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DaySESs.setUnits("seconds")
_CSdslStucPerfCurr1DayUASs_Type = SdslPerfCurrDayCount
_CSdslStucPerfCurr1DayUASs_Object = MibTableColumn
cSdslStucPerfCurr1DayUASs = _CSdslStucPerfCurr1DayUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 26),
    _CSdslStucPerfCurr1DayUASs_Type()
)
cSdslStucPerfCurr1DayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayUASs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayUASs.setUnits("seconds")
_CSdslStucPerfCurr1DayInits_Type = SdslPerfCurrDayCount
_CSdslStucPerfCurr1DayInits_Object = MibTableColumn
cSdslStucPerfCurr1DayInits = _CSdslStucPerfCurr1DayInits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 27),
    _CSdslStucPerfCurr1DayInits_Type()
)
cSdslStucPerfCurr1DayInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayInits.setStatus("current")
_CSdslStucPerfCurr1DayUnavlRsrcs_Type = SdslPerfCurrDayCount
_CSdslStucPerfCurr1DayUnavlRsrcs_Object = MibTableColumn
cSdslStucPerfCurr1DayUnavlRsrcs = _CSdslStucPerfCurr1DayUnavlRsrcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 28),
    _CSdslStucPerfCurr1DayUnavlRsrcs_Type()
)
cSdslStucPerfCurr1DayUnavlRsrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfCurr1DayUnavlRsrcs.setStatus("current")


class _CSdslStucPerfPrev1DayMoniSecs_Type(Integer32):
    """Custom type cSdslStucPerfPrev1DayMoniSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CSdslStucPerfPrev1DayMoniSecs_Type.__name__ = "Integer32"
_CSdslStucPerfPrev1DayMoniSecs_Object = MibTableColumn
cSdslStucPerfPrev1DayMoniSecs = _CSdslStucPerfPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 29),
    _CSdslStucPerfPrev1DayMoniSecs_Type()
)
cSdslStucPerfPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayMoniSecs.setUnits("seconds")
_CSdslStucPerfPrev1DayLOSs_Type = SdslPerfPrevDayCount
_CSdslStucPerfPrev1DayLOSs_Object = MibTableColumn
cSdslStucPerfPrev1DayLOSs = _CSdslStucPerfPrev1DayLOSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 30),
    _CSdslStucPerfPrev1DayLOSs_Type()
)
cSdslStucPerfPrev1DayLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayLOSs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayLOSs.setUnits("seconds")
_CSdslStucPerfPrev1DayLOSQs_Type = SdslPerfPrevDayCount
_CSdslStucPerfPrev1DayLOSQs_Object = MibTableColumn
cSdslStucPerfPrev1DayLOSQs = _CSdslStucPerfPrev1DayLOSQs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 31),
    _CSdslStucPerfPrev1DayLOSQs_Type()
)
cSdslStucPerfPrev1DayLOSQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayLOSQs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayLOSQs.setUnits("seconds")
_CSdslStucPerfPrev1DayCVs_Type = SdslPerfPrevDayCount
_CSdslStucPerfPrev1DayCVs_Object = MibTableColumn
cSdslStucPerfPrev1DayCVs = _CSdslStucPerfPrev1DayCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 32),
    _CSdslStucPerfPrev1DayCVs_Type()
)
cSdslStucPerfPrev1DayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayCVs.setStatus("current")
_CSdslStucPerfPrev1DayESs_Type = SdslPerfPrevDayCount
_CSdslStucPerfPrev1DayESs_Object = MibTableColumn
cSdslStucPerfPrev1DayESs = _CSdslStucPerfPrev1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 33),
    _CSdslStucPerfPrev1DayESs_Type()
)
cSdslStucPerfPrev1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayESs.setUnits("seconds")
_CSdslStucPerfPrev1DaySESs_Type = SdslPerfPrevDayCount
_CSdslStucPerfPrev1DaySESs_Object = MibTableColumn
cSdslStucPerfPrev1DaySESs = _CSdslStucPerfPrev1DaySESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 34),
    _CSdslStucPerfPrev1DaySESs_Type()
)
cSdslStucPerfPrev1DaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DaySESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DaySESs.setUnits("seconds")
_CSdslStucPerfPrev1DayUASs_Type = SdslPerfPrevDayCount
_CSdslStucPerfPrev1DayUASs_Object = MibTableColumn
cSdslStucPerfPrev1DayUASs = _CSdslStucPerfPrev1DayUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 35),
    _CSdslStucPerfPrev1DayUASs_Type()
)
cSdslStucPerfPrev1DayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayUASs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayUASs.setUnits("seconds")
_CSdslStucPerfPrev1DayInits_Type = SdslPerfPrevDayCount
_CSdslStucPerfPrev1DayInits_Object = MibTableColumn
cSdslStucPerfPrev1DayInits = _CSdslStucPerfPrev1DayInits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 36),
    _CSdslStucPerfPrev1DayInits_Type()
)
cSdslStucPerfPrev1DayInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayInits.setStatus("current")
_CSdslStucPerfPrev1DayUnavlRsrcs_Type = SdslPerfPrevDayCount
_CSdslStucPerfPrev1DayUnavlRsrcs_Object = MibTableColumn
cSdslStucPerfPrev1DayUnavlRsrcs = _CSdslStucPerfPrev1DayUnavlRsrcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 6, 1, 37),
    _CSdslStucPerfPrev1DayUnavlRsrcs_Type()
)
cSdslStucPerfPrev1DayUnavlRsrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucPerfPrev1DayUnavlRsrcs.setStatus("current")
_CSdslSturPerfDataTable_Object = MibTable
cSdslSturPerfDataTable = _CSdslSturPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7)
)
if mibBuilder.loadTexts:
    cSdslSturPerfDataTable.setStatus("current")
_CSdslSturPerfDataEntry_Object = MibTableRow
cSdslSturPerfDataEntry = _CSdslSturPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1)
)
cSdslSturPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cSdslSturPerfDataEntry.setStatus("current")
_CSdslSturPerfLOSs_Type = Counter32
_CSdslSturPerfLOSs_Object = MibTableColumn
cSdslSturPerfLOSs = _CSdslSturPerfLOSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 1),
    _CSdslSturPerfLOSs_Type()
)
cSdslSturPerfLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfLOSs.setStatus("current")
_CSdslSturPerfLOSQs_Type = Counter32
_CSdslSturPerfLOSQs_Object = MibTableColumn
cSdslSturPerfLOSQs = _CSdslSturPerfLOSQs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 2),
    _CSdslSturPerfLOSQs_Type()
)
cSdslSturPerfLOSQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfLOSQs.setStatus("current")
_CSdslSturPerfCVs_Type = Counter32
_CSdslSturPerfCVs_Object = MibTableColumn
cSdslSturPerfCVs = _CSdslSturPerfCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 3),
    _CSdslSturPerfCVs_Type()
)
cSdslSturPerfCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCVs.setStatus("current")
_CSdslSturPerfESs_Type = Counter32
_CSdslSturPerfESs_Object = MibTableColumn
cSdslSturPerfESs = _CSdslSturPerfESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 4),
    _CSdslSturPerfESs_Type()
)
cSdslSturPerfESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfESs.setUnits("seconds")
_CSdslSturPerfSESs_Type = Counter32
_CSdslSturPerfSESs_Object = MibTableColumn
cSdslSturPerfSESs = _CSdslSturPerfSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 5),
    _CSdslSturPerfSESs_Type()
)
cSdslSturPerfSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfSESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfSESs.setUnits("seconds")
_CSdslSturPerfUASs_Type = Counter32
_CSdslSturPerfUASs_Object = MibTableColumn
cSdslSturPerfUASs = _CSdslSturPerfUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 6),
    _CSdslSturPerfUASs_Type()
)
cSdslSturPerfUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfUASs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfUASs.setUnits("seconds")


class _CSdslSturPerfValidIntervals_Type(Integer32):
    """Custom type cSdslSturPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CSdslSturPerfValidIntervals_Type.__name__ = "Integer32"
_CSdslSturPerfValidIntervals_Object = MibTableColumn
cSdslSturPerfValidIntervals = _CSdslSturPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 7),
    _CSdslSturPerfValidIntervals_Type()
)
cSdslSturPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfValidIntervals.setStatus("current")


class _CSdslSturPerfInvalidIntervals_Type(Integer32):
    """Custom type cSdslSturPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CSdslSturPerfInvalidIntervals_Type.__name__ = "Integer32"
_CSdslSturPerfInvalidIntervals_Object = MibTableColumn
cSdslSturPerfInvalidIntervals = _CSdslSturPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 8),
    _CSdslSturPerfInvalidIntervals_Type()
)
cSdslSturPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfInvalidIntervals.setStatus("current")


class _CSdslSturPerfCurr15MinTimeElapse_Type(SdslPerfTimeElapsed):
    """Custom type cSdslSturPerfCurr15MinTimeElapse based on SdslPerfTimeElapsed"""
    subtypeSpec = SdslPerfTimeElapsed.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_CSdslSturPerfCurr15MinTimeElapse_Type.__name__ = "SdslPerfTimeElapsed"
_CSdslSturPerfCurr15MinTimeElapse_Object = MibTableColumn
cSdslSturPerfCurr15MinTimeElapse = _CSdslSturPerfCurr15MinTimeElapse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 9),
    _CSdslSturPerfCurr15MinTimeElapse_Type()
)
cSdslSturPerfCurr15MinTimeElapse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinTimeElapse.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinTimeElapse.setUnits("seconds")
_CSdslSturPerfCurr15MinLOSs_Type = PerfCurrentCount
_CSdslSturPerfCurr15MinLOSs_Object = MibTableColumn
cSdslSturPerfCurr15MinLOSs = _CSdslSturPerfCurr15MinLOSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 10),
    _CSdslSturPerfCurr15MinLOSs_Type()
)
cSdslSturPerfCurr15MinLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinLOSs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinLOSs.setUnits("seconds")
_CSdslSturPerfCurr15MinLOSQs_Type = PerfCurrentCount
_CSdslSturPerfCurr15MinLOSQs_Object = MibTableColumn
cSdslSturPerfCurr15MinLOSQs = _CSdslSturPerfCurr15MinLOSQs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 11),
    _CSdslSturPerfCurr15MinLOSQs_Type()
)
cSdslSturPerfCurr15MinLOSQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinLOSQs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinLOSQs.setUnits("seconds")
_CSdslSturPerfCurr15MinCVs_Type = PerfCurrentCount
_CSdslSturPerfCurr15MinCVs_Object = MibTableColumn
cSdslSturPerfCurr15MinCVs = _CSdslSturPerfCurr15MinCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 12),
    _CSdslSturPerfCurr15MinCVs_Type()
)
cSdslSturPerfCurr15MinCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinCVs.setStatus("current")
_CSdslSturPerfCurr15MinESs_Type = PerfCurrentCount
_CSdslSturPerfCurr15MinESs_Object = MibTableColumn
cSdslSturPerfCurr15MinESs = _CSdslSturPerfCurr15MinESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 13),
    _CSdslSturPerfCurr15MinESs_Type()
)
cSdslSturPerfCurr15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinESs.setUnits("seconds")
_CSdslSturPerfCurr15MinSESs_Type = PerfCurrentCount
_CSdslSturPerfCurr15MinSESs_Object = MibTableColumn
cSdslSturPerfCurr15MinSESs = _CSdslSturPerfCurr15MinSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 14),
    _CSdslSturPerfCurr15MinSESs_Type()
)
cSdslSturPerfCurr15MinSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinSESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinSESs.setUnits("seconds")
_CSdslSturPerfCurr15MinUASs_Type = PerfCurrentCount
_CSdslSturPerfCurr15MinUASs_Object = MibTableColumn
cSdslSturPerfCurr15MinUASs = _CSdslSturPerfCurr15MinUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 15),
    _CSdslSturPerfCurr15MinUASs_Type()
)
cSdslSturPerfCurr15MinUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinUASs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr15MinUASs.setUnits("seconds")


class _CSdslSturPerfCurr1DayTimeElapsed_Type(SdslPerfTimeElapsed):
    """Custom type cSdslSturPerfCurr1DayTimeElapsed based on SdslPerfTimeElapsed"""
    subtypeSpec = SdslPerfTimeElapsed.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_CSdslSturPerfCurr1DayTimeElapsed_Type.__name__ = "SdslPerfTimeElapsed"
_CSdslSturPerfCurr1DayTimeElapsed_Object = MibTableColumn
cSdslSturPerfCurr1DayTimeElapsed = _CSdslSturPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 16),
    _CSdslSturPerfCurr1DayTimeElapsed_Type()
)
cSdslSturPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DayTimeElapsed.setUnits("seconds")
_CSdslSturPerfCurr1DayLOSs_Type = SdslPerfCurrDayCount
_CSdslSturPerfCurr1DayLOSs_Object = MibTableColumn
cSdslSturPerfCurr1DayLOSs = _CSdslSturPerfCurr1DayLOSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 17),
    _CSdslSturPerfCurr1DayLOSs_Type()
)
cSdslSturPerfCurr1DayLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DayLOSs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DayLOSs.setUnits("seconds")
_CSdslSturPerfCurr1DayLOSQs_Type = SdslPerfCurrDayCount
_CSdslSturPerfCurr1DayLOSQs_Object = MibTableColumn
cSdslSturPerfCurr1DayLOSQs = _CSdslSturPerfCurr1DayLOSQs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 18),
    _CSdslSturPerfCurr1DayLOSQs_Type()
)
cSdslSturPerfCurr1DayLOSQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DayLOSQs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DayLOSQs.setUnits("seconds")
_CSdslSturPerfCurr1DayCVs_Type = SdslPerfCurrDayCount
_CSdslSturPerfCurr1DayCVs_Object = MibTableColumn
cSdslSturPerfCurr1DayCVs = _CSdslSturPerfCurr1DayCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 19),
    _CSdslSturPerfCurr1DayCVs_Type()
)
cSdslSturPerfCurr1DayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DayCVs.setStatus("current")
_CSdslSturPerfCurr1DayESs_Type = SdslPerfCurrDayCount
_CSdslSturPerfCurr1DayESs_Object = MibTableColumn
cSdslSturPerfCurr1DayESs = _CSdslSturPerfCurr1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 20),
    _CSdslSturPerfCurr1DayESs_Type()
)
cSdslSturPerfCurr1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DayESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DayESs.setUnits("seconds")
_CSdslSturPerfCurr1DaySESs_Type = SdslPerfCurrDayCount
_CSdslSturPerfCurr1DaySESs_Object = MibTableColumn
cSdslSturPerfCurr1DaySESs = _CSdslSturPerfCurr1DaySESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 21),
    _CSdslSturPerfCurr1DaySESs_Type()
)
cSdslSturPerfCurr1DaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DaySESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DaySESs.setUnits("seconds")
_CSdslSturPerfCurr1DayUASs_Type = SdslPerfCurrDayCount
_CSdslSturPerfCurr1DayUASs_Object = MibTableColumn
cSdslSturPerfCurr1DayUASs = _CSdslSturPerfCurr1DayUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 22),
    _CSdslSturPerfCurr1DayUASs_Type()
)
cSdslSturPerfCurr1DayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DayUASs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfCurr1DayUASs.setUnits("seconds")


class _CSdslSturPerfPrev1DayMoniSecs_Type(Integer32):
    """Custom type cSdslSturPerfPrev1DayMoniSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CSdslSturPerfPrev1DayMoniSecs_Type.__name__ = "Integer32"
_CSdslSturPerfPrev1DayMoniSecs_Object = MibTableColumn
cSdslSturPerfPrev1DayMoniSecs = _CSdslSturPerfPrev1DayMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 23),
    _CSdslSturPerfPrev1DayMoniSecs_Type()
)
cSdslSturPerfPrev1DayMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DayMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DayMoniSecs.setUnits("seconds")
_CSdslSturPerfPrev1DayLOSs_Type = SdslPerfPrevDayCount
_CSdslSturPerfPrev1DayLOSs_Object = MibTableColumn
cSdslSturPerfPrev1DayLOSs = _CSdslSturPerfPrev1DayLOSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 24),
    _CSdslSturPerfPrev1DayLOSs_Type()
)
cSdslSturPerfPrev1DayLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DayLOSs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DayLOSs.setUnits("seconds")
_CSdslSturPerfPrev1DayLOSQs_Type = SdslPerfPrevDayCount
_CSdslSturPerfPrev1DayLOSQs_Object = MibTableColumn
cSdslSturPerfPrev1DayLOSQs = _CSdslSturPerfPrev1DayLOSQs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 25),
    _CSdslSturPerfPrev1DayLOSQs_Type()
)
cSdslSturPerfPrev1DayLOSQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DayLOSQs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DayLOSQs.setUnits("seconds")
_CSdslSturPerfPrev1DayCVs_Type = SdslPerfPrevDayCount
_CSdslSturPerfPrev1DayCVs_Object = MibTableColumn
cSdslSturPerfPrev1DayCVs = _CSdslSturPerfPrev1DayCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 26),
    _CSdslSturPerfPrev1DayCVs_Type()
)
cSdslSturPerfPrev1DayCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DayCVs.setStatus("current")
_CSdslSturPerfPrev1DayESs_Type = SdslPerfPrevDayCount
_CSdslSturPerfPrev1DayESs_Object = MibTableColumn
cSdslSturPerfPrev1DayESs = _CSdslSturPerfPrev1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 27),
    _CSdslSturPerfPrev1DayESs_Type()
)
cSdslSturPerfPrev1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DayESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DayESs.setUnits("seconds")
_CSdslSturPerfPrev1DaySESs_Type = SdslPerfPrevDayCount
_CSdslSturPerfPrev1DaySESs_Object = MibTableColumn
cSdslSturPerfPrev1DaySESs = _CSdslSturPerfPrev1DaySESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 28),
    _CSdslSturPerfPrev1DaySESs_Type()
)
cSdslSturPerfPrev1DaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DaySESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DaySESs.setUnits("seconds")
_CSdslSturPerfPrev1DayUASs_Type = SdslPerfPrevDayCount
_CSdslSturPerfPrev1DayUASs_Object = MibTableColumn
cSdslSturPerfPrev1DayUASs = _CSdslSturPerfPrev1DayUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 7, 1, 29),
    _CSdslSturPerfPrev1DayUASs_Type()
)
cSdslSturPerfPrev1DayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DayUASs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturPerfPrev1DayUASs.setUnits("seconds")
_CSdslStucIntervalTable_Object = MibTable
cSdslStucIntervalTable = _CSdslStucIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 8)
)
if mibBuilder.loadTexts:
    cSdslStucIntervalTable.setStatus("current")
_CSdslStucIntervalEntry_Object = MibTableRow
cSdslStucIntervalEntry = _CSdslStucIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 8, 1)
)
cSdslStucIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SDSL-LINE-MIB", "cSdslStucIntervalNumber"),
)
if mibBuilder.loadTexts:
    cSdslStucIntervalEntry.setStatus("current")


class _CSdslStucIntervalNumber_Type(Integer32):
    """Custom type cSdslStucIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CSdslStucIntervalNumber_Type.__name__ = "Integer32"
_CSdslStucIntervalNumber_Object = MibTableColumn
cSdslStucIntervalNumber = _CSdslStucIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 8, 1, 1),
    _CSdslStucIntervalNumber_Type()
)
cSdslStucIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSdslStucIntervalNumber.setStatus("current")
_CSdslStucIntervalValidData_Type = TruthValue
_CSdslStucIntervalValidData_Object = MibTableColumn
cSdslStucIntervalValidData = _CSdslStucIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 8, 1, 2),
    _CSdslStucIntervalValidData_Type()
)
cSdslStucIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucIntervalValidData.setStatus("current")
_CSdslStucIntervalLOSs_Type = PerfIntervalCount
_CSdslStucIntervalLOSs_Object = MibTableColumn
cSdslStucIntervalLOSs = _CSdslStucIntervalLOSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 8, 1, 3),
    _CSdslStucIntervalLOSs_Type()
)
cSdslStucIntervalLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucIntervalLOSs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucIntervalLOSs.setUnits("seconds")
_CSdslStucIntervalLOSQs_Type = PerfIntervalCount
_CSdslStucIntervalLOSQs_Object = MibTableColumn
cSdslStucIntervalLOSQs = _CSdslStucIntervalLOSQs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 8, 1, 4),
    _CSdslStucIntervalLOSQs_Type()
)
cSdslStucIntervalLOSQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucIntervalLOSQs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucIntervalLOSQs.setUnits("seconds")
_CSdslStucIntervalCVs_Type = PerfIntervalCount
_CSdslStucIntervalCVs_Object = MibTableColumn
cSdslStucIntervalCVs = _CSdslStucIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 8, 1, 5),
    _CSdslStucIntervalCVs_Type()
)
cSdslStucIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucIntervalCVs.setStatus("current")
_CSdslStucIntervalESs_Type = PerfIntervalCount
_CSdslStucIntervalESs_Object = MibTableColumn
cSdslStucIntervalESs = _CSdslStucIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 8, 1, 6),
    _CSdslStucIntervalESs_Type()
)
cSdslStucIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucIntervalESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucIntervalESs.setUnits("seconds")
_CSdslStucIntervalSESs_Type = PerfIntervalCount
_CSdslStucIntervalSESs_Object = MibTableColumn
cSdslStucIntervalSESs = _CSdslStucIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 8, 1, 7),
    _CSdslStucIntervalSESs_Type()
)
cSdslStucIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucIntervalSESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucIntervalSESs.setUnits("seconds")
_CSdslStucIntervalUASs_Type = PerfIntervalCount
_CSdslStucIntervalUASs_Object = MibTableColumn
cSdslStucIntervalUASs = _CSdslStucIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 8, 1, 8),
    _CSdslStucIntervalUASs_Type()
)
cSdslStucIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucIntervalUASs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucIntervalUASs.setUnits("seconds")
_CSdslStucIntervalInits_Type = PerfIntervalCount
_CSdslStucIntervalInits_Object = MibTableColumn
cSdslStucIntervalInits = _CSdslStucIntervalInits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 8, 1, 9),
    _CSdslStucIntervalInits_Type()
)
cSdslStucIntervalInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucIntervalInits.setStatus("current")
_CSdslStucIntervalUnavlRsrcs_Type = PerfIntervalCount
_CSdslStucIntervalUnavlRsrcs_Object = MibTableColumn
cSdslStucIntervalUnavlRsrcs = _CSdslStucIntervalUnavlRsrcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 8, 1, 10),
    _CSdslStucIntervalUnavlRsrcs_Type()
)
cSdslStucIntervalUnavlRsrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslStucIntervalUnavlRsrcs.setStatus("current")
_CSdslSturIntervalTable_Object = MibTable
cSdslSturIntervalTable = _CSdslSturIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 9)
)
if mibBuilder.loadTexts:
    cSdslSturIntervalTable.setStatus("current")
_CSdslSturIntervalEntry_Object = MibTableRow
cSdslSturIntervalEntry = _CSdslSturIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 9, 1)
)
cSdslSturIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SDSL-LINE-MIB", "cSdslSturIntervalNumber"),
)
if mibBuilder.loadTexts:
    cSdslSturIntervalEntry.setStatus("current")


class _CSdslSturIntervalNumber_Type(Integer32):
    """Custom type cSdslSturIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CSdslSturIntervalNumber_Type.__name__ = "Integer32"
_CSdslSturIntervalNumber_Object = MibTableColumn
cSdslSturIntervalNumber = _CSdslSturIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 9, 1, 1),
    _CSdslSturIntervalNumber_Type()
)
cSdslSturIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSdslSturIntervalNumber.setStatus("current")
_CSdslSturIntervalValidData_Type = TruthValue
_CSdslSturIntervalValidData_Object = MibTableColumn
cSdslSturIntervalValidData = _CSdslSturIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 9, 1, 2),
    _CSdslSturIntervalValidData_Type()
)
cSdslSturIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturIntervalValidData.setStatus("current")
_CSdslSturIntervalLOSs_Type = PerfIntervalCount
_CSdslSturIntervalLOSs_Object = MibTableColumn
cSdslSturIntervalLOSs = _CSdslSturIntervalLOSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 9, 1, 3),
    _CSdslSturIntervalLOSs_Type()
)
cSdslSturIntervalLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturIntervalLOSs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturIntervalLOSs.setUnits("seconds")
_CSdslSturIntervalLOSQs_Type = PerfIntervalCount
_CSdslSturIntervalLOSQs_Object = MibTableColumn
cSdslSturIntervalLOSQs = _CSdslSturIntervalLOSQs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 9, 1, 4),
    _CSdslSturIntervalLOSQs_Type()
)
cSdslSturIntervalLOSQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturIntervalLOSQs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturIntervalLOSQs.setUnits("seconds")
_CSdslSturIntervalCVs_Type = PerfIntervalCount
_CSdslSturIntervalCVs_Object = MibTableColumn
cSdslSturIntervalCVs = _CSdslSturIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 9, 1, 5),
    _CSdslSturIntervalCVs_Type()
)
cSdslSturIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturIntervalCVs.setStatus("current")
_CSdslSturIntervalESs_Type = PerfIntervalCount
_CSdslSturIntervalESs_Object = MibTableColumn
cSdslSturIntervalESs = _CSdslSturIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 9, 1, 6),
    _CSdslSturIntervalESs_Type()
)
cSdslSturIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturIntervalESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturIntervalESs.setUnits("seconds")
_CSdslSturIntervalSESs_Type = PerfIntervalCount
_CSdslSturIntervalSESs_Object = MibTableColumn
cSdslSturIntervalSESs = _CSdslSturIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 9, 1, 7),
    _CSdslSturIntervalSESs_Type()
)
cSdslSturIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturIntervalSESs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturIntervalSESs.setUnits("seconds")
_CSdslSturIntervalUASs_Type = PerfIntervalCount
_CSdslSturIntervalUASs_Object = MibTableColumn
cSdslSturIntervalUASs = _CSdslSturIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 9, 1, 8),
    _CSdslSturIntervalUASs_Type()
)
cSdslSturIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSdslSturIntervalUASs.setStatus("current")
if mibBuilder.loadTexts:
    cSdslSturIntervalUASs.setUnits("seconds")
_CSdslLineConfProfileTable_Object = MibTable
cSdslLineConfProfileTable = _CSdslLineConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14)
)
if mibBuilder.loadTexts:
    cSdslLineConfProfileTable.setStatus("current")
_CSdslLineConfProfileEntry_Object = MibTableRow
cSdslLineConfProfileEntry = _CSdslLineConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1)
)
cSdslLineConfProfileEntry.setIndexNames(
    (1, "ADSL-LINE-MIB", "adslLineConfProfileName"),
)
if mibBuilder.loadTexts:
    cSdslLineConfProfileEntry.setStatus("current")


class _CSdslLineMaxRate_Type(Integer32):
    """Custom type cSdslLineMaxRate based on Integer32"""
    defaultValue = 784000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(144000, 144000),
        ValueRangeConstraint(272000, 272000),
        ValueRangeConstraint(400000, 400000),
        ValueRangeConstraint(528000, 528000),
        ValueRangeConstraint(784000, 784000),
        ValueRangeConstraint(1040000, 1040000),
        ValueRangeConstraint(1168000, 1168000),
        ValueRangeConstraint(1552000, 1552000),
        ValueRangeConstraint(2064000, 2064000),
        ValueRangeConstraint(2320000, 2320000),
    )


_CSdslLineMaxRate_Type.__name__ = "Integer32"
_CSdslLineMaxRate_Object = MibTableColumn
cSdslLineMaxRate = _CSdslLineMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 1),
    _CSdslLineMaxRate_Type()
)
cSdslLineMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslLineMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    cSdslLineMaxRate.setUnits("bps")


class _CSdslLineFramingMode_Type(Integer32):
    """Custom type cSdslLineFramingMode based on Integer32"""
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
        *(("ds1", 6),
          ("gShdsl", 4),
          ("hdsl", 3),
          ("hdsl2", 5),
          ("none", 1),
          ("other", 2))
    )


_CSdslLineFramingMode_Type.__name__ = "Integer32"
_CSdslLineFramingMode_Object = MibTableColumn
cSdslLineFramingMode = _CSdslLineFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 2),
    _CSdslLineFramingMode_Type()
)
cSdslLineFramingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslLineFramingMode.setStatus("current")


class _CSdslStucTargetSnrMgn_Type(Integer32):
    """Custom type cSdslStucTargetSnrMgn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_CSdslStucTargetSnrMgn_Type.__name__ = "Integer32"
_CSdslStucTargetSnrMgn_Object = MibTableColumn
cSdslStucTargetSnrMgn = _CSdslStucTargetSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 3),
    _CSdslStucTargetSnrMgn_Type()
)
cSdslStucTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslStucTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucTargetSnrMgn.setUnits("tenth dB")


class _CSdslStucMaxSnrMgn_Type(Integer32):
    """Custom type cSdslStucMaxSnrMgn based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_CSdslStucMaxSnrMgn_Type.__name__ = "Integer32"
_CSdslStucMaxSnrMgn_Object = MibTableColumn
cSdslStucMaxSnrMgn = _CSdslStucMaxSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 4),
    _CSdslStucMaxSnrMgn_Type()
)
cSdslStucMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslStucMaxSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucMaxSnrMgn.setUnits("tenth dB")


class _CSdslStucMinSnrMgn_Type(Integer32):
    """Custom type cSdslStucMinSnrMgn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_CSdslStucMinSnrMgn_Type.__name__ = "Integer32"
_CSdslStucMinSnrMgn_Object = MibTableColumn
cSdslStucMinSnrMgn = _CSdslStucMinSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 5),
    _CSdslStucMinSnrMgn_Type()
)
cSdslStucMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslStucMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucMinSnrMgn.setUnits("tenth dB")


class _CSdslStucOutputPwr_Type(Integer32):
    """Custom type cSdslStucOutputPwr based on Integer32"""
    defaultValue = 130

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_CSdslStucOutputPwr_Type.__name__ = "Integer32"
_CSdslStucOutputPwr_Object = MibTableColumn
cSdslStucOutputPwr = _CSdslStucOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 6),
    _CSdslStucOutputPwr_Type()
)
cSdslStucOutputPwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslStucOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucOutputPwr.setUnits("tenth dBm")


class _CSdslShdslLineMaxRate_Type(Integer32):
    """Custom type cSdslShdslLineMaxRate based on Integer32"""
    defaultValue = 776000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(72000,
              136000,
              200000,
              264000,
              392000,
              520000,
              776000,
              784000,
              1032000,
              1160000,
              1544000,
              1552000,
              2056000,
              2312000,
              2376000)
        )
    )
    namedValues = NamedValues(
        *(("r1032000", 1032000),
          ("r1160000", 1160000),
          ("r136000", 136000),
          ("r1544000", 1544000),
          ("r1552000", 1552000),
          ("r200000", 200000),
          ("r2056000", 2056000),
          ("r2312000", 2312000),
          ("r2376000", 2376000),
          ("r264000", 264000),
          ("r392000", 392000),
          ("r520000", 520000),
          ("r72000", 72000),
          ("r776000", 776000),
          ("r784000", 784000))
    )


_CSdslShdslLineMaxRate_Type.__name__ = "Integer32"
_CSdslShdslLineMaxRate_Object = MibTableColumn
cSdslShdslLineMaxRate = _CSdslShdslLineMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 7),
    _CSdslShdslLineMaxRate_Type()
)
cSdslShdslLineMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslShdslLineMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    cSdslShdslLineMaxRate.setUnits("bps")


class _CSdslStucPsdMaskType_Type(Integer32):
    """Custom type cSdslStucPsdMaskType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asymmetric", 2),
          ("symmetric", 1))
    )


_CSdslStucPsdMaskType_Type.__name__ = "Integer32"
_CSdslStucPsdMaskType_Object = MibTableColumn
cSdslStucPsdMaskType = _CSdslStucPsdMaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 8),
    _CSdslStucPsdMaskType_Type()
)
cSdslStucPsdMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslStucPsdMaskType.setStatus("current")


class _CSdslStucAnnex_Type(Integer32):
    """Custom type cSdslStucAnnex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 1),
          ("annexB", 2))
    )


_CSdslStucAnnex_Type.__name__ = "Integer32"
_CSdslStucAnnex_Object = MibTableColumn
cSdslStucAnnex = _CSdslStucAnnex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 9),
    _CSdslStucAnnex_Type()
)
cSdslStucAnnex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslStucAnnex.setStatus("current")


class _CSdslLineEquipmentType_Type(Integer32):
    """Custom type cSdslLineEquipmentType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stuC", 2),
          ("stuR", 1))
    )


_CSdslLineEquipmentType_Type.__name__ = "Integer32"
_CSdslLineEquipmentType_Object = MibTableColumn
cSdslLineEquipmentType = _CSdslLineEquipmentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 10),
    _CSdslLineEquipmentType_Type()
)
cSdslLineEquipmentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslLineEquipmentType.setStatus("current")


class _CSdslLineAutoRateEnable_Type(TruthValue):
    """Custom type cSdslLineAutoRateEnable based on TruthValue"""


_CSdslLineAutoRateEnable_Object = MibTableColumn
cSdslLineAutoRateEnable = _CSdslLineAutoRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 11),
    _CSdslLineAutoRateEnable_Type()
)
cSdslLineAutoRateEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslLineAutoRateEnable.setStatus("current")


class _CSdslStucThresholdSnrMgn_Type(Integer32):
    """Custom type cSdslStucThresholdSnrMgn based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_CSdslStucThresholdSnrMgn_Type.__name__ = "Integer32"
_CSdslStucThresholdSnrMgn_Object = MibTableColumn
cSdslStucThresholdSnrMgn = _CSdslStucThresholdSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 12),
    _CSdslStucThresholdSnrMgn_Type()
)
cSdslStucThresholdSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslStucThresholdSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucThresholdSnrMgn.setUnits("tenth dB")


class _CSdslSturAnnex_Type(Integer32):
    """Custom type cSdslSturAnnex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 1),
          ("annexB", 2))
    )


_CSdslSturAnnex_Type.__name__ = "Integer32"
_CSdslSturAnnex_Object = MibTableColumn
cSdslSturAnnex = _CSdslSturAnnex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 14, 1, 13),
    _CSdslSturAnnex_Type()
)
cSdslSturAnnex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslSturAnnex.setStatus("current")
_CSdslLineAlarmConfProfileTable_Object = MibTable
cSdslLineAlarmConfProfileTable = _CSdslLineAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 15)
)
if mibBuilder.loadTexts:
    cSdslLineAlarmConfProfileTable.setStatus("current")
_CSdslLineAlarmConfProfileEntry_Object = MibTableRow
cSdslLineAlarmConfProfileEntry = _CSdslLineAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 15, 1)
)
cSdslLineAlarmConfProfileEntry.setIndexNames(
    (1, "ADSL-LINE-MIB", "adslLineAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    cSdslLineAlarmConfProfileEntry.setStatus("current")


class _CSdslStucThreshMinRate_Type(Integer32):
    """Custom type cSdslStucThreshMinRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_CSdslStucThreshMinRate_Type.__name__ = "Integer32"
_CSdslStucThreshMinRate_Object = MibTableColumn
cSdslStucThreshMinRate = _CSdslStucThreshMinRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 15, 1, 1),
    _CSdslStucThreshMinRate_Type()
)
cSdslStucThreshMinRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslStucThreshMinRate.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucThreshMinRate.setUnits("bps")


class _CSdslStucThreshMinSnrMgn_Type(Integer32):
    """Custom type cSdslStucThreshMinSnrMgn based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_CSdslStucThreshMinSnrMgn_Type.__name__ = "Integer32"
_CSdslStucThreshMinSnrMgn_Object = MibTableColumn
cSdslStucThreshMinSnrMgn = _CSdslStucThreshMinSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 1, 15, 1, 2),
    _CSdslStucThreshMinSnrMgn_Type()
)
cSdslStucThreshMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSdslStucThreshMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    cSdslStucThreshMinSnrMgn.setUnits("tenth dB")
_CiscoSdslLineMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoSdslLineMIBNotificationsPrefix = _CiscoSdslLineMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 2)
)
_CiscoSdslLineMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoSdslLineMIBNotifications = _CiscoSdslLineMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 2, 0)
)
_CiscoSdslLineMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSdslLineMIBConformance = _CiscoSdslLineMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3)
)
_CiscoSdslLineMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSdslLineMIBCompliances = _CiscoSdslLineMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 1)
)
_CiscoSdslLineMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSdslLineMIBGroups = _CiscoSdslLineMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2)
)

# Managed Objects groups

cSdslStucBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 1)
)
cSdslStucBasicGroup.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslLineCoding"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineFraming"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineSpecific"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineConfProfile"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineAlarmConfProfile"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucInvSerialNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucInvVendorId"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucInvVersionNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucState"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucDefect"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrGain"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrOutputPwr"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrAtn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineMaxRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineFramingMode"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucTargetSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucOutputPwr"))
)
if mibBuilder.loadTexts:
    cSdslStucBasicGroup.setStatus("deprecated")

cSdslSturBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 2)
)
cSdslSturBasicGroup.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslLineCoding"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineFraming"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineSpecific"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvSerialNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvVendorId"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvVersionNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturState"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturDefect"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrGain"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrOutputPwr"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrAtn"))
)
if mibBuilder.loadTexts:
    cSdslSturBasicGroup.setStatus("deprecated")

cSdslSturGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 3)
)
cSdslSturGroup.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslSturInvSerialNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvVendorId"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvVersionNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturState"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturDefect"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrGain"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrOutputPwr"))
)
if mibBuilder.loadTexts:
    cSdslSturGroup.setStatus("deprecated")

cSdslStucPMCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 4)
)
cSdslStucPMCounterGroup.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslStucPerfLOSs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfLOSQs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCVs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfSESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfUASs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfInits"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucUnavailRsrcs"))
)
if mibBuilder.loadTexts:
    cSdslStucPMCounterGroup.setStatus("current")

cSdslStucPM15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 5)
)
cSdslStucPM15MinIntervalGroup.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslStucPerfValidIntervals"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfInvalidIntervals"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr15MinTimeElapse"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr15MinLOSs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr15MinLOSQs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr15MinCVs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr15MinESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr15MinSESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr15MinUASs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr15MinInits"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr15MinUnavlRsrcs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucIntervalValidData"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucIntervalLOSs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucIntervalLOSQs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucIntervalCVs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucIntervalESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucIntervalSESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucIntervalUASs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucIntervalInits"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucIntervalUnavlRsrcs"))
)
if mibBuilder.loadTexts:
    cSdslStucPM15MinIntervalGroup.setStatus("current")

cSdslStucPM1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 6)
)
cSdslStucPM1DayIntervalGroup.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr1DayTimeElapsed"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr1DayLOSs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr1DayLOSQs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr1DayCVs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr1DayESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr1DaySESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr1DayUASs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr1DayInits"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfCurr1DayUnavlRsrcs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfPrev1DayMoniSecs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfPrev1DayLOSs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfPrev1DayLOSQs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfPrev1DayCVs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfPrev1DayESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfPrev1DaySESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfPrev1DayUASs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfPrev1DayInits"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPerfPrev1DayUnavlRsrcs"))
)
if mibBuilder.loadTexts:
    cSdslStucPM1DayIntervalGroup.setStatus("current")

cSdslSturPMCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 7)
)
cSdslSturPMCounterGroup.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslSturPerfLOSs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfLOSQs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCVs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfSESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfUASs"))
)
if mibBuilder.loadTexts:
    cSdslSturPMCounterGroup.setStatus("current")

cSdslSturPM15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 8)
)
cSdslSturPM15MinIntervalGroup.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslSturPerfValidIntervals"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfInvalidIntervals"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr15MinTimeElapse"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr15MinLOSs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr15MinLOSQs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr15MinCVs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr15MinESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr15MinSESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr15MinUASs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturIntervalLOSs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturIntervalLOSQs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturIntervalCVs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturIntervalESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturIntervalSESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturIntervalUASs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturIntervalValidData"))
)
if mibBuilder.loadTexts:
    cSdslSturPM15MinIntervalGroup.setStatus("current")

cSdslSturPM1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 9)
)
cSdslSturPM1DayIntervalGroup.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr1DayTimeElapsed"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr1DayLOSs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr1DayLOSQs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr1DayCVs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr1DayESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr1DaySESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfCurr1DayUASs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfPrev1DayMoniSecs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfPrev1DayLOSs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfPrev1DayLOSQs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfPrev1DayCVs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfPrev1DayESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfPrev1DaySESs"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturPerfPrev1DayUASs"))
)
if mibBuilder.loadTexts:
    cSdslSturPM1DayIntervalGroup.setStatus("current")

cSdslStucRateAdaptiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 10)
)
cSdslStucRateAdaptiveGroup.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslStucCurrRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucMaxSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucMinSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucThreshMinRate"))
)
if mibBuilder.loadTexts:
    cSdslStucRateAdaptiveGroup.setStatus("current")

cSdslStucAlarmConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 11)
)
cSdslStucAlarmConfProfileGroup.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslStucThreshMinRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucThreshMinSnrMgn"))
)
if mibBuilder.loadTexts:
    cSdslStucAlarmConfProfileGroup.setStatus("current")

cSdslStucBasicGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 12)
)
cSdslStucBasicGroupRev1.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslLineCoding"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineFraming"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineSpecific"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineConfProfile"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineAlarmConfProfile"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucInvSerialNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucInvVendorId"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucInvVersionNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucState"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucDefect"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrGain"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrOutputPwr"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrAtn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineMaxRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineFramingMode"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucTargetSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucMaxSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucMinSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucOutputPwr"),
        ("CISCO-SDSL-LINE-MIB", "cSdslShdslLineMaxRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPsdMaskType"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucAnnex"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineEquipmentType"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineAutoRateEnable"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucThresholdSnrMgn"))
)
if mibBuilder.loadTexts:
    cSdslStucBasicGroupRev1.setStatus("deprecated")

cSdslSturBasicGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 13)
)
cSdslSturBasicGroupRev1.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslLineCoding"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineFraming"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvSerialNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvVendorId"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvVersionNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturState"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturDefect"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrGain"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrOutputPwr"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrAtn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslShdslLineMaxRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineEquipmentType"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineAutoRateEnable"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturAnnex"))
)
if mibBuilder.loadTexts:
    cSdslSturBasicGroupRev1.setStatus("deprecated")

cSdslStucBasicGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 14)
)
cSdslStucBasicGroupRev2.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslLineCoding"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineFraming"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineSpecific"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineConfProfile"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineAlarmConfProfile"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucInvSerialNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucInvVendorId"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucInvVersionNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucState"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucDefect"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrGainRev"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrOutputPwr"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucCurrAtn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineMaxRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineFramingMode"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucTargetSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucMaxSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucMinSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucOutputPwr"),
        ("CISCO-SDSL-LINE-MIB", "cSdslShdslLineMaxRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucPsdMaskType"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucAnnex"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineEquipmentType"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineAutoRateEnable"),
        ("CISCO-SDSL-LINE-MIB", "cSdslStucThresholdSnrMgn"))
)
if mibBuilder.loadTexts:
    cSdslStucBasicGroupRev2.setStatus("current")

cSdslSturBasicGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 15)
)
cSdslSturBasicGroupRev2.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslLineCoding"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineFraming"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvSerialNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvVendorId"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvVersionNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturState"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturDefect"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrGainRev"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrOutputPwr"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrAtn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslShdslLineMaxRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineEquipmentType"),
        ("CISCO-SDSL-LINE-MIB", "cSdslLineAutoRateEnable"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturAnnex"))
)
if mibBuilder.loadTexts:
    cSdslSturBasicGroupRev2.setStatus("current")

cSdslSturGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 2, 16)
)
cSdslSturGroupRev1.setObjects(
      *(("CISCO-SDSL-LINE-MIB", "cSdslSturInvSerialNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvVendorId"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturInvVersionNumber"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturState"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturDefect"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrRate"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrSnrMgn"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrGainRev"),
        ("CISCO-SDSL-LINE-MIB", "cSdslSturCurrOutputPwr"))
)
if mibBuilder.loadTexts:
    cSdslSturGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSdslLineMIBStucCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSdslLineMIBStucCompliance.setStatus(
        "deprecated"
    )

ciscoSdslLineMIBSturCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSdslLineMIBSturCompliance.setStatus(
        "deprecated"
    )

ciscoSdslLineMIBStucComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSdslLineMIBStucComplianceRev1.setStatus(
        "current"
    )

ciscoSdslLineMIBSturComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 155, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoSdslLineMIBSturComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SDSL-LINE-MIB",
    **{"SdslPerfTimeElapsed": SdslPerfTimeElapsed,
       "SdslPerfCurrDayCount": SdslPerfCurrDayCount,
       "SdslPerfPrevDayCount": SdslPerfPrevDayCount,
       "SdslStuxDefect": SdslStuxDefect,
       "ciscoSdslLineMIB": ciscoSdslLineMIB,
       "ciscoSdslLineMIBObjects": ciscoSdslLineMIBObjects,
       "cSdslLineTable": cSdslLineTable,
       "cSdslLineEntry": cSdslLineEntry,
       "cSdslLineCoding": cSdslLineCoding,
       "cSdslLineFraming": cSdslLineFraming,
       "cSdslLineSpecific": cSdslLineSpecific,
       "cSdslLineConfProfile": cSdslLineConfProfile,
       "cSdslLineAlarmConfProfile": cSdslLineAlarmConfProfile,
       "cSdslStucPhysTable": cSdslStucPhysTable,
       "cSdslStucPhysEntry": cSdslStucPhysEntry,
       "cSdslStucInvSerialNumber": cSdslStucInvSerialNumber,
       "cSdslStucInvVendorId": cSdslStucInvVendorId,
       "cSdslStucInvVersionNumber": cSdslStucInvVersionNumber,
       "cSdslStucState": cSdslStucState,
       "cSdslStucDefect": cSdslStucDefect,
       "cSdslStucCurrRate": cSdslStucCurrRate,
       "cSdslStucCurrSnrMgn": cSdslStucCurrSnrMgn,
       "cSdslStucCurrGain": cSdslStucCurrGain,
       "cSdslStucCurrOutputPwr": cSdslStucCurrOutputPwr,
       "cSdslStucCurrAtn": cSdslStucCurrAtn,
       "cSdslStucCurrGainRev": cSdslStucCurrGainRev,
       "cSdslSturPhysTable": cSdslSturPhysTable,
       "cSdslSturPhysEntry": cSdslSturPhysEntry,
       "cSdslSturInvSerialNumber": cSdslSturInvSerialNumber,
       "cSdslSturInvVendorId": cSdslSturInvVendorId,
       "cSdslSturInvVersionNumber": cSdslSturInvVersionNumber,
       "cSdslSturState": cSdslSturState,
       "cSdslSturDefect": cSdslSturDefect,
       "cSdslSturCurrRate": cSdslSturCurrRate,
       "cSdslSturCurrSnrMgn": cSdslSturCurrSnrMgn,
       "cSdslSturCurrGain": cSdslSturCurrGain,
       "cSdslSturCurrOutputPwr": cSdslSturCurrOutputPwr,
       "cSdslSturCurrAtn": cSdslSturCurrAtn,
       "cSdslSturCurrGainRev": cSdslSturCurrGainRev,
       "cSdslStucPerfDataTable": cSdslStucPerfDataTable,
       "cSdslStucPerfDataEntry": cSdslStucPerfDataEntry,
       "cSdslStucPerfLOSs": cSdslStucPerfLOSs,
       "cSdslStucPerfLOSQs": cSdslStucPerfLOSQs,
       "cSdslStucPerfCVs": cSdslStucPerfCVs,
       "cSdslStucPerfESs": cSdslStucPerfESs,
       "cSdslStucPerfSESs": cSdslStucPerfSESs,
       "cSdslStucPerfUASs": cSdslStucPerfUASs,
       "cSdslStucPerfInits": cSdslStucPerfInits,
       "cSdslStucUnavailRsrcs": cSdslStucUnavailRsrcs,
       "cSdslStucPerfValidIntervals": cSdslStucPerfValidIntervals,
       "cSdslStucPerfInvalidIntervals": cSdslStucPerfInvalidIntervals,
       "cSdslStucPerfCurr15MinTimeElapse": cSdslStucPerfCurr15MinTimeElapse,
       "cSdslStucPerfCurr15MinLOSs": cSdslStucPerfCurr15MinLOSs,
       "cSdslStucPerfCurr15MinLOSQs": cSdslStucPerfCurr15MinLOSQs,
       "cSdslStucPerfCurr15MinCVs": cSdslStucPerfCurr15MinCVs,
       "cSdslStucPerfCurr15MinESs": cSdslStucPerfCurr15MinESs,
       "cSdslStucPerfCurr15MinSESs": cSdslStucPerfCurr15MinSESs,
       "cSdslStucPerfCurr15MinUASs": cSdslStucPerfCurr15MinUASs,
       "cSdslStucPerfCurr15MinInits": cSdslStucPerfCurr15MinInits,
       "cSdslStucPerfCurr15MinUnavlRsrcs": cSdslStucPerfCurr15MinUnavlRsrcs,
       "cSdslStucPerfCurr1DayTimeElapsed": cSdslStucPerfCurr1DayTimeElapsed,
       "cSdslStucPerfCurr1DayLOSs": cSdslStucPerfCurr1DayLOSs,
       "cSdslStucPerfCurr1DayLOSQs": cSdslStucPerfCurr1DayLOSQs,
       "cSdslStucPerfCurr1DayCVs": cSdslStucPerfCurr1DayCVs,
       "cSdslStucPerfCurr1DayESs": cSdslStucPerfCurr1DayESs,
       "cSdslStucPerfCurr1DaySESs": cSdslStucPerfCurr1DaySESs,
       "cSdslStucPerfCurr1DayUASs": cSdslStucPerfCurr1DayUASs,
       "cSdslStucPerfCurr1DayInits": cSdslStucPerfCurr1DayInits,
       "cSdslStucPerfCurr1DayUnavlRsrcs": cSdslStucPerfCurr1DayUnavlRsrcs,
       "cSdslStucPerfPrev1DayMoniSecs": cSdslStucPerfPrev1DayMoniSecs,
       "cSdslStucPerfPrev1DayLOSs": cSdslStucPerfPrev1DayLOSs,
       "cSdslStucPerfPrev1DayLOSQs": cSdslStucPerfPrev1DayLOSQs,
       "cSdslStucPerfPrev1DayCVs": cSdslStucPerfPrev1DayCVs,
       "cSdslStucPerfPrev1DayESs": cSdslStucPerfPrev1DayESs,
       "cSdslStucPerfPrev1DaySESs": cSdslStucPerfPrev1DaySESs,
       "cSdslStucPerfPrev1DayUASs": cSdslStucPerfPrev1DayUASs,
       "cSdslStucPerfPrev1DayInits": cSdslStucPerfPrev1DayInits,
       "cSdslStucPerfPrev1DayUnavlRsrcs": cSdslStucPerfPrev1DayUnavlRsrcs,
       "cSdslSturPerfDataTable": cSdslSturPerfDataTable,
       "cSdslSturPerfDataEntry": cSdslSturPerfDataEntry,
       "cSdslSturPerfLOSs": cSdslSturPerfLOSs,
       "cSdslSturPerfLOSQs": cSdslSturPerfLOSQs,
       "cSdslSturPerfCVs": cSdslSturPerfCVs,
       "cSdslSturPerfESs": cSdslSturPerfESs,
       "cSdslSturPerfSESs": cSdslSturPerfSESs,
       "cSdslSturPerfUASs": cSdslSturPerfUASs,
       "cSdslSturPerfValidIntervals": cSdslSturPerfValidIntervals,
       "cSdslSturPerfInvalidIntervals": cSdslSturPerfInvalidIntervals,
       "cSdslSturPerfCurr15MinTimeElapse": cSdslSturPerfCurr15MinTimeElapse,
       "cSdslSturPerfCurr15MinLOSs": cSdslSturPerfCurr15MinLOSs,
       "cSdslSturPerfCurr15MinLOSQs": cSdslSturPerfCurr15MinLOSQs,
       "cSdslSturPerfCurr15MinCVs": cSdslSturPerfCurr15MinCVs,
       "cSdslSturPerfCurr15MinESs": cSdslSturPerfCurr15MinESs,
       "cSdslSturPerfCurr15MinSESs": cSdslSturPerfCurr15MinSESs,
       "cSdslSturPerfCurr15MinUASs": cSdslSturPerfCurr15MinUASs,
       "cSdslSturPerfCurr1DayTimeElapsed": cSdslSturPerfCurr1DayTimeElapsed,
       "cSdslSturPerfCurr1DayLOSs": cSdslSturPerfCurr1DayLOSs,
       "cSdslSturPerfCurr1DayLOSQs": cSdslSturPerfCurr1DayLOSQs,
       "cSdslSturPerfCurr1DayCVs": cSdslSturPerfCurr1DayCVs,
       "cSdslSturPerfCurr1DayESs": cSdslSturPerfCurr1DayESs,
       "cSdslSturPerfCurr1DaySESs": cSdslSturPerfCurr1DaySESs,
       "cSdslSturPerfCurr1DayUASs": cSdslSturPerfCurr1DayUASs,
       "cSdslSturPerfPrev1DayMoniSecs": cSdslSturPerfPrev1DayMoniSecs,
       "cSdslSturPerfPrev1DayLOSs": cSdslSturPerfPrev1DayLOSs,
       "cSdslSturPerfPrev1DayLOSQs": cSdslSturPerfPrev1DayLOSQs,
       "cSdslSturPerfPrev1DayCVs": cSdslSturPerfPrev1DayCVs,
       "cSdslSturPerfPrev1DayESs": cSdslSturPerfPrev1DayESs,
       "cSdslSturPerfPrev1DaySESs": cSdslSturPerfPrev1DaySESs,
       "cSdslSturPerfPrev1DayUASs": cSdslSturPerfPrev1DayUASs,
       "cSdslStucIntervalTable": cSdslStucIntervalTable,
       "cSdslStucIntervalEntry": cSdslStucIntervalEntry,
       "cSdslStucIntervalNumber": cSdslStucIntervalNumber,
       "cSdslStucIntervalValidData": cSdslStucIntervalValidData,
       "cSdslStucIntervalLOSs": cSdslStucIntervalLOSs,
       "cSdslStucIntervalLOSQs": cSdslStucIntervalLOSQs,
       "cSdslStucIntervalCVs": cSdslStucIntervalCVs,
       "cSdslStucIntervalESs": cSdslStucIntervalESs,
       "cSdslStucIntervalSESs": cSdslStucIntervalSESs,
       "cSdslStucIntervalUASs": cSdslStucIntervalUASs,
       "cSdslStucIntervalInits": cSdslStucIntervalInits,
       "cSdslStucIntervalUnavlRsrcs": cSdslStucIntervalUnavlRsrcs,
       "cSdslSturIntervalTable": cSdslSturIntervalTable,
       "cSdslSturIntervalEntry": cSdslSturIntervalEntry,
       "cSdslSturIntervalNumber": cSdslSturIntervalNumber,
       "cSdslSturIntervalValidData": cSdslSturIntervalValidData,
       "cSdslSturIntervalLOSs": cSdslSturIntervalLOSs,
       "cSdslSturIntervalLOSQs": cSdslSturIntervalLOSQs,
       "cSdslSturIntervalCVs": cSdslSturIntervalCVs,
       "cSdslSturIntervalESs": cSdslSturIntervalESs,
       "cSdslSturIntervalSESs": cSdslSturIntervalSESs,
       "cSdslSturIntervalUASs": cSdslSturIntervalUASs,
       "cSdslLineConfProfileTable": cSdslLineConfProfileTable,
       "cSdslLineConfProfileEntry": cSdslLineConfProfileEntry,
       "cSdslLineMaxRate": cSdslLineMaxRate,
       "cSdslLineFramingMode": cSdslLineFramingMode,
       "cSdslStucTargetSnrMgn": cSdslStucTargetSnrMgn,
       "cSdslStucMaxSnrMgn": cSdslStucMaxSnrMgn,
       "cSdslStucMinSnrMgn": cSdslStucMinSnrMgn,
       "cSdslStucOutputPwr": cSdslStucOutputPwr,
       "cSdslShdslLineMaxRate": cSdslShdslLineMaxRate,
       "cSdslStucPsdMaskType": cSdslStucPsdMaskType,
       "cSdslStucAnnex": cSdslStucAnnex,
       "cSdslLineEquipmentType": cSdslLineEquipmentType,
       "cSdslLineAutoRateEnable": cSdslLineAutoRateEnable,
       "cSdslStucThresholdSnrMgn": cSdslStucThresholdSnrMgn,
       "cSdslSturAnnex": cSdslSturAnnex,
       "cSdslLineAlarmConfProfileTable": cSdslLineAlarmConfProfileTable,
       "cSdslLineAlarmConfProfileEntry": cSdslLineAlarmConfProfileEntry,
       "cSdslStucThreshMinRate": cSdslStucThreshMinRate,
       "cSdslStucThreshMinSnrMgn": cSdslStucThreshMinSnrMgn,
       "ciscoSdslLineMIBNotificationsPrefix": ciscoSdslLineMIBNotificationsPrefix,
       "ciscoSdslLineMIBNotifications": ciscoSdslLineMIBNotifications,
       "ciscoSdslLineMIBConformance": ciscoSdslLineMIBConformance,
       "ciscoSdslLineMIBCompliances": ciscoSdslLineMIBCompliances,
       "ciscoSdslLineMIBStucCompliance": ciscoSdslLineMIBStucCompliance,
       "ciscoSdslLineMIBSturCompliance": ciscoSdslLineMIBSturCompliance,
       "ciscoSdslLineMIBStucComplianceRev1": ciscoSdslLineMIBStucComplianceRev1,
       "ciscoSdslLineMIBSturComplianceRev1": ciscoSdslLineMIBSturComplianceRev1,
       "ciscoSdslLineMIBGroups": ciscoSdslLineMIBGroups,
       "cSdslStucBasicGroup": cSdslStucBasicGroup,
       "cSdslSturBasicGroup": cSdslSturBasicGroup,
       "cSdslSturGroup": cSdslSturGroup,
       "cSdslStucPMCounterGroup": cSdslStucPMCounterGroup,
       "cSdslStucPM15MinIntervalGroup": cSdslStucPM15MinIntervalGroup,
       "cSdslStucPM1DayIntervalGroup": cSdslStucPM1DayIntervalGroup,
       "cSdslSturPMCounterGroup": cSdslSturPMCounterGroup,
       "cSdslSturPM15MinIntervalGroup": cSdslSturPM15MinIntervalGroup,
       "cSdslSturPM1DayIntervalGroup": cSdslSturPM1DayIntervalGroup,
       "cSdslStucRateAdaptiveGroup": cSdslStucRateAdaptiveGroup,
       "cSdslStucAlarmConfProfileGroup": cSdslStucAlarmConfProfileGroup,
       "cSdslStucBasicGroupRev1": cSdslStucBasicGroupRev1,
       "cSdslSturBasicGroupRev1": cSdslSturBasicGroupRev1,
       "cSdslStucBasicGroupRev2": cSdslStucBasicGroupRev2,
       "cSdslSturBasicGroupRev2": cSdslSturBasicGroupRev2,
       "cSdslSturGroupRev1": cSdslSturGroupRev1}
)
