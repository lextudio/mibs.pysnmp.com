# SNMP MIB module (NETI-CHMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETI-CHMGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:30 2024
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

(netiExperimentalGeneric,) = mibBuilder.importSymbols(
    "NETI-COMMON-MIB",
    "netiExperimentalGeneric")

(DtmAddress,) = mibBuilder.importSymbols(
    "NETI-DTM-MIB",
    "DtmAddress")

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
 MacAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

netiChmgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14)
)
netiChmgrMIB.setRevisions(
        ("2015-01-08 15:00",
         "2014-05-05 12:00",
         "2014-02-06 15:00",
         "2013-09-02 16:00",
         "2012-03-19 09:00",
         "2012-01-26 15:00",
         "2010-04-06 08:00",
         "2009-09-25 11:00",
         "2008-12-12 14:00",
         "2008-01-28 14:00",
         "2008-01-03 16:00",
         "2007-06-29 12:00",
         "2006-09-20 08:00",
         "2006-04-20 09:00",
         "2005-09-27 00:00",
         "2004-11-18 00:00",
         "2003-04-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dst(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              8,
              12,
              13,
              14,
              15,
              16,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("aesebu", 20),
          ("ctrl", 0),
          ("dleCrtlAndData", 1),
          ("dleInterServer", 5),
          ("ds1", 14),
          ("dvb", 16),
          ("e1", 13),
          ("ets", 8),
          ("j2k3gSdi", 23),
          ("j2k3gSdi2", 25),
          ("j2kHdSdi", 22),
          ("j2kHdSdi2", 24),
          ("j2kSdSdi", 21),
          ("j2kSdSdi2", 26),
          ("pdh", 4),
          ("ping", 12),
          ("sdh", 18),
          ("sdi", 15),
          ("ttcp", 19))
    )



class Dsti(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32769),
    )



class ChannelId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"


class DcapType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dcap0", 1),
          ("dcap1", 2))
    )



class DtmNode(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class DcpVersion(Integer32, TextualConvention):
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
        *(("auto", 1),
          ("dcp2", 2),
          ("dcp3", 3))
    )



# MIB Managed Objects in the order of their OIDs

_ChmgrObjects_ObjectIdentity = ObjectIdentity
chmgrObjects = _ChmgrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1)
)
_ChmgrODescriptionGroup_ObjectIdentity = ObjectIdentity
chmgrODescriptionGroup = _ChmgrODescriptionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1)
)
_ChmgrODescriptionTimeStamp_Type = TimeStamp
_ChmgrODescriptionTimeStamp_Object = MibScalar
chmgrODescriptionTimeStamp = _ChmgrODescriptionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 1),
    _ChmgrODescriptionTimeStamp_Type()
)
chmgrODescriptionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrODescriptionTimeStamp.setStatus("current")
_ChmgrODescriptionTable_Object = MibTable
chmgrODescriptionTable = _ChmgrODescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2)
)
if mibBuilder.loadTexts:
    chmgrODescriptionTable.setStatus("current")
_ChmgrODescriptionEntry_Object = MibTableRow
chmgrODescriptionEntry = _ChmgrODescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1)
)
chmgrODescriptionEntry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrODescrIndex"),
)
if mibBuilder.loadTexts:
    chmgrODescriptionEntry.setStatus("current")
_ChmgrODescrIndex_Type = Unsigned32
_ChmgrODescrIndex_Object = MibTableColumn
chmgrODescrIndex = _ChmgrODescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 1),
    _ChmgrODescrIndex_Type()
)
chmgrODescrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrODescrIndex.setStatus("current")


class _ChmgrODescrType_Type(Integer32):
    """Custom type chmgrODescrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dle", 3),
          ("ets", 1),
          ("its", 2))
    )


_ChmgrODescrType_Type.__name__ = "Integer32"
_ChmgrODescrType_Object = MibTableColumn
chmgrODescrType = _ChmgrODescrType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 2),
    _ChmgrODescrType_Type()
)
chmgrODescrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrODescrType.setStatus("current")


class _ChmgrODescrCapabilities_Type(Bits):
    """Custom type chmgrODescrCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("allowAlternative", 10),
          ("allowCapacityInterval", 0),
          ("allowDynamicCapacity", 2),
          ("allowEstablish", 4),
          ("allowProtection", 5),
          ("allowReestablish", 6),
          ("allowScheduling", 7),
          ("allowSourceRoute", 8),
          ("allowZeroCapacity", 11),
          ("destination", 1),
          ("isMulticast", 3),
          ("requireCapacity", 9))
    )

_ChmgrODescrCapabilities_Type.__name__ = "Bits"
_ChmgrODescrCapabilities_Object = MibTableColumn
chmgrODescrCapabilities = _ChmgrODescrCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 3),
    _ChmgrODescrCapabilities_Type()
)
chmgrODescrCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrODescrCapabilities.setStatus("current")
_ChmgrODescrCustomerId_Type = Unsigned32
_ChmgrODescrCustomerId_Object = MibTableColumn
chmgrODescrCustomerId = _ChmgrODescrCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 4),
    _ChmgrODescrCustomerId_Type()
)
chmgrODescrCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrODescrCustomerId.setStatus("current")
_ChmgrODescrServiceReference_Type = RowPointer
_ChmgrODescrServiceReference_Object = MibTableColumn
chmgrODescrServiceReference = _ChmgrODescrServiceReference_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 5),
    _ChmgrODescrServiceReference_Type()
)
chmgrODescrServiceReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrODescrServiceReference.setStatus("current")
_ChmgrODescrAcceptableBps_Type = Gauge32
_ChmgrODescrAcceptableBps_Object = MibTableColumn
chmgrODescrAcceptableBps = _ChmgrODescrAcceptableBps_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 6),
    _ChmgrODescrAcceptableBps_Type()
)
chmgrODescrAcceptableBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrODescrAcceptableBps.setStatus("current")
_ChmgrODescrAcceptableSlots_Type = Gauge32
_ChmgrODescrAcceptableSlots_Object = MibTableColumn
chmgrODescrAcceptableSlots = _ChmgrODescrAcceptableSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 7),
    _ChmgrODescrAcceptableSlots_Type()
)
chmgrODescrAcceptableSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrODescrAcceptableSlots.setStatus("current")
_ChmgrODescrRequestedBps_Type = Gauge32
_ChmgrODescrRequestedBps_Object = MibTableColumn
chmgrODescrRequestedBps = _ChmgrODescrRequestedBps_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 8),
    _ChmgrODescrRequestedBps_Type()
)
chmgrODescrRequestedBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrODescrRequestedBps.setStatus("current")
_ChmgrODescrRequestedSlots_Type = Gauge32
_ChmgrODescrRequestedSlots_Object = MibTableColumn
chmgrODescrRequestedSlots = _ChmgrODescrRequestedSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 9),
    _ChmgrODescrRequestedSlots_Type()
)
chmgrODescrRequestedSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrODescrRequestedSlots.setStatus("current")


class _ChmgrODescrReestablishMethod_Type(Integer32):
    """Custom type chmgrODescrReestablishMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("exponential", 1)
    )


_ChmgrODescrReestablishMethod_Type.__name__ = "Integer32"
_ChmgrODescrReestablishMethod_Object = MibTableColumn
chmgrODescrReestablishMethod = _ChmgrODescrReestablishMethod_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 10),
    _ChmgrODescrReestablishMethod_Type()
)
chmgrODescrReestablishMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrODescrReestablishMethod.setStatus("current")


class _ChmgrODescrMinInterval_Type(Gauge32):
    """Custom type chmgrODescrMinInterval based on Gauge32"""
    defaultValue = 500

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_ChmgrODescrMinInterval_Type.__name__ = "Gauge32"
_ChmgrODescrMinInterval_Object = MibTableColumn
chmgrODescrMinInterval = _ChmgrODescrMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 11),
    _ChmgrODescrMinInterval_Type()
)
chmgrODescrMinInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrODescrMinInterval.setStatus("current")


class _ChmgrODescrMaxInterval_Type(Gauge32):
    """Custom type chmgrODescrMaxInterval based on Gauge32"""
    defaultValue = 10000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_ChmgrODescrMaxInterval_Type.__name__ = "Gauge32"
_ChmgrODescrMaxInterval_Object = MibTableColumn
chmgrODescrMaxInterval = _ChmgrODescrMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 12),
    _ChmgrODescrMaxInterval_Type()
)
chmgrODescrMaxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrODescrMaxInterval.setStatus("current")


class _ChmgrODescrEstablish_Type(TruthValue):
    """Custom type chmgrODescrEstablish based on TruthValue"""


_ChmgrODescrEstablish_Object = MibTableColumn
chmgrODescrEstablish = _ChmgrODescrEstablish_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 13),
    _ChmgrODescrEstablish_Type()
)
chmgrODescrEstablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrODescrEstablish.setStatus("current")


class _ChmgrODescrNextDestTableIndex_Type(Unsigned32):
    """Custom type chmgrODescrNextDestTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChmgrODescrNextDestTableIndex_Type.__name__ = "Unsigned32"
