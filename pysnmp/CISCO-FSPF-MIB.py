# SNMP MIB module (CISCO-FSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:44 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(DomainId,
 DomainIdOrZero) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "DomainId",
    "DomainIdOrZero")

(CiscoMilliSeconds,
 TimeIntervalMin,
 TimeIntervalSec) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoMilliSeconds",
    "TimeIntervalMin",
    "TimeIntervalSec")

(notifyVsanIndex,
 vsanIndex) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "notifyVsanIndex",
    "vsanIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoFspfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 287)
)
ciscoFspfMIB.setRevisions(
        ("2003-10-08 00:00",
         "2003-04-13 00:00",
         "2003-02-21 00:00",
         "2002-11-21 00:00",
         "2002-11-01 00:00",
         "2002-10-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FspfRegionId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class FspfLsrType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class FspfLinkType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class FspfInterfaceState(Integer32, TextualConvention):
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
        *(("dbAckwait", 4),
          ("dbExchange", 3),
          ("dbWait", 5),
          ("down", 1),
          ("full", 6),
          ("init", 2))
    )



class LastCreationTime(TimeTicks, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_FspfConfiguration_ObjectIdentity = ObjectIdentity
fspfConfiguration = _FspfConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1)
)
_FspfTable_Object = MibTable
fspfTable = _FspfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1)
)
if mibBuilder.loadTexts:
    fspfTable.setStatus("current")
_FspfEntry_Object = MibTableRow
fspfEntry = _FspfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1)
)
fspfEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    fspfEntry.setStatus("current")


class _FspfRegionId_Type(FspfRegionId):
    """Custom type fspfRegionId based on FspfRegionId"""
    defaultValue = 0


_FspfRegionId_Object = MibTableColumn
fspfRegionId = _FspfRegionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 1),
    _FspfRegionId_Type()
)
fspfRegionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfRegionId.setStatus("current")
_FspfDomainId_Type = DomainId
_FspfDomainId_Object = MibTableColumn
fspfDomainId = _FspfDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 2),
    _FspfDomainId_Type()
)
fspfDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfDomainId.setStatus("current")
_FspfSpfDelay_Type = TimeIntervalSec
_FspfSpfDelay_Object = MibTableColumn
fspfSpfDelay = _FspfSpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 3),
    _FspfSpfDelay_Type()
)
fspfSpfDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfSpfDelay.setStatus("current")
if mibBuilder.loadTexts:
    fspfSpfDelay.setUnits("Seconds")


class _FspfSpfHoldTime_Type(CiscoMilliSeconds):
    """Custom type fspfSpfHoldTime based on CiscoMilliSeconds"""
    defaultValue = 0

    subtypeSpec = CiscoMilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FspfSpfHoldTime_Type.__name__ = "CiscoMilliSeconds"
_FspfSpfHoldTime_Object = MibTableColumn
fspfSpfHoldTime = _FspfSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 4),
    _FspfSpfHoldTime_Type()
)
fspfSpfHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfSpfHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    fspfSpfHoldTime.setUnits("MilliSeconds")


class _FspfMinLsArrival_Type(CiscoMilliSeconds):
    """Custom type fspfMinLsArrival based on CiscoMilliSeconds"""
    defaultValue = 1000

    subtypeSpec = CiscoMilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FspfMinLsArrival_Type.__name__ = "CiscoMilliSeconds"
_FspfMinLsArrival_Object = MibTableColumn
fspfMinLsArrival = _FspfMinLsArrival_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 5),
    _FspfMinLsArrival_Type()
)
fspfMinLsArrival.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfMinLsArrival.setStatus("current")
if mibBuilder.loadTexts:
    fspfMinLsArrival.setUnits("MilliSeconds")


class _FspfMinLsInterval_Type(CiscoMilliSeconds):
    """Custom type fspfMinLsInterval based on CiscoMilliSeconds"""
    defaultValue = 5000

    subtypeSpec = CiscoMilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FspfMinLsInterval_Type.__name__ = "CiscoMilliSeconds"
_FspfMinLsInterval_Object = MibTableColumn
fspfMinLsInterval = _FspfMinLsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 6),
    _FspfMinLsInterval_Type()
)
fspfMinLsInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfMinLsInterval.setStatus("current")
if mibBuilder.loadTexts:
    fspfMinLsInterval.setUnits("MilliSeconds")
_FspfLsRefreshTime_Type = TimeIntervalMin
_FspfLsRefreshTime_Object = MibTableColumn
fspfLsRefreshTime = _FspfLsRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 7),
    _FspfLsRefreshTime_Type()
)
fspfLsRefreshTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsRefreshTime.setStatus("current")
if mibBuilder.loadTexts:
    fspfLsRefreshTime.setUnits("Minutes")
