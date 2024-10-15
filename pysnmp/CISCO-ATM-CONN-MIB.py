# SNMP MIB module (CISCO-ATM-CONN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-CONN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:49 2024
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

(AtmTrafficDescrParamIndex,
 atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "AtmTrafficDescrParamIndex",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(NsapAtmAddr,) = mibBuilder.importSymbols(
    "CISCO-ATM-IF-MIB",
    "NsapAtmAddr")

(LsPerVcqThresholdGroup,) = mibBuilder.importSymbols(
    "CISCO-ATM-RM-MIB",
    "LsPerVcqThresholdGroup")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoAtmConnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 13)
)
ciscoAtmConnMIB.setRevisions(
        ("2002-07-12 00:00",
         "2001-10-30 00:00",
         "2001-10-10 00:00",
         "2001-08-06 00:00",
         "2001-01-29 00:00",
         "1998-10-02 00:00",
         "1997-05-26 00:00",
         "1996-11-01 00:00",
         "1998-07-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CastType(Integer32, TextualConvention):
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
        *(("pointToMultiPointLeaf", 3),
          ("pointToMultiPointRoot", 2),
          ("pointToPoint", 1))
    )



class ConfigType(Integer32, TextualConvention):
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
        *(("other", 1),
          ("permanent", 2),
          ("soft", 4),
          ("softPassive", 5),
          ("switch", 3))
    )



class SpanType(Integer32, TextualConvention):
    status = "current"
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
        *(("both", 4),
          ("terminate", 3),
          ("transit", 2),
          ("unknown", 1))
    )



class EnableStatus(Integer32, TextualConvention):
    status = "current"
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



class UpcStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("dropping", 3),
          ("localShaping", 4),
          ("passing", 1),
          ("tagging", 2))
    )



class ConnState(Integer32, TextualConvention):
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
        *(("down", 4),
          ("notInstalled", 3),
          ("release", 2),
          ("setup", 1),
          ("up", 5))
    )



class Location(Integer32, TextualConvention):
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
        *(("called", 3),
          ("calling", 2),
          ("unknown", 1))
    )



class Direction(Integer32, TextualConvention):
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
        *(("p2mpLeaf", 5),
          ("p2mpRoot", 4),
          ("p2pCalledSide", 3),
          ("p2pCallingSide", 2),
          ("unknown", 1))
    )



class SnoopDirType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 2),
          ("transmit", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmConnMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmConnMIBObjects = _CiscoAtmConnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1)
)
_CiscoAtmVpl_ObjectIdentity = ObjectIdentity
ciscoAtmVpl = _CiscoAtmVpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1)
)
_CiscoAtmVplTable_Object = MibTable
ciscoAtmVplTable = _CiscoAtmVplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmVplTable.setStatus("current")
_CiscoAtmVplEntry_Object = MibTableRow
ciscoAtmVplEntry = _CiscoAtmVplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1)
)
ciscoAtmVplEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    ciscoAtmVplEntry.setStatus("current")


class _CiscoAtmVplCastType_Type(CastType):
    """Custom type ciscoAtmVplCastType based on CastType"""


_CiscoAtmVplCastType_Object = MibTableColumn
ciscoAtmVplCastType = _CiscoAtmVplCastType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 1),
    _CiscoAtmVplCastType_Type()
)
ciscoAtmVplCastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplCastType.setStatus("current")


class _CiscoAtmVplSpanType_Type(SpanType):
    """Custom type ciscoAtmVplSpanType based on SpanType"""


_CiscoAtmVplSpanType_Object = MibTableColumn
ciscoAtmVplSpanType = _CiscoAtmVplSpanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 2),
    _CiscoAtmVplSpanType_Type()
)
ciscoAtmVplSpanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplSpanType.setStatus("current")


class _CiscoAtmVplConfigType_Type(ConfigType):
    """Custom type ciscoAtmVplConfigType based on ConfigType"""


_CiscoAtmVplConfigType_Object = MibTableColumn
ciscoAtmVplConfigType = _CiscoAtmVplConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 3),
    _CiscoAtmVplConfigType_Type()
)
ciscoAtmVplConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplConfigType.setStatus("current")


class _CiscoAtmVplRxUpcMode_Type(UpcStatus):
    """Custom type ciscoAtmVplRxUpcMode based on UpcStatus"""


_CiscoAtmVplRxUpcMode_Object = MibTableColumn
ciscoAtmVplRxUpcMode = _CiscoAtmVplRxUpcMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 4),
    _CiscoAtmVplRxUpcMode_Type()
)
ciscoAtmVplRxUpcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplRxUpcMode.setStatus("current")
_CiscoAtmVplConnState_Type = ConnState
_CiscoAtmVplConnState_Object = MibTableColumn
ciscoAtmVplConnState = _CiscoAtmVplConnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 5),
    _CiscoAtmVplConnState_Type()
)
ciscoAtmVplConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplConnState.setStatus("current")


class _CiscoAtmVplOamLoopbkTxInterval_Type(Integer32):
    """Custom type ciscoAtmVplOamLoopbkTxInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_CiscoAtmVplOamLoopbkTxInterval_Type.__name__ = "Integer32"
_CiscoAtmVplOamLoopbkTxInterval_Object = MibTableColumn
ciscoAtmVplOamLoopbkTxInterval = _CiscoAtmVplOamLoopbkTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 6),
    _CiscoAtmVplOamLoopbkTxInterval_Type()
)
ciscoAtmVplOamLoopbkTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplOamLoopbkTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciscoAtmVplOamLoopbkTxInterval.setUnits("seconds")


class _CiscoAtmVplOamSegmentLoopback_Type(EnableStatus):
    """Custom type ciscoAtmVplOamSegmentLoopback based on EnableStatus"""


_CiscoAtmVplOamSegmentLoopback_Object = MibTableColumn
ciscoAtmVplOamSegmentLoopback = _CiscoAtmVplOamSegmentLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 7),
    _CiscoAtmVplOamSegmentLoopback_Type()
)
ciscoAtmVplOamSegmentLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplOamSegmentLoopback.setStatus("current")


class _CiscoAtmVplOamEndLoopback_Type(EnableStatus):
    """Custom type ciscoAtmVplOamEndLoopback based on EnableStatus"""


_CiscoAtmVplOamEndLoopback_Object = MibTableColumn
ciscoAtmVplOamEndLoopback = _CiscoAtmVplOamEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 8),
    _CiscoAtmVplOamEndLoopback_Type()
)
ciscoAtmVplOamEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplOamEndLoopback.setStatus("current")


class _CiscoAtmVplOamAisEnable_Type(EnableStatus):
    """Custom type ciscoAtmVplOamAisEnable based on EnableStatus"""


_CiscoAtmVplOamAisEnable_Object = MibTableColumn
ciscoAtmVplOamAisEnable = _CiscoAtmVplOamAisEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 9),
    _CiscoAtmVplOamAisEnable_Type()
)
ciscoAtmVplOamAisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplOamAisEnable.setStatus("current")


class _CiscoAtmVplOamRdiEnable_Type(EnableStatus):
    """Custom type ciscoAtmVplOamRdiEnable based on EnableStatus"""


_CiscoAtmVplOamRdiEnable_Object = MibTableColumn
ciscoAtmVplOamRdiEnable = _CiscoAtmVplOamRdiEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 10),
    _CiscoAtmVplOamRdiEnable_Type()
)
ciscoAtmVplOamRdiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplOamRdiEnable.setStatus("current")
_CiscoAtmVplInstallTime_Type = TimeStamp
_CiscoAtmVplInstallTime_Object = MibTableColumn
ciscoAtmVplInstallTime = _CiscoAtmVplInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 11),
    _CiscoAtmVplInstallTime_Type()
)
ciscoAtmVplInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplInstallTime.setStatus("current")
_CiscoAtmVplInCells_Type = Counter32
_CiscoAtmVplInCells_Object = MibTableColumn
ciscoAtmVplInCells = _CiscoAtmVplInCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 12),
    _CiscoAtmVplInCells_Type()
)
ciscoAtmVplInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplInCells.setStatus("current")
_CiscoAtmVplOutCells_Type = Counter32
_CiscoAtmVplOutCells_Object = MibTableColumn
ciscoAtmVplOutCells = _CiscoAtmVplOutCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 13),
    _CiscoAtmVplOutCells_Type()
)
ciscoAtmVplOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplOutCells.setStatus("current")


class _CiscoAtmVplCrossIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ciscoAtmVplCrossIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CiscoAtmVplCrossIfIndex_Object = MibTableColumn
ciscoAtmVplCrossIfIndex = _CiscoAtmVplCrossIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 14),
    _CiscoAtmVplCrossIfIndex_Type()
)
ciscoAtmVplCrossIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplCrossIfIndex.setStatus("current")


class _CiscoAtmVplCrossVpi_Type(Integer32):
    """Custom type ciscoAtmVplCrossVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CiscoAtmVplCrossVpi_Type.__name__ = "Integer32"
_CiscoAtmVplCrossVpi_Object = MibTableColumn
ciscoAtmVplCrossVpi = _CiscoAtmVplCrossVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 15),
    _CiscoAtmVplCrossVpi_Type()
)
ciscoAtmVplCrossVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplCrossVpi.setStatus("current")


class _CiscoAtmVplNextLeafIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ciscoAtmVplNextLeafIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CiscoAtmVplNextLeafIfIndex_Object = MibTableColumn
ciscoAtmVplNextLeafIfIndex = _CiscoAtmVplNextLeafIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 16),
    _CiscoAtmVplNextLeafIfIndex_Type()
)
ciscoAtmVplNextLeafIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplNextLeafIfIndex.setStatus("current")


class _CiscoAtmVplNextLeafVpi_Type(Integer32):
    """Custom type ciscoAtmVplNextLeafVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CiscoAtmVplNextLeafVpi_Type.__name__ = "Integer32"
_CiscoAtmVplNextLeafVpi_Object = MibTableColumn
ciscoAtmVplNextLeafVpi = _CiscoAtmVplNextLeafVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 17),
    _CiscoAtmVplNextLeafVpi_Type()
)
ciscoAtmVplNextLeafVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplNextLeafVpi.setStatus("current")
_CiscoAtmVplRemoteAddr_Type = NsapAtmAddr
_CiscoAtmVplRemoteAddr_Object = MibTableColumn
ciscoAtmVplRemoteAddr = _CiscoAtmVplRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 18),
    _CiscoAtmVplRemoteAddr_Type()
)
ciscoAtmVplRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplRemoteAddr.setStatus("current")


class _CiscoAtmVplRemoteVpi_Type(Integer32):
    """Custom type ciscoAtmVplRemoteVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CiscoAtmVplRemoteVpi_Type.__name__ = "Integer32"
_CiscoAtmVplRemoteVpi_Object = MibTableColumn
ciscoAtmVplRemoteVpi = _CiscoAtmVplRemoteVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 19),
    _CiscoAtmVplRemoteVpi_Type()
)
ciscoAtmVplRemoteVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplRemoteVpi.setStatus("current")
_CiscoAtmVplLocation_Type = Location
_CiscoAtmVplLocation_Object = MibTableColumn
ciscoAtmVplLocation = _CiscoAtmVplLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 20),
    _CiscoAtmVplLocation_Type()
)
ciscoAtmVplLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplLocation.setStatus("current")