_ChmgrODescrNextDestTableIndex_Object = MibTableColumn
chmgrODescrNextDestTableIndex = _ChmgrODescrNextDestTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 14),
    _ChmgrODescrNextDestTableIndex_Type()
)
chmgrODescrNextDestTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrODescrNextDestTableIndex.setStatus("current")


class _ChmgrODescrPrecedence_Type(TruthValue):
    """Custom type chmgrODescrPrecedence based on TruthValue"""


_ChmgrODescrPrecedence_Object = MibTableColumn
chmgrODescrPrecedence = _ChmgrODescrPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 15),
    _ChmgrODescrPrecedence_Type()
)
chmgrODescrPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrODescrPrecedence.setStatus("current")


class _ChmgrODescrSuppressAlarms_Type(Bits):
    """Custom type chmgrODescrSuppressAlarms based on Bits"""
    namedValues = NamedValues(
        ("route", 0)
    )

_ChmgrODescrSuppressAlarms_Type.__name__ = "Bits"
_ChmgrODescrSuppressAlarms_Object = MibTableColumn
chmgrODescrSuppressAlarms = _ChmgrODescrSuppressAlarms_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 16),
    _ChmgrODescrSuppressAlarms_Type()
)
chmgrODescrSuppressAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrODescrSuppressAlarms.setStatus("current")
_ChmgrODescrAcceptableMbps_Type = Gauge32
_ChmgrODescrAcceptableMbps_Object = MibTableColumn
chmgrODescrAcceptableMbps = _ChmgrODescrAcceptableMbps_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 17),
    _ChmgrODescrAcceptableMbps_Type()
)
chmgrODescrAcceptableMbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrODescrAcceptableMbps.setStatus("current")
_ChmgrODescrRequestedMbps_Type = Gauge32
_ChmgrODescrRequestedMbps_Object = MibTableColumn
chmgrODescrRequestedMbps = _ChmgrODescrRequestedMbps_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 18),
    _ChmgrODescrRequestedMbps_Type()
)
chmgrODescrRequestedMbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrODescrRequestedMbps.setStatus("current")
_ChmgrODescrRequestedDcpVersion_Type = DcpVersion
_ChmgrODescrRequestedDcpVersion_Object = MibTableColumn
chmgrODescrRequestedDcpVersion = _ChmgrODescrRequestedDcpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 19),
    _ChmgrODescrRequestedDcpVersion_Type()
)
chmgrODescrRequestedDcpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrODescrRequestedDcpVersion.setStatus("current")
_ChmgrODescrOneHopSpareCapUtilization_Type = TruthValue
_ChmgrODescrOneHopSpareCapUtilization_Object = MibTableColumn
chmgrODescrOneHopSpareCapUtilization = _ChmgrODescrOneHopSpareCapUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 2, 1, 20),
    _ChmgrODescrOneHopSpareCapUtilization_Type()
)
chmgrODescrOneHopSpareCapUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrODescrOneHopSpareCapUtilization.setStatus("current")
_ChmgrODescrDestinationTable_Object = MibTable
chmgrODescrDestinationTable = _ChmgrODescrDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 3)
)
if mibBuilder.loadTexts:
    chmgrODescrDestinationTable.setStatus("current")
_ChmgrODescrDestinationEntry_Object = MibTableRow
chmgrODescrDestinationEntry = _ChmgrODescrDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 3, 1)
)
chmgrODescrDestinationEntry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrODescrIndex"),
    (0, "NETI-CHMGR-MIB", "chmgrODescrDestIndex"),
)
if mibBuilder.loadTexts:
    chmgrODescrDestinationEntry.setStatus("current")
_ChmgrODescrDestIndex_Type = Unsigned32
_ChmgrODescrDestIndex_Object = MibTableColumn
chmgrODescrDestIndex = _ChmgrODescrDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 3, 1, 1),
    _ChmgrODescrDestIndex_Type()
)
chmgrODescrDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrODescrDestIndex.setStatus("current")


class _ChmgrODescrDestAddress_Type(DtmNode):
    """Custom type chmgrODescrDestAddress based on DtmNode"""
    defaultHexValue = ""


_ChmgrODescrDestAddress_Object = MibTableColumn
chmgrODescrDestAddress = _ChmgrODescrDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 3, 1, 2),
    _ChmgrODescrDestAddress_Type()
)
chmgrODescrDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrODescrDestAddress.setStatus("current")


class _ChmgrODescrDestDsti_Type(Dsti):
    """Custom type chmgrODescrDestDsti based on Dsti"""
    defaultValue = 0


_ChmgrODescrDestDsti_Object = MibTableColumn
chmgrODescrDestDsti = _ChmgrODescrDestDsti_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 3, 1, 3),
    _ChmgrODescrDestDsti_Type()
)
chmgrODescrDestDsti.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrODescrDestDsti.setStatus("current")
_ChmgrODescrDestRowStatus_Type = RowStatus
_ChmgrODescrDestRowStatus_Object = MibTableColumn
chmgrODescrDestRowStatus = _ChmgrODescrDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 3, 1, 4),
    _ChmgrODescrDestRowStatus_Type()
)
chmgrODescrDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrODescrDestRowStatus.setStatus("current")


class _ChmgrODescrDestAdminStatus_Type(Integer32):
    """Custom type chmgrODescrDestAdminStatus based on Integer32"""
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


_ChmgrODescrDestAdminStatus_Type.__name__ = "Integer32"
_ChmgrODescrDestAdminStatus_Object = MibTableColumn
chmgrODescrDestAdminStatus = _ChmgrODescrDestAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 3, 1, 5),
    _ChmgrODescrDestAdminStatus_Type()
)
chmgrODescrDestAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrODescrDestAdminStatus.setStatus("current")
_ChmgrODescrChannelTable_Object = MibTable
chmgrODescrChannelTable = _ChmgrODescrChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 4)
)
if mibBuilder.loadTexts:
    chmgrODescrChannelTable.setStatus("current")
_ChmgrODescrChannelEntry_Object = MibTableRow
chmgrODescrChannelEntry = _ChmgrODescrChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 4, 1)
)
chmgrODescrChannelEntry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrODescrIndex"),
    (0, "NETI-CHMGR-MIB", "chmgrODescrDestIndex"),
    (0, "NETI-CHMGR-MIB", "chmgrODescrChanIndex"),
    (0, "NETI-CHMGR-MIB", "chmgrODescrChanSourceRouteIndex"),
)
if mibBuilder.loadTexts:
    chmgrODescrChannelEntry.setStatus("current")


class _ChmgrODescrChanIndex_Type(Unsigned32):
    """Custom type chmgrODescrChanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ChmgrODescrChanIndex_Type.__name__ = "Unsigned32"
_ChmgrODescrChanIndex_Object = MibTableColumn
chmgrODescrChanIndex = _ChmgrODescrChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 4, 1, 1),
    _ChmgrODescrChanIndex_Type()
)
chmgrODescrChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrODescrChanIndex.setStatus("current")
_ChmgrODescrChanSourceRouteIndex_Type = Unsigned32
_ChmgrODescrChanSourceRouteIndex_Object = MibTableColumn
chmgrODescrChanSourceRouteIndex = _ChmgrODescrChanSourceRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 4, 1, 2),
    _ChmgrODescrChanSourceRouteIndex_Type()
)
chmgrODescrChanSourceRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrODescrChanSourceRouteIndex.setStatus("current")
_ChmgrODescrChanSourceRoute_Type = Unsigned32
_ChmgrODescrChanSourceRoute_Object = MibTableColumn
chmgrODescrChanSourceRoute = _ChmgrODescrChanSourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 4, 1, 3),
    _ChmgrODescrChanSourceRoute_Type()
)
chmgrODescrChanSourceRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrODescrChanSourceRoute.setStatus("current")
_ChmgrODescrChanRowStatus_Type = RowStatus
_ChmgrODescrChanRowStatus_Object = MibTableColumn
chmgrODescrChanRowStatus = _ChmgrODescrChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 1, 4, 1, 4),
    _ChmgrODescrChanRowStatus_Type()
)
chmgrODescrChanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrODescrChanRowStatus.setStatus("current")
_ChmgrTDescriptionGroup_ObjectIdentity = ObjectIdentity
chmgrTDescriptionGroup = _ChmgrTDescriptionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 2)
)
_ChmgrSourceRouteGroup_ObjectIdentity = ObjectIdentity
chmgrSourceRouteGroup = _ChmgrSourceRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3)
)
_ChmgrSourceRouteTimeStamp_Type = TimeStamp
_ChmgrSourceRouteTimeStamp_Object = MibScalar
chmgrSourceRouteTimeStamp = _ChmgrSourceRouteTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 1),
    _ChmgrSourceRouteTimeStamp_Type()
)
chmgrSourceRouteTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrSourceRouteTimeStamp.setStatus("current")
_ChmgrSourceRouteTable_Object = MibTable
chmgrSourceRouteTable = _ChmgrSourceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 2)
)
if mibBuilder.loadTexts:
    chmgrSourceRouteTable.setStatus("current")
_ChmgrSourceRouteEntry_Object = MibTableRow
chmgrSourceRouteEntry = _ChmgrSourceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 2, 1)
)
chmgrSourceRouteEntry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrSourceRouteIndex"),
)
if mibBuilder.loadTexts:
    chmgrSourceRouteEntry.setStatus("current")
_ChmgrSourceRouteIndex_Type = Unsigned32
_ChmgrSourceRouteIndex_Object = MibTableColumn
chmgrSourceRouteIndex = _ChmgrSourceRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 2, 1, 1),
    _ChmgrSourceRouteIndex_Type()
)
chmgrSourceRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrSourceRouteIndex.setStatus("current")
_ChmgrSourceRouteName_Type = SnmpAdminString
_ChmgrSourceRouteName_Object = MibTableColumn
chmgrSourceRouteName = _ChmgrSourceRouteName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 2, 1, 2),
    _ChmgrSourceRouteName_Type()
)
chmgrSourceRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrSourceRouteName.setStatus("current")


class _ChmgrSourceRouteTypeOfRoute_Type(Integer32):
    """Custom type chmgrSourceRouteTypeOfRoute based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 2),
          ("strict", 1))
    )


