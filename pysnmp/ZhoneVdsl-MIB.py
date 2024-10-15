# SNMP MIB module (ZhoneVdsl-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZhoneVdsl-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:23 2024
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

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfTimeElapsed) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfTimeElapsed")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zhoneModules,
 zhoneVdsl) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhoneVdsl")


# MODULE-IDENTITY

zhoneVdslMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 110)
)
zhoneVdslMib.setRevisions(
        ("2013-10-08 06:43",
         "2013-02-27 18:00",
         "2013-02-11 14:15",
         "2011-12-01 05:59",
         "2011-11-16 12:14",
         "2011-10-18 11:13",
         "2011-10-14 11:24",
         "2011-04-28 11:55",
         "2010-11-05 07:16",
         "2010-10-13 04:59",
         "2010-06-07 11:29",
         "2010-05-31 00:11",
         "2010-04-02 06:40",
         "2010-03-29 05:54",
         "2010-03-02 08:44",
         "2008-04-14 12:28",
         "2008-02-05 08:56",
         "2007-10-23 16:53",
         "2007-10-05 13:24",
         "2007-06-20 10:56",
         "2007-03-14 16:08",
         "2006-12-05 15:09",
         "2006-11-10 08:58",
         "2006-10-10 15:25",
         "2006-09-10 11:16",
         "2006-08-22 17:21",
         "2006-06-15 15:29",
         "2004-02-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZhoneVdslLineCodingType(Integer32, TextualConvention):
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
        *(("mcm", 2),
          ("other", 1),
          ("scm", 3))
    )



class ZhoneVdslLineEntity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vtuc", 1),
          ("vtur", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ZhoneVdslLineMib_ObjectIdentity = ObjectIdentity
zhoneVdslLineMib = _ZhoneVdslLineMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1)
)
_ZhoneVdslNotifications_ObjectIdentity = ObjectIdentity
zhoneVdslNotifications = _ZhoneVdslNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0)
)
_ZhoneVdslMibObjects_ObjectIdentity = ObjectIdentity
zhoneVdslMibObjects = _ZhoneVdslMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1)
)
_ZhoneVdslLineTable_Object = MibTable
zhoneVdslLineTable = _ZhoneVdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneVdslLineTable.setStatus("current")
_ZhoneVdslLineEntry_Object = MibTableRow
zhoneVdslLineEntry = _ZhoneVdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 1, 1)
)
zhoneVdslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneVdslLineEntry.setStatus("current")
_ZhoneVdslLineCoding_Type = ZhoneVdslLineCodingType
_ZhoneVdslLineCoding_Object = MibTableColumn
zhoneVdslLineCoding = _ZhoneVdslLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 1, 1, 1),
    _ZhoneVdslLineCoding_Type()
)
zhoneVdslLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslLineCoding.setStatus("current")


class _ZhoneVdslLineType_Type(Integer32):
    """Custom type zhoneVdslLineType based on Integer32"""
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
        *(("fastAndInterleaved", 5),
          ("fastOnly", 2),
          ("fastOrInterleaved", 4),
          ("interleavedOnly", 3),
          ("noChannel", 1))
    )


_ZhoneVdslLineType_Type.__name__ = "Integer32"
_ZhoneVdslLineType_Object = MibTableColumn
zhoneVdslLineType = _ZhoneVdslLineType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 1, 1, 2),
    _ZhoneVdslLineType_Type()
)
zhoneVdslLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslLineType.setStatus("current")


class _ZhoneVdslLineConfProfile_Type(SnmpAdminString):
    """Custom type zhoneVdslLineConfProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZhoneVdslLineConfProfile_Type.__name__ = "SnmpAdminString"
_ZhoneVdslLineConfProfile_Object = MibTableColumn
zhoneVdslLineConfProfile = _ZhoneVdslLineConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 1, 1, 3),
    _ZhoneVdslLineConfProfile_Type()
)
zhoneVdslLineConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVdslLineConfProfile.setStatus("current")


class _ZhoneVdslLineAlarmConfProfile_Type(SnmpAdminString):
    """Custom type zhoneVdslLineAlarmConfProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZhoneVdslLineAlarmConfProfile_Type.__name__ = "SnmpAdminString"
_ZhoneVdslLineAlarmConfProfile_Object = MibTableColumn
zhoneVdslLineAlarmConfProfile = _ZhoneVdslLineAlarmConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 1, 1, 4),
    _ZhoneVdslLineAlarmConfProfile_Type()
)
zhoneVdslLineAlarmConfProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfProfile.setStatus("current")
_ZhoneVdslPhysTable_Object = MibTable
zhoneVdslPhysTable = _ZhoneVdslPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    zhoneVdslPhysTable.setStatus("current")
_ZhoneVdslPhysEntry_Object = MibTableRow
zhoneVdslPhysEntry = _ZhoneVdslPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1)
)
zhoneVdslPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslPhysSide"),
)
if mibBuilder.loadTexts:
    zhoneVdslPhysEntry.setStatus("current")
_ZhoneVdslPhysSide_Type = ZhoneVdslLineEntity
_ZhoneVdslPhysSide_Object = MibTableColumn
zhoneVdslPhysSide = _ZhoneVdslPhysSide_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 1),
    _ZhoneVdslPhysSide_Type()
)
zhoneVdslPhysSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVdslPhysSide.setStatus("current")


class _ZhoneVdslPhysInvSerialNumber_Type(OctetString):
    """Custom type zhoneVdslPhysInvSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZhoneVdslPhysInvSerialNumber_Type.__name__ = "OctetString"
_ZhoneVdslPhysInvSerialNumber_Object = MibTableColumn
zhoneVdslPhysInvSerialNumber = _ZhoneVdslPhysInvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 2),
    _ZhoneVdslPhysInvSerialNumber_Type()
)
zhoneVdslPhysInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysInvSerialNumber.setStatus("current")


class _ZhoneVdslPhysInvVendorID_Type(OctetString):
    """Custom type zhoneVdslPhysInvVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZhoneVdslPhysInvVendorID_Type.__name__ = "OctetString"
_ZhoneVdslPhysInvVendorID_Object = MibTableColumn
zhoneVdslPhysInvVendorID = _ZhoneVdslPhysInvVendorID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 3),
    _ZhoneVdslPhysInvVendorID_Type()
)
zhoneVdslPhysInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysInvVendorID.setStatus("current")


class _ZhoneVdslPhysInvVersionNumber_Type(OctetString):
    """Custom type zhoneVdslPhysInvVersionNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZhoneVdslPhysInvVersionNumber_Type.__name__ = "OctetString"
_ZhoneVdslPhysInvVersionNumber_Object = MibTableColumn
zhoneVdslPhysInvVersionNumber = _ZhoneVdslPhysInvVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 4),
    _ZhoneVdslPhysInvVersionNumber_Type()
)
zhoneVdslPhysInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysInvVersionNumber.setStatus("current")


class _ZhoneVdslPhysCurrSnrMgn_Type(Integer32):
    """Custom type zhoneVdslPhysCurrSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_ZhoneVdslPhysCurrSnrMgn_Type.__name__ = "Integer32"
_ZhoneVdslPhysCurrSnrMgn_Object = MibTableColumn
zhoneVdslPhysCurrSnrMgn = _ZhoneVdslPhysCurrSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 5),
    _ZhoneVdslPhysCurrSnrMgn_Type()
)
zhoneVdslPhysCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrSnrMgn.setUnits("0.10dBm")


class _ZhoneVdslPhysCurrAtn_Type(Gauge32):
    """Custom type zhoneVdslPhysCurrAtn based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneVdslPhysCurrAtn_Type.__name__ = "Gauge32"
_ZhoneVdslPhysCurrAtn_Object = MibTableColumn
zhoneVdslPhysCurrAtn = _ZhoneVdslPhysCurrAtn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 6),
    _ZhoneVdslPhysCurrAtn_Type()
)
zhoneVdslPhysCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrAtn.setUnits("0.10dBm")


class _ZhoneVdslPhysCurrStatus_Type(Bits):
    """Custom type zhoneVdslPhysCurrStatus based on Bits"""
    namedValues = NamedValues(
        *(("configInitFailure", 7),
          ("dataInitFailure", 6),
          ("lossOfFraming", 1),
          ("lossOfLink", 5),
          ("lossOfPower", 3),
          ("lossOfSignal", 2),
          ("lossOfSignalQuality", 4),
          ("noDefect", 0),
          ("noPeerVtuPresent", 9),
          ("protocolInitFailure", 8))
    )

_ZhoneVdslPhysCurrStatus_Type.__name__ = "Bits"
_ZhoneVdslPhysCurrStatus_Object = MibTableColumn
zhoneVdslPhysCurrStatus = _ZhoneVdslPhysCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 7),
    _ZhoneVdslPhysCurrStatus_Type()
)
zhoneVdslPhysCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrStatus.setStatus("current")


class _ZhoneVdslPhysCurrOutputPwr_Type(Integer32):
    """Custom type zhoneVdslPhysCurrOutputPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_ZhoneVdslPhysCurrOutputPwr_Type.__name__ = "Integer32"
_ZhoneVdslPhysCurrOutputPwr_Object = MibTableColumn
zhoneVdslPhysCurrOutputPwr = _ZhoneVdslPhysCurrOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 8),
    _ZhoneVdslPhysCurrOutputPwr_Type()
)
zhoneVdslPhysCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrOutputPwr.setUnits("0.1dBm")
_ZhoneVdslPhysCurrAttainableRate_Type = Gauge32
_ZhoneVdslPhysCurrAttainableRate_Object = MibTableColumn
zhoneVdslPhysCurrAttainableRate = _ZhoneVdslPhysCurrAttainableRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 9),
    _ZhoneVdslPhysCurrAttainableRate_Type()
)
zhoneVdslPhysCurrAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrAttainableRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrAttainableRate.setUnits("kbps")
_ZhoneVdslPhysCurrLineRate_Type = Gauge32
_ZhoneVdslPhysCurrLineRate_Object = MibTableColumn
zhoneVdslPhysCurrLineRate = _ZhoneVdslPhysCurrLineRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 10),
    _ZhoneVdslPhysCurrLineRate_Type()
)
zhoneVdslPhysCurrLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrLineRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrLineRate.setUnits("kbps")


class _ZhoneVdslPhysCurrConnType_Type(Integer32):
    """Custom type zhoneVdslPhysCurrConnType based on Integer32"""
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
        *(("adsl", 4),
          ("adsl2", 5),
          ("adsl2-annexm", 6),
          ("adsl2plus", 7),
          ("adsl2plus-annexm", 8),
          ("invalid", 3),
          ("not-connected", 2),
          ("unknown", 1),
          ("vdsl1", 9),
          ("vdsl2", 10))
    )


_ZhoneVdslPhysCurrConnType_Type.__name__ = "Integer32"
_ZhoneVdslPhysCurrConnType_Object = MibTableColumn
zhoneVdslPhysCurrConnType = _ZhoneVdslPhysCurrConnType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 12),
    _ZhoneVdslPhysCurrConnType_Type()
)
zhoneVdslPhysCurrConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrConnType.setStatus("current")


class _ZhoneVdslPhysCurrProfile_Type(Integer32):
    """Custom type zhoneVdslPhysCurrProfile based on Integer32"""
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
        *(("g993-2-12a", 5),
          ("g993-2-12b", 6),
          ("g993-2-17a", 7),
          ("g993-2-30a", 8),
          ("g993-2-8a", 1),
          ("g993-2-8b", 2),
          ("g993-2-8c", 3),
          ("g993-2-8d", 4),
          ("no-vdsl-connection", 9))
    )


_ZhoneVdslPhysCurrProfile_Type.__name__ = "Integer32"
_ZhoneVdslPhysCurrProfile_Object = MibTableColumn
zhoneVdslPhysCurrProfile = _ZhoneVdslPhysCurrProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 13),
    _ZhoneVdslPhysCurrProfile_Type()
)
zhoneVdslPhysCurrProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysCurrProfile.setStatus("current")
_ZhoneVdslPhysPhyRActive_Type = TruthValue
_ZhoneVdslPhysPhyRActive_Object = MibTableColumn
zhoneVdslPhysPhyRActive = _ZhoneVdslPhysPhyRActive_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 14),
    _ZhoneVdslPhysPhyRActive_Type()
)
zhoneVdslPhysPhyRActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysPhyRActive.setStatus("current")
_ZhoneVdslPhysGinpActive_Type = TruthValue
_ZhoneVdslPhysGinpActive_Object = MibTableColumn
zhoneVdslPhysGinpActive = _ZhoneVdslPhysGinpActive_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 15),
    _ZhoneVdslPhysGinpActive_Type()
)
zhoneVdslPhysGinpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysGinpActive.setStatus("current")


class _ZhoneVdslPhysTransportMode_Type(Integer32):
    """Custom type zhoneVdslPhysTransportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("ptm", 2))
    )


_ZhoneVdslPhysTransportMode_Type.__name__ = "Integer32"
_ZhoneVdslPhysTransportMode_Object = MibTableColumn
zhoneVdslPhysTransportMode = _ZhoneVdslPhysTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 2, 1, 16),
    _ZhoneVdslPhysTransportMode_Type()
)
zhoneVdslPhysTransportMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhysTransportMode.setStatus("current")
_ZhoneVdslChanTable_Object = MibTable
zhoneVdslChanTable = _ZhoneVdslChanTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 3)
)
if mibBuilder.loadTexts:
    zhoneVdslChanTable.setStatus("current")
_ZhoneVdslChanEntry_Object = MibTableRow
zhoneVdslChanEntry = _ZhoneVdslChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 3, 1)
)
zhoneVdslChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslPhysSide"),
)
if mibBuilder.loadTexts:
    zhoneVdslChanEntry.setStatus("current")
_ZhoneVdslChanInterleaveDelay_Type = Gauge32
_ZhoneVdslChanInterleaveDelay_Object = MibTableColumn
zhoneVdslChanInterleaveDelay = _ZhoneVdslChanInterleaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 3, 1, 1),
    _ZhoneVdslChanInterleaveDelay_Type()
)
zhoneVdslChanInterleaveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanInterleaveDelay.setUnits("milliseconds")
_ZhoneVdslChanCrcBlockLength_Type = Gauge32
_ZhoneVdslChanCrcBlockLength_Object = MibTableColumn
zhoneVdslChanCrcBlockLength = _ZhoneVdslChanCrcBlockLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 3, 1, 2),
    _ZhoneVdslChanCrcBlockLength_Type()
)
zhoneVdslChanCrcBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanCrcBlockLength.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanCrcBlockLength.setUnits("bytes")
_ZhoneVdslChanCurrTxRate_Type = Gauge32
_ZhoneVdslChanCurrTxRate_Object = MibTableColumn
zhoneVdslChanCurrTxRate = _ZhoneVdslChanCurrTxRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 3, 1, 3),
    _ZhoneVdslChanCurrTxRate_Type()
)
zhoneVdslChanCurrTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanCurrTxRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanCurrTxRate.setUnits("kbps")


class _ZhoneVdslChanCurrTxSlowBurstProtect_Type(Gauge32):
    """Custom type zhoneVdslChanCurrTxSlowBurstProtect based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1275),
    )


_ZhoneVdslChanCurrTxSlowBurstProtect_Type.__name__ = "Gauge32"
_ZhoneVdslChanCurrTxSlowBurstProtect_Object = MibTableColumn
zhoneVdslChanCurrTxSlowBurstProtect = _ZhoneVdslChanCurrTxSlowBurstProtect_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 3, 1, 4),
    _ZhoneVdslChanCurrTxSlowBurstProtect_Type()
)
zhoneVdslChanCurrTxSlowBurstProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanCurrTxSlowBurstProtect.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanCurrTxSlowBurstProtect.setUnits("microseconds")


class _ZhoneVdslChanCurrTxFastFec_Type(Gauge32):
    """Custom type zhoneVdslChanCurrTxFastFec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_ZhoneVdslChanCurrTxFastFec_Type.__name__ = "Gauge32"
_ZhoneVdslChanCurrTxFastFec_Object = MibTableColumn
zhoneVdslChanCurrTxFastFec = _ZhoneVdslChanCurrTxFastFec_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 3, 1, 5),
    _ZhoneVdslChanCurrTxFastFec_Type()
)
zhoneVdslChanCurrTxFastFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanCurrTxFastFec.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanCurrTxFastFec.setUnits("%")
_ZhoneVdslPerfDataTable_Object = MibTable
zhoneVdslPerfDataTable = _ZhoneVdslPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4)
)
if mibBuilder.loadTexts:
    zhoneVdslPerfDataTable.setStatus("current")
_ZhoneVdslPerfDataEntry_Object = MibTableRow
zhoneVdslPerfDataEntry = _ZhoneVdslPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1)
)
zhoneVdslPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslPhysSide"),
)
if mibBuilder.loadTexts:
    zhoneVdslPerfDataEntry.setStatus("current")


class _ZhoneVdslPerfDataValidIntervals_Type(Integer32):
    """Custom type zhoneVdslPerfDataValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZhoneVdslPerfDataValidIntervals_Type.__name__ = "Integer32"
_ZhoneVdslPerfDataValidIntervals_Object = MibTableColumn
zhoneVdslPerfDataValidIntervals = _ZhoneVdslPerfDataValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 1),
    _ZhoneVdslPerfDataValidIntervals_Type()
)
zhoneVdslPerfDataValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataValidIntervals.setUnits("intervals")


class _ZhoneVdslPerfDataInvalidIntervals_Type(Integer32):
    """Custom type zhoneVdslPerfDataInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZhoneVdslPerfDataInvalidIntervals_Type.__name__ = "Integer32"
_ZhoneVdslPerfDataInvalidIntervals_Object = MibTableColumn
zhoneVdslPerfDataInvalidIntervals = _ZhoneVdslPerfDataInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 2),
    _ZhoneVdslPerfDataInvalidIntervals_Type()
)
zhoneVdslPerfDataInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataInvalidIntervals.setUnits("intervals")
_ZhoneVdslPerfDataLofs_Type = Unsigned32
_ZhoneVdslPerfDataLofs_Object = MibTableColumn
zhoneVdslPerfDataLofs = _ZhoneVdslPerfDataLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 3),
    _ZhoneVdslPerfDataLofs_Type()
)
zhoneVdslPerfDataLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataLofs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataLofs.setUnits("seconds")
_ZhoneVdslPerfDataLoss_Type = Unsigned32
_ZhoneVdslPerfDataLoss_Object = MibTableColumn
zhoneVdslPerfDataLoss = _ZhoneVdslPerfDataLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 4),
    _ZhoneVdslPerfDataLoss_Type()
)
zhoneVdslPerfDataLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataLoss.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataLoss.setUnits("seconds")
_ZhoneVdslPerfDataLprs_Type = Unsigned32
_ZhoneVdslPerfDataLprs_Object = MibTableColumn
zhoneVdslPerfDataLprs = _ZhoneVdslPerfDataLprs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 5),
    _ZhoneVdslPerfDataLprs_Type()
)
zhoneVdslPerfDataLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataLprs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataLprs.setUnits("seconds")
_ZhoneVdslPerfDataLols_Type = Unsigned32
_ZhoneVdslPerfDataLols_Object = MibTableColumn
zhoneVdslPerfDataLols = _ZhoneVdslPerfDataLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 6),
    _ZhoneVdslPerfDataLols_Type()
)
zhoneVdslPerfDataLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataLols.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataLols.setUnits("seconds")
_ZhoneVdslPerfDataESs_Type = Unsigned32
_ZhoneVdslPerfDataESs_Object = MibTableColumn
zhoneVdslPerfDataESs = _ZhoneVdslPerfDataESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 7),
    _ZhoneVdslPerfDataESs_Type()
)
zhoneVdslPerfDataESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataESs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataESs.setUnits("seconds")
_ZhoneVdslPerfDataSESs_Type = Unsigned32
_ZhoneVdslPerfDataSESs_Object = MibTableColumn
zhoneVdslPerfDataSESs = _ZhoneVdslPerfDataSESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 8),
    _ZhoneVdslPerfDataSESs_Type()
)
zhoneVdslPerfDataSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataSESs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataSESs.setUnits("seconds")
_ZhoneVdslPerfDataUASs_Type = Unsigned32
_ZhoneVdslPerfDataUASs_Object = MibTableColumn
zhoneVdslPerfDataUASs = _ZhoneVdslPerfDataUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 9),
    _ZhoneVdslPerfDataUASs_Type()
)
zhoneVdslPerfDataUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataUASs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataUASs.setUnits("seconds")
_ZhoneVdslPerfDataInits_Type = Unsigned32
_ZhoneVdslPerfDataInits_Object = MibTableColumn
zhoneVdslPerfDataInits = _ZhoneVdslPerfDataInits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 10),
    _ZhoneVdslPerfDataInits_Type()
)
zhoneVdslPerfDataInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataInits.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataInits.setUnits("occurrences")


class _ZhoneVdslPerfDataCurr15MinTimeElapsed_Type(Integer32):
    """Custom type zhoneVdslPerfDataCurr15MinTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_ZhoneVdslPerfDataCurr15MinTimeElapsed_Type.__name__ = "Integer32"
_ZhoneVdslPerfDataCurr15MinTimeElapsed_Object = MibTableColumn
zhoneVdslPerfDataCurr15MinTimeElapsed = _ZhoneVdslPerfDataCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 11),
    _ZhoneVdslPerfDataCurr15MinTimeElapsed_Type()
)
zhoneVdslPerfDataCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinTimeElapsed.setUnits("seconds")
_ZhoneVdslPerfDataCurr15MinLofs_Type = Unsigned32
_ZhoneVdslPerfDataCurr15MinLofs_Object = MibTableColumn
zhoneVdslPerfDataCurr15MinLofs = _ZhoneVdslPerfDataCurr15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 12),
    _ZhoneVdslPerfDataCurr15MinLofs_Type()
)
zhoneVdslPerfDataCurr15MinLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinLofs.setUnits("seconds")
_ZhoneVdslPerfDataCurr15MinLoss_Type = Unsigned32
_ZhoneVdslPerfDataCurr15MinLoss_Object = MibTableColumn
zhoneVdslPerfDataCurr15MinLoss = _ZhoneVdslPerfDataCurr15MinLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 13),
    _ZhoneVdslPerfDataCurr15MinLoss_Type()
)
zhoneVdslPerfDataCurr15MinLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinLoss.setUnits("seconds")
_ZhoneVdslPerfDataCurr15MinLprs_Type = Unsigned32
_ZhoneVdslPerfDataCurr15MinLprs_Object = MibTableColumn
zhoneVdslPerfDataCurr15MinLprs = _ZhoneVdslPerfDataCurr15MinLprs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 14),
    _ZhoneVdslPerfDataCurr15MinLprs_Type()
)
zhoneVdslPerfDataCurr15MinLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinLprs.setUnits("seconds")
_ZhoneVdslPerfDataCurr15MinLols_Type = Unsigned32
_ZhoneVdslPerfDataCurr15MinLols_Object = MibTableColumn
zhoneVdslPerfDataCurr15MinLols = _ZhoneVdslPerfDataCurr15MinLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 15),
    _ZhoneVdslPerfDataCurr15MinLols_Type()
)
zhoneVdslPerfDataCurr15MinLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinLols.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinLols.setUnits("seconds")
_ZhoneVdslPerfDataCurr15MinESs_Type = Unsigned32
_ZhoneVdslPerfDataCurr15MinESs_Object = MibTableColumn
zhoneVdslPerfDataCurr15MinESs = _ZhoneVdslPerfDataCurr15MinESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 16),
    _ZhoneVdslPerfDataCurr15MinESs_Type()
)
zhoneVdslPerfDataCurr15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinESs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinESs.setUnits("seconds")
_ZhoneVdslPerfDataCurr15MinSESs_Type = Unsigned32
_ZhoneVdslPerfDataCurr15MinSESs_Object = MibTableColumn
zhoneVdslPerfDataCurr15MinSESs = _ZhoneVdslPerfDataCurr15MinSESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 17),
    _ZhoneVdslPerfDataCurr15MinSESs_Type()
)
zhoneVdslPerfDataCurr15MinSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinSESs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinSESs.setUnits("seconds")
_ZhoneVdslPerfDataCurr15MinUASs_Type = Unsigned32
_ZhoneVdslPerfDataCurr15MinUASs_Object = MibTableColumn
zhoneVdslPerfDataCurr15MinUASs = _ZhoneVdslPerfDataCurr15MinUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 18),
    _ZhoneVdslPerfDataCurr15MinUASs_Type()
)
zhoneVdslPerfDataCurr15MinUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinUASs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinUASs.setUnits("seconds")
_ZhoneVdslPerfDataCurr15MinInits_Type = Unsigned32
_ZhoneVdslPerfDataCurr15MinInits_Object = MibTableColumn
zhoneVdslPerfDataCurr15MinInits = _ZhoneVdslPerfDataCurr15MinInits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 19),
    _ZhoneVdslPerfDataCurr15MinInits_Type()
)
zhoneVdslPerfDataCurr15MinInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinInits.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr15MinInits.setUnits("occurrences")


class _ZhoneVdslPerfData1DayValidIntervals_Type(Integer32):
    """Custom type zhoneVdslPerfData1DayValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZhoneVdslPerfData1DayValidIntervals_Type.__name__ = "Integer32"
_ZhoneVdslPerfData1DayValidIntervals_Object = MibTableColumn
zhoneVdslPerfData1DayValidIntervals = _ZhoneVdslPerfData1DayValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 20),
    _ZhoneVdslPerfData1DayValidIntervals_Type()
)
zhoneVdslPerfData1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfData1DayValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfData1DayValidIntervals.setUnits("intervals")


class _ZhoneVdslPerfData1DayInvalidIntervals_Type(Integer32):
    """Custom type zhoneVdslPerfData1DayInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZhoneVdslPerfData1DayInvalidIntervals_Type.__name__ = "Integer32"
_ZhoneVdslPerfData1DayInvalidIntervals_Object = MibTableColumn
zhoneVdslPerfData1DayInvalidIntervals = _ZhoneVdslPerfData1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 21),
    _ZhoneVdslPerfData1DayInvalidIntervals_Type()
)
zhoneVdslPerfData1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfData1DayInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfData1DayInvalidIntervals.setUnits("intervals")