_FspfMaxAge_Type = TimeIntervalMin
_FspfMaxAge_Object = MibTableColumn
fspfMaxAge = _FspfMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 8),
    _FspfMaxAge_Type()
)
fspfMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    fspfMaxAge.setUnits("Minutes")
_FspfMaxAgeCount_Type = Counter32
_FspfMaxAgeCount_Object = MibTableColumn
fspfMaxAgeCount = _FspfMaxAgeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 9),
    _FspfMaxAgeCount_Type()
)
fspfMaxAgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfMaxAgeCount.setStatus("current")
_FspfSpfComputations_Type = Counter32
_FspfSpfComputations_Object = MibTableColumn
fspfSpfComputations = _FspfSpfComputations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 10),
    _FspfSpfComputations_Type()
)
fspfSpfComputations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfSpfComputations.setStatus("current")
_FspfChecksumErrors_Type = Counter32
_FspfChecksumErrors_Object = MibTableColumn
fspfChecksumErrors = _FspfChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 11),
    _FspfChecksumErrors_Type()
)
fspfChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfChecksumErrors.setStatus("current")
_FspfLsuRxPkts_Type = Counter32
_FspfLsuRxPkts_Object = MibTableColumn
fspfLsuRxPkts = _FspfLsuRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 12),
    _FspfLsuRxPkts_Type()
)
fspfLsuRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsuRxPkts.setStatus("current")
_FspfLsaRxPkts_Type = Counter32
_FspfLsaRxPkts_Object = MibTableColumn
fspfLsaRxPkts = _FspfLsaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 13),
    _FspfLsaRxPkts_Type()
)
fspfLsaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsaRxPkts.setStatus("current")
_FspfLsuTxPkts_Type = Counter32
_FspfLsuTxPkts_Object = MibTableColumn
fspfLsuTxPkts = _FspfLsuTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 14),
    _FspfLsuTxPkts_Type()
)
fspfLsuTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsuTxPkts.setStatus("current")
_FspfLsaTxPkts_Type = Counter32
_FspfLsaTxPkts_Object = MibTableColumn
fspfLsaTxPkts = _FspfLsaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 15),
    _FspfLsaTxPkts_Type()
)
fspfLsaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsaTxPkts.setStatus("current")
_FspfHelloTxPkts_Type = Counter32
_FspfHelloTxPkts_Object = MibTableColumn
fspfHelloTxPkts = _FspfHelloTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 16),
    _FspfHelloTxPkts_Type()
)
fspfHelloTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfHelloTxPkts.setStatus("current")
_FspfHelloRxPkts_Type = Counter32
_FspfHelloRxPkts_Object = MibTableColumn
fspfHelloRxPkts = _FspfHelloRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 17),
    _FspfHelloRxPkts_Type()
)
fspfHelloRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfHelloRxPkts.setStatus("current")
_FspfRetransmittedLsuTxPkts_Type = Counter32
_FspfRetransmittedLsuTxPkts_Object = MibTableColumn
fspfRetransmittedLsuTxPkts = _FspfRetransmittedLsuTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 18),
    _FspfRetransmittedLsuTxPkts_Type()
)
fspfRetransmittedLsuTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfRetransmittedLsuTxPkts.setStatus("current")
_FspfErrorRxPkts_Type = Counter32
_FspfErrorRxPkts_Object = MibTableColumn
fspfErrorRxPkts = _FspfErrorRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 19),
    _FspfErrorRxPkts_Type()
)
fspfErrorRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfErrorRxPkts.setStatus("current")
_FspfLsrs_Type = Gauge32
_FspfLsrs_Object = MibTableColumn
fspfLsrs = _FspfLsrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 20),
    _FspfLsrs_Type()
)
fspfLsrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsrs.setStatus("current")
_FspfCreateTime_Type = LastCreationTime
_FspfCreateTime_Object = MibTableColumn
fspfCreateTime = _FspfCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 21),
    _FspfCreateTime_Type()
)
fspfCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfCreateTime.setStatus("current")


class _FspfAdminStatus_Type(Integer32):
    """Custom type fspfAdminStatus based on Integer32"""
    defaultValue = 1

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


_FspfAdminStatus_Type.__name__ = "Integer32"
_FspfAdminStatus_Object = MibTableColumn
fspfAdminStatus = _FspfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 22),
    _FspfAdminStatus_Type()
)
fspfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfAdminStatus.setStatus("current")


class _FspfOperStatus_Type(Integer32):
    """Custom type fspfOperStatus based on Integer32"""
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


_FspfOperStatus_Type.__name__ = "Integer32"
_FspfOperStatus_Object = MibTableColumn
fspfOperStatus = _FspfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 23),
    _FspfOperStatus_Type()
)
fspfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfOperStatus.setStatus("current")


class _FspfSetToDefault_Type(Integer32):
    """Custom type fspfSetToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("noOp", 2))
    )


_FspfSetToDefault_Type.__name__ = "Integer32"
_FspfSetToDefault_Object = MibTableColumn
fspfSetToDefault = _FspfSetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 24),
    _FspfSetToDefault_Type()
)
fspfSetToDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfSetToDefault.setStatus("current")
_FspfRowStatus_Type = RowStatus
_FspfRowStatus_Object = MibTableColumn
fspfRowStatus = _FspfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 25),
    _FspfRowStatus_Type()
)
fspfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfRowStatus.setStatus("current")
_FspfTotalCheckSum_Type = Unsigned32
_FspfTotalCheckSum_Object = MibTableColumn
fspfTotalCheckSum = _FspfTotalCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 1, 1, 26),
    _FspfTotalCheckSum_Type()
)
fspfTotalCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfTotalCheckSum.setStatus("current")
_FspfIfTable_Object = MibTable
fspfIfTable = _FspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2)
)
if mibBuilder.loadTexts:
    fspfIfTable.setStatus("current")
_FspfIfEntry_Object = MibTableRow
fspfIfEntry = _FspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1)
)
fspfIfEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fspfIfEntry.setStatus("current")


class _FspfIfCost_Type(Unsigned32):
    """Custom type fspfIfCost based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FspfIfCost_Type.__name__ = "Unsigned32"