_ChmgrSourceRouteTypeOfRoute_Type.__name__ = "Integer32"
_ChmgrSourceRouteTypeOfRoute_Object = MibTableColumn
chmgrSourceRouteTypeOfRoute = _ChmgrSourceRouteTypeOfRoute_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 2, 1, 3),
    _ChmgrSourceRouteTypeOfRoute_Type()
)
chmgrSourceRouteTypeOfRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrSourceRouteTypeOfRoute.setStatus("current")


class _ChmgrSourceRouteFirstIfBoard_Type(Unsigned32):
    """Custom type chmgrSourceRouteFirstIfBoard based on Unsigned32"""
    defaultValue = 0


_ChmgrSourceRouteFirstIfBoard_Object = MibTableColumn
chmgrSourceRouteFirstIfBoard = _ChmgrSourceRouteFirstIfBoard_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 2, 1, 4),
    _ChmgrSourceRouteFirstIfBoard_Type()
)
chmgrSourceRouteFirstIfBoard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrSourceRouteFirstIfBoard.setStatus("current")


class _ChmgrSourceRouteFirstIfPort_Type(Unsigned32):
    """Custom type chmgrSourceRouteFirstIfPort based on Unsigned32"""
    defaultValue = 0


_ChmgrSourceRouteFirstIfPort_Object = MibTableColumn
chmgrSourceRouteFirstIfPort = _ChmgrSourceRouteFirstIfPort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 2, 1, 5),
    _ChmgrSourceRouteFirstIfPort_Type()
)
chmgrSourceRouteFirstIfPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrSourceRouteFirstIfPort.setStatus("current")
_ChmgrSourceRouteRowStatus_Type = RowStatus
_ChmgrSourceRouteRowStatus_Object = MibTableColumn
chmgrSourceRouteRowStatus = _ChmgrSourceRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 2, 1, 6),
    _ChmgrSourceRouteRowStatus_Type()
)
chmgrSourceRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrSourceRouteRowStatus.setStatus("current")
_ChmgrSourceRouteHopTable_Object = MibTable
chmgrSourceRouteHopTable = _ChmgrSourceRouteHopTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 3)
)
if mibBuilder.loadTexts:
    chmgrSourceRouteHopTable.setStatus("current")
_ChmgrSourceRouteHopEntry_Object = MibTableRow
chmgrSourceRouteHopEntry = _ChmgrSourceRouteHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 3, 1)
)
chmgrSourceRouteHopEntry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrSourceRouteIndex"),
    (0, "NETI-CHMGR-MIB", "chmgrSourceRouteHopIndex"),
)
if mibBuilder.loadTexts:
    chmgrSourceRouteHopEntry.setStatus("current")
_ChmgrSourceRouteHopIndex_Type = Unsigned32
_ChmgrSourceRouteHopIndex_Object = MibTableColumn
chmgrSourceRouteHopIndex = _ChmgrSourceRouteHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 3, 1, 1),
    _ChmgrSourceRouteHopIndex_Type()
)
chmgrSourceRouteHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrSourceRouteHopIndex.setStatus("current")
_ChmgrSourceRouteHopAddress_Type = DtmNode
_ChmgrSourceRouteHopAddress_Object = MibTableColumn
chmgrSourceRouteHopAddress = _ChmgrSourceRouteHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 3, 1, 2),
    _ChmgrSourceRouteHopAddress_Type()
)
chmgrSourceRouteHopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrSourceRouteHopAddress.setStatus("current")


class _ChmgrSourceRouteHopNextIfBoard_Type(Unsigned32):
    """Custom type chmgrSourceRouteHopNextIfBoard based on Unsigned32"""
    defaultValue = 0


_ChmgrSourceRouteHopNextIfBoard_Object = MibTableColumn
chmgrSourceRouteHopNextIfBoard = _ChmgrSourceRouteHopNextIfBoard_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 3, 1, 3),
    _ChmgrSourceRouteHopNextIfBoard_Type()
)
chmgrSourceRouteHopNextIfBoard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrSourceRouteHopNextIfBoard.setStatus("current")


class _ChmgrSourceRouteHopNextIfPort_Type(Unsigned32):
    """Custom type chmgrSourceRouteHopNextIfPort based on Unsigned32"""
    defaultValue = 0


_ChmgrSourceRouteHopNextIfPort_Object = MibTableColumn
chmgrSourceRouteHopNextIfPort = _ChmgrSourceRouteHopNextIfPort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 3, 1, 4),
    _ChmgrSourceRouteHopNextIfPort_Type()
)
chmgrSourceRouteHopNextIfPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrSourceRouteHopNextIfPort.setStatus("current")
_ChmgrSourceRouteHopRowStatus_Type = RowStatus
_ChmgrSourceRouteHopRowStatus_Object = MibTableColumn
chmgrSourceRouteHopRowStatus = _ChmgrSourceRouteHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 3, 3, 1, 5),
    _ChmgrSourceRouteHopRowStatus_Type()
)
chmgrSourceRouteHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chmgrSourceRouteHopRowStatus.setStatus("current")
_ChmgrOConnectionGroup_ObjectIdentity = ObjectIdentity
chmgrOConnectionGroup = _ChmgrOConnectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4)
)
_ChmgrOConnectionTimeStamp_Type = TimeStamp
_ChmgrOConnectionTimeStamp_Object = MibScalar
chmgrOConnectionTimeStamp = _ChmgrOConnectionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 1),
    _ChmgrOConnectionTimeStamp_Type()
)
chmgrOConnectionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnectionTimeStamp.setStatus("current")
_ChmgrOConnectionTable_Object = MibTable
chmgrOConnectionTable = _ChmgrOConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2)
)
if mibBuilder.loadTexts:
    chmgrOConnectionTable.setStatus("current")
_ChmgrOConnectionEntry_Object = MibTableRow
chmgrOConnectionEntry = _ChmgrOConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1)
)
chmgrOConnectionEntry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrOConnIndex"),
)
if mibBuilder.loadTexts:
    chmgrOConnectionEntry.setStatus("current")
_ChmgrOConnIndex_Type = Unsigned32
_ChmgrOConnIndex_Object = MibTableColumn
chmgrOConnIndex = _ChmgrOConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 1),
    _ChmgrOConnIndex_Type()
)
chmgrOConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrOConnIndex.setStatus("current")
_ChmgrOConnCustomerId_Type = Unsigned32
_ChmgrOConnCustomerId_Object = MibTableColumn
chmgrOConnCustomerId = _ChmgrOConnCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 2),
    _ChmgrOConnCustomerId_Type()
)
chmgrOConnCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnCustomerId.setStatus("current")


class _ChmgrOConnODescrIndex_Type(Unsigned32):
    """Custom type chmgrOConnODescrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChmgrOConnODescrIndex_Type.__name__ = "Unsigned32"
_ChmgrOConnODescrIndex_Object = MibTableColumn
chmgrOConnODescrIndex = _ChmgrOConnODescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 3),
    _ChmgrOConnODescrIndex_Type()
)
chmgrOConnODescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnODescrIndex.setStatus("current")
_ChmgrOConnServiceReference_Type = RowPointer
_ChmgrOConnServiceReference_Object = MibTableColumn
chmgrOConnServiceReference = _ChmgrOConnServiceReference_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 4),
    _ChmgrOConnServiceReference_Type()
)
chmgrOConnServiceReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnServiceReference.setStatus("current")


class _ChmgrOConnAllocatedSlots_Type(Gauge32):
    """Custom type chmgrOConnAllocatedSlots based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8389),
    )