class _ZhoneVdslPerfDataCurr1DayTimeElapsed_Type(Integer32):
    """Custom type zhoneVdslPerfDataCurr1DayTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_ZhoneVdslPerfDataCurr1DayTimeElapsed_Type.__name__ = "Integer32"
_ZhoneVdslPerfDataCurr1DayTimeElapsed_Object = MibTableColumn
zhoneVdslPerfDataCurr1DayTimeElapsed = _ZhoneVdslPerfDataCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 22),
    _ZhoneVdslPerfDataCurr1DayTimeElapsed_Type()
)
zhoneVdslPerfDataCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayTimeElapsed.setUnits("seconds")
_ZhoneVdslPerfDataCurr1DayLofs_Type = Unsigned32
_ZhoneVdslPerfDataCurr1DayLofs_Object = MibTableColumn
zhoneVdslPerfDataCurr1DayLofs = _ZhoneVdslPerfDataCurr1DayLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 23),
    _ZhoneVdslPerfDataCurr1DayLofs_Type()
)
zhoneVdslPerfDataCurr1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayLofs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayLofs.setUnits("seconds")
_ZhoneVdslPerfDataCurr1DayLoss_Type = Unsigned32
_ZhoneVdslPerfDataCurr1DayLoss_Object = MibTableColumn
zhoneVdslPerfDataCurr1DayLoss = _ZhoneVdslPerfDataCurr1DayLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 24),
    _ZhoneVdslPerfDataCurr1DayLoss_Type()
)
zhoneVdslPerfDataCurr1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayLoss.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayLoss.setUnits("seconds")
_ZhoneVdslPerfDataCurr1DayLprs_Type = Unsigned32
_ZhoneVdslPerfDataCurr1DayLprs_Object = MibTableColumn
zhoneVdslPerfDataCurr1DayLprs = _ZhoneVdslPerfDataCurr1DayLprs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 25),
    _ZhoneVdslPerfDataCurr1DayLprs_Type()
)
zhoneVdslPerfDataCurr1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayLprs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayLprs.setUnits("seconds")
_ZhoneVdslPerfDataCurr1DayLols_Type = Unsigned32
_ZhoneVdslPerfDataCurr1DayLols_Object = MibTableColumn
zhoneVdslPerfDataCurr1DayLols = _ZhoneVdslPerfDataCurr1DayLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 26),
    _ZhoneVdslPerfDataCurr1DayLols_Type()
)
zhoneVdslPerfDataCurr1DayLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayLols.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayLols.setUnits("seconds")
_ZhoneVdslPerfDataCurr1DayESs_Type = Unsigned32
_ZhoneVdslPerfDataCurr1DayESs_Object = MibTableColumn
zhoneVdslPerfDataCurr1DayESs = _ZhoneVdslPerfDataCurr1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 27),
    _ZhoneVdslPerfDataCurr1DayESs_Type()
)
zhoneVdslPerfDataCurr1DayESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayESs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayESs.setUnits("seconds")
_ZhoneVdslPerfDataCurr1DaySESs_Type = Unsigned32
_ZhoneVdslPerfDataCurr1DaySESs_Object = MibTableColumn
zhoneVdslPerfDataCurr1DaySESs = _ZhoneVdslPerfDataCurr1DaySESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 28),
    _ZhoneVdslPerfDataCurr1DaySESs_Type()
)
zhoneVdslPerfDataCurr1DaySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DaySESs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DaySESs.setUnits("seconds")
_ZhoneVdslPerfDataCurr1DayUASs_Type = Unsigned32
_ZhoneVdslPerfDataCurr1DayUASs_Object = MibTableColumn
zhoneVdslPerfDataCurr1DayUASs = _ZhoneVdslPerfDataCurr1DayUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 29),
    _ZhoneVdslPerfDataCurr1DayUASs_Type()
)
zhoneVdslPerfDataCurr1DayUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayUASs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayUASs.setUnits("seconds")
_ZhoneVdslPerfDataCurr1DayInits_Type = Unsigned32
_ZhoneVdslPerfDataCurr1DayInits_Object = MibTableColumn
zhoneVdslPerfDataCurr1DayInits = _ZhoneVdslPerfDataCurr1DayInits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 30),
    _ZhoneVdslPerfDataCurr1DayInits_Type()
)
zhoneVdslPerfDataCurr1DayInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayInits.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfDataCurr1DayInits.setUnits("seconds")
_ZhoneVdslPhyrRetransmittedCodewords_Type = Unsigned32
_ZhoneVdslPhyrRetransmittedCodewords_Object = MibTableColumn
zhoneVdslPhyrRetransmittedCodewords = _ZhoneVdslPhyrRetransmittedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 31),
    _ZhoneVdslPhyrRetransmittedCodewords_Type()
)
zhoneVdslPhyrRetransmittedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhyrRetransmittedCodewords.setStatus("current")
_ZhoneVdslPhyrCorrectedRetransmittedCodewords_Type = Unsigned32
_ZhoneVdslPhyrCorrectedRetransmittedCodewords_Object = MibTableColumn
zhoneVdslPhyrCorrectedRetransmittedCodewords = _ZhoneVdslPhyrCorrectedRetransmittedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 32),
    _ZhoneVdslPhyrCorrectedRetransmittedCodewords_Type()
)
zhoneVdslPhyrCorrectedRetransmittedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhyrCorrectedRetransmittedCodewords.setStatus("current")
_ZhoneVdslPhyrUncorrectableRetransmittedCodewords_Type = Unsigned32
_ZhoneVdslPhyrUncorrectableRetransmittedCodewords_Object = MibTableColumn
zhoneVdslPhyrUncorrectableRetransmittedCodewords = _ZhoneVdslPhyrUncorrectableRetransmittedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 33),
    _ZhoneVdslPhyrUncorrectableRetransmittedCodewords_Type()
)
zhoneVdslPhyrUncorrectableRetransmittedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhyrUncorrectableRetransmittedCodewords.setStatus("current")
_ZhoneVdslPhyrCurr15MinRetransmittedCodewords_Type = Unsigned32
_ZhoneVdslPhyrCurr15MinRetransmittedCodewords_Object = MibTableColumn
zhoneVdslPhyrCurr15MinRetransmittedCodewords = _ZhoneVdslPhyrCurr15MinRetransmittedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 34),
    _ZhoneVdslPhyrCurr15MinRetransmittedCodewords_Type()
)
zhoneVdslPhyrCurr15MinRetransmittedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhyrCurr15MinRetransmittedCodewords.setStatus("current")
_ZhoneVdslPhyrCurr15MinCorrectedRetransmittedCodewords_Type = Unsigned32
_ZhoneVdslPhyrCurr15MinCorrectedRetransmittedCodewords_Object = MibTableColumn
zhoneVdslPhyrCurr15MinCorrectedRetransmittedCodewords = _ZhoneVdslPhyrCurr15MinCorrectedRetransmittedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 35),
    _ZhoneVdslPhyrCurr15MinCorrectedRetransmittedCodewords_Type()
)
zhoneVdslPhyrCurr15MinCorrectedRetransmittedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhyrCurr15MinCorrectedRetransmittedCodewords.setStatus("current")
_ZhoneVdslPhyrCurr15MinUncorrectableRetransmittedCodewords_Type = Unsigned32
_ZhoneVdslPhyrCurr15MinUncorrectableRetransmittedCodewords_Object = MibTableColumn
zhoneVdslPhyrCurr15MinUncorrectableRetransmittedCodewords = _ZhoneVdslPhyrCurr15MinUncorrectableRetransmittedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 36),
    _ZhoneVdslPhyrCurr15MinUncorrectableRetransmittedCodewords_Type()
)
zhoneVdslPhyrCurr15MinUncorrectableRetransmittedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhyrCurr15MinUncorrectableRetransmittedCodewords.setStatus("current")
_ZhoneVdslPhyrCurr1DayRetransmittedCodewords_Type = Unsigned32
_ZhoneVdslPhyrCurr1DayRetransmittedCodewords_Object = MibTableColumn
zhoneVdslPhyrCurr1DayRetransmittedCodewords = _ZhoneVdslPhyrCurr1DayRetransmittedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 37),
    _ZhoneVdslPhyrCurr1DayRetransmittedCodewords_Type()
)
zhoneVdslPhyrCurr1DayRetransmittedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhyrCurr1DayRetransmittedCodewords.setStatus("current")
_ZhoneVdslPhyrCurr1DayCorrectedRetransmittedCodewords_Type = Unsigned32
_ZhoneVdslPhyrCurr1DayCorrectedRetransmittedCodewords_Object = MibTableColumn
zhoneVdslPhyrCurr1DayCorrectedRetransmittedCodewords = _ZhoneVdslPhyrCurr1DayCorrectedRetransmittedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 38),
    _ZhoneVdslPhyrCurr1DayCorrectedRetransmittedCodewords_Type()
)
zhoneVdslPhyrCurr1DayCorrectedRetransmittedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhyrCurr1DayCorrectedRetransmittedCodewords.setStatus("current")
_ZhoneVdslPhyrCurr1DayUncorrectableRetransmittedCodewords_Type = Unsigned32
_ZhoneVdslPhyrCurr1DayUncorrectableRetransmittedCodewords_Object = MibTableColumn
zhoneVdslPhyrCurr1DayUncorrectableRetransmittedCodewords = _ZhoneVdslPhyrCurr1DayUncorrectableRetransmittedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 39),
    _ZhoneVdslPhyrCurr1DayUncorrectableRetransmittedCodewords_Type()
)
zhoneVdslPhyrCurr1DayUncorrectableRetransmittedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhyrCurr1DayUncorrectableRetransmittedCodewords.setStatus("current")
_ZhoneVdslPhyrPrev1DayRetransmittedCodewords_Type = Unsigned32
_ZhoneVdslPhyrPrev1DayRetransmittedCodewords_Object = MibTableColumn
zhoneVdslPhyrPrev1DayRetransmittedCodewords = _ZhoneVdslPhyrPrev1DayRetransmittedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 40),
    _ZhoneVdslPhyrPrev1DayRetransmittedCodewords_Type()
)
zhoneVdslPhyrPrev1DayRetransmittedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhyrPrev1DayRetransmittedCodewords.setStatus("current")
_ZhoneVdslPhyrPrev1DayCorrectedRetransmittedCodewords_Type = Unsigned32
_ZhoneVdslPhyrPrev1DayCorrectedRetransmittedCodewords_Object = MibTableColumn
zhoneVdslPhyrPrev1DayCorrectedRetransmittedCodewords = _ZhoneVdslPhyrPrev1DayCorrectedRetransmittedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 41),
    _ZhoneVdslPhyrPrev1DayCorrectedRetransmittedCodewords_Type()
)
zhoneVdslPhyrPrev1DayCorrectedRetransmittedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhyrPrev1DayCorrectedRetransmittedCodewords.setStatus("current")
_ZhoneVdslPhyrPrev1DayUncorrectableRetransmittedCodewords_Type = Unsigned32
_ZhoneVdslPhyrPrev1DayUncorrectableRetransmittedCodewords_Object = MibTableColumn
zhoneVdslPhyrPrev1DayUncorrectableRetransmittedCodewords = _ZhoneVdslPhyrPrev1DayUncorrectableRetransmittedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 42),
    _ZhoneVdslPhyrPrev1DayUncorrectableRetransmittedCodewords_Type()
)
zhoneVdslPhyrPrev1DayUncorrectableRetransmittedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPhyrPrev1DayUncorrectableRetransmittedCodewords.setStatus("current")
_ZhoneVdslGinpLeftrSecs_Type = Unsigned32
_ZhoneVdslGinpLeftrSecs_Object = MibTableColumn
zhoneVdslGinpLeftrSecs = _ZhoneVdslGinpLeftrSecs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 43),
    _ZhoneVdslGinpLeftrSecs_Type()
)
zhoneVdslGinpLeftrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslGinpLeftrSecs.setStatus("current")
_ZhoneVdslGinpErrorFreeBits_Type = Unsigned32
_ZhoneVdslGinpErrorFreeBits_Object = MibTableColumn
zhoneVdslGinpErrorFreeBits = _ZhoneVdslGinpErrorFreeBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 44),
    _ZhoneVdslGinpErrorFreeBits_Type()
)
zhoneVdslGinpErrorFreeBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslGinpErrorFreeBits.setStatus("current")
_ZhoneVdslGinpMinEftr_Type = Unsigned32
_ZhoneVdslGinpMinEftr_Object = MibTableColumn
zhoneVdslGinpMinEftr = _ZhoneVdslGinpMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 45),
    _ZhoneVdslGinpMinEftr_Type()
)
zhoneVdslGinpMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslGinpMinEftr.setStatus("current")
_ZhoneVdslGinpCurr15MinLeftrSecs_Type = Unsigned32
_ZhoneVdslGinpCurr15MinLeftrSecs_Object = MibTableColumn
zhoneVdslGinpCurr15MinLeftrSecs = _ZhoneVdslGinpCurr15MinLeftrSecs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 46),
    _ZhoneVdslGinpCurr15MinLeftrSecs_Type()
)
zhoneVdslGinpCurr15MinLeftrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslGinpCurr15MinLeftrSecs.setStatus("current")
_ZhoneVdslGinpCurr15MinErrorFreeBits_Type = Unsigned32
_ZhoneVdslGinpCurr15MinErrorFreeBits_Object = MibTableColumn
zhoneVdslGinpCurr15MinErrorFreeBits = _ZhoneVdslGinpCurr15MinErrorFreeBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 47),
    _ZhoneVdslGinpCurr15MinErrorFreeBits_Type()
)
zhoneVdslGinpCurr15MinErrorFreeBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslGinpCurr15MinErrorFreeBits.setStatus("current")
_ZhoneVdslGinpCurr15MinMinEftr_Type = Unsigned32
_ZhoneVdslGinpCurr15MinMinEftr_Object = MibTableColumn
zhoneVdslGinpCurr15MinMinEftr = _ZhoneVdslGinpCurr15MinMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 48),
    _ZhoneVdslGinpCurr15MinMinEftr_Type()
)
zhoneVdslGinpCurr15MinMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslGinpCurr15MinMinEftr.setStatus("current")
_ZhoneVdslGinpCurr1DayLeftrSecs_Type = Unsigned32
_ZhoneVdslGinpCurr1DayLeftrSecs_Object = MibTableColumn
zhoneVdslGinpCurr1DayLeftrSecs = _ZhoneVdslGinpCurr1DayLeftrSecs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 49),
    _ZhoneVdslGinpCurr1DayLeftrSecs_Type()
)
zhoneVdslGinpCurr1DayLeftrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslGinpCurr1DayLeftrSecs.setStatus("current")
_ZhoneVdslGinpCurr1DayErrorFreeBits_Type = Unsigned32
_ZhoneVdslGinpCurr1DayErrorFreeBits_Object = MibTableColumn
zhoneVdslGinpCurr1DayErrorFreeBits = _ZhoneVdslGinpCurr1DayErrorFreeBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 50),
    _ZhoneVdslGinpCurr1DayErrorFreeBits_Type()
)
zhoneVdslGinpCurr1DayErrorFreeBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslGinpCurr1DayErrorFreeBits.setStatus("current")
_ZhoneVdslGinpCurr1DayMinEftr_Type = Unsigned32
_ZhoneVdslGinpCurr1DayMinEftr_Object = MibTableColumn
zhoneVdslGinpCurr1DayMinEftr = _ZhoneVdslGinpCurr1DayMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 51),
    _ZhoneVdslGinpCurr1DayMinEftr_Type()
)
zhoneVdslGinpCurr1DayMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslGinpCurr1DayMinEftr.setStatus("current")
_ZhoneVdslGinpPrev1DayLeftrSecs_Type = Integer32
_ZhoneVdslGinpPrev1DayLeftrSecs_Object = MibTableColumn
zhoneVdslGinpPrev1DayLeftrSecs = _ZhoneVdslGinpPrev1DayLeftrSecs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 52),
    _ZhoneVdslGinpPrev1DayLeftrSecs_Type()
)
zhoneVdslGinpPrev1DayLeftrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslGinpPrev1DayLeftrSecs.setStatus("current")
_ZhoneVdslGinpPrev1DayErrorFreeBits_Type = Integer32
_ZhoneVdslGinpPrev1DayErrorFreeBits_Object = MibTableColumn
zhoneVdslGinpPrev1DayErrorFreeBits = _ZhoneVdslGinpPrev1DayErrorFreeBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 53),
    _ZhoneVdslGinpPrev1DayErrorFreeBits_Type()
)
zhoneVdslGinpPrev1DayErrorFreeBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslGinpPrev1DayErrorFreeBits.setStatus("current")
_ZhoneVdslGinpPrev1DayMinEftr_Type = Integer32
_ZhoneVdslGinpPrev1DayMinEftr_Object = MibTableColumn
zhoneVdslGinpPrev1DayMinEftr = _ZhoneVdslGinpPrev1DayMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 4, 1, 54),
    _ZhoneVdslGinpPrev1DayMinEftr_Type()
)
zhoneVdslGinpPrev1DayMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslGinpPrev1DayMinEftr.setStatus("current")
_ZhoneVdslPerfIntervalTable_Object = MibTable
zhoneVdslPerfIntervalTable = _ZhoneVdslPerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 5)
)
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalTable.setStatus("current")
_ZhoneVdslPerfIntervalEntry_Object = MibTableRow
zhoneVdslPerfIntervalEntry = _ZhoneVdslPerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 5, 1)
)
zhoneVdslPerfIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslPhysSide"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalEntry.setStatus("current")


class _ZhoneVdslPerfIntervalNumber_Type(Unsigned32):
    """Custom type zhoneVdslPerfIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ZhoneVdslPerfIntervalNumber_Type.__name__ = "Unsigned32"
_ZhoneVdslPerfIntervalNumber_Object = MibTableColumn
zhoneVdslPerfIntervalNumber = _ZhoneVdslPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 5, 1, 1),
    _ZhoneVdslPerfIntervalNumber_Type()
)
zhoneVdslPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalNumber.setStatus("current")
_ZhoneVdslPerfIntervalLofs_Type = HCPerfIntervalCount
_ZhoneVdslPerfIntervalLofs_Object = MibTableColumn
zhoneVdslPerfIntervalLofs = _ZhoneVdslPerfIntervalLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 5, 1, 2),
    _ZhoneVdslPerfIntervalLofs_Type()
)
zhoneVdslPerfIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalLofs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalLofs.setUnits("seconds")
_ZhoneVdslPerfIntervalLoss_Type = HCPerfIntervalCount
_ZhoneVdslPerfIntervalLoss_Object = MibTableColumn
zhoneVdslPerfIntervalLoss = _ZhoneVdslPerfIntervalLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 5, 1, 3),
    _ZhoneVdslPerfIntervalLoss_Type()
)
zhoneVdslPerfIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalLoss.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalLoss.setUnits("seconds")
_ZhoneVdslPerfIntervalLprs_Type = HCPerfIntervalCount
_ZhoneVdslPerfIntervalLprs_Object = MibTableColumn
zhoneVdslPerfIntervalLprs = _ZhoneVdslPerfIntervalLprs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 5, 1, 4),
    _ZhoneVdslPerfIntervalLprs_Type()
)
zhoneVdslPerfIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalLprs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalLprs.setUnits("seconds")
_ZhoneVdslPerfIntervalLols_Type = HCPerfIntervalCount
_ZhoneVdslPerfIntervalLols_Object = MibTableColumn
zhoneVdslPerfIntervalLols = _ZhoneVdslPerfIntervalLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 5, 1, 5),
    _ZhoneVdslPerfIntervalLols_Type()
)
zhoneVdslPerfIntervalLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalLols.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalLols.setUnits("seconds")
_ZhoneVdslPerfIntervalESs_Type = HCPerfIntervalCount
_ZhoneVdslPerfIntervalESs_Object = MibTableColumn
zhoneVdslPerfIntervalESs = _ZhoneVdslPerfIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 5, 1, 6),
    _ZhoneVdslPerfIntervalESs_Type()
)
zhoneVdslPerfIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalESs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalESs.setUnits("seconds")
_ZhoneVdslPerfIntervalSESs_Type = HCPerfIntervalCount
_ZhoneVdslPerfIntervalSESs_Object = MibTableColumn
zhoneVdslPerfIntervalSESs = _ZhoneVdslPerfIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 5, 1, 7),
    _ZhoneVdslPerfIntervalSESs_Type()
)
zhoneVdslPerfIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalSESs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalSESs.setUnits("seconds")
_ZhoneVdslPerfIntervalUASs_Type = HCPerfIntervalCount
_ZhoneVdslPerfIntervalUASs_Object = MibTableColumn
zhoneVdslPerfIntervalUASs = _ZhoneVdslPerfIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 5, 1, 8),
    _ZhoneVdslPerfIntervalUASs_Type()
)
zhoneVdslPerfIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalUASs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalUASs.setUnits("seconds")
_ZhoneVdslPerfIntervalInits_Type = HCPerfIntervalCount
_ZhoneVdslPerfIntervalInits_Object = MibTableColumn
zhoneVdslPerfIntervalInits = _ZhoneVdslPerfIntervalInits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 5, 1, 9),
    _ZhoneVdslPerfIntervalInits_Type()
)
zhoneVdslPerfIntervalInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerfIntervalInits.setStatus("current")
_ZhoneVdslPerf1DayIntervalTable_Object = MibTable
zhoneVdslPerf1DayIntervalTable = _ZhoneVdslPerf1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 6)
)
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalTable.setStatus("current")
_ZhoneVdslPerf1DayIntervalEntry_Object = MibTableRow
zhoneVdslPerf1DayIntervalEntry = _ZhoneVdslPerf1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 6, 1)
)
zhoneVdslPerf1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslPhysSide"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslPerf1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalEntry.setStatus("current")


class _ZhoneVdslPerf1DayIntervalNumber_Type(Unsigned32):
    """Custom type zhoneVdslPerf1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ZhoneVdslPerf1DayIntervalNumber_Type.__name__ = "Unsigned32"
_ZhoneVdslPerf1DayIntervalNumber_Object = MibTableColumn
zhoneVdslPerf1DayIntervalNumber = _ZhoneVdslPerf1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 6, 1, 1),
    _ZhoneVdslPerf1DayIntervalNumber_Type()
)
zhoneVdslPerf1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalNumber.setStatus("current")
_ZhoneVdslPerf1DayIntervalMoniSecs_Type = HCPerfTimeElapsed
_ZhoneVdslPerf1DayIntervalMoniSecs_Object = MibTableColumn
zhoneVdslPerf1DayIntervalMoniSecs = _ZhoneVdslPerf1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 6, 1, 2),
    _ZhoneVdslPerf1DayIntervalMoniSecs_Type()
)
zhoneVdslPerf1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalMoniSecs.setUnits("seconds")
_ZhoneVdslPerf1DayIntervalLofs_Type = Unsigned32
_ZhoneVdslPerf1DayIntervalLofs_Object = MibTableColumn
zhoneVdslPerf1DayIntervalLofs = _ZhoneVdslPerf1DayIntervalLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 6, 1, 3),
    _ZhoneVdslPerf1DayIntervalLofs_Type()
)
zhoneVdslPerf1DayIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalLofs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalLofs.setUnits("seconds")
_ZhoneVdslPerf1DayIntervalLoss_Type = Unsigned32
_ZhoneVdslPerf1DayIntervalLoss_Object = MibTableColumn
zhoneVdslPerf1DayIntervalLoss = _ZhoneVdslPerf1DayIntervalLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 6, 1, 4),
    _ZhoneVdslPerf1DayIntervalLoss_Type()
)
zhoneVdslPerf1DayIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalLoss.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalLoss.setUnits("seconds")
_ZhoneVdslPerf1DayIntervalLprs_Type = Unsigned32
_ZhoneVdslPerf1DayIntervalLprs_Object = MibTableColumn
zhoneVdslPerf1DayIntervalLprs = _ZhoneVdslPerf1DayIntervalLprs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 6, 1, 5),
    _ZhoneVdslPerf1DayIntervalLprs_Type()
)
zhoneVdslPerf1DayIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalLprs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalLprs.setUnits("seconds")
_ZhoneVdslPerf1DayIntervalLols_Type = Unsigned32
_ZhoneVdslPerf1DayIntervalLols_Object = MibTableColumn
zhoneVdslPerf1DayIntervalLols = _ZhoneVdslPerf1DayIntervalLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 6, 1, 6),
    _ZhoneVdslPerf1DayIntervalLols_Type()
)
zhoneVdslPerf1DayIntervalLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalLols.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalLols.setUnits("seconds")
_ZhoneVdslPerf1DayIntervalESs_Type = Unsigned32
_ZhoneVdslPerf1DayIntervalESs_Object = MibTableColumn
zhoneVdslPerf1DayIntervalESs = _ZhoneVdslPerf1DayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 6, 1, 7),
    _ZhoneVdslPerf1DayIntervalESs_Type()
)
zhoneVdslPerf1DayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalESs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalESs.setUnits("seconds")
_ZhoneVdslPerf1DayIntervalSESs_Type = Unsigned32
_ZhoneVdslPerf1DayIntervalSESs_Object = MibTableColumn
zhoneVdslPerf1DayIntervalSESs = _ZhoneVdslPerf1DayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 6, 1, 8),
    _ZhoneVdslPerf1DayIntervalSESs_Type()
)
zhoneVdslPerf1DayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalSESs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalSESs.setUnits("seconds")
_ZhoneVdslPerf1DayIntervalUASs_Type = Unsigned32
_ZhoneVdslPerf1DayIntervalUASs_Object = MibTableColumn
zhoneVdslPerf1DayIntervalUASs = _ZhoneVdslPerf1DayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 6, 1, 9),
    _ZhoneVdslPerf1DayIntervalUASs_Type()
)
zhoneVdslPerf1DayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalUASs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalUASs.setUnits("seconds")
_ZhoneVdslPerf1DayIntervalInits_Type = Unsigned32
_ZhoneVdslPerf1DayIntervalInits_Object = MibTableColumn
zhoneVdslPerf1DayIntervalInits = _ZhoneVdslPerf1DayIntervalInits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 6, 1, 10),
    _ZhoneVdslPerf1DayIntervalInits_Type()
)
zhoneVdslPerf1DayIntervalInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalInits.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslPerf1DayIntervalInits.setUnits("seconds")
_ZhoneVdslChanPerfDataTable_Object = MibTable
zhoneVdslChanPerfDataTable = _ZhoneVdslChanPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7)
)
if mibBuilder.loadTexts:
    zhoneVdslChanPerfDataTable.setStatus("current")
_ZhoneVdslChanPerfDataEntry_Object = MibTableRow
zhoneVdslChanPerfDataEntry = _ZhoneVdslChanPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1)
)
zhoneVdslChanPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslPhysSide"),
)
if mibBuilder.loadTexts:
    zhoneVdslChanPerfDataEntry.setStatus("current")


class _ZhoneVdslChanValidIntervals_Type(Integer32):
    """Custom type zhoneVdslChanValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZhoneVdslChanValidIntervals_Type.__name__ = "Integer32"
_ZhoneVdslChanValidIntervals_Object = MibTableColumn
zhoneVdslChanValidIntervals = _ZhoneVdslChanValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1, 1),
    _ZhoneVdslChanValidIntervals_Type()
)
zhoneVdslChanValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanValidIntervals.setUnits("intervals")


class _ZhoneVdslChanInvalidIntervals_Type(Integer32):
    """Custom type zhoneVdslChanInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZhoneVdslChanInvalidIntervals_Type.__name__ = "Integer32"
_ZhoneVdslChanInvalidIntervals_Object = MibTableColumn
zhoneVdslChanInvalidIntervals = _ZhoneVdslChanInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1, 2),
    _ZhoneVdslChanInvalidIntervals_Type()
)
zhoneVdslChanInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanInvalidIntervals.setUnits("intervals")
_ZhoneVdslChanFixedOctets_Type = Integer32
_ZhoneVdslChanFixedOctets_Object = MibTableColumn
zhoneVdslChanFixedOctets = _ZhoneVdslChanFixedOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1, 3),
    _ZhoneVdslChanFixedOctets_Type()
)
zhoneVdslChanFixedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanFixedOctets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanFixedOctets.setUnits("octets")
_ZhoneVdslChanBadBlks_Type = Integer32
_ZhoneVdslChanBadBlks_Object = MibTableColumn
zhoneVdslChanBadBlks = _ZhoneVdslChanBadBlks_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1, 4),
    _ZhoneVdslChanBadBlks_Type()
)
zhoneVdslChanBadBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanBadBlks.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanBadBlks.setUnits("blocks")


class _ZhoneVdslChanCurr15MinTimeElapsed_Type(Integer32):
    """Custom type zhoneVdslChanCurr15MinTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_ZhoneVdslChanCurr15MinTimeElapsed_Type.__name__ = "Integer32"
_ZhoneVdslChanCurr15MinTimeElapsed_Object = MibTableColumn
zhoneVdslChanCurr15MinTimeElapsed = _ZhoneVdslChanCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1, 5),
    _ZhoneVdslChanCurr15MinTimeElapsed_Type()
)
zhoneVdslChanCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanCurr15MinTimeElapsed.setUnits("seconds")
_ZhoneVdslChanCurr15MinFixedOctets_Type = Integer32
_ZhoneVdslChanCurr15MinFixedOctets_Object = MibTableColumn
zhoneVdslChanCurr15MinFixedOctets = _ZhoneVdslChanCurr15MinFixedOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1, 6),
    _ZhoneVdslChanCurr15MinFixedOctets_Type()
)
zhoneVdslChanCurr15MinFixedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanCurr15MinFixedOctets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanCurr15MinFixedOctets.setUnits("octets")
_ZhoneVdslChanCurr15MinBadBlks_Type = Integer32
_ZhoneVdslChanCurr15MinBadBlks_Object = MibTableColumn
zhoneVdslChanCurr15MinBadBlks = _ZhoneVdslChanCurr15MinBadBlks_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1, 7),
    _ZhoneVdslChanCurr15MinBadBlks_Type()
)
zhoneVdslChanCurr15MinBadBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanCurr15MinBadBlks.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanCurr15MinBadBlks.setUnits("blocks")


class _ZhoneVdslChan1DayValidIntervals_Type(Integer32):
    """Custom type zhoneVdslChan1DayValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZhoneVdslChan1DayValidIntervals_Type.__name__ = "Integer32"
_ZhoneVdslChan1DayValidIntervals_Object = MibTableColumn
zhoneVdslChan1DayValidIntervals = _ZhoneVdslChan1DayValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1, 8),
    _ZhoneVdslChan1DayValidIntervals_Type()
)
zhoneVdslChan1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChan1DayValidIntervals.setStatus("current")


class _ZhoneVdslChan1DayInvalidIntervals_Type(Integer32):
    """Custom type zhoneVdslChan1DayInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZhoneVdslChan1DayInvalidIntervals_Type.__name__ = "Integer32"
_ZhoneVdslChan1DayInvalidIntervals_Object = MibTableColumn
zhoneVdslChan1DayInvalidIntervals = _ZhoneVdslChan1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1, 9),
    _ZhoneVdslChan1DayInvalidIntervals_Type()
)
zhoneVdslChan1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChan1DayInvalidIntervals.setStatus("current")