class _CiscoAtmVplSlowRetryIntv_Type(Integer32):
    """Custom type ciscoAtmVplSlowRetryIntv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoAtmVplSlowRetryIntv_Type.__name__ = "Integer32"
_CiscoAtmVplSlowRetryIntv_Object = MibTableColumn
ciscoAtmVplSlowRetryIntv = _CiscoAtmVplSlowRetryIntv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 21),
    _CiscoAtmVplSlowRetryIntv_Type()
)
ciscoAtmVplSlowRetryIntv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplSlowRetryIntv.setStatus("current")
_CiscoAtmVplNumAttempts_Type = Counter32
_CiscoAtmVplNumAttempts_Object = MibTableColumn
ciscoAtmVplNumAttempts = _CiscoAtmVplNumAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 22),
    _CiscoAtmVplNumAttempts_Type()
)
ciscoAtmVplNumAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplNumAttempts.setStatus("current")


class _CiscoAtmVplLastReleaseCause_Type(Integer32):
    """Custom type ciscoAtmVplLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CiscoAtmVplLastReleaseCause_Type.__name__ = "Integer32"
_CiscoAtmVplLastReleaseCause_Object = MibTableColumn
ciscoAtmVplLastReleaseCause = _CiscoAtmVplLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 23),
    _CiscoAtmVplLastReleaseCause_Type()
)
ciscoAtmVplLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplLastReleaseCause.setStatus("current")


class _CiscoAtmVplLogicalPortDef_Type(Integer32):
    """Custom type ciscoAtmVplLogicalPortDef based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isLogicalIf", 2),
          ("notLogicalIf", 1))
    )


_CiscoAtmVplLogicalPortDef_Type.__name__ = "Integer32"
_CiscoAtmVplLogicalPortDef_Object = MibTableColumn
ciscoAtmVplLogicalPortDef = _CiscoAtmVplLogicalPortDef_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 24),
    _CiscoAtmVplLogicalPortDef_Type()
)
ciscoAtmVplLogicalPortDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplLogicalPortDef.setStatus("current")
_CiscoAtmVplLogicalPortIndex_Type = InterfaceIndexOrZero
_CiscoAtmVplLogicalPortIndex_Object = MibTableColumn
ciscoAtmVplLogicalPortIndex = _CiscoAtmVplLogicalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 25),
    _CiscoAtmVplLogicalPortIndex_Type()
)
ciscoAtmVplLogicalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplLogicalPortIndex.setStatus("current")
_CiscoAtmVplUpcViolations_Type = Counter32
_CiscoAtmVplUpcViolations_Object = MibTableColumn
ciscoAtmVplUpcViolations = _CiscoAtmVplUpcViolations_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 26),
    _CiscoAtmVplUpcViolations_Type()
)
ciscoAtmVplUpcViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplUpcViolations.setStatus("current")
_CiscoAtmVplEpdTpdCellDrops_Type = Counter32
_CiscoAtmVplEpdTpdCellDrops_Object = MibTableColumn
ciscoAtmVplEpdTpdCellDrops = _CiscoAtmVplEpdTpdCellDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 27),
    _CiscoAtmVplEpdTpdCellDrops_Type()
)
ciscoAtmVplEpdTpdCellDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplEpdTpdCellDrops.setStatus("obsolete")
_CiscoAtmVplEpdTpdPacketDrops_Type = Counter32
_CiscoAtmVplEpdTpdPacketDrops_Object = MibTableColumn
ciscoAtmVplEpdTpdPacketDrops = _CiscoAtmVplEpdTpdPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 28),
    _CiscoAtmVplEpdTpdPacketDrops_Type()
)
ciscoAtmVplEpdTpdPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplEpdTpdPacketDrops.setStatus("obsolete")
_CiscoAtmVplEpdTpdPacketsIn_Type = Counter32
_CiscoAtmVplEpdTpdPacketsIn_Object = MibTableColumn
ciscoAtmVplEpdTpdPacketsIn = _CiscoAtmVplEpdTpdPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 29),
    _CiscoAtmVplEpdTpdPacketsIn_Type()
)
ciscoAtmVplEpdTpdPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplEpdTpdPacketsIn.setStatus("obsolete")
_CiscoAtmVplClp1Drops_Type = Counter32
_CiscoAtmVplClp1Drops_Object = MibTableColumn
ciscoAtmVplClp1Drops = _CiscoAtmVplClp1Drops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 30),
    _CiscoAtmVplClp1Drops_Type()
)
ciscoAtmVplClp1Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplClp1Drops.setStatus("obsolete")
_CiscoAtmVplDefaultRxUpcTolerance_Type = Integer32
_CiscoAtmVplDefaultRxUpcTolerance_Object = MibTableColumn
ciscoAtmVplDefaultRxUpcTolerance = _CiscoAtmVplDefaultRxUpcTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 31),
    _CiscoAtmVplDefaultRxUpcTolerance_Type()
)
ciscoAtmVplDefaultRxUpcTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplDefaultRxUpcTolerance.setStatus("current")
_CiscoAtmVplDefaultRxUpcVbrCdvt_Type = Integer32
_CiscoAtmVplDefaultRxUpcVbrCdvt_Object = MibTableColumn
ciscoAtmVplDefaultRxUpcVbrCdvt = _CiscoAtmVplDefaultRxUpcVbrCdvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 32),
    _CiscoAtmVplDefaultRxUpcVbrCdvt_Type()
)
ciscoAtmVplDefaultRxUpcVbrCdvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplDefaultRxUpcVbrCdvt.setStatus("current")


class _CiscoAtmVplLsPerVcqWrrWeight_Type(Integer32):
    """Custom type ciscoAtmVplLsPerVcqWrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CiscoAtmVplLsPerVcqWrrWeight_Type.__name__ = "Integer32"
_CiscoAtmVplLsPerVcqWrrWeight_Object = MibTableColumn
ciscoAtmVplLsPerVcqWrrWeight = _CiscoAtmVplLsPerVcqWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 33),
    _CiscoAtmVplLsPerVcqWrrWeight_Type()
)
ciscoAtmVplLsPerVcqWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplLsPerVcqWrrWeight.setStatus("current")
_CiscoAtmVplLsPerVcqTunnelIsShaped_Type = TruthValue
_CiscoAtmVplLsPerVcqTunnelIsShaped_Object = MibTableColumn
ciscoAtmVplLsPerVcqTunnelIsShaped = _CiscoAtmVplLsPerVcqTunnelIsShaped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 34),
    _CiscoAtmVplLsPerVcqTunnelIsShaped_Type()
)
ciscoAtmVplLsPerVcqTunnelIsShaped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplLsPerVcqTunnelIsShaped.setStatus("current")
_CiscoAtmVplLsPerVcqXmtQueuedCells_Type = Gauge32
_CiscoAtmVplLsPerVcqXmtQueuedCells_Object = MibTableColumn
ciscoAtmVplLsPerVcqXmtQueuedCells = _CiscoAtmVplLsPerVcqXmtQueuedCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 35),
    _CiscoAtmVplLsPerVcqXmtQueuedCells_Type()
)
ciscoAtmVplLsPerVcqXmtQueuedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplLsPerVcqXmtQueuedCells.setStatus("current")
_CiscoAtmVplLsPerVcQThreshGrp_Type = LsPerVcqThresholdGroup
_CiscoAtmVplLsPerVcQThreshGrp_Object = MibTableColumn
ciscoAtmVplLsPerVcQThreshGrp = _CiscoAtmVplLsPerVcQThreshGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 36),
    _CiscoAtmVplLsPerVcQThreshGrp_Type()
)
ciscoAtmVplLsPerVcQThreshGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplLsPerVcQThreshGrp.setStatus("current")
_CiscoAtmVplInClp0Cells_Type = Counter32
_CiscoAtmVplInClp0Cells_Object = MibTableColumn
ciscoAtmVplInClp0Cells = _CiscoAtmVplInClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 37),
    _CiscoAtmVplInClp0Cells_Type()
)
ciscoAtmVplInClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplInClp0Cells.setStatus("current")
_CiscoAtmVplInClp1Cells_Type = Counter32
_CiscoAtmVplInClp1Cells_Object = MibTableColumn
ciscoAtmVplInClp1Cells = _CiscoAtmVplInClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 38),
    _CiscoAtmVplInClp1Cells_Type()
)
ciscoAtmVplInClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplInClp1Cells.setStatus("current")
_CiscoAtmVplOutClp0Cells_Type = Counter32
_CiscoAtmVplOutClp0Cells_Object = MibTableColumn
ciscoAtmVplOutClp0Cells = _CiscoAtmVplOutClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 39),
    _CiscoAtmVplOutClp0Cells_Type()
)
ciscoAtmVplOutClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplOutClp0Cells.setStatus("current")
_CiscoAtmVplOutClp1Cells_Type = Counter32
_CiscoAtmVplOutClp1Cells_Object = MibTableColumn
ciscoAtmVplOutClp1Cells = _CiscoAtmVplOutClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 40),
    _CiscoAtmVplOutClp1Cells_Type()
)
ciscoAtmVplOutClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplOutClp1Cells.setStatus("current")
_CiscoAtmVplCellDrops_Type = Counter32
_CiscoAtmVplCellDrops_Object = MibTableColumn
ciscoAtmVplCellDrops = _CiscoAtmVplCellDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 41),
    _CiscoAtmVplCellDrops_Type()
)
ciscoAtmVplCellDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplCellDrops.setStatus("current")
_CiscoAtmVplClp0VcqFullCellDrops_Type = Counter32
_CiscoAtmVplClp0VcqFullCellDrops_Object = MibTableColumn
ciscoAtmVplClp0VcqFullCellDrops = _CiscoAtmVplClp0VcqFullCellDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 43),
    _CiscoAtmVplClp0VcqFullCellDrops_Type()
)
ciscoAtmVplClp0VcqFullCellDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplClp0VcqFullCellDrops.setStatus("current")
_CiscoAtmVplVcqClpThreshCellDrops_Type = Counter32
_CiscoAtmVplVcqClpThreshCellDrops_Object = MibTableColumn
ciscoAtmVplVcqClpThreshCellDrops = _CiscoAtmVplVcqClpThreshCellDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 44),
    _CiscoAtmVplVcqClpThreshCellDrops_Type()
)
ciscoAtmVplVcqClpThreshCellDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplVcqClpThreshCellDrops.setStatus("current")
_CiscoAtmVplLsPerVcqTunnelIsHierarchical_Type = TruthValue
_CiscoAtmVplLsPerVcqTunnelIsHierarchical_Object = MibTableColumn
ciscoAtmVplLsPerVcqTunnelIsHierarchical = _CiscoAtmVplLsPerVcqTunnelIsHierarchical_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 45),
    _CiscoAtmVplLsPerVcqTunnelIsHierarchical_Type()
)
ciscoAtmVplLsPerVcqTunnelIsHierarchical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplLsPerVcqTunnelIsHierarchical.setStatus("current")
_CiscoAtmVplRxNegTraffDescrIndex_Type = AtmTrafficDescrParamIndex
_CiscoAtmVplRxNegTraffDescrIndex_Object = MibTableColumn
ciscoAtmVplRxNegTraffDescrIndex = _CiscoAtmVplRxNegTraffDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 46),
    _CiscoAtmVplRxNegTraffDescrIndex_Type()
)
ciscoAtmVplRxNegTraffDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplRxNegTraffDescrIndex.setStatus("current")
_CiscoAtmVplTxNegTraffDescrIndex_Type = AtmTrafficDescrParamIndex
_CiscoAtmVplTxNegTraffDescrIndex_Object = MibTableColumn
ciscoAtmVplTxNegTraffDescrIndex = _CiscoAtmVplTxNegTraffDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 47),
    _CiscoAtmVplTxNegTraffDescrIndex_Type()
)
ciscoAtmVplTxNegTraffDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplTxNegTraffDescrIndex.setStatus("current")
_CiscoAtmVplSwFabOutCells_Type = Counter32
_CiscoAtmVplSwFabOutCells_Object = MibTableColumn
ciscoAtmVplSwFabOutCells = _CiscoAtmVplSwFabOutCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 48),
    _CiscoAtmVplSwFabOutCells_Type()
)
ciscoAtmVplSwFabOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplSwFabOutCells.setStatus("current")
_CiscoAtmVplSwFabOutClp0Cells_Type = Counter32
_CiscoAtmVplSwFabOutClp0Cells_Object = MibTableColumn
ciscoAtmVplSwFabOutClp0Cells = _CiscoAtmVplSwFabOutClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 49),
    _CiscoAtmVplSwFabOutClp0Cells_Type()
)
ciscoAtmVplSwFabOutClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplSwFabOutClp0Cells.setStatus("current")
_CiscoAtmVplSwFabOutClp1Cells_Type = Counter32
_CiscoAtmVplSwFabOutClp1Cells_Object = MibTableColumn
ciscoAtmVplSwFabOutClp1Cells = _CiscoAtmVplSwFabOutClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 50),
    _CiscoAtmVplSwFabOutClp1Cells_Type()
)
ciscoAtmVplSwFabOutClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVplSwFabOutClp1Cells.setStatus("current")
_CiscoAtmVplConnName_Type = SnmpAdminString
_CiscoAtmVplConnName_Object = MibTableColumn
ciscoAtmVplConnName = _CiscoAtmVplConnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 51),
    _CiscoAtmVplConnName_Type()
)
ciscoAtmVplConnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplConnName.setStatus("current")