_ChmgrOConnAllocatedSlots_Type.__name__ = "Gauge32"
_ChmgrOConnAllocatedSlots_Object = MibTableColumn
chmgrOConnAllocatedSlots = _ChmgrOConnAllocatedSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 5),
    _ChmgrOConnAllocatedSlots_Type()
)
chmgrOConnAllocatedSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnAllocatedSlots.setStatus("current")
_ChmgrOConnAllocatedSlotsChanged_Type = TimeStamp
_ChmgrOConnAllocatedSlotsChanged_Object = MibTableColumn
chmgrOConnAllocatedSlotsChanged = _ChmgrOConnAllocatedSlotsChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 6),
    _ChmgrOConnAllocatedSlotsChanged_Type()
)
chmgrOConnAllocatedSlotsChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnAllocatedSlotsChanged.setStatus("current")
_ChmgrOConnDcapType_Type = DcapType
_ChmgrOConnDcapType_Object = MibTableColumn
chmgrOConnDcapType = _ChmgrOConnDcapType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 7),
    _ChmgrOConnDcapType_Type()
)
chmgrOConnDcapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnDcapType.setStatus("current")
_ChmgrOConnDst_Type = Dst
_ChmgrOConnDst_Object = MibTableColumn
chmgrOConnDst = _ChmgrOConnDst_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 8),
    _ChmgrOConnDst_Type()
)
chmgrOConnDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnDst.setStatus("current")
_ChmgrOConnSourceAddress_Type = DtmNode
_ChmgrOConnSourceAddress_Object = MibTableColumn
chmgrOConnSourceAddress = _ChmgrOConnSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 9),
    _ChmgrOConnSourceAddress_Type()
)
chmgrOConnSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnSourceAddress.setStatus("current")
_ChmgrOConnSourceDsti_Type = Dsti
_ChmgrOConnSourceDsti_Object = MibTableColumn
chmgrOConnSourceDsti = _ChmgrOConnSourceDsti_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 10),
    _ChmgrOConnSourceDsti_Type()
)
chmgrOConnSourceDsti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnSourceDsti.setStatus("current")
_ChmgrOConnStatusLastChanged_Type = TimeStamp
_ChmgrOConnStatusLastChanged_Object = MibTableColumn
chmgrOConnStatusLastChanged = _ChmgrOConnStatusLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 11),
    _ChmgrOConnStatusLastChanged_Type()
)
chmgrOConnStatusLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnStatusLastChanged.setStatus("current")


class _ChmgrOConnAdminStatus_Type(Integer32):
    """Custom type chmgrOConnAdminStatus based on Integer32"""
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


_ChmgrOConnAdminStatus_Type.__name__ = "Integer32"
_ChmgrOConnAdminStatus_Object = MibTableColumn
chmgrOConnAdminStatus = _ChmgrOConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 12),
    _ChmgrOConnAdminStatus_Type()
)
chmgrOConnAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnAdminStatus.setStatus("current")


class _ChmgrOConnOperStatus_Type(Integer32):
    """Custom type chmgrOConnOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("partial", 3),
          ("up", 1))
    )


_ChmgrOConnOperStatus_Type.__name__ = "Integer32"
_ChmgrOConnOperStatus_Object = MibTableColumn
chmgrOConnOperStatus = _ChmgrOConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 13),
    _ChmgrOConnOperStatus_Type()
)
chmgrOConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnOperStatus.setStatus("current")


class _ChmgrOConnReestablish_Type(Integer32):
    """Custom type chmgrOConnReestablish based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("reestablish", 1))
    )


_ChmgrOConnReestablish_Type.__name__ = "Integer32"
_ChmgrOConnReestablish_Object = MibTableColumn
chmgrOConnReestablish = _ChmgrOConnReestablish_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 14),
    _ChmgrOConnReestablish_Type()
)
chmgrOConnReestablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrOConnReestablish.setStatus("current")
_ChmgrOConnForceSourceRoute_Type = Unsigned32
_ChmgrOConnForceSourceRoute_Object = MibTableColumn
chmgrOConnForceSourceRoute = _ChmgrOConnForceSourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 15),
    _ChmgrOConnForceSourceRoute_Type()
)
chmgrOConnForceSourceRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrOConnForceSourceRoute.setStatus("current")
_ChmgrOConnDcpVersion_Type = DcpVersion
_ChmgrOConnDcpVersion_Object = MibTableColumn
chmgrOConnDcpVersion = _ChmgrOConnDcpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 2, 1, 16),
    _ChmgrOConnDcpVersion_Type()
)
chmgrOConnDcpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOConnDcpVersion.setStatus("current")
_ChmgrODestinationTable_Object = MibTable
chmgrODestinationTable = _ChmgrODestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 3)
)
if mibBuilder.loadTexts:
    chmgrODestinationTable.setStatus("current")
_ChmgrODestinationEntry_Object = MibTableRow
chmgrODestinationEntry = _ChmgrODestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 3, 1)
)
chmgrODestinationEntry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrOConnIndex"),
    (0, "NETI-CHMGR-MIB", "chmgrODescrDestIndex"),
)
if mibBuilder.loadTexts:
    chmgrODestinationEntry.setStatus("current")
_ChmgrODestDestinationAddress_Type = DtmNode
_ChmgrODestDestinationAddress_Object = MibTableColumn
chmgrODestDestinationAddress = _ChmgrODestDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 3, 1, 1),
    _ChmgrODestDestinationAddress_Type()
)
chmgrODestDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrODestDestinationAddress.setStatus("current")
_ChmgrODestDestinationDsti_Type = Dsti
_ChmgrODestDestinationDsti_Object = MibTableColumn
chmgrODestDestinationDsti = _ChmgrODestDestinationDsti_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 3, 1, 2),
    _ChmgrODestDestinationDsti_Type()
)
chmgrODestDestinationDsti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrODestDestinationDsti.setStatus("current")
_ChmgrOChannelTable_Object = MibTable
chmgrOChannelTable = _ChmgrOChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 4)
)
if mibBuilder.loadTexts:
    chmgrOChannelTable.setStatus("current")
_ChmgrOChannelEntry_Object = MibTableRow
chmgrOChannelEntry = _ChmgrOChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 4, 1)
)
chmgrOChannelEntry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrOConnIndex"),
    (0, "NETI-CHMGR-MIB", "chmgrODescrDestIndex"),
    (0, "NETI-CHMGR-MIB", "chmgrODescrChanIndex"),
)
if mibBuilder.loadTexts:
    chmgrOChannelEntry.setStatus("current")
_ChmgrOChanSourceRouteIndex_Type = Unsigned32
_ChmgrOChanSourceRouteIndex_Object = MibTableColumn
chmgrOChanSourceRouteIndex = _ChmgrOChanSourceRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 4, 1, 1),
    _ChmgrOChanSourceRouteIndex_Type()
)
chmgrOChanSourceRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOChanSourceRouteIndex.setStatus("current")
_ChmgrOChanChannelId_Type = ChannelId
_ChmgrOChanChannelId_Object = MibTableColumn
chmgrOChanChannelId = _ChmgrOChanChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 4, 1, 2),
    _ChmgrOChanChannelId_Type()
)
chmgrOChanChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOChanChannelId.setStatus("current")
_ChmgrOChanErrorMessage_Type = SnmpAdminString
_ChmgrOChanErrorMessage_Object = MibTableColumn
chmgrOChanErrorMessage = _ChmgrOChanErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 4, 1, 3),
    _ChmgrOChanErrorMessage_Type()
)
chmgrOChanErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOChanErrorMessage.setStatus("current")
_ChmgrOChanErrorAddress_Type = DtmNode
_ChmgrOChanErrorAddress_Object = MibTableColumn
chmgrOChanErrorAddress = _ChmgrOChanErrorAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 4, 1, 4),
    _ChmgrOChanErrorAddress_Type()
)
chmgrOChanErrorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOChanErrorAddress.setStatus("current")


class _ChmgrOChanOperStatus_Type(Integer32):
    """Custom type chmgrOChanOperStatus based on Integer32"""
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


_ChmgrOChanOperStatus_Type.__name__ = "Integer32"
_ChmgrOChanOperStatus_Object = MibTableColumn
chmgrOChanOperStatus = _ChmgrOChanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 4, 1, 5),
    _ChmgrOChanOperStatus_Type()
)
chmgrOChanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOChanOperStatus.setStatus("current")
_ChmgrOChanStatusChanged_Type = TimeStamp
_ChmgrOChanStatusChanged_Object = MibTableColumn
chmgrOChanStatusChanged = _ChmgrOChanStatusChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 4, 1, 6),
    _ChmgrOChanStatusChanged_Type()
)
chmgrOChanStatusChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOChanStatusChanged.setStatus("current")


class _ChmgrOChanReestablish_Type(Integer32):
    """Custom type chmgrOChanReestablish based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("reestablish", 1))
    )


_ChmgrOChanReestablish_Type.__name__ = "Integer32"
_ChmgrOChanReestablish_Object = MibTableColumn
chmgrOChanReestablish = _ChmgrOChanReestablish_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 4, 4, 1, 7),
    _ChmgrOChanReestablish_Type()
)
chmgrOChanReestablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chmgrOChanReestablish.setStatus("current")
_ChmgrTConnectionGroup_ObjectIdentity = ObjectIdentity
chmgrTConnectionGroup = _ChmgrTConnectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5)
)
_ChmgrTConnectionTimeStamp_Type = TimeStamp
_ChmgrTConnectionTimeStamp_Object = MibScalar
chmgrTConnectionTimeStamp = _ChmgrTConnectionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 1),
    _ChmgrTConnectionTimeStamp_Type()
)
chmgrTConnectionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnectionTimeStamp.setStatus("current")
_ChmgrTConnectionTable_Object = MibTable
chmgrTConnectionTable = _ChmgrTConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2)
)
if mibBuilder.loadTexts:
    chmgrTConnectionTable.setStatus("current")
_ChmgrTConnectionEntry_Object = MibTableRow
chmgrTConnectionEntry = _ChmgrTConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1)
)
chmgrTConnectionEntry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrTConnIndex"),
)
if mibBuilder.loadTexts:
    chmgrTConnectionEntry.setStatus("current")
_ChmgrTConnIndex_Type = Unsigned32
_ChmgrTConnIndex_Object = MibTableColumn
chmgrTConnIndex = _ChmgrTConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 1),
    _ChmgrTConnIndex_Type()
)
chmgrTConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrTConnIndex.setStatus("current")
_ChmgrTConnCustomerId_Type = Unsigned32
_ChmgrTConnCustomerId_Object = MibTableColumn
chmgrTConnCustomerId = _ChmgrTConnCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 2),
    _ChmgrTConnCustomerId_Type()
)
chmgrTConnCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnCustomerId.setStatus("current")


class _ChmgrTConnNumberOfChannels_Type(Unsigned32):
    """Custom type chmgrTConnNumberOfChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ChmgrTConnNumberOfChannels_Type.__name__ = "Unsigned32"