class _ZhoneVdslChanCurr1DayTimeElapsed_Type(Integer32):
    """Custom type zhoneVdslChanCurr1DayTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_ZhoneVdslChanCurr1DayTimeElapsed_Type.__name__ = "Integer32"
_ZhoneVdslChanCurr1DayTimeElapsed_Object = MibTableColumn
zhoneVdslChanCurr1DayTimeElapsed = _ZhoneVdslChanCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1, 10),
    _ZhoneVdslChanCurr1DayTimeElapsed_Type()
)
zhoneVdslChanCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanCurr1DayTimeElapsed.setUnits("seconds")
_ZhoneVdslChanCurr1DayFixedOctets_Type = Integer32
_ZhoneVdslChanCurr1DayFixedOctets_Object = MibTableColumn
zhoneVdslChanCurr1DayFixedOctets = _ZhoneVdslChanCurr1DayFixedOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1, 11),
    _ZhoneVdslChanCurr1DayFixedOctets_Type()
)
zhoneVdslChanCurr1DayFixedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanCurr1DayFixedOctets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanCurr1DayFixedOctets.setUnits("octets")
_ZhoneVdslChanCurr1DayBadBlks_Type = Integer32
_ZhoneVdslChanCurr1DayBadBlks_Object = MibTableColumn
zhoneVdslChanCurr1DayBadBlks = _ZhoneVdslChanCurr1DayBadBlks_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 7, 1, 12),
    _ZhoneVdslChanCurr1DayBadBlks_Type()
)
zhoneVdslChanCurr1DayBadBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanCurr1DayBadBlks.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanCurr1DayBadBlks.setUnits("blocks")
_ZhoneVdslChanIntervalTable_Object = MibTable
zhoneVdslChanIntervalTable = _ZhoneVdslChanIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 8)
)
if mibBuilder.loadTexts:
    zhoneVdslChanIntervalTable.setStatus("current")
_ZhoneVdslChanIntervalEntry_Object = MibTableRow
zhoneVdslChanIntervalEntry = _ZhoneVdslChanIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 8, 1)
)
zhoneVdslChanIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslPhysSide"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslChanIntervalNumber"),
)
if mibBuilder.loadTexts:
    zhoneVdslChanIntervalEntry.setStatus("current")


class _ZhoneVdslChanIntervalNumber_Type(Unsigned32):
    """Custom type zhoneVdslChanIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ZhoneVdslChanIntervalNumber_Type.__name__ = "Unsigned32"
_ZhoneVdslChanIntervalNumber_Object = MibTableColumn
zhoneVdslChanIntervalNumber = _ZhoneVdslChanIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 8, 1, 1),
    _ZhoneVdslChanIntervalNumber_Type()
)
zhoneVdslChanIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVdslChanIntervalNumber.setStatus("current")
_ZhoneVdslChanIntervalFixedOctets_Type = HCPerfIntervalCount
_ZhoneVdslChanIntervalFixedOctets_Object = MibTableColumn
zhoneVdslChanIntervalFixedOctets = _ZhoneVdslChanIntervalFixedOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 8, 1, 2),
    _ZhoneVdslChanIntervalFixedOctets_Type()
)
zhoneVdslChanIntervalFixedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanIntervalFixedOctets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanIntervalFixedOctets.setUnits("octets")
_ZhoneVdslChanIntervalBadBlks_Type = HCPerfIntervalCount
_ZhoneVdslChanIntervalBadBlks_Object = MibTableColumn
zhoneVdslChanIntervalBadBlks = _ZhoneVdslChanIntervalBadBlks_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 8, 1, 3),
    _ZhoneVdslChanIntervalBadBlks_Type()
)
zhoneVdslChanIntervalBadBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChanIntervalBadBlks.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChanIntervalBadBlks.setUnits("blocks")
_ZhoneVdslChan1DayIntervalTable_Object = MibTable
zhoneVdslChan1DayIntervalTable = _ZhoneVdslChan1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 9)
)
if mibBuilder.loadTexts:
    zhoneVdslChan1DayIntervalTable.setStatus("current")
_ZhoneVdslChan1DayIntervalEntry_Object = MibTableRow
zhoneVdslChan1DayIntervalEntry = _ZhoneVdslChan1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 9, 1)
)
zhoneVdslChan1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslPhysSide"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslChan1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    zhoneVdslChan1DayIntervalEntry.setStatus("current")


class _ZhoneVdslChan1DayIntervalNumber_Type(Unsigned32):
    """Custom type zhoneVdslChan1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ZhoneVdslChan1DayIntervalNumber_Type.__name__ = "Unsigned32"
_ZhoneVdslChan1DayIntervalNumber_Object = MibTableColumn
zhoneVdslChan1DayIntervalNumber = _ZhoneVdslChan1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 9, 1, 1),
    _ZhoneVdslChan1DayIntervalNumber_Type()
)
zhoneVdslChan1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVdslChan1DayIntervalNumber.setStatus("current")
_ZhoneVdslChan1DayIntervalMoniSecs_Type = HCPerfTimeElapsed
_ZhoneVdslChan1DayIntervalMoniSecs_Object = MibTableColumn
zhoneVdslChan1DayIntervalMoniSecs = _ZhoneVdslChan1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 9, 1, 2),
    _ZhoneVdslChan1DayIntervalMoniSecs_Type()
)
zhoneVdslChan1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChan1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChan1DayIntervalMoniSecs.setUnits("seconds")
_ZhoneVdslChan1DayIntervalFixedOctets_Type = HCPerfCurrentCount
_ZhoneVdslChan1DayIntervalFixedOctets_Object = MibTableColumn
zhoneVdslChan1DayIntervalFixedOctets = _ZhoneVdslChan1DayIntervalFixedOctets_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 9, 1, 3),
    _ZhoneVdslChan1DayIntervalFixedOctets_Type()
)
zhoneVdslChan1DayIntervalFixedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChan1DayIntervalFixedOctets.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChan1DayIntervalFixedOctets.setUnits("octets")
_ZhoneVdslChan1DayIntervalBadBlks_Type = HCPerfCurrentCount
_ZhoneVdslChan1DayIntervalBadBlks_Object = MibTableColumn
zhoneVdslChan1DayIntervalBadBlks = _ZhoneVdslChan1DayIntervalBadBlks_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 9, 1, 4),
    _ZhoneVdslChan1DayIntervalBadBlks_Type()
)
zhoneVdslChan1DayIntervalBadBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslChan1DayIntervalBadBlks.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslChan1DayIntervalBadBlks.setUnits("blocks")
_ZhoneVdslLineConfProfileTable_Object = MibTable
zhoneVdslLineConfProfileTable = _ZhoneVdslLineConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11)
)
if mibBuilder.loadTexts:
    zhoneVdslLineConfProfileTable.setStatus("current")
_ZhoneVdslLineConfProfileEntry_Object = MibTableRow
zhoneVdslLineConfProfileEntry = _ZhoneVdslLineConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1)
)
zhoneVdslLineConfProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneVdslLineConfProfileEntry.setStatus("current")


class _ZhoneVdslLineConfProfileName_Type(SnmpAdminString):
    """Custom type zhoneVdslLineConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZhoneVdslLineConfProfileName_Type.__name__ = "SnmpAdminString"
_ZhoneVdslLineConfProfileName_Object = MibTableColumn
zhoneVdslLineConfProfileName = _ZhoneVdslLineConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 1),
    _ZhoneVdslLineConfProfileName_Type()
)
zhoneVdslLineConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVdslLineConfProfileName.setStatus("current")


class _ZhoneVdslLineConfDownRateMode_Type(Integer32):
    """Custom type zhoneVdslLineConfDownRateMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adapt-at-init", 2),
          ("dynamic", 3),
          ("manual", 1))
    )


_ZhoneVdslLineConfDownRateMode_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownRateMode_Object = MibTableColumn
zhoneVdslLineConfDownRateMode = _ZhoneVdslLineConfDownRateMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 2),
    _ZhoneVdslLineConfDownRateMode_Type()
)
zhoneVdslLineConfDownRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownRateMode.setStatus("current")


class _ZhoneVdslLineConfUpRateMode_Type(Integer32):
    """Custom type zhoneVdslLineConfUpRateMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adapt-at-init", 2),
          ("dynamic", 3),
          ("manual", 1))
    )


_ZhoneVdslLineConfUpRateMode_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpRateMode_Object = MibTableColumn
zhoneVdslLineConfUpRateMode = _ZhoneVdslLineConfUpRateMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 3),
    _ZhoneVdslLineConfUpRateMode_Type()
)
zhoneVdslLineConfUpRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpRateMode.setStatus("current")


class _ZhoneVdslLineConfDownMaxPwr_Type(Integer32):
    """Custom type zhoneVdslLineConfDownMaxPwr based on Integer32"""
    defaultValue = 145

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_ZhoneVdslLineConfDownMaxPwr_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownMaxPwr_Object = MibTableColumn
zhoneVdslLineConfDownMaxPwr = _ZhoneVdslLineConfDownMaxPwr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 4),
    _ZhoneVdslLineConfDownMaxPwr_Type()
)
zhoneVdslLineConfDownMaxPwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxPwr.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxPwr.setUnits("0.10dBm")


class _ZhoneVdslLineConfUpMaxPwr_Type(Integer32):
    """Custom type zhoneVdslLineConfUpMaxPwr based on Integer32"""
    defaultValue = 145

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-130, 200),
    )


_ZhoneVdslLineConfUpMaxPwr_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpMaxPwr_Object = MibTableColumn
zhoneVdslLineConfUpMaxPwr = _ZhoneVdslLineConfUpMaxPwr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 5),
    _ZhoneVdslLineConfUpMaxPwr_Type()
)
zhoneVdslLineConfUpMaxPwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxPwr.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxPwr.setUnits("0.10dBm")


class _ZhoneVdslLineConfDownMaxSnrMgn_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownMaxSnrMgn based on Unsigned32"""
    defaultValue = 160

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_ZhoneVdslLineConfDownMaxSnrMgn_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownMaxSnrMgn_Object = MibTableColumn
zhoneVdslLineConfDownMaxSnrMgn = _ZhoneVdslLineConfDownMaxSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 6),
    _ZhoneVdslLineConfDownMaxSnrMgn_Type()
)
zhoneVdslLineConfDownMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxSnrMgn.setUnits("0.10dBm")


class _ZhoneVdslLineConfDownMinSnrMgn_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownMinSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_ZhoneVdslLineConfDownMinSnrMgn_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownMinSnrMgn_Object = MibTableColumn
zhoneVdslLineConfDownMinSnrMgn = _ZhoneVdslLineConfDownMinSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 7),
    _ZhoneVdslLineConfDownMinSnrMgn_Type()
)
zhoneVdslLineConfDownMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMinSnrMgn.setUnits("0.10dBm")


class _ZhoneVdslLineConfDownTargetSnrMgn_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownTargetSnrMgn based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_ZhoneVdslLineConfDownTargetSnrMgn_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownTargetSnrMgn_Object = MibTableColumn
zhoneVdslLineConfDownTargetSnrMgn = _ZhoneVdslLineConfDownTargetSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 8),
    _ZhoneVdslLineConfDownTargetSnrMgn_Type()
)
zhoneVdslLineConfDownTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownTargetSnrMgn.setUnits("0.10dBm")


class _ZhoneVdslLineConfUpMaxSnrMgn_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpMaxSnrMgn based on Unsigned32"""
    defaultValue = 160

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_ZhoneVdslLineConfUpMaxSnrMgn_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpMaxSnrMgn_Object = MibTableColumn
zhoneVdslLineConfUpMaxSnrMgn = _ZhoneVdslLineConfUpMaxSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 9),
    _ZhoneVdslLineConfUpMaxSnrMgn_Type()
)
zhoneVdslLineConfUpMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxSnrMgn.setUnits("0.10dBm")


class _ZhoneVdslLineConfUpMinSnrMgn_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpMinSnrMgn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_ZhoneVdslLineConfUpMinSnrMgn_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpMinSnrMgn_Object = MibTableColumn
zhoneVdslLineConfUpMinSnrMgn = _ZhoneVdslLineConfUpMinSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 10),
    _ZhoneVdslLineConfUpMinSnrMgn_Type()
)
zhoneVdslLineConfUpMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMinSnrMgn.setUnits("0.10dBm")


class _ZhoneVdslLineConfUpTargetSnrMgn_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpTargetSnrMgn based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_ZhoneVdslLineConfUpTargetSnrMgn_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpTargetSnrMgn_Object = MibTableColumn
zhoneVdslLineConfUpTargetSnrMgn = _ZhoneVdslLineConfUpTargetSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 11),
    _ZhoneVdslLineConfUpTargetSnrMgn_Type()
)
zhoneVdslLineConfUpTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpTargetSnrMgn.setUnits("0.10dBm")


class _ZhoneVdslLineConfDownFastMaxDataRate_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownFastMaxDataRate based on Unsigned32"""
    defaultValue = 200000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ZhoneVdslLineConfDownFastMaxDataRate_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownFastMaxDataRate_Object = MibTableColumn
zhoneVdslLineConfDownFastMaxDataRate = _ZhoneVdslLineConfDownFastMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 12),
    _ZhoneVdslLineConfDownFastMaxDataRate_Type()
)
zhoneVdslLineConfDownFastMaxDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownFastMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownFastMaxDataRate.setUnits("kbps")


class _ZhoneVdslLineConfDownFastMinDataRate_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownFastMinDataRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ZhoneVdslLineConfDownFastMinDataRate_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownFastMinDataRate_Object = MibTableColumn
zhoneVdslLineConfDownFastMinDataRate = _ZhoneVdslLineConfDownFastMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 13),
    _ZhoneVdslLineConfDownFastMinDataRate_Type()
)
zhoneVdslLineConfDownFastMinDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownFastMinDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownFastMinDataRate.setUnits("kbps")


class _ZhoneVdslLineConfDownSlowMaxDataRate_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownSlowMaxDataRate based on Unsigned32"""
    defaultValue = 200000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ZhoneVdslLineConfDownSlowMaxDataRate_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownSlowMaxDataRate_Object = MibTableColumn
zhoneVdslLineConfDownSlowMaxDataRate = _ZhoneVdslLineConfDownSlowMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 14),
    _ZhoneVdslLineConfDownSlowMaxDataRate_Type()
)
zhoneVdslLineConfDownSlowMaxDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownSlowMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownSlowMaxDataRate.setUnits("kbps")


class _ZhoneVdslLineConfDownSlowMinDataRate_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownSlowMinDataRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ZhoneVdslLineConfDownSlowMinDataRate_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownSlowMinDataRate_Object = MibTableColumn
zhoneVdslLineConfDownSlowMinDataRate = _ZhoneVdslLineConfDownSlowMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 15),
    _ZhoneVdslLineConfDownSlowMinDataRate_Type()
)
zhoneVdslLineConfDownSlowMinDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownSlowMinDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownSlowMinDataRate.setUnits("kbps")


class _ZhoneVdslLineConfUpFastMaxDataRate_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpFastMaxDataRate based on Unsigned32"""
    defaultValue = 200000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ZhoneVdslLineConfUpFastMaxDataRate_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpFastMaxDataRate_Object = MibTableColumn
zhoneVdslLineConfUpFastMaxDataRate = _ZhoneVdslLineConfUpFastMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 16),
    _ZhoneVdslLineConfUpFastMaxDataRate_Type()
)
zhoneVdslLineConfUpFastMaxDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpFastMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpFastMaxDataRate.setUnits("kbps")


class _ZhoneVdslLineConfUpFastMinDataRate_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpFastMinDataRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ZhoneVdslLineConfUpFastMinDataRate_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpFastMinDataRate_Object = MibTableColumn
zhoneVdslLineConfUpFastMinDataRate = _ZhoneVdslLineConfUpFastMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 17),
    _ZhoneVdslLineConfUpFastMinDataRate_Type()
)
zhoneVdslLineConfUpFastMinDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpFastMinDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpFastMinDataRate.setUnits("kbps")


class _ZhoneVdslLineConfUpSlowMaxDataRate_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpSlowMaxDataRate based on Unsigned32"""
    defaultValue = 200000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ZhoneVdslLineConfUpSlowMaxDataRate_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpSlowMaxDataRate_Object = MibTableColumn
zhoneVdslLineConfUpSlowMaxDataRate = _ZhoneVdslLineConfUpSlowMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 18),
    _ZhoneVdslLineConfUpSlowMaxDataRate_Type()
)
zhoneVdslLineConfUpSlowMaxDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpSlowMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpSlowMaxDataRate.setUnits("kbps")


class _ZhoneVdslLineConfUpSlowMinDataRate_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpSlowMinDataRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ZhoneVdslLineConfUpSlowMinDataRate_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpSlowMinDataRate_Object = MibTableColumn
zhoneVdslLineConfUpSlowMinDataRate = _ZhoneVdslLineConfUpSlowMinDataRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 19),
    _ZhoneVdslLineConfUpSlowMinDataRate_Type()
)
zhoneVdslLineConfUpSlowMinDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpSlowMinDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpSlowMinDataRate.setUnits("kbps")


class _ZhoneVdslLineConfDownRateRatio_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownRateRatio based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZhoneVdslLineConfDownRateRatio_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownRateRatio_Object = MibTableColumn
zhoneVdslLineConfDownRateRatio = _ZhoneVdslLineConfDownRateRatio_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 20),
    _ZhoneVdslLineConfDownRateRatio_Type()
)
zhoneVdslLineConfDownRateRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownRateRatio.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownRateRatio.setUnits("percent")


class _ZhoneVdslLineConfUpRateRatio_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpRateRatio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZhoneVdslLineConfUpRateRatio_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpRateRatio_Object = MibTableColumn
zhoneVdslLineConfUpRateRatio = _ZhoneVdslLineConfUpRateRatio_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 21),
    _ZhoneVdslLineConfUpRateRatio_Type()
)
zhoneVdslLineConfUpRateRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpRateRatio.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpRateRatio.setUnits("percent")


class _ZhoneVdslLineConfDownMaxInterDelay_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownMaxInterDelay based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneVdslLineConfDownMaxInterDelay_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownMaxInterDelay_Object = MibTableColumn
zhoneVdslLineConfDownMaxInterDelay = _ZhoneVdslLineConfDownMaxInterDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 22),
    _ZhoneVdslLineConfDownMaxInterDelay_Type()
)
zhoneVdslLineConfDownMaxInterDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxInterDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxInterDelay.setUnits("milliseconds")


class _ZhoneVdslLineConfUpMaxInterDelay_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpMaxInterDelay based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneVdslLineConfUpMaxInterDelay_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpMaxInterDelay_Object = MibTableColumn
zhoneVdslLineConfUpMaxInterDelay = _ZhoneVdslLineConfUpMaxInterDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 23),
    _ZhoneVdslLineConfUpMaxInterDelay_Type()
)
zhoneVdslLineConfUpMaxInterDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxInterDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxInterDelay.setUnits("milliseconds")


class _ZhoneVdslLineConfDownPboControl_Type(Integer32):
    """Custom type zhoneVdslLineConfDownPboControl based on Integer32"""
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
        *(("auto", 2),
          ("disabled", 1),
          ("manual", 3))
    )


_ZhoneVdslLineConfDownPboControl_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownPboControl_Object = MibTableColumn
zhoneVdslLineConfDownPboControl = _ZhoneVdslLineConfDownPboControl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 24),
    _ZhoneVdslLineConfDownPboControl_Type()
)
zhoneVdslLineConfDownPboControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownPboControl.setStatus("current")


class _ZhoneVdslLineConfUpPboControl_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPboControl based on Integer32"""
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
        *(("auto", 2),
          ("disabled", 1),
          ("manual", 3))
    )


_ZhoneVdslLineConfUpPboControl_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPboControl_Object = MibTableColumn
zhoneVdslLineConfUpPboControl = _ZhoneVdslLineConfUpPboControl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 25),
    _ZhoneVdslLineConfUpPboControl_Type()
)
zhoneVdslLineConfUpPboControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboControl.setStatus("current")


class _ZhoneVdslLineConfDownPboLevel_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownPboLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_ZhoneVdslLineConfDownPboLevel_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownPboLevel_Object = MibTableColumn
zhoneVdslLineConfDownPboLevel = _ZhoneVdslLineConfDownPboLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 26),
    _ZhoneVdslLineConfDownPboLevel_Type()
)
zhoneVdslLineConfDownPboLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownPboLevel.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownPboLevel.setUnits("0.25dB")


class _ZhoneVdslLineConfUpPboLevel_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpPboLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_ZhoneVdslLineConfUpPboLevel_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpPboLevel_Object = MibTableColumn
zhoneVdslLineConfUpPboLevel = _ZhoneVdslLineConfUpPboLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 27),
    _ZhoneVdslLineConfUpPboLevel_Type()
)
zhoneVdslLineConfUpPboLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboLevel.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboLevel.setUnits("0.25dB")


class _ZhoneVdslLineConfDeploymentScenario_Type(Integer32):
    """Custom type zhoneVdslLineConfDeploymentScenario based on Integer32"""
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
        *(("fttCab", 1),
          ("fttEx", 2),
          ("other", 3))
    )


_ZhoneVdslLineConfDeploymentScenario_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDeploymentScenario_Object = MibTableColumn
zhoneVdslLineConfDeploymentScenario = _ZhoneVdslLineConfDeploymentScenario_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 28),
    _ZhoneVdslLineConfDeploymentScenario_Type()
)
zhoneVdslLineConfDeploymentScenario.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDeploymentScenario.setStatus("current")


class _ZhoneVdslLineConfAdslPresence_Type(Integer32):
    """Custom type zhoneVdslLineConfAdslPresence based on Integer32"""
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
        *(("adslOverISDN", 3),
          ("adslOverPots", 2),
          ("none", 1))
    )


_ZhoneVdslLineConfAdslPresence_Type.__name__ = "Integer32"
_ZhoneVdslLineConfAdslPresence_Object = MibTableColumn
zhoneVdslLineConfAdslPresence = _ZhoneVdslLineConfAdslPresence_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 29),
    _ZhoneVdslLineConfAdslPresence_Type()
)
zhoneVdslLineConfAdslPresence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfAdslPresence.setStatus("current")


class _ZhoneVdslLineConfApplicableStandard_Type(Integer32):
    """Custom type zhoneVdslLineConfApplicableStandard based on Integer32"""
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
        *(("ansi", 1),
          ("etsi", 2),
          ("itu", 3),
          ("other", 4))
    )


_ZhoneVdslLineConfApplicableStandard_Type.__name__ = "Integer32"
_ZhoneVdslLineConfApplicableStandard_Object = MibTableColumn
zhoneVdslLineConfApplicableStandard = _ZhoneVdslLineConfApplicableStandard_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 30),
    _ZhoneVdslLineConfApplicableStandard_Type()
)
zhoneVdslLineConfApplicableStandard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfApplicableStandard.setStatus("current")


class _ZhoneVdslLineConfBandPlan_Type(Integer32):
    """Custom type zhoneVdslLineConfBandPlan based on Integer32"""
    defaultValue = 2

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
              15)
        )
    )
    namedValues = NamedValues(
        *(("bandPlan997", 1),
          ("bandPlan997-2", 5),
          ("bandPlan997-3", 6),
          ("bandPlan998", 2),
          ("bandPlan998-17-6", 9),
          ("bandPlan998-2", 7),
          ("bandPlan998-3", 8),
          ("bandPlanFx", 3),
          ("china-a-2", 12),
          ("china-a-3", 13),
          ("china-b-2", 14),
          ("china-b-3", 15),
          ("fx-2", 10),
          ("fx-3", 11),
          ("other", 4))
    )


_ZhoneVdslLineConfBandPlan_Type.__name__ = "Integer32"
_ZhoneVdslLineConfBandPlan_Object = MibTableColumn
zhoneVdslLineConfBandPlan = _ZhoneVdslLineConfBandPlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 31),
    _ZhoneVdslLineConfBandPlan_Type()
)
zhoneVdslLineConfBandPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfBandPlan.setStatus("current")


class _ZhoneVdslLineConfBandPlanFx_Type(Unsigned32):
    """Custom type zhoneVdslLineConfBandPlanFx based on Unsigned32"""
    defaultValue = 3750

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3750, 12000),
    )


_ZhoneVdslLineConfBandPlanFx_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfBandPlanFx_Object = MibTableColumn
zhoneVdslLineConfBandPlanFx = _ZhoneVdslLineConfBandPlanFx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 32),
    _ZhoneVdslLineConfBandPlanFx_Type()
)
zhoneVdslLineConfBandPlanFx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfBandPlanFx.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfBandPlanFx.setUnits("kHz")


class _ZhoneVdslLineConfBandOptUsage_Type(Integer32):
    """Custom type zhoneVdslLineConfBandOptUsage based on Integer32"""
    defaultValue = 2

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
        *(("downstream", 3),
          ("unused", 1),
          ("upstream", 2),
          ("upstream-forced", 4))
    )


_ZhoneVdslLineConfBandOptUsage_Type.__name__ = "Integer32"
_ZhoneVdslLineConfBandOptUsage_Object = MibTableColumn
zhoneVdslLineConfBandOptUsage = _ZhoneVdslLineConfBandOptUsage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 33),
    _ZhoneVdslLineConfBandOptUsage_Type()
)
zhoneVdslLineConfBandOptUsage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfBandOptUsage.setStatus("current")


class _ZhoneVdslLineConfUpPsdTemplate_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPsdTemplate based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ansi-fftcab-m1", 5),
          ("ansi-fftex-m1", 3),
          ("ansi-fftex-m2", 4),
          ("etsi-m1", 7),
          ("etsi-m2", 8),
          ("fftcab-m2", 6),
          ("psd-custom", 9))
    )


_ZhoneVdslLineConfUpPsdTemplate_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPsdTemplate_Object = MibTableColumn
zhoneVdslLineConfUpPsdTemplate = _ZhoneVdslLineConfUpPsdTemplate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 34),
    _ZhoneVdslLineConfUpPsdTemplate_Type()
)
zhoneVdslLineConfUpPsdTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPsdTemplate.setStatus("current")


class _ZhoneVdslLineConfDownPsdTemplate_Type(Integer32):
    """Custom type zhoneVdslLineConfDownPsdTemplate based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("ansi-fftcab-m1", 5),
          ("ansi-fftex-m1", 3),
          ("ansi-fftex-m2", 4),
          ("etsi-pcab-m1", 20),
          ("etsi-pcab-m2", 21),
          ("etsi-pexm2-sample1", 16),
          ("etsi-pexm2-sample2", 17),
          ("etsi-pexm2-sample3", 18),
          ("etsi-pexm2-sample4", 19),
          ("etsi-pexp1-m1", 11),
          ("etsi-pexp1-m2", 12),
          ("etsi-pexp2-m1", 13),
          ("etsi-pexp2-m2", 14),
          ("fftcab-m1-adsl", 7),
          ("fftcab-m1-adslplus", 8),
          ("fftcab-m2", 6),
          ("fftcab-m2-adsl", 9),
          ("fftcab-m2-adslplus", 10),
          ("psd-custom", 15))
    )


_ZhoneVdslLineConfDownPsdTemplate_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownPsdTemplate_Object = MibTableColumn
zhoneVdslLineConfDownPsdTemplate = _ZhoneVdslLineConfDownPsdTemplate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 35),
    _ZhoneVdslLineConfDownPsdTemplate_Type()
)
zhoneVdslLineConfDownPsdTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownPsdTemplate.setStatus("current")


class _ZhoneVdslLineConfHamBandMask_Type(Bits):
    """Custom type zhoneVdslLineConfHamBandMask based on Bits"""
    namedValues = NamedValues(
        *(("amateurBand160m", 5),
          ("amateurBand30m", 2),
          ("amateurBand40m", 3),
          ("amateurBand80m", 4),
          ("customNotch1", 0),
          ("customNotch2", 1))
    )

_ZhoneVdslLineConfHamBandMask_Type.__name__ = "Bits"
_ZhoneVdslLineConfHamBandMask_Object = MibTableColumn
zhoneVdslLineConfHamBandMask = _ZhoneVdslLineConfHamBandMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 36),
    _ZhoneVdslLineConfHamBandMask_Type()
)
zhoneVdslLineConfHamBandMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfHamBandMask.setStatus("current")


class _ZhoneVdslLineConfCustomNotch1Start_Type(Unsigned32):
    """Custom type zhoneVdslLineConfCustomNotch1Start based on Unsigned32"""
    defaultValue = 0


_ZhoneVdslLineConfCustomNotch1Start_Object = MibTableColumn
zhoneVdslLineConfCustomNotch1Start = _ZhoneVdslLineConfCustomNotch1Start_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 37),
    _ZhoneVdslLineConfCustomNotch1Start_Type()
)
zhoneVdslLineConfCustomNotch1Start.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfCustomNotch1Start.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfCustomNotch1Start.setUnits("kHz")


class _ZhoneVdslLineConfCustomNotch1Stop_Type(Unsigned32):
    """Custom type zhoneVdslLineConfCustomNotch1Stop based on Unsigned32"""
    defaultValue = 0


_ZhoneVdslLineConfCustomNotch1Stop_Object = MibTableColumn
zhoneVdslLineConfCustomNotch1Stop = _ZhoneVdslLineConfCustomNotch1Stop_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 38),
    _ZhoneVdslLineConfCustomNotch1Stop_Type()
)
zhoneVdslLineConfCustomNotch1Stop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfCustomNotch1Stop.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfCustomNotch1Stop.setUnits("kHz")


class _ZhoneVdslLineConfCustomNotch2Start_Type(Unsigned32):
    """Custom type zhoneVdslLineConfCustomNotch2Start based on Unsigned32"""
    defaultValue = 0


