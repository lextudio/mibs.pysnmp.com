# SNMP MIB module (ACD-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-CFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:18 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdCfm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7)
)
acdCfm.setRevisions(
        ("2013-01-07 01:00",
         "2012-04-10 01:00",
         "2012-01-18 01:00",
         "2012-01-09 01:00",
         "2011-12-21 01:00",
         "2011-12-20 01:00",
         "2011-09-21 01:00",
         "2011-03-30 01:00",
         "2009-11-01 01:00",
         "2009-02-23 01:00",
         "2008-05-01 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcdCfmMepDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )



class AcdCfmMepLowestAlarmPri(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("soamAis", 6),
          ("soamAll", 1),
          ("soamErrXcon", 4),
          ("soamMacRemErrXcon", 2),
          ("soamNone", 7),
          ("soamRemErrXcon", 3),
          ("soamXcon", 5))
    )



# MIB Managed Objects in the order of their OIDs

_AcdCfmNotifications_ObjectIdentity = ObjectIdentity
acdCfmNotifications = _AcdCfmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 0)
)
_AcdCfmMIBObjects_ObjectIdentity = ObjectIdentity
acdCfmMIBObjects = _AcdCfmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1)
)
_AcdCfmDelayMeasurement_ObjectIdentity = ObjectIdentity
acdCfmDelayMeasurement = _AcdCfmDelayMeasurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1)
)
_AcdCfmDmCfgTable_Object = MibTable
acdCfmDmCfgTable = _AcdCfmDmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acdCfmDmCfgTable.setStatus("current")
_AcdCfmDmCfgEntry_Object = MibTableRow
acdCfmDmCfgEntry = _AcdCfmDmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1)
)
acdCfmDmCfgEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmDmCfgID"),
)
if mibBuilder.loadTexts:
    acdCfmDmCfgEntry.setStatus("current")
_AcdCfmDmCfgID_Type = Unsigned32
_AcdCfmDmCfgID_Object = MibTableColumn
acdCfmDmCfgID = _AcdCfmDmCfgID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 1),
    _AcdCfmDmCfgID_Type()
)
acdCfmDmCfgID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmDmCfgID.setStatus("current")
_AcdCfmDmCfgRowStatus_Type = RowStatus
_AcdCfmDmCfgRowStatus_Object = MibTableColumn
acdCfmDmCfgRowStatus = _AcdCfmDmCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 2),
    _AcdCfmDmCfgRowStatus_Type()
)
acdCfmDmCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmDmCfgRowStatus.setStatus("current")
_AcdCfmDmCfgMepIdx_Type = Unsigned32
_AcdCfmDmCfgMepIdx_Object = MibTableColumn
acdCfmDmCfgMepIdx = _AcdCfmDmCfgMepIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 3),
    _AcdCfmDmCfgMepIdx_Type()
)
acdCfmDmCfgMepIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmDmCfgMepIdx.setStatus("current")


class _AcdCfmDmCfgRemoteMepId_Type(Unsigned32):
    """Custom type acdCfmDmCfgRemoteMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AcdCfmDmCfgRemoteMepId_Type.__name__ = "Unsigned32"
_AcdCfmDmCfgRemoteMepId_Object = MibTableColumn
acdCfmDmCfgRemoteMepId = _AcdCfmDmCfgRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 4),
    _AcdCfmDmCfgRemoteMepId_Type()
)
acdCfmDmCfgRemoteMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmDmCfgRemoteMepId.setStatus("current")


class _AcdCfmDmCfgPriority_Type(Unsigned32):
    """Custom type acdCfmDmCfgPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdCfmDmCfgPriority_Type.__name__ = "Unsigned32"
_AcdCfmDmCfgPriority_Object = MibTableColumn
acdCfmDmCfgPriority = _AcdCfmDmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 5),
    _AcdCfmDmCfgPriority_Type()
)
acdCfmDmCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmDmCfgPriority.setStatus("current")


class _AcdCfmDmCfgEnable_Type(TruthValue):
    """Custom type acdCfmDmCfgEnable based on TruthValue"""


_AcdCfmDmCfgEnable_Object = MibTableColumn
acdCfmDmCfgEnable = _AcdCfmDmCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 6),
    _AcdCfmDmCfgEnable_Type()
)
acdCfmDmCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmDmCfgEnable.setStatus("current")


class _AcdCfmDmCfgInterval_Type(Unsigned32):
    """Custom type acdCfmDmCfgInterval based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_AcdCfmDmCfgInterval_Type.__name__ = "Unsigned32"
_AcdCfmDmCfgInterval_Object = MibTableColumn
acdCfmDmCfgInterval = _AcdCfmDmCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 7),
    _AcdCfmDmCfgInterval_Type()
)
acdCfmDmCfgInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmDmCfgInterval.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmDmCfgInterval.setUnits("milliseconds")


class _AcdCfmDmCfgRefPeriod_Type(Unsigned32):
    """Custom type acdCfmDmCfgRefPeriod based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_AcdCfmDmCfgRefPeriod_Type.__name__ = "Unsigned32"
_AcdCfmDmCfgRefPeriod_Object = MibTableColumn
acdCfmDmCfgRefPeriod = _AcdCfmDmCfgRefPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 8),
    _AcdCfmDmCfgRefPeriod_Type()
)
acdCfmDmCfgRefPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmDmCfgRefPeriod.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmDmCfgRefPeriod.setUnits("minutes")


class _AcdCfmDmCfgOneWayDelayEnable_Type(TruthValue):
    """Custom type acdCfmDmCfgOneWayDelayEnable based on TruthValue"""


_AcdCfmDmCfgOneWayDelayEnable_Object = MibTableColumn
acdCfmDmCfgOneWayDelayEnable = _AcdCfmDmCfgOneWayDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 9),
    _AcdCfmDmCfgOneWayDelayEnable_Type()
)
acdCfmDmCfgOneWayDelayEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmDmCfgOneWayDelayEnable.setStatus("current")


class _AcdCfmDmCfgOneWayDelayMax_Type(Unsigned32):
    """Custom type acdCfmDmCfgOneWayDelayMax based on Unsigned32"""
    defaultValue = 50


_AcdCfmDmCfgOneWayDelayMax_Object = MibTableColumn
acdCfmDmCfgOneWayDelayMax = _AcdCfmDmCfgOneWayDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 10),
    _AcdCfmDmCfgOneWayDelayMax_Type()
)
acdCfmDmCfgOneWayDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgOneWayDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmDmCfgOneWayDelayMax.setUnits("milliseconds")


class _AcdCfmDmCfgOneWayDelayThresh_Type(Unsigned32):
    """Custom type acdCfmDmCfgOneWayDelayThresh based on Unsigned32"""
    defaultValue = 4


_AcdCfmDmCfgOneWayDelayThresh_Object = MibTableColumn
acdCfmDmCfgOneWayDelayThresh = _AcdCfmDmCfgOneWayDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 11),
    _AcdCfmDmCfgOneWayDelayThresh_Type()
)
acdCfmDmCfgOneWayDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgOneWayDelayThresh.setStatus("current")


class _AcdCfmDmCfgOneWayAvgDelayThresh_Type(Unsigned32):
    """Custom type acdCfmDmCfgOneWayAvgDelayThresh based on Unsigned32"""
    defaultValue = 50


_AcdCfmDmCfgOneWayAvgDelayThresh_Object = MibTableColumn
acdCfmDmCfgOneWayAvgDelayThresh = _AcdCfmDmCfgOneWayAvgDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 12),
    _AcdCfmDmCfgOneWayAvgDelayThresh_Type()
)
acdCfmDmCfgOneWayAvgDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgOneWayAvgDelayThresh.setStatus("current")


class _AcdCfmDmCfgOneWayDvEnable_Type(TruthValue):
    """Custom type acdCfmDmCfgOneWayDvEnable based on TruthValue"""


_AcdCfmDmCfgOneWayDvEnable_Object = MibTableColumn
acdCfmDmCfgOneWayDvEnable = _AcdCfmDmCfgOneWayDvEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 13),
    _AcdCfmDmCfgOneWayDvEnable_Type()
)
acdCfmDmCfgOneWayDvEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmDmCfgOneWayDvEnable.setStatus("current")


class _AcdCfmDmCfgOneWayDvMax_Type(Unsigned32):
    """Custom type acdCfmDmCfgOneWayDvMax based on Unsigned32"""
    defaultValue = 50


_AcdCfmDmCfgOneWayDvMax_Object = MibTableColumn
acdCfmDmCfgOneWayDvMax = _AcdCfmDmCfgOneWayDvMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 14),
    _AcdCfmDmCfgOneWayDvMax_Type()
)
acdCfmDmCfgOneWayDvMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgOneWayDvMax.setStatus("current")


class _AcdCfmDmCfgOneWayDvThresh_Type(Unsigned32):
    """Custom type acdCfmDmCfgOneWayDvThresh based on Unsigned32"""
    defaultValue = 10


_AcdCfmDmCfgOneWayDvThresh_Object = MibTableColumn
acdCfmDmCfgOneWayDvThresh = _AcdCfmDmCfgOneWayDvThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 15),
    _AcdCfmDmCfgOneWayDvThresh_Type()
)
acdCfmDmCfgOneWayDvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgOneWayDvThresh.setStatus("current")


class _AcdCfmDmCfgOneWayAvgDvThresh_Type(Unsigned32):
    """Custom type acdCfmDmCfgOneWayAvgDvThresh based on Unsigned32"""
    defaultValue = 4


_AcdCfmDmCfgOneWayAvgDvThresh_Object = MibTableColumn
acdCfmDmCfgOneWayAvgDvThresh = _AcdCfmDmCfgOneWayAvgDvThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 16),
    _AcdCfmDmCfgOneWayAvgDvThresh_Type()
)
acdCfmDmCfgOneWayAvgDvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgOneWayAvgDvThresh.setStatus("current")


class _AcdCfmDmCfgTwoWayDelayEnable_Type(TruthValue):
    """Custom type acdCfmDmCfgTwoWayDelayEnable based on TruthValue"""


_AcdCfmDmCfgTwoWayDelayEnable_Object = MibTableColumn
acdCfmDmCfgTwoWayDelayEnable = _AcdCfmDmCfgTwoWayDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 17),
    _AcdCfmDmCfgTwoWayDelayEnable_Type()
)
acdCfmDmCfgTwoWayDelayEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmDmCfgTwoWayDelayEnable.setStatus("current")


class _AcdCfmDmCfgTwoWayDelayMax_Type(Unsigned32):
    """Custom type acdCfmDmCfgTwoWayDelayMax based on Unsigned32"""
    defaultValue = 100


_AcdCfmDmCfgTwoWayDelayMax_Object = MibTableColumn
acdCfmDmCfgTwoWayDelayMax = _AcdCfmDmCfgTwoWayDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 18),
    _AcdCfmDmCfgTwoWayDelayMax_Type()
)
acdCfmDmCfgTwoWayDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgTwoWayDelayMax.setStatus("current")


class _AcdCfmDmCfgTwoWayDelayThresh_Type(Unsigned32):
    """Custom type acdCfmDmCfgTwoWayDelayThresh based on Unsigned32"""
    defaultValue = 40


_AcdCfmDmCfgTwoWayDelayThresh_Object = MibTableColumn
acdCfmDmCfgTwoWayDelayThresh = _AcdCfmDmCfgTwoWayDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 19),
    _AcdCfmDmCfgTwoWayDelayThresh_Type()
)
acdCfmDmCfgTwoWayDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgTwoWayDelayThresh.setStatus("current")


class _AcdCfmDmCfgTwoWayAvgDelayThresh_Type(Unsigned32):
    """Custom type acdCfmDmCfgTwoWayAvgDelayThresh based on Unsigned32"""
    defaultValue = 100


_AcdCfmDmCfgTwoWayAvgDelayThresh_Object = MibTableColumn
acdCfmDmCfgTwoWayAvgDelayThresh = _AcdCfmDmCfgTwoWayAvgDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 20),
    _AcdCfmDmCfgTwoWayAvgDelayThresh_Type()
)
acdCfmDmCfgTwoWayAvgDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgTwoWayAvgDelayThresh.setStatus("current")


class _AcdCfmDmCfgTwoWayDvEnable_Type(TruthValue):
    """Custom type acdCfmDmCfgTwoWayDvEnable based on TruthValue"""


_AcdCfmDmCfgTwoWayDvEnable_Object = MibTableColumn
acdCfmDmCfgTwoWayDvEnable = _AcdCfmDmCfgTwoWayDvEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 21),
    _AcdCfmDmCfgTwoWayDvEnable_Type()
)
acdCfmDmCfgTwoWayDvEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmDmCfgTwoWayDvEnable.setStatus("current")


class _AcdCfmDmCfgTwoWayDvMax_Type(Unsigned32):
    """Custom type acdCfmDmCfgTwoWayDvMax based on Unsigned32"""
    defaultValue = 10


_AcdCfmDmCfgTwoWayDvMax_Object = MibTableColumn
acdCfmDmCfgTwoWayDvMax = _AcdCfmDmCfgTwoWayDvMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 22),
    _AcdCfmDmCfgTwoWayDvMax_Type()
)
acdCfmDmCfgTwoWayDvMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgTwoWayDvMax.setStatus("current")


class _AcdCfmDmCfgTwoWayDvThresh_Type(Unsigned32):
    """Custom type acdCfmDmCfgTwoWayDvThresh based on Unsigned32"""
    defaultValue = 4


_AcdCfmDmCfgTwoWayDvThresh_Object = MibTableColumn
acdCfmDmCfgTwoWayDvThresh = _AcdCfmDmCfgTwoWayDvThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 23),
    _AcdCfmDmCfgTwoWayDvThresh_Type()
)
acdCfmDmCfgTwoWayDvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgTwoWayDvThresh.setStatus("current")


class _AcdCfmDmCfgTwoWayAvgDvThresh_Type(Unsigned32):
    """Custom type acdCfmDmCfgTwoWayAvgDvThresh based on Unsigned32"""
    defaultValue = 10


_AcdCfmDmCfgTwoWayAvgDvThresh_Object = MibTableColumn
acdCfmDmCfgTwoWayAvgDvThresh = _AcdCfmDmCfgTwoWayAvgDvThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 24),
    _AcdCfmDmCfgTwoWayAvgDvThresh_Type()
)
acdCfmDmCfgTwoWayAvgDvThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgTwoWayAvgDvThresh.setStatus("current")


class _AcdCfmDmCfgName_Type(DisplayString):
    """Custom type acdCfmDmCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmDmCfgName_Type.__name__ = "DisplayString"
_AcdCfmDmCfgName_Object = MibTableColumn
acdCfmDmCfgName = _AcdCfmDmCfgName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 1, 1, 25),
    _AcdCfmDmCfgName_Type()
)
acdCfmDmCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmDmCfgName.setStatus("current")
_AcdCfmResultOneWayDelayTable_Object = MibTable
acdCfmResultOneWayDelayTable = _AcdCfmResultOneWayDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayTable.setStatus("current")
_AcdCfmResultOneWayDelayEntry_Object = MibTableRow
acdCfmResultOneWayDelayEntry = _AcdCfmResultOneWayDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1)
)
acdCfmResultOneWayDelayEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmResultOneWayDelayID"),
)
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayEntry.setStatus("current")
_AcdCfmResultOneWayDelayID_Type = Unsigned32
_AcdCfmResultOneWayDelayID_Object = MibTableColumn
acdCfmResultOneWayDelayID = _AcdCfmResultOneWayDelayID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 1),
    _AcdCfmResultOneWayDelayID_Type()
)
acdCfmResultOneWayDelayID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayID.setStatus("current")
_AcdCfmResultOneWayDelayPeriodIndex_Type = Unsigned32
_AcdCfmResultOneWayDelayPeriodIndex_Object = MibTableColumn
acdCfmResultOneWayDelayPeriodIndex = _AcdCfmResultOneWayDelayPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 2),
    _AcdCfmResultOneWayDelayPeriodIndex_Type()
)
acdCfmResultOneWayDelayPeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayPeriodIndex.setStatus("current")
_AcdCfmResultOneWayDelayIntervalStart_Type = DateAndTime
_AcdCfmResultOneWayDelayIntervalStart_Object = MibTableColumn
acdCfmResultOneWayDelayIntervalStart = _AcdCfmResultOneWayDelayIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 3),
    _AcdCfmResultOneWayDelayIntervalStart_Type()
)
acdCfmResultOneWayDelayIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayIntervalStart.setStatus("current")
_AcdCfmResultOneWayDelayValid_Type = TruthValue
_AcdCfmResultOneWayDelayValid_Object = MibTableColumn
acdCfmResultOneWayDelayValid = _AcdCfmResultOneWayDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 4),
    _AcdCfmResultOneWayDelayValid_Type()
)
acdCfmResultOneWayDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayValid.setStatus("current")
_AcdCfmResultOneWayDelayAlert_Type = TruthValue
_AcdCfmResultOneWayDelayAlert_Object = MibTableColumn
acdCfmResultOneWayDelayAlert = _AcdCfmResultOneWayDelayAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 5),
    _AcdCfmResultOneWayDelayAlert_Type()
)
acdCfmResultOneWayDelayAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayAlert.setStatus("current")
_AcdCfmResultOneWayDelayAvgAlert_Type = TruthValue
_AcdCfmResultOneWayDelayAvgAlert_Object = MibTableColumn
acdCfmResultOneWayDelayAvgAlert = _AcdCfmResultOneWayDelayAvgAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 6),
    _AcdCfmResultOneWayDelayAvgAlert_Type()
)
acdCfmResultOneWayDelayAvgAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayAvgAlert.setStatus("current")
_AcdCfmResultOneWayDelaySamples_Type = Unsigned32
_AcdCfmResultOneWayDelaySamples_Object = MibTableColumn
acdCfmResultOneWayDelaySamples = _AcdCfmResultOneWayDelaySamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 7),
    _AcdCfmResultOneWayDelaySamples_Type()
)
acdCfmResultOneWayDelaySamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelaySamples.setStatus("current")
_AcdCfmResultOneWayDelayMinValue_Type = Integer32
_AcdCfmResultOneWayDelayMinValue_Object = MibTableColumn
acdCfmResultOneWayDelayMinValue = _AcdCfmResultOneWayDelayMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 8),
    _AcdCfmResultOneWayDelayMinValue_Type()
)
acdCfmResultOneWayDelayMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayMinValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayMinValue.setUnits("microseconds")
_AcdCfmResultOneWayDelayMaxValue_Type = Integer32
_AcdCfmResultOneWayDelayMaxValue_Object = MibTableColumn
acdCfmResultOneWayDelayMaxValue = _AcdCfmResultOneWayDelayMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 9),
    _AcdCfmResultOneWayDelayMaxValue_Type()
)
acdCfmResultOneWayDelayMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayMaxValue.setUnits("microseconds")
_AcdCfmResultOneWayDelayAvgValue_Type = Integer32
_AcdCfmResultOneWayDelayAvgValue_Object = MibTableColumn
acdCfmResultOneWayDelayAvgValue = _AcdCfmResultOneWayDelayAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 10),
    _AcdCfmResultOneWayDelayAvgValue_Type()
)
acdCfmResultOneWayDelayAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayAvgValue.setUnits("microseconds")
_AcdCfmResultOneWayDelayThreshExc_Type = Unsigned32
_AcdCfmResultOneWayDelayThreshExc_Object = MibTableColumn
acdCfmResultOneWayDelayThreshExc = _AcdCfmResultOneWayDelayThreshExc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 11),
    _AcdCfmResultOneWayDelayThreshExc_Type()
)
acdCfmResultOneWayDelayThreshExc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayThreshExc.setStatus("current")
_AcdCfmResultOneWayDelayInstValue_Type = Integer32
_AcdCfmResultOneWayDelayInstValue_Object = MibTableColumn
acdCfmResultOneWayDelayInstValue = _AcdCfmResultOneWayDelayInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 12),
    _AcdCfmResultOneWayDelayInstValue_Type()
)
acdCfmResultOneWayDelayInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayInstValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayInstValue.setUnits("microseconds")


class _AcdCfmResultOneWayDelayName_Type(DisplayString):
    """Custom type acdCfmResultOneWayDelayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmResultOneWayDelayName_Type.__name__ = "DisplayString"
_AcdCfmResultOneWayDelayName_Object = MibTableColumn
acdCfmResultOneWayDelayName = _AcdCfmResultOneWayDelayName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 2, 1, 13),
    _AcdCfmResultOneWayDelayName_Type()
)
acdCfmResultOneWayDelayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayName.setStatus("current")
_AcdCfmResultOneWayDvTable_Object = MibTable
acdCfmResultOneWayDvTable = _AcdCfmResultOneWayDvTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvTable.setStatus("current")
_AcdCfmResultOneWayDvEntry_Object = MibTableRow
acdCfmResultOneWayDvEntry = _AcdCfmResultOneWayDvEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1)
)
acdCfmResultOneWayDvEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmResultOneWayDvID"),
)
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvEntry.setStatus("current")
_AcdCfmResultOneWayDvID_Type = Unsigned32
_AcdCfmResultOneWayDvID_Object = MibTableColumn
acdCfmResultOneWayDvID = _AcdCfmResultOneWayDvID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 1),
    _AcdCfmResultOneWayDvID_Type()
)
acdCfmResultOneWayDvID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvID.setStatus("current")
_AcdCfmResultOneWayDvPeriodIndex_Type = Unsigned32
_AcdCfmResultOneWayDvPeriodIndex_Object = MibTableColumn
acdCfmResultOneWayDvPeriodIndex = _AcdCfmResultOneWayDvPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 2),
    _AcdCfmResultOneWayDvPeriodIndex_Type()
)
acdCfmResultOneWayDvPeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvPeriodIndex.setStatus("current")
_AcdCfmResultOneWayDvIntervalStart_Type = DateAndTime
_AcdCfmResultOneWayDvIntervalStart_Object = MibTableColumn
acdCfmResultOneWayDvIntervalStart = _AcdCfmResultOneWayDvIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 3),
    _AcdCfmResultOneWayDvIntervalStart_Type()
)
acdCfmResultOneWayDvIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvIntervalStart.setStatus("current")
_AcdCfmResultOneWayDvValid_Type = TruthValue
_AcdCfmResultOneWayDvValid_Object = MibTableColumn
acdCfmResultOneWayDvValid = _AcdCfmResultOneWayDvValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 4),
    _AcdCfmResultOneWayDvValid_Type()
)
acdCfmResultOneWayDvValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvValid.setStatus("current")
_AcdCfmResultOneWayDvAlert_Type = TruthValue
_AcdCfmResultOneWayDvAlert_Object = MibTableColumn
acdCfmResultOneWayDvAlert = _AcdCfmResultOneWayDvAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 5),
    _AcdCfmResultOneWayDvAlert_Type()
)
acdCfmResultOneWayDvAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvAlert.setStatus("current")
_AcdCfmResultOneWayDvAvgAlert_Type = TruthValue
_AcdCfmResultOneWayDvAvgAlert_Object = MibTableColumn
acdCfmResultOneWayDvAvgAlert = _AcdCfmResultOneWayDvAvgAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 6),
    _AcdCfmResultOneWayDvAvgAlert_Type()
)
acdCfmResultOneWayDvAvgAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvAvgAlert.setStatus("current")
_AcdCfmResultOneWayDvSamples_Type = Unsigned32
_AcdCfmResultOneWayDvSamples_Object = MibTableColumn
acdCfmResultOneWayDvSamples = _AcdCfmResultOneWayDvSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 7),
    _AcdCfmResultOneWayDvSamples_Type()
)
acdCfmResultOneWayDvSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvSamples.setStatus("current")
_AcdCfmResultOneWayDvMinValue_Type = Integer32
_AcdCfmResultOneWayDvMinValue_Object = MibTableColumn
acdCfmResultOneWayDvMinValue = _AcdCfmResultOneWayDvMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 8),
    _AcdCfmResultOneWayDvMinValue_Type()
)
acdCfmResultOneWayDvMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvMinValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvMinValue.setUnits("microseconds")
_AcdCfmResultOneWayDvMaxValue_Type = Integer32
_AcdCfmResultOneWayDvMaxValue_Object = MibTableColumn
acdCfmResultOneWayDvMaxValue = _AcdCfmResultOneWayDvMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 9),
    _AcdCfmResultOneWayDvMaxValue_Type()
)
acdCfmResultOneWayDvMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvMaxValue.setUnits("microseconds")
_AcdCfmResultOneWayDvAvgValue_Type = Integer32
_AcdCfmResultOneWayDvAvgValue_Object = MibTableColumn
acdCfmResultOneWayDvAvgValue = _AcdCfmResultOneWayDvAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 10),
    _AcdCfmResultOneWayDvAvgValue_Type()
)
acdCfmResultOneWayDvAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvAvgValue.setUnits("microseconds")
_AcdCfmResultOneWayDvThreshExc_Type = Unsigned32
_AcdCfmResultOneWayDvThreshExc_Object = MibTableColumn
acdCfmResultOneWayDvThreshExc = _AcdCfmResultOneWayDvThreshExc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 11),
    _AcdCfmResultOneWayDvThreshExc_Type()
)
acdCfmResultOneWayDvThreshExc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvThreshExc.setStatus("current")
_AcdCfmResultOneWayDvInstValue_Type = Integer32
_AcdCfmResultOneWayDvInstValue_Object = MibTableColumn
acdCfmResultOneWayDvInstValue = _AcdCfmResultOneWayDvInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 12),
    _AcdCfmResultOneWayDvInstValue_Type()
)
acdCfmResultOneWayDvInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvInstValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvInstValue.setUnits("microseconds")