_ChmgrTConnNumberOfChannels_Object = MibTableColumn
chmgrTConnNumberOfChannels = _ChmgrTConnNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 3),
    _ChmgrTConnNumberOfChannels_Type()
)
chmgrTConnNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnNumberOfChannels.setStatus("current")


class _ChmgrTConnActiveChannel_Type(Unsigned32):
    """Custom type chmgrTConnActiveChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ChmgrTConnActiveChannel_Type.__name__ = "Unsigned32"
_ChmgrTConnActiveChannel_Object = MibTableColumn
chmgrTConnActiveChannel = _ChmgrTConnActiveChannel_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 4),
    _ChmgrTConnActiveChannel_Type()
)
chmgrTConnActiveChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnActiveChannel.setStatus("current")
_ChmgrTConnServiceReference_Type = RowPointer
_ChmgrTConnServiceReference_Object = MibTableColumn
chmgrTConnServiceReference = _ChmgrTConnServiceReference_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 5),
    _ChmgrTConnServiceReference_Type()
)
chmgrTConnServiceReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnServiceReference.setStatus("current")


class _ChmgrTConnAllocatedSlots_Type(Gauge32):
    """Custom type chmgrTConnAllocatedSlots based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8389),
    )


_ChmgrTConnAllocatedSlots_Type.__name__ = "Gauge32"
_ChmgrTConnAllocatedSlots_Object = MibTableColumn
chmgrTConnAllocatedSlots = _ChmgrTConnAllocatedSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 6),
    _ChmgrTConnAllocatedSlots_Type()
)
chmgrTConnAllocatedSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnAllocatedSlots.setStatus("current")
_ChmgrTConnAllocatedSlotsChanged_Type = TimeStamp
_ChmgrTConnAllocatedSlotsChanged_Object = MibTableColumn
chmgrTConnAllocatedSlotsChanged = _ChmgrTConnAllocatedSlotsChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 7),
    _ChmgrTConnAllocatedSlotsChanged_Type()
)
chmgrTConnAllocatedSlotsChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnAllocatedSlotsChanged.setStatus("current")
_ChmgrTConnDcapType_Type = DcapType
_ChmgrTConnDcapType_Object = MibTableColumn
chmgrTConnDcapType = _ChmgrTConnDcapType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 8),
    _ChmgrTConnDcapType_Type()
)
chmgrTConnDcapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnDcapType.setStatus("current")
_ChmgrTConnDst_Type = Dst
_ChmgrTConnDst_Object = MibTableColumn
chmgrTConnDst = _ChmgrTConnDst_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 9),
    _ChmgrTConnDst_Type()
)
chmgrTConnDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnDst.setStatus("current")
_ChmgrTConnSourceDsti_Type = Dsti
_ChmgrTConnSourceDsti_Object = MibTableColumn
chmgrTConnSourceDsti = _ChmgrTConnSourceDsti_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 10),
    _ChmgrTConnSourceDsti_Type()
)
chmgrTConnSourceDsti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnSourceDsti.setStatus("current")
_ChmgrTConnSourceAddress_Type = DtmNode
_ChmgrTConnSourceAddress_Object = MibTableColumn
chmgrTConnSourceAddress = _ChmgrTConnSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 11),
    _ChmgrTConnSourceAddress_Type()
)
chmgrTConnSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnSourceAddress.setStatus("current")
_ChmgrTConnDestinationDsti_Type = Dsti
_ChmgrTConnDestinationDsti_Object = MibTableColumn
chmgrTConnDestinationDsti = _ChmgrTConnDestinationDsti_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 12),
    _ChmgrTConnDestinationDsti_Type()
)
chmgrTConnDestinationDsti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnDestinationDsti.setStatus("current")
_ChmgrTConnDestinationAddress_Type = DtmNode
_ChmgrTConnDestinationAddress_Object = MibTableColumn
chmgrTConnDestinationAddress = _ChmgrTConnDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 13),
    _ChmgrTConnDestinationAddress_Type()
)
chmgrTConnDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnDestinationAddress.setStatus("current")
_ChmgrTConnStatusLastChanged_Type = TimeStamp
_ChmgrTConnStatusLastChanged_Object = MibTableColumn
chmgrTConnStatusLastChanged = _ChmgrTConnStatusLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 14),
    _ChmgrTConnStatusLastChanged_Type()
)
chmgrTConnStatusLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnStatusLastChanged.setStatus("current")


class _ChmgrTConnAdminStatus_Type(Integer32):
    """Custom type chmgrTConnAdminStatus based on Integer32"""
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


_ChmgrTConnAdminStatus_Type.__name__ = "Integer32"
_ChmgrTConnAdminStatus_Object = MibTableColumn
chmgrTConnAdminStatus = _ChmgrTConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 15),
    _ChmgrTConnAdminStatus_Type()
)
chmgrTConnAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnAdminStatus.setStatus("current")


class _ChmgrTConnOperStatus_Type(Integer32):
    """Custom type chmgrTConnOperStatus based on Integer32"""
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


_ChmgrTConnOperStatus_Type.__name__ = "Integer32"
_ChmgrTConnOperStatus_Object = MibTableColumn
chmgrTConnOperStatus = _ChmgrTConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 16),
    _ChmgrTConnOperStatus_Type()
)
chmgrTConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnOperStatus.setStatus("current")
_ChmgrTConnDcpVersion_Type = DcpVersion
_ChmgrTConnDcpVersion_Object = MibTableColumn
chmgrTConnDcpVersion = _ChmgrTConnDcpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 2, 1, 17),
    _ChmgrTConnDcpVersion_Type()
)
chmgrTConnDcpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTConnDcpVersion.setStatus("current")
_ChmgrTChannelTable_Object = MibTable
chmgrTChannelTable = _ChmgrTChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 3)
)
if mibBuilder.loadTexts:
    chmgrTChannelTable.setStatus("current")
_ChmgrTChannelEntry_Object = MibTableRow
chmgrTChannelEntry = _ChmgrTChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 3, 1)
)
chmgrTChannelEntry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrTConnIndex"),
    (0, "NETI-CHMGR-MIB", "chmgrTChanIndex"),
)
if mibBuilder.loadTexts:
    chmgrTChannelEntry.setStatus("current")