_ZhoneVdslLineConfCustomNotch2Start_Object = MibTableColumn
zhoneVdslLineConfCustomNotch2Start = _ZhoneVdslLineConfCustomNotch2Start_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 39),
    _ZhoneVdslLineConfCustomNotch2Start_Type()
)
zhoneVdslLineConfCustomNotch2Start.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfCustomNotch2Start.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfCustomNotch2Start.setUnits("kHz")


class _ZhoneVdslLineConfCustomNotch2Stop_Type(Unsigned32):
    """Custom type zhoneVdslLineConfCustomNotch2Stop based on Unsigned32"""
    defaultValue = 0


_ZhoneVdslLineConfCustomNotch2Stop_Object = MibTableColumn
zhoneVdslLineConfCustomNotch2Stop = _ZhoneVdslLineConfCustomNotch2Stop_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 40),
    _ZhoneVdslLineConfCustomNotch2Stop_Type()
)
zhoneVdslLineConfCustomNotch2Stop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfCustomNotch2Stop.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfCustomNotch2Stop.setUnits("kHz")


class _ZhoneVdslLineConfDownTargetSlowBurst_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownTargetSlowBurst based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1275),
    )


_ZhoneVdslLineConfDownTargetSlowBurst_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownTargetSlowBurst_Object = MibTableColumn
zhoneVdslLineConfDownTargetSlowBurst = _ZhoneVdslLineConfDownTargetSlowBurst_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 41),
    _ZhoneVdslLineConfDownTargetSlowBurst_Type()
)
zhoneVdslLineConfDownTargetSlowBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownTargetSlowBurst.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownTargetSlowBurst.setUnits("microseconds")


class _ZhoneVdslLineConfUpTargetSlowBurst_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpTargetSlowBurst based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1275),
    )


_ZhoneVdslLineConfUpTargetSlowBurst_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpTargetSlowBurst_Object = MibTableColumn
zhoneVdslLineConfUpTargetSlowBurst = _ZhoneVdslLineConfUpTargetSlowBurst_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 42),
    _ZhoneVdslLineConfUpTargetSlowBurst_Type()
)
zhoneVdslLineConfUpTargetSlowBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpTargetSlowBurst.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpTargetSlowBurst.setUnits("microseconds")


class _ZhoneVdslLineConfDownMaxFastFec_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownMaxFastFec based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_ZhoneVdslLineConfDownMaxFastFec_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownMaxFastFec_Object = MibTableColumn
zhoneVdslLineConfDownMaxFastFec = _ZhoneVdslLineConfDownMaxFastFec_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 43),
    _ZhoneVdslLineConfDownMaxFastFec_Type()
)
zhoneVdslLineConfDownMaxFastFec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxFastFec.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxFastFec.setUnits("%")


class _ZhoneVdslLineConfUpMaxFastFec_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpMaxFastFec based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_ZhoneVdslLineConfUpMaxFastFec_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpMaxFastFec_Object = MibTableColumn
zhoneVdslLineConfUpMaxFastFec = _ZhoneVdslLineConfUpMaxFastFec_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 44),
    _ZhoneVdslLineConfUpMaxFastFec_Type()
)
zhoneVdslLineConfUpMaxFastFec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxFastFec.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxFastFec.setUnits("%")


class _ZhoneVdslLineConfLineType_Type(Integer32):
    """Custom type zhoneVdslLineConfLineType based on Integer32"""
    defaultValue = 2

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
        *(("fastAndInterleaved", 5),
          ("fastOnly", 2),
          ("fastOrInterleaved", 4),
          ("interleavedOnly", 3),
          ("noChannel", 1))
    )


_ZhoneVdslLineConfLineType_Type.__name__ = "Integer32"
_ZhoneVdslLineConfLineType_Object = MibTableColumn
zhoneVdslLineConfLineType = _ZhoneVdslLineConfLineType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 45),
    _ZhoneVdslLineConfLineType_Type()
)
zhoneVdslLineConfLineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfLineType.setStatus("current")
_ZhoneVdslLineConfProfRowStatus_Type = RowStatus
_ZhoneVdslLineConfProfRowStatus_Object = MibTableColumn
zhoneVdslLineConfProfRowStatus = _ZhoneVdslLineConfProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 47),
    _ZhoneVdslLineConfProfRowStatus_Type()
)
zhoneVdslLineConfProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfProfRowStatus.setStatus("current")


class _ZhoneVdslLineConfTransmissionMode_Type(Integer32):
    """Custom type zhoneVdslLineConfTransmissionMode based on Integer32"""
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
        *(("adsl2Mode", 5),
          ("adsl2PlusMode", 4),
          ("autoNegotiateMode", 1),
          ("gdmtMode", 6),
          ("vdsl2Mode", 3),
          ("vdslMode", 2))
    )


_ZhoneVdslLineConfTransmissionMode_Type.__name__ = "Integer32"
_ZhoneVdslLineConfTransmissionMode_Object = MibTableColumn
zhoneVdslLineConfTransmissionMode = _ZhoneVdslLineConfTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 48),
    _ZhoneVdslLineConfTransmissionMode_Type()
)
zhoneVdslLineConfTransmissionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfTransmissionMode.setStatus("current")


class _ZhoneVdslLineConfVdsl2Profile_Type(Integer32):
    """Custom type zhoneVdslLineConfVdsl2Profile based on Integer32"""
    defaultValue = 5

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
        *(("g993-2-12a", 5),
          ("g993-2-12b", 6),
          ("g993-2-17a", 7),
          ("g993-2-30a", 8),
          ("g993-2-8a", 1),
          ("g993-2-8b", 2),
          ("g993-2-8c", 3),
          ("g993-2-8d", 4))
    )


_ZhoneVdslLineConfVdsl2Profile_Type.__name__ = "Integer32"
_ZhoneVdslLineConfVdsl2Profile_Object = MibTableColumn
zhoneVdslLineConfVdsl2Profile = _ZhoneVdslLineConfVdsl2Profile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 49),
    _ZhoneVdslLineConfVdsl2Profile_Type()
)
zhoneVdslLineConfVdsl2Profile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfVdsl2Profile.setStatus("current")


class _ZhoneVdslLineConfVdslMode_Type(Integer32):
    """Custom type zhoneVdslLineConfVdslMode based on Integer32"""
    defaultValue = 1

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
        *(("long-reach-8k", 2),
          ("lr-8k", 5),
          ("r8k", 3),
          ("standard", 1),
          ("std-8k", 4),
          ("std-lr", 6),
          ("std-lr-8k", 7))
    )


_ZhoneVdslLineConfVdslMode_Type.__name__ = "Integer32"
_ZhoneVdslLineConfVdslMode_Object = MibTableColumn
zhoneVdslLineConfVdslMode = _ZhoneVdslLineConfVdslMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 50),
    _ZhoneVdslLineConfVdslMode_Type()
)
zhoneVdslLineConfVdslMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfVdslMode.setStatus("current")


class _ZhoneVdslLineConfPboElectricalOverride_Type(Integer32):
    """Custom type zhoneVdslLineConfPboElectricalOverride based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ZhoneVdslLineConfPboElectricalOverride_Type.__name__ = "Integer32"
_ZhoneVdslLineConfPboElectricalOverride_Object = MibTableColumn
zhoneVdslLineConfPboElectricalOverride = _ZhoneVdslLineConfPboElectricalOverride_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 51),
    _ZhoneVdslLineConfPboElectricalOverride_Type()
)
zhoneVdslLineConfPboElectricalOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfPboElectricalOverride.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfPboElectricalOverride.setUnits(".5 dBm/Mhz")


class _ZhoneVdslLineConfAutoModeCrtrn_Type(Integer32):
    """Custom type zhoneVdslLineConfAutoModeCrtrn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crtrn-chip-prop", 1),
          ("optimize-ds", 3),
          ("optimize-us", 2))
    )


_ZhoneVdslLineConfAutoModeCrtrn_Type.__name__ = "Integer32"
_ZhoneVdslLineConfAutoModeCrtrn_Object = MibTableColumn
zhoneVdslLineConfAutoModeCrtrn = _ZhoneVdslLineConfAutoModeCrtrn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 52),
    _ZhoneVdslLineConfAutoModeCrtrn_Type()
)
zhoneVdslLineConfAutoModeCrtrn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfAutoModeCrtrn.setStatus("current")


class _ZhoneVdslLineConfNetworkTimingRef_Type(Integer32):
    """Custom type zhoneVdslLineConfNetworkTimingRef based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfNetworkTimingRef_Type.__name__ = "Integer32"
_ZhoneVdslLineConfNetworkTimingRef_Object = MibTableColumn
zhoneVdslLineConfNetworkTimingRef = _ZhoneVdslLineConfNetworkTimingRef_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 53),
    _ZhoneVdslLineConfNetworkTimingRef_Type()
)
zhoneVdslLineConfNetworkTimingRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslLineConfNetworkTimingRef.setStatus("current")


class _ZhoneVdslLineConfAdslBandMode_Type(Integer32):
    """Custom type zhoneVdslLineConfAdslBandMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("not-allowed", 2))
    )


_ZhoneVdslLineConfAdslBandMode_Type.__name__ = "Integer32"
_ZhoneVdslLineConfAdslBandMode_Object = MibTableColumn
zhoneVdslLineConfAdslBandMode = _ZhoneVdslLineConfAdslBandMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 54),
    _ZhoneVdslLineConfAdslBandMode_Type()
)
zhoneVdslLineConfAdslBandMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfAdslBandMode.setStatus("current")


class _ZhoneVdslLineConfAdslBandModeEndFreq_Type(Integer32):
    """Custom type zhoneVdslLineConfAdslBandModeEndFreq based on Integer32"""
    defaultValue = 1104

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(276, 2208),
    )


_ZhoneVdslLineConfAdslBandModeEndFreq_Type.__name__ = "Integer32"
_ZhoneVdslLineConfAdslBandModeEndFreq_Object = MibTableColumn
zhoneVdslLineConfAdslBandModeEndFreq = _ZhoneVdslLineConfAdslBandModeEndFreq_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 55),
    _ZhoneVdslLineConfAdslBandModeEndFreq_Type()
)
zhoneVdslLineConfAdslBandModeEndFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfAdslBandModeEndFreq.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfAdslBandModeEndFreq.setUnits("kHz")


class _ZhoneVdslLineConfSeltEchoMeasurementTime_Type(Integer32):
    """Custom type zhoneVdslLineConfSeltEchoMeasurementTime based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 240),
    )


_ZhoneVdslLineConfSeltEchoMeasurementTime_Type.__name__ = "Integer32"
_ZhoneVdslLineConfSeltEchoMeasurementTime_Object = MibTableColumn
zhoneVdslLineConfSeltEchoMeasurementTime = _ZhoneVdslLineConfSeltEchoMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 56),
    _ZhoneVdslLineConfSeltEchoMeasurementTime_Type()
)
zhoneVdslLineConfSeltEchoMeasurementTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfSeltEchoMeasurementTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfSeltEchoMeasurementTime.setUnits("secs")


class _ZhoneVdslLineConfSeltNoiseMeasurementTime_Type(Integer32):
    """Custom type zhoneVdslLineConfSeltNoiseMeasurementTime based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 240),
    )


_ZhoneVdslLineConfSeltNoiseMeasurementTime_Type.__name__ = "Integer32"
_ZhoneVdslLineConfSeltNoiseMeasurementTime_Object = MibTableColumn
zhoneVdslLineConfSeltNoiseMeasurementTime = _ZhoneVdslLineConfSeltNoiseMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 57),
    _ZhoneVdslLineConfSeltNoiseMeasurementTime_Type()
)
zhoneVdslLineConfSeltNoiseMeasurementTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfSeltNoiseMeasurementTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfSeltNoiseMeasurementTime.setUnits("secs")


class _ZhoneVdslLineConfSeltAgc_Type(Integer32):
    """Custom type zhoneVdslLineConfSeltAgc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_ZhoneVdslLineConfSeltAgc_Type.__name__ = "Integer32"
_ZhoneVdslLineConfSeltAgc_Object = MibTableColumn
zhoneVdslLineConfSeltAgc = _ZhoneVdslLineConfSeltAgc_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 58),
    _ZhoneVdslLineConfSeltAgc_Type()
)
zhoneVdslLineConfSeltAgc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfSeltAgc.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfSeltAgc.setUnits("1 dBm")


class _ZhoneVdslLineConfDownTrellis_Type(Integer32):
    """Custom type zhoneVdslLineConfDownTrellis based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfDownTrellis_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownTrellis_Object = MibTableColumn
zhoneVdslLineConfDownTrellis = _ZhoneVdslLineConfDownTrellis_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 59),
    _ZhoneVdslLineConfDownTrellis_Type()
)
zhoneVdslLineConfDownTrellis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownTrellis.setStatus("current")


class _ZhoneVdslLineConfUpTrellis_Type(Integer32):
    """Custom type zhoneVdslLineConfUpTrellis based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfUpTrellis_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpTrellis_Object = MibTableColumn
zhoneVdslLineConfUpTrellis = _ZhoneVdslLineConfUpTrellis_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 60),
    _ZhoneVdslLineConfUpTrellis_Type()
)
zhoneVdslLineConfUpTrellis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpTrellis.setStatus("current")


class _ZhoneVdslLineConfDownMaxAggregateTxPwr_Type(Integer32):
    """Custom type zhoneVdslLineConfDownMaxAggregateTxPwr based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("unlimited", 4)
    )


_ZhoneVdslLineConfDownMaxAggregateTxPwr_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownMaxAggregateTxPwr_Object = MibTableColumn
zhoneVdslLineConfDownMaxAggregateTxPwr = _ZhoneVdslLineConfDownMaxAggregateTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 61),
    _ZhoneVdslLineConfDownMaxAggregateTxPwr_Type()
)
zhoneVdslLineConfDownMaxAggregateTxPwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxAggregateTxPwr.setStatus("current")


class _ZhoneVdslLineConfUpMaxAggregateTxPwr_Type(Integer32):
    """Custom type zhoneVdslLineConfUpMaxAggregateTxPwr based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("unlimited", 4)
    )


_ZhoneVdslLineConfUpMaxAggregateTxPwr_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpMaxAggregateTxPwr_Object = MibTableColumn
zhoneVdslLineConfUpMaxAggregateTxPwr = _ZhoneVdslLineConfUpMaxAggregateTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 62),
    _ZhoneVdslLineConfUpMaxAggregateTxPwr_Type()
)
zhoneVdslLineConfUpMaxAggregateTxPwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxAggregateTxPwr.setStatus("current")


class _ZhoneVdslLineConfDownMaxPsd_Type(Integer32):
    """Custom type zhoneVdslLineConfDownMaxPsd based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-955, 0),
    )


_ZhoneVdslLineConfDownMaxPsd_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownMaxPsd_Object = MibTableColumn
zhoneVdslLineConfDownMaxPsd = _ZhoneVdslLineConfDownMaxPsd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 63),
    _ZhoneVdslLineConfDownMaxPsd_Type()
)
zhoneVdslLineConfDownMaxPsd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxPsd.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxPsd.setUnits(".1 dBm/Hz")


class _ZhoneVdslLineConfUpMaxPsd_Type(Integer32):
    """Custom type zhoneVdslLineConfUpMaxPsd based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-955, 0),
    )


_ZhoneVdslLineConfUpMaxPsd_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpMaxPsd_Object = MibTableColumn
zhoneVdslLineConfUpMaxPsd = _ZhoneVdslLineConfUpMaxPsd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 64),
    _ZhoneVdslLineConfUpMaxPsd_Type()
)
zhoneVdslLineConfUpMaxPsd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxPsd.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxPsd.setUnits(".1 dBm/Hz")


class _ZhoneVdslLineConfDownPsdShape_Type(Integer32):
    """Custom type zhoneVdslLineConfDownPsdShape based on Integer32"""
    defaultValue = 2

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
        *(("custom-psd", 1),
          ("region-a-psd", 2),
          ("region-b-m1-a-psd", 4),
          ("region-b-m1-b-psd", 5),
          ("region-b-m1-us0-psd", 6),
          ("region-b-m2-a-psd", 7),
          ("region-b-m2-b-psd", 9),
          ("region-b-m2-m-psd", 8),
          ("region-b-m2-us0-psd", 10),
          ("region-c-psd", 3))
    )


_ZhoneVdslLineConfDownPsdShape_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownPsdShape_Object = MibTableColumn
zhoneVdslLineConfDownPsdShape = _ZhoneVdslLineConfDownPsdShape_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 65),
    _ZhoneVdslLineConfDownPsdShape_Type()
)
zhoneVdslLineConfDownPsdShape.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownPsdShape.setStatus("current")


class _ZhoneVdslLineConfUpPsdShape_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPsdShape based on Integer32"""
    defaultValue = 2

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
        *(("custom-psd", 1),
          ("region-a-psd", 2),
          ("region-b-m1-a-psd", 4),
          ("region-b-m1-b-psd", 5),
          ("region-b-m1-us0-psd", 6),
          ("region-b-m2-a-psd", 7),
          ("region-b-m2-b-psd", 9),
          ("region-b-m2-m-psd", 8),
          ("region-b-m2-us0-psd", 10),
          ("region-c-psd", 3))
    )


_ZhoneVdslLineConfUpPsdShape_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPsdShape_Object = MibTableColumn
zhoneVdslLineConfUpPsdShape = _ZhoneVdslLineConfUpPsdShape_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 66),
    _ZhoneVdslLineConfUpPsdShape_Type()
)
zhoneVdslLineConfUpPsdShape.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPsdShape.setStatus("current")


class _ZhoneVdslLineConfDownVirtualNoiseSnrMode_Type(Integer32):
    """Custom type zhoneVdslLineConfDownVirtualNoiseSnrMode based on Integer32"""
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
        *(("mode1", 1),
          ("mode2", 2),
          ("mode3", 3))
    )


_ZhoneVdslLineConfDownVirtualNoiseSnrMode_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownVirtualNoiseSnrMode_Object = MibTableColumn
zhoneVdslLineConfDownVirtualNoiseSnrMode = _ZhoneVdslLineConfDownVirtualNoiseSnrMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 67),
    _ZhoneVdslLineConfDownVirtualNoiseSnrMode_Type()
)
zhoneVdslLineConfDownVirtualNoiseSnrMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownVirtualNoiseSnrMode.setStatus("current")


class _ZhoneVdslLineConfUpVirtualNoiseSnrMode_Type(Integer32):
    """Custom type zhoneVdslLineConfUpVirtualNoiseSnrMode based on Integer32"""
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
        *(("mode1", 1),
          ("mode2", 2),
          ("mode3", 3))
    )


_ZhoneVdslLineConfUpVirtualNoiseSnrMode_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpVirtualNoiseSnrMode_Object = MibTableColumn
zhoneVdslLineConfUpVirtualNoiseSnrMode = _ZhoneVdslLineConfUpVirtualNoiseSnrMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 68),
    _ZhoneVdslLineConfUpVirtualNoiseSnrMode_Type()
)
zhoneVdslLineConfUpVirtualNoiseSnrMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpVirtualNoiseSnrMode.setStatus("current")


class _ZhoneVdslLineConfDownErasureDetectionFast_Type(Integer32):
    """Custom type zhoneVdslLineConfDownErasureDetectionFast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfDownErasureDetectionFast_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownErasureDetectionFast_Object = MibTableColumn
zhoneVdslLineConfDownErasureDetectionFast = _ZhoneVdslLineConfDownErasureDetectionFast_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 69),
    _ZhoneVdslLineConfDownErasureDetectionFast_Type()
)
zhoneVdslLineConfDownErasureDetectionFast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownErasureDetectionFast.setStatus("current")


class _ZhoneVdslLineConfUpErasureDetectionFast_Type(Integer32):
    """Custom type zhoneVdslLineConfUpErasureDetectionFast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfUpErasureDetectionFast_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpErasureDetectionFast_Object = MibTableColumn
zhoneVdslLineConfUpErasureDetectionFast = _ZhoneVdslLineConfUpErasureDetectionFast_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 70),
    _ZhoneVdslLineConfUpErasureDetectionFast_Type()
)
zhoneVdslLineConfUpErasureDetectionFast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpErasureDetectionFast.setStatus("current")


class _ZhoneVdslLineConfDownErasureDetectionInterleave_Type(Integer32):
    """Custom type zhoneVdslLineConfDownErasureDetectionInterleave based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfDownErasureDetectionInterleave_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownErasureDetectionInterleave_Object = MibTableColumn
zhoneVdslLineConfDownErasureDetectionInterleave = _ZhoneVdslLineConfDownErasureDetectionInterleave_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 71),
    _ZhoneVdslLineConfDownErasureDetectionInterleave_Type()
)
zhoneVdslLineConfDownErasureDetectionInterleave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownErasureDetectionInterleave.setStatus("current")


class _ZhoneVdslLineConfUpErasureDetectionInterleave_Type(Integer32):
    """Custom type zhoneVdslLineConfUpErasureDetectionInterleave based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfUpErasureDetectionInterleave_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpErasureDetectionInterleave_Object = MibTableColumn
zhoneVdslLineConfUpErasureDetectionInterleave = _ZhoneVdslLineConfUpErasureDetectionInterleave_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 72),
    _ZhoneVdslLineConfUpErasureDetectionInterleave_Type()
)
zhoneVdslLineConfUpErasureDetectionInterleave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpErasureDetectionInterleave.setStatus("current")


class _ZhoneVdslLineConfDownGhsA43TonePwr_Type(Integer32):
    """Custom type zhoneVdslLineConfDownGhsA43TonePwr based on Integer32"""
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
        *(("auto", 2),
          ("default", 1),
          ("manual", 3))
    )


_ZhoneVdslLineConfDownGhsA43TonePwr_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownGhsA43TonePwr_Object = MibTableColumn
zhoneVdslLineConfDownGhsA43TonePwr = _ZhoneVdslLineConfDownGhsA43TonePwr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 73),
    _ZhoneVdslLineConfDownGhsA43TonePwr_Type()
)
zhoneVdslLineConfDownGhsA43TonePwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGhsA43TonePwr.setStatus("current")


class _ZhoneVdslLineConfDownGhsB43TonePwr_Type(Integer32):
    """Custom type zhoneVdslLineConfDownGhsB43TonePwr based on Integer32"""
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
        *(("auto", 2),
          ("default", 1),
          ("manual", 3))
    )


_ZhoneVdslLineConfDownGhsB43TonePwr_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownGhsB43TonePwr_Object = MibTableColumn
zhoneVdslLineConfDownGhsB43TonePwr = _ZhoneVdslLineConfDownGhsB43TonePwr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 74),
    _ZhoneVdslLineConfDownGhsB43TonePwr_Type()
)
zhoneVdslLineConfDownGhsB43TonePwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGhsB43TonePwr.setStatus("current")


class _ZhoneVdslLineConfDownGhsA43cTonePwr_Type(Integer32):
    """Custom type zhoneVdslLineConfDownGhsA43cTonePwr based on Integer32"""
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
        *(("auto", 2),
          ("default", 1),
          ("manual", 3))
    )


_ZhoneVdslLineConfDownGhsA43cTonePwr_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownGhsA43cTonePwr_Object = MibTableColumn
zhoneVdslLineConfDownGhsA43cTonePwr = _ZhoneVdslLineConfDownGhsA43cTonePwr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 75),
    _ZhoneVdslLineConfDownGhsA43cTonePwr_Type()
)
zhoneVdslLineConfDownGhsA43cTonePwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGhsA43cTonePwr.setStatus("current")


class _ZhoneVdslLineConfDownGhsV43TonePwr_Type(Integer32):
    """Custom type zhoneVdslLineConfDownGhsV43TonePwr based on Integer32"""
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
        *(("auto", 2),
          ("default", 1),
          ("manual", 3))
    )


_ZhoneVdslLineConfDownGhsV43TonePwr_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownGhsV43TonePwr_Object = MibTableColumn
zhoneVdslLineConfDownGhsV43TonePwr = _ZhoneVdslLineConfDownGhsV43TonePwr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 76),
    _ZhoneVdslLineConfDownGhsV43TonePwr_Type()
)
zhoneVdslLineConfDownGhsV43TonePwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGhsV43TonePwr.setStatus("current")


class _ZhoneVdslLineConfDownGhsA43TonePwrMaxLvl_Type(Integer32):
    """Custom type zhoneVdslLineConfDownGhsA43TonePwrMaxLvl based on Integer32"""
    defaultValue = -99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -40),
    )


_ZhoneVdslLineConfDownGhsA43TonePwrMaxLvl_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownGhsA43TonePwrMaxLvl_Object = MibTableColumn
zhoneVdslLineConfDownGhsA43TonePwrMaxLvl = _ZhoneVdslLineConfDownGhsA43TonePwrMaxLvl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 77),
    _ZhoneVdslLineConfDownGhsA43TonePwrMaxLvl_Type()
)
zhoneVdslLineConfDownGhsA43TonePwrMaxLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGhsA43TonePwrMaxLvl.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGhsA43TonePwrMaxLvl.setUnits("0.5 dBm/Hz")


class _ZhoneVdslLineConfDownGhsB43TonePwrMaxLvl_Type(Integer32):
    """Custom type zhoneVdslLineConfDownGhsB43TonePwrMaxLvl based on Integer32"""
    defaultValue = -99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -40),
    )


_ZhoneVdslLineConfDownGhsB43TonePwrMaxLvl_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownGhsB43TonePwrMaxLvl_Object = MibTableColumn
zhoneVdslLineConfDownGhsB43TonePwrMaxLvl = _ZhoneVdslLineConfDownGhsB43TonePwrMaxLvl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 78),
    _ZhoneVdslLineConfDownGhsB43TonePwrMaxLvl_Type()
)
zhoneVdslLineConfDownGhsB43TonePwrMaxLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGhsB43TonePwrMaxLvl.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGhsB43TonePwrMaxLvl.setUnits("0.5 dBm/Hz")


class _ZhoneVdslLineConfDownGhsA43cTonePwrMaxLvl_Type(Integer32):
    """Custom type zhoneVdslLineConfDownGhsA43cTonePwrMaxLvl based on Integer32"""
    defaultValue = -99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -40),
    )


_ZhoneVdslLineConfDownGhsA43cTonePwrMaxLvl_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownGhsA43cTonePwrMaxLvl_Object = MibTableColumn
zhoneVdslLineConfDownGhsA43cTonePwrMaxLvl = _ZhoneVdslLineConfDownGhsA43cTonePwrMaxLvl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 79),
    _ZhoneVdslLineConfDownGhsA43cTonePwrMaxLvl_Type()
)
zhoneVdslLineConfDownGhsA43cTonePwrMaxLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGhsA43cTonePwrMaxLvl.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGhsA43cTonePwrMaxLvl.setUnits("0.5 dBm/Hz")


class _ZhoneVdslLineConfDownGhsV43TonePwrMaxLvl_Type(Integer32):
    """Custom type zhoneVdslLineConfDownGhsV43TonePwrMaxLvl based on Integer32"""
    defaultValue = -99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -40),
    )


_ZhoneVdslLineConfDownGhsV43TonePwrMaxLvl_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownGhsV43TonePwrMaxLvl_Object = MibTableColumn
zhoneVdslLineConfDownGhsV43TonePwrMaxLvl = _ZhoneVdslLineConfDownGhsV43TonePwrMaxLvl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 80),
    _ZhoneVdslLineConfDownGhsV43TonePwrMaxLvl_Type()
)
zhoneVdslLineConfDownGhsV43TonePwrMaxLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGhsV43TonePwrMaxLvl.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGhsV43TonePwrMaxLvl.setUnits("0.5 dBm/Hz")


class _ZhoneVdslLineConfDownRsCoding_Type(Integer32):
    """Custom type zhoneVdslLineConfDownRsCoding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfDownRsCoding_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownRsCoding_Object = MibTableColumn
zhoneVdslLineConfDownRsCoding = _ZhoneVdslLineConfDownRsCoding_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 81),
    _ZhoneVdslLineConfDownRsCoding_Type()
)
zhoneVdslLineConfDownRsCoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownRsCoding.setStatus("current")


class _ZhoneVdslLineConfUpRsCoding_Type(Integer32):
    """Custom type zhoneVdslLineConfUpRsCoding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfUpRsCoding_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpRsCoding_Object = MibTableColumn
zhoneVdslLineConfUpRsCoding = _ZhoneVdslLineConfUpRsCoding_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 82),
    _ZhoneVdslLineConfUpRsCoding_Type()
)
zhoneVdslLineConfUpRsCoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpRsCoding.setStatus("current")