class _AcdCfmResultOneWayDvName_Type(DisplayString):
    """Custom type acdCfmResultOneWayDvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmResultOneWayDvName_Type.__name__ = "DisplayString"
_AcdCfmResultOneWayDvName_Object = MibTableColumn
acdCfmResultOneWayDvName = _AcdCfmResultOneWayDvName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 3, 1, 13),
    _AcdCfmResultOneWayDvName_Type()
)
acdCfmResultOneWayDvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvName.setStatus("current")
_AcdCfmResultTwoWayDelayTable_Object = MibTable
acdCfmResultTwoWayDelayTable = _AcdCfmResultTwoWayDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayTable.setStatus("current")
_AcdCfmResultTwoWayDelayEntry_Object = MibTableRow
acdCfmResultTwoWayDelayEntry = _AcdCfmResultTwoWayDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1)
)
acdCfmResultTwoWayDelayEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmResultTwoWayDelayID"),
)
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayEntry.setStatus("current")
_AcdCfmResultTwoWayDelayID_Type = Unsigned32
_AcdCfmResultTwoWayDelayID_Object = MibTableColumn
acdCfmResultTwoWayDelayID = _AcdCfmResultTwoWayDelayID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 1),
    _AcdCfmResultTwoWayDelayID_Type()
)
acdCfmResultTwoWayDelayID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayID.setStatus("current")
_AcdCfmResultTwoWayDelayPeriodIndex_Type = Unsigned32
_AcdCfmResultTwoWayDelayPeriodIndex_Object = MibTableColumn
acdCfmResultTwoWayDelayPeriodIndex = _AcdCfmResultTwoWayDelayPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 2),
    _AcdCfmResultTwoWayDelayPeriodIndex_Type()
)
acdCfmResultTwoWayDelayPeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayPeriodIndex.setStatus("current")
_AcdCfmResultTwoWayDelayIntervalStart_Type = DateAndTime
_AcdCfmResultTwoWayDelayIntervalStart_Object = MibTableColumn
acdCfmResultTwoWayDelayIntervalStart = _AcdCfmResultTwoWayDelayIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 3),
    _AcdCfmResultTwoWayDelayIntervalStart_Type()
)
acdCfmResultTwoWayDelayIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayIntervalStart.setStatus("current")
_AcdCfmResultTwoWayDelayValid_Type = TruthValue
_AcdCfmResultTwoWayDelayValid_Object = MibTableColumn
acdCfmResultTwoWayDelayValid = _AcdCfmResultTwoWayDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 4),
    _AcdCfmResultTwoWayDelayValid_Type()
)
acdCfmResultTwoWayDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayValid.setStatus("current")
_AcdCfmResultTwoWayDelayAlert_Type = TruthValue
_AcdCfmResultTwoWayDelayAlert_Object = MibTableColumn
acdCfmResultTwoWayDelayAlert = _AcdCfmResultTwoWayDelayAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 5),
    _AcdCfmResultTwoWayDelayAlert_Type()
)
acdCfmResultTwoWayDelayAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayAlert.setStatus("current")
_AcdCfmResultTwoWayDelayAvgAlert_Type = TruthValue
_AcdCfmResultTwoWayDelayAvgAlert_Object = MibTableColumn
acdCfmResultTwoWayDelayAvgAlert = _AcdCfmResultTwoWayDelayAvgAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 6),
    _AcdCfmResultTwoWayDelayAvgAlert_Type()
)
acdCfmResultTwoWayDelayAvgAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayAvgAlert.setStatus("current")
_AcdCfmResultTwoWayDelaySamples_Type = Unsigned32
_AcdCfmResultTwoWayDelaySamples_Object = MibTableColumn
acdCfmResultTwoWayDelaySamples = _AcdCfmResultTwoWayDelaySamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 7),
    _AcdCfmResultTwoWayDelaySamples_Type()
)
acdCfmResultTwoWayDelaySamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelaySamples.setStatus("current")
_AcdCfmResultTwoWayDelayMinValue_Type = Integer32
_AcdCfmResultTwoWayDelayMinValue_Object = MibTableColumn
acdCfmResultTwoWayDelayMinValue = _AcdCfmResultTwoWayDelayMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 8),
    _AcdCfmResultTwoWayDelayMinValue_Type()
)
acdCfmResultTwoWayDelayMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayMinValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayMinValue.setUnits("microseconds")
_AcdCfmResultTwoWayDelayMaxValue_Type = Integer32
_AcdCfmResultTwoWayDelayMaxValue_Object = MibTableColumn
acdCfmResultTwoWayDelayMaxValue = _AcdCfmResultTwoWayDelayMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 9),
    _AcdCfmResultTwoWayDelayMaxValue_Type()
)
acdCfmResultTwoWayDelayMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayMaxValue.setUnits("microseconds")
_AcdCfmResultTwoWayDelayAvgValue_Type = Integer32
_AcdCfmResultTwoWayDelayAvgValue_Object = MibTableColumn
acdCfmResultTwoWayDelayAvgValue = _AcdCfmResultTwoWayDelayAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 10),
    _AcdCfmResultTwoWayDelayAvgValue_Type()
)
acdCfmResultTwoWayDelayAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayAvgValue.setUnits("microseconds")
_AcdCfmResultTwoWayDelayThreshExc_Type = Unsigned32
_AcdCfmResultTwoWayDelayThreshExc_Object = MibTableColumn
acdCfmResultTwoWayDelayThreshExc = _AcdCfmResultTwoWayDelayThreshExc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 11),
    _AcdCfmResultTwoWayDelayThreshExc_Type()
)
acdCfmResultTwoWayDelayThreshExc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayThreshExc.setStatus("current")
_AcdCfmResultTwoWayDelayInstValue_Type = Integer32
_AcdCfmResultTwoWayDelayInstValue_Object = MibTableColumn
acdCfmResultTwoWayDelayInstValue = _AcdCfmResultTwoWayDelayInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 12),
    _AcdCfmResultTwoWayDelayInstValue_Type()
)
acdCfmResultTwoWayDelayInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayInstValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayInstValue.setUnits("microseconds")


class _AcdCfmResultTwoWayDelayName_Type(DisplayString):
    """Custom type acdCfmResultTwoWayDelayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmResultTwoWayDelayName_Type.__name__ = "DisplayString"
_AcdCfmResultTwoWayDelayName_Object = MibTableColumn
acdCfmResultTwoWayDelayName = _AcdCfmResultTwoWayDelayName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 4, 1, 13),
    _AcdCfmResultTwoWayDelayName_Type()
)
acdCfmResultTwoWayDelayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayName.setStatus("current")
_AcdCfmResultTwoWayDvTable_Object = MibTable
acdCfmResultTwoWayDvTable = _AcdCfmResultTwoWayDvTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5)
)
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvTable.setStatus("current")
_AcdCfmResultTwoWayDvEntry_Object = MibTableRow
acdCfmResultTwoWayDvEntry = _AcdCfmResultTwoWayDvEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1)
)
acdCfmResultTwoWayDvEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmResultTwoWayDvID"),
)
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvEntry.setStatus("current")
_AcdCfmResultTwoWayDvID_Type = Unsigned32
_AcdCfmResultTwoWayDvID_Object = MibTableColumn
acdCfmResultTwoWayDvID = _AcdCfmResultTwoWayDvID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 1),
    _AcdCfmResultTwoWayDvID_Type()
)
acdCfmResultTwoWayDvID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvID.setStatus("current")
_AcdCfmResultTwoWayDvPeriodIndex_Type = Unsigned32
_AcdCfmResultTwoWayDvPeriodIndex_Object = MibTableColumn
acdCfmResultTwoWayDvPeriodIndex = _AcdCfmResultTwoWayDvPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 2),
    _AcdCfmResultTwoWayDvPeriodIndex_Type()
)
acdCfmResultTwoWayDvPeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvPeriodIndex.setStatus("current")
_AcdCfmResultTwoWayDvIntervalStart_Type = DateAndTime
_AcdCfmResultTwoWayDvIntervalStart_Object = MibTableColumn
acdCfmResultTwoWayDvIntervalStart = _AcdCfmResultTwoWayDvIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 3),
    _AcdCfmResultTwoWayDvIntervalStart_Type()
)
acdCfmResultTwoWayDvIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvIntervalStart.setStatus("current")
_AcdCfmResultTwoWayDvValid_Type = TruthValue
_AcdCfmResultTwoWayDvValid_Object = MibTableColumn
acdCfmResultTwoWayDvValid = _AcdCfmResultTwoWayDvValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 4),
    _AcdCfmResultTwoWayDvValid_Type()
)
acdCfmResultTwoWayDvValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvValid.setStatus("current")
_AcdCfmResultTwoWayDvAlert_Type = TruthValue
_AcdCfmResultTwoWayDvAlert_Object = MibTableColumn
acdCfmResultTwoWayDvAlert = _AcdCfmResultTwoWayDvAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 5),
    _AcdCfmResultTwoWayDvAlert_Type()
)
acdCfmResultTwoWayDvAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvAlert.setStatus("current")
_AcdCfmResultTwoWayDvAvgAlert_Type = TruthValue
_AcdCfmResultTwoWayDvAvgAlert_Object = MibTableColumn
acdCfmResultTwoWayDvAvgAlert = _AcdCfmResultTwoWayDvAvgAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 6),
    _AcdCfmResultTwoWayDvAvgAlert_Type()
)
acdCfmResultTwoWayDvAvgAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvAvgAlert.setStatus("current")
_AcdCfmResultTwoWayDvSamples_Type = Unsigned32
_AcdCfmResultTwoWayDvSamples_Object = MibTableColumn
acdCfmResultTwoWayDvSamples = _AcdCfmResultTwoWayDvSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 7),
    _AcdCfmResultTwoWayDvSamples_Type()
)
acdCfmResultTwoWayDvSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvSamples.setStatus("current")
_AcdCfmResultTwoWayDvMinValue_Type = Integer32
_AcdCfmResultTwoWayDvMinValue_Object = MibTableColumn
acdCfmResultTwoWayDvMinValue = _AcdCfmResultTwoWayDvMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 8),
    _AcdCfmResultTwoWayDvMinValue_Type()
)
acdCfmResultTwoWayDvMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvMinValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvMinValue.setUnits("microseconds")
_AcdCfmResultTwoWayDvMaxValue_Type = Integer32
_AcdCfmResultTwoWayDvMaxValue_Object = MibTableColumn
acdCfmResultTwoWayDvMaxValue = _AcdCfmResultTwoWayDvMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 9),
    _AcdCfmResultTwoWayDvMaxValue_Type()
)
acdCfmResultTwoWayDvMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvMaxValue.setUnits("microseconds")
_AcdCfmResultTwoWayDvAvgValue_Type = Integer32
_AcdCfmResultTwoWayDvAvgValue_Object = MibTableColumn
acdCfmResultTwoWayDvAvgValue = _AcdCfmResultTwoWayDvAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 10),
    _AcdCfmResultTwoWayDvAvgValue_Type()
)
acdCfmResultTwoWayDvAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvAvgValue.setUnits("microseconds")
_AcdCfmResultTwoWayDvThreshExc_Type = Unsigned32
_AcdCfmResultTwoWayDvThreshExc_Object = MibTableColumn
acdCfmResultTwoWayDvThreshExc = _AcdCfmResultTwoWayDvThreshExc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 11),
    _AcdCfmResultTwoWayDvThreshExc_Type()
)
acdCfmResultTwoWayDvThreshExc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvThreshExc.setStatus("current")
_AcdCfmResultTwoWayDvInstValue_Type = Integer32
_AcdCfmResultTwoWayDvInstValue_Object = MibTableColumn
acdCfmResultTwoWayDvInstValue = _AcdCfmResultTwoWayDvInstValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 12),
    _AcdCfmResultTwoWayDvInstValue_Type()
)
acdCfmResultTwoWayDvInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvInstValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvInstValue.setUnits("microseconds")


class _AcdCfmResultTwoWayDvName_Type(DisplayString):
    """Custom type acdCfmResultTwoWayDvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmResultTwoWayDvName_Type.__name__ = "DisplayString"
_AcdCfmResultTwoWayDvName_Object = MibTableColumn
acdCfmResultTwoWayDvName = _AcdCfmResultTwoWayDvName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 5, 1, 13),
    _AcdCfmResultTwoWayDvName_Type()
)
acdCfmResultTwoWayDvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvName.setStatus("current")
_AcdCfmHistResultOneWayDelayTable_Object = MibTable
acdCfmHistResultOneWayDelayTable = _AcdCfmHistResultOneWayDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6)
)
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayTable.setStatus("current")
_AcdCfmHistResultOneWayDelayEntry_Object = MibTableRow
acdCfmHistResultOneWayDelayEntry = _AcdCfmHistResultOneWayDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6, 1)
)
acdCfmHistResultOneWayDelayEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmHistResultOneWayDelayID"),
    (0, "ACD-CFM-MIB", "acdCfmHistResultOneWayDelaySampleIndex"),
)
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayEntry.setStatus("current")
_AcdCfmHistResultOneWayDelayID_Type = Unsigned32
_AcdCfmHistResultOneWayDelayID_Object = MibTableColumn
acdCfmHistResultOneWayDelayID = _AcdCfmHistResultOneWayDelayID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6, 1, 1),
    _AcdCfmHistResultOneWayDelayID_Type()
)
acdCfmHistResultOneWayDelayID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayID.setStatus("current")
_AcdCfmHistResultOneWayDelaySampleIndex_Type = Unsigned32
_AcdCfmHistResultOneWayDelaySampleIndex_Object = MibTableColumn
acdCfmHistResultOneWayDelaySampleIndex = _AcdCfmHistResultOneWayDelaySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6, 1, 2),
    _AcdCfmHistResultOneWayDelaySampleIndex_Type()
)
acdCfmHistResultOneWayDelaySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelaySampleIndex.setStatus("current")


class _AcdCfmHistResultOneWayDelayStatus_Type(Integer32):
    """Custom type acdCfmHistResultOneWayDelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AcdCfmHistResultOneWayDelayStatus_Type.__name__ = "Integer32"
_AcdCfmHistResultOneWayDelayStatus_Object = MibTableColumn
acdCfmHistResultOneWayDelayStatus = _AcdCfmHistResultOneWayDelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6, 1, 3),
    _AcdCfmHistResultOneWayDelayStatus_Type()
)
acdCfmHistResultOneWayDelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayStatus.setStatus("current")
_AcdCfmHistResultOneWayDelayDuration_Type = Unsigned32
_AcdCfmHistResultOneWayDelayDuration_Object = MibTableColumn
acdCfmHistResultOneWayDelayDuration = _AcdCfmHistResultOneWayDelayDuration_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6, 1, 4),
    _AcdCfmHistResultOneWayDelayDuration_Type()
)
acdCfmHistResultOneWayDelayDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayDuration.setStatus("current")
_AcdCfmHistResultOneWayDelayIntervalEnd_Type = DateAndTime
_AcdCfmHistResultOneWayDelayIntervalEnd_Object = MibTableColumn
acdCfmHistResultOneWayDelayIntervalEnd = _AcdCfmHistResultOneWayDelayIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6, 1, 5),
    _AcdCfmHistResultOneWayDelayIntervalEnd_Type()
)
acdCfmHistResultOneWayDelayIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayIntervalEnd.setStatus("current")
_AcdCfmHistResultOneWayDelaySamples_Type = Unsigned32
_AcdCfmHistResultOneWayDelaySamples_Object = MibTableColumn
acdCfmHistResultOneWayDelaySamples = _AcdCfmHistResultOneWayDelaySamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6, 1, 6),
    _AcdCfmHistResultOneWayDelaySamples_Type()
)
acdCfmHistResultOneWayDelaySamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelaySamples.setStatus("current")
_AcdCfmHistResultOneWayDelayMinValue_Type = Integer32
_AcdCfmHistResultOneWayDelayMinValue_Object = MibTableColumn
acdCfmHistResultOneWayDelayMinValue = _AcdCfmHistResultOneWayDelayMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6, 1, 7),
    _AcdCfmHistResultOneWayDelayMinValue_Type()
)
acdCfmHistResultOneWayDelayMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayMinValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayMinValue.setUnits("microseconds")
_AcdCfmHistResultOneWayDelayMaxValue_Type = Integer32
_AcdCfmHistResultOneWayDelayMaxValue_Object = MibTableColumn
acdCfmHistResultOneWayDelayMaxValue = _AcdCfmHistResultOneWayDelayMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6, 1, 8),
    _AcdCfmHistResultOneWayDelayMaxValue_Type()
)
acdCfmHistResultOneWayDelayMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayMaxValue.setUnits("microseconds")
_AcdCfmHistResultOneWayDelayAvgValue_Type = Integer32
_AcdCfmHistResultOneWayDelayAvgValue_Object = MibTableColumn
acdCfmHistResultOneWayDelayAvgValue = _AcdCfmHistResultOneWayDelayAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6, 1, 9),
    _AcdCfmHistResultOneWayDelayAvgValue_Type()
)
acdCfmHistResultOneWayDelayAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayAvgValue.setUnits("microseconds")
_AcdCfmHistResultOneWayDelayThreshExc_Type = Unsigned32
_AcdCfmHistResultOneWayDelayThreshExc_Object = MibTableColumn
acdCfmHistResultOneWayDelayThreshExc = _AcdCfmHistResultOneWayDelayThreshExc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6, 1, 10),
    _AcdCfmHistResultOneWayDelayThreshExc_Type()
)
acdCfmHistResultOneWayDelayThreshExc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayThreshExc.setStatus("current")


class _AcdCfmHistResultOneWayDelayName_Type(DisplayString):
    """Custom type acdCfmHistResultOneWayDelayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmHistResultOneWayDelayName_Type.__name__ = "DisplayString"
_AcdCfmHistResultOneWayDelayName_Object = MibTableColumn
acdCfmHistResultOneWayDelayName = _AcdCfmHistResultOneWayDelayName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 6, 1, 11),
    _AcdCfmHistResultOneWayDelayName_Type()
)
acdCfmHistResultOneWayDelayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayName.setStatus("current")
_AcdCfmHistResultOneWayDvTable_Object = MibTable
acdCfmHistResultOneWayDvTable = _AcdCfmHistResultOneWayDvTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7)
)
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvTable.setStatus("current")
_AcdCfmHistResultOneWayDvEntry_Object = MibTableRow
acdCfmHistResultOneWayDvEntry = _AcdCfmHistResultOneWayDvEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7, 1)
)
acdCfmHistResultOneWayDvEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmHistResultOneWayDvID"),
    (0, "ACD-CFM-MIB", "acdCfmHistResultOneWayDvSampleIndex"),
)
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvEntry.setStatus("current")
_AcdCfmHistResultOneWayDvID_Type = Unsigned32
_AcdCfmHistResultOneWayDvID_Object = MibTableColumn
acdCfmHistResultOneWayDvID = _AcdCfmHistResultOneWayDvID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7, 1, 1),
    _AcdCfmHistResultOneWayDvID_Type()
)
acdCfmHistResultOneWayDvID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvID.setStatus("current")
_AcdCfmHistResultOneWayDvSampleIndex_Type = Unsigned32
_AcdCfmHistResultOneWayDvSampleIndex_Object = MibTableColumn
acdCfmHistResultOneWayDvSampleIndex = _AcdCfmHistResultOneWayDvSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7, 1, 2),
    _AcdCfmHistResultOneWayDvSampleIndex_Type()
)
acdCfmHistResultOneWayDvSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvSampleIndex.setStatus("current")


class _AcdCfmHistResultOneWayDvStatus_Type(Integer32):
    """Custom type acdCfmHistResultOneWayDvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AcdCfmHistResultOneWayDvStatus_Type.__name__ = "Integer32"
_AcdCfmHistResultOneWayDvStatus_Object = MibTableColumn
acdCfmHistResultOneWayDvStatus = _AcdCfmHistResultOneWayDvStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7, 1, 3),
    _AcdCfmHistResultOneWayDvStatus_Type()
)
acdCfmHistResultOneWayDvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvStatus.setStatus("current")
_AcdCfmHistResultOneWayDvDuration_Type = Unsigned32
_AcdCfmHistResultOneWayDvDuration_Object = MibTableColumn
acdCfmHistResultOneWayDvDuration = _AcdCfmHistResultOneWayDvDuration_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7, 1, 4),
    _AcdCfmHistResultOneWayDvDuration_Type()
)
acdCfmHistResultOneWayDvDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvDuration.setStatus("current")
_AcdCfmHistResultOneWayDvIntervalEnd_Type = DateAndTime
_AcdCfmHistResultOneWayDvIntervalEnd_Object = MibTableColumn
acdCfmHistResultOneWayDvIntervalEnd = _AcdCfmHistResultOneWayDvIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7, 1, 5),
    _AcdCfmHistResultOneWayDvIntervalEnd_Type()
)
acdCfmHistResultOneWayDvIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvIntervalEnd.setStatus("current")
_AcdCfmHistResultOneWayDvSamples_Type = Unsigned32
_AcdCfmHistResultOneWayDvSamples_Object = MibTableColumn
acdCfmHistResultOneWayDvSamples = _AcdCfmHistResultOneWayDvSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7, 1, 6),
    _AcdCfmHistResultOneWayDvSamples_Type()
)
acdCfmHistResultOneWayDvSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvSamples.setStatus("current")
_AcdCfmHistResultOneWayDvMinValue_Type = Integer32
_AcdCfmHistResultOneWayDvMinValue_Object = MibTableColumn
acdCfmHistResultOneWayDvMinValue = _AcdCfmHistResultOneWayDvMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7, 1, 7),
    _AcdCfmHistResultOneWayDvMinValue_Type()
)
acdCfmHistResultOneWayDvMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvMinValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvMinValue.setUnits("microseconds")
_AcdCfmHistResultOneWayDvMaxValue_Type = Integer32
_AcdCfmHistResultOneWayDvMaxValue_Object = MibTableColumn
acdCfmHistResultOneWayDvMaxValue = _AcdCfmHistResultOneWayDvMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7, 1, 8),
    _AcdCfmHistResultOneWayDvMaxValue_Type()
)
acdCfmHistResultOneWayDvMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvMaxValue.setUnits("microseconds")
_AcdCfmHistResultOneWayDvAvgValue_Type = Integer32
_AcdCfmHistResultOneWayDvAvgValue_Object = MibTableColumn
acdCfmHistResultOneWayDvAvgValue = _AcdCfmHistResultOneWayDvAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7, 1, 9),
    _AcdCfmHistResultOneWayDvAvgValue_Type()
)
acdCfmHistResultOneWayDvAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvAvgValue.setUnits("microseconds")
_AcdCfmHistResultOneWayDvThreshExc_Type = Unsigned32
_AcdCfmHistResultOneWayDvThreshExc_Object = MibTableColumn
acdCfmHistResultOneWayDvThreshExc = _AcdCfmHistResultOneWayDvThreshExc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7, 1, 10),
    _AcdCfmHistResultOneWayDvThreshExc_Type()
)
acdCfmHistResultOneWayDvThreshExc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvThreshExc.setStatus("current")