class _ChmgrTChanIndex_Type(Unsigned32):
    """Custom type chmgrTChanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ChmgrTChanIndex_Type.__name__ = "Unsigned32"
_ChmgrTChanIndex_Object = MibTableColumn
chmgrTChanIndex = _ChmgrTChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 3, 1, 1),
    _ChmgrTChanIndex_Type()
)
chmgrTChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrTChanIndex.setStatus("current")
_ChmgrTChanChannelId_Type = ChannelId
_ChmgrTChanChannelId_Object = MibTableColumn
chmgrTChanChannelId = _ChmgrTChanChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 3, 1, 2),
    _ChmgrTChanChannelId_Type()
)
chmgrTChanChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTChanChannelId.setStatus("current")
_ChmgrTChanCreated_Type = TimeStamp
_ChmgrTChanCreated_Object = MibTableColumn
chmgrTChanCreated = _ChmgrTChanCreated_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 5, 3, 1, 3),
    _ChmgrTChanCreated_Type()
)
chmgrTChanCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTChanCreated.setStatus("current")
_ChmgrStatisticsGroup_ObjectIdentity = ObjectIdentity
chmgrStatisticsGroup = _ChmgrStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6)
)
_ChmgrOStatDcap1Table_Object = MibTable
chmgrOStatDcap1Table = _ChmgrOStatDcap1Table_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 1)
)
if mibBuilder.loadTexts:
    chmgrOStatDcap1Table.setStatus("current")
_ChmgrOStatDcap1Entry_Object = MibTableRow
chmgrOStatDcap1Entry = _ChmgrOStatDcap1Entry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 1, 1)
)
chmgrOStatDcap1Entry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrOConnIndex"),
)
if mibBuilder.loadTexts:
    chmgrOStatDcap1Entry.setStatus("current")
_ChmgrOStatDcap1Octets_Type = Counter32
_ChmgrOStatDcap1Octets_Object = MibTableColumn
chmgrOStatDcap1Octets = _ChmgrOStatDcap1Octets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 1, 1, 1),
    _ChmgrOStatDcap1Octets_Type()
)
chmgrOStatDcap1Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOStatDcap1Octets.setStatus("current")
_ChmgrOStatDcap1Packets_Type = Counter32
_ChmgrOStatDcap1Packets_Object = MibTableColumn
chmgrOStatDcap1Packets = _ChmgrOStatDcap1Packets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 1, 1, 2),
    _ChmgrOStatDcap1Packets_Type()
)
chmgrOStatDcap1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOStatDcap1Packets.setStatus("current")
_ChmgrOStatDcap1UtilizedBps_Type = Gauge32
_ChmgrOStatDcap1UtilizedBps_Object = MibTableColumn
chmgrOStatDcap1UtilizedBps = _ChmgrOStatDcap1UtilizedBps_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 1, 1, 3),
    _ChmgrOStatDcap1UtilizedBps_Type()
)
chmgrOStatDcap1UtilizedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOStatDcap1UtilizedBps.setStatus("current")
_ChmgrOStatDcap1DiscardOctets_Type = Counter32
_ChmgrOStatDcap1DiscardOctets_Object = MibTableColumn
chmgrOStatDcap1DiscardOctets = _ChmgrOStatDcap1DiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 1, 1, 4),
    _ChmgrOStatDcap1DiscardOctets_Type()
)
chmgrOStatDcap1DiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOStatDcap1DiscardOctets.setStatus("current")
_ChmgrOStatDcap1DiscardPackets_Type = Counter32
_ChmgrOStatDcap1DiscardPackets_Object = MibTableColumn
chmgrOStatDcap1DiscardPackets = _ChmgrOStatDcap1DiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 1, 1, 5),
    _ChmgrOStatDcap1DiscardPackets_Type()
)
chmgrOStatDcap1DiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOStatDcap1DiscardPackets.setStatus("current")
_ChmgrOStatDcap1Bitrate_Type = Counter64
_ChmgrOStatDcap1Bitrate_Object = MibTableColumn
chmgrOStatDcap1Bitrate = _ChmgrOStatDcap1Bitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 1, 1, 6),
    _ChmgrOStatDcap1Bitrate_Type()
)
chmgrOStatDcap1Bitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOStatDcap1Bitrate.setStatus("current")


class _ChmgrOStatDcap1Load_Type(Unsigned32):
    """Custom type chmgrOStatDcap1Load based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChmgrOStatDcap1Load_Type.__name__ = "Unsigned32"
_ChmgrOStatDcap1Load_Object = MibTableColumn
chmgrOStatDcap1Load = _ChmgrOStatDcap1Load_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 1, 1, 7),
    _ChmgrOStatDcap1Load_Type()
)
chmgrOStatDcap1Load.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrOStatDcap1Load.setStatus("current")
_ChmgrTStatDcap1Table_Object = MibTable
chmgrTStatDcap1Table = _ChmgrTStatDcap1Table_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 2)
)
if mibBuilder.loadTexts:
    chmgrTStatDcap1Table.setStatus("current")
_ChmgrTStatDcap1Entry_Object = MibTableRow
chmgrTStatDcap1Entry = _ChmgrTStatDcap1Entry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 2, 1)
)
chmgrTStatDcap1Entry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrTConnIndex"),
)
if mibBuilder.loadTexts:
    chmgrTStatDcap1Entry.setStatus("current")
_ChmgrTStatDcap1Octets_Type = Counter32
_ChmgrTStatDcap1Octets_Object = MibTableColumn
chmgrTStatDcap1Octets = _ChmgrTStatDcap1Octets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 2, 1, 1),
    _ChmgrTStatDcap1Octets_Type()
)
chmgrTStatDcap1Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTStatDcap1Octets.setStatus("current")
_ChmgrTStatDcap1Packets_Type = Counter32
_ChmgrTStatDcap1Packets_Object = MibTableColumn
chmgrTStatDcap1Packets = _ChmgrTStatDcap1Packets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 2, 1, 2),
    _ChmgrTStatDcap1Packets_Type()
)
chmgrTStatDcap1Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTStatDcap1Packets.setStatus("current")
_ChmgrTStatDcap1UtilizedBps_Type = Gauge32
_ChmgrTStatDcap1UtilizedBps_Object = MibTableColumn
chmgrTStatDcap1UtilizedBps = _ChmgrTStatDcap1UtilizedBps_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 2, 1, 3),
    _ChmgrTStatDcap1UtilizedBps_Type()
)
chmgrTStatDcap1UtilizedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTStatDcap1UtilizedBps.setStatus("current")
_ChmgrTStatDcap1DiscardOctets_Type = Counter32
_ChmgrTStatDcap1DiscardOctets_Object = MibTableColumn
chmgrTStatDcap1DiscardOctets = _ChmgrTStatDcap1DiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 2, 1, 4),
    _ChmgrTStatDcap1DiscardOctets_Type()
)
chmgrTStatDcap1DiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTStatDcap1DiscardOctets.setStatus("current")
_ChmgrTStatDcap1DiscardPackets_Type = Counter32
_ChmgrTStatDcap1DiscardPackets_Object = MibTableColumn
chmgrTStatDcap1DiscardPackets = _ChmgrTStatDcap1DiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 2, 1, 5),
    _ChmgrTStatDcap1DiscardPackets_Type()
)
chmgrTStatDcap1DiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTStatDcap1DiscardPackets.setStatus("current")
_ChmgrTStatDcap1ErrorCRC_Type = Counter32
_ChmgrTStatDcap1ErrorCRC_Object = MibTableColumn
chmgrTStatDcap1ErrorCRC = _ChmgrTStatDcap1ErrorCRC_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 2, 1, 6),
    _ChmgrTStatDcap1ErrorCRC_Type()
)
chmgrTStatDcap1ErrorCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTStatDcap1ErrorCRC.setStatus("current")
_ChmgrTStatDcap1ErrorLods_Type = Counter32
_ChmgrTStatDcap1ErrorLods_Object = MibTableColumn
chmgrTStatDcap1ErrorLods = _ChmgrTStatDcap1ErrorLods_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 2, 1, 7),
    _ChmgrTStatDcap1ErrorLods_Type()
)
chmgrTStatDcap1ErrorLods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTStatDcap1ErrorLods.setStatus("current")
_ChmgrTStatDcap1Bitrate_Type = Counter64
_ChmgrTStatDcap1Bitrate_Object = MibTableColumn
chmgrTStatDcap1Bitrate = _ChmgrTStatDcap1Bitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 2, 1, 8),
    _ChmgrTStatDcap1Bitrate_Type()
)
chmgrTStatDcap1Bitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTStatDcap1Bitrate.setStatus("current")