class _ZhoneVdslLineConfUpPboPsdTemplate_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPboPsdTemplate based on Integer32"""
    defaultValue = 1

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
        *(("ab-param", 10),
          ("ansi-a", 1),
          ("ansi-f", 2),
          ("custom", 9),
          ("etsi-a", 3),
          ("etsi-b", 4),
          ("etsi-c", 5),
          ("etsi-d", 6),
          ("etsi-e", 7),
          ("etsi-f", 8))
    )


_ZhoneVdslLineConfUpPboPsdTemplate_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPboPsdTemplate_Object = MibTableColumn
zhoneVdslLineConfUpPboPsdTemplate = _ZhoneVdslLineConfUpPboPsdTemplate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 83),
    _ZhoneVdslLineConfUpPboPsdTemplate_Type()
)
zhoneVdslLineConfUpPboPsdTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdTemplate.setStatus("current")


class _ZhoneVdslLineConfUpPboPsdParamA1_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPboPsdParamA1 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 8589),
    )


_ZhoneVdslLineConfUpPboPsdParamA1_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPboPsdParamA1_Object = MibTableColumn
zhoneVdslLineConfUpPboPsdParamA1 = _ZhoneVdslLineConfUpPboPsdParamA1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 84),
    _ZhoneVdslLineConfUpPboPsdParamA1_Type()
)
zhoneVdslLineConfUpPboPsdParamA1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamA1.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamA1.setUnits(".01 dBm/Hz")


class _ZhoneVdslLineConfUpPboPsdParamA2_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPboPsdParamA2 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 8589),
    )


_ZhoneVdslLineConfUpPboPsdParamA2_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPboPsdParamA2_Object = MibTableColumn
zhoneVdslLineConfUpPboPsdParamA2 = _ZhoneVdslLineConfUpPboPsdParamA2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 85),
    _ZhoneVdslLineConfUpPboPsdParamA2_Type()
)
zhoneVdslLineConfUpPboPsdParamA2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamA2.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamA2.setUnits(".01 dBm/Hz")


class _ZhoneVdslLineConfUpPboPsdParamB1_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPboPsdParamB1 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8589),
    )


_ZhoneVdslLineConfUpPboPsdParamB1_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPboPsdParamB1_Object = MibTableColumn
zhoneVdslLineConfUpPboPsdParamB1 = _ZhoneVdslLineConfUpPboPsdParamB1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 86),
    _ZhoneVdslLineConfUpPboPsdParamB1_Type()
)
zhoneVdslLineConfUpPboPsdParamB1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamB1.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamB1.setUnits(".01 dBm/Hz")


class _ZhoneVdslLineConfUpPboPsdParamB2_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPboPsdParamB2 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8589),
    )


_ZhoneVdslLineConfUpPboPsdParamB2_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPboPsdParamB2_Object = MibTableColumn
zhoneVdslLineConfUpPboPsdParamB2 = _ZhoneVdslLineConfUpPboPsdParamB2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 87),
    _ZhoneVdslLineConfUpPboPsdParamB2_Type()
)
zhoneVdslLineConfUpPboPsdParamB2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamB2.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamB2.setUnits(".01 dBm/Hz")


class _ZhoneVdslLineConfDownDownshiftSnrMgn_Type(Integer32):
    """Custom type zhoneVdslLineConfDownDownshiftSnrMgn based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_ZhoneVdslLineConfDownDownshiftSnrMgn_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownDownshiftSnrMgn_Object = MibTableColumn
zhoneVdslLineConfDownDownshiftSnrMgn = _ZhoneVdslLineConfDownDownshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 88),
    _ZhoneVdslLineConfDownDownshiftSnrMgn_Type()
)
zhoneVdslLineConfDownDownshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownDownshiftSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownDownshiftSnrMgn.setUnits("tenth dB")


class _ZhoneVdslLineConfDownUpshiftSnrMgn_Type(Integer32):
    """Custom type zhoneVdslLineConfDownUpshiftSnrMgn based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_ZhoneVdslLineConfDownUpshiftSnrMgn_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownUpshiftSnrMgn_Object = MibTableColumn
zhoneVdslLineConfDownUpshiftSnrMgn = _ZhoneVdslLineConfDownUpshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 89),
    _ZhoneVdslLineConfDownUpshiftSnrMgn_Type()
)
zhoneVdslLineConfDownUpshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownUpshiftSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownUpshiftSnrMgn.setUnits("tenth dB")


class _ZhoneVdslLineConfDownMinDownshiftTime_Type(Integer32):
    """Custom type zhoneVdslLineConfDownMinDownshiftTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ZhoneVdslLineConfDownMinDownshiftTime_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownMinDownshiftTime_Object = MibTableColumn
zhoneVdslLineConfDownMinDownshiftTime = _ZhoneVdslLineConfDownMinDownshiftTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 90),
    _ZhoneVdslLineConfDownMinDownshiftTime_Type()
)
zhoneVdslLineConfDownMinDownshiftTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMinDownshiftTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMinDownshiftTime.setUnits("seconds")


class _ZhoneVdslLineConfDownMinUpshiftTime_Type(Integer32):
    """Custom type zhoneVdslLineConfDownMinUpshiftTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ZhoneVdslLineConfDownMinUpshiftTime_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownMinUpshiftTime_Object = MibTableColumn
zhoneVdslLineConfDownMinUpshiftTime = _ZhoneVdslLineConfDownMinUpshiftTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 91),
    _ZhoneVdslLineConfDownMinUpshiftTime_Type()
)
zhoneVdslLineConfDownMinUpshiftTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMinUpshiftTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMinUpshiftTime.setUnits("seconds")


class _ZhoneVdslLineConfUpDownshiftSnrMgn_Type(Integer32):
    """Custom type zhoneVdslLineConfUpDownshiftSnrMgn based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_ZhoneVdslLineConfUpDownshiftSnrMgn_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpDownshiftSnrMgn_Object = MibTableColumn
zhoneVdslLineConfUpDownshiftSnrMgn = _ZhoneVdslLineConfUpDownshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 92),
    _ZhoneVdslLineConfUpDownshiftSnrMgn_Type()
)
zhoneVdslLineConfUpDownshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpDownshiftSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpDownshiftSnrMgn.setUnits("tenth dB")


class _ZhoneVdslLineConfUpUpshiftSnrMgn_Type(Integer32):
    """Custom type zhoneVdslLineConfUpUpshiftSnrMgn based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_ZhoneVdslLineConfUpUpshiftSnrMgn_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpUpshiftSnrMgn_Object = MibTableColumn
zhoneVdslLineConfUpUpshiftSnrMgn = _ZhoneVdslLineConfUpUpshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 93),
    _ZhoneVdslLineConfUpUpshiftSnrMgn_Type()
)
zhoneVdslLineConfUpUpshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpUpshiftSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpUpshiftSnrMgn.setUnits("tenth dB")


class _ZhoneVdslLineConfUpMinDownshiftTime_Type(Integer32):
    """Custom type zhoneVdslLineConfUpMinDownshiftTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ZhoneVdslLineConfUpMinDownshiftTime_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpMinDownshiftTime_Object = MibTableColumn
zhoneVdslLineConfUpMinDownshiftTime = _ZhoneVdslLineConfUpMinDownshiftTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 94),
    _ZhoneVdslLineConfUpMinDownshiftTime_Type()
)
zhoneVdslLineConfUpMinDownshiftTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMinDownshiftTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMinDownshiftTime.setUnits("seconds")


class _ZhoneVdslLineConfUpMinUpshiftTime_Type(Integer32):
    """Custom type zhoneVdslLineConfUpMinUpshiftTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_ZhoneVdslLineConfUpMinUpshiftTime_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpMinUpshiftTime_Object = MibTableColumn
zhoneVdslLineConfUpMinUpshiftTime = _ZhoneVdslLineConfUpMinUpshiftTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 95),
    _ZhoneVdslLineConfUpMinUpshiftTime_Type()
)
zhoneVdslLineConfUpMinUpshiftTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMinUpshiftTime.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMinUpshiftTime.setUnits("seconds")


class _ZhoneVdslLineConfDownMinTxThresholdAlarm_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownMinTxThresholdAlarm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ZhoneVdslLineConfDownMinTxThresholdAlarm_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownMinTxThresholdAlarm_Object = MibTableColumn
zhoneVdslLineConfDownMinTxThresholdAlarm = _ZhoneVdslLineConfDownMinTxThresholdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 96),
    _ZhoneVdslLineConfDownMinTxThresholdAlarm_Type()
)
zhoneVdslLineConfDownMinTxThresholdAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMinTxThresholdAlarm.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMinTxThresholdAlarm.setUnits("kbps")


class _ZhoneVdslLineConfUpMinTxThresholdAlarm_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpMinTxThresholdAlarm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ZhoneVdslLineConfUpMinTxThresholdAlarm_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpMinTxThresholdAlarm_Object = MibTableColumn
zhoneVdslLineConfUpMinTxThresholdAlarm = _ZhoneVdslLineConfUpMinTxThresholdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 97),
    _ZhoneVdslLineConfUpMinTxThresholdAlarm_Type()
)
zhoneVdslLineConfUpMinTxThresholdAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMinTxThresholdAlarm.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMinTxThresholdAlarm.setUnits("kbps")


class _ZhoneVdslLineConfPotsBypassRelayMaxDuration_Type(Integer32):
    """Custom type zhoneVdslLineConfPotsBypassRelayMaxDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_ZhoneVdslLineConfPotsBypassRelayMaxDuration_Type.__name__ = "Integer32"
_ZhoneVdslLineConfPotsBypassRelayMaxDuration_Object = MibTableColumn
zhoneVdslLineConfPotsBypassRelayMaxDuration = _ZhoneVdslLineConfPotsBypassRelayMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 98),
    _ZhoneVdslLineConfPotsBypassRelayMaxDuration_Type()
)
zhoneVdslLineConfPotsBypassRelayMaxDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfPotsBypassRelayMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfPotsBypassRelayMaxDuration.setUnits("secs")


class _ZhoneVdslLineConfDMTConfMode_Type(Integer32):
    """Custom type zhoneVdslLineConfDMTConfMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("echocancel", 1),
          ("freqdivmux", 2))
    )


_ZhoneVdslLineConfDMTConfMode_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDMTConfMode_Object = MibTableColumn
zhoneVdslLineConfDMTConfMode = _ZhoneVdslLineConfDMTConfMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 99),
    _ZhoneVdslLineConfDMTConfMode_Type()
)
zhoneVdslLineConfDMTConfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDMTConfMode.setStatus("current")


class _ZhoneVdslLineConfDownBitSwap_Type(Integer32):
    """Custom type zhoneVdslLineConfDownBitSwap based on Integer32"""
    defaultValue = 2

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


_ZhoneVdslLineConfDownBitSwap_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownBitSwap_Object = MibTableColumn
zhoneVdslLineConfDownBitSwap = _ZhoneVdslLineConfDownBitSwap_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 100),
    _ZhoneVdslLineConfDownBitSwap_Type()
)
zhoneVdslLineConfDownBitSwap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownBitSwap.setStatus("current")


class _ZhoneVdslLineConfUpBitSwap_Type(Integer32):
    """Custom type zhoneVdslLineConfUpBitSwap based on Integer32"""
    defaultValue = 2

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


_ZhoneVdslLineConfUpBitSwap_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpBitSwap_Object = MibTableColumn
zhoneVdslLineConfUpBitSwap = _ZhoneVdslLineConfUpBitSwap_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 101),
    _ZhoneVdslLineConfUpBitSwap_Type()
)
zhoneVdslLineConfUpBitSwap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpBitSwap.setStatus("current")


class _ZhoneVdslLineConfAdslAnnexMModeEnabled_Type(TruthValue):
    """Custom type zhoneVdslLineConfAdslAnnexMModeEnabled based on TruthValue"""


_ZhoneVdslLineConfAdslAnnexMModeEnabled_Object = MibTableColumn
zhoneVdslLineConfAdslAnnexMModeEnabled = _ZhoneVdslLineConfAdslAnnexMModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 102),
    _ZhoneVdslLineConfAdslAnnexMModeEnabled_Type()
)
zhoneVdslLineConfAdslAnnexMModeEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfAdslAnnexMModeEnabled.setStatus("current")


class _ZhoneVdslLineConfAdslAnnexMPsdMask_Type(Integer32):
    """Custom type zhoneVdslLineConfAdslAnnexMPsdMask based on Integer32"""
    defaultValue = 9

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
        *(("all", 10),
          ("eu32", 9),
          ("eu36", 8),
          ("eu40", 7),
          ("eu44", 6),
          ("eu48", 5),
          ("eu52", 4),
          ("eu56", 3),
          ("eu60", 2),
          ("eu64", 1))
    )


_ZhoneVdslLineConfAdslAnnexMPsdMask_Type.__name__ = "Integer32"
_ZhoneVdslLineConfAdslAnnexMPsdMask_Object = MibTableColumn
zhoneVdslLineConfAdslAnnexMPsdMask = _ZhoneVdslLineConfAdslAnnexMPsdMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 103),
    _ZhoneVdslLineConfAdslAnnexMPsdMask_Type()
)
zhoneVdslLineConfAdslAnnexMPsdMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfAdslAnnexMPsdMask.setStatus("current")


class _ZhoneVdslLineConfUs0BoundaryTone_Type(Integer32):
    """Custom type zhoneVdslLineConfUs0BoundaryTone based on Integer32"""
    defaultValue = 1

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
        *(("d32", 1),
          ("d36", 2),
          ("d40", 3),
          ("d44", 4),
          ("d48", 5),
          ("d52", 6),
          ("d56", 7),
          ("d64", 8))
    )


_ZhoneVdslLineConfUs0BoundaryTone_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUs0BoundaryTone_Object = MibTableColumn
zhoneVdslLineConfUs0BoundaryTone = _ZhoneVdslLineConfUs0BoundaryTone_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 104),
    _ZhoneVdslLineConfUs0BoundaryTone_Type()
)
zhoneVdslLineConfUs0BoundaryTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUs0BoundaryTone.setStatus("current")


class _ZhoneVdslLineConfDownInp_Type(Integer32):
    """Custom type zhoneVdslLineConfDownInp based on Integer32"""
    defaultValue = 4

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
              18)
        )
    )
    namedValues = NamedValues(
        *(("eightSymbols", 10),
          ("elevenSymbols", 13),
          ("fifteenSymbols", 17),
          ("fiveSymbols", 7),
          ("fourSymbols", 6),
          ("fourteenSymbols", 16),
          ("halfSymbol", 2),
          ("nineSymbols", 11),
          ("noProtection", 1),
          ("sevenSymbols", 9),
          ("singleSymbol", 3),
          ("sixSymbols", 8),
          ("sixteenSymbols", 18),
          ("tenSymbols", 12),
          ("thirteenSymbols", 15),
          ("threeSymbols", 5),
          ("twelveSymbols", 14),
          ("twoSymbols", 4))
    )


_ZhoneVdslLineConfDownInp_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownInp_Object = MibTableColumn
zhoneVdslLineConfDownInp = _ZhoneVdslLineConfDownInp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 105),
    _ZhoneVdslLineConfDownInp_Type()
)
zhoneVdslLineConfDownInp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownInp.setStatus("current")


class _ZhoneVdslLineConfUpInp_Type(Integer32):
    """Custom type zhoneVdslLineConfUpInp based on Integer32"""
    defaultValue = 4

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
              18)
        )
    )
    namedValues = NamedValues(
        *(("eightSymbols", 6),
          ("elevenSymbols", 14),
          ("fifteenSymbols", 18),
          ("fiveSymbols", 9),
          ("fourSymbols", 5),
          ("fourteenSymbols", 17),
          ("halfSymbol", 2),
          ("nineSymbols", 12),
          ("noProtection", 1),
          ("sevenSymbols", 11),
          ("singleSymbol", 3),
          ("sixSymbols", 10),
          ("sixteenSymbols", 7),
          ("tenSymbols", 13),
          ("thirteenSymbols", 16),
          ("threeSymbols", 8),
          ("twelveSymbols", 15),
          ("twoSymbols", 4))
    )


_ZhoneVdslLineConfUpInp_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpInp_Object = MibTableColumn
zhoneVdslLineConfUpInp = _ZhoneVdslLineConfUpInp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 106),
    _ZhoneVdslLineConfUpInp_Type()
)
zhoneVdslLineConfUpInp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpInp.setStatus("current")


class _ZhoneVdslLineConfDownMaxInterleavingDelay_Type(Integer32):
    """Custom type zhoneVdslLineConfDownMaxInterleavingDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZhoneVdslLineConfDownMaxInterleavingDelay_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownMaxInterleavingDelay_Object = MibTableColumn
zhoneVdslLineConfDownMaxInterleavingDelay = _ZhoneVdslLineConfDownMaxInterleavingDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 107),
    _ZhoneVdslLineConfDownMaxInterleavingDelay_Type()
)
zhoneVdslLineConfDownMaxInterleavingDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxInterleavingDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownMaxInterleavingDelay.setUnits("milliseconds")


class _ZhoneVdslLineConfUpMaxInterleavingDelay_Type(Integer32):
    """Custom type zhoneVdslLineConfUpMaxInterleavingDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZhoneVdslLineConfUpMaxInterleavingDelay_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpMaxInterleavingDelay_Object = MibTableColumn
zhoneVdslLineConfUpMaxInterleavingDelay = _ZhoneVdslLineConfUpMaxInterleavingDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 108),
    _ZhoneVdslLineConfUpMaxInterleavingDelay_Type()
)
zhoneVdslLineConfUpMaxInterleavingDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxInterleavingDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpMaxInterleavingDelay.setUnits("milliseconds")


class _ZhoneVdslLineConfDownPsdMaskEnable_Type(Integer32):
    """Custom type zhoneVdslLineConfDownPsdMaskEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mod", 3),
          ("modFallback", 4),
          ("standard", 2))
    )


_ZhoneVdslLineConfDownPsdMaskEnable_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownPsdMaskEnable_Object = MibTableColumn
zhoneVdslLineConfDownPsdMaskEnable = _ZhoneVdslLineConfDownPsdMaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 109),
    _ZhoneVdslLineConfDownPsdMaskEnable_Type()
)
zhoneVdslLineConfDownPsdMaskEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownPsdMaskEnable.setStatus("current")


class _ZhoneVdslLineConfUpPsdMaskEnable_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPsdMaskEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mod", 3),
          ("modFallback", 4),
          ("standard", 2))
    )


_ZhoneVdslLineConfUpPsdMaskEnable_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPsdMaskEnable_Object = MibTableColumn
zhoneVdslLineConfUpPsdMaskEnable = _ZhoneVdslLineConfUpPsdMaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 110),
    _ZhoneVdslLineConfUpPsdMaskEnable_Type()
)
zhoneVdslLineConfUpPsdMaskEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPsdMaskEnable.setStatus("current")


class _ZhoneVdslLineConfDownPsdMaskSelect_Type(Integer32):
    """Custom type zhoneVdslLineConfDownPsdMaskSelect based on Integer32"""
    defaultValue = 13

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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("custom", 1),
          ("customMOD", 2),
          ("dmtPSDADSL2NONOVLPFLAT", 11),
          ("dmtPSDADSL2NONOVLPM1", 9),
          ("dmtPSDADSL2NONOVLPM2", 10),
          ("dmtPSDCABMSK2", 5),
          ("dmtPSDCABMSK2RFI", 8),
          ("dmtPSDCOMSK2", 3),
          ("dmtPSDCOMSK2RFI", 6),
          ("dmtPSDFLATMSK", 4),
          ("dmtPSDFLATMSKRFI", 7),
          ("g993RegionA", 13),
          ("g993RegionA-E17a-D-128", 17),
          ("g993RegionA-E17a-D-32", 14),
          ("g993RegionA-E17a-D-48", 15),
          ("g993RegionA-E17a-D-64", 16),
          ("g993RegionC", 12),
          ("g997RegionB-E17-M2x-A", 44),
          ("g997RegionB-E30-M2x-NUS0", 45),
          ("g997RegionB-HPE17-M1-NUS0", 42),
          ("g997RegionB-HPE30-M1-NUS0", 43),
          ("g997RegionB-M1c-A-7", 36),
          ("g997RegionB-M1x-M", 38),
          ("g997RegionB-M1x-M-8", 37),
          ("g997RegionB-M2x-A", 40),
          ("g997RegionB-M2x-M", 41),
          ("g997RegionB-M2x-M-8", 39),
          ("g998RegionB-ADE17-M2x-A", 28),
          ("g998RegionB-ADE17-M2x-B", 29),
          ("g998RegionB-ADE17-M2x-NUS0-M", 27),
          ("g998RegionB-ADE30-M2x-NUS0-A", 33),
          ("g998RegionB-ADE30-M2x-NUS0-M", 32),
          ("g998RegionB-E17-M2x-NUS0", 25),
          ("g998RegionB-E17-M2x-NUS0-M", 26),
          ("g998RegionB-E30-M2x-NUS0", 30),
          ("g998RegionB-E30-M2x-NUS0-M", 31),
          ("g998RegionB-M1x-A", 18),
          ("g998RegionB-M1x-B", 19),
          ("g998RegionB-M1x-NUS0", 20),
          ("g998RegionB-M2x-A", 21),
          ("g998RegionB-M2x-B", 23),
          ("g998RegionB-M2x-M", 22),
          ("g998RegionB-M2x-NUS0", 24),
          ("g998RegionB-NONSTD-E17-M2x", 34),
          ("g998RegionB-NONSTD-E17-M2x-M", 35))
    )


_ZhoneVdslLineConfDownPsdMaskSelect_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownPsdMaskSelect_Object = MibTableColumn
zhoneVdslLineConfDownPsdMaskSelect = _ZhoneVdslLineConfDownPsdMaskSelect_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 111),
    _ZhoneVdslLineConfDownPsdMaskSelect_Type()
)
zhoneVdslLineConfDownPsdMaskSelect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownPsdMaskSelect.setStatus("current")


class _ZhoneVdslLineConfUpPsdMaskSelect_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPsdMaskSelect based on Integer32"""
    defaultValue = 21

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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57)
        )
    )
    namedValues = NamedValues(
        *(("custom", 1),
          ("dmtExtended", 18),
          ("dmtJJ100", 19),
          ("dmtStandard", 20),
          ("g993J-ADLU-32", 2),
          ("g993J-ADLU-36", 3),
          ("g993J-ADLU-40", 4),
          ("g993J-ADLU-44", 5),
          ("g993J-ADLU-48", 6),
          ("g993J-ADLU-52", 7),
          ("g993J-ADLU-60", 8),
          ("g993J-ADLU-64", 9),
          ("g993JM-EU-32", 10),
          ("g993JM-EU-36", 11),
          ("g993JM-EU-40", 12),
          ("g993JM-EU-44", 13),
          ("g993JM-EU-48", 14),
          ("g993JM-EU-52", 15),
          ("g993JM-EU-60", 16),
          ("g993JM-EU-64", 17),
          ("g993RegionA-EU-32", 21),
          ("g993RegionA-EU-36", 22),
          ("g993RegionA-EU-40", 23),
          ("g993RegionA-EU-44", 24),
          ("g993RegionA-EU-48", 25),
          ("g993RegionA-EU-52", 26),
          ("g993RegionA-EU-56", 27),
          ("g993RegionA-EU-60", 28),
          ("g993RegionA-EU-64", 29),
          ("g997RegionB-E17-M2x-A", 56),
          ("g997RegionB-E30-M2x-NUS0", 57),
          ("g997RegionB-HPE17-M1-NUS0", 54),
          ("g997RegionB-HPE30-M1-NUS0", 55),
          ("g997RegionB-M1c-A-7", 48),
          ("g997RegionB-M1x-M", 50),
          ("g997RegionB-M1x-M-8", 49),
          ("g997RegionB-M2x-A", 52),
          ("g997RegionB-M2x-M", 53),
          ("g997RegionB-M2x-M-8", 51),
          ("g998RegionB-ADE17-M2x-A", 40),
          ("g998RegionB-ADE17-M2x-B", 41),
          ("g998RegionB-ADE17-M2x-NUS0-M", 39),
          ("g998RegionB-ADE30-M2x-NUS0-A", 45),
          ("g998RegionB-ADE30-M2x-NUS0-M", 44),
          ("g998RegionB-E17-M2x-NUS0", 37),
          ("g998RegionB-E17-M2x-NUS0-M", 38),
          ("g998RegionB-E30-M2x-NUS0", 42),
          ("g998RegionB-E30-M2x-NUS0-M", 43),
          ("g998RegionB-M1x-A", 30),
          ("g998RegionB-M1x-B", 31),
          ("g998RegionB-M1x-NUS0", 32),
          ("g998RegionB-M2x-A", 33),
          ("g998RegionB-M2x-B", 35),
          ("g998RegionB-M2x-M", 34),
          ("g998RegionB-M2x-NUS0", 36),
          ("g998RegionB-NONSTD-E17-M2x", 46),
          ("g998RegionB-NONSTD-E17-M2x-M", 47))
    )


_ZhoneVdslLineConfUpPsdMaskSelect_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPsdMaskSelect_Object = MibTableColumn
zhoneVdslLineConfUpPsdMaskSelect = _ZhoneVdslLineConfUpPsdMaskSelect_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 112),
    _ZhoneVdslLineConfUpPsdMaskSelect_Type()
)
zhoneVdslLineConfUpPsdMaskSelect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPsdMaskSelect.setStatus("current")


class _ZhoneVdslLineEnableTrellisCoding_Type(TruthValue):
    """Custom type zhoneVdslLineEnableTrellisCoding based on TruthValue"""


_ZhoneVdslLineEnableTrellisCoding_Object = MibTableColumn
zhoneVdslLineEnableTrellisCoding = _ZhoneVdslLineEnableTrellisCoding_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 113),
    _ZhoneVdslLineEnableTrellisCoding_Type()
)
zhoneVdslLineEnableTrellisCoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineEnableTrellisCoding.setStatus("current")


class _ZhoneVdslLineEnableRsCoding_Type(TruthValue):
    """Custom type zhoneVdslLineEnableRsCoding based on TruthValue"""


_ZhoneVdslLineEnableRsCoding_Object = MibTableColumn
zhoneVdslLineEnableRsCoding = _ZhoneVdslLineEnableRsCoding_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 114),
    _ZhoneVdslLineEnableRsCoding_Type()
)
zhoneVdslLineEnableRsCoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineEnableRsCoding.setStatus("current")


class _ZhoneVdslLineConfPsdShape_Type(Integer32):
    """Custom type zhoneVdslLineConfPsdShape based on Integer32"""
    defaultValue = 2

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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55)
        )
    )
    namedValues = NamedValues(
        *(("region-a-adlu-128", 21),
          ("region-a-adlu-32", 12),
          ("region-a-adlu-36", 13),
          ("region-a-adlu-40", 14),
          ("region-a-adlu-44", 15),
          ("region-a-adlu-48", 16),
          ("region-a-adlu-52", 17),
          ("region-a-adlu-56", 18),
          ("region-a-adlu-60", 19),
          ("region-a-adlu-64", 20),
          ("region-a-eu-128", 11),
          ("region-a-eu-32", 2),
          ("region-a-eu-36", 3),
          ("region-a-eu-40", 4),
          ("region-a-eu-44", 5),
          ("region-a-eu-48", 6),
          ("region-a-eu-52", 7),
          ("region-a-eu-56", 8),
          ("region-a-eu-60", 9),
          ("region-a-eu-64", 10),
          ("region-a-nus0", 1),
          ("region-b-997-bt-anfp", 48),
          ("region-b-997-e17-m2x-a", 46),
          ("region-b-997-e30-m2x-nus0", 47),
          ("region-b-997-hpe17-m1-nus0", 44),
          ("region-b-997-hpe30-m1-nus0", 45),
          ("region-b-997-m1c-a-7", 38),
          ("region-b-997-m1x-m", 40),
          ("region-b-997-m1x-m-8", 39),
          ("region-b-997-m2x-a", 42),
          ("region-b-997-m2x-m", 43),
          ("region-b-997-m2x-m-8", 41),
          ("region-b-998-ade17-m2x-a", 32),
          ("region-b-998-ade17-m2x-b", 33),
          ("region-b-998-ade17-m2x-nus0-m", 31),
          ("region-b-998-ade30-m2x-nus0-a", 37),
          ("region-b-998-ade30-m2x-nus0-m", 36),
          ("region-b-998-e17-m2x-nus0", 29),
          ("region-b-998-e17-m2x-nus0-m", 30),
          ("region-b-998-e30-m2x-nus0", 34),
          ("region-b-998-e30-m2x-nus0-m", 35),
          ("region-b-998-m1x-a", 22),
          ("region-b-998-m1x-b", 23),
          ("region-b-998-m1x-nus0", 24),
          ("region-b-998-m2x-a", 25),
          ("region-b-998-m2x-b", 27),
          ("region-b-998-m2x-m", 26),
          ("region-b-998-m2x-nus0", 28),
          ("region-c-1104-co-17a", 54),
          ("region-c-1104-co-30a", 55),
          ("region-c-138-b", 49),
          ("region-c-138-co", 51),
          ("region-c-276-b", 50),
          ("region-c-276-co", 52),
          ("region-c-tcmisdn", 53))
    )


_ZhoneVdslLineConfPsdShape_Type.__name__ = "Integer32"
_ZhoneVdslLineConfPsdShape_Object = MibTableColumn
zhoneVdslLineConfPsdShape = _ZhoneVdslLineConfPsdShape_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 115),
    _ZhoneVdslLineConfPsdShape_Type()
)
zhoneVdslLineConfPsdShape.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfPsdShape.setStatus("current")


class _ZhoneVdslLineConfDownPhyRSupport_Type(Integer32):
    """Custom type zhoneVdslLineConfDownPhyRSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfDownPhyRSupport_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownPhyRSupport_Object = MibTableColumn