class _CiscoAtmVplConnType_Type(Integer32):
    """Custom type ciscoAtmVplConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 2),
          ("local", 1))
    )


_CiscoAtmVplConnType_Type.__name__ = "Integer32"
_CiscoAtmVplConnType_Object = MibTableColumn
ciscoAtmVplConnType = _CiscoAtmVplConnType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 1, 1, 1, 52),
    _CiscoAtmVplConnType_Type()
)
ciscoAtmVplConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVplConnType.setStatus("current")
_CiscoAtmVcl_ObjectIdentity = ObjectIdentity
ciscoAtmVcl = _CiscoAtmVcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2)
)
_CiscoAtmVclTable_Object = MibTable
ciscoAtmVclTable = _CiscoAtmVclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmVclTable.setStatus("current")
_CiscoAtmVclEntry_Object = MibTableRow
ciscoAtmVclEntry = _CiscoAtmVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1)
)
ciscoAtmVclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    ciscoAtmVclEntry.setStatus("current")


class _CiscoAtmVclCastType_Type(CastType):
    """Custom type ciscoAtmVclCastType based on CastType"""


_CiscoAtmVclCastType_Object = MibTableColumn
ciscoAtmVclCastType = _CiscoAtmVclCastType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 1),
    _CiscoAtmVclCastType_Type()
)
ciscoAtmVclCastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclCastType.setStatus("current")


class _CiscoAtmVclSpanType_Type(SpanType):
    """Custom type ciscoAtmVclSpanType based on SpanType"""


_CiscoAtmVclSpanType_Object = MibTableColumn
ciscoAtmVclSpanType = _CiscoAtmVclSpanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 2),
    _CiscoAtmVclSpanType_Type()
)
ciscoAtmVclSpanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclSpanType.setStatus("current")


class _CiscoAtmVclConfigType_Type(ConfigType):
    """Custom type ciscoAtmVclConfigType based on ConfigType"""


_CiscoAtmVclConfigType_Object = MibTableColumn
ciscoAtmVclConfigType = _CiscoAtmVclConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 3),
    _CiscoAtmVclConfigType_Type()
)
ciscoAtmVclConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclConfigType.setStatus("current")


class _CiscoAtmVclRxUpcMode_Type(UpcStatus):
    """Custom type ciscoAtmVclRxUpcMode based on UpcStatus"""


_CiscoAtmVclRxUpcMode_Object = MibTableColumn
ciscoAtmVclRxUpcMode = _CiscoAtmVclRxUpcMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 4),
    _CiscoAtmVclRxUpcMode_Type()
)
ciscoAtmVclRxUpcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclRxUpcMode.setStatus("current")


class _CiscoAtmVclEpdEnable_Type(Integer32):
    """Custom type ciscoAtmVclEpdEnable based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("useTrafficDescr", 3))
    )


_CiscoAtmVclEpdEnable_Type.__name__ = "Integer32"
_CiscoAtmVclEpdEnable_Object = MibTableColumn
ciscoAtmVclEpdEnable = _CiscoAtmVclEpdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 5),
    _CiscoAtmVclEpdEnable_Type()
)
ciscoAtmVclEpdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclEpdEnable.setStatus("current")
_CiscoAtmVclConnState_Type = ConnState
_CiscoAtmVclConnState_Object = MibTableColumn
ciscoAtmVclConnState = _CiscoAtmVclConnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 6),
    _CiscoAtmVclConnState_Type()
)
ciscoAtmVclConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclConnState.setStatus("current")


class _CiscoAtmVclOamLoopbkTxInterval_Type(Integer32):
    """Custom type ciscoAtmVclOamLoopbkTxInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_CiscoAtmVclOamLoopbkTxInterval_Type.__name__ = "Integer32"
_CiscoAtmVclOamLoopbkTxInterval_Object = MibTableColumn
ciscoAtmVclOamLoopbkTxInterval = _CiscoAtmVclOamLoopbkTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 7),
    _CiscoAtmVclOamLoopbkTxInterval_Type()
)
ciscoAtmVclOamLoopbkTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclOamLoopbkTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciscoAtmVclOamLoopbkTxInterval.setUnits("seconds")


class _CiscoAtmVclOamSegmentLoopback_Type(EnableStatus):
    """Custom type ciscoAtmVclOamSegmentLoopback based on EnableStatus"""


_CiscoAtmVclOamSegmentLoopback_Object = MibTableColumn
ciscoAtmVclOamSegmentLoopback = _CiscoAtmVclOamSegmentLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 8),
    _CiscoAtmVclOamSegmentLoopback_Type()
)
ciscoAtmVclOamSegmentLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclOamSegmentLoopback.setStatus("current")


class _CiscoAtmVclOamEndLoopback_Type(EnableStatus):
    """Custom type ciscoAtmVclOamEndLoopback based on EnableStatus"""


_CiscoAtmVclOamEndLoopback_Object = MibTableColumn
ciscoAtmVclOamEndLoopback = _CiscoAtmVclOamEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 9),
    _CiscoAtmVclOamEndLoopback_Type()
)
ciscoAtmVclOamEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclOamEndLoopback.setStatus("current")


class _CiscoAtmVclOamAisEnable_Type(EnableStatus):
    """Custom type ciscoAtmVclOamAisEnable based on EnableStatus"""


_CiscoAtmVclOamAisEnable_Object = MibTableColumn
ciscoAtmVclOamAisEnable = _CiscoAtmVclOamAisEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 10),
    _CiscoAtmVclOamAisEnable_Type()
)
ciscoAtmVclOamAisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclOamAisEnable.setStatus("current")


class _CiscoAtmVclOamRdiEnable_Type(EnableStatus):
    """Custom type ciscoAtmVclOamRdiEnable based on EnableStatus"""


_CiscoAtmVclOamRdiEnable_Object = MibTableColumn
ciscoAtmVclOamRdiEnable = _CiscoAtmVclOamRdiEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 11),
    _CiscoAtmVclOamRdiEnable_Type()
)
ciscoAtmVclOamRdiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclOamRdiEnable.setStatus("current")
_CiscoAtmVclInstallTime_Type = TimeStamp
_CiscoAtmVclInstallTime_Object = MibTableColumn
ciscoAtmVclInstallTime = _CiscoAtmVclInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 12),
    _CiscoAtmVclInstallTime_Type()
)
ciscoAtmVclInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclInstallTime.setStatus("current")
_CiscoAtmVclInCells_Type = Counter32
_CiscoAtmVclInCells_Object = MibTableColumn
ciscoAtmVclInCells = _CiscoAtmVclInCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 13),
    _CiscoAtmVclInCells_Type()
)
ciscoAtmVclInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclInCells.setStatus("current")
_CiscoAtmVclOutCells_Type = Counter32
_CiscoAtmVclOutCells_Object = MibTableColumn
ciscoAtmVclOutCells = _CiscoAtmVclOutCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 14),
    _CiscoAtmVclOutCells_Type()
)
ciscoAtmVclOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclOutCells.setStatus("current")


class _CiscoAtmVclCrossIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ciscoAtmVclCrossIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CiscoAtmVclCrossIfIndex_Object = MibTableColumn
ciscoAtmVclCrossIfIndex = _CiscoAtmVclCrossIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 15),
    _CiscoAtmVclCrossIfIndex_Type()
)
ciscoAtmVclCrossIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclCrossIfIndex.setStatus("current")


class _CiscoAtmVclCrossVpi_Type(Integer32):
    """Custom type ciscoAtmVclCrossVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CiscoAtmVclCrossVpi_Type.__name__ = "Integer32"
_CiscoAtmVclCrossVpi_Object = MibTableColumn
ciscoAtmVclCrossVpi = _CiscoAtmVclCrossVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 16),
    _CiscoAtmVclCrossVpi_Type()
)
ciscoAtmVclCrossVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclCrossVpi.setStatus("current")


class _CiscoAtmVclCrossVci_Type(Integer32):
    """Custom type ciscoAtmVclCrossVci based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoAtmVclCrossVci_Type.__name__ = "Integer32"
_CiscoAtmVclCrossVci_Object = MibTableColumn
ciscoAtmVclCrossVci = _CiscoAtmVclCrossVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 17),
    _CiscoAtmVclCrossVci_Type()
)
ciscoAtmVclCrossVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclCrossVci.setStatus("current")


class _CiscoAtmVclNextLeafIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ciscoAtmVclNextLeafIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CiscoAtmVclNextLeafIfIndex_Object = MibTableColumn
ciscoAtmVclNextLeafIfIndex = _CiscoAtmVclNextLeafIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 18),
    _CiscoAtmVclNextLeafIfIndex_Type()
)
ciscoAtmVclNextLeafIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclNextLeafIfIndex.setStatus("current")


class _CiscoAtmVclNextLeafVpi_Type(Integer32):
    """Custom type ciscoAtmVclNextLeafVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CiscoAtmVclNextLeafVpi_Type.__name__ = "Integer32"