class _AcdCfmHistResultOneWayDvName_Type(DisplayString):
    """Custom type acdCfmHistResultOneWayDvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmHistResultOneWayDvName_Type.__name__ = "DisplayString"
_AcdCfmHistResultOneWayDvName_Object = MibTableColumn
acdCfmHistResultOneWayDvName = _AcdCfmHistResultOneWayDvName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 7, 1, 11),
    _AcdCfmHistResultOneWayDvName_Type()
)
acdCfmHistResultOneWayDvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvName.setStatus("current")
_AcdCfmHistResultTwoWayDelayTable_Object = MibTable
acdCfmHistResultTwoWayDelayTable = _AcdCfmHistResultTwoWayDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8)
)
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayTable.setStatus("current")
_AcdCfmHistResultTwoWayDelayEntry_Object = MibTableRow
acdCfmHistResultTwoWayDelayEntry = _AcdCfmHistResultTwoWayDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8, 1)
)
acdCfmHistResultTwoWayDelayEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmHistResultTwoWayDelayID"),
    (0, "ACD-CFM-MIB", "acdCfmHistResultTwoWayDelaySampleIndex"),
)
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayEntry.setStatus("current")
_AcdCfmHistResultTwoWayDelayID_Type = Unsigned32
_AcdCfmHistResultTwoWayDelayID_Object = MibTableColumn
acdCfmHistResultTwoWayDelayID = _AcdCfmHistResultTwoWayDelayID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8, 1, 1),
    _AcdCfmHistResultTwoWayDelayID_Type()
)
acdCfmHistResultTwoWayDelayID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayID.setStatus("current")
_AcdCfmHistResultTwoWayDelaySampleIndex_Type = Unsigned32
_AcdCfmHistResultTwoWayDelaySampleIndex_Object = MibTableColumn
acdCfmHistResultTwoWayDelaySampleIndex = _AcdCfmHistResultTwoWayDelaySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8, 1, 2),
    _AcdCfmHistResultTwoWayDelaySampleIndex_Type()
)
acdCfmHistResultTwoWayDelaySampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelaySampleIndex.setStatus("current")


class _AcdCfmHistResultTwoWayDelayStatus_Type(Integer32):
    """Custom type acdCfmHistResultTwoWayDelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AcdCfmHistResultTwoWayDelayStatus_Type.__name__ = "Integer32"
_AcdCfmHistResultTwoWayDelayStatus_Object = MibTableColumn
acdCfmHistResultTwoWayDelayStatus = _AcdCfmHistResultTwoWayDelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8, 1, 3),
    _AcdCfmHistResultTwoWayDelayStatus_Type()
)
acdCfmHistResultTwoWayDelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayStatus.setStatus("current")
_AcdCfmHistResultTwoWayDelayDuration_Type = Unsigned32
_AcdCfmHistResultTwoWayDelayDuration_Object = MibTableColumn
acdCfmHistResultTwoWayDelayDuration = _AcdCfmHistResultTwoWayDelayDuration_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8, 1, 4),
    _AcdCfmHistResultTwoWayDelayDuration_Type()
)
acdCfmHistResultTwoWayDelayDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayDuration.setStatus("current")
_AcdCfmHistResultTwoWayDelayIntervalEnd_Type = DateAndTime
_AcdCfmHistResultTwoWayDelayIntervalEnd_Object = MibTableColumn
acdCfmHistResultTwoWayDelayIntervalEnd = _AcdCfmHistResultTwoWayDelayIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8, 1, 5),
    _AcdCfmHistResultTwoWayDelayIntervalEnd_Type()
)
acdCfmHistResultTwoWayDelayIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayIntervalEnd.setStatus("current")
_AcdCfmHistResultTwoWayDelaySamples_Type = Unsigned32
_AcdCfmHistResultTwoWayDelaySamples_Object = MibTableColumn
acdCfmHistResultTwoWayDelaySamples = _AcdCfmHistResultTwoWayDelaySamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8, 1, 6),
    _AcdCfmHistResultTwoWayDelaySamples_Type()
)
acdCfmHistResultTwoWayDelaySamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelaySamples.setStatus("current")
_AcdCfmHistResultTwoWayDelayMinValue_Type = Integer32
_AcdCfmHistResultTwoWayDelayMinValue_Object = MibTableColumn
acdCfmHistResultTwoWayDelayMinValue = _AcdCfmHistResultTwoWayDelayMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8, 1, 7),
    _AcdCfmHistResultTwoWayDelayMinValue_Type()
)
acdCfmHistResultTwoWayDelayMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayMinValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayMinValue.setUnits("microseconds")
_AcdCfmHistResultTwoWayDelayMaxValue_Type = Integer32
_AcdCfmHistResultTwoWayDelayMaxValue_Object = MibTableColumn
acdCfmHistResultTwoWayDelayMaxValue = _AcdCfmHistResultTwoWayDelayMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8, 1, 8),
    _AcdCfmHistResultTwoWayDelayMaxValue_Type()
)
acdCfmHistResultTwoWayDelayMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayMaxValue.setUnits("microseconds")
_AcdCfmHistResultTwoWayDelayAvgValue_Type = Integer32
_AcdCfmHistResultTwoWayDelayAvgValue_Object = MibTableColumn
acdCfmHistResultTwoWayDelayAvgValue = _AcdCfmHistResultTwoWayDelayAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8, 1, 9),
    _AcdCfmHistResultTwoWayDelayAvgValue_Type()
)
acdCfmHistResultTwoWayDelayAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayAvgValue.setUnits("microseconds")
_AcdCfmHistResultTwoWayDelayThreshExc_Type = Unsigned32
_AcdCfmHistResultTwoWayDelayThreshExc_Object = MibTableColumn
acdCfmHistResultTwoWayDelayThreshExc = _AcdCfmHistResultTwoWayDelayThreshExc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8, 1, 10),
    _AcdCfmHistResultTwoWayDelayThreshExc_Type()
)
acdCfmHistResultTwoWayDelayThreshExc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayThreshExc.setStatus("current")


class _AcdCfmHistResultTwoWayDelayName_Type(DisplayString):
    """Custom type acdCfmHistResultTwoWayDelayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmHistResultTwoWayDelayName_Type.__name__ = "DisplayString"
_AcdCfmHistResultTwoWayDelayName_Object = MibTableColumn
acdCfmHistResultTwoWayDelayName = _AcdCfmHistResultTwoWayDelayName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 8, 1, 11),
    _AcdCfmHistResultTwoWayDelayName_Type()
)
acdCfmHistResultTwoWayDelayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayName.setStatus("current")
_AcdCfmHistResultTwoWayDvTable_Object = MibTable
acdCfmHistResultTwoWayDvTable = _AcdCfmHistResultTwoWayDvTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9)
)
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvTable.setStatus("current")
_AcdCfmHistResultTwoWayDvEntry_Object = MibTableRow
acdCfmHistResultTwoWayDvEntry = _AcdCfmHistResultTwoWayDvEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9, 1)
)
acdCfmHistResultTwoWayDvEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmHistResultTwoWayDvID"),
    (0, "ACD-CFM-MIB", "acdCfmHistResultTwoWayDvSampleIndex"),
)
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvEntry.setStatus("current")
_AcdCfmHistResultTwoWayDvID_Type = Unsigned32
_AcdCfmHistResultTwoWayDvID_Object = MibTableColumn
acdCfmHistResultTwoWayDvID = _AcdCfmHistResultTwoWayDvID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9, 1, 1),
    _AcdCfmHistResultTwoWayDvID_Type()
)
acdCfmHistResultTwoWayDvID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvID.setStatus("current")
_AcdCfmHistResultTwoWayDvSampleIndex_Type = Unsigned32
_AcdCfmHistResultTwoWayDvSampleIndex_Object = MibTableColumn
acdCfmHistResultTwoWayDvSampleIndex = _AcdCfmHistResultTwoWayDvSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9, 1, 2),
    _AcdCfmHistResultTwoWayDvSampleIndex_Type()
)
acdCfmHistResultTwoWayDvSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvSampleIndex.setStatus("current")


class _AcdCfmHistResultTwoWayDvStatus_Type(Integer32):
    """Custom type acdCfmHistResultTwoWayDvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AcdCfmHistResultTwoWayDvStatus_Type.__name__ = "Integer32"
_AcdCfmHistResultTwoWayDvStatus_Object = MibTableColumn
acdCfmHistResultTwoWayDvStatus = _AcdCfmHistResultTwoWayDvStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9, 1, 3),
    _AcdCfmHistResultTwoWayDvStatus_Type()
)
acdCfmHistResultTwoWayDvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvStatus.setStatus("current")
_AcdCfmHistResultTwoWayDvDuration_Type = Unsigned32
_AcdCfmHistResultTwoWayDvDuration_Object = MibTableColumn
acdCfmHistResultTwoWayDvDuration = _AcdCfmHistResultTwoWayDvDuration_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9, 1, 4),
    _AcdCfmHistResultTwoWayDvDuration_Type()
)
acdCfmHistResultTwoWayDvDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvDuration.setStatus("current")
_AcdCfmHistResultTwoWayDvIntervalEnd_Type = DateAndTime
_AcdCfmHistResultTwoWayDvIntervalEnd_Object = MibTableColumn
acdCfmHistResultTwoWayDvIntervalEnd = _AcdCfmHistResultTwoWayDvIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9, 1, 5),
    _AcdCfmHistResultTwoWayDvIntervalEnd_Type()
)
acdCfmHistResultTwoWayDvIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvIntervalEnd.setStatus("current")
_AcdCfmHistResultTwoWayDvSamples_Type = Unsigned32
_AcdCfmHistResultTwoWayDvSamples_Object = MibTableColumn
acdCfmHistResultTwoWayDvSamples = _AcdCfmHistResultTwoWayDvSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9, 1, 6),
    _AcdCfmHistResultTwoWayDvSamples_Type()
)
acdCfmHistResultTwoWayDvSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvSamples.setStatus("current")
_AcdCfmHistResultTwoWayDvMinValue_Type = Integer32
_AcdCfmHistResultTwoWayDvMinValue_Object = MibTableColumn
acdCfmHistResultTwoWayDvMinValue = _AcdCfmHistResultTwoWayDvMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9, 1, 7),
    _AcdCfmHistResultTwoWayDvMinValue_Type()
)
acdCfmHistResultTwoWayDvMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvMinValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvMinValue.setUnits("microseconds")
_AcdCfmHistResultTwoWayDvMaxValue_Type = Integer32
_AcdCfmHistResultTwoWayDvMaxValue_Object = MibTableColumn
acdCfmHistResultTwoWayDvMaxValue = _AcdCfmHistResultTwoWayDvMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9, 1, 8),
    _AcdCfmHistResultTwoWayDvMaxValue_Type()
)
acdCfmHistResultTwoWayDvMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvMaxValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvMaxValue.setUnits("microseconds")
_AcdCfmHistResultTwoWayDvAvgValue_Type = Integer32
_AcdCfmHistResultTwoWayDvAvgValue_Object = MibTableColumn
acdCfmHistResultTwoWayDvAvgValue = _AcdCfmHistResultTwoWayDvAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9, 1, 9),
    _AcdCfmHistResultTwoWayDvAvgValue_Type()
)
acdCfmHistResultTwoWayDvAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvAvgValue.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvAvgValue.setUnits("microseconds")
_AcdCfmHistResultTwoWayDvThreshExc_Type = Unsigned32
_AcdCfmHistResultTwoWayDvThreshExc_Object = MibTableColumn
acdCfmHistResultTwoWayDvThreshExc = _AcdCfmHistResultTwoWayDvThreshExc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9, 1, 10),
    _AcdCfmHistResultTwoWayDvThreshExc_Type()
)
acdCfmHistResultTwoWayDvThreshExc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvThreshExc.setStatus("current")


class _AcdCfmHistResultTwoWayDvName_Type(DisplayString):
    """Custom type acdCfmHistResultTwoWayDvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmHistResultTwoWayDvName_Type.__name__ = "DisplayString"
_AcdCfmHistResultTwoWayDvName_Object = MibTableColumn
acdCfmHistResultTwoWayDvName = _AcdCfmHistResultTwoWayDvName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 1, 9, 1, 11),
    _AcdCfmHistResultTwoWayDvName_Type()
)
acdCfmHistResultTwoWayDvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvName.setStatus("current")
_AcdCfmPacketLoss_ObjectIdentity = ObjectIdentity
acdCfmPacketLoss = _AcdCfmPacketLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2)
)
_AcdCfmPktLossCfgTable_Object = MibTable
acdCfmPktLossCfgTable = _AcdCfmPktLossCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acdCfmPktLossCfgTable.setStatus("current")
_AcdCfmPktLossCfgEntry_Object = MibTableRow
acdCfmPktLossCfgEntry = _AcdCfmPktLossCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1, 1)
)
acdCfmPktLossCfgEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmPktLossCfgID"),
)
if mibBuilder.loadTexts:
    acdCfmPktLossCfgEntry.setStatus("current")
_AcdCfmPktLossCfgID_Type = Unsigned32
_AcdCfmPktLossCfgID_Object = MibTableColumn
acdCfmPktLossCfgID = _AcdCfmPktLossCfgID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1, 1, 1),
    _AcdCfmPktLossCfgID_Type()
)
acdCfmPktLossCfgID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgID.setStatus("current")
_AcdCfmPktLossCfgRowStatus_Type = RowStatus
_AcdCfmPktLossCfgRowStatus_Object = MibTableColumn
acdCfmPktLossCfgRowStatus = _AcdCfmPktLossCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1, 1, 2),
    _AcdCfmPktLossCfgRowStatus_Type()
)
acdCfmPktLossCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgRowStatus.setStatus("current")
_AcdCfmPktLossCfgMepIdx_Type = Unsigned32
_AcdCfmPktLossCfgMepIdx_Object = MibTableColumn
acdCfmPktLossCfgMepIdx = _AcdCfmPktLossCfgMepIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1, 1, 3),
    _AcdCfmPktLossCfgMepIdx_Type()
)
acdCfmPktLossCfgMepIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgMepIdx.setStatus("current")


class _AcdCfmPktLossCfgRemoteMepId_Type(Unsigned32):
    """Custom type acdCfmPktLossCfgRemoteMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AcdCfmPktLossCfgRemoteMepId_Type.__name__ = "Unsigned32"
_AcdCfmPktLossCfgRemoteMepId_Object = MibTableColumn
acdCfmPktLossCfgRemoteMepId = _AcdCfmPktLossCfgRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1, 1, 4),
    _AcdCfmPktLossCfgRemoteMepId_Type()
)
acdCfmPktLossCfgRemoteMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgRemoteMepId.setStatus("current")


class _AcdCfmPktLossCfgPriority_Type(Unsigned32):
    """Custom type acdCfmPktLossCfgPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdCfmPktLossCfgPriority_Type.__name__ = "Unsigned32"
_AcdCfmPktLossCfgPriority_Object = MibTableColumn
acdCfmPktLossCfgPriority = _AcdCfmPktLossCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1, 1, 5),
    _AcdCfmPktLossCfgPriority_Type()
)
acdCfmPktLossCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgPriority.setStatus("current")


class _AcdCfmPktLossCfgEnable_Type(TruthValue):
    """Custom type acdCfmPktLossCfgEnable based on TruthValue"""


_AcdCfmPktLossCfgEnable_Object = MibTableColumn
acdCfmPktLossCfgEnable = _AcdCfmPktLossCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1, 1, 6),
    _AcdCfmPktLossCfgEnable_Type()
)
acdCfmPktLossCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgEnable.setStatus("current")


class _AcdCfmPktLossCfgInterval_Type(Unsigned32):
    """Custom type acdCfmPktLossCfgInterval based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_AcdCfmPktLossCfgInterval_Type.__name__ = "Unsigned32"
_AcdCfmPktLossCfgInterval_Object = MibTableColumn
acdCfmPktLossCfgInterval = _AcdCfmPktLossCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1, 1, 7),
    _AcdCfmPktLossCfgInterval_Type()
)
acdCfmPktLossCfgInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgInterval.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgInterval.setUnits("milliseconds")


class _AcdCfmPktLossCfgRefPeriod_Type(Unsigned32):
    """Custom type acdCfmPktLossCfgRefPeriod based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_AcdCfmPktLossCfgRefPeriod_Type.__name__ = "Unsigned32"
_AcdCfmPktLossCfgRefPeriod_Object = MibTableColumn
acdCfmPktLossCfgRefPeriod = _AcdCfmPktLossCfgRefPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1, 1, 8),
    _AcdCfmPktLossCfgRefPeriod_Type()
)
acdCfmPktLossCfgRefPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgRefPeriod.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgRefPeriod.setUnits("minutes")


class _AcdCfmPktLossCfgThresh_Type(Unsigned32):
    """Custom type acdCfmPktLossCfgThresh based on Unsigned32"""
    defaultValue = 1


_AcdCfmPktLossCfgThresh_Object = MibTableColumn
acdCfmPktLossCfgThresh = _AcdCfmPktLossCfgThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1, 1, 9),
    _AcdCfmPktLossCfgThresh_Type()
)
acdCfmPktLossCfgThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgThresh.setStatus("current")


class _AcdCfmPktLossCfgRatioThresh_Type(Unsigned32):
    """Custom type acdCfmPktLossCfgRatioThresh based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdCfmPktLossCfgRatioThresh_Type.__name__ = "Unsigned32"
_AcdCfmPktLossCfgRatioThresh_Object = MibTableColumn
acdCfmPktLossCfgRatioThresh = _AcdCfmPktLossCfgRatioThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1, 1, 10),
    _AcdCfmPktLossCfgRatioThresh_Type()
)
acdCfmPktLossCfgRatioThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgRatioThresh.setStatus("current")


class _AcdCfmPktLossCfgName_Type(DisplayString):
    """Custom type acdCfmPktLossCfgName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmPktLossCfgName_Type.__name__ = "DisplayString"
_AcdCfmPktLossCfgName_Object = MibTableColumn
acdCfmPktLossCfgName = _AcdCfmPktLossCfgName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 1, 1, 11),
    _AcdCfmPktLossCfgName_Type()
)
acdCfmPktLossCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmPktLossCfgName.setStatus("current")
_AcdCfmResultPktLossTable_Object = MibTable
acdCfmResultPktLossTable = _AcdCfmResultPktLossTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    acdCfmResultPktLossTable.setStatus("current")
_AcdCfmResultPktLossEntry_Object = MibTableRow
acdCfmResultPktLossEntry = _AcdCfmResultPktLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1)
)
acdCfmResultPktLossEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmResultPktLossID"),
)
if mibBuilder.loadTexts:
    acdCfmResultPktLossEntry.setStatus("current")
_AcdCfmResultPktLossID_Type = Unsigned32
_AcdCfmResultPktLossID_Object = MibTableColumn
acdCfmResultPktLossID = _AcdCfmResultPktLossID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 1),
    _AcdCfmResultPktLossID_Type()
)
acdCfmResultPktLossID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmResultPktLossID.setStatus("current")
_AcdCfmResultPktLossPeriodIndex_Type = Unsigned32
_AcdCfmResultPktLossPeriodIndex_Object = MibTableColumn
acdCfmResultPktLossPeriodIndex = _AcdCfmResultPktLossPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 2),
    _AcdCfmResultPktLossPeriodIndex_Type()
)
acdCfmResultPktLossPeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossPeriodIndex.setStatus("current")
_AcdCfmResultPktLossIntervalStart_Type = DateAndTime
_AcdCfmResultPktLossIntervalStart_Object = MibTableColumn
acdCfmResultPktLossIntervalStart = _AcdCfmResultPktLossIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 3),
    _AcdCfmResultPktLossIntervalStart_Type()
)
acdCfmResultPktLossIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossIntervalStart.setStatus("current")
_AcdCfmResultPktLossValid_Type = TruthValue
_AcdCfmResultPktLossValid_Object = MibTableColumn
acdCfmResultPktLossValid = _AcdCfmResultPktLossValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 4),
    _AcdCfmResultPktLossValid_Type()
)
acdCfmResultPktLossValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossValid.setStatus("current")
_AcdCfmResultPktLossAlert_Type = TruthValue
_AcdCfmResultPktLossAlert_Object = MibTableColumn
acdCfmResultPktLossAlert = _AcdCfmResultPktLossAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 5),
    _AcdCfmResultPktLossAlert_Type()
)
acdCfmResultPktLossAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossAlert.setStatus("current")
_AcdCfmResultPktLossSamples_Type = Counter32
_AcdCfmResultPktLossSamples_Object = MibTableColumn
acdCfmResultPktLossSamples = _AcdCfmResultPktLossSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 6),
    _AcdCfmResultPktLossSamples_Type()
)
acdCfmResultPktLossSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossSamples.setStatus("current")
_AcdCfmResultPktLossOverflowSamples_Type = Counter32
_AcdCfmResultPktLossOverflowSamples_Object = MibTableColumn
acdCfmResultPktLossOverflowSamples = _AcdCfmResultPktLossOverflowSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 7),
    _AcdCfmResultPktLossOverflowSamples_Type()
)
acdCfmResultPktLossOverflowSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossOverflowSamples.setStatus("current")
_AcdCfmResultPktLossHCSamples_Type = Counter64
_AcdCfmResultPktLossHCSamples_Object = MibTableColumn
acdCfmResultPktLossHCSamples = _AcdCfmResultPktLossHCSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 8),
    _AcdCfmResultPktLossHCSamples_Type()
)
acdCfmResultPktLossHCSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossHCSamples.setStatus("current")
_AcdCfmResultPktLossNbrLoss_Type = Counter32
_AcdCfmResultPktLossNbrLoss_Object = MibTableColumn
acdCfmResultPktLossNbrLoss = _AcdCfmResultPktLossNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 9),
    _AcdCfmResultPktLossNbrLoss_Type()
)
acdCfmResultPktLossNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossNbrLoss.setStatus("current")
_AcdCfmResultPktLossOverflowNbrLoss_Type = Counter32
_AcdCfmResultPktLossOverflowNbrLoss_Object = MibTableColumn
acdCfmResultPktLossOverflowNbrLoss = _AcdCfmResultPktLossOverflowNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 10),
    _AcdCfmResultPktLossOverflowNbrLoss_Type()
)
acdCfmResultPktLossOverflowNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossOverflowNbrLoss.setStatus("current")
_AcdCfmResultPktLossHCNbrLoss_Type = Counter64
_AcdCfmResultPktLossHCNbrLoss_Object = MibTableColumn
acdCfmResultPktLossHCNbrLoss = _AcdCfmResultPktLossHCNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 11),
    _AcdCfmResultPktLossHCNbrLoss_Type()
)
acdCfmResultPktLossHCNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossHCNbrLoss.setStatus("current")
_AcdCfmResultPktLossNbrGaps_Type = Counter32
_AcdCfmResultPktLossNbrGaps_Object = MibTableColumn
acdCfmResultPktLossNbrGaps = _AcdCfmResultPktLossNbrGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 12),
    _AcdCfmResultPktLossNbrGaps_Type()
)
acdCfmResultPktLossNbrGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossNbrGaps.setStatus("current")
_AcdCfmResultPktLossOverflowNbrGaps_Type = Counter32
_AcdCfmResultPktLossOverflowNbrGaps_Object = MibTableColumn
acdCfmResultPktLossOverflowNbrGaps = _AcdCfmResultPktLossOverflowNbrGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 13),
    _AcdCfmResultPktLossOverflowNbrGaps_Type()
)
acdCfmResultPktLossOverflowNbrGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossOverflowNbrGaps.setStatus("current")
_AcdCfmResultPktLossHCNbrGaps_Type = Counter64
_AcdCfmResultPktLossHCNbrGaps_Object = MibTableColumn
acdCfmResultPktLossHCNbrGaps = _AcdCfmResultPktLossHCNbrGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 14),
    _AcdCfmResultPktLossHCNbrGaps_Type()
)
acdCfmResultPktLossHCNbrGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossHCNbrGaps.setStatus("current")
_AcdCfmResultPktLossLargestGap_Type = Counter32
_AcdCfmResultPktLossLargestGap_Object = MibTableColumn
acdCfmResultPktLossLargestGap = _AcdCfmResultPktLossLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 15),
    _AcdCfmResultPktLossLargestGap_Type()
)
acdCfmResultPktLossLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossLargestGap.setStatus("current")
_AcdCfmResultPktLossOverflowLargestGap_Type = Counter32
_AcdCfmResultPktLossOverflowLargestGap_Object = MibTableColumn
acdCfmResultPktLossOverflowLargestGap = _AcdCfmResultPktLossOverflowLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 16),
    _AcdCfmResultPktLossOverflowLargestGap_Type()
)
acdCfmResultPktLossOverflowLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossOverflowLargestGap.setStatus("current")
_AcdCfmResultPktLossHCLargestGap_Type = Counter64
_AcdCfmResultPktLossHCLargestGap_Object = MibTableColumn
acdCfmResultPktLossHCLargestGap = _AcdCfmResultPktLossHCLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 17),
    _AcdCfmResultPktLossHCLargestGap_Type()
)
acdCfmResultPktLossHCLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossHCLargestGap.setStatus("current")


class _AcdCfmResultPktLossRatio_Type(Unsigned32):
    """Custom type acdCfmResultPktLossRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdCfmResultPktLossRatio_Type.__name__ = "Unsigned32"