zhoneVdslLineConfDownPhyRSupport = _ZhoneVdslLineConfDownPhyRSupport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 116),
    _ZhoneVdslLineConfDownPhyRSupport_Type()
)
zhoneVdslLineConfDownPhyRSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownPhyRSupport.setStatus("current")


class _ZhoneVdslLineConfUpPhyRSupport_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPhyRSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfUpPhyRSupport_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPhyRSupport_Object = MibTableColumn
zhoneVdslLineConfUpPhyRSupport = _ZhoneVdslLineConfUpPhyRSupport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 117),
    _ZhoneVdslLineConfUpPhyRSupport_Type()
)
zhoneVdslLineConfUpPhyRSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPhyRSupport.setStatus("current")


class _ZhoneVdslLineConfDownPhyRmaxINP_Type(Integer32):
    """Custom type zhoneVdslLineConfDownPhyRmaxINP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 160),
    )


_ZhoneVdslLineConfDownPhyRmaxINP_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownPhyRmaxINP_Object = MibTableColumn
zhoneVdslLineConfDownPhyRmaxINP = _ZhoneVdslLineConfDownPhyRmaxINP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 118),
    _ZhoneVdslLineConfDownPhyRmaxINP_Type()
)
zhoneVdslLineConfDownPhyRmaxINP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownPhyRmaxINP.setStatus("current")


class _ZhoneVdslLineConfUpPhyRmaxINP_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPhyRmaxINP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 160),
    )


_ZhoneVdslLineConfUpPhyRmaxINP_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPhyRmaxINP_Object = MibTableColumn
zhoneVdslLineConfUpPhyRmaxINP = _ZhoneVdslLineConfUpPhyRmaxINP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 119),
    _ZhoneVdslLineConfUpPhyRmaxINP_Type()
)
zhoneVdslLineConfUpPhyRmaxINP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPhyRmaxINP.setStatus("current")


class _ZhoneVdslLineConfDownPhyRminRSoverhead_Type(Integer32):
    """Custom type zhoneVdslLineConfDownPhyRminRSoverhead based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneVdslLineConfDownPhyRminRSoverhead_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownPhyRminRSoverhead_Object = MibTableColumn
zhoneVdslLineConfDownPhyRminRSoverhead = _ZhoneVdslLineConfDownPhyRminRSoverhead_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 120),
    _ZhoneVdslLineConfDownPhyRminRSoverhead_Type()
)
zhoneVdslLineConfDownPhyRminRSoverhead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownPhyRminRSoverhead.setStatus("current")


class _ZhoneVdslLineConfUpPhyRminRSoverhead_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPhyRminRSoverhead based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneVdslLineConfUpPhyRminRSoverhead_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPhyRminRSoverhead_Object = MibTableColumn
zhoneVdslLineConfUpPhyRminRSoverhead = _ZhoneVdslLineConfUpPhyRminRSoverhead_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 121),
    _ZhoneVdslLineConfUpPhyRminRSoverhead_Type()
)
zhoneVdslLineConfUpPhyRminRSoverhead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPhyRminRSoverhead.setStatus("current")


class _ZhoneVdslLineConfDownPhyRRtxRatio_Type(Integer32):
    """Custom type zhoneVdslLineConfDownPhyRRtxRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneVdslLineConfDownPhyRRtxRatio_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownPhyRRtxRatio_Object = MibTableColumn
zhoneVdslLineConfDownPhyRRtxRatio = _ZhoneVdslLineConfDownPhyRRtxRatio_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 122),
    _ZhoneVdslLineConfDownPhyRRtxRatio_Type()
)
zhoneVdslLineConfDownPhyRRtxRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownPhyRRtxRatio.setStatus("current")


class _ZhoneVdslLineConfUpPhyRRtxRatio_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPhyRRtxRatio based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneVdslLineConfUpPhyRRtxRatio_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPhyRRtxRatio_Object = MibTableColumn
zhoneVdslLineConfUpPhyRRtxRatio = _ZhoneVdslLineConfUpPhyRRtxRatio_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 123),
    _ZhoneVdslLineConfUpPhyRRtxRatio_Type()
)
zhoneVdslLineConfUpPhyRRtxRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPhyRRtxRatio.setStatus("current")


class _ZhoneVdslLineConfUpPboPsdParamA3_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPboPsdParamA3 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 8096),
    )


_ZhoneVdslLineConfUpPboPsdParamA3_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPboPsdParamA3_Object = MibTableColumn
zhoneVdslLineConfUpPboPsdParamA3 = _ZhoneVdslLineConfUpPboPsdParamA3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 124),
    _ZhoneVdslLineConfUpPboPsdParamA3_Type()
)
zhoneVdslLineConfUpPboPsdParamA3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamA3.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamA3.setUnits(".01 dBm/Hz")


class _ZhoneVdslLineConfUpPboPsdParamA4_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPboPsdParamA4 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 8096),
    )


_ZhoneVdslLineConfUpPboPsdParamA4_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPboPsdParamA4_Object = MibTableColumn
zhoneVdslLineConfUpPboPsdParamA4 = _ZhoneVdslLineConfUpPboPsdParamA4_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 125),
    _ZhoneVdslLineConfUpPboPsdParamA4_Type()
)
zhoneVdslLineConfUpPboPsdParamA4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamA4.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamA4.setUnits(".01 dBm/Hz")


class _ZhoneVdslLineConfUpPboPsdParamB3_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPboPsdParamB3 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZhoneVdslLineConfUpPboPsdParamB3_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPboPsdParamB3_Object = MibTableColumn
zhoneVdslLineConfUpPboPsdParamB3 = _ZhoneVdslLineConfUpPboPsdParamB3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 126),
    _ZhoneVdslLineConfUpPboPsdParamB3_Type()
)
zhoneVdslLineConfUpPboPsdParamB3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamB3.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamB3.setUnits(".01 dBm/Hz")


class _ZhoneVdslLineConfUpPboPsdParamB4_Type(Integer32):
    """Custom type zhoneVdslLineConfUpPboPsdParamB4 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ZhoneVdslLineConfUpPboPsdParamB4_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpPboPsdParamB4_Object = MibTableColumn
zhoneVdslLineConfUpPboPsdParamB4 = _ZhoneVdslLineConfUpPboPsdParamB4_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 127),
    _ZhoneVdslLineConfUpPboPsdParamB4_Type()
)
zhoneVdslLineConfUpPboPsdParamB4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamB4.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpPboPsdParamB4.setUnits(".01 dBm/Hz")


class _ZhoneVdslLineConfFallbackDefaultVpi_Type(Unsigned32):
    """Custom type zhoneVdslLineConfFallbackDefaultVpi based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneVdslLineConfFallbackDefaultVpi_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfFallbackDefaultVpi_Object = MibTableColumn
zhoneVdslLineConfFallbackDefaultVpi = _ZhoneVdslLineConfFallbackDefaultVpi_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 128),
    _ZhoneVdslLineConfFallbackDefaultVpi_Type()
)
zhoneVdslLineConfFallbackDefaultVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfFallbackDefaultVpi.setStatus("current")


class _ZhoneVdslLineConfFallbackDefaultVci_Type(Unsigned32):
    """Custom type zhoneVdslLineConfFallbackDefaultVci based on Unsigned32"""
    defaultValue = 35

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneVdslLineConfFallbackDefaultVci_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfFallbackDefaultVci_Object = MibTableColumn
zhoneVdslLineConfFallbackDefaultVci = _ZhoneVdslLineConfFallbackDefaultVci_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 129),
    _ZhoneVdslLineConfFallbackDefaultVci_Type()
)
zhoneVdslLineConfFallbackDefaultVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfFallbackDefaultVci.setStatus("current")


class _ZhoneVdslLineConfDownGinpSupport_Type(Integer32):
    """Custom type zhoneVdslLineConfDownGinpSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfDownGinpSupport_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownGinpSupport_Object = MibTableColumn
zhoneVdslLineConfDownGinpSupport = _ZhoneVdslLineConfDownGinpSupport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 130),
    _ZhoneVdslLineConfDownGinpSupport_Type()
)
zhoneVdslLineConfDownGinpSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpSupport.setStatus("current")


class _ZhoneVdslLineConfUpGinpSupport_Type(Integer32):
    """Custom type zhoneVdslLineConfUpGinpSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZhoneVdslLineConfUpGinpSupport_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpGinpSupport_Object = MibTableColumn
zhoneVdslLineConfUpGinpSupport = _ZhoneVdslLineConfUpGinpSupport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 131),
    _ZhoneVdslLineConfUpGinpSupport_Type()
)
zhoneVdslLineConfUpGinpSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpSupport.setStatus("current")


class _ZhoneVdslLineConfDownGinpEtrMax_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownGinpEtrMax based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 200000),
    )


_ZhoneVdslLineConfDownGinpEtrMax_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownGinpEtrMax_Object = MibTableColumn
zhoneVdslLineConfDownGinpEtrMax = _ZhoneVdslLineConfDownGinpEtrMax_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 132),
    _ZhoneVdslLineConfDownGinpEtrMax_Type()
)
zhoneVdslLineConfDownGinpEtrMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpEtrMax.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpEtrMax.setUnits("kbps")


class _ZhoneVdslLineConfUpGinpEtrMax_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpGinpEtrMax based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2000000),
    )


_ZhoneVdslLineConfUpGinpEtrMax_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpGinpEtrMax_Object = MibTableColumn
zhoneVdslLineConfUpGinpEtrMax = _ZhoneVdslLineConfUpGinpEtrMax_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 133),
    _ZhoneVdslLineConfUpGinpEtrMax_Type()
)
zhoneVdslLineConfUpGinpEtrMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpEtrMax.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpEtrMax.setUnits("kbps")


class _ZhoneVdslLineConfDownGinpEtrMin_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownGinpEtrMin based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 200000),
    )


_ZhoneVdslLineConfDownGinpEtrMin_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownGinpEtrMin_Object = MibTableColumn
zhoneVdslLineConfDownGinpEtrMin = _ZhoneVdslLineConfDownGinpEtrMin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 134),
    _ZhoneVdslLineConfDownGinpEtrMin_Type()
)
zhoneVdslLineConfDownGinpEtrMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpEtrMin.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpEtrMin.setUnits("kbps")


class _ZhoneVdslLineConfUpGinpEtrMin_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpGinpEtrMin based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 200000),
    )


_ZhoneVdslLineConfUpGinpEtrMin_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpGinpEtrMin_Object = MibTableColumn
zhoneVdslLineConfUpGinpEtrMin = _ZhoneVdslLineConfUpGinpEtrMin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 135),
    _ZhoneVdslLineConfUpGinpEtrMin_Type()
)
zhoneVdslLineConfUpGinpEtrMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpEtrMin.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpEtrMin.setUnits("kbps")


class _ZhoneVdslLineConfDownGinpNdrMax_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownGinpNdrMax based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 200000),
    )


_ZhoneVdslLineConfDownGinpNdrMax_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownGinpNdrMax_Object = MibTableColumn
zhoneVdslLineConfDownGinpNdrMax = _ZhoneVdslLineConfDownGinpNdrMax_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 136),
    _ZhoneVdslLineConfDownGinpNdrMax_Type()
)
zhoneVdslLineConfDownGinpNdrMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpNdrMax.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpNdrMax.setUnits("kbps")


class _ZhoneVdslLineConfUpGinpNdrMax_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpGinpNdrMax based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 200000),
    )


_ZhoneVdslLineConfUpGinpNdrMax_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpGinpNdrMax_Object = MibTableColumn
zhoneVdslLineConfUpGinpNdrMax = _ZhoneVdslLineConfUpGinpNdrMax_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 137),
    _ZhoneVdslLineConfUpGinpNdrMax_Type()
)
zhoneVdslLineConfUpGinpNdrMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpNdrMax.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpNdrMax.setUnits("kbps")


class _ZhoneVdslLineConfDownGinpShineRatio_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownGinpShineRatio based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneVdslLineConfDownGinpShineRatio_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownGinpShineRatio_Object = MibTableColumn
zhoneVdslLineConfDownGinpShineRatio = _ZhoneVdslLineConfDownGinpShineRatio_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 138),
    _ZhoneVdslLineConfDownGinpShineRatio_Type()
)
zhoneVdslLineConfDownGinpShineRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpShineRatio.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpShineRatio.setUnits("ratio")


class _ZhoneVdslLineConfUpGinpShineRatio_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpGinpShineRatio based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZhoneVdslLineConfUpGinpShineRatio_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpGinpShineRatio_Object = MibTableColumn
zhoneVdslLineConfUpGinpShineRatio = _ZhoneVdslLineConfUpGinpShineRatio_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 139),
    _ZhoneVdslLineConfUpGinpShineRatio_Type()
)
zhoneVdslLineConfUpGinpShineRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpShineRatio.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpShineRatio.setUnits("ratio")


class _ZhoneVdslLineConfDownGinpLeftrThreshold_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownGinpLeftrThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ZhoneVdslLineConfDownGinpLeftrThreshold_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownGinpLeftrThreshold_Object = MibTableColumn
zhoneVdslLineConfDownGinpLeftrThreshold = _ZhoneVdslLineConfDownGinpLeftrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 140),
    _ZhoneVdslLineConfDownGinpLeftrThreshold_Type()
)
zhoneVdslLineConfDownGinpLeftrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpLeftrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpLeftrThreshold.setUnits("ratio")


class _ZhoneVdslLineConfUpGinpLeftrThreshold_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpGinpLeftrThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ZhoneVdslLineConfUpGinpLeftrThreshold_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpGinpLeftrThreshold_Object = MibTableColumn
zhoneVdslLineConfUpGinpLeftrThreshold = _ZhoneVdslLineConfUpGinpLeftrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 141),
    _ZhoneVdslLineConfUpGinpLeftrThreshold_Type()
)
zhoneVdslLineConfUpGinpLeftrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpLeftrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpLeftrThreshold.setUnits("ratio")


class _ZhoneVdslLineConfDownGinpMaxDelay_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownGinpMaxDelay based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZhoneVdslLineConfDownGinpMaxDelay_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownGinpMaxDelay_Object = MibTableColumn
zhoneVdslLineConfDownGinpMaxDelay = _ZhoneVdslLineConfDownGinpMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 142),
    _ZhoneVdslLineConfDownGinpMaxDelay_Type()
)
zhoneVdslLineConfDownGinpMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpMaxDelay.setUnits("mSecs")


class _ZhoneVdslLineConfUpGinpMaxDelay_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpGinpMaxDelay based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZhoneVdslLineConfUpGinpMaxDelay_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpGinpMaxDelay_Object = MibTableColumn
zhoneVdslLineConfUpGinpMaxDelay = _ZhoneVdslLineConfUpGinpMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 143),
    _ZhoneVdslLineConfUpGinpMaxDelay_Type()
)
zhoneVdslLineConfUpGinpMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpMaxDelay.setUnits("mSecs")


class _ZhoneVdslLineConfDownGinpMinDelay_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownGinpMinDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZhoneVdslLineConfDownGinpMinDelay_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownGinpMinDelay_Object = MibTableColumn
zhoneVdslLineConfDownGinpMinDelay = _ZhoneVdslLineConfDownGinpMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 144),
    _ZhoneVdslLineConfDownGinpMinDelay_Type()
)
zhoneVdslLineConfDownGinpMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpMinDelay.setUnits("mSecs")


class _ZhoneVdslLineConfUpGinpMinDelay_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpGinpMinDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZhoneVdslLineConfUpGinpMinDelay_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpGinpMinDelay_Object = MibTableColumn
zhoneVdslLineConfUpGinpMinDelay = _ZhoneVdslLineConfUpGinpMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 145),
    _ZhoneVdslLineConfUpGinpMinDelay_Type()
)
zhoneVdslLineConfUpGinpMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpMinDelay.setUnits("mSecs")


class _ZhoneVdslLineConfDownGinpMin_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownGinpMin based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_ZhoneVdslLineConfDownGinpMin_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownGinpMin_Object = MibTableColumn
zhoneVdslLineConfDownGinpMin = _ZhoneVdslLineConfDownGinpMin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 146),
    _ZhoneVdslLineConfDownGinpMin_Type()
)
zhoneVdslLineConfDownGinpMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpMin.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpMin.setUnits("symbols")


class _ZhoneVdslLineConfUpGinpMin_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpGinpMin based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_ZhoneVdslLineConfUpGinpMin_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpGinpMin_Object = MibTableColumn
zhoneVdslLineConfUpGinpMin = _ZhoneVdslLineConfUpGinpMin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 147),
    _ZhoneVdslLineConfUpGinpMin_Type()
)
zhoneVdslLineConfUpGinpMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpMin.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpMin.setUnits("symbols")


class _ZhoneVdslLineConfDownGinpMinRSoverhead_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownGinpMinRSoverhead based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ZhoneVdslLineConfDownGinpMinRSoverhead_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownGinpMinRSoverhead_Object = MibTableColumn
zhoneVdslLineConfDownGinpMinRSoverhead = _ZhoneVdslLineConfDownGinpMinRSoverhead_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 148),
    _ZhoneVdslLineConfDownGinpMinRSoverhead_Type()
)
zhoneVdslLineConfDownGinpMinRSoverhead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpMinRSoverhead.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpMinRSoverhead.setUnits("ratio")


class _ZhoneVdslLineConfUpGinpMinRSoverhead_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpGinpMinRSoverhead based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ZhoneVdslLineConfUpGinpMinRSoverhead_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpGinpMinRSoverhead_Object = MibTableColumn
zhoneVdslLineConfUpGinpMinRSoverhead = _ZhoneVdslLineConfUpGinpMinRSoverhead_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 149),
    _ZhoneVdslLineConfUpGinpMinRSoverhead_Type()
)
zhoneVdslLineConfUpGinpMinRSoverhead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpMinRSoverhead.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpMinRSoverhead.setUnits("ratio")


class _ZhoneVdslLineConfDownGinpReinCfg_Type(Unsigned32):
    """Custom type zhoneVdslLineConfDownGinpReinCfg based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZhoneVdslLineConfDownGinpReinCfg_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfDownGinpReinCfg_Object = MibTableColumn
zhoneVdslLineConfDownGinpReinCfg = _ZhoneVdslLineConfDownGinpReinCfg_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 150),
    _ZhoneVdslLineConfDownGinpReinCfg_Type()
)
zhoneVdslLineConfDownGinpReinCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpReinCfg.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpReinCfg.setUnits("symbols")


class _ZhoneVdslLineConfUpGinpReinCfg_Type(Unsigned32):
    """Custom type zhoneVdslLineConfUpGinpReinCfg based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZhoneVdslLineConfUpGinpReinCfg_Type.__name__ = "Unsigned32"
_ZhoneVdslLineConfUpGinpReinCfg_Object = MibTableColumn
zhoneVdslLineConfUpGinpReinCfg = _ZhoneVdslLineConfUpGinpReinCfg_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 151),
    _ZhoneVdslLineConfUpGinpReinCfg_Type()
)
zhoneVdslLineConfUpGinpReinCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpReinCfg.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpReinCfg.setUnits("symbols")


class _ZhoneVdslLineConfDownGinpReinFreq_Type(Integer32):
    """Custom type zhoneVdslLineConfDownGinpReinFreq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freq100hz", 1),
          ("freq120hz", 2))
    )


_ZhoneVdslLineConfDownGinpReinFreq_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownGinpReinFreq_Object = MibTableColumn
zhoneVdslLineConfDownGinpReinFreq = _ZhoneVdslLineConfDownGinpReinFreq_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 152),
    _ZhoneVdslLineConfDownGinpReinFreq_Type()
)
zhoneVdslLineConfDownGinpReinFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpReinFreq.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpReinFreq.setUnits("Hz")


class _ZhoneVdslLineConfUpGinpReinFreq_Type(Integer32):
    """Custom type zhoneVdslLineConfUpGinpReinFreq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freq100hz", 1),
          ("freq120hz", 2))
    )


_ZhoneVdslLineConfUpGinpReinFreq_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpGinpReinFreq_Object = MibTableColumn
zhoneVdslLineConfUpGinpReinFreq = _ZhoneVdslLineConfUpGinpReinFreq_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 153),
    _ZhoneVdslLineConfUpGinpReinFreq_Type()
)
zhoneVdslLineConfUpGinpReinFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpReinFreq.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpReinFreq.setUnits("Hz")


class _ZhoneVdslLineConfDownGinpRtxMode_Type(Integer32):
    """Custom type zhoneVdslLineConfDownGinpRtxMode based on Integer32"""
    defaultValue = 2

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
        *(("forbidden", 1),
          ("forced", 3),
          ("preferred", 2),
          ("testmode", 4))
    )


_ZhoneVdslLineConfDownGinpRtxMode_Type.__name__ = "Integer32"
_ZhoneVdslLineConfDownGinpRtxMode_Object = MibTableColumn
zhoneVdslLineConfDownGinpRtxMode = _ZhoneVdslLineConfDownGinpRtxMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 154),
    _ZhoneVdslLineConfDownGinpRtxMode_Type()
)
zhoneVdslLineConfDownGinpRtxMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfDownGinpRtxMode.setStatus("current")


class _ZhoneVdslLineConfUpGinpRtxMode_Type(Integer32):
    """Custom type zhoneVdslLineConfUpGinpRtxMode based on Integer32"""
    defaultValue = 2

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
        *(("forbidden", 1),
          ("forced", 3),
          ("preferred", 2),
          ("testmode", 4))
    )


_ZhoneVdslLineConfUpGinpRtxMode_Type.__name__ = "Integer32"
_ZhoneVdslLineConfUpGinpRtxMode_Object = MibTableColumn
zhoneVdslLineConfUpGinpRtxMode = _ZhoneVdslLineConfUpGinpRtxMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 11, 1, 155),
    _ZhoneVdslLineConfUpGinpRtxMode_Type()
)
zhoneVdslLineConfUpGinpRtxMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineConfUpGinpRtxMode.setStatus("current")
_ZhoneVdslLineAlarmConfProfileTable_Object = MibTable
zhoneVdslLineAlarmConfProfileTable = _ZhoneVdslLineAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20)
)
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfProfileTable.setStatus("current")
_ZhoneVdslLineAlarmConfProfileEntry_Object = MibTableRow
zhoneVdslLineAlarmConfProfileEntry = _ZhoneVdslLineAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1)
)
zhoneVdslLineAlarmConfProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfProfileEntry.setStatus("current")


class _ZhoneVdslLineAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type zhoneVdslLineAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZhoneVdslLineAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_ZhoneVdslLineAlarmConfProfileName_Object = MibTableColumn
zhoneVdslLineAlarmConfProfileName = _ZhoneVdslLineAlarmConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 1),
    _ZhoneVdslLineAlarmConfProfileName_Type()
)
zhoneVdslLineAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfProfileName.setStatus("current")


class _ZhoneVdslLineAlarmConfThresh15MinLofs_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh15MinLofs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneVdslLineAlarmConfThresh15MinLofs_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh15MinLofs_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh15MinLofs = _ZhoneVdslLineAlarmConfThresh15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 2),
    _ZhoneVdslLineAlarmConfThresh15MinLofs_Type()
)
zhoneVdslLineAlarmConfThresh15MinLofs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinLofs.setUnits("seconds")


class _ZhoneVdslLineAlarmConfThresh15MinLoss_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh15MinLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneVdslLineAlarmConfThresh15MinLoss_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh15MinLoss_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh15MinLoss = _ZhoneVdslLineAlarmConfThresh15MinLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 3),
    _ZhoneVdslLineAlarmConfThresh15MinLoss_Type()
)
zhoneVdslLineAlarmConfThresh15MinLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinLoss.setUnits("seconds")


class _ZhoneVdslLineAlarmConfThresh15MinLprs_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh15MinLprs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneVdslLineAlarmConfThresh15MinLprs_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh15MinLprs_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh15MinLprs = _ZhoneVdslLineAlarmConfThresh15MinLprs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 4),
    _ZhoneVdslLineAlarmConfThresh15MinLprs_Type()
)
zhoneVdslLineAlarmConfThresh15MinLprs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinLprs.setUnits("seconds")


class _ZhoneVdslLineAlarmConfThresh15MinLols_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh15MinLols based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneVdslLineAlarmConfThresh15MinLols_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh15MinLols_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh15MinLols = _ZhoneVdslLineAlarmConfThresh15MinLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 5),
    _ZhoneVdslLineAlarmConfThresh15MinLols_Type()
)
zhoneVdslLineAlarmConfThresh15MinLols.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinLols.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinLols.setUnits("seconds")


class _ZhoneVdslLineAlarmConfThresh15MinESs_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh15MinESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneVdslLineAlarmConfThresh15MinESs_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh15MinESs_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh15MinESs = _ZhoneVdslLineAlarmConfThresh15MinESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 6),
    _ZhoneVdslLineAlarmConfThresh15MinESs_Type()
)
zhoneVdslLineAlarmConfThresh15MinESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinESs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinESs.setUnits("seconds")


class _ZhoneVdslLineAlarmConfThresh15MinSESs_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh15MinSESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneVdslLineAlarmConfThresh15MinSESs_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh15MinSESs_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh15MinSESs = _ZhoneVdslLineAlarmConfThresh15MinSESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 7),
    _ZhoneVdslLineAlarmConfThresh15MinSESs_Type()
)
zhoneVdslLineAlarmConfThresh15MinSESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinSESs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinSESs.setUnits("seconds")


class _ZhoneVdslLineAlarmConfThresh15MinUASs_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh15MinUASs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneVdslLineAlarmConfThresh15MinUASs_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh15MinUASs_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh15MinUASs = _ZhoneVdslLineAlarmConfThresh15MinUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 8),
    _ZhoneVdslLineAlarmConfThresh15MinUASs_Type()
)
zhoneVdslLineAlarmConfThresh15MinUASs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinUASs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh15MinUASs.setUnits("seconds")


class _ZhoneVdslLineAlarmConfInitFailure_Type(TruthValue):
    """Custom type zhoneVdslLineAlarmConfInitFailure based on TruthValue"""


_ZhoneVdslLineAlarmConfInitFailure_Object = MibTableColumn
zhoneVdslLineAlarmConfInitFailure = _ZhoneVdslLineAlarmConfInitFailure_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 9),
    _ZhoneVdslLineAlarmConfInitFailure_Type()
)
zhoneVdslLineAlarmConfInitFailure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfInitFailure.setStatus("current")
_ZhoneVdslLineAlarmConfProfRowStatus_Type = RowStatus
_ZhoneVdslLineAlarmConfProfRowStatus_Object = MibTableColumn
zhoneVdslLineAlarmConfProfRowStatus = _ZhoneVdslLineAlarmConfProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 10),
    _ZhoneVdslLineAlarmConfProfRowStatus_Type()
)
zhoneVdslLineAlarmConfProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfProfRowStatus.setStatus("current")


class _ZhoneVdslLineAlarmConfThresh1DayLofs_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh1DayLofs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ZhoneVdslLineAlarmConfThresh1DayLofs_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh1DayLofs_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh1DayLofs = _ZhoneVdslLineAlarmConfThresh1DayLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 11),
    _ZhoneVdslLineAlarmConfThresh1DayLofs_Type()
)
zhoneVdslLineAlarmConfThresh1DayLofs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh1DayLofs.setStatus("current")


class _ZhoneVdslLineAlarmConfThresh1DayLoss_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh1DayLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ZhoneVdslLineAlarmConfThresh1DayLoss_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh1DayLoss_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh1DayLoss = _ZhoneVdslLineAlarmConfThresh1DayLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 12),
    _ZhoneVdslLineAlarmConfThresh1DayLoss_Type()
)
zhoneVdslLineAlarmConfThresh1DayLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh1DayLoss.setStatus("current")


class _ZhoneVdslLineAlarmConfThresh1DayLprs_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh1DayLprs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ZhoneVdslLineAlarmConfThresh1DayLprs_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh1DayLprs_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh1DayLprs = _ZhoneVdslLineAlarmConfThresh1DayLprs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 13),
    _ZhoneVdslLineAlarmConfThresh1DayLprs_Type()
)
zhoneVdslLineAlarmConfThresh1DayLprs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh1DayLprs.setStatus("current")


class _ZhoneVdslLineAlarmConfThresh1DayLols_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh1DayLols based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ZhoneVdslLineAlarmConfThresh1DayLols_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh1DayLols_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh1DayLols = _ZhoneVdslLineAlarmConfThresh1DayLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 14),
    _ZhoneVdslLineAlarmConfThresh1DayLols_Type()
)
zhoneVdslLineAlarmConfThresh1DayLols.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh1DayLols.setStatus("current")


class _ZhoneVdslLineAlarmConfThresh1DayESs_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh1DayESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ZhoneVdslLineAlarmConfThresh1DayESs_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh1DayESs_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh1DayESs = _ZhoneVdslLineAlarmConfThresh1DayESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 15),
    _ZhoneVdslLineAlarmConfThresh1DayESs_Type()
)
zhoneVdslLineAlarmConfThresh1DayESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh1DayESs.setStatus("current")


class _ZhoneVdslLineAlarmConfThresh1DaySESs_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh1DaySESs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ZhoneVdslLineAlarmConfThresh1DaySESs_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh1DaySESs_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh1DaySESs = _ZhoneVdslLineAlarmConfThresh1DaySESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 16),
    _ZhoneVdslLineAlarmConfThresh1DaySESs_Type()
)
zhoneVdslLineAlarmConfThresh1DaySESs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh1DaySESs.setStatus("current")


class _ZhoneVdslLineAlarmConfThresh1DayUASs_Type(Integer32):
    """Custom type zhoneVdslLineAlarmConfThresh1DayUASs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ZhoneVdslLineAlarmConfThresh1DayUASs_Type.__name__ = "Integer32"