_FspfIfCost_Object = MibTableColumn
fspfIfCost = _FspfIfCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 1),
    _FspfIfCost_Type()
)
fspfIfCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfIfCost.setStatus("current")


class _FspfIfHelloInterval_Type(TimeIntervalSec):
    """Custom type fspfIfHelloInterval based on TimeIntervalSec"""
    defaultValue = 20

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FspfIfHelloInterval_Type.__name__ = "TimeIntervalSec"
_FspfIfHelloInterval_Object = MibTableColumn
fspfIfHelloInterval = _FspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 2),
    _FspfIfHelloInterval_Type()
)
fspfIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    fspfIfHelloInterval.setUnits("Seconds")


class _FspfIfDeadInterval_Type(TimeIntervalSec):
    """Custom type fspfIfDeadInterval based on TimeIntervalSec"""
    defaultValue = 80

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_FspfIfDeadInterval_Type.__name__ = "TimeIntervalSec"
_FspfIfDeadInterval_Object = MibTableColumn
fspfIfDeadInterval = _FspfIfDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 3),
    _FspfIfDeadInterval_Type()
)
fspfIfDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfIfDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    fspfIfDeadInterval.setUnits("Seconds")


class _FspfIfRetransmitInterval_Type(TimeIntervalSec):
    """Custom type fspfIfRetransmitInterval based on TimeIntervalSec"""
    defaultValue = 5

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FspfIfRetransmitInterval_Type.__name__ = "TimeIntervalSec"
_FspfIfRetransmitInterval_Object = MibTableColumn
fspfIfRetransmitInterval = _FspfIfRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 4),
    _FspfIfRetransmitInterval_Type()
)
fspfIfRetransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfIfRetransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    fspfIfRetransmitInterval.setUnits("Seconds")
_FspfIfLsuRxPkts_Type = Counter32
_FspfIfLsuRxPkts_Object = MibTableColumn
fspfIfLsuRxPkts = _FspfIfLsuRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 5),
    _FspfIfLsuRxPkts_Type()
)
fspfIfLsuRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfLsuRxPkts.setStatus("current")
_FspfIfLsaRxPkts_Type = Counter32
_FspfIfLsaRxPkts_Object = MibTableColumn
fspfIfLsaRxPkts = _FspfIfLsaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 6),
    _FspfIfLsaRxPkts_Type()
)
fspfIfLsaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfLsaRxPkts.setStatus("current")
_FspfIfLsuTxPkts_Type = Counter32
_FspfIfLsuTxPkts_Object = MibTableColumn
fspfIfLsuTxPkts = _FspfIfLsuTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 7),
    _FspfIfLsuTxPkts_Type()
)
fspfIfLsuTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfLsuTxPkts.setStatus("current")
_FspfIfLsaTxPkts_Type = Counter32
_FspfIfLsaTxPkts_Object = MibTableColumn
fspfIfLsaTxPkts = _FspfIfLsaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 8),
    _FspfIfLsaTxPkts_Type()
)
fspfIfLsaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfLsaTxPkts.setStatus("current")
_FspfIfHelloTxPkts_Type = Counter32
_FspfIfHelloTxPkts_Object = MibTableColumn
fspfIfHelloTxPkts = _FspfIfHelloTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 9),
    _FspfIfHelloTxPkts_Type()
)
fspfIfHelloTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfHelloTxPkts.setStatus("current")
_FspfIfHelloRxPkts_Type = Counter32
_FspfIfHelloRxPkts_Object = MibTableColumn
fspfIfHelloRxPkts = _FspfIfHelloRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 10),
    _FspfIfHelloRxPkts_Type()
)
fspfIfHelloRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfHelloRxPkts.setStatus("current")
_FspfIfRetransmittedLsuTxPkts_Type = Counter32
_FspfIfRetransmittedLsuTxPkts_Object = MibTableColumn
fspfIfRetransmittedLsuTxPkts = _FspfIfRetransmittedLsuTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 11),
    _FspfIfRetransmittedLsuTxPkts_Type()
)
fspfIfRetransmittedLsuTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfRetransmittedLsuTxPkts.setStatus("current")
_FspfIfErrorRxPkts_Type = Counter32
_FspfIfErrorRxPkts_Object = MibTableColumn
fspfIfErrorRxPkts = _FspfIfErrorRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 12),
    _FspfIfErrorRxPkts_Type()
)
fspfIfErrorRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfErrorRxPkts.setStatus("current")
_FspfIfInactivityExpirations_Type = Counter32
_FspfIfInactivityExpirations_Object = MibTableColumn
fspfIfInactivityExpirations = _FspfIfInactivityExpirations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 13),
    _FspfIfInactivityExpirations_Type()
)
fspfIfInactivityExpirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfInactivityExpirations.setStatus("current")
_FspfIfNbrState_Type = FspfInterfaceState
_FspfIfNbrState_Object = MibTableColumn
fspfIfNbrState = _FspfIfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 14),
    _FspfIfNbrState_Type()
)
fspfIfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfNbrState.setStatus("current")
_FspfIfNbrDomainId_Type = DomainIdOrZero
_FspfIfNbrDomainId_Object = MibTableColumn
fspfIfNbrDomainId = _FspfIfNbrDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 15),
    _FspfIfNbrDomainId_Type()
)
fspfIfNbrDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfNbrDomainId.setStatus("current")