_CiscoAtmVclNextLeafVpi_Object = MibTableColumn
ciscoAtmVclNextLeafVpi = _CiscoAtmVclNextLeafVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 19),
    _CiscoAtmVclNextLeafVpi_Type()
)
ciscoAtmVclNextLeafVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclNextLeafVpi.setStatus("current")


class _CiscoAtmVclNextLeafVci_Type(Integer32):
    """Custom type ciscoAtmVclNextLeafVci based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoAtmVclNextLeafVci_Type.__name__ = "Integer32"
_CiscoAtmVclNextLeafVci_Object = MibTableColumn
ciscoAtmVclNextLeafVci = _CiscoAtmVclNextLeafVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 20),
    _CiscoAtmVclNextLeafVci_Type()
)
ciscoAtmVclNextLeafVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclNextLeafVci.setStatus("current")


class _CiscoAtmVclAalEncapFlag_Type(Integer32):
    """Custom type ciscoAtmVclAalEncapFlag based on Integer32"""
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
        *(("aal34Smds", 6),
          ("aal5FrNlpid", 4),
          ("aal5Ilmi", 8),
          ("aal5Lane", 9),
          ("aal5Mux", 5),
          ("aal5Nlpid", 3),
          ("aal5Pnni", 10),
          ("aal5Snap", 2),
          ("aalQsAal", 7),
          ("other", 1))
    )


_CiscoAtmVclAalEncapFlag_Type.__name__ = "Integer32"
_CiscoAtmVclAalEncapFlag_Object = MibTableColumn
ciscoAtmVclAalEncapFlag = _CiscoAtmVclAalEncapFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 21),
    _CiscoAtmVclAalEncapFlag_Type()
)
ciscoAtmVclAalEncapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclAalEncapFlag.setStatus("current")


class _CiscoAtmVclAalEncapProtocol_Type(Integer32):
    """Custom type ciscoAtmVclAalEncapProtocol based on Integer32"""
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
        *(("apollo", 8),
          ("appletalk", 4),
          ("clns", 5),
          ("decnet", 6),
          ("ip", 2),
          ("novell", 7),
          ("other", 1),
          ("vines", 9),
          ("xns", 3))
    )


_CiscoAtmVclAalEncapProtocol_Type.__name__ = "Integer32"
_CiscoAtmVclAalEncapProtocol_Object = MibTableColumn
ciscoAtmVclAalEncapProtocol = _CiscoAtmVclAalEncapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 22),
    _CiscoAtmVclAalEncapProtocol_Type()
)
ciscoAtmVclAalEncapProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclAalEncapProtocol.setStatus("current")


class _CiscoAtmVclAalUserVcType_Type(Integer32):
    """Custom type ciscoAtmVclAalUserVcType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("boxConfigure", 2),
          ("busForward", 3),
          ("busSend", 4),
          ("clientConfigure", 5),
          ("clientData", 6),
          ("clientDirect", 7),
          ("clientDistribute", 8),
          ("clientForward", 9),
          ("clientSend", 10),
          ("configure", 11),
          ("other", 1),
          ("serverConfigure", 12),
          ("serverDirect", 13),
          ("serverDistribute", 14))
    )


_CiscoAtmVclAalUserVcType_Type.__name__ = "Integer32"
_CiscoAtmVclAalUserVcType_Object = MibTableColumn
ciscoAtmVclAalUserVcType = _CiscoAtmVclAalUserVcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 23),
    _CiscoAtmVclAalUserVcType_Type()
)
ciscoAtmVclAalUserVcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclAalUserVcType.setStatus("current")


class _CiscoAtmVclAtmInArpInterval_Type(Integer32):
    """Custom type ciscoAtmVclAtmInArpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CiscoAtmVclAtmInArpInterval_Type.__name__ = "Integer32"
_CiscoAtmVclAtmInArpInterval_Object = MibTableColumn
ciscoAtmVclAtmInArpInterval = _CiscoAtmVclAtmInArpInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 24),
    _CiscoAtmVclAtmInArpInterval_Type()
)
ciscoAtmVclAtmInArpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclAtmInArpInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciscoAtmVclAtmInArpInterval.setUnits("minutes")
_CiscoAtmVclRemoteAddr_Type = NsapAtmAddr
_CiscoAtmVclRemoteAddr_Object = MibTableColumn
ciscoAtmVclRemoteAddr = _CiscoAtmVclRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 25),
    _CiscoAtmVclRemoteAddr_Type()
)
ciscoAtmVclRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclRemoteAddr.setStatus("current")


class _CiscoAtmVclRemoteVpi_Type(Integer32):
    """Custom type ciscoAtmVclRemoteVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CiscoAtmVclRemoteVpi_Type.__name__ = "Integer32"
_CiscoAtmVclRemoteVpi_Object = MibTableColumn
ciscoAtmVclRemoteVpi = _CiscoAtmVclRemoteVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 26),
    _CiscoAtmVclRemoteVpi_Type()
)
ciscoAtmVclRemoteVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclRemoteVpi.setStatus("current")


class _CiscoAtmVclRemoteVci_Type(Integer32):
    """Custom type ciscoAtmVclRemoteVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoAtmVclRemoteVci_Type.__name__ = "Integer32"
_CiscoAtmVclRemoteVci_Object = MibTableColumn
ciscoAtmVclRemoteVci = _CiscoAtmVclRemoteVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 27),
    _CiscoAtmVclRemoteVci_Type()
)
ciscoAtmVclRemoteVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclRemoteVci.setStatus("current")
_CiscoAtmVclLocation_Type = Location
_CiscoAtmVclLocation_Object = MibTableColumn
ciscoAtmVclLocation = _CiscoAtmVclLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 28),
    _CiscoAtmVclLocation_Type()
)
ciscoAtmVclLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclLocation.setStatus("current")


class _CiscoAtmVclSlowRetryIntv_Type(Integer32):
    """Custom type ciscoAtmVclSlowRetryIntv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoAtmVclSlowRetryIntv_Type.__name__ = "Integer32"
_CiscoAtmVclSlowRetryIntv_Object = MibTableColumn
ciscoAtmVclSlowRetryIntv = _CiscoAtmVclSlowRetryIntv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 29),
    _CiscoAtmVclSlowRetryIntv_Type()
)
ciscoAtmVclSlowRetryIntv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclSlowRetryIntv.setStatus("current")
if mibBuilder.loadTexts:
    ciscoAtmVclSlowRetryIntv.setUnits("seconds")
_CiscoAtmVclNumAttempts_Type = Counter32
_CiscoAtmVclNumAttempts_Object = MibTableColumn
ciscoAtmVclNumAttempts = _CiscoAtmVclNumAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 30),
    _CiscoAtmVclNumAttempts_Type()
)
ciscoAtmVclNumAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclNumAttempts.setStatus("current")


class _CiscoAtmVclLastReleaseCause_Type(Integer32):
    """Custom type ciscoAtmVclLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CiscoAtmVclLastReleaseCause_Type.__name__ = "Integer32"
_CiscoAtmVclLastReleaseCause_Object = MibTableColumn
ciscoAtmVclLastReleaseCause = _CiscoAtmVclLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 31),
    _CiscoAtmVclLastReleaseCause_Type()
)
ciscoAtmVclLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclLastReleaseCause.setStatus("current")
_CiscoAtmVclUpcViolations_Type = Counter32
_CiscoAtmVclUpcViolations_Object = MibTableColumn
ciscoAtmVclUpcViolations = _CiscoAtmVclUpcViolations_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 32),
    _CiscoAtmVclUpcViolations_Type()
)
ciscoAtmVclUpcViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclUpcViolations.setStatus("current")
_CiscoAtmVclEpdTpdCellDrops_Type = Counter32
_CiscoAtmVclEpdTpdCellDrops_Object = MibTableColumn
ciscoAtmVclEpdTpdCellDrops = _CiscoAtmVclEpdTpdCellDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 33),
    _CiscoAtmVclEpdTpdCellDrops_Type()
)
ciscoAtmVclEpdTpdCellDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclEpdTpdCellDrops.setStatus("obsolete")
_CiscoAtmVclEpdTpdPacketDrops_Type = Counter32
_CiscoAtmVclEpdTpdPacketDrops_Object = MibTableColumn
ciscoAtmVclEpdTpdPacketDrops = _CiscoAtmVclEpdTpdPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 34),
    _CiscoAtmVclEpdTpdPacketDrops_Type()
)
ciscoAtmVclEpdTpdPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclEpdTpdPacketDrops.setStatus("current")
_CiscoAtmVclEpdTpdPacketsIn_Type = Counter32
_CiscoAtmVclEpdTpdPacketsIn_Object = MibTableColumn
ciscoAtmVclEpdTpdPacketsIn = _CiscoAtmVclEpdTpdPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 35),
    _CiscoAtmVclEpdTpdPacketsIn_Type()
)
ciscoAtmVclEpdTpdPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclEpdTpdPacketsIn.setStatus("current")
_CiscoAtmVclClp1Drops_Type = Counter32
_CiscoAtmVclClp1Drops_Object = MibTableColumn
ciscoAtmVclClp1Drops = _CiscoAtmVclClp1Drops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 37),
    _CiscoAtmVclClp1Drops_Type()
)
ciscoAtmVclClp1Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclClp1Drops.setStatus("obsolete")
_CiscoAtmVclDefaultRxUpcTolerance_Type = Integer32
_CiscoAtmVclDefaultRxUpcTolerance_Object = MibTableColumn
ciscoAtmVclDefaultRxUpcTolerance = _CiscoAtmVclDefaultRxUpcTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 38),
    _CiscoAtmVclDefaultRxUpcTolerance_Type()
)
ciscoAtmVclDefaultRxUpcTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclDefaultRxUpcTolerance.setStatus("current")
_CiscoAtmVclDefaultRxUpcVbrCdvt_Type = Integer32
_CiscoAtmVclDefaultRxUpcVbrCdvt_Object = MibTableColumn
ciscoAtmVclDefaultRxUpcVbrCdvt = _CiscoAtmVclDefaultRxUpcVbrCdvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 39),
    _CiscoAtmVclDefaultRxUpcVbrCdvt_Type()
)
ciscoAtmVclDefaultRxUpcVbrCdvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclDefaultRxUpcVbrCdvt.setStatus("current")


class _CiscoAtmVclLsPerVcqWrrWeight_Type(Integer32):
    """Custom type ciscoAtmVclLsPerVcqWrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CiscoAtmVclLsPerVcqWrrWeight_Type.__name__ = "Integer32"