_AcdCfmResultPktLossRatio_Object = MibTableColumn
acdCfmResultPktLossRatio = _AcdCfmResultPktLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 18),
    _AcdCfmResultPktLossRatio_Type()
)
acdCfmResultPktLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossRatio.setStatus("current")


class _AcdCfmResultPktLossName_Type(DisplayString):
    """Custom type acdCfmResultPktLossName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmResultPktLossName_Type.__name__ = "DisplayString"
_AcdCfmResultPktLossName_Object = MibTableColumn
acdCfmResultPktLossName = _AcdCfmResultPktLossName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 2, 1, 19),
    _AcdCfmResultPktLossName_Type()
)
acdCfmResultPktLossName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmResultPktLossName.setStatus("current")
_AcdCfmHistResultPktLossTable_Object = MibTable
acdCfmHistResultPktLossTable = _AcdCfmHistResultPktLossTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossTable.setStatus("current")
_AcdCfmHistResultPktLossEntry_Object = MibTableRow
acdCfmHistResultPktLossEntry = _AcdCfmHistResultPktLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1)
)
acdCfmHistResultPktLossEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmHistResultPktLossID"),
    (0, "ACD-CFM-MIB", "acdCfmHistResultPktLossSampleIndex"),
)
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossEntry.setStatus("current")
_AcdCfmHistResultPktLossID_Type = Unsigned32
_AcdCfmHistResultPktLossID_Object = MibTableColumn
acdCfmHistResultPktLossID = _AcdCfmHistResultPktLossID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 1),
    _AcdCfmHistResultPktLossID_Type()
)
acdCfmHistResultPktLossID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossID.setStatus("current")
_AcdCfmHistResultPktLossSampleIndex_Type = Unsigned32
_AcdCfmHistResultPktLossSampleIndex_Object = MibTableColumn
acdCfmHistResultPktLossSampleIndex = _AcdCfmHistResultPktLossSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 2),
    _AcdCfmHistResultPktLossSampleIndex_Type()
)
acdCfmHistResultPktLossSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossSampleIndex.setStatus("current")


class _AcdCfmHistResultPktLossStatus_Type(Integer32):
    """Custom type acdCfmHistResultPktLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AcdCfmHistResultPktLossStatus_Type.__name__ = "Integer32"
_AcdCfmHistResultPktLossStatus_Object = MibTableColumn
acdCfmHistResultPktLossStatus = _AcdCfmHistResultPktLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 3),
    _AcdCfmHistResultPktLossStatus_Type()
)
acdCfmHistResultPktLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossStatus.setStatus("current")
_AcdCfmHistResultPktLossDuration_Type = Unsigned32
_AcdCfmHistResultPktLossDuration_Object = MibTableColumn
acdCfmHistResultPktLossDuration = _AcdCfmHistResultPktLossDuration_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 4),
    _AcdCfmHistResultPktLossDuration_Type()
)
acdCfmHistResultPktLossDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossDuration.setStatus("current")
_AcdCfmHistResultPktLossIntervalEnd_Type = DateAndTime
_AcdCfmHistResultPktLossIntervalEnd_Object = MibTableColumn
acdCfmHistResultPktLossIntervalEnd = _AcdCfmHistResultPktLossIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 5),
    _AcdCfmHistResultPktLossIntervalEnd_Type()
)
acdCfmHistResultPktLossIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossIntervalEnd.setStatus("current")
_AcdCfmHistResultPktLossSamples_Type = Counter32
_AcdCfmHistResultPktLossSamples_Object = MibTableColumn
acdCfmHistResultPktLossSamples = _AcdCfmHistResultPktLossSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 6),
    _AcdCfmHistResultPktLossSamples_Type()
)
acdCfmHistResultPktLossSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossSamples.setStatus("current")
_AcdCfmHistResultPktLossOverflowSamples_Type = Counter32
_AcdCfmHistResultPktLossOverflowSamples_Object = MibTableColumn
acdCfmHistResultPktLossOverflowSamples = _AcdCfmHistResultPktLossOverflowSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 7),
    _AcdCfmHistResultPktLossOverflowSamples_Type()
)
acdCfmHistResultPktLossOverflowSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossOverflowSamples.setStatus("current")
_AcdCfmHistResultPktLossHCSamples_Type = Counter64
_AcdCfmHistResultPktLossHCSamples_Object = MibTableColumn
acdCfmHistResultPktLossHCSamples = _AcdCfmHistResultPktLossHCSamples_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 8),
    _AcdCfmHistResultPktLossHCSamples_Type()
)
acdCfmHistResultPktLossHCSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossHCSamples.setStatus("current")
_AcdCfmHistResultPktLossNbrLoss_Type = Counter32
_AcdCfmHistResultPktLossNbrLoss_Object = MibTableColumn
acdCfmHistResultPktLossNbrLoss = _AcdCfmHistResultPktLossNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 9),
    _AcdCfmHistResultPktLossNbrLoss_Type()
)
acdCfmHistResultPktLossNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossNbrLoss.setStatus("current")
_AcdCfmHistResultPktLossOverflowNbrLoss_Type = Counter32
_AcdCfmHistResultPktLossOverflowNbrLoss_Object = MibTableColumn
acdCfmHistResultPktLossOverflowNbrLoss = _AcdCfmHistResultPktLossOverflowNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 10),
    _AcdCfmHistResultPktLossOverflowNbrLoss_Type()
)
acdCfmHistResultPktLossOverflowNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossOverflowNbrLoss.setStatus("current")
_AcdCfmHistResultPktLossHCNbrLoss_Type = Counter64
_AcdCfmHistResultPktLossHCNbrLoss_Object = MibTableColumn
acdCfmHistResultPktLossHCNbrLoss = _AcdCfmHistResultPktLossHCNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 11),
    _AcdCfmHistResultPktLossHCNbrLoss_Type()
)
acdCfmHistResultPktLossHCNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossHCNbrLoss.setStatus("current")
_AcdCfmHistResultPktLossNbrGaps_Type = Counter32
_AcdCfmHistResultPktLossNbrGaps_Object = MibTableColumn
acdCfmHistResultPktLossNbrGaps = _AcdCfmHistResultPktLossNbrGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 12),
    _AcdCfmHistResultPktLossNbrGaps_Type()
)
acdCfmHistResultPktLossNbrGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossNbrGaps.setStatus("current")
_AcdCfmHistResultPktLossOverflowNbrGaps_Type = Counter32
_AcdCfmHistResultPktLossOverflowNbrGaps_Object = MibTableColumn
acdCfmHistResultPktLossOverflowNbrGaps = _AcdCfmHistResultPktLossOverflowNbrGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 13),
    _AcdCfmHistResultPktLossOverflowNbrGaps_Type()
)
acdCfmHistResultPktLossOverflowNbrGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossOverflowNbrGaps.setStatus("current")
_AcdCfmHistResultPktLossHCNbrGaps_Type = Counter64
_AcdCfmHistResultPktLossHCNbrGaps_Object = MibTableColumn
acdCfmHistResultPktLossHCNbrGaps = _AcdCfmHistResultPktLossHCNbrGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 14),
    _AcdCfmHistResultPktLossHCNbrGaps_Type()
)
acdCfmHistResultPktLossHCNbrGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossHCNbrGaps.setStatus("current")
_AcdCfmHistResultPktLossLargestGap_Type = Counter32
_AcdCfmHistResultPktLossLargestGap_Object = MibTableColumn
acdCfmHistResultPktLossLargestGap = _AcdCfmHistResultPktLossLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 15),
    _AcdCfmHistResultPktLossLargestGap_Type()
)
acdCfmHistResultPktLossLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossLargestGap.setStatus("current")
_AcdCfmHistResultPktLossOverflowLargestGap_Type = Counter32
_AcdCfmHistResultPktLossOverflowLargestGap_Object = MibTableColumn
acdCfmHistResultPktLossOverflowLargestGap = _AcdCfmHistResultPktLossOverflowLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 16),
    _AcdCfmHistResultPktLossOverflowLargestGap_Type()
)
acdCfmHistResultPktLossOverflowLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossOverflowLargestGap.setStatus("current")
_AcdCfmHistResultPktLossHCLargestGap_Type = Counter64
_AcdCfmHistResultPktLossHCLargestGap_Object = MibTableColumn
acdCfmHistResultPktLossHCLargestGap = _AcdCfmHistResultPktLossHCLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 17),
    _AcdCfmHistResultPktLossHCLargestGap_Type()
)
acdCfmHistResultPktLossHCLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossHCLargestGap.setStatus("current")


class _AcdCfmHistResultPktLossRatio_Type(Unsigned32):
    """Custom type acdCfmHistResultPktLossRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdCfmHistResultPktLossRatio_Type.__name__ = "Unsigned32"
_AcdCfmHistResultPktLossRatio_Object = MibTableColumn
acdCfmHistResultPktLossRatio = _AcdCfmHistResultPktLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 18),
    _AcdCfmHistResultPktLossRatio_Type()
)
acdCfmHistResultPktLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossRatio.setStatus("current")


class _AcdCfmHistResultPktLossName_Type(DisplayString):
    """Custom type acdCfmHistResultPktLossName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmHistResultPktLossName_Type.__name__ = "DisplayString"
_AcdCfmHistResultPktLossName_Object = MibTableColumn
acdCfmHistResultPktLossName = _AcdCfmHistResultPktLossName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 2, 3, 1, 19),
    _AcdCfmHistResultPktLossName_Type()
)
acdCfmHistResultPktLossName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossName.setStatus("current")
_AcdCfmMep_ObjectIdentity = ObjectIdentity
acdCfmMep = _AcdCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3)
)
_AcdCfmMepStatsTxTable_Object = MibTable
acdCfmMepStatsTxTable = _AcdCfmMepStatsTxTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2)
)
if mibBuilder.loadTexts:
    acdCfmMepStatsTxTable.setStatus("current")
_AcdCfmMepStatsTxEntry_Object = MibTableRow
acdCfmMepStatsTxEntry = _AcdCfmMepStatsTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1)
)
acdCfmMepStatsTxEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmMepStatsTxID"),
)
if mibBuilder.loadTexts:
    acdCfmMepStatsTxEntry.setStatus("current")
_AcdCfmMepStatsTxID_Type = Unsigned32
_AcdCfmMepStatsTxID_Object = MibTableColumn
acdCfmMepStatsTxID = _AcdCfmMepStatsTxID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 1),
    _AcdCfmMepStatsTxID_Type()
)
acdCfmMepStatsTxID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxID.setStatus("current")
_AcdCfmMepStatsTxCcmPdu_Type = Counter64
_AcdCfmMepStatsTxCcmPdu_Object = MibTableColumn
acdCfmMepStatsTxCcmPdu = _AcdCfmMepStatsTxCcmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 2),
    _AcdCfmMepStatsTxCcmPdu_Type()
)
acdCfmMepStatsTxCcmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxCcmPdu.setStatus("current")
_AcdCfmMepStatsTxLbmPdu_Type = Counter64
_AcdCfmMepStatsTxLbmPdu_Object = MibTableColumn
acdCfmMepStatsTxLbmPdu = _AcdCfmMepStatsTxLbmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 3),
    _AcdCfmMepStatsTxLbmPdu_Type()
)
acdCfmMepStatsTxLbmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxLbmPdu.setStatus("current")
_AcdCfmMepStatsTxLbrPdu_Type = Counter64
_AcdCfmMepStatsTxLbrPdu_Object = MibTableColumn
acdCfmMepStatsTxLbrPdu = _AcdCfmMepStatsTxLbrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 4),
    _AcdCfmMepStatsTxLbrPdu_Type()
)
acdCfmMepStatsTxLbrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxLbrPdu.setStatus("current")
_AcdCfmMepStatsTxLtmPdu_Type = Counter64
_AcdCfmMepStatsTxLtmPdu_Object = MibTableColumn
acdCfmMepStatsTxLtmPdu = _AcdCfmMepStatsTxLtmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 5),
    _AcdCfmMepStatsTxLtmPdu_Type()
)
acdCfmMepStatsTxLtmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxLtmPdu.setStatus("current")
_AcdCfmMepStatsTxLtrPdu_Type = Counter64
_AcdCfmMepStatsTxLtrPdu_Object = MibTableColumn
acdCfmMepStatsTxLtrPdu = _AcdCfmMepStatsTxLtrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 6),
    _AcdCfmMepStatsTxLtrPdu_Type()
)
acdCfmMepStatsTxLtrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxLtrPdu.setStatus("current")
_AcdCfmMepStatsTxAisPdu_Type = Counter64
_AcdCfmMepStatsTxAisPdu_Object = MibTableColumn
acdCfmMepStatsTxAisPdu = _AcdCfmMepStatsTxAisPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 7),
    _AcdCfmMepStatsTxAisPdu_Type()
)
acdCfmMepStatsTxAisPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxAisPdu.setStatus("current")
_AcdCfmMepStatsTxLckPdu_Type = Counter64
_AcdCfmMepStatsTxLckPdu_Object = MibTableColumn
acdCfmMepStatsTxLckPdu = _AcdCfmMepStatsTxLckPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 8),
    _AcdCfmMepStatsTxLckPdu_Type()
)
acdCfmMepStatsTxLckPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxLckPdu.setStatus("current")
_AcdCfmMepStatsTxTstPdu_Type = Counter64
_AcdCfmMepStatsTxTstPdu_Object = MibTableColumn
acdCfmMepStatsTxTstPdu = _AcdCfmMepStatsTxTstPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 9),
    _AcdCfmMepStatsTxTstPdu_Type()
)
acdCfmMepStatsTxTstPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxTstPdu.setStatus("current")
_AcdCfmMepStatsTxLinearApsPdu_Type = Counter64
_AcdCfmMepStatsTxLinearApsPdu_Object = MibTableColumn
acdCfmMepStatsTxLinearApsPdu = _AcdCfmMepStatsTxLinearApsPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 10),
    _AcdCfmMepStatsTxLinearApsPdu_Type()
)
acdCfmMepStatsTxLinearApsPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxLinearApsPdu.setStatus("current")
_AcdCfmMepStatsTxRingApsPdu_Type = Counter64
_AcdCfmMepStatsTxRingApsPdu_Object = MibTableColumn
acdCfmMepStatsTxRingApsPdu = _AcdCfmMepStatsTxRingApsPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 11),
    _AcdCfmMepStatsTxRingApsPdu_Type()
)
acdCfmMepStatsTxRingApsPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxRingApsPdu.setStatus("current")
_AcdCfmMepStatsTxMccPdu_Type = Counter64
_AcdCfmMepStatsTxMccPdu_Object = MibTableColumn
acdCfmMepStatsTxMccPdu = _AcdCfmMepStatsTxMccPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 12),
    _AcdCfmMepStatsTxMccPdu_Type()
)
acdCfmMepStatsTxMccPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxMccPdu.setStatus("current")
_AcdCfmMepStatsTxLmmPdu_Type = Counter64
_AcdCfmMepStatsTxLmmPdu_Object = MibTableColumn
acdCfmMepStatsTxLmmPdu = _AcdCfmMepStatsTxLmmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 13),
    _AcdCfmMepStatsTxLmmPdu_Type()
)
acdCfmMepStatsTxLmmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxLmmPdu.setStatus("current")
_AcdCfmMepStatsTxLmrPdu_Type = Counter64
_AcdCfmMepStatsTxLmrPdu_Object = MibTableColumn
acdCfmMepStatsTxLmrPdu = _AcdCfmMepStatsTxLmrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 14),
    _AcdCfmMepStatsTxLmrPdu_Type()
)
acdCfmMepStatsTxLmrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxLmrPdu.setStatus("current")
_AcdCfmMepStatsTx1dmPdu_Type = Counter64
_AcdCfmMepStatsTx1dmPdu_Object = MibTableColumn
acdCfmMepStatsTx1dmPdu = _AcdCfmMepStatsTx1dmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 15),
    _AcdCfmMepStatsTx1dmPdu_Type()
)
acdCfmMepStatsTx1dmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTx1dmPdu.setStatus("current")
_AcdCfmMepStatsTxDmmPdu_Type = Counter64
_AcdCfmMepStatsTxDmmPdu_Object = MibTableColumn
acdCfmMepStatsTxDmmPdu = _AcdCfmMepStatsTxDmmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 16),
    _AcdCfmMepStatsTxDmmPdu_Type()
)
acdCfmMepStatsTxDmmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxDmmPdu.setStatus("current")
_AcdCfmMepStatsTxDmrPdu_Type = Counter64
_AcdCfmMepStatsTxDmrPdu_Object = MibTableColumn
acdCfmMepStatsTxDmrPdu = _AcdCfmMepStatsTxDmrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 17),
    _AcdCfmMepStatsTxDmrPdu_Type()
)
acdCfmMepStatsTxDmrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxDmrPdu.setStatus("current")
_AcdCfmMepStatsTxExmPdu_Type = Counter64
_AcdCfmMepStatsTxExmPdu_Object = MibTableColumn
acdCfmMepStatsTxExmPdu = _AcdCfmMepStatsTxExmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 18),
    _AcdCfmMepStatsTxExmPdu_Type()
)
acdCfmMepStatsTxExmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxExmPdu.setStatus("current")
_AcdCfmMepStatsTxExrPdu_Type = Counter64
_AcdCfmMepStatsTxExrPdu_Object = MibTableColumn
acdCfmMepStatsTxExrPdu = _AcdCfmMepStatsTxExrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 19),
    _AcdCfmMepStatsTxExrPdu_Type()
)
acdCfmMepStatsTxExrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxExrPdu.setStatus("current")
_AcdCfmMepStatsTxVsmPdu_Type = Counter64
_AcdCfmMepStatsTxVsmPdu_Object = MibTableColumn
acdCfmMepStatsTxVsmPdu = _AcdCfmMepStatsTxVsmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 20),
    _AcdCfmMepStatsTxVsmPdu_Type()
)
acdCfmMepStatsTxVsmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxVsmPdu.setStatus("current")
_AcdCfmMepStatsTxVsrPdu_Type = Counter64
_AcdCfmMepStatsTxVsrPdu_Object = MibTableColumn
acdCfmMepStatsTxVsrPdu = _AcdCfmMepStatsTxVsrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 21),
    _AcdCfmMepStatsTxVsrPdu_Type()
)
acdCfmMepStatsTxVsrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxVsrPdu.setStatus("current")
_AcdCfmMepStatsTxCsfPdu_Type = Counter64
_AcdCfmMepStatsTxCsfPdu_Object = MibTableColumn
acdCfmMepStatsTxCsfPdu = _AcdCfmMepStatsTxCsfPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 22),
    _AcdCfmMepStatsTxCsfPdu_Type()
)
acdCfmMepStatsTxCsfPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxCsfPdu.setStatus("current")
_AcdCfmMepStatsTxSlmPdu_Type = Counter64
_AcdCfmMepStatsTxSlmPdu_Object = MibTableColumn
acdCfmMepStatsTxSlmPdu = _AcdCfmMepStatsTxSlmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 23),
    _AcdCfmMepStatsTxSlmPdu_Type()
)
acdCfmMepStatsTxSlmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxSlmPdu.setStatus("current")
_AcdCfmMepStatsTxSlrPdu_Type = Counter64
_AcdCfmMepStatsTxSlrPdu_Object = MibTableColumn
acdCfmMepStatsTxSlrPdu = _AcdCfmMepStatsTxSlrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 24),
    _AcdCfmMepStatsTxSlrPdu_Type()
)
acdCfmMepStatsTxSlrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxSlrPdu.setStatus("current")