class _FspfIfNbrPortIndex_Type(Unsigned32):
    """Custom type fspfIfNbrPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FspfIfNbrPortIndex_Type.__name__ = "Unsigned32"
_FspfIfNbrPortIndex_Object = MibTableColumn
fspfIfNbrPortIndex = _FspfIfNbrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 16),
    _FspfIfNbrPortIndex_Type()
)
fspfIfNbrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfNbrPortIndex.setStatus("current")


class _FspfIfAdminStatus_Type(Integer32):
    """Custom type fspfIfAdminStatus based on Integer32"""
    defaultValue = 1

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


_FspfIfAdminStatus_Type.__name__ = "Integer32"
_FspfIfAdminStatus_Object = MibTableColumn
fspfIfAdminStatus = _FspfIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 17),
    _FspfIfAdminStatus_Type()
)
fspfIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfIfAdminStatus.setStatus("current")
_FspfIfCreateTime_Type = LastCreationTime
_FspfIfCreateTime_Object = MibTableColumn
fspfIfCreateTime = _FspfIfCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 18),
    _FspfIfCreateTime_Type()
)
fspfIfCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfIfCreateTime.setStatus("current")


class _FspfIfSetToDefault_Type(Integer32):
    """Custom type fspfIfSetToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("noOp", 2))
    )


_FspfIfSetToDefault_Type.__name__ = "Integer32"
_FspfIfSetToDefault_Object = MibTableColumn
fspfIfSetToDefault = _FspfIfSetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 19),
    _FspfIfSetToDefault_Type()
)
fspfIfSetToDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfIfSetToDefault.setStatus("current")
_FspfIfRowStatus_Type = RowStatus
_FspfIfRowStatus_Object = MibTableColumn
fspfIfRowStatus = _FspfIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 2, 1, 20),
    _FspfIfRowStatus_Type()
)
fspfIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspfIfRowStatus.setStatus("current")


class _FspfNbrStateChangeNotifyEnable_Type(TruthValue):
    """Custom type fspfNbrStateChangeNotifyEnable based on TruthValue"""


_FspfNbrStateChangeNotifyEnable_Object = MibScalar
fspfNbrStateChangeNotifyEnable = _FspfNbrStateChangeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 3),
    _FspfNbrStateChangeNotifyEnable_Type()
)
fspfNbrStateChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspfNbrStateChangeNotifyEnable.setStatus("current")
_FspfIfPrevNbrState_Type = FspfInterfaceState
_FspfIfPrevNbrState_Object = MibScalar
fspfIfPrevNbrState = _FspfIfPrevNbrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 1, 4),
    _FspfIfPrevNbrState_Type()
)
fspfIfPrevNbrState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fspfIfPrevNbrState.setStatus("current")
_FspfDatabase_ObjectIdentity = ObjectIdentity
fspfDatabase = _FspfDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2)
)
_FspfLsrTable_Object = MibTable
fspfLsrTable = _FspfLsrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1)
)
if mibBuilder.loadTexts:
    fspfLsrTable.setStatus("current")
_FspfLsrEntry_Object = MibTableRow
fspfLsrEntry = _FspfLsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1)
)
fspfLsrEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FSPF-MIB", "fspfLsrDomainId"),
    (0, "CISCO-FSPF-MIB", "fspfLsrType"),
)
if mibBuilder.loadTexts:
    fspfLsrEntry.setStatus("current")
_FspfLsrDomainId_Type = DomainId
_FspfLsrDomainId_Object = MibTableColumn
fspfLsrDomainId = _FspfLsrDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 1),
    _FspfLsrDomainId_Type()
)
fspfLsrDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fspfLsrDomainId.setStatus("current")
_FspfLsrType_Type = FspfLsrType
_FspfLsrType_Object = MibTableColumn
fspfLsrType = _FspfLsrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 2),
    _FspfLsrType_Type()
)
fspfLsrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fspfLsrType.setStatus("current")
_FspfLsrAdvDomainId_Type = DomainId
_FspfLsrAdvDomainId_Object = MibTableColumn
fspfLsrAdvDomainId = _FspfLsrAdvDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 3),
    _FspfLsrAdvDomainId_Type()
)
fspfLsrAdvDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsrAdvDomainId.setStatus("current")


class _FspfLsrAge_Type(TimeIntervalSec):
    """Custom type fspfLsrAge based on TimeIntervalSec"""
    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FspfLsrAge_Type.__name__ = "TimeIntervalSec"
_FspfLsrAge_Object = MibTableColumn
fspfLsrAge = _FspfLsrAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 4),
    _FspfLsrAge_Type()
)
fspfLsrAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsrAge.setStatus("current")
if mibBuilder.loadTexts:
    fspfLsrAge.setUnits("Seconds")


class _FspfLsrIncarnationNumber_Type(Unsigned32):
    """Custom type fspfLsrIncarnationNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FspfLsrIncarnationNumber_Type.__name__ = "Unsigned32"
_FspfLsrIncarnationNumber_Object = MibTableColumn
fspfLsrIncarnationNumber = _FspfLsrIncarnationNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 5),
    _FspfLsrIncarnationNumber_Type()
)
fspfLsrIncarnationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsrIncarnationNumber.setStatus("current")


class _FspfLsrCheckSum_Type(Unsigned32):
    """Custom type fspfLsrCheckSum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FspfLsrCheckSum_Type.__name__ = "Unsigned32"
_FspfLsrCheckSum_Object = MibTableColumn
fspfLsrCheckSum = _FspfLsrCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 6),
    _FspfLsrCheckSum_Type()
)
fspfLsrCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsrCheckSum.setStatus("current")