_CiscoAtmVclLsPerVcqWrrWeight_Object = MibTableColumn
ciscoAtmVclLsPerVcqWrrWeight = _CiscoAtmVclLsPerVcqWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 40),
    _CiscoAtmVclLsPerVcqWrrWeight_Type()
)
ciscoAtmVclLsPerVcqWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclLsPerVcqWrrWeight.setStatus("current")
_CiscoAtmVclLsPerVcqXmtQueuedCells_Type = Gauge32
_CiscoAtmVclLsPerVcqXmtQueuedCells_Object = MibTableColumn
ciscoAtmVclLsPerVcqXmtQueuedCells = _CiscoAtmVclLsPerVcqXmtQueuedCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 41),
    _CiscoAtmVclLsPerVcqXmtQueuedCells_Type()
)
ciscoAtmVclLsPerVcqXmtQueuedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclLsPerVcqXmtQueuedCells.setStatus("current")
_CiscoAtmVclLsPerVcQThreshGrp_Type = LsPerVcqThresholdGroup
_CiscoAtmVclLsPerVcQThreshGrp_Object = MibTableColumn
ciscoAtmVclLsPerVcQThreshGrp = _CiscoAtmVclLsPerVcQThreshGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 42),
    _CiscoAtmVclLsPerVcQThreshGrp_Type()
)
ciscoAtmVclLsPerVcQThreshGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclLsPerVcQThreshGrp.setStatus("current")
_CiscoAtmVclInClp0Cells_Type = Counter32
_CiscoAtmVclInClp0Cells_Object = MibTableColumn
ciscoAtmVclInClp0Cells = _CiscoAtmVclInClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 43),
    _CiscoAtmVclInClp0Cells_Type()
)
ciscoAtmVclInClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclInClp0Cells.setStatus("current")
_CiscoAtmVclInClp1Cells_Type = Counter32
_CiscoAtmVclInClp1Cells_Object = MibTableColumn
ciscoAtmVclInClp1Cells = _CiscoAtmVclInClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 44),
    _CiscoAtmVclInClp1Cells_Type()
)
ciscoAtmVclInClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclInClp1Cells.setStatus("current")
_CiscoAtmVclOutClp0Cells_Type = Counter32
_CiscoAtmVclOutClp0Cells_Object = MibTableColumn
ciscoAtmVclOutClp0Cells = _CiscoAtmVclOutClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 45),
    _CiscoAtmVclOutClp0Cells_Type()
)
ciscoAtmVclOutClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclOutClp0Cells.setStatus("current")
_CiscoAtmVclOutClp1Cells_Type = Counter32
_CiscoAtmVclOutClp1Cells_Object = MibTableColumn
ciscoAtmVclOutClp1Cells = _CiscoAtmVclOutClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 46),
    _CiscoAtmVclOutClp1Cells_Type()
)
ciscoAtmVclOutClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclOutClp1Cells.setStatus("current")
_CiscoAtmVclCellDrops_Type = Counter32
_CiscoAtmVclCellDrops_Object = MibTableColumn
ciscoAtmVclCellDrops = _CiscoAtmVclCellDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 47),
    _CiscoAtmVclCellDrops_Type()
)
ciscoAtmVclCellDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclCellDrops.setStatus("current")
_CiscoAtmVclClp0VcqFullCellDrops_Type = Counter32
_CiscoAtmVclClp0VcqFullCellDrops_Object = MibTableColumn
ciscoAtmVclClp0VcqFullCellDrops = _CiscoAtmVclClp0VcqFullCellDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 48),
    _CiscoAtmVclClp0VcqFullCellDrops_Type()
)
ciscoAtmVclClp0VcqFullCellDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclClp0VcqFullCellDrops.setStatus("current")
_CiscoAtmVclVcqClpThreshCellDrops_Type = Counter32
_CiscoAtmVclVcqClpThreshCellDrops_Object = MibTableColumn
ciscoAtmVclVcqClpThreshCellDrops = _CiscoAtmVclVcqClpThreshCellDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 49),
    _CiscoAtmVclVcqClpThreshCellDrops_Type()
)
ciscoAtmVclVcqClpThreshCellDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclVcqClpThreshCellDrops.setStatus("current")
_CiscoAtmVclRxNegTraffDescrIndex_Type = AtmTrafficDescrParamIndex
_CiscoAtmVclRxNegTraffDescrIndex_Object = MibTableColumn
ciscoAtmVclRxNegTraffDescrIndex = _CiscoAtmVclRxNegTraffDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 50),
    _CiscoAtmVclRxNegTraffDescrIndex_Type()
)
ciscoAtmVclRxNegTraffDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclRxNegTraffDescrIndex.setStatus("current")
_CiscoAtmVclTxNegTraffDescrIndex_Type = AtmTrafficDescrParamIndex
_CiscoAtmVclTxNegTraffDescrIndex_Object = MibTableColumn
ciscoAtmVclTxNegTraffDescrIndex = _CiscoAtmVclTxNegTraffDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 51),
    _CiscoAtmVclTxNegTraffDescrIndex_Type()
)
ciscoAtmVclTxNegTraffDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclTxNegTraffDescrIndex.setStatus("current")
_CiscoAtmVclSwFabOutCells_Type = Counter32
_CiscoAtmVclSwFabOutCells_Object = MibTableColumn
ciscoAtmVclSwFabOutCells = _CiscoAtmVclSwFabOutCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 52),
    _CiscoAtmVclSwFabOutCells_Type()
)
ciscoAtmVclSwFabOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclSwFabOutCells.setStatus("current")
_CiscoAtmVclSwFabOutClp0Cells_Type = Counter32
_CiscoAtmVclSwFabOutClp0Cells_Object = MibTableColumn
ciscoAtmVclSwFabOutClp0Cells = _CiscoAtmVclSwFabOutClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 53),
    _CiscoAtmVclSwFabOutClp0Cells_Type()
)
ciscoAtmVclSwFabOutClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclSwFabOutClp0Cells.setStatus("current")
_CiscoAtmVclSwFabOutClp1Cells_Type = Counter32
_CiscoAtmVclSwFabOutClp1Cells_Object = MibTableColumn
ciscoAtmVclSwFabOutClp1Cells = _CiscoAtmVclSwFabOutClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 54),
    _CiscoAtmVclSwFabOutClp1Cells_Type()
)
ciscoAtmVclSwFabOutClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmVclSwFabOutClp1Cells.setStatus("current")
_CiscoAtmVclConnName_Type = SnmpAdminString
_CiscoAtmVclConnName_Object = MibTableColumn
ciscoAtmVclConnName = _CiscoAtmVclConnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 55),
    _CiscoAtmVclConnName_Type()
)
ciscoAtmVclConnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclConnName.setStatus("current")


class _CiscoAtmVclConnType_Type(Integer32):
    """Custom type ciscoAtmVclConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 2),
          ("local", 1))
    )


_CiscoAtmVclConnType_Type.__name__ = "Integer32"
_CiscoAtmVclConnType_Object = MibTableColumn
ciscoAtmVclConnType = _CiscoAtmVclConnType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 2, 1, 1, 56),
    _CiscoAtmVclConnType_Type()
)
ciscoAtmVclConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmVclConnType.setStatus("current")
_CiscoAtmSvp_ObjectIdentity = ObjectIdentity
ciscoAtmSvp = _CiscoAtmSvp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 3)
)
_CiscoAtmSvpAddrTable_Object = MibTable
ciscoAtmSvpAddrTable = _CiscoAtmSvpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmSvpAddrTable.setStatus("current")
_CiscoAtmSvpAddrEntry_Object = MibTableRow
ciscoAtmSvpAddrEntry = _CiscoAtmSvpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 3, 1, 1)
)
ciscoAtmSvpAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-CONN-MIB", "ciscoAtmSvpAddr"),
    (0, "CISCO-ATM-CONN-MIB", "ciscoAtmSvpVpi"),
)
if mibBuilder.loadTexts:
    ciscoAtmSvpAddrEntry.setStatus("current")


class _CiscoAtmSvpAddr_Type(OctetString):
    """Custom type ciscoAtmSvpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_CiscoAtmSvpAddr_Type.__name__ = "OctetString"
_CiscoAtmSvpAddr_Object = MibTableColumn
ciscoAtmSvpAddr = _CiscoAtmSvpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 3, 1, 1, 1),
    _CiscoAtmSvpAddr_Type()
)
ciscoAtmSvpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoAtmSvpAddr.setStatus("current")


class _CiscoAtmSvpVpi_Type(Integer32):
    """Custom type ciscoAtmSvpVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CiscoAtmSvpVpi_Type.__name__ = "Integer32"
_CiscoAtmSvpVpi_Object = MibTableColumn
ciscoAtmSvpVpi = _CiscoAtmSvpVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 3, 1, 1, 2),
    _CiscoAtmSvpVpi_Type()
)
ciscoAtmSvpVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoAtmSvpVpi.setStatus("current")
_CiscoAtmSvpDirection_Type = Direction
_CiscoAtmSvpDirection_Object = MibTableColumn
ciscoAtmSvpDirection = _CiscoAtmSvpDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 3, 1, 1, 3),
    _CiscoAtmSvpDirection_Type()
)
ciscoAtmSvpDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmSvpDirection.setStatus("current")
_CiscoAtmSvc_ObjectIdentity = ObjectIdentity
ciscoAtmSvc = _CiscoAtmSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 4)
)
_CiscoAtmSvcAddrTable_Object = MibTable
ciscoAtmSvcAddrTable = _CiscoAtmSvcAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmSvcAddrTable.setStatus("current")
_CiscoAtmSvcAddrEntry_Object = MibTableRow
ciscoAtmSvcAddrEntry = _CiscoAtmSvcAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 4, 1, 1)
)
ciscoAtmSvcAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-CONN-MIB", "ciscoAtmSvcAddr"),
    (0, "CISCO-ATM-CONN-MIB", "ciscoAtmSvcVpi"),
    (0, "CISCO-ATM-CONN-MIB", "ciscoAtmSvcVci"),
)
if mibBuilder.loadTexts:
    ciscoAtmSvcAddrEntry.setStatus("current")


class _CiscoAtmSvcAddr_Type(OctetString):
    """Custom type ciscoAtmSvcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_CiscoAtmSvcAddr_Type.__name__ = "OctetString"
_CiscoAtmSvcAddr_Object = MibTableColumn
ciscoAtmSvcAddr = _CiscoAtmSvcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 4, 1, 1, 1),
    _CiscoAtmSvcAddr_Type()
)
ciscoAtmSvcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoAtmSvcAddr.setStatus("current")


class _CiscoAtmSvcVpi_Type(Integer32):
    """Custom type ciscoAtmSvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CiscoAtmSvcVpi_Type.__name__ = "Integer32"
_CiscoAtmSvcVpi_Object = MibTableColumn
ciscoAtmSvcVpi = _CiscoAtmSvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 4, 1, 1, 2),
    _CiscoAtmSvcVpi_Type()
)
ciscoAtmSvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoAtmSvcVpi.setStatus("current")


class _CiscoAtmSvcVci_Type(Integer32):
    """Custom type ciscoAtmSvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoAtmSvcVci_Type.__name__ = "Integer32"
_CiscoAtmSvcVci_Object = MibTableColumn
ciscoAtmSvcVci = _CiscoAtmSvcVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 4, 1, 1, 3),
    _CiscoAtmSvcVci_Type()
)
ciscoAtmSvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoAtmSvcVci.setStatus("current")
_CiscoAtmSvcDirection_Type = Direction
_CiscoAtmSvcDirection_Object = MibTableColumn
ciscoAtmSvcDirection = _CiscoAtmSvcDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 4, 1, 1, 4),
    _CiscoAtmSvcDirection_Type()
)
ciscoAtmSvcDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmSvcDirection.setStatus("current")


class _CiscoAtmSvcFrameDiscardUsesAal5Ie_Type(TruthValue):
    """Custom type ciscoAtmSvcFrameDiscardUsesAal5Ie based on TruthValue"""