class _AcdCfmMepStatsTxName_Type(DisplayString):
    """Custom type acdCfmMepStatsTxName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmMepStatsTxName_Type.__name__ = "DisplayString"
_AcdCfmMepStatsTxName_Object = MibTableColumn
acdCfmMepStatsTxName = _AcdCfmMepStatsTxName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 2, 1, 25),
    _AcdCfmMepStatsTxName_Type()
)
acdCfmMepStatsTxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsTxName.setStatus("current")
_AcdCfmMepStatsRxTable_Object = MibTable
acdCfmMepStatsRxTable = _AcdCfmMepStatsRxTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3)
)
if mibBuilder.loadTexts:
    acdCfmMepStatsRxTable.setStatus("current")
_AcdCfmMepStatsRxEntry_Object = MibTableRow
acdCfmMepStatsRxEntry = _AcdCfmMepStatsRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1)
)
acdCfmMepStatsRxEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmMepStatsRxID"),
)
if mibBuilder.loadTexts:
    acdCfmMepStatsRxEntry.setStatus("current")
_AcdCfmMepStatsRxID_Type = Unsigned32
_AcdCfmMepStatsRxID_Object = MibTableColumn
acdCfmMepStatsRxID = _AcdCfmMepStatsRxID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 1),
    _AcdCfmMepStatsRxID_Type()
)
acdCfmMepStatsRxID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxID.setStatus("current")
_AcdCfmMepStatsRxCcmPdu_Type = Counter64
_AcdCfmMepStatsRxCcmPdu_Object = MibTableColumn
acdCfmMepStatsRxCcmPdu = _AcdCfmMepStatsRxCcmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 2),
    _AcdCfmMepStatsRxCcmPdu_Type()
)
acdCfmMepStatsRxCcmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxCcmPdu.setStatus("current")
_AcdCfmMepStatsRxLbmPdu_Type = Counter64
_AcdCfmMepStatsRxLbmPdu_Object = MibTableColumn
acdCfmMepStatsRxLbmPdu = _AcdCfmMepStatsRxLbmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 3),
    _AcdCfmMepStatsRxLbmPdu_Type()
)
acdCfmMepStatsRxLbmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLbmPdu.setStatus("current")
_AcdCfmMepStatsRxLbrPdu_Type = Counter64
_AcdCfmMepStatsRxLbrPdu_Object = MibTableColumn
acdCfmMepStatsRxLbrPdu = _AcdCfmMepStatsRxLbrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 4),
    _AcdCfmMepStatsRxLbrPdu_Type()
)
acdCfmMepStatsRxLbrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLbrPdu.setStatus("current")
_AcdCfmMepStatsRxLtmPdu_Type = Counter64
_AcdCfmMepStatsRxLtmPdu_Object = MibTableColumn
acdCfmMepStatsRxLtmPdu = _AcdCfmMepStatsRxLtmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 5),
    _AcdCfmMepStatsRxLtmPdu_Type()
)
acdCfmMepStatsRxLtmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLtmPdu.setStatus("current")
_AcdCfmMepStatsRxLtrPdu_Type = Counter64
_AcdCfmMepStatsRxLtrPdu_Object = MibTableColumn
acdCfmMepStatsRxLtrPdu = _AcdCfmMepStatsRxLtrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 6),
    _AcdCfmMepStatsRxLtrPdu_Type()
)
acdCfmMepStatsRxLtrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLtrPdu.setStatus("current")
_AcdCfmMepStatsRxAisPdu_Type = Counter64
_AcdCfmMepStatsRxAisPdu_Object = MibTableColumn
acdCfmMepStatsRxAisPdu = _AcdCfmMepStatsRxAisPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 7),
    _AcdCfmMepStatsRxAisPdu_Type()
)
acdCfmMepStatsRxAisPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxAisPdu.setStatus("current")
_AcdCfmMepStatsRxLckPdu_Type = Counter64
_AcdCfmMepStatsRxLckPdu_Object = MibTableColumn
acdCfmMepStatsRxLckPdu = _AcdCfmMepStatsRxLckPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 8),
    _AcdCfmMepStatsRxLckPdu_Type()
)
acdCfmMepStatsRxLckPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLckPdu.setStatus("current")
_AcdCfmMepStatsRxTstPdu_Type = Counter64
_AcdCfmMepStatsRxTstPdu_Object = MibTableColumn
acdCfmMepStatsRxTstPdu = _AcdCfmMepStatsRxTstPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 9),
    _AcdCfmMepStatsRxTstPdu_Type()
)
acdCfmMepStatsRxTstPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxTstPdu.setStatus("current")
_AcdCfmMepStatsRxLinearApsPdu_Type = Counter64
_AcdCfmMepStatsRxLinearApsPdu_Object = MibTableColumn
acdCfmMepStatsRxLinearApsPdu = _AcdCfmMepStatsRxLinearApsPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 10),
    _AcdCfmMepStatsRxLinearApsPdu_Type()
)
acdCfmMepStatsRxLinearApsPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLinearApsPdu.setStatus("current")
_AcdCfmMepStatsRxRingApsPdu_Type = Counter64
_AcdCfmMepStatsRxRingApsPdu_Object = MibTableColumn
acdCfmMepStatsRxRingApsPdu = _AcdCfmMepStatsRxRingApsPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 11),
    _AcdCfmMepStatsRxRingApsPdu_Type()
)
acdCfmMepStatsRxRingApsPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxRingApsPdu.setStatus("current")
_AcdCfmMepStatsRxMccPdu_Type = Counter64
_AcdCfmMepStatsRxMccPdu_Object = MibTableColumn
acdCfmMepStatsRxMccPdu = _AcdCfmMepStatsRxMccPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 12),
    _AcdCfmMepStatsRxMccPdu_Type()
)
acdCfmMepStatsRxMccPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxMccPdu.setStatus("current")
_AcdCfmMepStatsRxLmmPdu_Type = Counter64
_AcdCfmMepStatsRxLmmPdu_Object = MibTableColumn
acdCfmMepStatsRxLmmPdu = _AcdCfmMepStatsRxLmmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 13),
    _AcdCfmMepStatsRxLmmPdu_Type()
)
acdCfmMepStatsRxLmmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLmmPdu.setStatus("current")
_AcdCfmMepStatsRxLmrPdu_Type = Counter64
_AcdCfmMepStatsRxLmrPdu_Object = MibTableColumn
acdCfmMepStatsRxLmrPdu = _AcdCfmMepStatsRxLmrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 14),
    _AcdCfmMepStatsRxLmrPdu_Type()
)
acdCfmMepStatsRxLmrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLmrPdu.setStatus("current")
_AcdCfmMepStatsRx1dmPdu_Type = Counter64
_AcdCfmMepStatsRx1dmPdu_Object = MibTableColumn
acdCfmMepStatsRx1dmPdu = _AcdCfmMepStatsRx1dmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 15),
    _AcdCfmMepStatsRx1dmPdu_Type()
)
acdCfmMepStatsRx1dmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRx1dmPdu.setStatus("current")
_AcdCfmMepStatsRxDmmPdu_Type = Counter64
_AcdCfmMepStatsRxDmmPdu_Object = MibTableColumn
acdCfmMepStatsRxDmmPdu = _AcdCfmMepStatsRxDmmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 16),
    _AcdCfmMepStatsRxDmmPdu_Type()
)
acdCfmMepStatsRxDmmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxDmmPdu.setStatus("current")
_AcdCfmMepStatsRxDmrPdu_Type = Counter64
_AcdCfmMepStatsRxDmrPdu_Object = MibTableColumn
acdCfmMepStatsRxDmrPdu = _AcdCfmMepStatsRxDmrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 17),
    _AcdCfmMepStatsRxDmrPdu_Type()
)
acdCfmMepStatsRxDmrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxDmrPdu.setStatus("current")
_AcdCfmMepStatsRxExmPdu_Type = Counter64
_AcdCfmMepStatsRxExmPdu_Object = MibTableColumn
acdCfmMepStatsRxExmPdu = _AcdCfmMepStatsRxExmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 18),
    _AcdCfmMepStatsRxExmPdu_Type()
)
acdCfmMepStatsRxExmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxExmPdu.setStatus("current")
_AcdCfmMepStatsRxExrPdu_Type = Counter64
_AcdCfmMepStatsRxExrPdu_Object = MibTableColumn
acdCfmMepStatsRxExrPdu = _AcdCfmMepStatsRxExrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 19),
    _AcdCfmMepStatsRxExrPdu_Type()
)
acdCfmMepStatsRxExrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxExrPdu.setStatus("current")
_AcdCfmMepStatsRxVsmPdu_Type = Counter64
_AcdCfmMepStatsRxVsmPdu_Object = MibTableColumn
acdCfmMepStatsRxVsmPdu = _AcdCfmMepStatsRxVsmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 20),
    _AcdCfmMepStatsRxVsmPdu_Type()
)
acdCfmMepStatsRxVsmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxVsmPdu.setStatus("current")
_AcdCfmMepStatsRxVsrPdu_Type = Counter64
_AcdCfmMepStatsRxVsrPdu_Object = MibTableColumn
acdCfmMepStatsRxVsrPdu = _AcdCfmMepStatsRxVsrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 21),
    _AcdCfmMepStatsRxVsrPdu_Type()
)
acdCfmMepStatsRxVsrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxVsrPdu.setStatus("current")
_AcdCfmMepStatsRxCcmSeqErrors_Type = Counter64
_AcdCfmMepStatsRxCcmSeqErrors_Object = MibTableColumn
acdCfmMepStatsRxCcmSeqErrors = _AcdCfmMepStatsRxCcmSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 22),
    _AcdCfmMepStatsRxCcmSeqErrors_Type()
)
acdCfmMepStatsRxCcmSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxCcmSeqErrors.setStatus("current")
_AcdCfmMepStatsRxLtrUnexpectedPdu_Type = Counter64
_AcdCfmMepStatsRxLtrUnexpectedPdu_Object = MibTableColumn
acdCfmMepStatsRxLtrUnexpectedPdu = _AcdCfmMepStatsRxLtrUnexpectedPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 23),
    _AcdCfmMepStatsRxLtrUnexpectedPdu_Type()
)
acdCfmMepStatsRxLtrUnexpectedPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLtrUnexpectedPdu.setStatus("current")
_AcdCfmMepStatsRxLtrMacErrors_Type = Counter64
_AcdCfmMepStatsRxLtrMacErrors_Object = MibTableColumn
acdCfmMepStatsRxLtrMacErrors = _AcdCfmMepStatsRxLtrMacErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 24),
    _AcdCfmMepStatsRxLtrMacErrors_Type()
)
acdCfmMepStatsRxLtrMacErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLtrMacErrors.setStatus("current")
_AcdCfmMepStatsRxLbrOooErrors_Type = Counter64
_AcdCfmMepStatsRxLbrOooErrors_Object = MibTableColumn
acdCfmMepStatsRxLbrOooErrors = _AcdCfmMepStatsRxLbrOooErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 25),
    _AcdCfmMepStatsRxLbrOooErrors_Type()
)
acdCfmMepStatsRxLbrOooErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLbrOooErrors.setStatus("current")
_AcdCfmMepStatsRxLbrUnexpectedPdu_Type = Counter64
_AcdCfmMepStatsRxLbrUnexpectedPdu_Object = MibTableColumn
acdCfmMepStatsRxLbrUnexpectedPdu = _AcdCfmMepStatsRxLbrUnexpectedPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 26),
    _AcdCfmMepStatsRxLbrUnexpectedPdu_Type()
)
acdCfmMepStatsRxLbrUnexpectedPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLbrUnexpectedPdu.setStatus("current")
_AcdCfmMepStatsRxLbrDataErrors_Type = Counter64
_AcdCfmMepStatsRxLbrDataErrors_Object = MibTableColumn
acdCfmMepStatsRxLbrDataErrors = _AcdCfmMepStatsRxLbrDataErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 27),
    _AcdCfmMepStatsRxLbrDataErrors_Type()
)
acdCfmMepStatsRxLbrDataErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxLbrDataErrors.setStatus("current")
_AcdCfmMepStatsRxCsfPdu_Type = Counter64
_AcdCfmMepStatsRxCsfPdu_Object = MibTableColumn
acdCfmMepStatsRxCsfPdu = _AcdCfmMepStatsRxCsfPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 28),
    _AcdCfmMepStatsRxCsfPdu_Type()
)
acdCfmMepStatsRxCsfPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxCsfPdu.setStatus("current")
_AcdCfmMepStatsRxSlmPdu_Type = Counter64
_AcdCfmMepStatsRxSlmPdu_Object = MibTableColumn
acdCfmMepStatsRxSlmPdu = _AcdCfmMepStatsRxSlmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 29),
    _AcdCfmMepStatsRxSlmPdu_Type()
)
acdCfmMepStatsRxSlmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxSlmPdu.setStatus("current")
_AcdCfmMepStatsRxSlrPdu_Type = Counter64
_AcdCfmMepStatsRxSlrPdu_Object = MibTableColumn
acdCfmMepStatsRxSlrPdu = _AcdCfmMepStatsRxSlrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 30),
    _AcdCfmMepStatsRxSlrPdu_Type()
)
acdCfmMepStatsRxSlrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxSlrPdu.setStatus("current")
_AcdCfmMepStatsRxCsfInvalidFlags_Type = Counter64
_AcdCfmMepStatsRxCsfInvalidFlags_Object = MibTableColumn
acdCfmMepStatsRxCsfInvalidFlags = _AcdCfmMepStatsRxCsfInvalidFlags_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 31),
    _AcdCfmMepStatsRxCsfInvalidFlags_Type()
)
acdCfmMepStatsRxCsfInvalidFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxCsfInvalidFlags.setStatus("current")


class _AcdCfmMepStatsRxName_Type(DisplayString):
    """Custom type acdCfmMepStatsRxName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmMepStatsRxName_Type.__name__ = "DisplayString"
_AcdCfmMepStatsRxName_Object = MibTableColumn
acdCfmMepStatsRxName = _AcdCfmMepStatsRxName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 3, 1, 32),
    _AcdCfmMepStatsRxName_Type()
)
acdCfmMepStatsRxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepStatsRxName.setStatus("current")
_AcdCfmMepDmStatsTable_Object = MibTable
acdCfmMepDmStatsTable = _AcdCfmMepDmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 4)
)
if mibBuilder.loadTexts:
    acdCfmMepDmStatsTable.setStatus("current")
_AcdCfmMepDmStatsEntry_Object = MibTableRow
acdCfmMepDmStatsEntry = _AcdCfmMepDmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 4, 1)
)
acdCfmMepDmStatsEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmMepDmStatsID"),
    (0, "ACD-CFM-MIB", "acdCfmMepDmStatsPriority"),
)
if mibBuilder.loadTexts:
    acdCfmMepDmStatsEntry.setStatus("current")
_AcdCfmMepDmStatsID_Type = Unsigned32
_AcdCfmMepDmStatsID_Object = MibTableColumn
acdCfmMepDmStatsID = _AcdCfmMepDmStatsID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 4, 1, 1),
    _AcdCfmMepDmStatsID_Type()
)
acdCfmMepDmStatsID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmMepDmStatsID.setStatus("current")
_AcdCfmMepDmStatsPriority_Type = Unsigned32
_AcdCfmMepDmStatsPriority_Object = MibTableColumn
acdCfmMepDmStatsPriority = _AcdCfmMepDmStatsPriority_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 4, 1, 2),
    _AcdCfmMepDmStatsPriority_Type()
)
acdCfmMepDmStatsPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmMepDmStatsPriority.setStatus("current")
_AcdCfmMepDmStatsTxDmmPdu_Type = Counter64
_AcdCfmMepDmStatsTxDmmPdu_Object = MibTableColumn
acdCfmMepDmStatsTxDmmPdu = _AcdCfmMepDmStatsTxDmmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 4, 1, 3),
    _AcdCfmMepDmStatsTxDmmPdu_Type()
)
acdCfmMepDmStatsTxDmmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepDmStatsTxDmmPdu.setStatus("current")
_AcdCfmMepDmStatsRxDmmPdu_Type = Counter64
_AcdCfmMepDmStatsRxDmmPdu_Object = MibTableColumn
acdCfmMepDmStatsRxDmmPdu = _AcdCfmMepDmStatsRxDmmPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 4, 1, 4),
    _AcdCfmMepDmStatsRxDmmPdu_Type()
)
acdCfmMepDmStatsRxDmmPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepDmStatsRxDmmPdu.setStatus("current")
_AcdCfmMepDmStatsTxDmrPdu_Type = Counter64
_AcdCfmMepDmStatsTxDmrPdu_Object = MibTableColumn
acdCfmMepDmStatsTxDmrPdu = _AcdCfmMepDmStatsTxDmrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 4, 1, 5),
    _AcdCfmMepDmStatsTxDmrPdu_Type()
)
acdCfmMepDmStatsTxDmrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepDmStatsTxDmrPdu.setStatus("current")
_AcdCfmMepDmStatsRxDmrPdu_Type = Counter64
_AcdCfmMepDmStatsRxDmrPdu_Object = MibTableColumn
acdCfmMepDmStatsRxDmrPdu = _AcdCfmMepDmStatsRxDmrPdu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 4, 1, 6),
    _AcdCfmMepDmStatsRxDmrPdu_Type()
)
acdCfmMepDmStatsRxDmrPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepDmStatsRxDmrPdu.setStatus("current")


class _AcdCfmMepDmStatsName_Type(DisplayString):
    """Custom type acdCfmMepDmStatsName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmMepDmStatsName_Type.__name__ = "DisplayString"
_AcdCfmMepDmStatsName_Object = MibTableColumn
acdCfmMepDmStatsName = _AcdCfmMepDmStatsName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 4, 1, 7),
    _AcdCfmMepDmStatsName_Type()
)
acdCfmMepDmStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepDmStatsName.setStatus("current")
_AcdCfmMepCfgTable_Object = MibTable
acdCfmMepCfgTable = _AcdCfmMepCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5)
)
if mibBuilder.loadTexts:
    acdCfmMepCfgTable.setStatus("current")
_AcdCfmMepCfgEntry_Object = MibTableRow
acdCfmMepCfgEntry = _AcdCfmMepCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1)
)
acdCfmMepCfgEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmMepCfgIdx"),
)
if mibBuilder.loadTexts:
    acdCfmMepCfgEntry.setStatus("current")
_AcdCfmMepCfgIdx_Type = Unsigned32
_AcdCfmMepCfgIdx_Object = MibTableColumn
acdCfmMepCfgIdx = _AcdCfmMepCfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 1),
    _AcdCfmMepCfgIdx_Type()
)
acdCfmMepCfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmMepCfgIdx.setStatus("current")
_AcdCfmMepCfgRowStatus_Type = RowStatus
_AcdCfmMepCfgRowStatus_Object = MibTableColumn
acdCfmMepCfgRowStatus = _AcdCfmMepCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 2),
    _AcdCfmMepCfgRowStatus_Type()
)
acdCfmMepCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmMepCfgRowStatus.setStatus("current")
_AcdCfmMepCfgMdIdx_Type = Unsigned32
_AcdCfmMepCfgMdIdx_Object = MibTableColumn
acdCfmMepCfgMdIdx = _AcdCfmMepCfgMdIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 3),
    _AcdCfmMepCfgMdIdx_Type()
)
acdCfmMepCfgMdIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepCfgMdIdx.setStatus("current")


class _AcdCfmMepCfgMaIdx_Type(Unsigned32):
    """Custom type acdCfmMepCfgMaIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AcdCfmMepCfgMaIdx_Type.__name__ = "Unsigned32"
_AcdCfmMepCfgMaIdx_Object = MibTableColumn
acdCfmMepCfgMaIdx = _AcdCfmMepCfgMaIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 4),
    _AcdCfmMepCfgMaIdx_Type()
)
acdCfmMepCfgMaIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmMepCfgMaIdx.setStatus("current")


class _AcdCfmMepCfgMepId_Type(Unsigned32):
    """Custom type acdCfmMepCfgMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AcdCfmMepCfgMepId_Type.__name__ = "Unsigned32"
_AcdCfmMepCfgMepId_Object = MibTableColumn
acdCfmMepCfgMepId = _AcdCfmMepCfgMepId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 5),
    _AcdCfmMepCfgMepId_Type()
)
acdCfmMepCfgMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmMepCfgMepId.setStatus("current")


class _AcdCfmMepCfgName_Type(DisplayString):
    """Custom type acdCfmMepCfgName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmMepCfgName_Type.__name__ = "DisplayString"
_AcdCfmMepCfgName_Object = MibTableColumn
acdCfmMepCfgName = _AcdCfmMepCfgName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 6),
    _AcdCfmMepCfgName_Type()
)
acdCfmMepCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmMepCfgName.setStatus("current")


class _AcdCfmMepCfgPortId_Type(Unsigned32):
    """Custom type acdCfmMepCfgPortId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdCfmMepCfgPortId_Type.__name__ = "Unsigned32"
_AcdCfmMepCfgPortId_Object = MibTableColumn
acdCfmMepCfgPortId = _AcdCfmMepCfgPortId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 7),
    _AcdCfmMepCfgPortId_Type()
)
acdCfmMepCfgPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmMepCfgPortId.setStatus("current")
_AcdCfmMepCfgPortIdMacAddr_Type = MacAddress
_AcdCfmMepCfgPortIdMacAddr_Object = MibTableColumn
acdCfmMepCfgPortIdMacAddr = _AcdCfmMepCfgPortIdMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 8),
    _AcdCfmMepCfgPortIdMacAddr_Type()
)
acdCfmMepCfgPortIdMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepCfgPortIdMacAddr.setStatus("current")


class _AcdCfmMepCfgDirection_Type(AcdCfmMepDirection):
    """Custom type acdCfmMepCfgDirection based on AcdCfmMepDirection"""
    defaultValue = 1


_AcdCfmMepCfgDirection_Object = MibTableColumn
acdCfmMepCfgDirection = _AcdCfmMepCfgDirection_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 9),
    _AcdCfmMepCfgDirection_Type()
)
acdCfmMepCfgDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdCfmMepCfgDirection.setStatus("current")


class _AcdCfmMepCfgPrimaryVid_Type(VlanIdOrNone):
    """Custom type acdCfmMepCfgPrimaryVid based on VlanIdOrNone"""
    defaultValue = 0


_AcdCfmMepCfgPrimaryVid_Object = MibTableColumn
acdCfmMepCfgPrimaryVid = _AcdCfmMepCfgPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 10),
    _AcdCfmMepCfgPrimaryVid_Type()
)
acdCfmMepCfgPrimaryVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmMepCfgPrimaryVid.setStatus("current")


class _AcdCfmMepCfgActive_Type(TruthValue):
    """Custom type acdCfmMepCfgActive based on TruthValue"""


_AcdCfmMepCfgActive_Object = MibTableColumn
acdCfmMepCfgActive = _AcdCfmMepCfgActive_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 11),
    _AcdCfmMepCfgActive_Type()
)
acdCfmMepCfgActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmMepCfgActive.setStatus("current")


class _AcdCfmMepCfgCciEnable_Type(TruthValue):
    """Custom type acdCfmMepCfgCciEnable based on TruthValue"""


_AcdCfmMepCfgCciEnable_Object = MibTableColumn
acdCfmMepCfgCciEnable = _AcdCfmMepCfgCciEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 12),
    _AcdCfmMepCfgCciEnable_Type()
)
acdCfmMepCfgCciEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmMepCfgCciEnable.setStatus("current")


class _AcdCfmMepCfgCcmSeqEnable_Type(TruthValue):
    """Custom type acdCfmMepCfgCcmSeqEnable based on TruthValue"""


_AcdCfmMepCfgCcmSeqEnable_Object = MibTableColumn
acdCfmMepCfgCcmSeqEnable = _AcdCfmMepCfgCcmSeqEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 13),
    _AcdCfmMepCfgCcmSeqEnable_Type()
)
acdCfmMepCfgCcmSeqEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmMepCfgCcmSeqEnable.setStatus("current")


class _AcdCfmMepCfgPriority_Type(Unsigned32):
    """Custom type acdCfmMepCfgPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdCfmMepCfgPriority_Type.__name__ = "Unsigned32"
_AcdCfmMepCfgPriority_Object = MibTableColumn
acdCfmMepCfgPriority = _AcdCfmMepCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 14),
    _AcdCfmMepCfgPriority_Type()
)
acdCfmMepCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmMepCfgPriority.setStatus("current")
_AcdCfmMepCfgAlarmPri_Type = AcdCfmMepLowestAlarmPri
_AcdCfmMepCfgAlarmPri_Object = MibTableColumn
acdCfmMepCfgAlarmPri = _AcdCfmMepCfgAlarmPri_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 15),
    _AcdCfmMepCfgAlarmPri_Type()
)
acdCfmMepCfgAlarmPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmMepCfgAlarmPri.setStatus("current")


class _AcdCfmMepCfgFngAlarmTime_Type(Unsigned32):
    """Custom type acdCfmMepCfgFngAlarmTime based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2500, 10000),
    )


_AcdCfmMepCfgFngAlarmTime_Type.__name__ = "Unsigned32"
_AcdCfmMepCfgFngAlarmTime_Object = MibTableColumn
acdCfmMepCfgFngAlarmTime = _AcdCfmMepCfgFngAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 16),
    _AcdCfmMepCfgFngAlarmTime_Type()
)
acdCfmMepCfgFngAlarmTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmMepCfgFngAlarmTime.setStatus("current")


class _AcdCfmMepCfgFngResetTime_Type(Unsigned32):
    """Custom type acdCfmMepCfgFngResetTime based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2500, 10000),
    )


_AcdCfmMepCfgFngResetTime_Type.__name__ = "Unsigned32"
_AcdCfmMepCfgFngResetTime_Object = MibTableColumn
acdCfmMepCfgFngResetTime = _AcdCfmMepCfgFngResetTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 17),
    _AcdCfmMepCfgFngResetTime_Type()
)
acdCfmMepCfgFngResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmMepCfgFngResetTime.setStatus("current")


class _AcdCfmMepCfgFpEnable_Type(TruthValue):
    """Custom type acdCfmMepCfgFpEnable based on TruthValue"""


_AcdCfmMepCfgFpEnable_Object = MibTableColumn
acdCfmMepCfgFpEnable = _AcdCfmMepCfgFpEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 18),
    _AcdCfmMepCfgFpEnable_Type()
)
acdCfmMepCfgFpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmMepCfgFpEnable.setStatus("current")