_ZhoneVdslLineAlarmConfThresh1DayUASs_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh1DayUASs = _ZhoneVdslLineAlarmConfThresh1DayUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 17),
    _ZhoneVdslLineAlarmConfThresh1DayUASs_Type()
)
zhoneVdslLineAlarmConfThresh1DayUASs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh1DayUASs.setStatus("current")


class _ZhoneVdslLineAlarmConfThresh1DayInitFailure_Type(TruthValue):
    """Custom type zhoneVdslLineAlarmConfThresh1DayInitFailure based on TruthValue"""


_ZhoneVdslLineAlarmConfThresh1DayInitFailure_Object = MibTableColumn
zhoneVdslLineAlarmConfThresh1DayInitFailure = _ZhoneVdslLineAlarmConfThresh1DayInitFailure_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 20, 1, 18),
    _ZhoneVdslLineAlarmConfThresh1DayInitFailure_Type()
)
zhoneVdslLineAlarmConfThresh1DayInitFailure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslLineAlarmConfThresh1DayInitFailure.setStatus("current")
_ZhoneVdslCustomNotchConfProfileTable_Object = MibTable
zhoneVdslCustomNotchConfProfileTable = _ZhoneVdslCustomNotchConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 21)
)
if mibBuilder.loadTexts:
    zhoneVdslCustomNotchConfProfileTable.setStatus("current")
_ZhoneVdslCustomNotchConfProfileEntry_Object = MibTableRow
zhoneVdslCustomNotchConfProfileEntry = _ZhoneVdslCustomNotchConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 21, 1)
)
zhoneVdslCustomNotchConfProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZhoneVdsl-MIB", "zhoneVdslCustomNotchConfId"),
)
if mibBuilder.loadTexts:
    zhoneVdslCustomNotchConfProfileEntry.setStatus("current")


class _ZhoneVdslCustomNotchConfId_Type(Unsigned32):
    """Custom type zhoneVdslCustomNotchConfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZhoneVdslCustomNotchConfId_Type.__name__ = "Unsigned32"
_ZhoneVdslCustomNotchConfId_Object = MibTableColumn
zhoneVdslCustomNotchConfId = _ZhoneVdslCustomNotchConfId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 21, 1, 1),
    _ZhoneVdslCustomNotchConfId_Type()
)
zhoneVdslCustomNotchConfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslCustomNotchConfId.setStatus("current")


class _ZhoneVdslCustomNotchConfStart_Type(Unsigned32):
    """Custom type zhoneVdslCustomNotchConfStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ZhoneVdslCustomNotchConfStart_Type.__name__ = "Unsigned32"
_ZhoneVdslCustomNotchConfStart_Object = MibTableColumn
zhoneVdslCustomNotchConfStart = _ZhoneVdslCustomNotchConfStart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 21, 1, 2),
    _ZhoneVdslCustomNotchConfStart_Type()
)
zhoneVdslCustomNotchConfStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslCustomNotchConfStart.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslCustomNotchConfStart.setUnits("kHz")