_CiscoAtmSvcFrameDiscardUsesAal5Ie_Object = MibScalar
ciscoAtmSvcFrameDiscardUsesAal5Ie = _CiscoAtmSvcFrameDiscardUsesAal5Ie_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 4, 2),
    _CiscoAtmSvcFrameDiscardUsesAal5Ie_Type()
)
ciscoAtmSvcFrameDiscardUsesAal5Ie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmSvcFrameDiscardUsesAal5Ie.setStatus("current")
_CiscoAtmSnoopVc_ObjectIdentity = ObjectIdentity
ciscoAtmSnoopVc = _CiscoAtmSnoopVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 5)
)
_CiscoAtmSnoopVcTable_Object = MibTable
ciscoAtmSnoopVcTable = _CiscoAtmSnoopVcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmSnoopVcTable.setStatus("current")
_CiscoAtmSnoopVcEntry_Object = MibTableRow
ciscoAtmSnoopVcEntry = _CiscoAtmSnoopVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 5, 1, 1)
)
ciscoAtmSnoopVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    ciscoAtmSnoopVcEntry.setStatus("current")


class _CiscoAtmSnoopVcSnoopedIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ciscoAtmSnoopVcSnoopedIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CiscoAtmSnoopVcSnoopedIfIndex_Object = MibTableColumn
ciscoAtmSnoopVcSnoopedIfIndex = _CiscoAtmSnoopVcSnoopedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 5, 1, 1, 1),
    _CiscoAtmSnoopVcSnoopedIfIndex_Type()
)
ciscoAtmSnoopVcSnoopedIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoAtmSnoopVcSnoopedIfIndex.setStatus("current")


class _CiscoAtmSnoopVcSnoopedVpi_Type(Integer32):
    """Custom type ciscoAtmSnoopVcSnoopedVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CiscoAtmSnoopVcSnoopedVpi_Type.__name__ = "Integer32"
_CiscoAtmSnoopVcSnoopedVpi_Object = MibTableColumn
ciscoAtmSnoopVcSnoopedVpi = _CiscoAtmSnoopVcSnoopedVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 5, 1, 1, 2),
    _CiscoAtmSnoopVcSnoopedVpi_Type()
)
ciscoAtmSnoopVcSnoopedVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoAtmSnoopVcSnoopedVpi.setStatus("current")


class _CiscoAtmSnoopVcSnoopedVci_Type(Integer32):
    """Custom type ciscoAtmSnoopVcSnoopedVci based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoAtmSnoopVcSnoopedVci_Type.__name__ = "Integer32"
_CiscoAtmSnoopVcSnoopedVci_Object = MibTableColumn
ciscoAtmSnoopVcSnoopedVci = _CiscoAtmSnoopVcSnoopedVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 5, 1, 1, 3),
    _CiscoAtmSnoopVcSnoopedVci_Type()
)
ciscoAtmSnoopVcSnoopedVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoAtmSnoopVcSnoopedVci.setStatus("current")


class _CiscoAtmSnoopVcDir_Type(SnoopDirType):
    """Custom type ciscoAtmSnoopVcDir based on SnoopDirType"""


_CiscoAtmSnoopVcDir_Object = MibTableColumn
ciscoAtmSnoopVcDir = _CiscoAtmSnoopVcDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 5, 1, 1, 4),
    _CiscoAtmSnoopVcDir_Type()
)
ciscoAtmSnoopVcDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoAtmSnoopVcDir.setStatus("current")
_CiscoAtmSnoopVcState_Type = ConnState
_CiscoAtmSnoopVcState_Object = MibTableColumn
ciscoAtmSnoopVcState = _CiscoAtmSnoopVcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 5, 1, 1, 5),
    _CiscoAtmSnoopVcState_Type()
)
ciscoAtmSnoopVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmSnoopVcState.setStatus("current")


class _CiscoAtmSnoopVcRowStatus_Type(RowStatus):
    """Custom type ciscoAtmSnoopVcRowStatus based on RowStatus"""


_CiscoAtmSnoopVcRowStatus_Object = MibTableColumn
ciscoAtmSnoopVcRowStatus = _CiscoAtmSnoopVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 5, 1, 1, 6),
    _CiscoAtmSnoopVcRowStatus_Type()
)
ciscoAtmSnoopVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoAtmSnoopVcRowStatus.setStatus("current")
_CiscoAtmSnoopVp_ObjectIdentity = ObjectIdentity
ciscoAtmSnoopVp = _CiscoAtmSnoopVp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 6)
)
_CiscoAtmSnoopVpTable_Object = MibTable
ciscoAtmSnoopVpTable = _CiscoAtmSnoopVpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmSnoopVpTable.setStatus("current")
_CiscoAtmSnoopVpEntry_Object = MibTableRow
ciscoAtmSnoopVpEntry = _CiscoAtmSnoopVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 6, 1, 1)
)
ciscoAtmSnoopVpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    ciscoAtmSnoopVpEntry.setStatus("current")


class _CiscoAtmSnoopVpSnoopedIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ciscoAtmSnoopVpSnoopedIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CiscoAtmSnoopVpSnoopedIfIndex_Object = MibTableColumn
ciscoAtmSnoopVpSnoopedIfIndex = _CiscoAtmSnoopVpSnoopedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 6, 1, 1, 1),
    _CiscoAtmSnoopVpSnoopedIfIndex_Type()
)
ciscoAtmSnoopVpSnoopedIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoAtmSnoopVpSnoopedIfIndex.setStatus("current")