class _AcdCfmMepCfgFpPortId_Type(Unsigned32):
    """Custom type acdCfmMepCfgFpPortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdCfmMepCfgFpPortId_Type.__name__ = "Unsigned32"
_AcdCfmMepCfgFpPortId_Object = MibTableColumn
acdCfmMepCfgFpPortId = _AcdCfmMepCfgFpPortId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 19),
    _AcdCfmMepCfgFpPortId_Type()
)
acdCfmMepCfgFpPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmMepCfgFpPortId.setStatus("current")


class _AcdCfmMepCfgCsfEnable_Type(TruthValue):
    """Custom type acdCfmMepCfgCsfEnable based on TruthValue"""


_AcdCfmMepCfgCsfEnable_Object = MibTableColumn
acdCfmMepCfgCsfEnable = _AcdCfmMepCfgCsfEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 3, 5, 1, 20),
    _AcdCfmMepCfgCsfEnable_Type()
)
acdCfmMepCfgCsfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdCfmMepCfgCsfEnable.setStatus("current")
_AcdCfmStack_ObjectIdentity = ObjectIdentity
acdCfmStack = _AcdCfmStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 4)
)
_AcdCfmStackTable_Object = MibTable
acdCfmStackTable = _AcdCfmStackTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    acdCfmStackTable.setStatus("current")
_AcdCfmStackEntry_Object = MibTableRow
acdCfmStackEntry = _AcdCfmStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 4, 1, 1)
)
acdCfmStackEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmMdIdx"),
    (0, "ACD-CFM-MIB", "acdCfmMaIdx"),
    (0, "ACD-CFM-MIB", "acdCfmMepID"),
)
if mibBuilder.loadTexts:
    acdCfmStackEntry.setStatus("current")
_AcdCfmMdIdx_Type = Unsigned32
_AcdCfmMdIdx_Object = MibTableColumn
acdCfmMdIdx = _AcdCfmMdIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 4, 1, 1, 1),
    _AcdCfmMdIdx_Type()
)
acdCfmMdIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmMdIdx.setStatus("current")
_AcdCfmMaIdx_Type = Unsigned32
_AcdCfmMaIdx_Object = MibTableColumn
acdCfmMaIdx = _AcdCfmMaIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 4, 1, 1, 2),
    _AcdCfmMaIdx_Type()
)
acdCfmMaIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmMaIdx.setStatus("current")


class _AcdCfmMepID_Type(Unsigned32):
    """Custom type acdCfmMepID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AcdCfmMepID_Type.__name__ = "Unsigned32"
_AcdCfmMepID_Object = MibTableColumn
acdCfmMepID = _AcdCfmMepID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 4, 1, 1, 3),
    _AcdCfmMepID_Type()
)
acdCfmMepID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmMepID.setStatus("current")
_AcdCfmMepIdx_Type = Unsigned32
_AcdCfmMepIdx_Object = MibTableColumn
acdCfmMepIdx = _AcdCfmMepIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 4, 1, 1, 4),
    _AcdCfmMepIdx_Type()
)
acdCfmMepIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmMepIdx.setStatus("current")
_AcdCfmSlm_ObjectIdentity = ObjectIdentity
acdCfmSlm = _AcdCfmSlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5)
)
_AcdCfmSlmCfgTable_Object = MibTable
acdCfmSlmCfgTable = _AcdCfmSlmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1)
)
if mibBuilder.loadTexts:
    acdCfmSlmCfgTable.setStatus("current")
_AcdCfmSlmCfgEntry_Object = MibTableRow
acdCfmSlmCfgEntry = _AcdCfmSlmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1, 1)
)
acdCfmSlmCfgEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmSlmCfgID"),
)
if mibBuilder.loadTexts:
    acdCfmSlmCfgEntry.setStatus("current")
_AcdCfmSlmCfgID_Type = Unsigned32
_AcdCfmSlmCfgID_Object = MibTableColumn
acdCfmSlmCfgID = _AcdCfmSlmCfgID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1, 1, 1),
    _AcdCfmSlmCfgID_Type()
)
acdCfmSlmCfgID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmSlmCfgID.setStatus("current")
_AcdCfmSlmCfgRowStatus_Type = RowStatus
_AcdCfmSlmCfgRowStatus_Object = MibTableColumn
acdCfmSlmCfgRowStatus = _AcdCfmSlmCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1, 1, 2),
    _AcdCfmSlmCfgRowStatus_Type()
)
acdCfmSlmCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmCfgRowStatus.setStatus("current")
_AcdCfmSlmCfgMepIdx_Type = Unsigned32
_AcdCfmSlmCfgMepIdx_Object = MibTableColumn
acdCfmSlmCfgMepIdx = _AcdCfmSlmCfgMepIdx_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1, 1, 3),
    _AcdCfmSlmCfgMepIdx_Type()
)
acdCfmSlmCfgMepIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmCfgMepIdx.setStatus("current")


class _AcdCfmSlmCfgRemoteMepId_Type(Unsigned32):
    """Custom type acdCfmSlmCfgRemoteMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AcdCfmSlmCfgRemoteMepId_Type.__name__ = "Unsigned32"
_AcdCfmSlmCfgRemoteMepId_Object = MibTableColumn
acdCfmSlmCfgRemoteMepId = _AcdCfmSlmCfgRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1, 1, 4),
    _AcdCfmSlmCfgRemoteMepId_Type()
)
acdCfmSlmCfgRemoteMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmCfgRemoteMepId.setStatus("current")


class _AcdCfmSlmCfgPriority_Type(Unsigned32):
    """Custom type acdCfmSlmCfgPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdCfmSlmCfgPriority_Type.__name__ = "Unsigned32"
_AcdCfmSlmCfgPriority_Object = MibTableColumn
acdCfmSlmCfgPriority = _AcdCfmSlmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1, 1, 5),
    _AcdCfmSlmCfgPriority_Type()
)
acdCfmSlmCfgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmCfgPriority.setStatus("current")


class _AcdCfmSlmCfgState_Type(TruthValue):
    """Custom type acdCfmSlmCfgState based on TruthValue"""


_AcdCfmSlmCfgState_Object = MibTableColumn
acdCfmSlmCfgState = _AcdCfmSlmCfgState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1, 1, 6),
    _AcdCfmSlmCfgState_Type()
)
acdCfmSlmCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmCfgState.setStatus("current")


class _AcdCfmSlmCfgInterval_Type(Unsigned32):
    """Custom type acdCfmSlmCfgInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AcdCfmSlmCfgInterval_Type.__name__ = "Unsigned32"
_AcdCfmSlmCfgInterval_Object = MibTableColumn
acdCfmSlmCfgInterval = _AcdCfmSlmCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1, 1, 7),
    _AcdCfmSlmCfgInterval_Type()
)
acdCfmSlmCfgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmCfgInterval.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmSlmCfgInterval.setUnits("milliseconds")


class _AcdCfmSlmCfgRefPeriod_Type(Unsigned32):
    """Custom type acdCfmSlmCfgRefPeriod based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_AcdCfmSlmCfgRefPeriod_Type.__name__ = "Unsigned32"
_AcdCfmSlmCfgRefPeriod_Object = MibTableColumn
acdCfmSlmCfgRefPeriod = _AcdCfmSlmCfgRefPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1, 1, 8),
    _AcdCfmSlmCfgRefPeriod_Type()
)
acdCfmSlmCfgRefPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmCfgRefPeriod.setStatus("current")
if mibBuilder.loadTexts:
    acdCfmSlmCfgRefPeriod.setUnits("minutes")


class _AcdCfmSlmCfgNearEndThresh_Type(Unsigned32):
    """Custom type acdCfmSlmCfgNearEndThresh based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdCfmSlmCfgNearEndThresh_Type.__name__ = "Unsigned32"
_AcdCfmSlmCfgNearEndThresh_Object = MibTableColumn
acdCfmSlmCfgNearEndThresh = _AcdCfmSlmCfgNearEndThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1, 1, 9),
    _AcdCfmSlmCfgNearEndThresh_Type()
)
acdCfmSlmCfgNearEndThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmCfgNearEndThresh.setStatus("current")


class _AcdCfmSlmCfgFarEndThresh_Type(Unsigned32):
    """Custom type acdCfmSlmCfgFarEndThresh based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdCfmSlmCfgFarEndThresh_Type.__name__ = "Unsigned32"
_AcdCfmSlmCfgFarEndThresh_Object = MibTableColumn
acdCfmSlmCfgFarEndThresh = _AcdCfmSlmCfgFarEndThresh_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1, 1, 10),
    _AcdCfmSlmCfgFarEndThresh_Type()
)
acdCfmSlmCfgFarEndThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmCfgFarEndThresh.setStatus("current")


class _AcdCfmSlmCfgName_Type(DisplayString):
    """Custom type acdCfmSlmCfgName based on DisplayString"""
    defaultValue = OctetString("new")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdCfmSlmCfgName_Type.__name__ = "DisplayString"
_AcdCfmSlmCfgName_Object = MibTableColumn
acdCfmSlmCfgName = _AcdCfmSlmCfgName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 1, 1, 11),
    _AcdCfmSlmCfgName_Type()
)
acdCfmSlmCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmCfgName.setStatus("current")
_AcdCfmSlmResultTable_Object = MibTable
acdCfmSlmResultTable = _AcdCfmSlmResultTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2)
)
if mibBuilder.loadTexts:
    acdCfmSlmResultTable.setStatus("current")
_AcdCfmSlmResultEntry_Object = MibTableRow
acdCfmSlmResultEntry = _AcdCfmSlmResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1)
)
acdCfmSlmResultEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmSlmResultID"),
)
if mibBuilder.loadTexts:
    acdCfmSlmResultEntry.setStatus("current")
_AcdCfmSlmResultID_Type = Unsigned32
_AcdCfmSlmResultID_Object = MibTableColumn
acdCfmSlmResultID = _AcdCfmSlmResultID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 1),
    _AcdCfmSlmResultID_Type()
)
acdCfmSlmResultID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmSlmResultID.setStatus("current")
_AcdCfmSlmResultPeriodIndex_Type = Unsigned32
_AcdCfmSlmResultPeriodIndex_Object = MibTableColumn
acdCfmSlmResultPeriodIndex = _AcdCfmSlmResultPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 2),
    _AcdCfmSlmResultPeriodIndex_Type()
)
acdCfmSlmResultPeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultPeriodIndex.setStatus("current")
_AcdCfmSlmResultIntervalStart_Type = DateAndTime
_AcdCfmSlmResultIntervalStart_Object = MibTableColumn
acdCfmSlmResultIntervalStart = _AcdCfmSlmResultIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 3),
    _AcdCfmSlmResultIntervalStart_Type()
)
acdCfmSlmResultIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultIntervalStart.setStatus("current")
_AcdCfmSlmResultValid_Type = TruthValue
_AcdCfmSlmResultValid_Object = MibTableColumn
acdCfmSlmResultValid = _AcdCfmSlmResultValid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 4),
    _AcdCfmSlmResultValid_Type()
)
acdCfmSlmResultValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultValid.setStatus("current")
_AcdCfmSlmResultNearEndAlert_Type = TruthValue
_AcdCfmSlmResultNearEndAlert_Object = MibTableColumn
acdCfmSlmResultNearEndAlert = _AcdCfmSlmResultNearEndAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 5),
    _AcdCfmSlmResultNearEndAlert_Type()
)
acdCfmSlmResultNearEndAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultNearEndAlert.setStatus("current")
_AcdCfmSlmResultFarEndAlert_Type = TruthValue
_AcdCfmSlmResultFarEndAlert_Object = MibTableColumn
acdCfmSlmResultFarEndAlert = _AcdCfmSlmResultFarEndAlert_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 6),
    _AcdCfmSlmResultFarEndAlert_Type()
)
acdCfmSlmResultFarEndAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultFarEndAlert.setStatus("current")
_AcdCfmSlmResultTxSlm_Type = Counter32
_AcdCfmSlmResultTxSlm_Object = MibTableColumn
acdCfmSlmResultTxSlm = _AcdCfmSlmResultTxSlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 7),
    _AcdCfmSlmResultTxSlm_Type()
)
acdCfmSlmResultTxSlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultTxSlm.setStatus("current")
_AcdCfmSlmResultRxSlr_Type = Counter32
_AcdCfmSlmResultRxSlr_Object = MibTableColumn
acdCfmSlmResultRxSlr = _AcdCfmSlmResultRxSlr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 8),
    _AcdCfmSlmResultRxSlr_Type()
)
acdCfmSlmResultRxSlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultRxSlr.setStatus("current")
_AcdCfmSlmResultRemoteRxSlm_Type = Counter32
_AcdCfmSlmResultRemoteRxSlm_Object = MibTableColumn
acdCfmSlmResultRemoteRxSlm = _AcdCfmSlmResultRemoteRxSlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 9),
    _AcdCfmSlmResultRemoteRxSlm_Type()
)
acdCfmSlmResultRemoteRxSlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultRemoteRxSlm.setStatus("current")
_AcdCfmSlmResultNearEndNbrLoss_Type = Counter32
_AcdCfmSlmResultNearEndNbrLoss_Object = MibTableColumn
acdCfmSlmResultNearEndNbrLoss = _AcdCfmSlmResultNearEndNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 10),
    _AcdCfmSlmResultNearEndNbrLoss_Type()
)
acdCfmSlmResultNearEndNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultNearEndNbrLoss.setStatus("current")
_AcdCfmSlmResultFarEndNbrLoss_Type = Counter32
_AcdCfmSlmResultFarEndNbrLoss_Object = MibTableColumn
acdCfmSlmResultFarEndNbrLoss = _AcdCfmSlmResultFarEndNbrLoss_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 11),
    _AcdCfmSlmResultFarEndNbrLoss_Type()
)
acdCfmSlmResultFarEndNbrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultFarEndNbrLoss.setStatus("current")
_AcdCfmSlmResultNearEndRatio_Type = Gauge32
_AcdCfmSlmResultNearEndRatio_Object = MibTableColumn
acdCfmSlmResultNearEndRatio = _AcdCfmSlmResultNearEndRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 12),
    _AcdCfmSlmResultNearEndRatio_Type()
)
acdCfmSlmResultNearEndRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultNearEndRatio.setStatus("current")
_AcdCfmSlmResultFarEndRatio_Type = Gauge32
_AcdCfmSlmResultFarEndRatio_Object = MibTableColumn
acdCfmSlmResultFarEndRatio = _AcdCfmSlmResultFarEndRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 13),
    _AcdCfmSlmResultFarEndRatio_Type()
)
acdCfmSlmResultFarEndRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultFarEndRatio.setStatus("current")
_AcdCfmSlmResultNbrGaps_Type = Counter32
_AcdCfmSlmResultNbrGaps_Object = MibTableColumn
acdCfmSlmResultNbrGaps = _AcdCfmSlmResultNbrGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 14),
    _AcdCfmSlmResultNbrGaps_Type()
)
acdCfmSlmResultNbrGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultNbrGaps.setStatus("current")
_AcdCfmSlmResultLargestGap_Type = Counter32
_AcdCfmSlmResultLargestGap_Object = MibTableColumn
acdCfmSlmResultLargestGap = _AcdCfmSlmResultLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 15),
    _AcdCfmSlmResultLargestGap_Type()
)
acdCfmSlmResultLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultLargestGap.setStatus("current")


class _AcdCfmSlmResultName_Type(DisplayString):
    """Custom type acdCfmSlmResultName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmSlmResultName_Type.__name__ = "DisplayString"
_AcdCfmSlmResultName_Object = MibTableColumn
acdCfmSlmResultName = _AcdCfmSlmResultName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 2, 1, 16),
    _AcdCfmSlmResultName_Type()
)
acdCfmSlmResultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmResultName.setStatus("current")
_AcdCfmSlmHistResultTable_Object = MibTable
acdCfmSlmHistResultTable = _AcdCfmSlmHistResultTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3)
)
if mibBuilder.loadTexts:
    acdCfmSlmHistResultTable.setStatus("current")
_AcdCfmSlmHistResultEntry_Object = MibTableRow
acdCfmSlmHistResultEntry = _AcdCfmSlmHistResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1)
)
acdCfmSlmHistResultEntry.setIndexNames(
    (0, "ACD-CFM-MIB", "acdCfmSlmHistResultInstanceIndex"),
    (0, "ACD-CFM-MIB", "acdCfmSlmHistResultID"),
)
if mibBuilder.loadTexts:
    acdCfmSlmHistResultEntry.setStatus("current")
_AcdCfmSlmHistResultID_Type = Unsigned32
_AcdCfmSlmHistResultID_Object = MibTableColumn
acdCfmSlmHistResultID = _AcdCfmSlmHistResultID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1, 1),
    _AcdCfmSlmHistResultID_Type()
)
acdCfmSlmHistResultID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmSlmHistResultID.setStatus("current")
_AcdCfmSlmHistResultPeriodIndex_Type = Unsigned32
_AcdCfmSlmHistResultPeriodIndex_Object = MibTableColumn
acdCfmSlmHistResultPeriodIndex = _AcdCfmSlmHistResultPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1, 2),
    _AcdCfmSlmHistResultPeriodIndex_Type()
)
acdCfmSlmHistResultPeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmHistResultPeriodIndex.setStatus("current")
_AcdCfmSlmHistResultIntervalEnd_Type = DateAndTime
_AcdCfmSlmHistResultIntervalEnd_Object = MibTableColumn
acdCfmSlmHistResultIntervalEnd = _AcdCfmSlmHistResultIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1, 3),
    _AcdCfmSlmHistResultIntervalEnd_Type()
)
acdCfmSlmHistResultIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmHistResultIntervalEnd.setStatus("current")
_AcdCfmSlmHistResultTxSlm_Type = Counter32
_AcdCfmSlmHistResultTxSlm_Object = MibTableColumn
acdCfmSlmHistResultTxSlm = _AcdCfmSlmHistResultTxSlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1, 4),
    _AcdCfmSlmHistResultTxSlm_Type()
)
acdCfmSlmHistResultTxSlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmHistResultTxSlm.setStatus("current")
_AcdCfmSlmHistResultRxSlr_Type = Counter32
_AcdCfmSlmHistResultRxSlr_Object = MibTableColumn
acdCfmSlmHistResultRxSlr = _AcdCfmSlmHistResultRxSlr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1, 5),
    _AcdCfmSlmHistResultRxSlr_Type()
)
acdCfmSlmHistResultRxSlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmHistResultRxSlr.setStatus("current")
_AcdCfmSlmHistResultRemoteRxSlm_Type = Counter32
_AcdCfmSlmHistResultRemoteRxSlm_Object = MibTableColumn
acdCfmSlmHistResultRemoteRxSlm = _AcdCfmSlmHistResultRemoteRxSlm_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1, 6),
    _AcdCfmSlmHistResultRemoteRxSlm_Type()
)
acdCfmSlmHistResultRemoteRxSlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmHistResultRemoteRxSlm.setStatus("current")
_AcdCfmSlmHistResultNearEndRatio_Type = Gauge32
_AcdCfmSlmHistResultNearEndRatio_Object = MibTableColumn
acdCfmSlmHistResultNearEndRatio = _AcdCfmSlmHistResultNearEndRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1, 7),
    _AcdCfmSlmHistResultNearEndRatio_Type()
)
acdCfmSlmHistResultNearEndRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmHistResultNearEndRatio.setStatus("current")
_AcdCfmSlmHistResultFarEndRatio_Type = Gauge32
_AcdCfmSlmHistResultFarEndRatio_Object = MibTableColumn
acdCfmSlmHistResultFarEndRatio = _AcdCfmSlmHistResultFarEndRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1, 8),
    _AcdCfmSlmHistResultFarEndRatio_Type()
)
acdCfmSlmHistResultFarEndRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmHistResultFarEndRatio.setStatus("current")
_AcdCfmSlmHistResultNbrGaps_Type = Counter32
_AcdCfmSlmHistResultNbrGaps_Object = MibTableColumn
acdCfmSlmHistResultNbrGaps = _AcdCfmSlmHistResultNbrGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1, 9),
    _AcdCfmSlmHistResultNbrGaps_Type()
)
acdCfmSlmHistResultNbrGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmHistResultNbrGaps.setStatus("current")
_AcdCfmSlmHistResultLargestGap_Type = Counter32
_AcdCfmSlmHistResultLargestGap_Object = MibTableColumn
acdCfmSlmHistResultLargestGap = _AcdCfmSlmHistResultLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1, 10),
    _AcdCfmSlmHistResultLargestGap_Type()
)
acdCfmSlmHistResultLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmHistResultLargestGap.setStatus("current")
_AcdCfmSlmHistResultInstanceIndex_Type = Unsigned32
_AcdCfmSlmHistResultInstanceIndex_Object = MibTableColumn
acdCfmSlmHistResultInstanceIndex = _AcdCfmSlmHistResultInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1, 11),
    _AcdCfmSlmHistResultInstanceIndex_Type()
)
acdCfmSlmHistResultInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdCfmSlmHistResultInstanceIndex.setStatus("current")


class _AcdCfmSlmHistResultName_Type(DisplayString):
    """Custom type acdCfmSlmHistResultName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdCfmSlmHistResultName_Type.__name__ = "DisplayString"
_AcdCfmSlmHistResultName_Object = MibTableColumn
acdCfmSlmHistResultName = _AcdCfmSlmHistResultName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 1, 5, 3, 1, 12),
    _AcdCfmSlmHistResultName_Type()
)
acdCfmSlmHistResultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdCfmSlmHistResultName.setStatus("current")
_AcdCfmConformance_ObjectIdentity = ObjectIdentity
acdCfmConformance = _AcdCfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2)
)
_AcdCfmCompliances_ObjectIdentity = ObjectIdentity
acdCfmCompliances = _AcdCfmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 1)
)
_AcdCfmGroups_ObjectIdentity = ObjectIdentity
acdCfmGroups = _AcdCfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2)
)

# Managed Objects groups

acdCfmDmCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 1)
)
acdCfmDmCfgGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmDmCfgRowStatus"),
        ("ACD-CFM-MIB", "acdCfmDmCfgMepIdx"),
        ("ACD-CFM-MIB", "acdCfmDmCfgRemoteMepId"),
        ("ACD-CFM-MIB", "acdCfmDmCfgPriority"),
        ("ACD-CFM-MIB", "acdCfmDmCfgEnable"),
        ("ACD-CFM-MIB", "acdCfmDmCfgInterval"),
        ("ACD-CFM-MIB", "acdCfmDmCfgRefPeriod"),
        ("ACD-CFM-MIB", "acdCfmDmCfgOneWayDelayEnable"),
        ("ACD-CFM-MIB", "acdCfmDmCfgOneWayDelayMax"),
        ("ACD-CFM-MIB", "acdCfmDmCfgOneWayDelayThresh"),
        ("ACD-CFM-MIB", "acdCfmDmCfgOneWayAvgDelayThresh"),
        ("ACD-CFM-MIB", "acdCfmDmCfgOneWayDvEnable"),
        ("ACD-CFM-MIB", "acdCfmDmCfgOneWayDvMax"),
        ("ACD-CFM-MIB", "acdCfmDmCfgOneWayDvThresh"),
        ("ACD-CFM-MIB", "acdCfmDmCfgOneWayAvgDvThresh"),
        ("ACD-CFM-MIB", "acdCfmDmCfgTwoWayDelayEnable"),
        ("ACD-CFM-MIB", "acdCfmDmCfgTwoWayDelayMax"),
        ("ACD-CFM-MIB", "acdCfmDmCfgTwoWayDelayThresh"),
        ("ACD-CFM-MIB", "acdCfmDmCfgTwoWayAvgDelayThresh"),
        ("ACD-CFM-MIB", "acdCfmDmCfgTwoWayDvEnable"),
        ("ACD-CFM-MIB", "acdCfmDmCfgTwoWayDvMax"),
        ("ACD-CFM-MIB", "acdCfmDmCfgTwoWayDvThresh"),
        ("ACD-CFM-MIB", "acdCfmDmCfgTwoWayAvgDvThresh"),
        ("ACD-CFM-MIB", "acdCfmDmCfgName"))
)
if mibBuilder.loadTexts:
    acdCfmDmCfgGroup.setStatus("current")

acdCfmResultOneWayDelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 2)
)
acdCfmResultOneWayDelayGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmResultOneWayDelayPeriodIndex"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDelayIntervalStart"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDelayValid"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDelayAlert"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDelayAvgAlert"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDelaySamples"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDelayMinValue"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDelayMaxValue"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDelayAvgValue"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDelayThreshExc"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDelayInstValue"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDelayName"))
)
if mibBuilder.loadTexts:
    acdCfmResultOneWayDelayGroup.setStatus("current")

acdCfmResultOneWayDvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 3)
)
acdCfmResultOneWayDvGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmResultOneWayDvPeriodIndex"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDvIntervalStart"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDvValid"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDvAlert"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDvAvgAlert"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDvSamples"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDvMinValue"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDvMaxValue"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDvAvgValue"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDvThreshExc"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDvInstValue"),
        ("ACD-CFM-MIB", "acdCfmResultOneWayDvName"))
)
if mibBuilder.loadTexts:
    acdCfmResultOneWayDvGroup.setStatus("current")

acdCfmResultTwoWayDelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 4)
)
acdCfmResultTwoWayDelayGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmResultTwoWayDelayPeriodIndex"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDelayIntervalStart"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDelayValid"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDelayAlert"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDelayAvgAlert"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDelaySamples"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDelayMinValue"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDelayMaxValue"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDelayAvgValue"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDelayThreshExc"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDelayInstValue"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDelayName"))
)
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDelayGroup.setStatus("current")

acdCfmResultTwoWayDvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 5)
)
acdCfmResultTwoWayDvGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmResultTwoWayDvPeriodIndex"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDvIntervalStart"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDvValid"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDvAlert"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDvAvgAlert"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDvSamples"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDvMinValue"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDvMaxValue"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDvAvgValue"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDvThreshExc"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDvInstValue"),
        ("ACD-CFM-MIB", "acdCfmResultTwoWayDvName"))
)
if mibBuilder.loadTexts:
    acdCfmResultTwoWayDvGroup.setStatus("current")

acdCfmHistResultOneWayDelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 6)
)
acdCfmHistResultOneWayDelayGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmHistResultOneWayDelayStatus"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDelayDuration"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDelayIntervalEnd"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDelaySamples"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDelayMinValue"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDelayMaxValue"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDelayAvgValue"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDelayThreshExc"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDelayName"))
)
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDelayGroup.setStatus("current")

acdCfmHistResultOneWayDvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 7)
)
acdCfmHistResultOneWayDvGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmHistResultOneWayDvStatus"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDvDuration"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDvIntervalEnd"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDvSamples"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDvMinValue"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDvMaxValue"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDvAvgValue"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDvThreshExc"),
        ("ACD-CFM-MIB", "acdCfmHistResultOneWayDvName"))
)
if mibBuilder.loadTexts:
    acdCfmHistResultOneWayDvGroup.setStatus("current")

acdCfmHistResultTwoWayDelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 8)
)
acdCfmHistResultTwoWayDelayGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmHistResultTwoWayDelayStatus"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDelayDuration"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDelayIntervalEnd"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDelaySamples"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDelayMinValue"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDelayMaxValue"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDelayAvgValue"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDelayThreshExc"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDelayName"))
)
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDelayGroup.setStatus("current")

acdCfmHistResultTwoWayDvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 9)
)
acdCfmHistResultTwoWayDvGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmHistResultTwoWayDvStatus"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDvDuration"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDvIntervalEnd"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDvSamples"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDvMinValue"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDvMaxValue"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDvAvgValue"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDvThreshExc"),
        ("ACD-CFM-MIB", "acdCfmHistResultTwoWayDvName"))
)
if mibBuilder.loadTexts:
    acdCfmHistResultTwoWayDvGroup.setStatus("current")

acdCfmPktLossCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 10)
)
acdCfmPktLossCfgGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmPktLossCfgRowStatus"),
        ("ACD-CFM-MIB", "acdCfmPktLossCfgMepIdx"),
        ("ACD-CFM-MIB", "acdCfmPktLossCfgRemoteMepId"),
        ("ACD-CFM-MIB", "acdCfmPktLossCfgPriority"),
        ("ACD-CFM-MIB", "acdCfmPktLossCfgEnable"),
        ("ACD-CFM-MIB", "acdCfmPktLossCfgInterval"),
        ("ACD-CFM-MIB", "acdCfmPktLossCfgRefPeriod"),
        ("ACD-CFM-MIB", "acdCfmPktLossCfgThresh"),
        ("ACD-CFM-MIB", "acdCfmPktLossCfgRatioThresh"),
        ("ACD-CFM-MIB", "acdCfmPktLossCfgName"))
)
if mibBuilder.loadTexts:
    acdCfmPktLossCfgGroup.setStatus("current")

acdCfmResultPktLossGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 11)
)
acdCfmResultPktLossGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmResultPktLossPeriodIndex"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossIntervalStart"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossValid"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossAlert"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossSamples"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossOverflowSamples"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossHCSamples"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossNbrLoss"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossOverflowNbrLoss"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossHCNbrLoss"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossNbrGaps"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossOverflowNbrGaps"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossHCNbrGaps"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossLargestGap"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossOverflowLargestGap"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossHCLargestGap"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossRatio"),
        ("ACD-CFM-MIB", "acdCfmResultPktLossName"))
)
if mibBuilder.loadTexts:
    acdCfmResultPktLossGroup.setStatus("current")

acdCfmHistResultPktLossGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 12)
)
acdCfmHistResultPktLossGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmHistResultPktLossStatus"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossDuration"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossIntervalEnd"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossSamples"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossOverflowSamples"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossHCSamples"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossNbrLoss"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossOverflowNbrLoss"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossHCNbrLoss"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossNbrGaps"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossOverflowNbrGaps"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossHCNbrGaps"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossLargestGap"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossOverflowLargestGap"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossHCLargestGap"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossRatio"),
        ("ACD-CFM-MIB", "acdCfmHistResultPktLossName"))
)
if mibBuilder.loadTexts:
    acdCfmHistResultPktLossGroup.setStatus("current")

acdCfmMepStatsTxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 13)
)
acdCfmMepStatsTxGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmMepStatsTxCcmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxLbmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxLbrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxLtmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxLtrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxAisPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxLckPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxTstPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxLinearApsPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxRingApsPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxMccPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxLmmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxLmrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTx1dmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxDmmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxDmrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxExmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxExrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxVsmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxVsrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxCsfPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxSlmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxSlrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxName"))
)
if mibBuilder.loadTexts:
    acdCfmMepStatsTxGroup.setStatus("current")

acdCfmMepStatsRxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 14)
)
acdCfmMepStatsRxGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmMepStatsRxCcmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLbmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLbrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLtmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLtrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxAisPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLckPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxTstPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLinearApsPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxRingApsPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxMccPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLmmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLmrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRx1dmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxDmmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxDmrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxExmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxExrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxVsmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxVsrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxCcmSeqErrors"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLtrUnexpectedPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLtrMacErrors"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLbrOooErrors"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLbrUnexpectedPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxLbrDataErrors"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxCsfPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxSlrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxCsfInvalidFlags"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxName"))
)
if mibBuilder.loadTexts:
    acdCfmMepStatsRxGroup.setStatus("current")

acdCfmMepDmStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 15)
)
acdCfmMepDmStatsGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmMepDmStatsTxDmmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepDmStatsRxDmmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepDmStatsTxDmrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepDmStatsRxDmrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepDmStatsName"))
)
if mibBuilder.loadTexts:
    acdCfmMepDmStatsGroup.setStatus("current")

acdCfmMepStackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 16)
)
acdCfmMepStackGroup.setObjects(
    ("ACD-CFM-MIB", "acdCfmMepIdx")
)
if mibBuilder.loadTexts:
    acdCfmMepStackGroup.setStatus("current")

acdCfmMepSlmStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 17)
)
acdCfmMepSlmStatsGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmMepStatsTxSlmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxSlmPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsTxSlrPdu"),
        ("ACD-CFM-MIB", "acdCfmMepStatsRxSlrPdu"))
)
if mibBuilder.loadTexts:
    acdCfmMepSlmStatsGroup.setStatus("current")

acdCfmSlmCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 18)
)
acdCfmSlmCfgGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmSlmCfgRowStatus"),
        ("ACD-CFM-MIB", "acdCfmSlmCfgMepIdx"),
        ("ACD-CFM-MIB", "acdCfmSlmCfgRemoteMepId"),
        ("ACD-CFM-MIB", "acdCfmSlmCfgPriority"),
        ("ACD-CFM-MIB", "acdCfmSlmCfgState"),
        ("ACD-CFM-MIB", "acdCfmSlmCfgInterval"),
        ("ACD-CFM-MIB", "acdCfmSlmCfgRefPeriod"),
        ("ACD-CFM-MIB", "acdCfmSlmCfgNearEndThresh"),
        ("ACD-CFM-MIB", "acdCfmSlmCfgFarEndThresh"),
        ("ACD-CFM-MIB", "acdCfmSlmCfgName"))
)
if mibBuilder.loadTexts:
    acdCfmSlmCfgGroup.setStatus("current")

acdCfmSlmResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 19)
)
acdCfmSlmResultGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmSlmResultPeriodIndex"),
        ("ACD-CFM-MIB", "acdCfmSlmResultIntervalStart"),
        ("ACD-CFM-MIB", "acdCfmSlmResultValid"),
        ("ACD-CFM-MIB", "acdCfmSlmResultNearEndAlert"),
        ("ACD-CFM-MIB", "acdCfmSlmResultFarEndAlert"),
        ("ACD-CFM-MIB", "acdCfmSlmResultTxSlm"),
        ("ACD-CFM-MIB", "acdCfmSlmResultRxSlr"),
        ("ACD-CFM-MIB", "acdCfmSlmResultRemoteRxSlm"),
        ("ACD-CFM-MIB", "acdCfmSlmResultNearEndNbrLoss"),
        ("ACD-CFM-MIB", "acdCfmSlmResultFarEndNbrLoss"),
        ("ACD-CFM-MIB", "acdCfmSlmResultNearEndRatio"),
        ("ACD-CFM-MIB", "acdCfmSlmResultFarEndRatio"),
        ("ACD-CFM-MIB", "acdCfmSlmResultNbrGaps"),
        ("ACD-CFM-MIB", "acdCfmSlmResultLargestGap"),
        ("ACD-CFM-MIB", "acdCfmSlmResultName"))
)
if mibBuilder.loadTexts:
    acdCfmSlmResultGroup.setStatus("current")

acdCfmSlmHistResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 20)
)
acdCfmSlmHistResultGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmSlmHistResultPeriodIndex"),
        ("ACD-CFM-MIB", "acdCfmSlmHistResultIntervalEnd"),
        ("ACD-CFM-MIB", "acdCfmSlmHistResultTxSlm"),
        ("ACD-CFM-MIB", "acdCfmSlmHistResultRxSlr"),
        ("ACD-CFM-MIB", "acdCfmSlmHistResultRemoteRxSlm"),
        ("ACD-CFM-MIB", "acdCfmSlmHistResultNearEndRatio"),
        ("ACD-CFM-MIB", "acdCfmSlmHistResultFarEndRatio"),
        ("ACD-CFM-MIB", "acdCfmSlmHistResultNbrGaps"),
        ("ACD-CFM-MIB", "acdCfmSlmHistResultLargestGap"),
        ("ACD-CFM-MIB", "acdCfmSlmHistResultName"))
)
if mibBuilder.loadTexts:
    acdCfmSlmHistResultGroup.setStatus("current")

acdCfmMepCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 2, 21)
)
acdCfmMepCfgGroup.setObjects(
      *(("ACD-CFM-MIB", "acdCfmMepCfgRowStatus"),
        ("ACD-CFM-MIB", "acdCfmMepCfgMdIdx"),
        ("ACD-CFM-MIB", "acdCfmMepCfgMaIdx"),
        ("ACD-CFM-MIB", "acdCfmMepCfgMepId"),
        ("ACD-CFM-MIB", "acdCfmMepCfgName"),
        ("ACD-CFM-MIB", "acdCfmMepCfgPortId"),
        ("ACD-CFM-MIB", "acdCfmMepCfgPortIdMacAddr"),
        ("ACD-CFM-MIB", "acdCfmMepCfgDirection"),
        ("ACD-CFM-MIB", "acdCfmMepCfgPrimaryVid"),
        ("ACD-CFM-MIB", "acdCfmMepCfgActive"),
        ("ACD-CFM-MIB", "acdCfmMepCfgCciEnable"),
        ("ACD-CFM-MIB", "acdCfmMepCfgCcmSeqEnable"),
        ("ACD-CFM-MIB", "acdCfmMepCfgPriority"),
        ("ACD-CFM-MIB", "acdCfmMepCfgAlarmPri"),
        ("ACD-CFM-MIB", "acdCfmMepCfgFngAlarmTime"),
        ("ACD-CFM-MIB", "acdCfmMepCfgFngResetTime"),
        ("ACD-CFM-MIB", "acdCfmMepCfgFpEnable"),
        ("ACD-CFM-MIB", "acdCfmMepCfgFpPortId"),
        ("ACD-CFM-MIB", "acdCfmMepCfgCsfEnable"))
)
if mibBuilder.loadTexts:
    acdCfmMepCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdCfmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    acdCfmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-CFM-MIB",
    **{"AcdCfmMepDirection": AcdCfmMepDirection,
       "AcdCfmMepLowestAlarmPri": AcdCfmMepLowestAlarmPri,
       "acdCfm": acdCfm,
       "acdCfmNotifications": acdCfmNotifications,
       "acdCfmMIBObjects": acdCfmMIBObjects,
       "acdCfmDelayMeasurement": acdCfmDelayMeasurement,
       "acdCfmDmCfgTable": acdCfmDmCfgTable,
       "acdCfmDmCfgEntry": acdCfmDmCfgEntry,
       "acdCfmDmCfgID": acdCfmDmCfgID,
       "acdCfmDmCfgRowStatus": acdCfmDmCfgRowStatus,
       "acdCfmDmCfgMepIdx": acdCfmDmCfgMepIdx,
       "acdCfmDmCfgRemoteMepId": acdCfmDmCfgRemoteMepId,
       "acdCfmDmCfgPriority": acdCfmDmCfgPriority,
       "acdCfmDmCfgEnable": acdCfmDmCfgEnable,
       "acdCfmDmCfgInterval": acdCfmDmCfgInterval,
       "acdCfmDmCfgRefPeriod": acdCfmDmCfgRefPeriod,
       "acdCfmDmCfgOneWayDelayEnable": acdCfmDmCfgOneWayDelayEnable,
       "acdCfmDmCfgOneWayDelayMax": acdCfmDmCfgOneWayDelayMax,
       "acdCfmDmCfgOneWayDelayThresh": acdCfmDmCfgOneWayDelayThresh,
       "acdCfmDmCfgOneWayAvgDelayThresh": acdCfmDmCfgOneWayAvgDelayThresh,
       "acdCfmDmCfgOneWayDvEnable": acdCfmDmCfgOneWayDvEnable,
       "acdCfmDmCfgOneWayDvMax": acdCfmDmCfgOneWayDvMax,
       "acdCfmDmCfgOneWayDvThresh": acdCfmDmCfgOneWayDvThresh,
       "acdCfmDmCfgOneWayAvgDvThresh": acdCfmDmCfgOneWayAvgDvThresh,
       "acdCfmDmCfgTwoWayDelayEnable": acdCfmDmCfgTwoWayDelayEnable,
       "acdCfmDmCfgTwoWayDelayMax": acdCfmDmCfgTwoWayDelayMax,
       "acdCfmDmCfgTwoWayDelayThresh": acdCfmDmCfgTwoWayDelayThresh,
       "acdCfmDmCfgTwoWayAvgDelayThresh": acdCfmDmCfgTwoWayAvgDelayThresh,
       "acdCfmDmCfgTwoWayDvEnable": acdCfmDmCfgTwoWayDvEnable,
       "acdCfmDmCfgTwoWayDvMax": acdCfmDmCfgTwoWayDvMax,
       "acdCfmDmCfgTwoWayDvThresh": acdCfmDmCfgTwoWayDvThresh,
       "acdCfmDmCfgTwoWayAvgDvThresh": acdCfmDmCfgTwoWayAvgDvThresh,
       "acdCfmDmCfgName": acdCfmDmCfgName,
       "acdCfmResultOneWayDelayTable": acdCfmResultOneWayDelayTable,
       "acdCfmResultOneWayDelayEntry": acdCfmResultOneWayDelayEntry,
       "acdCfmResultOneWayDelayID": acdCfmResultOneWayDelayID,
       "acdCfmResultOneWayDelayPeriodIndex": acdCfmResultOneWayDelayPeriodIndex,
       "acdCfmResultOneWayDelayIntervalStart": acdCfmResultOneWayDelayIntervalStart,
       "acdCfmResultOneWayDelayValid": acdCfmResultOneWayDelayValid,
       "acdCfmResultOneWayDelayAlert": acdCfmResultOneWayDelayAlert,
       "acdCfmResultOneWayDelayAvgAlert": acdCfmResultOneWayDelayAvgAlert,
       "acdCfmResultOneWayDelaySamples": acdCfmResultOneWayDelaySamples,
       "acdCfmResultOneWayDelayMinValue": acdCfmResultOneWayDelayMinValue,
       "acdCfmResultOneWayDelayMaxValue": acdCfmResultOneWayDelayMaxValue,
       "acdCfmResultOneWayDelayAvgValue": acdCfmResultOneWayDelayAvgValue,
       "acdCfmResultOneWayDelayThreshExc": acdCfmResultOneWayDelayThreshExc,
       "acdCfmResultOneWayDelayInstValue": acdCfmResultOneWayDelayInstValue,
       "acdCfmResultOneWayDelayName": acdCfmResultOneWayDelayName,
       "acdCfmResultOneWayDvTable": acdCfmResultOneWayDvTable,
       "acdCfmResultOneWayDvEntry": acdCfmResultOneWayDvEntry,
       "acdCfmResultOneWayDvID": acdCfmResultOneWayDvID,
       "acdCfmResultOneWayDvPeriodIndex": acdCfmResultOneWayDvPeriodIndex,
       "acdCfmResultOneWayDvIntervalStart": acdCfmResultOneWayDvIntervalStart,
       "acdCfmResultOneWayDvValid": acdCfmResultOneWayDvValid,
       "acdCfmResultOneWayDvAlert": acdCfmResultOneWayDvAlert,
       "acdCfmResultOneWayDvAvgAlert": acdCfmResultOneWayDvAvgAlert,
       "acdCfmResultOneWayDvSamples": acdCfmResultOneWayDvSamples,
       "acdCfmResultOneWayDvMinValue": acdCfmResultOneWayDvMinValue,
       "acdCfmResultOneWayDvMaxValue": acdCfmResultOneWayDvMaxValue,
       "acdCfmResultOneWayDvAvgValue": acdCfmResultOneWayDvAvgValue,
       "acdCfmResultOneWayDvThreshExc": acdCfmResultOneWayDvThreshExc,
       "acdCfmResultOneWayDvInstValue": acdCfmResultOneWayDvInstValue,
       "acdCfmResultOneWayDvName": acdCfmResultOneWayDvName,
       "acdCfmResultTwoWayDelayTable": acdCfmResultTwoWayDelayTable,
       "acdCfmResultTwoWayDelayEntry": acdCfmResultTwoWayDelayEntry,
       "acdCfmResultTwoWayDelayID": acdCfmResultTwoWayDelayID,
       "acdCfmResultTwoWayDelayPeriodIndex": acdCfmResultTwoWayDelayPeriodIndex,
       "acdCfmResultTwoWayDelayIntervalStart": acdCfmResultTwoWayDelayIntervalStart,
       "acdCfmResultTwoWayDelayValid": acdCfmResultTwoWayDelayValid,
       "acdCfmResultTwoWayDelayAlert": acdCfmResultTwoWayDelayAlert,
       "acdCfmResultTwoWayDelayAvgAlert": acdCfmResultTwoWayDelayAvgAlert,
       "acdCfmResultTwoWayDelaySamples": acdCfmResultTwoWayDelaySamples,
       "acdCfmResultTwoWayDelayMinValue": acdCfmResultTwoWayDelayMinValue,
       "acdCfmResultTwoWayDelayMaxValue": acdCfmResultTwoWayDelayMaxValue,
       "acdCfmResultTwoWayDelayAvgValue": acdCfmResultTwoWayDelayAvgValue,
       "acdCfmResultTwoWayDelayThreshExc": acdCfmResultTwoWayDelayThreshExc,
       "acdCfmResultTwoWayDelayInstValue": acdCfmResultTwoWayDelayInstValue,
       "acdCfmResultTwoWayDelayName": acdCfmResultTwoWayDelayName,
       "acdCfmResultTwoWayDvTable": acdCfmResultTwoWayDvTable,
       "acdCfmResultTwoWayDvEntry": acdCfmResultTwoWayDvEntry,
       "acdCfmResultTwoWayDvID": acdCfmResultTwoWayDvID,
       "acdCfmResultTwoWayDvPeriodIndex": acdCfmResultTwoWayDvPeriodIndex,
       "acdCfmResultTwoWayDvIntervalStart": acdCfmResultTwoWayDvIntervalStart,
       "acdCfmResultTwoWayDvValid": acdCfmResultTwoWayDvValid,
       "acdCfmResultTwoWayDvAlert": acdCfmResultTwoWayDvAlert,
       "acdCfmResultTwoWayDvAvgAlert": acdCfmResultTwoWayDvAvgAlert,
       "acdCfmResultTwoWayDvSamples": acdCfmResultTwoWayDvSamples,
       "acdCfmResultTwoWayDvMinValue": acdCfmResultTwoWayDvMinValue,
       "acdCfmResultTwoWayDvMaxValue": acdCfmResultTwoWayDvMaxValue,
       "acdCfmResultTwoWayDvAvgValue": acdCfmResultTwoWayDvAvgValue,
       "acdCfmResultTwoWayDvThreshExc": acdCfmResultTwoWayDvThreshExc,
       "acdCfmResultTwoWayDvInstValue": acdCfmResultTwoWayDvInstValue,
       "acdCfmResultTwoWayDvName": acdCfmResultTwoWayDvName,
       "acdCfmHistResultOneWayDelayTable": acdCfmHistResultOneWayDelayTable,
       "acdCfmHistResultOneWayDelayEntry": acdCfmHistResultOneWayDelayEntry,
       "acdCfmHistResultOneWayDelayID": acdCfmHistResultOneWayDelayID,
       "acdCfmHistResultOneWayDelaySampleIndex": acdCfmHistResultOneWayDelaySampleIndex,
       "acdCfmHistResultOneWayDelayStatus": acdCfmHistResultOneWayDelayStatus,
       "acdCfmHistResultOneWayDelayDuration": acdCfmHistResultOneWayDelayDuration,
       "acdCfmHistResultOneWayDelayIntervalEnd": acdCfmHistResultOneWayDelayIntervalEnd,
       "acdCfmHistResultOneWayDelaySamples": acdCfmHistResultOneWayDelaySamples,
       "acdCfmHistResultOneWayDelayMinValue": acdCfmHistResultOneWayDelayMinValue,
       "acdCfmHistResultOneWayDelayMaxValue": acdCfmHistResultOneWayDelayMaxValue,
       "acdCfmHistResultOneWayDelayAvgValue": acdCfmHistResultOneWayDelayAvgValue,
       "acdCfmHistResultOneWayDelayThreshExc": acdCfmHistResultOneWayDelayThreshExc,
       "acdCfmHistResultOneWayDelayName": acdCfmHistResultOneWayDelayName,
       "acdCfmHistResultOneWayDvTable": acdCfmHistResultOneWayDvTable,
       "acdCfmHistResultOneWayDvEntry": acdCfmHistResultOneWayDvEntry,
       "acdCfmHistResultOneWayDvID": acdCfmHistResultOneWayDvID,
       "acdCfmHistResultOneWayDvSampleIndex": acdCfmHistResultOneWayDvSampleIndex,
       "acdCfmHistResultOneWayDvStatus": acdCfmHistResultOneWayDvStatus,
       "acdCfmHistResultOneWayDvDuration": acdCfmHistResultOneWayDvDuration,
       "acdCfmHistResultOneWayDvIntervalEnd": acdCfmHistResultOneWayDvIntervalEnd,
       "acdCfmHistResultOneWayDvSamples": acdCfmHistResultOneWayDvSamples,
       "acdCfmHistResultOneWayDvMinValue": acdCfmHistResultOneWayDvMinValue,
       "acdCfmHistResultOneWayDvMaxValue": acdCfmHistResultOneWayDvMaxValue,
       "acdCfmHistResultOneWayDvAvgValue": acdCfmHistResultOneWayDvAvgValue,
       "acdCfmHistResultOneWayDvThreshExc": acdCfmHistResultOneWayDvThreshExc,
       "acdCfmHistResultOneWayDvName": acdCfmHistResultOneWayDvName,
       "acdCfmHistResultTwoWayDelayTable": acdCfmHistResultTwoWayDelayTable,
       "acdCfmHistResultTwoWayDelayEntry": acdCfmHistResultTwoWayDelayEntry,
       "acdCfmHistResultTwoWayDelayID": acdCfmHistResultTwoWayDelayID,
       "acdCfmHistResultTwoWayDelaySampleIndex": acdCfmHistResultTwoWayDelaySampleIndex,
       "acdCfmHistResultTwoWayDelayStatus": acdCfmHistResultTwoWayDelayStatus,
       "acdCfmHistResultTwoWayDelayDuration": acdCfmHistResultTwoWayDelayDuration,
       "acdCfmHistResultTwoWayDelayIntervalEnd": acdCfmHistResultTwoWayDelayIntervalEnd,
       "acdCfmHistResultTwoWayDelaySamples": acdCfmHistResultTwoWayDelaySamples,
       "acdCfmHistResultTwoWayDelayMinValue": acdCfmHistResultTwoWayDelayMinValue,
       "acdCfmHistResultTwoWayDelayMaxValue": acdCfmHistResultTwoWayDelayMaxValue,
       "acdCfmHistResultTwoWayDelayAvgValue": acdCfmHistResultTwoWayDelayAvgValue,
       "acdCfmHistResultTwoWayDelayThreshExc": acdCfmHistResultTwoWayDelayThreshExc,
       "acdCfmHistResultTwoWayDelayName": acdCfmHistResultTwoWayDelayName,
       "acdCfmHistResultTwoWayDvTable": acdCfmHistResultTwoWayDvTable,
       "acdCfmHistResultTwoWayDvEntry": acdCfmHistResultTwoWayDvEntry,
       "acdCfmHistResultTwoWayDvID": acdCfmHistResultTwoWayDvID,
       "acdCfmHistResultTwoWayDvSampleIndex": acdCfmHistResultTwoWayDvSampleIndex,
       "acdCfmHistResultTwoWayDvStatus": acdCfmHistResultTwoWayDvStatus,
       "acdCfmHistResultTwoWayDvDuration": acdCfmHistResultTwoWayDvDuration,
       "acdCfmHistResultTwoWayDvIntervalEnd": acdCfmHistResultTwoWayDvIntervalEnd,
       "acdCfmHistResultTwoWayDvSamples": acdCfmHistResultTwoWayDvSamples,
       "acdCfmHistResultTwoWayDvMinValue": acdCfmHistResultTwoWayDvMinValue,
       "acdCfmHistResultTwoWayDvMaxValue": acdCfmHistResultTwoWayDvMaxValue,
       "acdCfmHistResultTwoWayDvAvgValue": acdCfmHistResultTwoWayDvAvgValue,
       "acdCfmHistResultTwoWayDvThreshExc": acdCfmHistResultTwoWayDvThreshExc,
       "acdCfmHistResultTwoWayDvName": acdCfmHistResultTwoWayDvName,
       "acdCfmPacketLoss": acdCfmPacketLoss,
       "acdCfmPktLossCfgTable": acdCfmPktLossCfgTable,
       "acdCfmPktLossCfgEntry": acdCfmPktLossCfgEntry,
       "acdCfmPktLossCfgID": acdCfmPktLossCfgID,
       "acdCfmPktLossCfgRowStatus": acdCfmPktLossCfgRowStatus,
       "acdCfmPktLossCfgMepIdx": acdCfmPktLossCfgMepIdx,
       "acdCfmPktLossCfgRemoteMepId": acdCfmPktLossCfgRemoteMepId,
       "acdCfmPktLossCfgPriority": acdCfmPktLossCfgPriority,
       "acdCfmPktLossCfgEnable": acdCfmPktLossCfgEnable,
       "acdCfmPktLossCfgInterval": acdCfmPktLossCfgInterval,
       "acdCfmPktLossCfgRefPeriod": acdCfmPktLossCfgRefPeriod,
       "acdCfmPktLossCfgThresh": acdCfmPktLossCfgThresh,
       "acdCfmPktLossCfgRatioThresh": acdCfmPktLossCfgRatioThresh,
       "acdCfmPktLossCfgName": acdCfmPktLossCfgName,
       "acdCfmResultPktLossTable": acdCfmResultPktLossTable,
       "acdCfmResultPktLossEntry": acdCfmResultPktLossEntry,
       "acdCfmResultPktLossID": acdCfmResultPktLossID,
       "acdCfmResultPktLossPeriodIndex": acdCfmResultPktLossPeriodIndex,
       "acdCfmResultPktLossIntervalStart": acdCfmResultPktLossIntervalStart,
       "acdCfmResultPktLossValid": acdCfmResultPktLossValid,
       "acdCfmResultPktLossAlert": acdCfmResultPktLossAlert,
       "acdCfmResultPktLossSamples": acdCfmResultPktLossSamples,
       "acdCfmResultPktLossOverflowSamples": acdCfmResultPktLossOverflowSamples,
       "acdCfmResultPktLossHCSamples": acdCfmResultPktLossHCSamples,
       "acdCfmResultPktLossNbrLoss": acdCfmResultPktLossNbrLoss,
       "acdCfmResultPktLossOverflowNbrLoss": acdCfmResultPktLossOverflowNbrLoss,
       "acdCfmResultPktLossHCNbrLoss": acdCfmResultPktLossHCNbrLoss,
       "acdCfmResultPktLossNbrGaps": acdCfmResultPktLossNbrGaps,
       "acdCfmResultPktLossOverflowNbrGaps": acdCfmResultPktLossOverflowNbrGaps,
       "acdCfmResultPktLossHCNbrGaps": acdCfmResultPktLossHCNbrGaps,
       "acdCfmResultPktLossLargestGap": acdCfmResultPktLossLargestGap,
       "acdCfmResultPktLossOverflowLargestGap": acdCfmResultPktLossOverflowLargestGap,
       "acdCfmResultPktLossHCLargestGap": acdCfmResultPktLossHCLargestGap,
       "acdCfmResultPktLossRatio": acdCfmResultPktLossRatio,
       "acdCfmResultPktLossName": acdCfmResultPktLossName,
       "acdCfmHistResultPktLossTable": acdCfmHistResultPktLossTable,
       "acdCfmHistResultPktLossEntry": acdCfmHistResultPktLossEntry,
       "acdCfmHistResultPktLossID": acdCfmHistResultPktLossID,
       "acdCfmHistResultPktLossSampleIndex": acdCfmHistResultPktLossSampleIndex,
       "acdCfmHistResultPktLossStatus": acdCfmHistResultPktLossStatus,
       "acdCfmHistResultPktLossDuration": acdCfmHistResultPktLossDuration,
       "acdCfmHistResultPktLossIntervalEnd": acdCfmHistResultPktLossIntervalEnd,
       "acdCfmHistResultPktLossSamples": acdCfmHistResultPktLossSamples,
       "acdCfmHistResultPktLossOverflowSamples": acdCfmHistResultPktLossOverflowSamples,
       "acdCfmHistResultPktLossHCSamples": acdCfmHistResultPktLossHCSamples,
       "acdCfmHistResultPktLossNbrLoss": acdCfmHistResultPktLossNbrLoss,
       "acdCfmHistResultPktLossOverflowNbrLoss": acdCfmHistResultPktLossOverflowNbrLoss,
       "acdCfmHistResultPktLossHCNbrLoss": acdCfmHistResultPktLossHCNbrLoss,
       "acdCfmHistResultPktLossNbrGaps": acdCfmHistResultPktLossNbrGaps,
       "acdCfmHistResultPktLossOverflowNbrGaps": acdCfmHistResultPktLossOverflowNbrGaps,
       "acdCfmHistResultPktLossHCNbrGaps": acdCfmHistResultPktLossHCNbrGaps,
       "acdCfmHistResultPktLossLargestGap": acdCfmHistResultPktLossLargestGap,
       "acdCfmHistResultPktLossOverflowLargestGap": acdCfmHistResultPktLossOverflowLargestGap,
       "acdCfmHistResultPktLossHCLargestGap": acdCfmHistResultPktLossHCLargestGap,
       "acdCfmHistResultPktLossRatio": acdCfmHistResultPktLossRatio,
       "acdCfmHistResultPktLossName": acdCfmHistResultPktLossName,
       "acdCfmMep": acdCfmMep,
       "acdCfmMepStatsTxTable": acdCfmMepStatsTxTable,
       "acdCfmMepStatsTxEntry": acdCfmMepStatsTxEntry,
       "acdCfmMepStatsTxID": acdCfmMepStatsTxID,
       "acdCfmMepStatsTxCcmPdu": acdCfmMepStatsTxCcmPdu,
       "acdCfmMepStatsTxLbmPdu": acdCfmMepStatsTxLbmPdu,
       "acdCfmMepStatsTxLbrPdu": acdCfmMepStatsTxLbrPdu,
       "acdCfmMepStatsTxLtmPdu": acdCfmMepStatsTxLtmPdu,
       "acdCfmMepStatsTxLtrPdu": acdCfmMepStatsTxLtrPdu,
       "acdCfmMepStatsTxAisPdu": acdCfmMepStatsTxAisPdu,
       "acdCfmMepStatsTxLckPdu": acdCfmMepStatsTxLckPdu,
       "acdCfmMepStatsTxTstPdu": acdCfmMepStatsTxTstPdu,
       "acdCfmMepStatsTxLinearApsPdu": acdCfmMepStatsTxLinearApsPdu,
       "acdCfmMepStatsTxRingApsPdu": acdCfmMepStatsTxRingApsPdu,
       "acdCfmMepStatsTxMccPdu": acdCfmMepStatsTxMccPdu,
       "acdCfmMepStatsTxLmmPdu": acdCfmMepStatsTxLmmPdu,
       "acdCfmMepStatsTxLmrPdu": acdCfmMepStatsTxLmrPdu,
       "acdCfmMepStatsTx1dmPdu": acdCfmMepStatsTx1dmPdu,
       "acdCfmMepStatsTxDmmPdu": acdCfmMepStatsTxDmmPdu,
       "acdCfmMepStatsTxDmrPdu": acdCfmMepStatsTxDmrPdu,
       "acdCfmMepStatsTxExmPdu": acdCfmMepStatsTxExmPdu,
       "acdCfmMepStatsTxExrPdu": acdCfmMepStatsTxExrPdu,
       "acdCfmMepStatsTxVsmPdu": acdCfmMepStatsTxVsmPdu,
       "acdCfmMepStatsTxVsrPdu": acdCfmMepStatsTxVsrPdu,
       "acdCfmMepStatsTxCsfPdu": acdCfmMepStatsTxCsfPdu,
       "acdCfmMepStatsTxSlmPdu": acdCfmMepStatsTxSlmPdu,
       "acdCfmMepStatsTxSlrPdu": acdCfmMepStatsTxSlrPdu,
       "acdCfmMepStatsTxName": acdCfmMepStatsTxName,
       "acdCfmMepStatsRxTable": acdCfmMepStatsRxTable,
       "acdCfmMepStatsRxEntry": acdCfmMepStatsRxEntry,
       "acdCfmMepStatsRxID": acdCfmMepStatsRxID,
       "acdCfmMepStatsRxCcmPdu": acdCfmMepStatsRxCcmPdu,
       "acdCfmMepStatsRxLbmPdu": acdCfmMepStatsRxLbmPdu,
       "acdCfmMepStatsRxLbrPdu": acdCfmMepStatsRxLbrPdu,
       "acdCfmMepStatsRxLtmPdu": acdCfmMepStatsRxLtmPdu,
       "acdCfmMepStatsRxLtrPdu": acdCfmMepStatsRxLtrPdu,
       "acdCfmMepStatsRxAisPdu": acdCfmMepStatsRxAisPdu,
       "acdCfmMepStatsRxLckPdu": acdCfmMepStatsRxLckPdu,
       "acdCfmMepStatsRxTstPdu": acdCfmMepStatsRxTstPdu,
       "acdCfmMepStatsRxLinearApsPdu": acdCfmMepStatsRxLinearApsPdu,
       "acdCfmMepStatsRxRingApsPdu": acdCfmMepStatsRxRingApsPdu,
       "acdCfmMepStatsRxMccPdu": acdCfmMepStatsRxMccPdu,
       "acdCfmMepStatsRxLmmPdu": acdCfmMepStatsRxLmmPdu,
       "acdCfmMepStatsRxLmrPdu": acdCfmMepStatsRxLmrPdu,
       "acdCfmMepStatsRx1dmPdu": acdCfmMepStatsRx1dmPdu,
       "acdCfmMepStatsRxDmmPdu": acdCfmMepStatsRxDmmPdu,
       "acdCfmMepStatsRxDmrPdu": acdCfmMepStatsRxDmrPdu,
       "acdCfmMepStatsRxExmPdu": acdCfmMepStatsRxExmPdu,
       "acdCfmMepStatsRxExrPdu": acdCfmMepStatsRxExrPdu,
       "acdCfmMepStatsRxVsmPdu": acdCfmMepStatsRxVsmPdu,
       "acdCfmMepStatsRxVsrPdu": acdCfmMepStatsRxVsrPdu,
       "acdCfmMepStatsRxCcmSeqErrors": acdCfmMepStatsRxCcmSeqErrors,
       "acdCfmMepStatsRxLtrUnexpectedPdu": acdCfmMepStatsRxLtrUnexpectedPdu,
       "acdCfmMepStatsRxLtrMacErrors": acdCfmMepStatsRxLtrMacErrors,
       "acdCfmMepStatsRxLbrOooErrors": acdCfmMepStatsRxLbrOooErrors,
       "acdCfmMepStatsRxLbrUnexpectedPdu": acdCfmMepStatsRxLbrUnexpectedPdu,
       "acdCfmMepStatsRxLbrDataErrors": acdCfmMepStatsRxLbrDataErrors,
       "acdCfmMepStatsRxCsfPdu": acdCfmMepStatsRxCsfPdu,
       "acdCfmMepStatsRxSlmPdu": acdCfmMepStatsRxSlmPdu,
       "acdCfmMepStatsRxSlrPdu": acdCfmMepStatsRxSlrPdu,
       "acdCfmMepStatsRxCsfInvalidFlags": acdCfmMepStatsRxCsfInvalidFlags,
       "acdCfmMepStatsRxName": acdCfmMepStatsRxName,
       "acdCfmMepDmStatsTable": acdCfmMepDmStatsTable,
       "acdCfmMepDmStatsEntry": acdCfmMepDmStatsEntry,
       "acdCfmMepDmStatsID": acdCfmMepDmStatsID,
       "acdCfmMepDmStatsPriority": acdCfmMepDmStatsPriority,
       "acdCfmMepDmStatsTxDmmPdu": acdCfmMepDmStatsTxDmmPdu,
       "acdCfmMepDmStatsRxDmmPdu": acdCfmMepDmStatsRxDmmPdu,
       "acdCfmMepDmStatsTxDmrPdu": acdCfmMepDmStatsTxDmrPdu,
       "acdCfmMepDmStatsRxDmrPdu": acdCfmMepDmStatsRxDmrPdu,
       "acdCfmMepDmStatsName": acdCfmMepDmStatsName,
       "acdCfmMepCfgTable": acdCfmMepCfgTable,
       "acdCfmMepCfgEntry": acdCfmMepCfgEntry,
       "acdCfmMepCfgIdx": acdCfmMepCfgIdx,
       "acdCfmMepCfgRowStatus": acdCfmMepCfgRowStatus,
       "acdCfmMepCfgMdIdx": acdCfmMepCfgMdIdx,
       "acdCfmMepCfgMaIdx": acdCfmMepCfgMaIdx,
       "acdCfmMepCfgMepId": acdCfmMepCfgMepId,
       "acdCfmMepCfgName": acdCfmMepCfgName,
       "acdCfmMepCfgPortId": acdCfmMepCfgPortId,
       "acdCfmMepCfgPortIdMacAddr": acdCfmMepCfgPortIdMacAddr,
       "acdCfmMepCfgDirection": acdCfmMepCfgDirection,
       "acdCfmMepCfgPrimaryVid": acdCfmMepCfgPrimaryVid,
       "acdCfmMepCfgActive": acdCfmMepCfgActive,
       "acdCfmMepCfgCciEnable": acdCfmMepCfgCciEnable,
       "acdCfmMepCfgCcmSeqEnable": acdCfmMepCfgCcmSeqEnable,
       "acdCfmMepCfgPriority": acdCfmMepCfgPriority,
       "acdCfmMepCfgAlarmPri": acdCfmMepCfgAlarmPri,
       "acdCfmMepCfgFngAlarmTime": acdCfmMepCfgFngAlarmTime,
       "acdCfmMepCfgFngResetTime": acdCfmMepCfgFngResetTime,
       "acdCfmMepCfgFpEnable": acdCfmMepCfgFpEnable,
       "acdCfmMepCfgFpPortId": acdCfmMepCfgFpPortId,
       "acdCfmMepCfgCsfEnable": acdCfmMepCfgCsfEnable,
       "acdCfmStack": acdCfmStack,
       "acdCfmStackTable": acdCfmStackTable,
       "acdCfmStackEntry": acdCfmStackEntry,
       "acdCfmMdIdx": acdCfmMdIdx,
       "acdCfmMaIdx": acdCfmMaIdx,
       "acdCfmMepID": acdCfmMepID,
       "acdCfmMepIdx": acdCfmMepIdx,
       "acdCfmSlm": acdCfmSlm,
       "acdCfmSlmCfgTable": acdCfmSlmCfgTable,
       "acdCfmSlmCfgEntry": acdCfmSlmCfgEntry,
       "acdCfmSlmCfgID": acdCfmSlmCfgID,
       "acdCfmSlmCfgRowStatus": acdCfmSlmCfgRowStatus,
       "acdCfmSlmCfgMepIdx": acdCfmSlmCfgMepIdx,
       "acdCfmSlmCfgRemoteMepId": acdCfmSlmCfgRemoteMepId,
       "acdCfmSlmCfgPriority": acdCfmSlmCfgPriority,
       "acdCfmSlmCfgState": acdCfmSlmCfgState,
       "acdCfmSlmCfgInterval": acdCfmSlmCfgInterval,
       "acdCfmSlmCfgRefPeriod": acdCfmSlmCfgRefPeriod,
       "acdCfmSlmCfgNearEndThresh": acdCfmSlmCfgNearEndThresh,
       "acdCfmSlmCfgFarEndThresh": acdCfmSlmCfgFarEndThresh,
       "acdCfmSlmCfgName": acdCfmSlmCfgName,
       "acdCfmSlmResultTable": acdCfmSlmResultTable,
       "acdCfmSlmResultEntry": acdCfmSlmResultEntry,
       "acdCfmSlmResultID": acdCfmSlmResultID,
       "acdCfmSlmResultPeriodIndex": acdCfmSlmResultPeriodIndex,
       "acdCfmSlmResultIntervalStart": acdCfmSlmResultIntervalStart,
       "acdCfmSlmResultValid": acdCfmSlmResultValid,
       "acdCfmSlmResultNearEndAlert": acdCfmSlmResultNearEndAlert,
       "acdCfmSlmResultFarEndAlert": acdCfmSlmResultFarEndAlert,
       "acdCfmSlmResultTxSlm": acdCfmSlmResultTxSlm,
       "acdCfmSlmResultRxSlr": acdCfmSlmResultRxSlr,
       "acdCfmSlmResultRemoteRxSlm": acdCfmSlmResultRemoteRxSlm,
       "acdCfmSlmResultNearEndNbrLoss": acdCfmSlmResultNearEndNbrLoss,
       "acdCfmSlmResultFarEndNbrLoss": acdCfmSlmResultFarEndNbrLoss,
       "acdCfmSlmResultNearEndRatio": acdCfmSlmResultNearEndRatio,
       "acdCfmSlmResultFarEndRatio": acdCfmSlmResultFarEndRatio,
       "acdCfmSlmResultNbrGaps": acdCfmSlmResultNbrGaps,
       "acdCfmSlmResultLargestGap": acdCfmSlmResultLargestGap,
       "acdCfmSlmResultName": acdCfmSlmResultName,
       "acdCfmSlmHistResultTable": acdCfmSlmHistResultTable,
       "acdCfmSlmHistResultEntry": acdCfmSlmHistResultEntry,
       "acdCfmSlmHistResultID": acdCfmSlmHistResultID,
       "acdCfmSlmHistResultPeriodIndex": acdCfmSlmHistResultPeriodIndex,
       "acdCfmSlmHistResultIntervalEnd": acdCfmSlmHistResultIntervalEnd,
       "acdCfmSlmHistResultTxSlm": acdCfmSlmHistResultTxSlm,
       "acdCfmSlmHistResultRxSlr": acdCfmSlmHistResultRxSlr,
       "acdCfmSlmHistResultRemoteRxSlm": acdCfmSlmHistResultRemoteRxSlm,
       "acdCfmSlmHistResultNearEndRatio": acdCfmSlmHistResultNearEndRatio,
       "acdCfmSlmHistResultFarEndRatio": acdCfmSlmHistResultFarEndRatio,
       "acdCfmSlmHistResultNbrGaps": acdCfmSlmHistResultNbrGaps,
       "acdCfmSlmHistResultLargestGap": acdCfmSlmHistResultLargestGap,
       "acdCfmSlmHistResultInstanceIndex": acdCfmSlmHistResultInstanceIndex,
       "acdCfmSlmHistResultName": acdCfmSlmHistResultName,
       "acdCfmConformance": acdCfmConformance,
       "acdCfmCompliances": acdCfmCompliances,
       "acdCfmCompliance": acdCfmCompliance,
       "acdCfmGroups": acdCfmGroups,
       "acdCfmDmCfgGroup": acdCfmDmCfgGroup,
       "acdCfmResultOneWayDelayGroup": acdCfmResultOneWayDelayGroup,
       "acdCfmResultOneWayDvGroup": acdCfmResultOneWayDvGroup,
       "acdCfmResultTwoWayDelayGroup": acdCfmResultTwoWayDelayGroup,
       "acdCfmResultTwoWayDvGroup": acdCfmResultTwoWayDvGroup,
       "acdCfmHistResultOneWayDelayGroup": acdCfmHistResultOneWayDelayGroup,
       "acdCfmHistResultOneWayDvGroup": acdCfmHistResultOneWayDvGroup,
       "acdCfmHistResultTwoWayDelayGroup": acdCfmHistResultTwoWayDelayGroup,
       "acdCfmHistResultTwoWayDvGroup": acdCfmHistResultTwoWayDvGroup,
       "acdCfmPktLossCfgGroup": acdCfmPktLossCfgGroup,
       "acdCfmResultPktLossGroup": acdCfmResultPktLossGroup,
       "acdCfmHistResultPktLossGroup": acdCfmHistResultPktLossGroup,
       "acdCfmMepStatsTxGroup": acdCfmMepStatsTxGroup,
       "acdCfmMepStatsRxGroup": acdCfmMepStatsRxGroup,
       "acdCfmMepDmStatsGroup": acdCfmMepDmStatsGroup,
       "acdCfmMepStackGroup": acdCfmMepStackGroup,
       "acdCfmMepSlmStatsGroup": acdCfmMepSlmStatsGroup,
       "acdCfmSlmCfgGroup": acdCfmSlmCfgGroup,
       "acdCfmSlmResultGroup": acdCfmSlmResultGroup,
       "acdCfmSlmHistResultGroup": acdCfmSlmHistResultGroup,
       "acdCfmMepCfgGroup": acdCfmMepCfgGroup}
)