class _ZhoneVdslCustomNotchConfStop_Type(Unsigned32):
    """Custom type zhoneVdslCustomNotchConfStop based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_ZhoneVdslCustomNotchConfStop_Type.__name__ = "Unsigned32"
_ZhoneVdslCustomNotchConfStop_Object = MibTableColumn
zhoneVdslCustomNotchConfStop = _ZhoneVdslCustomNotchConfStop_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 21, 1, 3),
    _ZhoneVdslCustomNotchConfStop_Type()
)
zhoneVdslCustomNotchConfStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneVdslCustomNotchConfStop.setStatus("current")
if mibBuilder.loadTexts:
    zhoneVdslCustomNotchConfStop.setUnits("kHz")
_ZhoneVdslVectDataTable_Object = MibTable
zhoneVdslVectDataTable = _ZhoneVdslVectDataTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 22)
)
if mibBuilder.loadTexts:
    zhoneVdslVectDataTable.setStatus("current")
_ZhoneVdslVectDataEntry_Object = MibTableRow
zhoneVdslVectDataEntry = _ZhoneVdslVectDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 22, 1)
)
zhoneVdslVectDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneVdslVectDataEntry.setStatus("current")


class _ZhoneVdslVectDataEsDsCounter_Type(Integer32):
    """Custom type zhoneVdslVectDataEsDsCounter based on Integer32"""
    defaultValue = 0


_ZhoneVdslVectDataEsDsCounter_Object = MibTableColumn
zhoneVdslVectDataEsDsCounter = _ZhoneVdslVectDataEsDsCounter_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 22, 1, 1),
    _ZhoneVdslVectDataEsDsCounter_Type()
)
zhoneVdslVectDataEsDsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslVectDataEsDsCounter.setStatus("current")
_ZhoneVdslVectDataEsUsCounter_Type = Integer32
_ZhoneVdslVectDataEsUsCounter_Object = MibTableColumn
zhoneVdslVectDataEsUsCounter = _ZhoneVdslVectDataEsUsCounter_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 22, 1, 2),
    _ZhoneVdslVectDataEsUsCounter_Type()
)
zhoneVdslVectDataEsUsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslVectDataEsUsCounter.setStatus("current")
_ZhoneVdslVectDataIsDsFeValid_Type = Integer32
_ZhoneVdslVectDataIsDsFeValid_Object = MibTableColumn
zhoneVdslVectDataIsDsFeValid = _ZhoneVdslVectDataIsDsFeValid_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 22, 1, 3),
    _ZhoneVdslVectDataIsDsFeValid_Type()
)
zhoneVdslVectDataIsDsFeValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslVectDataIsDsFeValid.setStatus("current")
_ZhoneVdslVectDataEsFeDsCounter_Type = Integer32
_ZhoneVdslVectDataEsFeDsCounter_Object = MibTableColumn
zhoneVdslVectDataEsFeDsCounter = _ZhoneVdslVectDataEsFeDsCounter_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 1, 22, 1, 4),
    _ZhoneVdslVectDataEsFeDsCounter_Type()
)
zhoneVdslVectDataEsFeDsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneVdslVectDataEsFeDsCounter.setStatus("current")
_ZhoneVdslConformance_ObjectIdentity = ObjectIdentity
zhoneVdslConformance = _ZhoneVdslConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 3)
)
_ZhoneVdslGroups_ObjectIdentity = ObjectIdentity
zhoneVdslGroups = _ZhoneVdslGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 3, 1)
)
_ZhoneVdslCompliances_ObjectIdentity = ObjectIdentity
zhoneVdslCompliances = _ZhoneVdslCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 3, 2)
)

# Managed Objects groups

zhoneVdslGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 3, 1, 1)
)
zhoneVdslGroup.setObjects(
      *(("ZhoneVdsl-MIB", "zhoneVdslLineCoding"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineType"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfProfile"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfProfile"),
        ("ZhoneVdsl-MIB", "zhoneVdslPhysInvSerialNumber"),
        ("ZhoneVdsl-MIB", "zhoneVdslPhysInvVendorID"),
        ("ZhoneVdsl-MIB", "zhoneVdslPhysInvVersionNumber"),
        ("ZhoneVdsl-MIB", "zhoneVdslPhysCurrSnrMgn"),
        ("ZhoneVdsl-MIB", "zhoneVdslPhysCurrAtn"),
        ("ZhoneVdsl-MIB", "zhoneVdslPhysCurrStatus"),
        ("ZhoneVdsl-MIB", "zhoneVdslPhysCurrOutputPwr"),
        ("ZhoneVdsl-MIB", "zhoneVdslPhysCurrAttainableRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslPhysCurrLineRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanInterleaveDelay"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanCrcBlockLength"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanCurrTxRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanCurrTxSlowBurstProtect"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanCurrTxFastFec"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataValidIntervals"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataInvalidIntervals"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataLofs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataLoss"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataLprs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataLols"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataSESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataUASs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataInits"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinTimeElapsed"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinLofs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinLoss"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinLprs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinLols"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinSESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinUASs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinInits"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfData1DayValidIntervals"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfData1DayInvalidIntervals"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayTimeElapsed"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayLofs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayLoss"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayLprs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayLols"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DaySESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayUASs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayInits"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfIntervalLofs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfIntervalLoss"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfIntervalLprs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfIntervalLols"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfIntervalESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfIntervalSESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfIntervalUASs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerfIntervalInits"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerf1DayIntervalMoniSecs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerf1DayIntervalLofs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerf1DayIntervalLoss"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerf1DayIntervalLprs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerf1DayIntervalLols"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerf1DayIntervalESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerf1DayIntervalSESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerf1DayIntervalUASs"),
        ("ZhoneVdsl-MIB", "zhoneVdslPerf1DayIntervalInits"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanValidIntervals"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanInvalidIntervals"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanFixedOctets"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanBadBlks"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanCurr15MinTimeElapsed"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanCurr15MinFixedOctets"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanCurr15MinBadBlks"),
        ("ZhoneVdsl-MIB", "zhoneVdslChan1DayValidIntervals"),
        ("ZhoneVdsl-MIB", "zhoneVdslChan1DayInvalidIntervals"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanCurr1DayTimeElapsed"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanCurr1DayFixedOctets"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanCurr1DayBadBlks"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanIntervalFixedOctets"),
        ("ZhoneVdsl-MIB", "zhoneVdslChanIntervalBadBlks"),
        ("ZhoneVdsl-MIB", "zhoneVdslChan1DayIntervalMoniSecs"),
        ("ZhoneVdsl-MIB", "zhoneVdslChan1DayIntervalFixedOctets"),
        ("ZhoneVdsl-MIB", "zhoneVdslChan1DayIntervalBadBlks"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownRateMode"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpRateMode"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownMaxPwr"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpMaxPwr"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownMaxSnrMgn"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownMinSnrMgn"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownTargetSnrMgn"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpMaxSnrMgn"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpMinSnrMgn"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpTargetSnrMgn"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownFastMaxDataRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownFastMinDataRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownSlowMaxDataRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownSlowMinDataRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpFastMaxDataRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpFastMinDataRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpSlowMaxDataRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpSlowMinDataRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownRateRatio"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpRateRatio"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownMaxInterDelay"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpMaxInterDelay"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownPboControl"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPboControl"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownPboLevel"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPboLevel"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDeploymentScenario"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfAdslPresence"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfApplicableStandard"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfBandPlan"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfBandPlanFx"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfBandOptUsage"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPsdTemplate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownPsdTemplate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfHamBandMask"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfCustomNotch1Start"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfCustomNotch1Stop"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfCustomNotch2Start"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfCustomNotch2Stop"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownTargetSlowBurst"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpTargetSlowBurst"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownMaxFastFec"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpMaxFastFec"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfLineType"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfProfRowStatus"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh15MinLofs"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh15MinLoss"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh15MinLprs"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh15MinLols"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh15MinESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh15MinSESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh15MinUASs"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfInitFailure"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh1DayLofs"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh1DayLoss"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh1DayLprs"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh1DayLols"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh1DayInitFailure"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfAutoModeCrtrn"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfAdslBandMode"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfAdslBandModeEndFreq"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfSeltAgc"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfVdsl2Profile"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfVdslMode"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfPboElectricalOverride"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownMaxPsd"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownMaxAggregateTxPwr"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownPsdShape"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownVirtualNoiseSnrMode"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownGhsA43TonePwr"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownErasureDetectionFast"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownErasureDetectionInterleave"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownGhsB43TonePwr"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownGhsV43TonePwr"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownGhsA43TonePwrMaxLvl"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownGhsA43cTonePwrMaxLvl"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownGhsB43TonePwrMaxLvl"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownGhsV43TonePwrMaxLvl"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownRsCoding"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfProfRowStatus"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpErasureDetectionFast"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPboPsdParamB1"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPboPsdParamA1"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPboPsdParamA2"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPboPsdParamB2"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpVirtualNoiseSnrMode"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpErasureDetectionInterleave"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpRsCoding"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPsdShape"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPboPsdTemplate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfNetworkTimingRef"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpMaxAggregateTxPwr"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownTrellis"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpTrellis"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpMaxPsd"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh1DayESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh1DaySESs"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineAlarmConfThresh1DayUASs"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfSeltEchoMeasurementTime"),
        ("ZhoneVdsl-MIB", "zhoneVdslCustomNotchConfStop"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfSeltNoiseMeasurementTime"),
        ("ZhoneVdsl-MIB", "zhoneVdslCustomNotchConfStart"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfTransmissionMode"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownDownshiftSnrMgn"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownUpshiftSnrMgn"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownMinDownshiftTime"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownMinUpshiftTime"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpDownshiftSnrMgn"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpUpshiftSnrMgn"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpMinDownshiftTime"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpMinUpshiftTime"),
        ("ZhoneVdsl-MIB", "zhoneVdslCustomNotchConfId"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownGhsA43cTonePwr"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDMTConfMode"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfPotsBypassRelayMaxDuration"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownBitSwap"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpBitSwap"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfAdslAnnexMModeEnabled"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfAdslAnnexMPsdMask"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUs0BoundaryTone"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownInp"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpInp"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownMaxInterleavingDelay"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpMaxInterleavingDelay"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownPsdMaskEnable"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPsdMaskEnable"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownPsdMaskSelect"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPsdMaskSelect"),
        ("ZhoneVdsl-MIB", "zhoneVdslPhysCurrProfile"),
        ("ZhoneVdsl-MIB", "zhoneVdslPhysCurrConnType"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineEnableTrellisCoding"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineEnableRsCoding"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfPsdShape"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownPhyRSupport"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPhyRSupport"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownPhyRmaxINP"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPhyRmaxINP"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownPhyRminRSoverhead"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPhyRminRSoverhead"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownPhyRRtxRatio"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPhyRRtxRatio"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPboPsdParamA3"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPboPsdParamA4"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPboPsdParamB3"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpPboPsdParamB4"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfFallbackDefaultVpi"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfFallbackDefaultVci"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpMinTxThresholdAlarm"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownMinTxThresholdAlarm"))
)
if mibBuilder.loadTexts:
    zhoneVdslGroup.setStatus("current")


# Notification objects

vdslXtucPerf15MinLofsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 1)
)
vdslXtucPerf15MinLofsThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinLofs")
)
if mibBuilder.loadTexts:
    vdslXtucPerf15MinLofsThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf15MinLossThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 2)
)
vdslXtucPerf15MinLossThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinLoss")
)
if mibBuilder.loadTexts:
    vdslXtucPerf15MinLossThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf15MinLprsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 3)
)
vdslXtucPerf15MinLprsThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinLprs")
)
if mibBuilder.loadTexts:
    vdslXtucPerf15MinLprsThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf15MinLolsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 4)
)
vdslXtucPerf15MinLolsThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinLols")
)
if mibBuilder.loadTexts:
    vdslXtucPerf15MinLolsThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf15MinESsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 5)
)
vdslXtucPerf15MinESsThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinESs")
)
if mibBuilder.loadTexts:
    vdslXtucPerf15MinESsThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf15MinSESsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 6)
)
vdslXtucPerf15MinSESsThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinSESs")
)
if mibBuilder.loadTexts:
    vdslXtucPerf15MinSESsThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf15MinUASsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 7)
)
vdslXtucPerf15MinUASsThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr15MinUASs")
)
if mibBuilder.loadTexts:
    vdslXtucPerf15MinUASsThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf1DayLofsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 8)
)
vdslXtucPerf1DayLofsThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayLofs")
)
if mibBuilder.loadTexts:
    vdslXtucPerf1DayLofsThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf1DayLossThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 9)
)
vdslXtucPerf1DayLossThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayLoss")
)
if mibBuilder.loadTexts:
    vdslXtucPerf1DayLossThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf1DayLprsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 10)
)
vdslXtucPerf1DayLprsThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayLprs")
)
if mibBuilder.loadTexts:
    vdslXtucPerf1DayLprsThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf1DayLolsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 11)
)
vdslXtucPerf1DayLolsThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayLols")
)
if mibBuilder.loadTexts:
    vdslXtucPerf1DayLolsThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf1DayESsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 12)
)
vdslXtucPerf1DayESsThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayESs")
)
if mibBuilder.loadTexts:
    vdslXtucPerf1DayESsThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf1DaySESsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 13)
)
vdslXtucPerf1DaySESsThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DaySESs")
)
if mibBuilder.loadTexts:
    vdslXtucPerf1DaySESsThreshTrap.setStatus(
        "current"
    )

vdslXtucPerf1DayUASsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 14)
)
vdslXtucPerf1DayUASsThreshTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataCurr1DayUASs")
)
if mibBuilder.loadTexts:
    vdslXtucPerf1DayUASsThreshTrap.setStatus(
        "current"
    )

zhoneVdslInitFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 15)
)
zhoneVdslInitFailureTrap.setObjects(
    ("ZhoneVdsl-MIB", "zhoneVdslPerfDataInits")
)
if mibBuilder.loadTexts:
    zhoneVdslInitFailureTrap.setStatus(
        "current"
    )

vdslXtucMinTxThresholdAlarmFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 16)
)
vdslXtucMinTxThresholdAlarmFailureTrap.setObjects(
      *(("ZhoneVdsl-MIB", "zhoneVdslChanCurrTxRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfDownMinTxThresholdAlarm"))
)
if mibBuilder.loadTexts:
    vdslXtucMinTxThresholdAlarmFailureTrap.setStatus(
        "current"
    )

vdslXturMinTxThresholdAlarmFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 0, 17)
)
vdslXturMinTxThresholdAlarmFailureTrap.setObjects(
      *(("ZhoneVdsl-MIB", "zhoneVdslChanCurrTxRate"),
        ("ZhoneVdsl-MIB", "zhoneVdslLineConfUpMinTxThresholdAlarm"))
)
if mibBuilder.loadTexts:
    vdslXturMinTxThresholdAlarmFailureTrap.setStatus(
        "current"
    )


# Notifications groups

zhoneVdslNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 3, 1, 2)
)
zhoneVdslNotificationGroup.setObjects(
      *(("ZhoneVdsl-MIB", "vdslXtucPerf15MinLofsThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf15MinLossThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf15MinLprsThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf15MinLolsThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf15MinESsThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf15MinSESsThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf15MinUASsThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf1DayLofsThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf1DayLossThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf1DayLprsThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf1DayLolsThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf1DayESsThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf1DaySESsThreshTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucPerf1DayUASsThreshTrap"),
        ("ZhoneVdsl-MIB", "zhoneVdslInitFailureTrap"),
        ("ZhoneVdsl-MIB", "vdslXtucMinTxThresholdAlarmFailureTrap"),
        ("ZhoneVdsl-MIB", "vdslXturMinTxThresholdAlarmFailureTrap"))
)
if mibBuilder.loadTexts:
    zhoneVdslNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

zhoneVdslLineMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 5, 13, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    zhoneVdslLineMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZhoneVdsl-MIB",
    **{"ZhoneVdslLineCodingType": ZhoneVdslLineCodingType,
       "ZhoneVdslLineEntity": ZhoneVdslLineEntity,
       "zhoneVdslLineMib": zhoneVdslLineMib,
       "zhoneVdslNotifications": zhoneVdslNotifications,
       "vdslXtucPerf15MinLofsThreshTrap": vdslXtucPerf15MinLofsThreshTrap,
       "vdslXtucPerf15MinLossThreshTrap": vdslXtucPerf15MinLossThreshTrap,
       "vdslXtucPerf15MinLprsThreshTrap": vdslXtucPerf15MinLprsThreshTrap,
       "vdslXtucPerf15MinLolsThreshTrap": vdslXtucPerf15MinLolsThreshTrap,
       "vdslXtucPerf15MinESsThreshTrap": vdslXtucPerf15MinESsThreshTrap,
       "vdslXtucPerf15MinSESsThreshTrap": vdslXtucPerf15MinSESsThreshTrap,
       "vdslXtucPerf15MinUASsThreshTrap": vdslXtucPerf15MinUASsThreshTrap,
       "vdslXtucPerf1DayLofsThreshTrap": vdslXtucPerf1DayLofsThreshTrap,
       "vdslXtucPerf1DayLossThreshTrap": vdslXtucPerf1DayLossThreshTrap,
       "vdslXtucPerf1DayLprsThreshTrap": vdslXtucPerf1DayLprsThreshTrap,
       "vdslXtucPerf1DayLolsThreshTrap": vdslXtucPerf1DayLolsThreshTrap,
       "vdslXtucPerf1DayESsThreshTrap": vdslXtucPerf1DayESsThreshTrap,
       "vdslXtucPerf1DaySESsThreshTrap": vdslXtucPerf1DaySESsThreshTrap,
       "vdslXtucPerf1DayUASsThreshTrap": vdslXtucPerf1DayUASsThreshTrap,
       "zhoneVdslInitFailureTrap": zhoneVdslInitFailureTrap,
       "vdslXtucMinTxThresholdAlarmFailureTrap": vdslXtucMinTxThresholdAlarmFailureTrap,
       "vdslXturMinTxThresholdAlarmFailureTrap": vdslXturMinTxThresholdAlarmFailureTrap,
       "zhoneVdslMibObjects": zhoneVdslMibObjects,
       "zhoneVdslLineTable": zhoneVdslLineTable,
       "zhoneVdslLineEntry": zhoneVdslLineEntry,
       "zhoneVdslLineCoding": zhoneVdslLineCoding,
       "zhoneVdslLineType": zhoneVdslLineType,
       "zhoneVdslLineConfProfile": zhoneVdslLineConfProfile,
       "zhoneVdslLineAlarmConfProfile": zhoneVdslLineAlarmConfProfile,
       "zhoneVdslPhysTable": zhoneVdslPhysTable,
       "zhoneVdslPhysEntry": zhoneVdslPhysEntry,
       "zhoneVdslPhysSide": zhoneVdslPhysSide,
       "zhoneVdslPhysInvSerialNumber": zhoneVdslPhysInvSerialNumber,
       "zhoneVdslPhysInvVendorID": zhoneVdslPhysInvVendorID,
       "zhoneVdslPhysInvVersionNumber": zhoneVdslPhysInvVersionNumber,
       "zhoneVdslPhysCurrSnrMgn": zhoneVdslPhysCurrSnrMgn,
       "zhoneVdslPhysCurrAtn": zhoneVdslPhysCurrAtn,
       "zhoneVdslPhysCurrStatus": zhoneVdslPhysCurrStatus,
       "zhoneVdslPhysCurrOutputPwr": zhoneVdslPhysCurrOutputPwr,
       "zhoneVdslPhysCurrAttainableRate": zhoneVdslPhysCurrAttainableRate,
       "zhoneVdslPhysCurrLineRate": zhoneVdslPhysCurrLineRate,
       "zhoneVdslPhysCurrConnType": zhoneVdslPhysCurrConnType,
       "zhoneVdslPhysCurrProfile": zhoneVdslPhysCurrProfile,
       "zhoneVdslPhysPhyRActive": zhoneVdslPhysPhyRActive,
       "zhoneVdslPhysGinpActive": zhoneVdslPhysGinpActive,
       "zhoneVdslPhysTransportMode": zhoneVdslPhysTransportMode,
       "zhoneVdslChanTable": zhoneVdslChanTable,
       "zhoneVdslChanEntry": zhoneVdslChanEntry,
       "zhoneVdslChanInterleaveDelay": zhoneVdslChanInterleaveDelay,
       "zhoneVdslChanCrcBlockLength": zhoneVdslChanCrcBlockLength,
       "zhoneVdslChanCurrTxRate": zhoneVdslChanCurrTxRate,
       "zhoneVdslChanCurrTxSlowBurstProtect": zhoneVdslChanCurrTxSlowBurstProtect,
       "zhoneVdslChanCurrTxFastFec": zhoneVdslChanCurrTxFastFec,
       "zhoneVdslPerfDataTable": zhoneVdslPerfDataTable,
       "zhoneVdslPerfDataEntry": zhoneVdslPerfDataEntry,
       "zhoneVdslPerfDataValidIntervals": zhoneVdslPerfDataValidIntervals,
       "zhoneVdslPerfDataInvalidIntervals": zhoneVdslPerfDataInvalidIntervals,
       "zhoneVdslPerfDataLofs": zhoneVdslPerfDataLofs,
       "zhoneVdslPerfDataLoss": zhoneVdslPerfDataLoss,
       "zhoneVdslPerfDataLprs": zhoneVdslPerfDataLprs,
       "zhoneVdslPerfDataLols": zhoneVdslPerfDataLols,
       "zhoneVdslPerfDataESs": zhoneVdslPerfDataESs,
       "zhoneVdslPerfDataSESs": zhoneVdslPerfDataSESs,
       "zhoneVdslPerfDataUASs": zhoneVdslPerfDataUASs,
       "zhoneVdslPerfDataInits": zhoneVdslPerfDataInits,
       "zhoneVdslPerfDataCurr15MinTimeElapsed": zhoneVdslPerfDataCurr15MinTimeElapsed,
       "zhoneVdslPerfDataCurr15MinLofs": zhoneVdslPerfDataCurr15MinLofs,
       "zhoneVdslPerfDataCurr15MinLoss": zhoneVdslPerfDataCurr15MinLoss,
       "zhoneVdslPerfDataCurr15MinLprs": zhoneVdslPerfDataCurr15MinLprs,
       "zhoneVdslPerfDataCurr15MinLols": zhoneVdslPerfDataCurr15MinLols,
       "zhoneVdslPerfDataCurr15MinESs": zhoneVdslPerfDataCurr15MinESs,
       "zhoneVdslPerfDataCurr15MinSESs": zhoneVdslPerfDataCurr15MinSESs,
       "zhoneVdslPerfDataCurr15MinUASs": zhoneVdslPerfDataCurr15MinUASs,
       "zhoneVdslPerfDataCurr15MinInits": zhoneVdslPerfDataCurr15MinInits,
       "zhoneVdslPerfData1DayValidIntervals": zhoneVdslPerfData1DayValidIntervals,
       "zhoneVdslPerfData1DayInvalidIntervals": zhoneVdslPerfData1DayInvalidIntervals,
       "zhoneVdslPerfDataCurr1DayTimeElapsed": zhoneVdslPerfDataCurr1DayTimeElapsed,
       "zhoneVdslPerfDataCurr1DayLofs": zhoneVdslPerfDataCurr1DayLofs,
       "zhoneVdslPerfDataCurr1DayLoss": zhoneVdslPerfDataCurr1DayLoss,
       "zhoneVdslPerfDataCurr1DayLprs": zhoneVdslPerfDataCurr1DayLprs,
       "zhoneVdslPerfDataCurr1DayLols": zhoneVdslPerfDataCurr1DayLols,
       "zhoneVdslPerfDataCurr1DayESs": zhoneVdslPerfDataCurr1DayESs,
       "zhoneVdslPerfDataCurr1DaySESs": zhoneVdslPerfDataCurr1DaySESs,
       "zhoneVdslPerfDataCurr1DayUASs": zhoneVdslPerfDataCurr1DayUASs,
       "zhoneVdslPerfDataCurr1DayInits": zhoneVdslPerfDataCurr1DayInits,
       "zhoneVdslPhyrRetransmittedCodewords": zhoneVdslPhyrRetransmittedCodewords,
       "zhoneVdslPhyrCorrectedRetransmittedCodewords": zhoneVdslPhyrCorrectedRetransmittedCodewords,
       "zhoneVdslPhyrUncorrectableRetransmittedCodewords": zhoneVdslPhyrUncorrectableRetransmittedCodewords,
       "zhoneVdslPhyrCurr15MinRetransmittedCodewords": zhoneVdslPhyrCurr15MinRetransmittedCodewords,
       "zhoneVdslPhyrCurr15MinCorrectedRetransmittedCodewords": zhoneVdslPhyrCurr15MinCorrectedRetransmittedCodewords,
       "zhoneVdslPhyrCurr15MinUncorrectableRetransmittedCodewords": zhoneVdslPhyrCurr15MinUncorrectableRetransmittedCodewords,
       "zhoneVdslPhyrCurr1DayRetransmittedCodewords": zhoneVdslPhyrCurr1DayRetransmittedCodewords,
       "zhoneVdslPhyrCurr1DayCorrectedRetransmittedCodewords": zhoneVdslPhyrCurr1DayCorrectedRetransmittedCodewords,
       "zhoneVdslPhyrCurr1DayUncorrectableRetransmittedCodewords": zhoneVdslPhyrCurr1DayUncorrectableRetransmittedCodewords,
       "zhoneVdslPhyrPrev1DayRetransmittedCodewords": zhoneVdslPhyrPrev1DayRetransmittedCodewords,
       "zhoneVdslPhyrPrev1DayCorrectedRetransmittedCodewords": zhoneVdslPhyrPrev1DayCorrectedRetransmittedCodewords,
       "zhoneVdslPhyrPrev1DayUncorrectableRetransmittedCodewords": zhoneVdslPhyrPrev1DayUncorrectableRetransmittedCodewords,
       "zhoneVdslGinpLeftrSecs": zhoneVdslGinpLeftrSecs,
       "zhoneVdslGinpErrorFreeBits": zhoneVdslGinpErrorFreeBits,
       "zhoneVdslGinpMinEftr": zhoneVdslGinpMinEftr,
       "zhoneVdslGinpCurr15MinLeftrSecs": zhoneVdslGinpCurr15MinLeftrSecs,
       "zhoneVdslGinpCurr15MinErrorFreeBits": zhoneVdslGinpCurr15MinErrorFreeBits,
       "zhoneVdslGinpCurr15MinMinEftr": zhoneVdslGinpCurr15MinMinEftr,
       "zhoneVdslGinpCurr1DayLeftrSecs": zhoneVdslGinpCurr1DayLeftrSecs,
       "zhoneVdslGinpCurr1DayErrorFreeBits": zhoneVdslGinpCurr1DayErrorFreeBits,
       "zhoneVdslGinpCurr1DayMinEftr": zhoneVdslGinpCurr1DayMinEftr,
       "zhoneVdslGinpPrev1DayLeftrSecs": zhoneVdslGinpPrev1DayLeftrSecs,
       "zhoneVdslGinpPrev1DayErrorFreeBits": zhoneVdslGinpPrev1DayErrorFreeBits,
       "zhoneVdslGinpPrev1DayMinEftr": zhoneVdslGinpPrev1DayMinEftr,
       "zhoneVdslPerfIntervalTable": zhoneVdslPerfIntervalTable,
       "zhoneVdslPerfIntervalEntry": zhoneVdslPerfIntervalEntry,
       "zhoneVdslPerfIntervalNumber": zhoneVdslPerfIntervalNumber,
       "zhoneVdslPerfIntervalLofs": zhoneVdslPerfIntervalLofs,
       "zhoneVdslPerfIntervalLoss": zhoneVdslPerfIntervalLoss,
       "zhoneVdslPerfIntervalLprs": zhoneVdslPerfIntervalLprs,
       "zhoneVdslPerfIntervalLols": zhoneVdslPerfIntervalLols,
       "zhoneVdslPerfIntervalESs": zhoneVdslPerfIntervalESs,
       "zhoneVdslPerfIntervalSESs": zhoneVdslPerfIntervalSESs,
       "zhoneVdslPerfIntervalUASs": zhoneVdslPerfIntervalUASs,
       "zhoneVdslPerfIntervalInits": zhoneVdslPerfIntervalInits,
       "zhoneVdslPerf1DayIntervalTable": zhoneVdslPerf1DayIntervalTable,
       "zhoneVdslPerf1DayIntervalEntry": zhoneVdslPerf1DayIntervalEntry,
       "zhoneVdslPerf1DayIntervalNumber": zhoneVdslPerf1DayIntervalNumber,
       "zhoneVdslPerf1DayIntervalMoniSecs": zhoneVdslPerf1DayIntervalMoniSecs,
       "zhoneVdslPerf1DayIntervalLofs": zhoneVdslPerf1DayIntervalLofs,
       "zhoneVdslPerf1DayIntervalLoss": zhoneVdslPerf1DayIntervalLoss,
       "zhoneVdslPerf1DayIntervalLprs": zhoneVdslPerf1DayIntervalLprs,
       "zhoneVdslPerf1DayIntervalLols": zhoneVdslPerf1DayIntervalLols,
       "zhoneVdslPerf1DayIntervalESs": zhoneVdslPerf1DayIntervalESs,
       "zhoneVdslPerf1DayIntervalSESs": zhoneVdslPerf1DayIntervalSESs,
       "zhoneVdslPerf1DayIntervalUASs": zhoneVdslPerf1DayIntervalUASs,
       "zhoneVdslPerf1DayIntervalInits": zhoneVdslPerf1DayIntervalInits,
       "zhoneVdslChanPerfDataTable": zhoneVdslChanPerfDataTable,
       "zhoneVdslChanPerfDataEntry": zhoneVdslChanPerfDataEntry,
       "zhoneVdslChanValidIntervals": zhoneVdslChanValidIntervals,
       "zhoneVdslChanInvalidIntervals": zhoneVdslChanInvalidIntervals,
       "zhoneVdslChanFixedOctets": zhoneVdslChanFixedOctets,
       "zhoneVdslChanBadBlks": zhoneVdslChanBadBlks,
       "zhoneVdslChanCurr15MinTimeElapsed": zhoneVdslChanCurr15MinTimeElapsed,
       "zhoneVdslChanCurr15MinFixedOctets": zhoneVdslChanCurr15MinFixedOctets,
       "zhoneVdslChanCurr15MinBadBlks": zhoneVdslChanCurr15MinBadBlks,
       "zhoneVdslChan1DayValidIntervals": zhoneVdslChan1DayValidIntervals,
       "zhoneVdslChan1DayInvalidIntervals": zhoneVdslChan1DayInvalidIntervals,
       "zhoneVdslChanCurr1DayTimeElapsed": zhoneVdslChanCurr1DayTimeElapsed,
       "zhoneVdslChanCurr1DayFixedOctets": zhoneVdslChanCurr1DayFixedOctets,
       "zhoneVdslChanCurr1DayBadBlks": zhoneVdslChanCurr1DayBadBlks,
       "zhoneVdslChanIntervalTable": zhoneVdslChanIntervalTable,
       "zhoneVdslChanIntervalEntry": zhoneVdslChanIntervalEntry,
       "zhoneVdslChanIntervalNumber": zhoneVdslChanIntervalNumber,
       "zhoneVdslChanIntervalFixedOctets": zhoneVdslChanIntervalFixedOctets,
       "zhoneVdslChanIntervalBadBlks": zhoneVdslChanIntervalBadBlks,
       "zhoneVdslChan1DayIntervalTable": zhoneVdslChan1DayIntervalTable,
       "zhoneVdslChan1DayIntervalEntry": zhoneVdslChan1DayIntervalEntry,
       "zhoneVdslChan1DayIntervalNumber": zhoneVdslChan1DayIntervalNumber,
       "zhoneVdslChan1DayIntervalMoniSecs": zhoneVdslChan1DayIntervalMoniSecs,
       "zhoneVdslChan1DayIntervalFixedOctets": zhoneVdslChan1DayIntervalFixedOctets,
       "zhoneVdslChan1DayIntervalBadBlks": zhoneVdslChan1DayIntervalBadBlks,
       "zhoneVdslLineConfProfileTable": zhoneVdslLineConfProfileTable,
       "zhoneVdslLineConfProfileEntry": zhoneVdslLineConfProfileEntry,
       "zhoneVdslLineConfProfileName": zhoneVdslLineConfProfileName,
       "zhoneVdslLineConfDownRateMode": zhoneVdslLineConfDownRateMode,
       "zhoneVdslLineConfUpRateMode": zhoneVdslLineConfUpRateMode,
       "zhoneVdslLineConfDownMaxPwr": zhoneVdslLineConfDownMaxPwr,
       "zhoneVdslLineConfUpMaxPwr": zhoneVdslLineConfUpMaxPwr,
       "zhoneVdslLineConfDownMaxSnrMgn": zhoneVdslLineConfDownMaxSnrMgn,
       "zhoneVdslLineConfDownMinSnrMgn": zhoneVdslLineConfDownMinSnrMgn,
       "zhoneVdslLineConfDownTargetSnrMgn": zhoneVdslLineConfDownTargetSnrMgn,
       "zhoneVdslLineConfUpMaxSnrMgn": zhoneVdslLineConfUpMaxSnrMgn,
       "zhoneVdslLineConfUpMinSnrMgn": zhoneVdslLineConfUpMinSnrMgn,
       "zhoneVdslLineConfUpTargetSnrMgn": zhoneVdslLineConfUpTargetSnrMgn,
       "zhoneVdslLineConfDownFastMaxDataRate": zhoneVdslLineConfDownFastMaxDataRate,
       "zhoneVdslLineConfDownFastMinDataRate": zhoneVdslLineConfDownFastMinDataRate,
       "zhoneVdslLineConfDownSlowMaxDataRate": zhoneVdslLineConfDownSlowMaxDataRate,
       "zhoneVdslLineConfDownSlowMinDataRate": zhoneVdslLineConfDownSlowMinDataRate,
       "zhoneVdslLineConfUpFastMaxDataRate": zhoneVdslLineConfUpFastMaxDataRate,
       "zhoneVdslLineConfUpFastMinDataRate": zhoneVdslLineConfUpFastMinDataRate,
       "zhoneVdslLineConfUpSlowMaxDataRate": zhoneVdslLineConfUpSlowMaxDataRate,
       "zhoneVdslLineConfUpSlowMinDataRate": zhoneVdslLineConfUpSlowMinDataRate,
       "zhoneVdslLineConfDownRateRatio": zhoneVdslLineConfDownRateRatio,
       "zhoneVdslLineConfUpRateRatio": zhoneVdslLineConfUpRateRatio,
       "zhoneVdslLineConfDownMaxInterDelay": zhoneVdslLineConfDownMaxInterDelay,
       "zhoneVdslLineConfUpMaxInterDelay": zhoneVdslLineConfUpMaxInterDelay,
       "zhoneVdslLineConfDownPboControl": zhoneVdslLineConfDownPboControl,
       "zhoneVdslLineConfUpPboControl": zhoneVdslLineConfUpPboControl,
       "zhoneVdslLineConfDownPboLevel": zhoneVdslLineConfDownPboLevel,
       "zhoneVdslLineConfUpPboLevel": zhoneVdslLineConfUpPboLevel,
       "zhoneVdslLineConfDeploymentScenario": zhoneVdslLineConfDeploymentScenario,
       "zhoneVdslLineConfAdslPresence": zhoneVdslLineConfAdslPresence,
       "zhoneVdslLineConfApplicableStandard": zhoneVdslLineConfApplicableStandard,
       "zhoneVdslLineConfBandPlan": zhoneVdslLineConfBandPlan,
       "zhoneVdslLineConfBandPlanFx": zhoneVdslLineConfBandPlanFx,
       "zhoneVdslLineConfBandOptUsage": zhoneVdslLineConfBandOptUsage,
       "zhoneVdslLineConfUpPsdTemplate": zhoneVdslLineConfUpPsdTemplate,
       "zhoneVdslLineConfDownPsdTemplate": zhoneVdslLineConfDownPsdTemplate,
       "zhoneVdslLineConfHamBandMask": zhoneVdslLineConfHamBandMask,
       "zhoneVdslLineConfCustomNotch1Start": zhoneVdslLineConfCustomNotch1Start,
       "zhoneVdslLineConfCustomNotch1Stop": zhoneVdslLineConfCustomNotch1Stop,
       "zhoneVdslLineConfCustomNotch2Start": zhoneVdslLineConfCustomNotch2Start,
       "zhoneVdslLineConfCustomNotch2Stop": zhoneVdslLineConfCustomNotch2Stop,
       "zhoneVdslLineConfDownTargetSlowBurst": zhoneVdslLineConfDownTargetSlowBurst,
       "zhoneVdslLineConfUpTargetSlowBurst": zhoneVdslLineConfUpTargetSlowBurst,
       "zhoneVdslLineConfDownMaxFastFec": zhoneVdslLineConfDownMaxFastFec,
       "zhoneVdslLineConfUpMaxFastFec": zhoneVdslLineConfUpMaxFastFec,
       "zhoneVdslLineConfLineType": zhoneVdslLineConfLineType,
       "zhoneVdslLineConfProfRowStatus": zhoneVdslLineConfProfRowStatus,
       "zhoneVdslLineConfTransmissionMode": zhoneVdslLineConfTransmissionMode,
       "zhoneVdslLineConfVdsl2Profile": zhoneVdslLineConfVdsl2Profile,
       "zhoneVdslLineConfVdslMode": zhoneVdslLineConfVdslMode,
       "zhoneVdslLineConfPboElectricalOverride": zhoneVdslLineConfPboElectricalOverride,
       "zhoneVdslLineConfAutoModeCrtrn": zhoneVdslLineConfAutoModeCrtrn,
       "zhoneVdslLineConfNetworkTimingRef": zhoneVdslLineConfNetworkTimingRef,
       "zhoneVdslLineConfAdslBandMode": zhoneVdslLineConfAdslBandMode,
       "zhoneVdslLineConfAdslBandModeEndFreq": zhoneVdslLineConfAdslBandModeEndFreq,
       "zhoneVdslLineConfSeltEchoMeasurementTime": zhoneVdslLineConfSeltEchoMeasurementTime,
       "zhoneVdslLineConfSeltNoiseMeasurementTime": zhoneVdslLineConfSeltNoiseMeasurementTime,
       "zhoneVdslLineConfSeltAgc": zhoneVdslLineConfSeltAgc,
       "zhoneVdslLineConfDownTrellis": zhoneVdslLineConfDownTrellis,
       "zhoneVdslLineConfUpTrellis": zhoneVdslLineConfUpTrellis,
       "zhoneVdslLineConfDownMaxAggregateTxPwr": zhoneVdslLineConfDownMaxAggregateTxPwr,
       "zhoneVdslLineConfUpMaxAggregateTxPwr": zhoneVdslLineConfUpMaxAggregateTxPwr,
       "zhoneVdslLineConfDownMaxPsd": zhoneVdslLineConfDownMaxPsd,
       "zhoneVdslLineConfUpMaxPsd": zhoneVdslLineConfUpMaxPsd,
       "zhoneVdslLineConfDownPsdShape": zhoneVdslLineConfDownPsdShape,
       "zhoneVdslLineConfUpPsdShape": zhoneVdslLineConfUpPsdShape,
       "zhoneVdslLineConfDownVirtualNoiseSnrMode": zhoneVdslLineConfDownVirtualNoiseSnrMode,
       "zhoneVdslLineConfUpVirtualNoiseSnrMode": zhoneVdslLineConfUpVirtualNoiseSnrMode,
       "zhoneVdslLineConfDownErasureDetectionFast": zhoneVdslLineConfDownErasureDetectionFast,
       "zhoneVdslLineConfUpErasureDetectionFast": zhoneVdslLineConfUpErasureDetectionFast,
       "zhoneVdslLineConfDownErasureDetectionInterleave": zhoneVdslLineConfDownErasureDetectionInterleave,
       "zhoneVdslLineConfUpErasureDetectionInterleave": zhoneVdslLineConfUpErasureDetectionInterleave,
       "zhoneVdslLineConfDownGhsA43TonePwr": zhoneVdslLineConfDownGhsA43TonePwr,
       "zhoneVdslLineConfDownGhsB43TonePwr": zhoneVdslLineConfDownGhsB43TonePwr,
       "zhoneVdslLineConfDownGhsA43cTonePwr": zhoneVdslLineConfDownGhsA43cTonePwr,
       "zhoneVdslLineConfDownGhsV43TonePwr": zhoneVdslLineConfDownGhsV43TonePwr,
       "zhoneVdslLineConfDownGhsA43TonePwrMaxLvl": zhoneVdslLineConfDownGhsA43TonePwrMaxLvl,
       "zhoneVdslLineConfDownGhsB43TonePwrMaxLvl": zhoneVdslLineConfDownGhsB43TonePwrMaxLvl,
       "zhoneVdslLineConfDownGhsA43cTonePwrMaxLvl": zhoneVdslLineConfDownGhsA43cTonePwrMaxLvl,
       "zhoneVdslLineConfDownGhsV43TonePwrMaxLvl": zhoneVdslLineConfDownGhsV43TonePwrMaxLvl,
       "zhoneVdslLineConfDownRsCoding": zhoneVdslLineConfDownRsCoding,
       "zhoneVdslLineConfUpRsCoding": zhoneVdslLineConfUpRsCoding,
       "zhoneVdslLineConfUpPboPsdTemplate": zhoneVdslLineConfUpPboPsdTemplate,
       "zhoneVdslLineConfUpPboPsdParamA1": zhoneVdslLineConfUpPboPsdParamA1,
       "zhoneVdslLineConfUpPboPsdParamA2": zhoneVdslLineConfUpPboPsdParamA2,
       "zhoneVdslLineConfUpPboPsdParamB1": zhoneVdslLineConfUpPboPsdParamB1,
       "zhoneVdslLineConfUpPboPsdParamB2": zhoneVdslLineConfUpPboPsdParamB2,
       "zhoneVdslLineConfDownDownshiftSnrMgn": zhoneVdslLineConfDownDownshiftSnrMgn,
       "zhoneVdslLineConfDownUpshiftSnrMgn": zhoneVdslLineConfDownUpshiftSnrMgn,
       "zhoneVdslLineConfDownMinDownshiftTime": zhoneVdslLineConfDownMinDownshiftTime,
       "zhoneVdslLineConfDownMinUpshiftTime": zhoneVdslLineConfDownMinUpshiftTime,
       "zhoneVdslLineConfUpDownshiftSnrMgn": zhoneVdslLineConfUpDownshiftSnrMgn,
       "zhoneVdslLineConfUpUpshiftSnrMgn": zhoneVdslLineConfUpUpshiftSnrMgn,
       "zhoneVdslLineConfUpMinDownshiftTime": zhoneVdslLineConfUpMinDownshiftTime,
       "zhoneVdslLineConfUpMinUpshiftTime": zhoneVdslLineConfUpMinUpshiftTime,
       "zhoneVdslLineConfDownMinTxThresholdAlarm": zhoneVdslLineConfDownMinTxThresholdAlarm,
       "zhoneVdslLineConfUpMinTxThresholdAlarm": zhoneVdslLineConfUpMinTxThresholdAlarm,
       "zhoneVdslLineConfPotsBypassRelayMaxDuration": zhoneVdslLineConfPotsBypassRelayMaxDuration,
       "zhoneVdslLineConfDMTConfMode": zhoneVdslLineConfDMTConfMode,
       "zhoneVdslLineConfDownBitSwap": zhoneVdslLineConfDownBitSwap,
       "zhoneVdslLineConfUpBitSwap": zhoneVdslLineConfUpBitSwap,
       "zhoneVdslLineConfAdslAnnexMModeEnabled": zhoneVdslLineConfAdslAnnexMModeEnabled,
       "zhoneVdslLineConfAdslAnnexMPsdMask": zhoneVdslLineConfAdslAnnexMPsdMask,
       "zhoneVdslLineConfUs0BoundaryTone": zhoneVdslLineConfUs0BoundaryTone,
       "zhoneVdslLineConfDownInp": zhoneVdslLineConfDownInp,
       "zhoneVdslLineConfUpInp": zhoneVdslLineConfUpInp,
       "zhoneVdslLineConfDownMaxInterleavingDelay": zhoneVdslLineConfDownMaxInterleavingDelay,
       "zhoneVdslLineConfUpMaxInterleavingDelay": zhoneVdslLineConfUpMaxInterleavingDelay,
       "zhoneVdslLineConfDownPsdMaskEnable": zhoneVdslLineConfDownPsdMaskEnable,
       "zhoneVdslLineConfUpPsdMaskEnable": zhoneVdslLineConfUpPsdMaskEnable,
       "zhoneVdslLineConfDownPsdMaskSelect": zhoneVdslLineConfDownPsdMaskSelect,
       "zhoneVdslLineConfUpPsdMaskSelect": zhoneVdslLineConfUpPsdMaskSelect,
       "zhoneVdslLineEnableTrellisCoding": zhoneVdslLineEnableTrellisCoding,
       "zhoneVdslLineEnableRsCoding": zhoneVdslLineEnableRsCoding,
       "zhoneVdslLineConfPsdShape": zhoneVdslLineConfPsdShape,
       "zhoneVdslLineConfDownPhyRSupport": zhoneVdslLineConfDownPhyRSupport,
       "zhoneVdslLineConfUpPhyRSupport": zhoneVdslLineConfUpPhyRSupport,
       "zhoneVdslLineConfDownPhyRmaxINP": zhoneVdslLineConfDownPhyRmaxINP,
       "zhoneVdslLineConfUpPhyRmaxINP": zhoneVdslLineConfUpPhyRmaxINP,
       "zhoneVdslLineConfDownPhyRminRSoverhead": zhoneVdslLineConfDownPhyRminRSoverhead,
       "zhoneVdslLineConfUpPhyRminRSoverhead": zhoneVdslLineConfUpPhyRminRSoverhead,
       "zhoneVdslLineConfDownPhyRRtxRatio": zhoneVdslLineConfDownPhyRRtxRatio,
       "zhoneVdslLineConfUpPhyRRtxRatio": zhoneVdslLineConfUpPhyRRtxRatio,
       "zhoneVdslLineConfUpPboPsdParamA3": zhoneVdslLineConfUpPboPsdParamA3,
       "zhoneVdslLineConfUpPboPsdParamA4": zhoneVdslLineConfUpPboPsdParamA4,
       "zhoneVdslLineConfUpPboPsdParamB3": zhoneVdslLineConfUpPboPsdParamB3,
       "zhoneVdslLineConfUpPboPsdParamB4": zhoneVdslLineConfUpPboPsdParamB4,
       "zhoneVdslLineConfFallbackDefaultVpi": zhoneVdslLineConfFallbackDefaultVpi,
       "zhoneVdslLineConfFallbackDefaultVci": zhoneVdslLineConfFallbackDefaultVci,
       "zhoneVdslLineConfDownGinpSupport": zhoneVdslLineConfDownGinpSupport,
       "zhoneVdslLineConfUpGinpSupport": zhoneVdslLineConfUpGinpSupport,
       "zhoneVdslLineConfDownGinpEtrMax": zhoneVdslLineConfDownGinpEtrMax,
       "zhoneVdslLineConfUpGinpEtrMax": zhoneVdslLineConfUpGinpEtrMax,
       "zhoneVdslLineConfDownGinpEtrMin": zhoneVdslLineConfDownGinpEtrMin,
       "zhoneVdslLineConfUpGinpEtrMin": zhoneVdslLineConfUpGinpEtrMin,
       "zhoneVdslLineConfDownGinpNdrMax": zhoneVdslLineConfDownGinpNdrMax,
       "zhoneVdslLineConfUpGinpNdrMax": zhoneVdslLineConfUpGinpNdrMax,
       "zhoneVdslLineConfDownGinpShineRatio": zhoneVdslLineConfDownGinpShineRatio,
       "zhoneVdslLineConfUpGinpShineRatio": zhoneVdslLineConfUpGinpShineRatio,
       "zhoneVdslLineConfDownGinpLeftrThreshold": zhoneVdslLineConfDownGinpLeftrThreshold,
       "zhoneVdslLineConfUpGinpLeftrThreshold": zhoneVdslLineConfUpGinpLeftrThreshold,
       "zhoneVdslLineConfDownGinpMaxDelay": zhoneVdslLineConfDownGinpMaxDelay,
       "zhoneVdslLineConfUpGinpMaxDelay": zhoneVdslLineConfUpGinpMaxDelay,
       "zhoneVdslLineConfDownGinpMinDelay": zhoneVdslLineConfDownGinpMinDelay,
       "zhoneVdslLineConfUpGinpMinDelay": zhoneVdslLineConfUpGinpMinDelay,
       "zhoneVdslLineConfDownGinpMin": zhoneVdslLineConfDownGinpMin,
       "zhoneVdslLineConfUpGinpMin": zhoneVdslLineConfUpGinpMin,
       "zhoneVdslLineConfDownGinpMinRSoverhead": zhoneVdslLineConfDownGinpMinRSoverhead,
       "zhoneVdslLineConfUpGinpMinRSoverhead": zhoneVdslLineConfUpGinpMinRSoverhead,
       "zhoneVdslLineConfDownGinpReinCfg": zhoneVdslLineConfDownGinpReinCfg,
       "zhoneVdslLineConfUpGinpReinCfg": zhoneVdslLineConfUpGinpReinCfg,
       "zhoneVdslLineConfDownGinpReinFreq": zhoneVdslLineConfDownGinpReinFreq,
       "zhoneVdslLineConfUpGinpReinFreq": zhoneVdslLineConfUpGinpReinFreq,
       "zhoneVdslLineConfDownGinpRtxMode": zhoneVdslLineConfDownGinpRtxMode,
       "zhoneVdslLineConfUpGinpRtxMode": zhoneVdslLineConfUpGinpRtxMode,
       "zhoneVdslLineAlarmConfProfileTable": zhoneVdslLineAlarmConfProfileTable,
       "zhoneVdslLineAlarmConfProfileEntry": zhoneVdslLineAlarmConfProfileEntry,
       "zhoneVdslLineAlarmConfProfileName": zhoneVdslLineAlarmConfProfileName,
       "zhoneVdslLineAlarmConfThresh15MinLofs": zhoneVdslLineAlarmConfThresh15MinLofs,
       "zhoneVdslLineAlarmConfThresh15MinLoss": zhoneVdslLineAlarmConfThresh15MinLoss,
       "zhoneVdslLineAlarmConfThresh15MinLprs": zhoneVdslLineAlarmConfThresh15MinLprs,
       "zhoneVdslLineAlarmConfThresh15MinLols": zhoneVdslLineAlarmConfThresh15MinLols,
       "zhoneVdslLineAlarmConfThresh15MinESs": zhoneVdslLineAlarmConfThresh15MinESs,
       "zhoneVdslLineAlarmConfThresh15MinSESs": zhoneVdslLineAlarmConfThresh15MinSESs,
       "zhoneVdslLineAlarmConfThresh15MinUASs": zhoneVdslLineAlarmConfThresh15MinUASs,
       "zhoneVdslLineAlarmConfInitFailure": zhoneVdslLineAlarmConfInitFailure,
       "zhoneVdslLineAlarmConfProfRowStatus": zhoneVdslLineAlarmConfProfRowStatus,
       "zhoneVdslLineAlarmConfThresh1DayLofs": zhoneVdslLineAlarmConfThresh1DayLofs,
       "zhoneVdslLineAlarmConfThresh1DayLoss": zhoneVdslLineAlarmConfThresh1DayLoss,
       "zhoneVdslLineAlarmConfThresh1DayLprs": zhoneVdslLineAlarmConfThresh1DayLprs,
       "zhoneVdslLineAlarmConfThresh1DayLols": zhoneVdslLineAlarmConfThresh1DayLols,
       "zhoneVdslLineAlarmConfThresh1DayESs": zhoneVdslLineAlarmConfThresh1DayESs,
       "zhoneVdslLineAlarmConfThresh1DaySESs": zhoneVdslLineAlarmConfThresh1DaySESs,
       "zhoneVdslLineAlarmConfThresh1DayUASs": zhoneVdslLineAlarmConfThresh1DayUASs,
       "zhoneVdslLineAlarmConfThresh1DayInitFailure": zhoneVdslLineAlarmConfThresh1DayInitFailure,
       "zhoneVdslCustomNotchConfProfileTable": zhoneVdslCustomNotchConfProfileTable,
       "zhoneVdslCustomNotchConfProfileEntry": zhoneVdslCustomNotchConfProfileEntry,
       "zhoneVdslCustomNotchConfId": zhoneVdslCustomNotchConfId,
       "zhoneVdslCustomNotchConfStart": zhoneVdslCustomNotchConfStart,
       "zhoneVdslCustomNotchConfStop": zhoneVdslCustomNotchConfStop,
       "zhoneVdslVectDataTable": zhoneVdslVectDataTable,
       "zhoneVdslVectDataEntry": zhoneVdslVectDataEntry,
       "zhoneVdslVectDataEsDsCounter": zhoneVdslVectDataEsDsCounter,
       "zhoneVdslVectDataEsUsCounter": zhoneVdslVectDataEsUsCounter,
       "zhoneVdslVectDataIsDsFeValid": zhoneVdslVectDataIsDsFeValid,
       "zhoneVdslVectDataEsFeDsCounter": zhoneVdslVectDataEsFeDsCounter,
       "zhoneVdslConformance": zhoneVdslConformance,
       "zhoneVdslGroups": zhoneVdslGroups,
       "zhoneVdslGroup": zhoneVdslGroup,
       "zhoneVdslNotificationGroup": zhoneVdslNotificationGroup,
       "zhoneVdslCompliances": zhoneVdslCompliances,
       "zhoneVdslLineMibCompliance": zhoneVdslLineMibCompliance,
       "zhoneVdslMib": zhoneVdslMib}
)