class _ChmgrTStatDcap1Load_Type(Unsigned32):
    """Custom type chmgrTStatDcap1Load based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChmgrTStatDcap1Load_Type.__name__ = "Unsigned32"
_ChmgrTStatDcap1Load_Object = MibTableColumn
chmgrTStatDcap1Load = _ChmgrTStatDcap1Load_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 2, 1, 9),
    _ChmgrTStatDcap1Load_Type()
)
chmgrTStatDcap1Load.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTStatDcap1Load.setStatus("current")
_ChmgrTStatPMReferenceTable_Object = MibTable
chmgrTStatPMReferenceTable = _ChmgrTStatPMReferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 3)
)
if mibBuilder.loadTexts:
    chmgrTStatPMReferenceTable.setStatus("deprecated")
_ChmgrTStatPMReferenceEntry_Object = MibTableRow
chmgrTStatPMReferenceEntry = _ChmgrTStatPMReferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 3, 1)
)
chmgrTStatPMReferenceEntry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrTConnIndex"),
)
if mibBuilder.loadTexts:
    chmgrTStatPMReferenceEntry.setStatus("deprecated")
_ChmgrTStatPMReference_Type = RowPointer
_ChmgrTStatPMReference_Object = MibTableColumn
chmgrTStatPMReference = _ChmgrTStatPMReference_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 6, 3, 1, 1),
    _ChmgrTStatPMReference_Type()
)
chmgrTStatPMReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrTStatPMReference.setStatus("deprecated")
_ChmgrChannelGroup_ObjectIdentity = ObjectIdentity
chmgrChannelGroup = _ChmgrChannelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7)
)
_ChmgrChannelTable_Object = MibTable
chmgrChannelTable = _ChmgrChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1)
)
if mibBuilder.loadTexts:
    chmgrChannelTable.setStatus("current")
_ChmgrChannelEntry_Object = MibTableRow
chmgrChannelEntry = _ChmgrChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1)
)
chmgrChannelEntry.setIndexNames(
    (0, "NETI-CHMGR-MIB", "chmgrChanSourceMacAddress"),
    (0, "NETI-CHMGR-MIB", "chmgrChanChannelId"),
    (0, "NETI-CHMGR-MIB", "chmgrChanOutgoingIfBoard"),
    (0, "NETI-CHMGR-MIB", "chmgrChanOutgoingIfPort"),
)
if mibBuilder.loadTexts:
    chmgrChannelEntry.setStatus("current")
_ChmgrChanSourceMacAddress_Type = MacAddress
_ChmgrChanSourceMacAddress_Object = MibTableColumn
chmgrChanSourceMacAddress = _ChmgrChanSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 1),
    _ChmgrChanSourceMacAddress_Type()
)
chmgrChanSourceMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrChanSourceMacAddress.setStatus("current")
_ChmgrChanChannelId_Type = ChannelId
_ChmgrChanChannelId_Object = MibTableColumn
chmgrChanChannelId = _ChmgrChanChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 2),
    _ChmgrChanChannelId_Type()
)
chmgrChanChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrChanChannelId.setStatus("current")
_ChmgrChanOutgoingIfBoard_Type = Unsigned32
_ChmgrChanOutgoingIfBoard_Object = MibTableColumn
chmgrChanOutgoingIfBoard = _ChmgrChanOutgoingIfBoard_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 3),
    _ChmgrChanOutgoingIfBoard_Type()
)
chmgrChanOutgoingIfBoard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrChanOutgoingIfBoard.setStatus("current")
_ChmgrChanOutgoingIfPort_Type = Unsigned32
_ChmgrChanOutgoingIfPort_Object = MibTableColumn
chmgrChanOutgoingIfPort = _ChmgrChanOutgoingIfPort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 4),
    _ChmgrChanOutgoingIfPort_Type()
)
chmgrChanOutgoingIfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chmgrChanOutgoingIfPort.setStatus("current")
_ChmgrChanOutgoingIfMacAddress_Type = MacAddress
_ChmgrChanOutgoingIfMacAddress_Object = MibTableColumn
chmgrChanOutgoingIfMacAddress = _ChmgrChanOutgoingIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 5),
    _ChmgrChanOutgoingIfMacAddress_Type()
)
chmgrChanOutgoingIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrChanOutgoingIfMacAddress.setStatus("current")
_ChmgrChanNextHopMacAddress_Type = MacAddress
_ChmgrChanNextHopMacAddress_Object = MibTableColumn
chmgrChanNextHopMacAddress = _ChmgrChanNextHopMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 6),
    _ChmgrChanNextHopMacAddress_Type()
)
chmgrChanNextHopMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrChanNextHopMacAddress.setStatus("current")
_ChmgrChanNextHopDtmAddress_Type = DtmAddress
_ChmgrChanNextHopDtmAddress_Object = MibTableColumn
chmgrChanNextHopDtmAddress = _ChmgrChanNextHopDtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 7),
    _ChmgrChanNextHopDtmAddress_Type()
)
chmgrChanNextHopDtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrChanNextHopDtmAddress.setStatus("current")
_ChmgrChanIncomingIfBoard_Type = Unsigned32
_ChmgrChanIncomingIfBoard_Object = MibTableColumn
chmgrChanIncomingIfBoard = _ChmgrChanIncomingIfBoard_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 8),
    _ChmgrChanIncomingIfBoard_Type()
)
chmgrChanIncomingIfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrChanIncomingIfBoard.setStatus("current")
_ChmgrChanIncomingIfPort_Type = Unsigned32
_ChmgrChanIncomingIfPort_Object = MibTableColumn
chmgrChanIncomingIfPort = _ChmgrChanIncomingIfPort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 9),
    _ChmgrChanIncomingIfPort_Type()
)
chmgrChanIncomingIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrChanIncomingIfPort.setStatus("current")
_ChmgrChanSourceDtmAddress_Type = DtmAddress
_ChmgrChanSourceDtmAddress_Object = MibTableColumn
chmgrChanSourceDtmAddress = _ChmgrChanSourceDtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 10),
    _ChmgrChanSourceDtmAddress_Type()
)
chmgrChanSourceDtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrChanSourceDtmAddress.setStatus("current")
_ChmgrChanDst_Type = Dst
_ChmgrChanDst_Object = MibTableColumn
chmgrChanDst = _ChmgrChanDst_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 11),
    _ChmgrChanDst_Type()
)
chmgrChanDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrChanDst.setStatus("current")
_ChmgrChanSourceDsti_Type = Dsti
_ChmgrChanSourceDsti_Object = MibTableColumn
chmgrChanSourceDsti = _ChmgrChanSourceDsti_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 12),
    _ChmgrChanSourceDsti_Type()
)
chmgrChanSourceDsti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrChanSourceDsti.setStatus("current")
_ChmgrChanIsMulticast_Type = TruthValue
_ChmgrChanIsMulticast_Object = MibTableColumn
chmgrChanIsMulticast = _ChmgrChanIsMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 13),
    _ChmgrChanIsMulticast_Type()
)
chmgrChanIsMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrChanIsMulticast.setStatus("current")
_ChmgrChanCapacity_Type = Unsigned32
_ChmgrChanCapacity_Object = MibTableColumn
chmgrChanCapacity = _ChmgrChanCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 14),
    _ChmgrChanCapacity_Type()
)
chmgrChanCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrChanCapacity.setStatus("current")
_ChmgrChanDestDsti_Type = Dsti
_ChmgrChanDestDsti_Object = MibTableColumn
chmgrChanDestDsti = _ChmgrChanDestDsti_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 1, 7, 1, 1, 15),
    _ChmgrChanDestDsti_Type()
)
chmgrChanDestDsti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chmgrChanDestDsti.setStatus("current")
_ChmgrNotifications_ObjectIdentity = ObjectIdentity
chmgrNotifications = _ChmgrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 2)
)
_ChmgrConformance_ObjectIdentity = ObjectIdentity
chmgrConformance = _ChmgrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 14, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETI-CHMGR-MIB",
    **{"Dst": Dst,
       "Dsti": Dsti,
       "ChannelId": ChannelId,
       "DcapType": DcapType,
       "DtmNode": DtmNode,
       "DcpVersion": DcpVersion,
       "netiChmgrMIB": netiChmgrMIB,
       "chmgrObjects": chmgrObjects,
       "chmgrODescriptionGroup": chmgrODescriptionGroup,
       "chmgrODescriptionTimeStamp": chmgrODescriptionTimeStamp,
       "chmgrODescriptionTable": chmgrODescriptionTable,
       "chmgrODescriptionEntry": chmgrODescriptionEntry,
       "chmgrODescrIndex": chmgrODescrIndex,
       "chmgrODescrType": chmgrODescrType,
       "chmgrODescrCapabilities": chmgrODescrCapabilities,
       "chmgrODescrCustomerId": chmgrODescrCustomerId,
       "chmgrODescrServiceReference": chmgrODescrServiceReference,
       "chmgrODescrAcceptableBps": chmgrODescrAcceptableBps,
       "chmgrODescrAcceptableSlots": chmgrODescrAcceptableSlots,
       "chmgrODescrRequestedBps": chmgrODescrRequestedBps,
       "chmgrODescrRequestedSlots": chmgrODescrRequestedSlots,
       "chmgrODescrReestablishMethod": chmgrODescrReestablishMethod,
       "chmgrODescrMinInterval": chmgrODescrMinInterval,
       "chmgrODescrMaxInterval": chmgrODescrMaxInterval,
       "chmgrODescrEstablish": chmgrODescrEstablish,
       "chmgrODescrNextDestTableIndex": chmgrODescrNextDestTableIndex,
       "chmgrODescrPrecedence": chmgrODescrPrecedence,
       "chmgrODescrSuppressAlarms": chmgrODescrSuppressAlarms,
       "chmgrODescrAcceptableMbps": chmgrODescrAcceptableMbps,
       "chmgrODescrRequestedMbps": chmgrODescrRequestedMbps,
       "chmgrODescrRequestedDcpVersion": chmgrODescrRequestedDcpVersion,
       "chmgrODescrOneHopSpareCapUtilization": chmgrODescrOneHopSpareCapUtilization,
       "chmgrODescrDestinationTable": chmgrODescrDestinationTable,
       "chmgrODescrDestinationEntry": chmgrODescrDestinationEntry,
       "chmgrODescrDestIndex": chmgrODescrDestIndex,
       "chmgrODescrDestAddress": chmgrODescrDestAddress,
       "chmgrODescrDestDsti": chmgrODescrDestDsti,
       "chmgrODescrDestRowStatus": chmgrODescrDestRowStatus,
       "chmgrODescrDestAdminStatus": chmgrODescrDestAdminStatus,
       "chmgrODescrChannelTable": chmgrODescrChannelTable,
       "chmgrODescrChannelEntry": chmgrODescrChannelEntry,
       "chmgrODescrChanIndex": chmgrODescrChanIndex,
       "chmgrODescrChanSourceRouteIndex": chmgrODescrChanSourceRouteIndex,
       "chmgrODescrChanSourceRoute": chmgrODescrChanSourceRoute,
       "chmgrODescrChanRowStatus": chmgrODescrChanRowStatus,
       "chmgrTDescriptionGroup": chmgrTDescriptionGroup,
       "chmgrSourceRouteGroup": chmgrSourceRouteGroup,
       "chmgrSourceRouteTimeStamp": chmgrSourceRouteTimeStamp,
       "chmgrSourceRouteTable": chmgrSourceRouteTable,
       "chmgrSourceRouteEntry": chmgrSourceRouteEntry,
       "chmgrSourceRouteIndex": chmgrSourceRouteIndex,
       "chmgrSourceRouteName": chmgrSourceRouteName,
       "chmgrSourceRouteTypeOfRoute": chmgrSourceRouteTypeOfRoute,
       "chmgrSourceRouteFirstIfBoard": chmgrSourceRouteFirstIfBoard,
       "chmgrSourceRouteFirstIfPort": chmgrSourceRouteFirstIfPort,
       "chmgrSourceRouteRowStatus": chmgrSourceRouteRowStatus,
       "chmgrSourceRouteHopTable": chmgrSourceRouteHopTable,
       "chmgrSourceRouteHopEntry": chmgrSourceRouteHopEntry,
       "chmgrSourceRouteHopIndex": chmgrSourceRouteHopIndex,
       "chmgrSourceRouteHopAddress": chmgrSourceRouteHopAddress,
       "chmgrSourceRouteHopNextIfBoard": chmgrSourceRouteHopNextIfBoard,
       "chmgrSourceRouteHopNextIfPort": chmgrSourceRouteHopNextIfPort,
       "chmgrSourceRouteHopRowStatus": chmgrSourceRouteHopRowStatus,
       "chmgrOConnectionGroup": chmgrOConnectionGroup,
       "chmgrOConnectionTimeStamp": chmgrOConnectionTimeStamp,
       "chmgrOConnectionTable": chmgrOConnectionTable,
       "chmgrOConnectionEntry": chmgrOConnectionEntry,
       "chmgrOConnIndex": chmgrOConnIndex,
       "chmgrOConnCustomerId": chmgrOConnCustomerId,
       "chmgrOConnODescrIndex": chmgrOConnODescrIndex,
       "chmgrOConnServiceReference": chmgrOConnServiceReference,
       "chmgrOConnAllocatedSlots": chmgrOConnAllocatedSlots,
       "chmgrOConnAllocatedSlotsChanged": chmgrOConnAllocatedSlotsChanged,
       "chmgrOConnDcapType": chmgrOConnDcapType,
       "chmgrOConnDst": chmgrOConnDst,
       "chmgrOConnSourceAddress": chmgrOConnSourceAddress,
       "chmgrOConnSourceDsti": chmgrOConnSourceDsti,
       "chmgrOConnStatusLastChanged": chmgrOConnStatusLastChanged,
       "chmgrOConnAdminStatus": chmgrOConnAdminStatus,
       "chmgrOConnOperStatus": chmgrOConnOperStatus,
       "chmgrOConnReestablish": chmgrOConnReestablish,
       "chmgrOConnForceSourceRoute": chmgrOConnForceSourceRoute,
       "chmgrOConnDcpVersion": chmgrOConnDcpVersion,
       "chmgrODestinationTable": chmgrODestinationTable,
       "chmgrODestinationEntry": chmgrODestinationEntry,
       "chmgrODestDestinationAddress": chmgrODestDestinationAddress,
       "chmgrODestDestinationDsti": chmgrODestDestinationDsti,
       "chmgrOChannelTable": chmgrOChannelTable,
       "chmgrOChannelEntry": chmgrOChannelEntry,
       "chmgrOChanSourceRouteIndex": chmgrOChanSourceRouteIndex,
       "chmgrOChanChannelId": chmgrOChanChannelId,
       "chmgrOChanErrorMessage": chmgrOChanErrorMessage,
       "chmgrOChanErrorAddress": chmgrOChanErrorAddress,
       "chmgrOChanOperStatus": chmgrOChanOperStatus,
       "chmgrOChanStatusChanged": chmgrOChanStatusChanged,
       "chmgrOChanReestablish": chmgrOChanReestablish,
       "chmgrTConnectionGroup": chmgrTConnectionGroup,
       "chmgrTConnectionTimeStamp": chmgrTConnectionTimeStamp,
       "chmgrTConnectionTable": chmgrTConnectionTable,
       "chmgrTConnectionEntry": chmgrTConnectionEntry,
       "chmgrTConnIndex": chmgrTConnIndex,
       "chmgrTConnCustomerId": chmgrTConnCustomerId,
       "chmgrTConnNumberOfChannels": chmgrTConnNumberOfChannels,
       "chmgrTConnActiveChannel": chmgrTConnActiveChannel,
       "chmgrTConnServiceReference": chmgrTConnServiceReference,
       "chmgrTConnAllocatedSlots": chmgrTConnAllocatedSlots,
       "chmgrTConnAllocatedSlotsChanged": chmgrTConnAllocatedSlotsChanged,
       "chmgrTConnDcapType": chmgrTConnDcapType,
       "chmgrTConnDst": chmgrTConnDst,
       "chmgrTConnSourceDsti": chmgrTConnSourceDsti,
       "chmgrTConnSourceAddress": chmgrTConnSourceAddress,
       "chmgrTConnDestinationDsti": chmgrTConnDestinationDsti,
       "chmgrTConnDestinationAddress": chmgrTConnDestinationAddress,
       "chmgrTConnStatusLastChanged": chmgrTConnStatusLastChanged,
       "chmgrTConnAdminStatus": chmgrTConnAdminStatus,
       "chmgrTConnOperStatus": chmgrTConnOperStatus,
       "chmgrTConnDcpVersion": chmgrTConnDcpVersion,
       "chmgrTChannelTable": chmgrTChannelTable,
       "chmgrTChannelEntry": chmgrTChannelEntry,
       "chmgrTChanIndex": chmgrTChanIndex,
       "chmgrTChanChannelId": chmgrTChanChannelId,
       "chmgrTChanCreated": chmgrTChanCreated,
       "chmgrStatisticsGroup": chmgrStatisticsGroup,
       "chmgrOStatDcap1Table": chmgrOStatDcap1Table,
       "chmgrOStatDcap1Entry": chmgrOStatDcap1Entry,
       "chmgrOStatDcap1Octets": chmgrOStatDcap1Octets,
       "chmgrOStatDcap1Packets": chmgrOStatDcap1Packets,
       "chmgrOStatDcap1UtilizedBps": chmgrOStatDcap1UtilizedBps,
       "chmgrOStatDcap1DiscardOctets": chmgrOStatDcap1DiscardOctets,
       "chmgrOStatDcap1DiscardPackets": chmgrOStatDcap1DiscardPackets,
       "chmgrOStatDcap1Bitrate": chmgrOStatDcap1Bitrate,
       "chmgrOStatDcap1Load": chmgrOStatDcap1Load,
       "chmgrTStatDcap1Table": chmgrTStatDcap1Table,
       "chmgrTStatDcap1Entry": chmgrTStatDcap1Entry,
       "chmgrTStatDcap1Octets": chmgrTStatDcap1Octets,
       "chmgrTStatDcap1Packets": chmgrTStatDcap1Packets,
       "chmgrTStatDcap1UtilizedBps": chmgrTStatDcap1UtilizedBps,
       "chmgrTStatDcap1DiscardOctets": chmgrTStatDcap1DiscardOctets,
       "chmgrTStatDcap1DiscardPackets": chmgrTStatDcap1DiscardPackets,
       "chmgrTStatDcap1ErrorCRC": chmgrTStatDcap1ErrorCRC,
       "chmgrTStatDcap1ErrorLods": chmgrTStatDcap1ErrorLods,
       "chmgrTStatDcap1Bitrate": chmgrTStatDcap1Bitrate,
       "chmgrTStatDcap1Load": chmgrTStatDcap1Load,
       "chmgrTStatPMReferenceTable": chmgrTStatPMReferenceTable,
       "chmgrTStatPMReferenceEntry": chmgrTStatPMReferenceEntry,
       "chmgrTStatPMReference": chmgrTStatPMReference,
       "chmgrChannelGroup": chmgrChannelGroup,
       "chmgrChannelTable": chmgrChannelTable,
       "chmgrChannelEntry": chmgrChannelEntry,
       "chmgrChanSourceMacAddress": chmgrChanSourceMacAddress,
       "chmgrChanChannelId": chmgrChanChannelId,
       "chmgrChanOutgoingIfBoard": chmgrChanOutgoingIfBoard,
       "chmgrChanOutgoingIfPort": chmgrChanOutgoingIfPort,
       "chmgrChanOutgoingIfMacAddress": chmgrChanOutgoingIfMacAddress,
       "chmgrChanNextHopMacAddress": chmgrChanNextHopMacAddress,
       "chmgrChanNextHopDtmAddress": chmgrChanNextHopDtmAddress,
       "chmgrChanIncomingIfBoard": chmgrChanIncomingIfBoard,
       "chmgrChanIncomingIfPort": chmgrChanIncomingIfPort,
       "chmgrChanSourceDtmAddress": chmgrChanSourceDtmAddress,
       "chmgrChanDst": chmgrChanDst,
       "chmgrChanSourceDsti": chmgrChanSourceDsti,
       "chmgrChanIsMulticast": chmgrChanIsMulticast,
       "chmgrChanCapacity": chmgrChanCapacity,
       "chmgrChanDestDsti": chmgrChanDestDsti,
       "chmgrNotifications": chmgrNotifications,
       "chmgrConformance": chmgrConformance}
)