class _FspfLsrLinks_Type(Unsigned32):
    """Custom type fspfLsrLinks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65355),
    )


_FspfLsrLinks_Type.__name__ = "Unsigned32"
_FspfLsrLinks_Object = MibTableColumn
fspfLsrLinks = _FspfLsrLinks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 7),
    _FspfLsrLinks_Type()
)
fspfLsrLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsrLinks.setStatus("current")
_FspfLsrExternal_Type = TruthValue
_FspfLsrExternal_Object = MibTableColumn
fspfLsrExternal = _FspfLsrExternal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 1, 1, 8),
    _FspfLsrExternal_Type()
)
fspfLsrExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsrExternal.setStatus("current")
_FspfLinkTable_Object = MibTable
fspfLinkTable = _FspfLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2)
)
if mibBuilder.loadTexts:
    fspfLinkTable.setStatus("current")
_FspfLinkEntry_Object = MibTableRow
fspfLinkEntry = _FspfLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1)
)
fspfLinkEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FSPF-MIB", "fspfLsrDomainId"),
    (0, "CISCO-FSPF-MIB", "fspfLsrType"),
    (0, "CISCO-FSPF-MIB", "fspfLinkIndex"),
)
if mibBuilder.loadTexts:
    fspfLinkEntry.setStatus("current")
_FspfLinkIndex_Type = Unsigned32
_FspfLinkIndex_Object = MibTableColumn
fspfLinkIndex = _FspfLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1, 1),
    _FspfLinkIndex_Type()
)
fspfLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fspfLinkIndex.setStatus("current")
_FspfLinkNbrDomainId_Type = DomainId
_FspfLinkNbrDomainId_Object = MibTableColumn
fspfLinkNbrDomainId = _FspfLinkNbrDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1, 2),
    _FspfLinkNbrDomainId_Type()
)
fspfLinkNbrDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLinkNbrDomainId.setStatus("current")


class _FspfLinkPortIndex_Type(Unsigned32):
    """Custom type fspfLinkPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FspfLinkPortIndex_Type.__name__ = "Unsigned32"
_FspfLinkPortIndex_Object = MibTableColumn
fspfLinkPortIndex = _FspfLinkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1, 3),
    _FspfLinkPortIndex_Type()
)
fspfLinkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLinkPortIndex.setStatus("current")


class _FspfLinkNbrPortIndex_Type(Unsigned32):
    """Custom type fspfLinkNbrPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FspfLinkNbrPortIndex_Type.__name__ = "Unsigned32"
_FspfLinkNbrPortIndex_Object = MibTableColumn
fspfLinkNbrPortIndex = _FspfLinkNbrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1, 4),
    _FspfLinkNbrPortIndex_Type()
)
fspfLinkNbrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLinkNbrPortIndex.setStatus("current")
_FspfLinkType_Type = FspfLinkType
_FspfLinkType_Object = MibTableColumn
fspfLinkType = _FspfLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1, 5),
    _FspfLinkType_Type()
)
fspfLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLinkType.setStatus("current")


class _FspfLinkCost_Type(Integer32):
    """Custom type fspfLinkCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FspfLinkCost_Type.__name__ = "Integer32"
_FspfLinkCost_Object = MibTableColumn
fspfLinkCost = _FspfLinkCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 2, 1, 6),
    _FspfLinkCost_Type()
)
fspfLinkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLinkCost.setStatus("current")


class _FspfLsrNumber_Type(Unsigned32):
    """Custom type fspfLsrNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FspfLsrNumber_Type.__name__ = "Unsigned32"
_FspfLsrNumber_Object = MibScalar
fspfLsrNumber = _FspfLsrNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 3),
    _FspfLsrNumber_Type()
)
fspfLsrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLsrNumber.setStatus("current")


class _FspfLinkNumber_Type(Unsigned32):
    """Custom type fspfLinkNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FspfLinkNumber_Type.__name__ = "Unsigned32"
_FspfLinkNumber_Object = MibScalar
fspfLinkNumber = _FspfLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 2, 4),
    _FspfLinkNumber_Type()
)
fspfLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspfLinkNumber.setStatus("current")
_FspfNotificationPrefix_ObjectIdentity = ObjectIdentity
fspfNotificationPrefix = _FspfNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 3)
)
_FspfNotification_ObjectIdentity = ObjectIdentity
fspfNotification = _FspfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 3, 0)
)
_FspfMIBConformance_ObjectIdentity = ObjectIdentity
fspfMIBConformance = _FspfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4)
)
_FspfMIBCompliances_ObjectIdentity = ObjectIdentity
fspfMIBCompliances = _FspfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 1)
)
_FspfMIBGroups_ObjectIdentity = ObjectIdentity
fspfMIBGroups = _FspfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2)
)

# Managed Objects groups

fspfGenericGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 1)
)
fspfGenericGroup.setObjects(
      *(("CISCO-FSPF-MIB", "fspfRegionId"),
        ("CISCO-FSPF-MIB", "fspfDomainId"),
        ("CISCO-FSPF-MIB", "fspfSpfDelay"),
        ("CISCO-FSPF-MIB", "fspfSpfHoldTime"),
        ("CISCO-FSPF-MIB", "fspfMinLsArrival"),
        ("CISCO-FSPF-MIB", "fspfMinLsInterval"),
        ("CISCO-FSPF-MIB", "fspfLsRefreshTime"),
        ("CISCO-FSPF-MIB", "fspfMaxAge"),
        ("CISCO-FSPF-MIB", "fspfMaxAgeCount"),
        ("CISCO-FSPF-MIB", "fspfSpfComputations"),
        ("CISCO-FSPF-MIB", "fspfChecksumErrors"),
        ("CISCO-FSPF-MIB", "fspfLsuRxPkts"),
        ("CISCO-FSPF-MIB", "fspfLsaRxPkts"),
        ("CISCO-FSPF-MIB", "fspfLsuTxPkts"),
        ("CISCO-FSPF-MIB", "fspfLsaTxPkts"),
        ("CISCO-FSPF-MIB", "fspfHelloTxPkts"),
        ("CISCO-FSPF-MIB", "fspfHelloRxPkts"),
        ("CISCO-FSPF-MIB", "fspfRetransmittedLsuTxPkts"),
        ("CISCO-FSPF-MIB", "fspfErrorRxPkts"),
        ("CISCO-FSPF-MIB", "fspfLsrs"),
        ("CISCO-FSPF-MIB", "fspfCreateTime"),
        ("CISCO-FSPF-MIB", "fspfAdminStatus"),
        ("CISCO-FSPF-MIB", "fspfOperStatus"),
        ("CISCO-FSPF-MIB", "fspfSetToDefault"),
        ("CISCO-FSPF-MIB", "fspfRowStatus"),
        ("CISCO-FSPF-MIB", "fspfNbrStateChangeNotifyEnable"))
)
if mibBuilder.loadTexts:
    fspfGenericGroup.setStatus("deprecated")

fspfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 3)
)
fspfIfGroup.setObjects(
      *(("CISCO-FSPF-MIB", "fspfIfCost"),
        ("CISCO-FSPF-MIB", "fspfIfHelloInterval"),
        ("CISCO-FSPF-MIB", "fspfIfDeadInterval"),
        ("CISCO-FSPF-MIB", "fspfIfRetransmitInterval"),
        ("CISCO-FSPF-MIB", "fspfIfLsuRxPkts"),
        ("CISCO-FSPF-MIB", "fspfIfLsaRxPkts"),
        ("CISCO-FSPF-MIB", "fspfIfLsuTxPkts"),
        ("CISCO-FSPF-MIB", "fspfIfLsaTxPkts"),
        ("CISCO-FSPF-MIB", "fspfIfHelloTxPkts"),
        ("CISCO-FSPF-MIB", "fspfIfHelloRxPkts"),
        ("CISCO-FSPF-MIB", "fspfIfRetransmittedLsuTxPkts"),
        ("CISCO-FSPF-MIB", "fspfIfErrorRxPkts"),
        ("CISCO-FSPF-MIB", "fspfIfInactivityExpirations"),
        ("CISCO-FSPF-MIB", "fspfIfNbrState"),
        ("CISCO-FSPF-MIB", "fspfIfNbrDomainId"),
        ("CISCO-FSPF-MIB", "fspfIfNbrPortIndex"),
        ("CISCO-FSPF-MIB", "fspfIfAdminStatus"),
        ("CISCO-FSPF-MIB", "fspfIfCreateTime"),
        ("CISCO-FSPF-MIB", "fspfIfSetToDefault"),
        ("CISCO-FSPF-MIB", "fspfIfRowStatus"),
        ("CISCO-FSPF-MIB", "fspfIfPrevNbrState"))
)
if mibBuilder.loadTexts:
    fspfIfGroup.setStatus("current")

fspfDatabaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 4)
)
fspfDatabaseGroup.setObjects(
      *(("CISCO-FSPF-MIB", "fspfLsrAdvDomainId"),
        ("CISCO-FSPF-MIB", "fspfLsrAge"),
        ("CISCO-FSPF-MIB", "fspfLsrIncarnationNumber"),
        ("CISCO-FSPF-MIB", "fspfLsrCheckSum"),
        ("CISCO-FSPF-MIB", "fspfLsrLinks"),
        ("CISCO-FSPF-MIB", "fspfLinkNbrDomainId"),
        ("CISCO-FSPF-MIB", "fspfLinkPortIndex"),
        ("CISCO-FSPF-MIB", "fspfLinkNbrPortIndex"),
        ("CISCO-FSPF-MIB", "fspfLinkType"),
        ("CISCO-FSPF-MIB", "fspfLinkCost"))
)
if mibBuilder.loadTexts:
    fspfDatabaseGroup.setStatus("deprecated")

fspfGenericGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 6)
)
fspfGenericGroupRev1.setObjects(
      *(("CISCO-FSPF-MIB", "fspfRegionId"),
        ("CISCO-FSPF-MIB", "fspfDomainId"),
        ("CISCO-FSPF-MIB", "fspfSpfDelay"),
        ("CISCO-FSPF-MIB", "fspfSpfHoldTime"),
        ("CISCO-FSPF-MIB", "fspfMinLsArrival"),
        ("CISCO-FSPF-MIB", "fspfMinLsInterval"),
        ("CISCO-FSPF-MIB", "fspfLsRefreshTime"),
        ("CISCO-FSPF-MIB", "fspfMaxAge"),
        ("CISCO-FSPF-MIB", "fspfMaxAgeCount"),
        ("CISCO-FSPF-MIB", "fspfSpfComputations"),
        ("CISCO-FSPF-MIB", "fspfChecksumErrors"),
        ("CISCO-FSPF-MIB", "fspfLsuRxPkts"),
        ("CISCO-FSPF-MIB", "fspfLsaRxPkts"),
        ("CISCO-FSPF-MIB", "fspfLsuTxPkts"),
        ("CISCO-FSPF-MIB", "fspfLsaTxPkts"),
        ("CISCO-FSPF-MIB", "fspfHelloTxPkts"),
        ("CISCO-FSPF-MIB", "fspfHelloRxPkts"),
        ("CISCO-FSPF-MIB", "fspfRetransmittedLsuTxPkts"),
        ("CISCO-FSPF-MIB", "fspfErrorRxPkts"),
        ("CISCO-FSPF-MIB", "fspfLsrs"),
        ("CISCO-FSPF-MIB", "fspfCreateTime"),
        ("CISCO-FSPF-MIB", "fspfAdminStatus"),
        ("CISCO-FSPF-MIB", "fspfOperStatus"),
        ("CISCO-FSPF-MIB", "fspfSetToDefault"),
        ("CISCO-FSPF-MIB", "fspfRowStatus"),
        ("CISCO-FSPF-MIB", "fspfTotalCheckSum"),
        ("CISCO-FSPF-MIB", "fspfNbrStateChangeNotifyEnable"))
)
if mibBuilder.loadTexts:
    fspfGenericGroupRev1.setStatus("current")

fspfDatabaseGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 7)
)
fspfDatabaseGroupRev1.setObjects(
      *(("CISCO-FSPF-MIB", "fspfLsrAdvDomainId"),
        ("CISCO-FSPF-MIB", "fspfLsrAge"),
        ("CISCO-FSPF-MIB", "fspfLsrIncarnationNumber"),
        ("CISCO-FSPF-MIB", "fspfLsrCheckSum"),
        ("CISCO-FSPF-MIB", "fspfLsrLinks"),
        ("CISCO-FSPF-MIB", "fspfLinkNbrDomainId"),
        ("CISCO-FSPF-MIB", "fspfLinkPortIndex"),
        ("CISCO-FSPF-MIB", "fspfLinkNbrPortIndex"),
        ("CISCO-FSPF-MIB", "fspfLinkType"),
        ("CISCO-FSPF-MIB", "fspfLinkCost"),
        ("CISCO-FSPF-MIB", "fspfLsrNumber"),
        ("CISCO-FSPF-MIB", "fspfLinkNumber"))
)
if mibBuilder.loadTexts:
    fspfDatabaseGroupRev1.setStatus("deprecated")

fspfDatabaseGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 8)
)
fspfDatabaseGroupRev2.setObjects(
      *(("CISCO-FSPF-MIB", "fspfLsrAdvDomainId"),
        ("CISCO-FSPF-MIB", "fspfLsrAge"),
        ("CISCO-FSPF-MIB", "fspfLsrIncarnationNumber"),
        ("CISCO-FSPF-MIB", "fspfLsrCheckSum"),
        ("CISCO-FSPF-MIB", "fspfLsrLinks"),
        ("CISCO-FSPF-MIB", "fspfLinkNbrDomainId"),
        ("CISCO-FSPF-MIB", "fspfLinkPortIndex"),
        ("CISCO-FSPF-MIB", "fspfLinkNbrPortIndex"),
        ("CISCO-FSPF-MIB", "fspfLinkType"),
        ("CISCO-FSPF-MIB", "fspfLinkCost"),
        ("CISCO-FSPF-MIB", "fspfLsrNumber"),
        ("CISCO-FSPF-MIB", "fspfLinkNumber"),
        ("CISCO-FSPF-MIB", "fspfLsrExternal"))
)
if mibBuilder.loadTexts:
    fspfDatabaseGroupRev2.setStatus("current")


# Notification objects

fspfNbrStateChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 3, 0, 1)
)
fspfNbrStateChangeNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-VSAN-MIB", "notifyVsanIndex"),
        ("CISCO-FSPF-MIB", "fspfDomainId"),
        ("CISCO-FSPF-MIB", "fspfIfNbrDomainId"),
        ("CISCO-FSPF-MIB", "fspfIfNbrState"),
        ("CISCO-FSPF-MIB", "fspfIfPrevNbrState"))
)
if mibBuilder.loadTexts:
    fspfNbrStateChangeNotify.setStatus(
        "current"
    )


# Notifications groups

fspfNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 2, 5)
)
fspfNotificationGroup.setObjects(
    ("CISCO-FSPF-MIB", "fspfNbrStateChangeNotify")
)
if mibBuilder.loadTexts:
    fspfNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fspfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fspfMIBCompliance.setStatus(
        "deprecated"
    )

fspfMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 1, 2)
)
if mibBuilder.loadTexts:
    fspfMIBCompliance1.setStatus(
        "deprecated"
    )

fspfMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 1, 3)
)
if mibBuilder.loadTexts:
    fspfMIBCompliance2.setStatus(
        "deprecated"
    )

fspfMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 287, 4, 1, 4)
)
if mibBuilder.loadTexts:
    fspfMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FSPF-MIB",
    **{"FspfRegionId": FspfRegionId,
       "FspfLsrType": FspfLsrType,
       "FspfLinkType": FspfLinkType,
       "FspfInterfaceState": FspfInterfaceState,
       "LastCreationTime": LastCreationTime,
       "ciscoFspfMIB": ciscoFspfMIB,
       "fspfConfiguration": fspfConfiguration,
       "fspfTable": fspfTable,
       "fspfEntry": fspfEntry,
       "fspfRegionId": fspfRegionId,
       "fspfDomainId": fspfDomainId,
       "fspfSpfDelay": fspfSpfDelay,
       "fspfSpfHoldTime": fspfSpfHoldTime,
       "fspfMinLsArrival": fspfMinLsArrival,
       "fspfMinLsInterval": fspfMinLsInterval,
       "fspfLsRefreshTime": fspfLsRefreshTime,
       "fspfMaxAge": fspfMaxAge,
       "fspfMaxAgeCount": fspfMaxAgeCount,
       "fspfSpfComputations": fspfSpfComputations,
       "fspfChecksumErrors": fspfChecksumErrors,
       "fspfLsuRxPkts": fspfLsuRxPkts,
       "fspfLsaRxPkts": fspfLsaRxPkts,
       "fspfLsuTxPkts": fspfLsuTxPkts,
       "fspfLsaTxPkts": fspfLsaTxPkts,
       "fspfHelloTxPkts": fspfHelloTxPkts,
       "fspfHelloRxPkts": fspfHelloRxPkts,
       "fspfRetransmittedLsuTxPkts": fspfRetransmittedLsuTxPkts,
       "fspfErrorRxPkts": fspfErrorRxPkts,
       "fspfLsrs": fspfLsrs,
       "fspfCreateTime": fspfCreateTime,
       "fspfAdminStatus": fspfAdminStatus,
       "fspfOperStatus": fspfOperStatus,
       "fspfSetToDefault": fspfSetToDefault,
       "fspfRowStatus": fspfRowStatus,
       "fspfTotalCheckSum": fspfTotalCheckSum,
       "fspfIfTable": fspfIfTable,
       "fspfIfEntry": fspfIfEntry,
       "fspfIfCost": fspfIfCost,
       "fspfIfHelloInterval": fspfIfHelloInterval,
       "fspfIfDeadInterval": fspfIfDeadInterval,
       "fspfIfRetransmitInterval": fspfIfRetransmitInterval,
       "fspfIfLsuRxPkts": fspfIfLsuRxPkts,
       "fspfIfLsaRxPkts": fspfIfLsaRxPkts,
       "fspfIfLsuTxPkts": fspfIfLsuTxPkts,
       "fspfIfLsaTxPkts": fspfIfLsaTxPkts,
       "fspfIfHelloTxPkts": fspfIfHelloTxPkts,
       "fspfIfHelloRxPkts": fspfIfHelloRxPkts,
       "fspfIfRetransmittedLsuTxPkts": fspfIfRetransmittedLsuTxPkts,
       "fspfIfErrorRxPkts": fspfIfErrorRxPkts,
       "fspfIfInactivityExpirations": fspfIfInactivityExpirations,
       "fspfIfNbrState": fspfIfNbrState,
       "fspfIfNbrDomainId": fspfIfNbrDomainId,
       "fspfIfNbrPortIndex": fspfIfNbrPortIndex,
       "fspfIfAdminStatus": fspfIfAdminStatus,
       "fspfIfCreateTime": fspfIfCreateTime,
       "fspfIfSetToDefault": fspfIfSetToDefault,
       "fspfIfRowStatus": fspfIfRowStatus,
       "fspfNbrStateChangeNotifyEnable": fspfNbrStateChangeNotifyEnable,
       "fspfIfPrevNbrState": fspfIfPrevNbrState,
       "fspfDatabase": fspfDatabase,
       "fspfLsrTable": fspfLsrTable,
       "fspfLsrEntry": fspfLsrEntry,
       "fspfLsrDomainId": fspfLsrDomainId,
       "fspfLsrType": fspfLsrType,
       "fspfLsrAdvDomainId": fspfLsrAdvDomainId,
       "fspfLsrAge": fspfLsrAge,
       "fspfLsrIncarnationNumber": fspfLsrIncarnationNumber,
       "fspfLsrCheckSum": fspfLsrCheckSum,
       "fspfLsrLinks": fspfLsrLinks,
       "fspfLsrExternal": fspfLsrExternal,
       "fspfLinkTable": fspfLinkTable,
       "fspfLinkEntry": fspfLinkEntry,
       "fspfLinkIndex": fspfLinkIndex,
       "fspfLinkNbrDomainId": fspfLinkNbrDomainId,
       "fspfLinkPortIndex": fspfLinkPortIndex,
       "fspfLinkNbrPortIndex": fspfLinkNbrPortIndex,
       "fspfLinkType": fspfLinkType,
       "fspfLinkCost": fspfLinkCost,
       "fspfLsrNumber": fspfLsrNumber,
       "fspfLinkNumber": fspfLinkNumber,
       "fspfNotificationPrefix": fspfNotificationPrefix,
       "fspfNotification": fspfNotification,
       "fspfNbrStateChangeNotify": fspfNbrStateChangeNotify,
       "fspfMIBConformance": fspfMIBConformance,
       "fspfMIBCompliances": fspfMIBCompliances,
       "fspfMIBCompliance": fspfMIBCompliance,
       "fspfMIBCompliance1": fspfMIBCompliance1,
       "fspfMIBCompliance2": fspfMIBCompliance2,
       "fspfMIBCompliance3": fspfMIBCompliance3,
       "fspfMIBGroups": fspfMIBGroups,
       "fspfGenericGroup": fspfGenericGroup,
       "fspfIfGroup": fspfIfGroup,
       "fspfDatabaseGroup": fspfDatabaseGroup,
       "fspfNotificationGroup": fspfNotificationGroup,
       "fspfGenericGroupRev1": fspfGenericGroupRev1,
       "fspfDatabaseGroupRev1": fspfDatabaseGroupRev1,
       "fspfDatabaseGroupRev2": fspfDatabaseGroupRev2}
)