class _CiscoAtmSnoopVpSnoopedVpi_Type(Integer32):
    """Custom type ciscoAtmSnoopVpSnoopedVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CiscoAtmSnoopVpSnoopedVpi_Type.__name__ = "Integer32"
_CiscoAtmSnoopVpSnoopedVpi_Object = MibTableColumn
ciscoAtmSnoopVpSnoopedVpi = _CiscoAtmSnoopVpSnoopedVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 6, 1, 1, 2),
    _CiscoAtmSnoopVpSnoopedVpi_Type()
)
ciscoAtmSnoopVpSnoopedVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoAtmSnoopVpSnoopedVpi.setStatus("current")


class _CiscoAtmSnoopVpDir_Type(SnoopDirType):
    """Custom type ciscoAtmSnoopVpDir based on SnoopDirType"""


_CiscoAtmSnoopVpDir_Object = MibTableColumn
ciscoAtmSnoopVpDir = _CiscoAtmSnoopVpDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 6, 1, 1, 3),
    _CiscoAtmSnoopVpDir_Type()
)
ciscoAtmSnoopVpDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoAtmSnoopVpDir.setStatus("current")
_CiscoAtmSnoopVpState_Type = ConnState
_CiscoAtmSnoopVpState_Object = MibTableColumn
ciscoAtmSnoopVpState = _CiscoAtmSnoopVpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 6, 1, 1, 4),
    _CiscoAtmSnoopVpState_Type()
)
ciscoAtmSnoopVpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmSnoopVpState.setStatus("current")


class _CiscoAtmSnoopVpRowStatus_Type(RowStatus):
    """Custom type ciscoAtmSnoopVpRowStatus based on RowStatus"""


_CiscoAtmSnoopVpRowStatus_Object = MibTableColumn
ciscoAtmSnoopVpRowStatus = _CiscoAtmSnoopVpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 1, 6, 1, 1, 5),
    _CiscoAtmSnoopVpRowStatus_Type()
)
ciscoAtmSnoopVpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoAtmSnoopVpRowStatus.setStatus("current")
_CiscoAtmConnMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmConnMIBConformance = _CiscoAtmConnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3)
)
_CiscoAtmConnMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmConnMIBCompliances = _CiscoAtmConnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 1)
)
_CiscoAtmConnMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmConnMIBGroups = _CiscoAtmConnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 2)
)

# Managed Objects groups

ciscoAtmConnMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 2, 1)
)
ciscoAtmConnMIBGroup.setObjects(
      *(("CISCO-ATM-CONN-MIB", "ciscoAtmVplCastType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplSpanType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplConfigType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplRxUpcMode"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplConnState"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamLoopbkTxInterval"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamSegmentLoopback"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamEndLoopback"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamAisEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamRdiEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplInstallTime"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplInCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOutCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplCrossIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplCrossVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplNextLeafIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplNextLeafVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplRemoteAddr"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplRemoteVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLocation"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplSlowRetryIntv"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplNumAttempts"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLastReleaseCause"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLogicalPortDef"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLogicalPortIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCastType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclSpanType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclConfigType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRxUpcMode"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclEpdEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclConnState"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamLoopbkTxInterval"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamSegmentLoopback"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamEndLoopback"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamAisEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamRdiEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclInstallTime"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclInCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOutCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCrossIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCrossVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCrossVci"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclNextLeafIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclNextLeafVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclNextLeafVci"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclAalEncapFlag"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclAalEncapProtocol"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclAalUserVcType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclAtmInArpInterval"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRemoteAddr"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRemoteVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRemoteVci"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclLocation"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclSlowRetryIntv"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclNumAttempts"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclLastReleaseCause"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSvpDirection"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSvcDirection"))
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBGroup.setStatus("deprecated")

ciscoAtmConnMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 2, 2)
)
ciscoAtmConnMIBGroup2.setObjects(
      *(("CISCO-ATM-CONN-MIB", "ciscoAtmVplUpcViolations"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplEpdTpdCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplEpdTpdPacketDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplEpdTpdPacketsIn"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplClp1Drops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplDefaultRxUpcTolerance"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclUpcViolations"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclEpdTpdCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclEpdTpdPacketDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclEpdTpdPacketsIn"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclClp1Drops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclDefaultRxUpcTolerance"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSvcFrameDiscardUsesAal5Ie"))
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBGroup2.setStatus("obsolete")

ciscoAtmConnMIBGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 2, 3)
)
ciscoAtmConnMIBGroup3.setObjects(
      *(("CISCO-ATM-CONN-MIB", "ciscoAtmVplDefaultRxUpcTolerance"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclDefaultRxUpcTolerance"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplDefaultRxUpcVbrCdvt"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclDefaultRxUpcVbrCdvt"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSvcFrameDiscardUsesAal5Ie"))
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBGroup3.setStatus("current")

ciscoAtmConnMIBlsPerVcqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 2, 4)
)
ciscoAtmConnMIBlsPerVcqGroup.setObjects(
      *(("CISCO-ATM-CONN-MIB", "ciscoAtmVplLsPerVcqWrrWeight"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLsPerVcqTunnelIsShaped"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLsPerVcqXmtQueuedCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLsPerVcQThreshGrp"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclLsPerVcqWrrWeight"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclLsPerVcqXmtQueuedCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclLsPerVcQThreshGrp"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVcSnoopedIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVcSnoopedVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVcSnoopedVci"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVcDir"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVcState"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVcRowStatus"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVpSnoopedIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVpSnoopedVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVpDir"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVpState"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVpRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBlsPerVcqGroup.setStatus("obsolete")

ciscoAtmConnMIBlsFcPfqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 2, 5)
)
ciscoAtmConnMIBlsFcPfqGroup.setObjects(
      *(("CISCO-ATM-CONN-MIB", "ciscoAtmVplUpcViolations"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclUpcViolations"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclEpdTpdPacketDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclEpdTpdPacketsIn"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplInClp0Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplInClp1Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOutClp0Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOutClp1Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplClp0VcqFullCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplVcqClpThreshCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclInClp0Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclInClp1Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOutClp0Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOutClp1Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclClp0VcqFullCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclVcqClpThreshCellDrops"))
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBlsFcPfqGroup.setStatus("deprecated")

ciscoAtmConnMIBlsPerVcqGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 2, 6)
)
ciscoAtmConnMIBlsPerVcqGroup2.setObjects(
      *(("CISCO-ATM-CONN-MIB", "ciscoAtmVplLsPerVcqWrrWeight"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLsPerVcqTunnelIsShaped"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLsPerVcqTunnelIsHierarchical"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLsPerVcqXmtQueuedCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLsPerVcQThreshGrp"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclLsPerVcqWrrWeight"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclLsPerVcqXmtQueuedCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclLsPerVcQThreshGrp"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVcSnoopedIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVcSnoopedVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVcSnoopedVci"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVcDir"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVcState"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVcRowStatus"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVpSnoopedIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVpSnoopedVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVpDir"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVpState"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSnoopVpRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBlsPerVcqGroup2.setStatus("current")

ciscoAtmConnMIBNegTraffGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 2, 7)
)
ciscoAtmConnMIBNegTraffGroup.setObjects(
      *(("CISCO-ATM-CONN-MIB", "ciscoAtmVplRxNegTraffDescrIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplTxNegTraffDescrIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRxNegTraffDescrIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclTxNegTraffDescrIndex"))
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBNegTraffGroup.setStatus("current")

ciscoAtmConnMIBlsFcPfqGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 2, 8)
)
ciscoAtmConnMIBlsFcPfqGroup1.setObjects(
      *(("CISCO-ATM-CONN-MIB", "ciscoAtmVplUpcViolations"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclUpcViolations"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclEpdTpdPacketDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclEpdTpdPacketsIn"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplInClp0Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplInClp1Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOutClp0Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOutClp1Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplClp0VcqFullCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplVcqClpThreshCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplSwFabOutCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplSwFabOutClp0Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplSwFabOutClp1Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclInClp0Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclInClp1Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOutClp0Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOutClp1Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclClp0VcqFullCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclVcqClpThreshCellDrops"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclSwFabOutCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclSwFabOutClp0Cells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclSwFabOutClp1Cells"))
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBlsFcPfqGroup1.setStatus("current")

ciscoAtmConnMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 2, 9)
)
ciscoAtmConnMIBGroup1.setObjects(
      *(("CISCO-ATM-CONN-MIB", "ciscoAtmVplCastType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplSpanType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplConfigType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplRxUpcMode"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplConnState"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamLoopbkTxInterval"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamSegmentLoopback"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamEndLoopback"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamAisEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamRdiEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplInstallTime"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplInCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOutCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplCrossIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplCrossVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplNextLeafIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplNextLeafVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplRemoteAddr"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplRemoteVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLocation"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplSlowRetryIntv"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplNumAttempts"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLastReleaseCause"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLogicalPortDef"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLogicalPortIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplConnName"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCastType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclSpanType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclConfigType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRxUpcMode"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclEpdEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclConnState"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamLoopbkTxInterval"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamSegmentLoopback"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamEndLoopback"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamAisEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamRdiEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclInstallTime"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclInCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOutCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCrossIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCrossVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCrossVci"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclNextLeafIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclNextLeafVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclNextLeafVci"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclAalEncapFlag"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclAalEncapProtocol"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclAalUserVcType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclAtmInArpInterval"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRemoteAddr"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRemoteVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRemoteVci"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclLocation"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclSlowRetryIntv"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclNumAttempts"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclLastReleaseCause"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclConnName"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSvpDirection"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSvcDirection"))
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBGroup1.setStatus("deprecated")

ciscoAtmConnMIBGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 2, 10)
)
ciscoAtmConnMIBGroup4.setObjects(
      *(("CISCO-ATM-CONN-MIB", "ciscoAtmVplCastType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplSpanType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplConfigType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplRxUpcMode"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplConnState"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamLoopbkTxInterval"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamSegmentLoopback"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamEndLoopback"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamAisEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOamRdiEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplInstallTime"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplInCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplOutCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplCrossIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplCrossVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplNextLeafIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplNextLeafVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplRemoteAddr"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplRemoteVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLocation"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplSlowRetryIntv"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplNumAttempts"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLastReleaseCause"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLogicalPortDef"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplLogicalPortIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCastType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclSpanType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclConfigType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRxUpcMode"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclEpdEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclConnState"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamLoopbkTxInterval"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamSegmentLoopback"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamEndLoopback"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamAisEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOamRdiEnable"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclInstallTime"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclInCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclOutCells"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCrossIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCrossVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclCrossVci"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclNextLeafIfIndex"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclNextLeafVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclNextLeafVci"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclAalEncapFlag"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclAalEncapProtocol"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclAalUserVcType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclAtmInArpInterval"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRemoteAddr"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRemoteVpi"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclRemoteVci"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclLocation"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclSlowRetryIntv"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclNumAttempts"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclLastReleaseCause"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSvpDirection"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmSvcDirection"))
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBGroup4.setStatus("current")

ciscoAtmConnNmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 2, 11)
)
ciscoAtmConnNmsGroup.setObjects(
      *(("CISCO-ATM-CONN-MIB", "ciscoAtmVplConnName"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVplConnType"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclConnName"),
        ("CISCO-ATM-CONN-MIB", "ciscoAtmVclConnType"))
)
if mibBuilder.loadTexts:
    ciscoAtmConnNmsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmConnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBCompliance.setStatus(
        "obsolete"
    )

ciscoAtmConnMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBCompliance2.setStatus(
        "obsolete"
    )

ciscoAtmConnMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBCompliance3.setStatus(
        "obsolete"
    )

ciscoAtmConnMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBCompliance4.setStatus(
        "obsolete"
    )

ciscoAtmConnMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBCompliance5.setStatus(
        "deprecated"
    )

ciscoAtmConnMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBCompliance6.setStatus(
        "deprecated"
    )

ciscoAtmConnMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBCompliance7.setStatus(
        "deprecated"
    )

ciscoAtmConnMIBCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 13, 3, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoAtmConnMIBCompliance8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-CONN-MIB",
    **{"CastType": CastType,
       "ConfigType": ConfigType,
       "SpanType": SpanType,
       "EnableStatus": EnableStatus,
       "UpcStatus": UpcStatus,
       "ConnState": ConnState,
       "Location": Location,
       "Direction": Direction,
       "SnoopDirType": SnoopDirType,
       "ciscoAtmConnMIB": ciscoAtmConnMIB,
       "ciscoAtmConnMIBObjects": ciscoAtmConnMIBObjects,
       "ciscoAtmVpl": ciscoAtmVpl,
       "ciscoAtmVplTable": ciscoAtmVplTable,
       "ciscoAtmVplEntry": ciscoAtmVplEntry,
       "ciscoAtmVplCastType": ciscoAtmVplCastType,
       "ciscoAtmVplSpanType": ciscoAtmVplSpanType,
       "ciscoAtmVplConfigType": ciscoAtmVplConfigType,
       "ciscoAtmVplRxUpcMode": ciscoAtmVplRxUpcMode,
       "ciscoAtmVplConnState": ciscoAtmVplConnState,
       "ciscoAtmVplOamLoopbkTxInterval": ciscoAtmVplOamLoopbkTxInterval,
       "ciscoAtmVplOamSegmentLoopback": ciscoAtmVplOamSegmentLoopback,
       "ciscoAtmVplOamEndLoopback": ciscoAtmVplOamEndLoopback,
       "ciscoAtmVplOamAisEnable": ciscoAtmVplOamAisEnable,
       "ciscoAtmVplOamRdiEnable": ciscoAtmVplOamRdiEnable,
       "ciscoAtmVplInstallTime": ciscoAtmVplInstallTime,
       "ciscoAtmVplInCells": ciscoAtmVplInCells,
       "ciscoAtmVplOutCells": ciscoAtmVplOutCells,
       "ciscoAtmVplCrossIfIndex": ciscoAtmVplCrossIfIndex,
       "ciscoAtmVplCrossVpi": ciscoAtmVplCrossVpi,
       "ciscoAtmVplNextLeafIfIndex": ciscoAtmVplNextLeafIfIndex,
       "ciscoAtmVplNextLeafVpi": ciscoAtmVplNextLeafVpi,
       "ciscoAtmVplRemoteAddr": ciscoAtmVplRemoteAddr,
       "ciscoAtmVplRemoteVpi": ciscoAtmVplRemoteVpi,
       "ciscoAtmVplLocation": ciscoAtmVplLocation,
       "ciscoAtmVplSlowRetryIntv": ciscoAtmVplSlowRetryIntv,
       "ciscoAtmVplNumAttempts": ciscoAtmVplNumAttempts,
       "ciscoAtmVplLastReleaseCause": ciscoAtmVplLastReleaseCause,
       "ciscoAtmVplLogicalPortDef": ciscoAtmVplLogicalPortDef,
       "ciscoAtmVplLogicalPortIndex": ciscoAtmVplLogicalPortIndex,
       "ciscoAtmVplUpcViolations": ciscoAtmVplUpcViolations,
       "ciscoAtmVplEpdTpdCellDrops": ciscoAtmVplEpdTpdCellDrops,
       "ciscoAtmVplEpdTpdPacketDrops": ciscoAtmVplEpdTpdPacketDrops,
       "ciscoAtmVplEpdTpdPacketsIn": ciscoAtmVplEpdTpdPacketsIn,
       "ciscoAtmVplClp1Drops": ciscoAtmVplClp1Drops,
       "ciscoAtmVplDefaultRxUpcTolerance": ciscoAtmVplDefaultRxUpcTolerance,
       "ciscoAtmVplDefaultRxUpcVbrCdvt": ciscoAtmVplDefaultRxUpcVbrCdvt,
       "ciscoAtmVplLsPerVcqWrrWeight": ciscoAtmVplLsPerVcqWrrWeight,
       "ciscoAtmVplLsPerVcqTunnelIsShaped": ciscoAtmVplLsPerVcqTunnelIsShaped,
       "ciscoAtmVplLsPerVcqXmtQueuedCells": ciscoAtmVplLsPerVcqXmtQueuedCells,
       "ciscoAtmVplLsPerVcQThreshGrp": ciscoAtmVplLsPerVcQThreshGrp,
       "ciscoAtmVplInClp0Cells": ciscoAtmVplInClp0Cells,
       "ciscoAtmVplInClp1Cells": ciscoAtmVplInClp1Cells,
       "ciscoAtmVplOutClp0Cells": ciscoAtmVplOutClp0Cells,
       "ciscoAtmVplOutClp1Cells": ciscoAtmVplOutClp1Cells,
       "ciscoAtmVplCellDrops": ciscoAtmVplCellDrops,
       "ciscoAtmVplClp0VcqFullCellDrops": ciscoAtmVplClp0VcqFullCellDrops,
       "ciscoAtmVplVcqClpThreshCellDrops": ciscoAtmVplVcqClpThreshCellDrops,
       "ciscoAtmVplLsPerVcqTunnelIsHierarchical": ciscoAtmVplLsPerVcqTunnelIsHierarchical,
       "ciscoAtmVplRxNegTraffDescrIndex": ciscoAtmVplRxNegTraffDescrIndex,
       "ciscoAtmVplTxNegTraffDescrIndex": ciscoAtmVplTxNegTraffDescrIndex,
       "ciscoAtmVplSwFabOutCells": ciscoAtmVplSwFabOutCells,
       "ciscoAtmVplSwFabOutClp0Cells": ciscoAtmVplSwFabOutClp0Cells,
       "ciscoAtmVplSwFabOutClp1Cells": ciscoAtmVplSwFabOutClp1Cells,
       "ciscoAtmVplConnName": ciscoAtmVplConnName,
       "ciscoAtmVplConnType": ciscoAtmVplConnType,
       "ciscoAtmVcl": ciscoAtmVcl,
       "ciscoAtmVclTable": ciscoAtmVclTable,
       "ciscoAtmVclEntry": ciscoAtmVclEntry,
       "ciscoAtmVclCastType": ciscoAtmVclCastType,
       "ciscoAtmVclSpanType": ciscoAtmVclSpanType,
       "ciscoAtmVclConfigType": ciscoAtmVclConfigType,
       "ciscoAtmVclRxUpcMode": ciscoAtmVclRxUpcMode,
       "ciscoAtmVclEpdEnable": ciscoAtmVclEpdEnable,
       "ciscoAtmVclConnState": ciscoAtmVclConnState,
       "ciscoAtmVclOamLoopbkTxInterval": ciscoAtmVclOamLoopbkTxInterval,
       "ciscoAtmVclOamSegmentLoopback": ciscoAtmVclOamSegmentLoopback,
       "ciscoAtmVclOamEndLoopback": ciscoAtmVclOamEndLoopback,
       "ciscoAtmVclOamAisEnable": ciscoAtmVclOamAisEnable,
       "ciscoAtmVclOamRdiEnable": ciscoAtmVclOamRdiEnable,
       "ciscoAtmVclInstallTime": ciscoAtmVclInstallTime,
       "ciscoAtmVclInCells": ciscoAtmVclInCells,
       "ciscoAtmVclOutCells": ciscoAtmVclOutCells,
       "ciscoAtmVclCrossIfIndex": ciscoAtmVclCrossIfIndex,
       "ciscoAtmVclCrossVpi": ciscoAtmVclCrossVpi,
       "ciscoAtmVclCrossVci": ciscoAtmVclCrossVci,
       "ciscoAtmVclNextLeafIfIndex": ciscoAtmVclNextLeafIfIndex,
       "ciscoAtmVclNextLeafVpi": ciscoAtmVclNextLeafVpi,
       "ciscoAtmVclNextLeafVci": ciscoAtmVclNextLeafVci,
       "ciscoAtmVclAalEncapFlag": ciscoAtmVclAalEncapFlag,
       "ciscoAtmVclAalEncapProtocol": ciscoAtmVclAalEncapProtocol,
       "ciscoAtmVclAalUserVcType": ciscoAtmVclAalUserVcType,
       "ciscoAtmVclAtmInArpInterval": ciscoAtmVclAtmInArpInterval,
       "ciscoAtmVclRemoteAddr": ciscoAtmVclRemoteAddr,
       "ciscoAtmVclRemoteVpi": ciscoAtmVclRemoteVpi,
       "ciscoAtmVclRemoteVci": ciscoAtmVclRemoteVci,
       "ciscoAtmVclLocation": ciscoAtmVclLocation,
       "ciscoAtmVclSlowRetryIntv": ciscoAtmVclSlowRetryIntv,
       "ciscoAtmVclNumAttempts": ciscoAtmVclNumAttempts,
       "ciscoAtmVclLastReleaseCause": ciscoAtmVclLastReleaseCause,
       "ciscoAtmVclUpcViolations": ciscoAtmVclUpcViolations,
       "ciscoAtmVclEpdTpdCellDrops": ciscoAtmVclEpdTpdCellDrops,
       "ciscoAtmVclEpdTpdPacketDrops": ciscoAtmVclEpdTpdPacketDrops,
       "ciscoAtmVclEpdTpdPacketsIn": ciscoAtmVclEpdTpdPacketsIn,
       "ciscoAtmVclClp1Drops": ciscoAtmVclClp1Drops,
       "ciscoAtmVclDefaultRxUpcTolerance": ciscoAtmVclDefaultRxUpcTolerance,
       "ciscoAtmVclDefaultRxUpcVbrCdvt": ciscoAtmVclDefaultRxUpcVbrCdvt,
       "ciscoAtmVclLsPerVcqWrrWeight": ciscoAtmVclLsPerVcqWrrWeight,
       "ciscoAtmVclLsPerVcqXmtQueuedCells": ciscoAtmVclLsPerVcqXmtQueuedCells,
       "ciscoAtmVclLsPerVcQThreshGrp": ciscoAtmVclLsPerVcQThreshGrp,
       "ciscoAtmVclInClp0Cells": ciscoAtmVclInClp0Cells,
       "ciscoAtmVclInClp1Cells": ciscoAtmVclInClp1Cells,
       "ciscoAtmVclOutClp0Cells": ciscoAtmVclOutClp0Cells,
       "ciscoAtmVclOutClp1Cells": ciscoAtmVclOutClp1Cells,
       "ciscoAtmVclCellDrops": ciscoAtmVclCellDrops,
       "ciscoAtmVclClp0VcqFullCellDrops": ciscoAtmVclClp0VcqFullCellDrops,
       "ciscoAtmVclVcqClpThreshCellDrops": ciscoAtmVclVcqClpThreshCellDrops,
       "ciscoAtmVclRxNegTraffDescrIndex": ciscoAtmVclRxNegTraffDescrIndex,
       "ciscoAtmVclTxNegTraffDescrIndex": ciscoAtmVclTxNegTraffDescrIndex,
       "ciscoAtmVclSwFabOutCells": ciscoAtmVclSwFabOutCells,
       "ciscoAtmVclSwFabOutClp0Cells": ciscoAtmVclSwFabOutClp0Cells,
       "ciscoAtmVclSwFabOutClp1Cells": ciscoAtmVclSwFabOutClp1Cells,
       "ciscoAtmVclConnName": ciscoAtmVclConnName,
       "ciscoAtmVclConnType": ciscoAtmVclConnType,
       "ciscoAtmSvp": ciscoAtmSvp,
       "ciscoAtmSvpAddrTable": ciscoAtmSvpAddrTable,
       "ciscoAtmSvpAddrEntry": ciscoAtmSvpAddrEntry,
       "ciscoAtmSvpAddr": ciscoAtmSvpAddr,
       "ciscoAtmSvpVpi": ciscoAtmSvpVpi,
       "ciscoAtmSvpDirection": ciscoAtmSvpDirection,
       "ciscoAtmSvc": ciscoAtmSvc,
       "ciscoAtmSvcAddrTable": ciscoAtmSvcAddrTable,
       "ciscoAtmSvcAddrEntry": ciscoAtmSvcAddrEntry,
       "ciscoAtmSvcAddr": ciscoAtmSvcAddr,
       "ciscoAtmSvcVpi": ciscoAtmSvcVpi,
       "ciscoAtmSvcVci": ciscoAtmSvcVci,
       "ciscoAtmSvcDirection": ciscoAtmSvcDirection,
       "ciscoAtmSvcFrameDiscardUsesAal5Ie": ciscoAtmSvcFrameDiscardUsesAal5Ie,
       "ciscoAtmSnoopVc": ciscoAtmSnoopVc,
       "ciscoAtmSnoopVcTable": ciscoAtmSnoopVcTable,
       "ciscoAtmSnoopVcEntry": ciscoAtmSnoopVcEntry,
       "ciscoAtmSnoopVcSnoopedIfIndex": ciscoAtmSnoopVcSnoopedIfIndex,
       "ciscoAtmSnoopVcSnoopedVpi": ciscoAtmSnoopVcSnoopedVpi,
       "ciscoAtmSnoopVcSnoopedVci": ciscoAtmSnoopVcSnoopedVci,
       "ciscoAtmSnoopVcDir": ciscoAtmSnoopVcDir,
       "ciscoAtmSnoopVcState": ciscoAtmSnoopVcState,
       "ciscoAtmSnoopVcRowStatus": ciscoAtmSnoopVcRowStatus,
       "ciscoAtmSnoopVp": ciscoAtmSnoopVp,
       "ciscoAtmSnoopVpTable": ciscoAtmSnoopVpTable,
       "ciscoAtmSnoopVpEntry": ciscoAtmSnoopVpEntry,
       "ciscoAtmSnoopVpSnoopedIfIndex": ciscoAtmSnoopVpSnoopedIfIndex,
       "ciscoAtmSnoopVpSnoopedVpi": ciscoAtmSnoopVpSnoopedVpi,
       "ciscoAtmSnoopVpDir": ciscoAtmSnoopVpDir,
       "ciscoAtmSnoopVpState": ciscoAtmSnoopVpState,
       "ciscoAtmSnoopVpRowStatus": ciscoAtmSnoopVpRowStatus,
       "ciscoAtmConnMIBConformance": ciscoAtmConnMIBConformance,
       "ciscoAtmConnMIBCompliances": ciscoAtmConnMIBCompliances,
       "ciscoAtmConnMIBCompliance": ciscoAtmConnMIBCompliance,
       "ciscoAtmConnMIBCompliance2": ciscoAtmConnMIBCompliance2,
       "ciscoAtmConnMIBCompliance3": ciscoAtmConnMIBCompliance3,
       "ciscoAtmConnMIBCompliance4": ciscoAtmConnMIBCompliance4,
       "ciscoAtmConnMIBCompliance5": ciscoAtmConnMIBCompliance5,
       "ciscoAtmConnMIBCompliance6": ciscoAtmConnMIBCompliance6,
       "ciscoAtmConnMIBCompliance7": ciscoAtmConnMIBCompliance7,
       "ciscoAtmConnMIBCompliance8": ciscoAtmConnMIBCompliance8,
       "ciscoAtmConnMIBGroups": ciscoAtmConnMIBGroups,
       "ciscoAtmConnMIBGroup": ciscoAtmConnMIBGroup,
       "ciscoAtmConnMIBGroup2": ciscoAtmConnMIBGroup2,
       "ciscoAtmConnMIBGroup3": ciscoAtmConnMIBGroup3,
       "ciscoAtmConnMIBlsPerVcqGroup": ciscoAtmConnMIBlsPerVcqGroup,
       "ciscoAtmConnMIBlsFcPfqGroup": ciscoAtmConnMIBlsFcPfqGroup,
       "ciscoAtmConnMIBlsPerVcqGroup2": ciscoAtmConnMIBlsPerVcqGroup2,
       "ciscoAtmConnMIBNegTraffGroup": ciscoAtmConnMIBNegTraffGroup,
       "ciscoAtmConnMIBlsFcPfqGroup1": ciscoAtmConnMIBlsFcPfqGroup1,
       "ciscoAtmConnMIBGroup1": ciscoAtmConnMIBGroup1,
       "ciscoAtmConnMIBGroup4": ciscoAtmConnMIBGroup4,
       "ciscoAtmConnNmsGroup": ciscoAtmConnNmsGroup}
)
