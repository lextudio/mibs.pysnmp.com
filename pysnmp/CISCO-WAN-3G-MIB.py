# SNMP MIB module (CISCO-WAN-3G-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-3G-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:44 2024
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

(entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalName")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWan3gMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661)
)
ciscoWan3gMIB.setRevisions(
        ("2013-08-12 00:00",
         "2012-07-25 00:00",
         "2012-07-10 00:00",
         "2010-08-11 00:00",
         "2010-08-04 00:00",
         "2009-02-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class C3gServiceCapability(Bits, TextualConvention):
    status = "current"


class C3gRssi(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )



class C3gEcIo(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )



class C3gTemperature(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )



class C3gPdpType(Integer32, TextualConvention):
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
        *(("ipV4", 2),
          ("ipV4V6", 5),
          ("ipV6", 4),
          ("ppp", 3),
          ("unknown", 1))
    )



class C3gUmtsQosTrafficClass(Integer32, TextualConvention):
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
        *(("background", 5),
          ("conversational", 2),
          ("interactive", 4),
          ("streaming", 3),
          ("subscription", 1))
    )



class C3gUmtsQosLinkBitRate(Integer32, TextualConvention):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("rate128kbps", 5),
          ("rate14dot4mbps", 11),
          ("rate16kbps", 2),
          ("rate1dot15mbps", 13),
          ("rate1dot6mbps", 14),
          ("rate1dot8mbps", 8),
          ("rate256kbps", 6),
          ("rate2dot1mbps", 15),
          ("rate2dot8mbps", 16),
          ("rate32kbps", 3),
          ("rate384kbps", 7),
          ("rate3dot6mbps", 9),
          ("rate4dot2mbps", 17),
          ("rate56kbps", 12),
          ("rate64kbps", 4),
          ("rate7dot2mbps", 10),
          ("rate8dot4mbps", 18),
          ("subscription", 1))
    )



class C3gUmtsQosOrder(Integer32, TextualConvention):
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
        *(("subscription", 1),
          ("withDeliverOrder", 2),
          ("withoutDeliverOrder", 3))
    )



class C3gUmtsQosErroneousSdu(Integer32, TextualConvention):
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
        *(("errSduDeliver", 3),
          ("errSduNotDeliver", 4),
          ("noDetect", 2),
          ("subscription", 1))
    )



class C3gUmtsQosSer(Integer32, TextualConvention):
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
        *(("oneExpMinus1", 8),
          ("oneExpMinus2", 2),
          ("oneExpMinus3", 4),
          ("oneExpMinus4", 5),
          ("oneExpMinus5", 6),
          ("oneExpMinus6", 7),
          ("sevenExpMinus3", 3),
          ("subscription", 1))
    )



class C3gUmtsQosBer(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("fiveExpMinus2", 2),
          ("fiveExpMinus3", 4),
          ("fourExpMinus3", 5),
          ("oneExpMinus2", 3),
          ("oneExpMinus3", 6),
          ("oneExpMinus4", 7),
          ("oneExpMinus5", 8),
          ("oneExpMinus6", 9),
          ("sixExpMinus8", 10),
          ("subscription", 1))
    )



class C3gUmtsQosPriority(Integer32, TextualConvention):
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
        *(("level1", 2),
          ("level2", 3),
          ("level3", 4),
          ("subscription", 1))
    )



class C3gUmtsQosSrcStatDescriptor(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speech", 2),
          ("unknown", 1))
    )



class C3gUmtsQosSignalIndication(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOptimized", 1),
          ("optimized", 2))
    )



class C3gGprsQosPrecedence(Integer32, TextualConvention):
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
        *(("highPriority", 2),
          ("lowPriority", 4),
          ("normalPriority", 3),
          ("subscription", 1))
    )



class C3gGprsQosDelay(Integer32, TextualConvention):
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
        *(("delayClass1", 2),
          ("delayClass2", 3),
          ("delayClass3", 4),
          ("delayClass4", 5),
          ("subscription", 1))
    )



class C3gGprsQosReliability(Integer32, TextualConvention):
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
        *(("ackGtpLlcRlcProtData", 2),
          ("subscription", 1),
          ("unAckGtpAckLlcRlcProtData", 3),
          ("unAckGtpLlcAckRlcProtData", 4),
          ("unAckGtpLlcRlcProtData", 5),
          ("unAckGtpLlcRlcUnProtData", 6))
    )



class C3gGprsQosPeakRate(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("subscription", 1),
          ("upTo128kops", 9),
          ("upTo16kops", 6),
          ("upTo1kops", 2),
          ("upTo256kops", 10),
          ("upTo2kops", 3),
          ("upTo32kops", 7),
          ("upTo4kops", 4),
          ("upTo64kops", 8),
          ("upTo8kops", 5))
    )



class C3gGprsQosMeanRate(Integer32, TextualConvention):
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 32),
          ("rate100", 2),
          ("rate100k", 11),
          ("rate10k", 8),
          ("rate10m", 17),
          ("rate1k", 5),
          ("rate1m", 14),
          ("rate200", 3),
          ("rate200k", 12),
          ("rate20k", 9),
          ("rate20m", 18),
          ("rate2k", 6),
          ("rate2m", 15),
          ("rate500", 4),
          ("rate500k", 13),
          ("rate50k", 10),
          ("rate50m", 19),
          ("rate5k", 7),
          ("rate5m", 16),
          ("resv1", 20),
          ("resv10", 29),
          ("resv11", 30),
          ("resv12", 31),
          ("resv2", 21),
          ("resv3", 22),
          ("resv4", 23),
          ("resv5", 24),
          ("resv6", 25),
          ("resv7", 26),
          ("resv8", 27),
          ("resv9", 28),
          ("subscription", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoWan3gMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWan3gMIBNotifs = _CiscoWan3gMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0)
)
_CiscoWan3gMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWan3gMIBObjects = _CiscoWan3gMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1)
)
_C3gWanCommonTable_Object = MibTable
c3gWanCommonTable = _C3gWanCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1)
)
if mibBuilder.loadTexts:
    c3gWanCommonTable.setStatus("current")
_C3gWanCommonEntry_Object = MibTableRow
c3gWanCommonEntry = _C3gWanCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1)
)
c3gWanCommonEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gWanCommonEntry.setStatus("current")


class _C3gStandard_Type(Integer32):
    """Custom type c3gStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cdma", 1),
          ("gsm", 2))
    )


_C3gStandard_Type.__name__ = "Integer32"
_C3gStandard_Object = MibTableColumn
c3gStandard = _C3gStandard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 1),
    _C3gStandard_Type()
)
c3gStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gStandard.setStatus("current")
_C3gCapability_Type = C3gServiceCapability
_C3gCapability_Object = MibTableColumn
c3gCapability = _C3gCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 2),
    _C3gCapability_Type()
)
c3gCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCapability.setStatus("current")


class _C3gModemState_Type(Integer32):
    """Custom type c3gModemState based on Integer32"""
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
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_C3gModemState_Type.__name__ = "Integer32"
_C3gModemState_Object = MibTableColumn
c3gModemState = _C3gModemState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 3),
    _C3gModemState_Type()
)
c3gModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gModemState.setStatus("current")
_C3gPreviousServiceType_Type = C3gServiceCapability
_C3gPreviousServiceType_Object = MibTableColumn
c3gPreviousServiceType = _C3gPreviousServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 4),
    _C3gPreviousServiceType_Type()
)
c3gPreviousServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gPreviousServiceType.setStatus("current")
_C3gCurrentServiceType_Type = C3gServiceCapability
_C3gCurrentServiceType_Object = MibTableColumn
c3gCurrentServiceType = _C3gCurrentServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 5),
    _C3gCurrentServiceType_Type()
)
c3gCurrentServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCurrentServiceType.setStatus("current")


class _C3gRoamingStatus_Type(Integer32):
    """Custom type c3gRoamingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("home", 3),
          ("roaming", 2),
          ("unknown", 1))
    )


_C3gRoamingStatus_Type.__name__ = "Integer32"
_C3gRoamingStatus_Object = MibTableColumn
c3gRoamingStatus = _C3gRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 6),
    _C3gRoamingStatus_Type()
)
c3gRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gRoamingStatus.setStatus("current")


class _C3gCurrentSystemTime_Type(DisplayString):
    """Custom type c3gCurrentSystemTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gCurrentSystemTime_Type.__name__ = "DisplayString"
_C3gCurrentSystemTime_Object = MibTableColumn
c3gCurrentSystemTime = _C3gCurrentSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 7),
    _C3gCurrentSystemTime_Type()
)
c3gCurrentSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCurrentSystemTime.setStatus("current")


class _C3gConnectionStatus_Type(Integer32):
    """Custom type c3gConnectionStatus based on Integer32"""
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
        *(("active", 8),
          ("connected", 5),
          ("connecting", 3),
          ("disconnected", 6),
          ("dormant", 4),
          ("error", 2),
          ("idle", 7),
          ("inactive", 9),
          ("unknown", 1))
    )


_C3gConnectionStatus_Type.__name__ = "Integer32"
_C3gConnectionStatus_Object = MibTableColumn
c3gConnectionStatus = _C3gConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 8),
    _C3gConnectionStatus_Type()
)
c3gConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gConnectionStatus.setStatus("current")
_C3gNotifRadioService_Type = C3gServiceCapability
_C3gNotifRadioService_Object = MibTableColumn
c3gNotifRadioService = _C3gNotifRadioService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 9),
    _C3gNotifRadioService_Type()
)
c3gNotifRadioService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gNotifRadioService.setStatus("current")
_C3gNotifRssi_Type = C3gRssi
_C3gNotifRssi_Object = MibTableColumn
c3gNotifRssi = _C3gNotifRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 10),
    _C3gNotifRssi_Type()
)
c3gNotifRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gNotifRssi.setStatus("current")
_C3gNotifEcIo_Type = C3gEcIo
_C3gNotifEcIo_Object = MibTableColumn
c3gNotifEcIo = _C3gNotifEcIo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 11),
    _C3gNotifEcIo_Type()
)
c3gNotifEcIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gNotifEcIo.setStatus("current")
_C3gModemTemperature_Type = C3gTemperature
_C3gModemTemperature_Object = MibTableColumn
c3gModemTemperature = _C3gModemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 12),
    _C3gModemTemperature_Type()
)
c3gModemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gModemTemperature.setStatus("current")
if mibBuilder.loadTexts:
    c3gModemTemperature.setUnits("degrees Celsius")


class _C3gRssiOnsetNotifThreshold_Type(C3gRssi):
    """Custom type c3gRssiOnsetNotifThreshold based on C3gRssi"""
    defaultValue = -150


_C3gRssiOnsetNotifThreshold_Object = MibTableColumn
c3gRssiOnsetNotifThreshold = _C3gRssiOnsetNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 13),
    _C3gRssiOnsetNotifThreshold_Type()
)
c3gRssiOnsetNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gRssiOnsetNotifThreshold.setStatus("current")
if mibBuilder.loadTexts:
    c3gRssiOnsetNotifThreshold.setUnits("dBm")


class _C3gRssiAbateNotifThreshold_Type(C3gRssi):
    """Custom type c3gRssiAbateNotifThreshold based on C3gRssi"""
    defaultValue = 0


_C3gRssiAbateNotifThreshold_Object = MibTableColumn
c3gRssiAbateNotifThreshold = _C3gRssiAbateNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 14),
    _C3gRssiAbateNotifThreshold_Type()
)
c3gRssiAbateNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gRssiAbateNotifThreshold.setStatus("current")
if mibBuilder.loadTexts:
    c3gRssiAbateNotifThreshold.setUnits("dBm")


class _C3gEcIoOnsetNotifThreshold_Type(C3gEcIo):
    """Custom type c3gEcIoOnsetNotifThreshold based on C3gEcIo"""
    defaultValue = -150


_C3gEcIoOnsetNotifThreshold_Object = MibTableColumn
c3gEcIoOnsetNotifThreshold = _C3gEcIoOnsetNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 15),
    _C3gEcIoOnsetNotifThreshold_Type()
)
c3gEcIoOnsetNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gEcIoOnsetNotifThreshold.setStatus("current")
if mibBuilder.loadTexts:
    c3gEcIoOnsetNotifThreshold.setUnits("dB")


class _C3gEcIoAbateNotifThreshold_Type(C3gEcIo):
    """Custom type c3gEcIoAbateNotifThreshold based on C3gEcIo"""
    defaultValue = 0


_C3gEcIoAbateNotifThreshold_Object = MibTableColumn
c3gEcIoAbateNotifThreshold = _C3gEcIoAbateNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 16),
    _C3gEcIoAbateNotifThreshold_Type()
)
c3gEcIoAbateNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gEcIoAbateNotifThreshold.setStatus("current")
if mibBuilder.loadTexts:
    c3gEcIoAbateNotifThreshold.setUnits("dB")


class _C3gModemTemperOnsetNotifThreshold_Type(C3gTemperature):
    """Custom type c3gModemTemperOnsetNotifThreshold based on C3gTemperature"""
    defaultValue = 100


_C3gModemTemperOnsetNotifThreshold_Object = MibTableColumn
c3gModemTemperOnsetNotifThreshold = _C3gModemTemperOnsetNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 17),
    _C3gModemTemperOnsetNotifThreshold_Type()
)
c3gModemTemperOnsetNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gModemTemperOnsetNotifThreshold.setStatus("current")
if mibBuilder.loadTexts:
    c3gModemTemperOnsetNotifThreshold.setUnits("degrees Celsius")


class _C3gModemTemperAbateNotifThreshold_Type(C3gTemperature):
    """Custom type c3gModemTemperAbateNotifThreshold based on C3gTemperature"""
    defaultValue = -50


_C3gModemTemperAbateNotifThreshold_Object = MibTableColumn
c3gModemTemperAbateNotifThreshold = _C3gModemTemperAbateNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 18),
    _C3gModemTemperAbateNotifThreshold_Type()
)
c3gModemTemperAbateNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gModemTemperAbateNotifThreshold.setStatus("current")
if mibBuilder.loadTexts:
    c3gModemTemperAbateNotifThreshold.setUnits("degrees Celsius")


class _C3gModemReset_Type(Integer32):
    """Custom type c3gModemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerCycle", 2),
          ("reset", 1))
    )


_C3gModemReset_Type.__name__ = "Integer32"
_C3gModemReset_Object = MibTableColumn
c3gModemReset = _C3gModemReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 19),
    _C3gModemReset_Type()
)
c3gModemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gModemReset.setStatus("current")


class _C3gModemUpNotifEnabled_Type(TruthValue):
    """Custom type c3gModemUpNotifEnabled based on TruthValue"""


_C3gModemUpNotifEnabled_Object = MibTableColumn
c3gModemUpNotifEnabled = _C3gModemUpNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 20),
    _C3gModemUpNotifEnabled_Type()
)
c3gModemUpNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gModemUpNotifEnabled.setStatus("current")


class _C3gModemDownNotifEnabled_Type(TruthValue):
    """Custom type c3gModemDownNotifEnabled based on TruthValue"""


_C3gModemDownNotifEnabled_Object = MibTableColumn
c3gModemDownNotifEnabled = _C3gModemDownNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 21),
    _C3gModemDownNotifEnabled_Type()
)
c3gModemDownNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gModemDownNotifEnabled.setStatus("current")


class _C3gServiceChangedNotifEnabled_Type(TruthValue):
    """Custom type c3gServiceChangedNotifEnabled based on TruthValue"""


_C3gServiceChangedNotifEnabled_Object = MibTableColumn
c3gServiceChangedNotifEnabled = _C3gServiceChangedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 22),
    _C3gServiceChangedNotifEnabled_Type()
)
c3gServiceChangedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gServiceChangedNotifEnabled.setStatus("current")


class _C3gNetworkChangedNotifEnabled_Type(TruthValue):
    """Custom type c3gNetworkChangedNotifEnabled based on TruthValue"""


_C3gNetworkChangedNotifEnabled_Object = MibTableColumn
c3gNetworkChangedNotifEnabled = _C3gNetworkChangedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 23),
    _C3gNetworkChangedNotifEnabled_Type()
)
c3gNetworkChangedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gNetworkChangedNotifEnabled.setStatus("current")


class _C3gConnectionStatusChangedNotifFlag_Type(Bits):
    """Custom type c3gConnectionStatusChangedNotifFlag based on Bits"""
    namedValues = NamedValues(
        *(("active", 7),
          ("connected", 4),
          ("connecting", 2),
          ("disconnected", 5),
          ("dormant", 3),
          ("error", 1),
          ("idle", 6),
          ("inactive", 8),
          ("unknown", 0))
    )

_C3gConnectionStatusChangedNotifFlag_Type.__name__ = "Bits"
_C3gConnectionStatusChangedNotifFlag_Object = MibTableColumn
c3gConnectionStatusChangedNotifFlag = _C3gConnectionStatusChangedNotifFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 24),
    _C3gConnectionStatusChangedNotifFlag_Type()
)
c3gConnectionStatusChangedNotifFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gConnectionStatusChangedNotifFlag.setStatus("current")
_C3gRssiOnsetNotifFlag_Type = C3gServiceCapability
_C3gRssiOnsetNotifFlag_Object = MibTableColumn
c3gRssiOnsetNotifFlag = _C3gRssiOnsetNotifFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 25),
    _C3gRssiOnsetNotifFlag_Type()
)
c3gRssiOnsetNotifFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gRssiOnsetNotifFlag.setStatus("current")
_C3gRssiAbateNotifFlag_Type = C3gServiceCapability
_C3gRssiAbateNotifFlag_Object = MibTableColumn
c3gRssiAbateNotifFlag = _C3gRssiAbateNotifFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 26),
    _C3gRssiAbateNotifFlag_Type()
)
c3gRssiAbateNotifFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gRssiAbateNotifFlag.setStatus("current")
_C3gEcIoOnsetNotifFlag_Type = C3gServiceCapability
_C3gEcIoOnsetNotifFlag_Object = MibTableColumn
c3gEcIoOnsetNotifFlag = _C3gEcIoOnsetNotifFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 27),
    _C3gEcIoOnsetNotifFlag_Type()
)
c3gEcIoOnsetNotifFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gEcIoOnsetNotifFlag.setStatus("current")
_C3gEcIoAbateNotifFlag_Type = C3gServiceCapability
_C3gEcIoAbateNotifFlag_Object = MibTableColumn
c3gEcIoAbateNotifFlag = _C3gEcIoAbateNotifFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 28),
    _C3gEcIoAbateNotifFlag_Type()
)
c3gEcIoAbateNotifFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gEcIoAbateNotifFlag.setStatus("current")


class _C3gModemTemperOnsetNotifEnabled_Type(TruthValue):
    """Custom type c3gModemTemperOnsetNotifEnabled based on TruthValue"""


_C3gModemTemperOnsetNotifEnabled_Object = MibTableColumn
c3gModemTemperOnsetNotifEnabled = _C3gModemTemperOnsetNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 29),
    _C3gModemTemperOnsetNotifEnabled_Type()
)
c3gModemTemperOnsetNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gModemTemperOnsetNotifEnabled.setStatus("current")


class _C3gModemTemperAbateNotifEnabled_Type(TruthValue):
    """Custom type c3gModemTemperAbateNotifEnabled based on TruthValue"""


_C3gModemTemperAbateNotifEnabled_Object = MibTableColumn
c3gModemTemperAbateNotifEnabled = _C3gModemTemperAbateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 30),
    _C3gModemTemperAbateNotifEnabled_Type()
)
c3gModemTemperAbateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gModemTemperAbateNotifEnabled.setStatus("current")


class _C3gGpsState_Type(TruthValue):
    """Custom type c3gGpsState based on TruthValue"""


_C3gGpsState_Object = MibTableColumn
c3gGpsState = _C3gGpsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 1, 1, 31),
    _C3gGpsState_Type()
)
c3gGpsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gGpsState.setStatus("current")
_C3gWanCdma_ObjectIdentity = ObjectIdentity
c3gWanCdma = _C3gWanCdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2)
)
_C3gCdmaSessionTable_Object = MibTable
c3gCdmaSessionTable = _C3gCdmaSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 1)
)
if mibBuilder.loadTexts:
    c3gCdmaSessionTable.setStatus("current")
_C3gCdmaSessionEntry_Object = MibTableRow
c3gCdmaSessionEntry = _C3gCdmaSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 1, 1)
)
c3gCdmaSessionEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gCdmaSessionEntry.setStatus("current")
_C3gCdmaTotalCallDuration_Type = Counter64
_C3gCdmaTotalCallDuration_Object = MibTableColumn
c3gCdmaTotalCallDuration = _C3gCdmaTotalCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 1, 1, 1),
    _C3gCdmaTotalCallDuration_Type()
)
c3gCdmaTotalCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaTotalCallDuration.setStatus("current")
if mibBuilder.loadTexts:
    c3gCdmaTotalCallDuration.setUnits("seconds")
_C3gCdmaTotalTransmitted_Type = Counter64
_C3gCdmaTotalTransmitted_Object = MibTableColumn
c3gCdmaTotalTransmitted = _C3gCdmaTotalTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 1, 1, 2),
    _C3gCdmaTotalTransmitted_Type()
)
c3gCdmaTotalTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaTotalTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    c3gCdmaTotalTransmitted.setUnits("bytes")
_C3gCdmaTotalReceived_Type = Counter64
_C3gCdmaTotalReceived_Object = MibTableColumn
c3gCdmaTotalReceived = _C3gCdmaTotalReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 1, 1, 3),
    _C3gCdmaTotalReceived_Type()
)
c3gCdmaTotalReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaTotalReceived.setStatus("current")
if mibBuilder.loadTexts:
    c3gCdmaTotalReceived.setUnits("bytes")


class _C3gHdrDdtmPreference_Type(Integer32):
    """Custom type c3gHdrDdtmPreference based on Integer32"""
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
        *(("noChange", 4),
          ("off", 2),
          ("on", 3),
          ("unknown", 1))
    )


_C3gHdrDdtmPreference_Type.__name__ = "Integer32"
_C3gHdrDdtmPreference_Object = MibTableColumn
c3gHdrDdtmPreference = _C3gHdrDdtmPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 1, 1, 4),
    _C3gHdrDdtmPreference_Type()
)
c3gHdrDdtmPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gHdrDdtmPreference.setStatus("current")
_C3gCdmaConnectionTable_Object = MibTable
c3gCdmaConnectionTable = _C3gCdmaConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2)
)
if mibBuilder.loadTexts:
    c3gCdmaConnectionTable.setStatus("current")
_C3gCdmaConnectionEntry_Object = MibTableRow
c3gCdmaConnectionEntry = _C3gCdmaConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1)
)
c3gCdmaConnectionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    c3gCdmaConnectionEntry.setStatus("current")


class _C3gOutgoingCallNumber_Type(DisplayString):
    """Custom type c3gOutgoingCallNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gOutgoingCallNumber_Type.__name__ = "DisplayString"
_C3gOutgoingCallNumber_Object = MibTableColumn
c3gOutgoingCallNumber = _C3gOutgoingCallNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 1),
    _C3gOutgoingCallNumber_Type()
)
c3gOutgoingCallNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gOutgoingCallNumber.setStatus("current")


class _C3gHdrAtState_Type(Integer32):
    """Custom type c3gHdrAtState based on Integer32"""
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
        *(("access", 6),
          ("acquisition", 3),
          ("connected", 7),
          ("idle", 5),
          ("inactive", 2),
          ("sync", 4),
          ("unknown", 1))
    )


_C3gHdrAtState_Type.__name__ = "Integer32"
_C3gHdrAtState_Object = MibTableColumn
c3gHdrAtState = _C3gHdrAtState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 2),
    _C3gHdrAtState_Type()
)
c3gHdrAtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gHdrAtState.setStatus("current")


class _C3gHdrSessionState_Type(Integer32):
    """Custom type c3gHdrSessionState based on Integer32"""
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
        *(("addressManagementProtocolSetup", 4),
          ("anInitiated", 6),
          ("atInitiated", 5),
          ("close", 3),
          ("open", 2),
          ("unknown", 1))
    )


_C3gHdrSessionState_Type.__name__ = "Integer32"
_C3gHdrSessionState_Object = MibTableColumn
c3gHdrSessionState = _C3gHdrSessionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 3),
    _C3gHdrSessionState_Type()
)
c3gHdrSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gHdrSessionState.setStatus("current")


class _C3gUati_Type(DisplayString):
    """Custom type c3gUati based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gUati_Type.__name__ = "DisplayString"
_C3gUati_Object = MibTableColumn
c3gUati = _C3gUati_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 4),
    _C3gUati_Type()
)
c3gUati.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gUati.setStatus("current")
_C3gColorCode_Type = Unsigned32
_C3gColorCode_Object = MibTableColumn
c3gColorCode = _C3gColorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 5),
    _C3gColorCode_Type()
)
c3gColorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gColorCode.setStatus("current")
_C3gRati_Type = Unsigned32
_C3gRati_Object = MibTableColumn
c3gRati = _C3gRati_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 6),
    _C3gRati_Type()
)
c3gRati.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gRati.setStatus("current")


class _C3gHdrSessionDuration_Type(Unsigned32):
    """Custom type c3gHdrSessionDuration based on Unsigned32"""
    defaultValue = 0


_C3gHdrSessionDuration_Object = MibTableColumn
c3gHdrSessionDuration = _C3gHdrSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 7),
    _C3gHdrSessionDuration_Type()
)
c3gHdrSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gHdrSessionDuration.setStatus("current")
if mibBuilder.loadTexts:
    c3gHdrSessionDuration.setUnits("milliseconds")


class _C3gHdrSessionStart_Type(Unsigned32):
    """Custom type c3gHdrSessionStart based on Unsigned32"""
    defaultValue = 0


_C3gHdrSessionStart_Object = MibTableColumn
c3gHdrSessionStart = _C3gHdrSessionStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 8),
    _C3gHdrSessionStart_Type()
)
c3gHdrSessionStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gHdrSessionStart.setStatus("current")
if mibBuilder.loadTexts:
    c3gHdrSessionStart.setUnits("milliseconds")


class _C3gHdrSessionEnd_Type(Unsigned32):
    """Custom type c3gHdrSessionEnd based on Unsigned32"""
    defaultValue = 0


_C3gHdrSessionEnd_Object = MibTableColumn
c3gHdrSessionEnd = _C3gHdrSessionEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 9),
    _C3gHdrSessionEnd_Type()
)
c3gHdrSessionEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gHdrSessionEnd.setStatus("current")
if mibBuilder.loadTexts:
    c3gHdrSessionEnd.setUnits("milliseconds")


class _C3gAuthStatus_Type(Integer32):
    """Custom type c3gAuthStatus based on Integer32"""
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
        *(("authenticated", 3),
          ("authenticationDisabled", 5),
          ("failed", 4),
          ("notAuthenticated", 2),
          ("unknown", 1))
    )


_C3gAuthStatus_Type.__name__ = "Integer32"
_C3gAuthStatus_Object = MibTableColumn
c3gAuthStatus = _C3gAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 10),
    _C3gAuthStatus_Type()
)
c3gAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gAuthStatus.setStatus("current")


class _C3gHdrDrc_Type(Unsigned32):
    """Custom type c3gHdrDrc based on Unsigned32"""
    defaultValue = 0


_C3gHdrDrc_Object = MibTableColumn
c3gHdrDrc = _C3gHdrDrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 11),
    _C3gHdrDrc_Type()
)
c3gHdrDrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gHdrDrc.setStatus("current")


class _C3gHdrDrcCover_Type(Unsigned32):
    """Custom type c3gHdrDrcCover based on Unsigned32"""
    defaultValue = 0


_C3gHdrDrcCover_Object = MibTableColumn
c3gHdrDrcCover = _C3gHdrDrcCover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 12),
    _C3gHdrDrcCover_Type()
)
c3gHdrDrcCover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gHdrDrcCover.setStatus("current")


class _C3gHdrRri_Type(Integer32):
    """Custom type c3gHdrRri based on Integer32"""
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
        *(("pilotOnly", 2),
          ("rri153dot6kbps", 7),
          ("rri19dot2kbps", 4),
          ("rri38dot4kbps", 5),
          ("rri76dot8kbps", 6),
          ("rri9dot6kbps", 3),
          ("unknown", 1))
    )


_C3gHdrRri_Type.__name__ = "Integer32"
_C3gHdrRri_Object = MibTableColumn
c3gHdrRri = _C3gHdrRri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 13),
    _C3gHdrRri_Type()
)
c3gHdrRri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gHdrRri.setStatus("current")
_C3gMobileIpErrorCode_Type = Integer32
_C3gMobileIpErrorCode_Object = MibTableColumn
c3gMobileIpErrorCode = _C3gMobileIpErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 14),
    _C3gMobileIpErrorCode_Type()
)
c3gMobileIpErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gMobileIpErrorCode.setStatus("current")
_C3gCdmaCurrentTransmitted_Type = Counter64
_C3gCdmaCurrentTransmitted_Object = MibTableColumn
c3gCdmaCurrentTransmitted = _C3gCdmaCurrentTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 15),
    _C3gCdmaCurrentTransmitted_Type()
)
c3gCdmaCurrentTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaCurrentTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    c3gCdmaCurrentTransmitted.setUnits("bytes")
_C3gCdmaCurrentReceived_Type = Counter64
_C3gCdmaCurrentReceived_Object = MibTableColumn
c3gCdmaCurrentReceived = _C3gCdmaCurrentReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 16),
    _C3gCdmaCurrentReceived_Type()
)
c3gCdmaCurrentReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaCurrentReceived.setStatus("current")
if mibBuilder.loadTexts:
    c3gCdmaCurrentReceived.setUnits("bytes")


class _C3gCdmaCurrentCallStatus_Type(Integer32):
    """Custom type c3gCdmaCurrentCallStatus based on Integer32"""
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
        *(("connected", 5),
          ("connecting", 3),
          ("disconnected", 6),
          ("dormant", 4),
          ("error", 2),
          ("unknown", 1))
    )


_C3gCdmaCurrentCallStatus_Type.__name__ = "Integer32"
_C3gCdmaCurrentCallStatus_Object = MibTableColumn
c3gCdmaCurrentCallStatus = _C3gCdmaCurrentCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 17),
    _C3gCdmaCurrentCallStatus_Type()
)
c3gCdmaCurrentCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaCurrentCallStatus.setStatus("current")


class _C3gCdmaCurrentCallDuration_Type(Unsigned32):
    """Custom type c3gCdmaCurrentCallDuration based on Unsigned32"""
    defaultValue = 0


_C3gCdmaCurrentCallDuration_Object = MibTableColumn
c3gCdmaCurrentCallDuration = _C3gCdmaCurrentCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 18),
    _C3gCdmaCurrentCallDuration_Type()
)
c3gCdmaCurrentCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaCurrentCallDuration.setStatus("current")
if mibBuilder.loadTexts:
    c3gCdmaCurrentCallDuration.setUnits("seconds")


class _C3gCdmaCurrentCallType_Type(Integer32):
    """Custom type c3gCdmaCurrentCallType based on Integer32"""
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
        *(("asyncData", 2),
          ("atAsyncDataCall", 5),
          ("atPacketCall", 7),
          ("atVoiceCall", 6),
          ("callWaiting", 12),
          ("dormant", 14),
          ("e911Call", 15),
          ("faxCall", 8),
          ("otaCall", 10),
          ("packet1xRttCall", 4),
          ("positionDetermination", 13),
          ("smsCall", 9),
          ("testCall", 11),
          ("unknown", 1),
          ("voiceCall", 3))
    )


_C3gCdmaCurrentCallType_Type.__name__ = "Integer32"
_C3gCdmaCurrentCallType_Object = MibTableColumn
c3gCdmaCurrentCallType = _C3gCdmaCurrentCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 19),
    _C3gCdmaCurrentCallType_Type()
)
c3gCdmaCurrentCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaCurrentCallType.setStatus("current")


class _C3gCdmaLastCallDisconnReason_Type(Integer32):
    """Custom type c3gCdmaLastCallDisconnReason based on Integer32"""
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
              37)
        )
    )
    namedValues = NamedValues(
        *(("abnormalCallEnd", 5),
          ("accessAttemptInProg", 18),
          ("accessBlockedByBs", 28),
          ("activationEndedOtasp", 13),
          ("alreadyOnTraffChann", 29),
          ("baseStatAlertStop", 11),
          ("baseStatIntercept", 6),
          ("baseStatRelease", 7),
          ("baseStatReleaseNoReas", 8),
          ("baseStatReleaseSoRej", 9),
          ("billingOrAuthErrHdr", 33),
          ("busyHdr", 32),
          ("callEndedHdr", 37),
          ("clientEndedCall", 12),
          ("dataCallEnded", 31),
          ("emergencyCall", 30),
          ("gpsCallEnded", 22),
          ("hdrExitDueToPrl", 35),
          ("incomingCall", 10),
          ("maxAccesProbTransmit", 15),
          ("modemCdmaLocTilPowCyc", 3),
          ("modemLocked", 21),
          ("modemOffline", 2),
          ("ndssFailure", 14),
          ("noConcurrentService", 24),
          ("noResponseFromBs", 25),
          ("noService", 4),
          ("noSessionHdr", 36),
          ("notCompatConcurServ", 27),
          ("persistTestFailure", 16),
          ("reasonUnspecified", 19),
          ("recdRetryOrder", 20),
          ("rejectedByBs", 26),
          ("ruimNotPresent", 17),
          ("smsCallEnded", 23),
          ("sysChangeDueToPrlHdr", 34),
          ("unknown", 1))
    )


_C3gCdmaLastCallDisconnReason_Type.__name__ = "Integer32"
_C3gCdmaLastCallDisconnReason_Object = MibTableColumn
c3gCdmaLastCallDisconnReason = _C3gCdmaLastCallDisconnReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 20),
    _C3gCdmaLastCallDisconnReason_Type()
)
c3gCdmaLastCallDisconnReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaLastCallDisconnReason.setStatus("current")


class _C3gCdmaLastConnError_Type(Integer32):
    """Custom type c3gCdmaLastConnError based on Integer32"""
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("badCallType", 3),
          ("badPrivacySetting", 24),
          ("badServiceType", 4),
          ("cannotAnswerIncomingCall", 23),
          ("communicationProblem", 26),
          ("dialedNumberProhibited", 15),
          ("expectingNumber", 5),
          ("invalidClientId", 2),
          ("invalidCommandCallState", 20),
          ("invalidCommandModemState", 21),
          ("invalidDigits", 7),
          ("invalidLastActiveNetwork", 28),
          ("invalidOtaspActivatCode", 11),
          ("modemInUse", 17),
          ("modemLocked", 13),
          ("modemOffline", 12),
          ("noCollocatedHdr", 29),
          ("noCommandBuffers", 25),
          ("noValidService", 22),
          ("none", 1),
          ("nullAalphaBuffer", 9),
          ("nullNumberBuffer", 6),
          ("onlyE911Calls", 16),
          ("outOfRangeAlphaNumber", 10),
          ("outOfRangeNumber", 8),
          ("uimNotPresent", 30),
          ("unspecifiedError", 27),
          ("unsupportedFlash", 14),
          ("unsupportedServiceType", 18),
          ("wrongCallType", 19))
    )


_C3gCdmaLastConnError_Type.__name__ = "Integer32"
_C3gCdmaLastConnError_Object = MibTableColumn
c3gCdmaLastConnError = _C3gCdmaLastConnError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 2, 1, 21),
    _C3gCdmaLastConnError_Type()
)
c3gCdmaLastConnError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaLastConnError.setStatus("current")
_C3gCdmaIdentityTable_Object = MibTable
c3gCdmaIdentityTable = _C3gCdmaIdentityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 3)
)
if mibBuilder.loadTexts:
    c3gCdmaIdentityTable.setStatus("current")
_C3gCdmaIdentityEntry_Object = MibTableRow
c3gCdmaIdentityEntry = _C3gCdmaIdentityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 3, 1)
)
c3gCdmaIdentityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gCdmaIdentityEntry.setStatus("current")


class _C3gEsn_Type(DisplayString):
    """Custom type c3gEsn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_C3gEsn_Type.__name__ = "DisplayString"
_C3gEsn_Object = MibTableColumn
c3gEsn = _C3gEsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 3, 1, 1),
    _C3gEsn_Type()
)
c3gEsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gEsn.setStatus("current")


class _C3gModemActivationStatus_Type(Integer32):
    """Custom type c3gModemActivationStatus based on Integer32"""
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
        *(("activated", 2),
          ("notActivated", 3),
          ("unknown", 1))
    )


_C3gModemActivationStatus_Type.__name__ = "Integer32"
_C3gModemActivationStatus_Object = MibTableColumn
c3gModemActivationStatus = _C3gModemActivationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 3, 1, 2),
    _C3gModemActivationStatus_Type()
)
c3gModemActivationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gModemActivationStatus.setStatus("current")


class _C3gAccountActivationDate_Type(DisplayString):
    """Custom type c3gAccountActivationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_C3gAccountActivationDate_Type.__name__ = "DisplayString"
_C3gAccountActivationDate_Object = MibTableColumn
c3gAccountActivationDate = _C3gAccountActivationDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 3, 1, 3),
    _C3gAccountActivationDate_Type()
)
c3gAccountActivationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gAccountActivationDate.setStatus("current")


class _C3gCdmaRoamingPreference_Type(Integer32):
    """Custom type c3gCdmaRoamingPreference based on Integer32"""
    defaultValue = 4

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
        *(("affiliated", 3),
          ("any", 4),
          ("home", 2),
          ("unknown", 1))
    )


_C3gCdmaRoamingPreference_Type.__name__ = "Integer32"
_C3gCdmaRoamingPreference_Object = MibTableColumn
c3gCdmaRoamingPreference = _C3gCdmaRoamingPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 3, 1, 4),
    _C3gCdmaRoamingPreference_Type()
)
c3gCdmaRoamingPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gCdmaRoamingPreference.setStatus("current")


class _C3gPrlVersion_Type(Unsigned32):
    """Custom type c3gPrlVersion based on Unsigned32"""
    defaultValue = 0


_C3gPrlVersion_Object = MibTableColumn
c3gPrlVersion = _C3gPrlVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 3, 1, 5),
    _C3gPrlVersion_Type()
)
c3gPrlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gPrlVersion.setStatus("current")


class _C3gMdn_Type(DisplayString):
    """Custom type c3gMdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gMdn_Type.__name__ = "DisplayString"
_C3gMdn_Object = MibTableColumn
c3gMdn = _C3gMdn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 3, 1, 6),
    _C3gMdn_Type()
)
c3gMdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gMdn.setStatus("current")


class _C3gMsid_Type(DisplayString):
    """Custom type c3gMsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gMsid_Type.__name__ = "DisplayString"
_C3gMsid_Object = MibTableColumn
c3gMsid = _C3gMsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 3, 1, 7),
    _C3gMsid_Type()
)
c3gMsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gMsid.setStatus("current")


class _C3gMsl_Type(DisplayString):
    """Custom type c3gMsl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gMsl_Type.__name__ = "DisplayString"
_C3gMsl_Object = MibTableColumn
c3gMsl = _C3gMsl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 3, 1, 8),
    _C3gMsl_Type()
)
c3gMsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gMsl.setStatus("current")
_C3gCdmaNetworkTable_Object = MibTable
c3gCdmaNetworkTable = _C3gCdmaNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4)
)
if mibBuilder.loadTexts:
    c3gCdmaNetworkTable.setStatus("current")
_C3gCdmaNetworkEntry_Object = MibTableRow
c3gCdmaNetworkEntry = _C3gCdmaNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4, 1)
)
c3gCdmaNetworkEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gCdmaNetworkEntry.setStatus("current")


class _C3gCdmaCurrentServiceStatus_Type(DisplayString):
    """Custom type c3gCdmaCurrentServiceStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gCdmaCurrentServiceStatus_Type.__name__ = "DisplayString"
_C3gCdmaCurrentServiceStatus_Object = MibTableColumn
c3gCdmaCurrentServiceStatus = _C3gCdmaCurrentServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4, 1, 1),
    _C3gCdmaCurrentServiceStatus_Type()
)
c3gCdmaCurrentServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaCurrentServiceStatus.setStatus("current")


class _C3gCdmaHybridModePreference_Type(Integer32):
    """Custom type c3gCdmaHybridModePreference based on Integer32"""
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
        *(("evDoOnly", 3),
          ("hybrid", 2),
          ("oneXRttOnly", 4),
          ("unknown", 1))
    )


_C3gCdmaHybridModePreference_Type.__name__ = "Integer32"
_C3gCdmaHybridModePreference_Object = MibTableColumn
c3gCdmaHybridModePreference = _C3gCdmaHybridModePreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4, 1, 2),
    _C3gCdmaHybridModePreference_Type()
)
c3gCdmaHybridModePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gCdmaHybridModePreference.setStatus("current")


class _C3gCdmaCurrentRoamingStatus_Type(Integer32):
    """Custom type c3gCdmaCurrentRoamingStatus based on Integer32"""
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
        *(("home", 2),
          ("roamingWithSid", 3),
          ("roamingWithoutSid", 4),
          ("unknown", 1))
    )


_C3gCdmaCurrentRoamingStatus_Type.__name__ = "Integer32"
_C3gCdmaCurrentRoamingStatus_Object = MibTableColumn
c3gCdmaCurrentRoamingStatus = _C3gCdmaCurrentRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4, 1, 3),
    _C3gCdmaCurrentRoamingStatus_Type()
)
c3gCdmaCurrentRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaCurrentRoamingStatus.setStatus("current")


class _C3gCurrentIdleDigitalMode_Type(Integer32):
    """Custom type c3gCurrentIdleDigitalMode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("amps", 3),
          ("cdma", 4),
          ("gps", 8),
          ("gsm", 5),
          ("hdr", 6),
          ("lte", 9),
          ("noService", 2),
          ("unknown", 1),
          ("wcdma", 7))
    )


_C3gCurrentIdleDigitalMode_Type.__name__ = "Integer32"
_C3gCurrentIdleDigitalMode_Object = MibTableColumn
c3gCurrentIdleDigitalMode = _C3gCurrentIdleDigitalMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4, 1, 4),
    _C3gCurrentIdleDigitalMode_Type()
)
c3gCurrentIdleDigitalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCurrentIdleDigitalMode.setStatus("current")


class _C3gCurrentSid_Type(Integer32):
    """Custom type c3gCurrentSid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_C3gCurrentSid_Type.__name__ = "Integer32"
_C3gCurrentSid_Object = MibTableColumn
c3gCurrentSid = _C3gCurrentSid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4, 1, 5),
    _C3gCurrentSid_Type()
)
c3gCurrentSid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gCurrentSid.setStatus("current")


class _C3gCurrentNid_Type(Integer32):
    """Custom type c3gCurrentNid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_C3gCurrentNid_Type.__name__ = "Integer32"
_C3gCurrentNid_Object = MibTableColumn
c3gCurrentNid = _C3gCurrentNid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4, 1, 6),
    _C3gCurrentNid_Type()
)
c3gCurrentNid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gCurrentNid.setStatus("current")


class _C3gCurrentCallSetupMode_Type(Integer32):
    """Custom type c3gCurrentCallSetupMode based on Integer32"""
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
        *(("mobileIpOnly", 4),
          ("mobileIpPreferWithSipFallback", 3),
          ("simpleIpOnly", 2),
          ("unknown", 1))
    )


_C3gCurrentCallSetupMode_Type.__name__ = "Integer32"
_C3gCurrentCallSetupMode_Object = MibTableColumn
c3gCurrentCallSetupMode = _C3gCurrentCallSetupMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4, 1, 7),
    _C3gCurrentCallSetupMode_Type()
)
c3gCurrentCallSetupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gCurrentCallSetupMode.setStatus("current")


class _C3gSipUsername_Type(DisplayString):
    """Custom type c3gSipUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gSipUsername_Type.__name__ = "DisplayString"
_C3gSipUsername_Object = MibTableColumn
c3gSipUsername = _C3gSipUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4, 1, 8),
    _C3gSipUsername_Type()
)
c3gSipUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gSipUsername.setStatus("current")


class _C3gSipPassword_Type(DisplayString):
    """Custom type c3gSipPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gSipPassword_Type.__name__ = "DisplayString"
_C3gSipPassword_Object = MibTableColumn
c3gSipPassword = _C3gSipPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4, 1, 9),
    _C3gSipPassword_Type()
)
c3gSipPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gSipPassword.setStatus("current")


class _C3gServingBaseStationLongitude_Type(DisplayString):
    """Custom type c3gServingBaseStationLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gServingBaseStationLongitude_Type.__name__ = "DisplayString"
_C3gServingBaseStationLongitude_Object = MibTableColumn
c3gServingBaseStationLongitude = _C3gServingBaseStationLongitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4, 1, 10),
    _C3gServingBaseStationLongitude_Type()
)
c3gServingBaseStationLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gServingBaseStationLongitude.setStatus("current")


class _C3gServingBaseStationLatitude_Type(DisplayString):
    """Custom type c3gServingBaseStationLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gServingBaseStationLatitude_Type.__name__ = "DisplayString"
_C3gServingBaseStationLatitude_Object = MibTableColumn
c3gServingBaseStationLatitude = _C3gServingBaseStationLatitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 4, 1, 11),
    _C3gServingBaseStationLatitude_Type()
)
c3gServingBaseStationLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gServingBaseStationLatitude.setStatus("current")
_C3gCdmaProfile_ObjectIdentity = ObjectIdentity
c3gCdmaProfile = _C3gCdmaProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5)
)
_C3gCdmaProfileCommonTable_Object = MibTable
c3gCdmaProfileCommonTable = _C3gCdmaProfileCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    c3gCdmaProfileCommonTable.setStatus("current")
_C3gCdmaProfileCommonEntry_Object = MibTableRow
c3gCdmaProfileCommonEntry = _C3gCdmaProfileCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 1, 1)
)
c3gCdmaProfileCommonEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gCdmaProfileCommonEntry.setStatus("current")


class _C3gNumberOfDataProfileConfigurable_Type(Unsigned32):
    """Custom type c3gNumberOfDataProfileConfigurable based on Unsigned32"""
    defaultValue = 0


_C3gNumberOfDataProfileConfigurable_Object = MibTableColumn
c3gNumberOfDataProfileConfigurable = _C3gNumberOfDataProfileConfigurable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 1, 1, 1),
    _C3gNumberOfDataProfileConfigurable_Type()
)
c3gNumberOfDataProfileConfigurable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gNumberOfDataProfileConfigurable.setStatus("current")
_C3gCurrentActiveDataProfile_Type = Unsigned32
_C3gCurrentActiveDataProfile_Object = MibTableColumn
c3gCurrentActiveDataProfile = _C3gCurrentActiveDataProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 1, 1, 2),
    _C3gCurrentActiveDataProfile_Type()
)
c3gCurrentActiveDataProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gCurrentActiveDataProfile.setStatus("current")
_C3gCdmaProfileTable_Object = MibTable
c3gCdmaProfileTable = _C3gCdmaProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    c3gCdmaProfileTable.setStatus("current")
_C3gCdmaProfileEntry_Object = MibTableRow
c3gCdmaProfileEntry = _C3gCdmaProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1)
)
c3gCdmaProfileEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gCdmaProfileIndex"),
)
if mibBuilder.loadTexts:
    c3gCdmaProfileEntry.setStatus("current")


class _C3gCdmaProfileIndex_Type(Integer32):
    """Custom type c3gCdmaProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_C3gCdmaProfileIndex_Type.__name__ = "Integer32"
_C3gCdmaProfileIndex_Object = MibTableColumn
c3gCdmaProfileIndex = _C3gCdmaProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 1),
    _C3gCdmaProfileIndex_Type()
)
c3gCdmaProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c3gCdmaProfileIndex.setStatus("current")


class _C3gNai_Type(DisplayString):
    """Custom type c3gNai based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gNai_Type.__name__ = "DisplayString"
_C3gNai_Object = MibTableColumn
c3gNai = _C3gNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 2),
    _C3gNai_Type()
)
c3gNai.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gNai.setStatus("current")


class _C3gAaaPassword_Type(DisplayString):
    """Custom type c3gAaaPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gAaaPassword_Type.__name__ = "DisplayString"
_C3gAaaPassword_Object = MibTableColumn
c3gAaaPassword = _C3gAaaPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 3),
    _C3gAaaPassword_Type()
)
c3gAaaPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gAaaPassword.setStatus("current")


class _C3gMnHaSs_Type(Integer32):
    """Custom type c3gMnHaSs based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSet", 2),
          ("set", 1))
    )


_C3gMnHaSs_Type.__name__ = "Integer32"
_C3gMnHaSs_Object = MibTableColumn
c3gMnHaSs = _C3gMnHaSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 4),
    _C3gMnHaSs_Type()
)
c3gMnHaSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gMnHaSs.setStatus("current")
_C3gMnHaSpi_Type = Unsigned32
_C3gMnHaSpi_Object = MibTableColumn
c3gMnHaSpi = _C3gMnHaSpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 5),
    _C3gMnHaSpi_Type()
)
c3gMnHaSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gMnHaSpi.setStatus("current")


class _C3gMnAaaSs_Type(Integer32):
    """Custom type c3gMnAaaSs based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSet", 2),
          ("set", 1))
    )


_C3gMnAaaSs_Type.__name__ = "Integer32"
_C3gMnAaaSs_Object = MibTableColumn
c3gMnAaaSs = _C3gMnAaaSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 6),
    _C3gMnAaaSs_Type()
)
c3gMnAaaSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gMnAaaSs.setStatus("current")
_C3gMnAaaSpi_Type = Unsigned32
_C3gMnAaaSpi_Object = MibTableColumn
c3gMnAaaSpi = _C3gMnAaaSpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 7),
    _C3gMnAaaSpi_Type()
)
c3gMnAaaSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gMnAaaSpi.setStatus("current")


class _C3gReverseTunnelPreference_Type(Integer32):
    """Custom type c3gReverseTunnelPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSet", 2),
          ("set", 1))
    )


_C3gReverseTunnelPreference_Type.__name__ = "Integer32"
_C3gReverseTunnelPreference_Object = MibTableColumn
c3gReverseTunnelPreference = _C3gReverseTunnelPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 8),
    _C3gReverseTunnelPreference_Type()
)
c3gReverseTunnelPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gReverseTunnelPreference.setStatus("current")
_C3gHomeAddrType_Type = InetAddressType
_C3gHomeAddrType_Object = MibTableColumn
c3gHomeAddrType = _C3gHomeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 9),
    _C3gHomeAddrType_Type()
)
c3gHomeAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gHomeAddrType.setStatus("current")
_C3gHomeAddr_Type = InetAddress
_C3gHomeAddr_Object = MibTableColumn
c3gHomeAddr = _C3gHomeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 10),
    _C3gHomeAddr_Type()
)
c3gHomeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gHomeAddr.setStatus("current")
_C3gPriHaAddrType_Type = InetAddressType
_C3gPriHaAddrType_Object = MibTableColumn
c3gPriHaAddrType = _C3gPriHaAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 11),
    _C3gPriHaAddrType_Type()
)
c3gPriHaAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gPriHaAddrType.setStatus("current")
_C3gPriHaAddr_Type = InetAddress
_C3gPriHaAddr_Object = MibTableColumn
c3gPriHaAddr = _C3gPriHaAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 12),
    _C3gPriHaAddr_Type()
)
c3gPriHaAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gPriHaAddr.setStatus("current")
_C3gSecHaAddrType_Type = InetAddressType
_C3gSecHaAddrType_Object = MibTableColumn
c3gSecHaAddrType = _C3gSecHaAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 13),
    _C3gSecHaAddrType_Type()
)
c3gSecHaAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gSecHaAddrType.setStatus("current")
_C3gSecHaAddr_Type = InetAddress
_C3gSecHaAddr_Object = MibTableColumn
c3gSecHaAddr = _C3gSecHaAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 5, 2, 1, 14),
    _C3gSecHaAddr_Type()
)
c3gSecHaAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gSecHaAddr.setStatus("current")
_C3gCdmaRadio_ObjectIdentity = ObjectIdentity
c3gCdmaRadio = _C3gCdmaRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6)
)
_C3gCdma1xRttRadioTable_Object = MibTable
c3gCdma1xRttRadioTable = _C3gCdma1xRttRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    c3gCdma1xRttRadioTable.setStatus("current")
_C3gCdma1xRttRadioEntry_Object = MibTableRow
c3gCdma1xRttRadioEntry = _C3gCdma1xRttRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 1, 1)
)
c3gCdma1xRttRadioEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gCdma1xRttRadioEntry.setStatus("current")
_C3gCurrent1xRttRssi_Type = C3gRssi
_C3gCurrent1xRttRssi_Object = MibTableColumn
c3gCurrent1xRttRssi = _C3gCurrent1xRttRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 1, 1, 1),
    _C3gCurrent1xRttRssi_Type()
)
c3gCurrent1xRttRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCurrent1xRttRssi.setStatus("current")
_C3gCurrent1xRttEcIo_Type = C3gEcIo
_C3gCurrent1xRttEcIo_Object = MibTableColumn
c3gCurrent1xRttEcIo = _C3gCurrent1xRttEcIo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 1, 1, 2),
    _C3gCurrent1xRttEcIo_Type()
)
c3gCurrent1xRttEcIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCurrent1xRttEcIo.setStatus("current")
_C3gCurrent1xRttChannelNumber_Type = Integer32
_C3gCurrent1xRttChannelNumber_Object = MibTableColumn
c3gCurrent1xRttChannelNumber = _C3gCurrent1xRttChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 1, 1, 3),
    _C3gCurrent1xRttChannelNumber_Type()
)
c3gCurrent1xRttChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCurrent1xRttChannelNumber.setStatus("current")


class _C3gCurrent1xRttChannelState_Type(Integer32):
    """Custom type c3gCurrent1xRttChannelState based on Integer32"""
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
        *(("acquired", 3),
          ("notAcquired", 2),
          ("scanning", 4),
          ("unknown", 1))
    )


_C3gCurrent1xRttChannelState_Type.__name__ = "Integer32"
_C3gCurrent1xRttChannelState_Object = MibTableColumn
c3gCurrent1xRttChannelState = _C3gCurrent1xRttChannelState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 1, 1, 4),
    _C3gCurrent1xRttChannelState_Type()
)
c3gCurrent1xRttChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCurrent1xRttChannelState.setStatus("current")
_C3gCdma1xRttBandClassTable_Object = MibTable
c3gCdma1xRttBandClassTable = _C3gCdma1xRttBandClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    c3gCdma1xRttBandClassTable.setStatus("current")
_C3gCdma1xRttBandClassEntry_Object = MibTableRow
c3gCdma1xRttBandClassEntry = _C3gCdma1xRttBandClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 2, 1)
)
c3gCdma1xRttBandClassEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gBandClassIndex"),
)
if mibBuilder.loadTexts:
    c3gCdma1xRttBandClassEntry.setStatus("current")


class _C3gBandClassIndex_Type(Integer32):
    """Custom type c3gBandClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_C3gBandClassIndex_Type.__name__ = "Integer32"
_C3gBandClassIndex_Object = MibTableColumn
c3gBandClassIndex = _C3gBandClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 2, 1, 1),
    _C3gBandClassIndex_Type()
)
c3gBandClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c3gBandClassIndex.setStatus("current")
_C3g1xRttBandClass_Type = Unsigned32
_C3g1xRttBandClass_Object = MibTableColumn
c3g1xRttBandClass = _C3g1xRttBandClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 2, 1, 2),
    _C3g1xRttBandClass_Type()
)
c3g1xRttBandClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3g1xRttBandClass.setStatus("current")
_C3gCdmaEvDoRadioTable_Object = MibTable
c3gCdmaEvDoRadioTable = _C3gCdmaEvDoRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    c3gCdmaEvDoRadioTable.setStatus("current")
_C3gCdmaEvDoRadioEntry_Object = MibTableRow
c3gCdmaEvDoRadioEntry = _C3gCdmaEvDoRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1)
)
c3gCdmaEvDoRadioEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gCdmaEvDoRadioEntry.setStatus("current")
_C3gCurrentEvDoRssi_Type = C3gRssi
_C3gCurrentEvDoRssi_Object = MibTableColumn
c3gCurrentEvDoRssi = _C3gCurrentEvDoRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1, 1),
    _C3gCurrentEvDoRssi_Type()
)
c3gCurrentEvDoRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCurrentEvDoRssi.setStatus("current")
_C3gCurrentEvDoEcIo_Type = C3gEcIo
_C3gCurrentEvDoEcIo_Object = MibTableColumn
c3gCurrentEvDoEcIo = _C3gCurrentEvDoEcIo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1, 2),
    _C3gCurrentEvDoEcIo_Type()
)
c3gCurrentEvDoEcIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCurrentEvDoEcIo.setStatus("current")
_C3gCurrentEvDoChannelNumber_Type = Integer32
_C3gCurrentEvDoChannelNumber_Object = MibTableColumn
c3gCurrentEvDoChannelNumber = _C3gCurrentEvDoChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1, 3),
    _C3gCurrentEvDoChannelNumber_Type()
)
c3gCurrentEvDoChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCurrentEvDoChannelNumber.setStatus("current")


class _C3gSectorId_Type(DisplayString):
    """Custom type c3gSectorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gSectorId_Type.__name__ = "DisplayString"
_C3gSectorId_Object = MibTableColumn
c3gSectorId = _C3gSectorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1, 4),
    _C3gSectorId_Type()
)
c3gSectorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSectorId.setStatus("current")
_C3gSubnetMask_Type = Unsigned32
_C3gSubnetMask_Object = MibTableColumn
c3gSubnetMask = _C3gSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1, 5),
    _C3gSubnetMask_Type()
)
c3gSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSubnetMask.setStatus("current")
_C3gHdrColorCode_Type = Unsigned32
_C3gHdrColorCode_Object = MibTableColumn
c3gHdrColorCode = _C3gHdrColorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1, 6),
    _C3gHdrColorCode_Type()
)
c3gHdrColorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gHdrColorCode.setStatus("current")
_C3gPnOffset_Type = Unsigned32
_C3gPnOffset_Object = MibTableColumn
c3gPnOffset = _C3gPnOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1, 7),
    _C3gPnOffset_Type()
)
c3gPnOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gPnOffset.setStatus("current")
_C3gRxMainGainControl_Type = Integer32
_C3gRxMainGainControl_Object = MibTableColumn
c3gRxMainGainControl = _C3gRxMainGainControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1, 8),
    _C3gRxMainGainControl_Type()
)
c3gRxMainGainControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gRxMainGainControl.setStatus("current")
if mibBuilder.loadTexts:
    c3gRxMainGainControl.setUnits("dBm")
_C3gRxDiversityGainControl_Type = Integer32
_C3gRxDiversityGainControl_Object = MibTableColumn
c3gRxDiversityGainControl = _C3gRxDiversityGainControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1, 9),
    _C3gRxDiversityGainControl_Type()
)
c3gRxDiversityGainControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gRxDiversityGainControl.setStatus("current")
if mibBuilder.loadTexts:
    c3gRxDiversityGainControl.setUnits("dBm")
_C3gTxTotalPower_Type = Integer32
_C3gTxTotalPower_Object = MibTableColumn
c3gTxTotalPower = _C3gTxTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1, 10),
    _C3gTxTotalPower_Type()
)
c3gTxTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gTxTotalPower.setStatus("current")
if mibBuilder.loadTexts:
    c3gTxTotalPower.setUnits("dBm")
_C3gTxGainAdjust_Type = Integer32
_C3gTxGainAdjust_Object = MibTableColumn
c3gTxGainAdjust = _C3gTxGainAdjust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1, 11),
    _C3gTxGainAdjust_Type()
)
c3gTxGainAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gTxGainAdjust.setStatus("current")
if mibBuilder.loadTexts:
    c3gTxGainAdjust.setUnits("dBm")
_C3gCarrierToInterferenceRatio_Type = Unsigned32
_C3gCarrierToInterferenceRatio_Object = MibTableColumn
c3gCarrierToInterferenceRatio = _C3gCarrierToInterferenceRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 3, 1, 12),
    _C3gCarrierToInterferenceRatio_Type()
)
c3gCarrierToInterferenceRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCarrierToInterferenceRatio.setStatus("current")
_C3gCdmaEvDoBandClassTable_Object = MibTable
c3gCdmaEvDoBandClassTable = _C3gCdmaEvDoBandClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    c3gCdmaEvDoBandClassTable.setStatus("current")
_C3gCdmaEvDoBandClassEntry_Object = MibTableRow
c3gCdmaEvDoBandClassEntry = _C3gCdmaEvDoBandClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 4, 1)
)
c3gCdmaEvDoBandClassEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gBandClassIndex"),
)
if mibBuilder.loadTexts:
    c3gCdmaEvDoBandClassEntry.setStatus("current")
_C3gEvDoBandClass_Type = Unsigned32
_C3gEvDoBandClass_Object = MibTableColumn
c3gEvDoBandClass = _C3gEvDoBandClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 4, 1, 1),
    _C3gEvDoBandClass_Type()
)
c3gEvDoBandClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gEvDoBandClass.setStatus("current")
_C3gCdmaHistoryTable_Object = MibTable
c3gCdmaHistoryTable = _C3gCdmaHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 5)
)
if mibBuilder.loadTexts:
    c3gCdmaHistoryTable.setStatus("current")
_C3gCdmaHistoryEntry_Object = MibTableRow
c3gCdmaHistoryEntry = _C3gCdmaHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 5, 1)
)
c3gCdmaHistoryEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gCdmaHistoryEntry.setStatus("current")


class _C3gCdmaHistory1xRttRssiPerSecond_Type(OctetString):
    """Custom type c3gCdmaHistory1xRttRssiPerSecond based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_C3gCdmaHistory1xRttRssiPerSecond_Type.__name__ = "OctetString"
_C3gCdmaHistory1xRttRssiPerSecond_Object = MibTableColumn
c3gCdmaHistory1xRttRssiPerSecond = _C3gCdmaHistory1xRttRssiPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 5, 1, 1),
    _C3gCdmaHistory1xRttRssiPerSecond_Type()
)
c3gCdmaHistory1xRttRssiPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaHistory1xRttRssiPerSecond.setStatus("current")
if mibBuilder.loadTexts:
    c3gCdmaHistory1xRttRssiPerSecond.setUnits("-dBm")


class _C3gCdmaHistory1xRttRssiPerMinute_Type(OctetString):
    """Custom type c3gCdmaHistory1xRttRssiPerMinute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_C3gCdmaHistory1xRttRssiPerMinute_Type.__name__ = "OctetString"
_C3gCdmaHistory1xRttRssiPerMinute_Object = MibTableColumn
c3gCdmaHistory1xRttRssiPerMinute = _C3gCdmaHistory1xRttRssiPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 5, 1, 2),
    _C3gCdmaHistory1xRttRssiPerMinute_Type()
)
c3gCdmaHistory1xRttRssiPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaHistory1xRttRssiPerMinute.setStatus("current")
if mibBuilder.loadTexts:
    c3gCdmaHistory1xRttRssiPerMinute.setUnits("-dBm")


class _C3gCdmaHistory1xRttRssiPerHour_Type(OctetString):
    """Custom type c3gCdmaHistory1xRttRssiPerHour based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(72, 72),
    )


_C3gCdmaHistory1xRttRssiPerHour_Type.__name__ = "OctetString"
_C3gCdmaHistory1xRttRssiPerHour_Object = MibTableColumn
c3gCdmaHistory1xRttRssiPerHour = _C3gCdmaHistory1xRttRssiPerHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 5, 1, 3),
    _C3gCdmaHistory1xRttRssiPerHour_Type()
)
c3gCdmaHistory1xRttRssiPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaHistory1xRttRssiPerHour.setStatus("current")
if mibBuilder.loadTexts:
    c3gCdmaHistory1xRttRssiPerHour.setUnits("-dBm")


class _C3gCdmaHistoryEvDoRssiPerSecond_Type(OctetString):
    """Custom type c3gCdmaHistoryEvDoRssiPerSecond based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_C3gCdmaHistoryEvDoRssiPerSecond_Type.__name__ = "OctetString"
_C3gCdmaHistoryEvDoRssiPerSecond_Object = MibTableColumn
c3gCdmaHistoryEvDoRssiPerSecond = _C3gCdmaHistoryEvDoRssiPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 5, 1, 4),
    _C3gCdmaHistoryEvDoRssiPerSecond_Type()
)
c3gCdmaHistoryEvDoRssiPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaHistoryEvDoRssiPerSecond.setStatus("current")
if mibBuilder.loadTexts:
    c3gCdmaHistoryEvDoRssiPerSecond.setUnits("-dBm")


class _C3gCdmaHistoryEvDoRssiPerMinute_Type(OctetString):
    """Custom type c3gCdmaHistoryEvDoRssiPerMinute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_C3gCdmaHistoryEvDoRssiPerMinute_Type.__name__ = "OctetString"
_C3gCdmaHistoryEvDoRssiPerMinute_Object = MibTableColumn
c3gCdmaHistoryEvDoRssiPerMinute = _C3gCdmaHistoryEvDoRssiPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 5, 1, 5),
    _C3gCdmaHistoryEvDoRssiPerMinute_Type()
)
c3gCdmaHistoryEvDoRssiPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaHistoryEvDoRssiPerMinute.setStatus("current")
if mibBuilder.loadTexts:
    c3gCdmaHistoryEvDoRssiPerMinute.setUnits("-dBm")


class _C3gCdmaHistoryEvDoRssiPerHour_Type(OctetString):
    """Custom type c3gCdmaHistoryEvDoRssiPerHour based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(72, 72),
    )


_C3gCdmaHistoryEvDoRssiPerHour_Type.__name__ = "OctetString"
_C3gCdmaHistoryEvDoRssiPerHour_Object = MibTableColumn
c3gCdmaHistoryEvDoRssiPerHour = _C3gCdmaHistoryEvDoRssiPerHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 6, 5, 1, 6),
    _C3gCdmaHistoryEvDoRssiPerHour_Type()
)
c3gCdmaHistoryEvDoRssiPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCdmaHistoryEvDoRssiPerHour.setStatus("current")
if mibBuilder.loadTexts:
    c3gCdmaHistoryEvDoRssiPerHour.setUnits("-dBm")
_C3gCdmaSecurity_ObjectIdentity = ObjectIdentity
c3gCdmaSecurity = _C3gCdmaSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 7)
)
_C3gCdmaSecurityTable_Object = MibTable
c3gCdmaSecurityTable = _C3gCdmaSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    c3gCdmaSecurityTable.setStatus("current")
_C3gCdmaSecurityEntry_Object = MibTableRow
c3gCdmaSecurityEntry = _C3gCdmaSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 7, 1, 1)
)
c3gCdmaSecurityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gCdmaSecurityEntry.setStatus("current")


class _C3gCdmaPinSecurityStatus_Type(Integer32):
    """Custom type c3gCdmaPinSecurityStatus based on Integer32"""
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
        *(("locked", 2),
          ("unknown", 1),
          ("unlocked", 3))
    )


_C3gCdmaPinSecurityStatus_Type.__name__ = "Integer32"
_C3gCdmaPinSecurityStatus_Object = MibTableColumn
c3gCdmaPinSecurityStatus = _C3gCdmaPinSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 7, 1, 1, 1),
    _C3gCdmaPinSecurityStatus_Type()
)
c3gCdmaPinSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gCdmaPinSecurityStatus.setStatus("current")


class _C3gCdmaPowerUpLockStatus_Type(Integer32):
    """Custom type c3gCdmaPowerUpLockStatus based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 2),
          ("unknown", 1))
    )


_C3gCdmaPowerUpLockStatus_Type.__name__ = "Integer32"
_C3gCdmaPowerUpLockStatus_Object = MibTableColumn
c3gCdmaPowerUpLockStatus = _C3gCdmaPowerUpLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 2, 7, 1, 1, 2),
    _C3gCdmaPowerUpLockStatus_Type()
)
c3gCdmaPowerUpLockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gCdmaPowerUpLockStatus.setStatus("current")
_C3gWanGsm_ObjectIdentity = ObjectIdentity
c3gWanGsm = _C3gWanGsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3)
)
_C3gGsmIdentityTable_Object = MibTable
c3gGsmIdentityTable = _C3gGsmIdentityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 1)
)
if mibBuilder.loadTexts:
    c3gGsmIdentityTable.setStatus("current")
_C3gGsmIdentityEntry_Object = MibTableRow
c3gGsmIdentityEntry = _C3gGsmIdentityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 1, 1)
)
c3gGsmIdentityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmIdentityEntry.setStatus("current")


class _C3gImsi_Type(DisplayString):
    """Custom type c3gImsi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gImsi_Type.__name__ = "DisplayString"
_C3gImsi_Object = MibTableColumn
c3gImsi = _C3gImsi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 1, 1, 1),
    _C3gImsi_Type()
)
c3gImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gImsi.setStatus("current")


class _C3gImei_Type(DisplayString):
    """Custom type c3gImei based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gImei_Type.__name__ = "DisplayString"
_C3gImei_Object = MibTableColumn
c3gImei = _C3gImei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 1, 1, 2),
    _C3gImei_Type()
)
c3gImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gImei.setStatus("current")


class _C3gIccId_Type(DisplayString):
    """Custom type c3gIccId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gIccId_Type.__name__ = "DisplayString"
_C3gIccId_Object = MibTableColumn
c3gIccId = _C3gIccId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 1, 1, 3),
    _C3gIccId_Type()
)
c3gIccId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gIccId.setStatus("current")


class _C3gMsisdn_Type(DisplayString):
    """Custom type c3gMsisdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gMsisdn_Type.__name__ = "DisplayString"
_C3gMsisdn_Object = MibTableColumn
c3gMsisdn = _C3gMsisdn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 1, 1, 4),
    _C3gMsisdn_Type()
)
c3gMsisdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gMsisdn.setStatus("current")


class _C3gFsn_Type(DisplayString):
    """Custom type c3gFsn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gFsn_Type.__name__ = "DisplayString"
_C3gFsn_Object = MibTableColumn
c3gFsn = _C3gFsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 1, 1, 5),
    _C3gFsn_Type()
)
c3gFsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gFsn.setStatus("current")


class _C3gModemStatus_Type(Integer32):
    """Custom type c3gModemStatus based on Integer32"""
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
        *(("lowPowerMode", 4),
          ("offLine", 2),
          ("onLine", 3),
          ("unknown", 1))
    )


_C3gModemStatus_Type.__name__ = "Integer32"
_C3gModemStatus_Object = MibTableColumn
c3gModemStatus = _C3gModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 1, 1, 6),
    _C3gModemStatus_Type()
)
c3gModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gModemStatus.setStatus("current")


class _C3gGsmRoamingPreference_Type(Integer32):
    """Custom type c3gGsmRoamingPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("home", 2),
          ("roaming", 3),
          ("unknown", 1))
    )


_C3gGsmRoamingPreference_Type.__name__ = "Integer32"
_C3gGsmRoamingPreference_Object = MibTableColumn
c3gGsmRoamingPreference = _C3gGsmRoamingPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 1, 1, 7),
    _C3gGsmRoamingPreference_Type()
)
c3gGsmRoamingPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gGsmRoamingPreference.setStatus("current")
_C3gGsmNetworkTable_Object = MibTable
c3gGsmNetworkTable = _C3gGsmNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2)
)
if mibBuilder.loadTexts:
    c3gGsmNetworkTable.setStatus("current")
_C3gGsmNetworkEntry_Object = MibTableRow
c3gGsmNetworkEntry = _C3gGsmNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1)
)
c3gGsmNetworkEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmNetworkEntry.setStatus("current")


class _C3gGsmLac_Type(Unsigned32):
    """Custom type c3gGsmLac based on Unsigned32"""
    defaultValue = 0


_C3gGsmLac_Object = MibTableColumn
c3gGsmLac = _C3gGsmLac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 1),
    _C3gGsmLac_Type()
)
c3gGsmLac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmLac.setStatus("current")


class _C3gGsmCurrentServiceStatus_Type(Integer32):
    """Custom type c3gGsmCurrentServiceStatus based on Integer32"""
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
        *(("emergencyOnly", 4),
          ("noService", 2),
          ("normal", 3),
          ("unknown", 1))
    )


_C3gGsmCurrentServiceStatus_Type.__name__ = "Integer32"
_C3gGsmCurrentServiceStatus_Object = MibTableColumn
c3gGsmCurrentServiceStatus = _C3gGsmCurrentServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 2),
    _C3gGsmCurrentServiceStatus_Type()
)
c3gGsmCurrentServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmCurrentServiceStatus.setStatus("current")


class _C3gGsmCurrentServiceError_Type(Integer32):
    """Custom type c3gGsmCurrentServiceError based on Integer32"""
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("callCannotIdentified", 26),
          ("congestion", 21),
          ("gprsNonGprsServNotAllow", 9),
          ("gprsServNotAllowInPlmn", 15),
          ("gprsServNotAllowed", 8),
          ("gsmAuthenNotAccept", 22),
          ("illegalMe", 7),
          ("illegalMs", 4),
          ("imeiNotAccepted", 6),
          ("implicitlyDetached", 11),
          ("imsiUnknownInHlr", 3),
          ("imsiUnknownInVlr", 5),
          ("invalidMandatInfo", 28),
          ("lacNotAllowed", 13),
          ("macFailure", 19),
          ("msIdentUnknown", 10),
          ("mscTempNotReachable", 17),
          ("networkFailure", 18),
          ("noPdpContextActivated", 27),
          ("noSuitableCellInLa", 16),
          ("none", 2),
          ("plmnNotAllowed", 12),
          ("reqServOptionNotSub", 24),
          ("roamingNotAllowed", 14),
          ("servOptionNotSupport", 23),
          ("servOptionOutOfOrder", 25),
          ("synchFailure", 20),
          ("unknown", 1),
          ("unpsecProtErr", 29))
    )


_C3gGsmCurrentServiceError_Type.__name__ = "Integer32"
_C3gGsmCurrentServiceError_Object = MibTableColumn
c3gGsmCurrentServiceError = _C3gGsmCurrentServiceError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 3),
    _C3gGsmCurrentServiceError_Type()
)
c3gGsmCurrentServiceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmCurrentServiceError.setStatus("current")


class _C3gGsmCurrentService_Type(Integer32):
    """Custom type c3gGsmCurrentService based on Integer32"""
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
        *(("circuitSwitched", 3),
          ("combined", 5),
          ("invalid", 2),
          ("packetSwitched", 4),
          ("unknown", 1))
    )


_C3gGsmCurrentService_Type.__name__ = "Integer32"
_C3gGsmCurrentService_Object = MibTableColumn
c3gGsmCurrentService = _C3gGsmCurrentService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 4),
    _C3gGsmCurrentService_Type()
)
c3gGsmCurrentService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmCurrentService.setStatus("current")


class _C3gGsmPacketService_Type(Integer32):
    """Custom type c3gGsmPacketService based on Integer32"""
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
        *(("edge", 4),
          ("gprs", 3),
          ("hsdpa", 6),
          ("hspa", 8),
          ("hspaPlus", 9),
          ("hsupa", 7),
          ("lte", 10),
          ("none", 2),
          ("umtsWcdma", 5),
          ("unknown", 1))
    )


_C3gGsmPacketService_Type.__name__ = "Integer32"
_C3gGsmPacketService_Object = MibTableColumn
c3gGsmPacketService = _C3gGsmPacketService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 5),
    _C3gGsmPacketService_Type()
)
c3gGsmPacketService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmPacketService.setStatus("current")


class _C3gGsmCurrentRoamingStatus_Type(Integer32):
    """Custom type c3gGsmCurrentRoamingStatus based on Integer32"""
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
        *(("home", 3),
          ("roaming", 2),
          ("unknown", 1))
    )


_C3gGsmCurrentRoamingStatus_Type.__name__ = "Integer32"
_C3gGsmCurrentRoamingStatus_Object = MibTableColumn
c3gGsmCurrentRoamingStatus = _C3gGsmCurrentRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 6),
    _C3gGsmCurrentRoamingStatus_Type()
)
c3gGsmCurrentRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmCurrentRoamingStatus.setStatus("current")


class _C3gGsmNetworkSelectionMode_Type(Integer32):
    """Custom type c3gGsmNetworkSelectionMode based on Integer32"""
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
        *(("automatic", 2),
          ("manual", 3),
          ("unknown", 1))
    )


_C3gGsmNetworkSelectionMode_Type.__name__ = "Integer32"
_C3gGsmNetworkSelectionMode_Object = MibTableColumn
c3gGsmNetworkSelectionMode = _C3gGsmNetworkSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 7),
    _C3gGsmNetworkSelectionMode_Type()
)
c3gGsmNetworkSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gGsmNetworkSelectionMode.setStatus("current")


class _C3gGsmCountry_Type(DisplayString):
    """Custom type c3gGsmCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gGsmCountry_Type.__name__ = "DisplayString"
_C3gGsmCountry_Object = MibTableColumn
c3gGsmCountry = _C3gGsmCountry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 8),
    _C3gGsmCountry_Type()
)
c3gGsmCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmCountry.setStatus("current")


class _C3gGsmNetwork_Type(DisplayString):
    """Custom type c3gGsmNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gGsmNetwork_Type.__name__ = "DisplayString"
_C3gGsmNetwork_Object = MibTableColumn
c3gGsmNetwork = _C3gGsmNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 9),
    _C3gGsmNetwork_Type()
)
c3gGsmNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNetwork.setStatus("current")


class _C3gGsmMcc_Type(Integer32):
    """Custom type c3gGsmMcc based on Integer32"""
    defaultValue = 0


_C3gGsmMcc_Object = MibTableColumn
c3gGsmMcc = _C3gGsmMcc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 10),
    _C3gGsmMcc_Type()
)
c3gGsmMcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gGsmMcc.setStatus("current")


class _C3gGsmMnc_Type(Integer32):
    """Custom type c3gGsmMnc based on Integer32"""
    defaultValue = 0


_C3gGsmMnc_Object = MibTableColumn
c3gGsmMnc = _C3gGsmMnc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 11),
    _C3gGsmMnc_Type()
)
c3gGsmMnc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gGsmMnc.setStatus("current")


class _C3gGsmRac_Type(Unsigned32):
    """Custom type c3gGsmRac based on Unsigned32"""
    defaultValue = 0


_C3gGsmRac_Object = MibTableColumn
c3gGsmRac = _C3gGsmRac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 12),
    _C3gGsmRac_Type()
)
c3gGsmRac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmRac.setStatus("current")


class _C3gGsmCurrentCellId_Type(Unsigned32):
    """Custom type c3gGsmCurrentCellId based on Unsigned32"""
    defaultValue = 0


_C3gGsmCurrentCellId_Object = MibTableColumn
c3gGsmCurrentCellId = _C3gGsmCurrentCellId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 13),
    _C3gGsmCurrentCellId_Type()
)
c3gGsmCurrentCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmCurrentCellId.setStatus("current")


class _C3gGsmCurrentPrimaryScramblingCode_Type(Unsigned32):
    """Custom type c3gGsmCurrentPrimaryScramblingCode based on Unsigned32"""
    defaultValue = 0


_C3gGsmCurrentPrimaryScramblingCode_Object = MibTableColumn
c3gGsmCurrentPrimaryScramblingCode = _C3gGsmCurrentPrimaryScramblingCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 14),
    _C3gGsmCurrentPrimaryScramblingCode_Type()
)
c3gGsmCurrentPrimaryScramblingCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmCurrentPrimaryScramblingCode.setStatus("current")


class _C3gGsmPlmnSelection_Type(Integer32):
    """Custom type c3gGsmPlmnSelection based on Integer32"""
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
        *(("automatic", 3),
          ("manual", 2),
          ("unknown", 1))
    )


_C3gGsmPlmnSelection_Type.__name__ = "Integer32"
_C3gGsmPlmnSelection_Object = MibTableColumn
c3gGsmPlmnSelection = _C3gGsmPlmnSelection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 15),
    _C3gGsmPlmnSelection_Type()
)
c3gGsmPlmnSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gGsmPlmnSelection.setStatus("current")


class _C3gGsmRegPlmn_Type(DisplayString):
    """Custom type c3gGsmRegPlmn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gGsmRegPlmn_Type.__name__ = "DisplayString"
_C3gGsmRegPlmn_Object = MibTableColumn
c3gGsmRegPlmn = _C3gGsmRegPlmn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 16),
    _C3gGsmRegPlmn_Type()
)
c3gGsmRegPlmn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmRegPlmn.setStatus("current")


class _C3gGsmPlmnAbbr_Type(DisplayString):
    """Custom type c3gGsmPlmnAbbr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gGsmPlmnAbbr_Type.__name__ = "DisplayString"
_C3gGsmPlmnAbbr_Object = MibTableColumn
c3gGsmPlmnAbbr = _C3gGsmPlmnAbbr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 17),
    _C3gGsmPlmnAbbr_Type()
)
c3gGsmPlmnAbbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmPlmnAbbr.setStatus("current")


class _C3gGsmServiceProvider_Type(DisplayString):
    """Custom type c3gGsmServiceProvider based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gGsmServiceProvider_Type.__name__ = "DisplayString"
_C3gGsmServiceProvider_Object = MibTableColumn
c3gGsmServiceProvider = _C3gGsmServiceProvider_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 18),
    _C3gGsmServiceProvider_Type()
)
c3gGsmServiceProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmServiceProvider.setStatus("current")
_C3gGsmTotalByteTransmitted_Type = Counter64
_C3gGsmTotalByteTransmitted_Object = MibTableColumn
c3gGsmTotalByteTransmitted = _C3gGsmTotalByteTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 19),
    _C3gGsmTotalByteTransmitted_Type()
)
c3gGsmTotalByteTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmTotalByteTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmTotalByteTransmitted.setUnits("bytes")
_C3gGsmTotalByteReceived_Type = Counter64
_C3gGsmTotalByteReceived_Object = MibTableColumn
c3gGsmTotalByteReceived = _C3gGsmTotalByteReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 2, 1, 20),
    _C3gGsmTotalByteReceived_Type()
)
c3gGsmTotalByteReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmTotalByteReceived.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmTotalByteReceived.setUnits("bytes")
_C3gGsmPdpProfile_ObjectIdentity = ObjectIdentity
c3gGsmPdpProfile = _C3gGsmPdpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3)
)
_C3gGsmPdpProfileTable_Object = MibTable
c3gGsmPdpProfileTable = _C3gGsmPdpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    c3gGsmPdpProfileTable.setStatus("current")
_C3gGsmPdpProfileEntry_Object = MibTableRow
c3gGsmPdpProfileEntry = _C3gGsmPdpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 1, 1)
)
c3gGsmPdpProfileEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gGsmPdpProfileIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmPdpProfileEntry.setStatus("current")


class _C3gGsmPdpProfileIndex_Type(Integer32):
    """Custom type c3gGsmPdpProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_C3gGsmPdpProfileIndex_Type.__name__ = "Integer32"
_C3gGsmPdpProfileIndex_Object = MibTableColumn
c3gGsmPdpProfileIndex = _C3gGsmPdpProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 1, 1, 1),
    _C3gGsmPdpProfileIndex_Type()
)
c3gGsmPdpProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c3gGsmPdpProfileIndex.setStatus("current")


class _C3gGsmPdpProfileType_Type(C3gPdpType):
    """Custom type c3gGsmPdpProfileType based on C3gPdpType"""


_C3gGsmPdpProfileType_Object = MibTableColumn
c3gGsmPdpProfileType = _C3gGsmPdpProfileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 1, 1, 2),
    _C3gGsmPdpProfileType_Type()
)
c3gGsmPdpProfileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmPdpProfileType.setStatus("current")


class _C3gGsmPdpProfileAddr_Type(DisplayString):
    """Custom type c3gGsmPdpProfileAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gGsmPdpProfileAddr_Type.__name__ = "DisplayString"
_C3gGsmPdpProfileAddr_Object = MibTableColumn
c3gGsmPdpProfileAddr = _C3gGsmPdpProfileAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 1, 1, 3),
    _C3gGsmPdpProfileAddr_Type()
)
c3gGsmPdpProfileAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmPdpProfileAddr.setStatus("current")


class _C3gGsmPdpProfileApn_Type(DisplayString):
    """Custom type c3gGsmPdpProfileApn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gGsmPdpProfileApn_Type.__name__ = "DisplayString"
_C3gGsmPdpProfileApn_Object = MibTableColumn
c3gGsmPdpProfileApn = _C3gGsmPdpProfileApn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 1, 1, 4),
    _C3gGsmPdpProfileApn_Type()
)
c3gGsmPdpProfileApn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmPdpProfileApn.setStatus("current")


class _C3gGsmPdpProfileAuthenType_Type(Integer32):
    """Custom type c3gGsmPdpProfileAuthenType based on Integer32"""
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
        *(("chap", 3),
          ("none", 2),
          ("pap", 4),
          ("unknown", 1))
    )


_C3gGsmPdpProfileAuthenType_Type.__name__ = "Integer32"
_C3gGsmPdpProfileAuthenType_Object = MibTableColumn
c3gGsmPdpProfileAuthenType = _C3gGsmPdpProfileAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 1, 1, 5),
    _C3gGsmPdpProfileAuthenType_Type()
)
c3gGsmPdpProfileAuthenType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmPdpProfileAuthenType.setStatus("current")


class _C3gGsmPdpProfileUsername_Type(DisplayString):
    """Custom type c3gGsmPdpProfileUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gGsmPdpProfileUsername_Type.__name__ = "DisplayString"
_C3gGsmPdpProfileUsername_Object = MibTableColumn
c3gGsmPdpProfileUsername = _C3gGsmPdpProfileUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 1, 1, 6),
    _C3gGsmPdpProfileUsername_Type()
)
c3gGsmPdpProfileUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmPdpProfileUsername.setStatus("current")


class _C3gGsmPdpProfilePassword_Type(DisplayString):
    """Custom type c3gGsmPdpProfilePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gGsmPdpProfilePassword_Type.__name__ = "DisplayString"
_C3gGsmPdpProfilePassword_Object = MibTableColumn
c3gGsmPdpProfilePassword = _C3gGsmPdpProfilePassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 1, 1, 7),
    _C3gGsmPdpProfilePassword_Type()
)
c3gGsmPdpProfilePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmPdpProfilePassword.setStatus("current")
_C3gGsmPdpProfileRowStatus_Type = RowStatus
_C3gGsmPdpProfileRowStatus_Object = MibTableColumn
c3gGsmPdpProfileRowStatus = _C3gGsmPdpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 1, 1, 8),
    _C3gGsmPdpProfileRowStatus_Type()
)
c3gGsmPdpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmPdpProfileRowStatus.setStatus("current")
_C3gGsmPacketSessionTable_Object = MibTable
c3gGsmPacketSessionTable = _C3gGsmPacketSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    c3gGsmPacketSessionTable.setStatus("current")
_C3gGsmPacketSessionEntry_Object = MibTableRow
c3gGsmPacketSessionEntry = _C3gGsmPacketSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 2, 1)
)
c3gGsmPacketSessionEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gGsmPdpProfileIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmPacketSessionEntry.setStatus("current")


class _C3gGsmPacketSessionStatus_Type(Integer32):
    """Custom type c3gGsmPacketSessionStatus based on Integer32"""
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
        *(("active", 2),
          ("inactive", 3),
          ("unknown", 1))
    )


_C3gGsmPacketSessionStatus_Type.__name__ = "Integer32"
_C3gGsmPacketSessionStatus_Object = MibTableColumn
c3gGsmPacketSessionStatus = _C3gGsmPacketSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 2, 1, 1),
    _C3gGsmPacketSessionStatus_Type()
)
c3gGsmPacketSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmPacketSessionStatus.setStatus("current")
_C3gGsmPdpType_Type = C3gPdpType
_C3gGsmPdpType_Object = MibTableColumn
c3gGsmPdpType = _C3gGsmPdpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 2, 1, 2),
    _C3gGsmPdpType_Type()
)
c3gGsmPdpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmPdpType.setStatus("current")


class _C3gGsmPdpAddress_Type(DisplayString):
    """Custom type c3gGsmPdpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_C3gGsmPdpAddress_Type.__name__ = "DisplayString"
_C3gGsmPdpAddress_Object = MibTableColumn
c3gGsmPdpAddress = _C3gGsmPdpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 2, 1, 3),
    _C3gGsmPdpAddress_Type()
)
c3gGsmPdpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmPdpAddress.setStatus("current")
_C3gGsmReqUmtsQosTable_Object = MibTable
c3gGsmReqUmtsQosTable = _C3gGsmReqUmtsQosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosTable.setStatus("current")
_C3gGsmReqUmtsQosEntry_Object = MibTableRow
c3gGsmReqUmtsQosEntry = _C3gGsmReqUmtsQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1)
)
c3gGsmReqUmtsQosEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gGsmPdpProfileIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosEntry.setStatus("current")
_C3gGsmReqUmtsQosTrafficClass_Type = C3gUmtsQosTrafficClass
_C3gGsmReqUmtsQosTrafficClass_Object = MibTableColumn
c3gGsmReqUmtsQosTrafficClass = _C3gGsmReqUmtsQosTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 2),
    _C3gGsmReqUmtsQosTrafficClass_Type()
)
c3gGsmReqUmtsQosTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosTrafficClass.setStatus("current")
_C3gGsmReqUmtsQosMaxUpLinkBitRate_Type = C3gUmtsQosLinkBitRate
_C3gGsmReqUmtsQosMaxUpLinkBitRate_Object = MibTableColumn
c3gGsmReqUmtsQosMaxUpLinkBitRate = _C3gGsmReqUmtsQosMaxUpLinkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 3),
    _C3gGsmReqUmtsQosMaxUpLinkBitRate_Type()
)
c3gGsmReqUmtsQosMaxUpLinkBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosMaxUpLinkBitRate.setStatus("current")
_C3gGsmReqUmtsQosMaxDownLinkBitRate_Type = C3gUmtsQosLinkBitRate
_C3gGsmReqUmtsQosMaxDownLinkBitRate_Object = MibTableColumn
c3gGsmReqUmtsQosMaxDownLinkBitRate = _C3gGsmReqUmtsQosMaxDownLinkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 4),
    _C3gGsmReqUmtsQosMaxDownLinkBitRate_Type()
)
c3gGsmReqUmtsQosMaxDownLinkBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosMaxDownLinkBitRate.setStatus("current")
_C3gGsmReqUmtsQosGuaUpLinkBitRate_Type = C3gUmtsQosLinkBitRate
_C3gGsmReqUmtsQosGuaUpLinkBitRate_Object = MibTableColumn
c3gGsmReqUmtsQosGuaUpLinkBitRate = _C3gGsmReqUmtsQosGuaUpLinkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 5),
    _C3gGsmReqUmtsQosGuaUpLinkBitRate_Type()
)
c3gGsmReqUmtsQosGuaUpLinkBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosGuaUpLinkBitRate.setStatus("current")
_C3gGsmReqUmtsQosGuaDownLinkBitRate_Type = C3gUmtsQosLinkBitRate
_C3gGsmReqUmtsQosGuaDownLinkBitRate_Object = MibTableColumn
c3gGsmReqUmtsQosGuaDownLinkBitRate = _C3gGsmReqUmtsQosGuaDownLinkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 6),
    _C3gGsmReqUmtsQosGuaDownLinkBitRate_Type()
)
c3gGsmReqUmtsQosGuaDownLinkBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosGuaDownLinkBitRate.setStatus("current")
_C3gGsmReqUmtsQosOrder_Type = C3gUmtsQosOrder
_C3gGsmReqUmtsQosOrder_Object = MibTableColumn
c3gGsmReqUmtsQosOrder = _C3gGsmReqUmtsQosOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 7),
    _C3gGsmReqUmtsQosOrder_Type()
)
c3gGsmReqUmtsQosOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosOrder.setStatus("current")
_C3gGsmReqUmtsQosErroneousSdu_Type = C3gUmtsQosErroneousSdu
_C3gGsmReqUmtsQosErroneousSdu_Object = MibTableColumn
c3gGsmReqUmtsQosErroneousSdu = _C3gGsmReqUmtsQosErroneousSdu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 8),
    _C3gGsmReqUmtsQosErroneousSdu_Type()
)
c3gGsmReqUmtsQosErroneousSdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosErroneousSdu.setStatus("current")


class _C3gGsmReqUmtsQosMaxSduSize_Type(Unsigned32):
    """Custom type c3gGsmReqUmtsQosMaxSduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1520),
    )


_C3gGsmReqUmtsQosMaxSduSize_Type.__name__ = "Unsigned32"
_C3gGsmReqUmtsQosMaxSduSize_Object = MibTableColumn
c3gGsmReqUmtsQosMaxSduSize = _C3gGsmReqUmtsQosMaxSduSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 9),
    _C3gGsmReqUmtsQosMaxSduSize_Type()
)
c3gGsmReqUmtsQosMaxSduSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosMaxSduSize.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosMaxSduSize.setUnits("bytes")
_C3gGsmReqUmtsQosSer_Type = C3gUmtsQosSer
_C3gGsmReqUmtsQosSer_Object = MibTableColumn
c3gGsmReqUmtsQosSer = _C3gGsmReqUmtsQosSer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 10),
    _C3gGsmReqUmtsQosSer_Type()
)
c3gGsmReqUmtsQosSer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosSer.setStatus("current")
_C3gGsmReqUmtsQosBer_Type = C3gUmtsQosBer
_C3gGsmReqUmtsQosBer_Object = MibTableColumn
c3gGsmReqUmtsQosBer = _C3gGsmReqUmtsQosBer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 11),
    _C3gGsmReqUmtsQosBer_Type()
)
c3gGsmReqUmtsQosBer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosBer.setStatus("current")


class _C3gGsmReqUmtsQosDelay_Type(Unsigned32):
    """Custom type c3gGsmReqUmtsQosDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_C3gGsmReqUmtsQosDelay_Type.__name__ = "Unsigned32"
_C3gGsmReqUmtsQosDelay_Object = MibTableColumn
c3gGsmReqUmtsQosDelay = _C3gGsmReqUmtsQosDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 12),
    _C3gGsmReqUmtsQosDelay_Type()
)
c3gGsmReqUmtsQosDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosDelay.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosDelay.setUnits("milliseconds")
_C3gGsmReqUmtsQosPriority_Type = C3gUmtsQosPriority
_C3gGsmReqUmtsQosPriority_Object = MibTableColumn
c3gGsmReqUmtsQosPriority = _C3gGsmReqUmtsQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 13),
    _C3gGsmReqUmtsQosPriority_Type()
)
c3gGsmReqUmtsQosPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosPriority.setStatus("current")
_C3gGsmReqUmtsQosSrcStatDescriptor_Type = C3gUmtsQosSrcStatDescriptor
_C3gGsmReqUmtsQosSrcStatDescriptor_Object = MibTableColumn
c3gGsmReqUmtsQosSrcStatDescriptor = _C3gGsmReqUmtsQosSrcStatDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 14),
    _C3gGsmReqUmtsQosSrcStatDescriptor_Type()
)
c3gGsmReqUmtsQosSrcStatDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosSrcStatDescriptor.setStatus("current")
_C3gGsmReqUmtsQosSignalIndication_Type = C3gUmtsQosSignalIndication
_C3gGsmReqUmtsQosSignalIndication_Object = MibTableColumn
c3gGsmReqUmtsQosSignalIndication = _C3gGsmReqUmtsQosSignalIndication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 15),
    _C3gGsmReqUmtsQosSignalIndication_Type()
)
c3gGsmReqUmtsQosSignalIndication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosSignalIndication.setStatus("current")
_C3gGsmReqUmtsQosRowStatus_Type = RowStatus
_C3gGsmReqUmtsQosRowStatus_Object = MibTableColumn
c3gGsmReqUmtsQosRowStatus = _C3gGsmReqUmtsQosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 3, 1, 16),
    _C3gGsmReqUmtsQosRowStatus_Type()
)
c3gGsmReqUmtsQosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqUmtsQosRowStatus.setStatus("current")
_C3gGsmMinUmtsQosTable_Object = MibTable
c3gGsmMinUmtsQosTable = _C3gGsmMinUmtsQosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosTable.setStatus("current")
_C3gGsmMinUmtsQosEntry_Object = MibTableRow
c3gGsmMinUmtsQosEntry = _C3gGsmMinUmtsQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1)
)
c3gGsmMinUmtsQosEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gGsmPdpProfileIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosEntry.setStatus("current")
_C3gGsmMinUmtsQosTrafficClass_Type = C3gUmtsQosTrafficClass
_C3gGsmMinUmtsQosTrafficClass_Object = MibTableColumn
c3gGsmMinUmtsQosTrafficClass = _C3gGsmMinUmtsQosTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 1),
    _C3gGsmMinUmtsQosTrafficClass_Type()
)
c3gGsmMinUmtsQosTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosTrafficClass.setStatus("current")
_C3gGsmMinUmtsQosMaxUpLinkBitRate_Type = C3gUmtsQosLinkBitRate
_C3gGsmMinUmtsQosMaxUpLinkBitRate_Object = MibTableColumn
c3gGsmMinUmtsQosMaxUpLinkBitRate = _C3gGsmMinUmtsQosMaxUpLinkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 2),
    _C3gGsmMinUmtsQosMaxUpLinkBitRate_Type()
)
c3gGsmMinUmtsQosMaxUpLinkBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosMaxUpLinkBitRate.setStatus("current")
_C3gGsmMinUmtsQosMaxDownLinkBitRate_Type = C3gUmtsQosLinkBitRate
_C3gGsmMinUmtsQosMaxDownLinkBitRate_Object = MibTableColumn
c3gGsmMinUmtsQosMaxDownLinkBitRate = _C3gGsmMinUmtsQosMaxDownLinkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 3),
    _C3gGsmMinUmtsQosMaxDownLinkBitRate_Type()
)
c3gGsmMinUmtsQosMaxDownLinkBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosMaxDownLinkBitRate.setStatus("current")
_C3gGsmMinUmtsQosGuaUpLinkBitRate_Type = C3gUmtsQosLinkBitRate
_C3gGsmMinUmtsQosGuaUpLinkBitRate_Object = MibTableColumn
c3gGsmMinUmtsQosGuaUpLinkBitRate = _C3gGsmMinUmtsQosGuaUpLinkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 4),
    _C3gGsmMinUmtsQosGuaUpLinkBitRate_Type()
)
c3gGsmMinUmtsQosGuaUpLinkBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosGuaUpLinkBitRate.setStatus("current")
_C3gGsmMinUmtsQosGuaDownLinkBitRate_Type = C3gUmtsQosLinkBitRate
_C3gGsmMinUmtsQosGuaDownLinkBitRate_Object = MibTableColumn
c3gGsmMinUmtsQosGuaDownLinkBitRate = _C3gGsmMinUmtsQosGuaDownLinkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 5),
    _C3gGsmMinUmtsQosGuaDownLinkBitRate_Type()
)
c3gGsmMinUmtsQosGuaDownLinkBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosGuaDownLinkBitRate.setStatus("current")
_C3gGsmMinUmtsQosOrder_Type = C3gUmtsQosOrder
_C3gGsmMinUmtsQosOrder_Object = MibTableColumn
c3gGsmMinUmtsQosOrder = _C3gGsmMinUmtsQosOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 6),
    _C3gGsmMinUmtsQosOrder_Type()
)
c3gGsmMinUmtsQosOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosOrder.setStatus("current")
_C3gGsmMinUmtsQosErroneousSdu_Type = C3gUmtsQosErroneousSdu
_C3gGsmMinUmtsQosErroneousSdu_Object = MibTableColumn
c3gGsmMinUmtsQosErroneousSdu = _C3gGsmMinUmtsQosErroneousSdu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 7),
    _C3gGsmMinUmtsQosErroneousSdu_Type()
)
c3gGsmMinUmtsQosErroneousSdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosErroneousSdu.setStatus("current")


class _C3gGsmMinUmtsQosMaxSduSize_Type(Unsigned32):
    """Custom type c3gGsmMinUmtsQosMaxSduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1520),
    )


_C3gGsmMinUmtsQosMaxSduSize_Type.__name__ = "Unsigned32"
_C3gGsmMinUmtsQosMaxSduSize_Object = MibTableColumn
c3gGsmMinUmtsQosMaxSduSize = _C3gGsmMinUmtsQosMaxSduSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 8),
    _C3gGsmMinUmtsQosMaxSduSize_Type()
)
c3gGsmMinUmtsQosMaxSduSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosMaxSduSize.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosMaxSduSize.setUnits("bytes")
_C3gGsmMinUmtsQosSer_Type = C3gUmtsQosSer
_C3gGsmMinUmtsQosSer_Object = MibTableColumn
c3gGsmMinUmtsQosSer = _C3gGsmMinUmtsQosSer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 9),
    _C3gGsmMinUmtsQosSer_Type()
)
c3gGsmMinUmtsQosSer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosSer.setStatus("current")
_C3gGsmMinUmtsQosBer_Type = C3gUmtsQosBer
_C3gGsmMinUmtsQosBer_Object = MibTableColumn
c3gGsmMinUmtsQosBer = _C3gGsmMinUmtsQosBer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 10),
    _C3gGsmMinUmtsQosBer_Type()
)
c3gGsmMinUmtsQosBer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosBer.setStatus("current")


class _C3gGsmMinUmtsQosDelay_Type(Unsigned32):
    """Custom type c3gGsmMinUmtsQosDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_C3gGsmMinUmtsQosDelay_Type.__name__ = "Unsigned32"
_C3gGsmMinUmtsQosDelay_Object = MibTableColumn
c3gGsmMinUmtsQosDelay = _C3gGsmMinUmtsQosDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 11),
    _C3gGsmMinUmtsQosDelay_Type()
)
c3gGsmMinUmtsQosDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosDelay.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosDelay.setUnits("milliseconds")
_C3gGsmMinUmtsQosPriority_Type = C3gUmtsQosPriority
_C3gGsmMinUmtsQosPriority_Object = MibTableColumn
c3gGsmMinUmtsQosPriority = _C3gGsmMinUmtsQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 12),
    _C3gGsmMinUmtsQosPriority_Type()
)
c3gGsmMinUmtsQosPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosPriority.setStatus("current")
_C3gGsmMinUmtsQosSrcStatDescriptor_Type = C3gUmtsQosSrcStatDescriptor
_C3gGsmMinUmtsQosSrcStatDescriptor_Object = MibTableColumn
c3gGsmMinUmtsQosSrcStatDescriptor = _C3gGsmMinUmtsQosSrcStatDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 13),
    _C3gGsmMinUmtsQosSrcStatDescriptor_Type()
)
c3gGsmMinUmtsQosSrcStatDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosSrcStatDescriptor.setStatus("current")
_C3gGsmMinUmtsQosSignalIndication_Type = C3gUmtsQosSignalIndication
_C3gGsmMinUmtsQosSignalIndication_Object = MibTableColumn
c3gGsmMinUmtsQosSignalIndication = _C3gGsmMinUmtsQosSignalIndication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 14),
    _C3gGsmMinUmtsQosSignalIndication_Type()
)
c3gGsmMinUmtsQosSignalIndication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosSignalIndication.setStatus("current")
_C3gGsmMinUmtsQosRowStatus_Type = RowStatus
_C3gGsmMinUmtsQosRowStatus_Object = MibTableColumn
c3gGsmMinUmtsQosRowStatus = _C3gGsmMinUmtsQosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 4, 1, 15),
    _C3gGsmMinUmtsQosRowStatus_Type()
)
c3gGsmMinUmtsQosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinUmtsQosRowStatus.setStatus("current")
_C3gGsmNegoUmtsQosTable_Object = MibTable
c3gGsmNegoUmtsQosTable = _C3gGsmNegoUmtsQosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosTable.setStatus("current")
_C3gGsmNegoUmtsQosEntry_Object = MibTableRow
c3gGsmNegoUmtsQosEntry = _C3gGsmNegoUmtsQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1)
)
c3gGsmNegoUmtsQosEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gGsmPdpProfileIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosEntry.setStatus("current")
_C3gGsmNegoUmtsQosTrafficClass_Type = C3gUmtsQosTrafficClass
_C3gGsmNegoUmtsQosTrafficClass_Object = MibTableColumn
c3gGsmNegoUmtsQosTrafficClass = _C3gGsmNegoUmtsQosTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 1),
    _C3gGsmNegoUmtsQosTrafficClass_Type()
)
c3gGsmNegoUmtsQosTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosTrafficClass.setStatus("current")
_C3gGsmNegoUmtsQosMaxUpLinkBitRate_Type = C3gUmtsQosLinkBitRate
_C3gGsmNegoUmtsQosMaxUpLinkBitRate_Object = MibTableColumn
c3gGsmNegoUmtsQosMaxUpLinkBitRate = _C3gGsmNegoUmtsQosMaxUpLinkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 2),
    _C3gGsmNegoUmtsQosMaxUpLinkBitRate_Type()
)
c3gGsmNegoUmtsQosMaxUpLinkBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosMaxUpLinkBitRate.setStatus("current")
_C3gGsmNegoUmtsQosMaxDownLinkBitRate_Type = C3gUmtsQosLinkBitRate
_C3gGsmNegoUmtsQosMaxDownLinkBitRate_Object = MibTableColumn
c3gGsmNegoUmtsQosMaxDownLinkBitRate = _C3gGsmNegoUmtsQosMaxDownLinkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 3),
    _C3gGsmNegoUmtsQosMaxDownLinkBitRate_Type()
)
c3gGsmNegoUmtsQosMaxDownLinkBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosMaxDownLinkBitRate.setStatus("current")
_C3gGsmNegoUmtsQosGuaUpLinkBitRate_Type = C3gUmtsQosLinkBitRate
_C3gGsmNegoUmtsQosGuaUpLinkBitRate_Object = MibTableColumn
c3gGsmNegoUmtsQosGuaUpLinkBitRate = _C3gGsmNegoUmtsQosGuaUpLinkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 4),
    _C3gGsmNegoUmtsQosGuaUpLinkBitRate_Type()
)
c3gGsmNegoUmtsQosGuaUpLinkBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosGuaUpLinkBitRate.setStatus("current")
_C3gGsmNegoUmtsQosGuaDownLinkBitRate_Type = C3gUmtsQosLinkBitRate
_C3gGsmNegoUmtsQosGuaDownLinkBitRate_Object = MibTableColumn
c3gGsmNegoUmtsQosGuaDownLinkBitRate = _C3gGsmNegoUmtsQosGuaDownLinkBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 5),
    _C3gGsmNegoUmtsQosGuaDownLinkBitRate_Type()
)
c3gGsmNegoUmtsQosGuaDownLinkBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosGuaDownLinkBitRate.setStatus("current")
_C3gGsmNegoUmtsQosOrder_Type = C3gUmtsQosOrder
_C3gGsmNegoUmtsQosOrder_Object = MibTableColumn
c3gGsmNegoUmtsQosOrder = _C3gGsmNegoUmtsQosOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 6),
    _C3gGsmNegoUmtsQosOrder_Type()
)
c3gGsmNegoUmtsQosOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosOrder.setStatus("current")
_C3gGsmNegoUmtsQosErroneousSdu_Type = C3gUmtsQosErroneousSdu
_C3gGsmNegoUmtsQosErroneousSdu_Object = MibTableColumn
c3gGsmNegoUmtsQosErroneousSdu = _C3gGsmNegoUmtsQosErroneousSdu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 7),
    _C3gGsmNegoUmtsQosErroneousSdu_Type()
)
c3gGsmNegoUmtsQosErroneousSdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosErroneousSdu.setStatus("current")


class _C3gGsmNegoUmtsQosMaxSduSize_Type(Unsigned32):
    """Custom type c3gGsmNegoUmtsQosMaxSduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1520),
    )


_C3gGsmNegoUmtsQosMaxSduSize_Type.__name__ = "Unsigned32"
_C3gGsmNegoUmtsQosMaxSduSize_Object = MibTableColumn
c3gGsmNegoUmtsQosMaxSduSize = _C3gGsmNegoUmtsQosMaxSduSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 8),
    _C3gGsmNegoUmtsQosMaxSduSize_Type()
)
c3gGsmNegoUmtsQosMaxSduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosMaxSduSize.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosMaxSduSize.setUnits("bytes")
_C3gGsmNegoUmtsQosSer_Type = C3gUmtsQosSer
_C3gGsmNegoUmtsQosSer_Object = MibTableColumn
c3gGsmNegoUmtsQosSer = _C3gGsmNegoUmtsQosSer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 9),
    _C3gGsmNegoUmtsQosSer_Type()
)
c3gGsmNegoUmtsQosSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosSer.setStatus("current")
_C3gGsmNegoUmtsQosBer_Type = C3gUmtsQosBer
_C3gGsmNegoUmtsQosBer_Object = MibTableColumn
c3gGsmNegoUmtsQosBer = _C3gGsmNegoUmtsQosBer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 10),
    _C3gGsmNegoUmtsQosBer_Type()
)
c3gGsmNegoUmtsQosBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosBer.setStatus("current")


class _C3gGsmNegoUmtsQosDelay_Type(Unsigned32):
    """Custom type c3gGsmNegoUmtsQosDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_C3gGsmNegoUmtsQosDelay_Type.__name__ = "Unsigned32"
_C3gGsmNegoUmtsQosDelay_Object = MibTableColumn
c3gGsmNegoUmtsQosDelay = _C3gGsmNegoUmtsQosDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 11),
    _C3gGsmNegoUmtsQosDelay_Type()
)
c3gGsmNegoUmtsQosDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosDelay.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosDelay.setUnits("milliseconds")
_C3gGsmNegoUmtsQosPriority_Type = C3gUmtsQosPriority
_C3gGsmNegoUmtsQosPriority_Object = MibTableColumn
c3gGsmNegoUmtsQosPriority = _C3gGsmNegoUmtsQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 12),
    _C3gGsmNegoUmtsQosPriority_Type()
)
c3gGsmNegoUmtsQosPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosPriority.setStatus("current")
_C3gGsmNegoUmtsQosSrcStatDescriptor_Type = C3gUmtsQosSrcStatDescriptor
_C3gGsmNegoUmtsQosSrcStatDescriptor_Object = MibTableColumn
c3gGsmNegoUmtsQosSrcStatDescriptor = _C3gGsmNegoUmtsQosSrcStatDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 13),
    _C3gGsmNegoUmtsQosSrcStatDescriptor_Type()
)
c3gGsmNegoUmtsQosSrcStatDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosSrcStatDescriptor.setStatus("current")
_C3gGsmNegoUmtsQosSignalIndication_Type = C3gUmtsQosSignalIndication
_C3gGsmNegoUmtsQosSignalIndication_Object = MibTableColumn
c3gGsmNegoUmtsQosSignalIndication = _C3gGsmNegoUmtsQosSignalIndication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 5, 1, 14),
    _C3gGsmNegoUmtsQosSignalIndication_Type()
)
c3gGsmNegoUmtsQosSignalIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoUmtsQosSignalIndication.setStatus("current")
_C3gGsmReqGprsQosTable_Object = MibTable
c3gGsmReqGprsQosTable = _C3gGsmReqGprsQosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 6)
)
if mibBuilder.loadTexts:
    c3gGsmReqGprsQosTable.setStatus("current")
_C3gGsmReqGprsQosEntry_Object = MibTableRow
c3gGsmReqGprsQosEntry = _C3gGsmReqGprsQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 6, 1)
)
c3gGsmReqGprsQosEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gGsmPdpProfileIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmReqGprsQosEntry.setStatus("current")
_C3gGsmReqGprsQosPrecedence_Type = C3gGprsQosPrecedence
_C3gGsmReqGprsQosPrecedence_Object = MibTableColumn
c3gGsmReqGprsQosPrecedence = _C3gGsmReqGprsQosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 6, 1, 1),
    _C3gGsmReqGprsQosPrecedence_Type()
)
c3gGsmReqGprsQosPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqGprsQosPrecedence.setStatus("current")
_C3gGsmReqGprsQosDelay_Type = C3gGprsQosDelay
_C3gGsmReqGprsQosDelay_Object = MibTableColumn
c3gGsmReqGprsQosDelay = _C3gGsmReqGprsQosDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 6, 1, 2),
    _C3gGsmReqGprsQosDelay_Type()
)
c3gGsmReqGprsQosDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqGprsQosDelay.setStatus("current")
_C3gGsmReqGprsQosReliability_Type = C3gGprsQosReliability
_C3gGsmReqGprsQosReliability_Object = MibTableColumn
c3gGsmReqGprsQosReliability = _C3gGsmReqGprsQosReliability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 6, 1, 3),
    _C3gGsmReqGprsQosReliability_Type()
)
c3gGsmReqGprsQosReliability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqGprsQosReliability.setStatus("current")
_C3gGsmReqGprsQosPeakRate_Type = C3gGprsQosPeakRate
_C3gGsmReqGprsQosPeakRate_Object = MibTableColumn
c3gGsmReqGprsQosPeakRate = _C3gGsmReqGprsQosPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 6, 1, 4),
    _C3gGsmReqGprsQosPeakRate_Type()
)
c3gGsmReqGprsQosPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqGprsQosPeakRate.setStatus("current")
_C3gGsmReqGprsQosMeanRate_Type = C3gGprsQosMeanRate
_C3gGsmReqGprsQosMeanRate_Object = MibTableColumn
c3gGsmReqGprsQosMeanRate = _C3gGsmReqGprsQosMeanRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 6, 1, 5),
    _C3gGsmReqGprsQosMeanRate_Type()
)
c3gGsmReqGprsQosMeanRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqGprsQosMeanRate.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmReqGprsQosMeanRate.setUnits("octet-per-hour")
_C3gGsmReqGprsQosRowStatus_Type = RowStatus
_C3gGsmReqGprsQosRowStatus_Object = MibTableColumn
c3gGsmReqGprsQosRowStatus = _C3gGsmReqGprsQosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 6, 1, 6),
    _C3gGsmReqGprsQosRowStatus_Type()
)
c3gGsmReqGprsQosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmReqGprsQosRowStatus.setStatus("current")
_C3gGsmMinGprsQosTable_Object = MibTable
c3gGsmMinGprsQosTable = _C3gGsmMinGprsQosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 7)
)
if mibBuilder.loadTexts:
    c3gGsmMinGprsQosTable.setStatus("current")
_C3gGsmMinGprsQosEntry_Object = MibTableRow
c3gGsmMinGprsQosEntry = _C3gGsmMinGprsQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 7, 1)
)
c3gGsmMinGprsQosEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gGsmPdpProfileIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmMinGprsQosEntry.setStatus("current")
_C3gGsmMinGprsQosPrecedence_Type = C3gGprsQosPrecedence
_C3gGsmMinGprsQosPrecedence_Object = MibTableColumn
c3gGsmMinGprsQosPrecedence = _C3gGsmMinGprsQosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 7, 1, 1),
    _C3gGsmMinGprsQosPrecedence_Type()
)
c3gGsmMinGprsQosPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinGprsQosPrecedence.setStatus("current")
_C3gGsmMinGprsQosDelay_Type = C3gGprsQosDelay
_C3gGsmMinGprsQosDelay_Object = MibTableColumn
c3gGsmMinGprsQosDelay = _C3gGsmMinGprsQosDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 7, 1, 2),
    _C3gGsmMinGprsQosDelay_Type()
)
c3gGsmMinGprsQosDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinGprsQosDelay.setStatus("current")
_C3gGsmMinGprsQosReliability_Type = C3gGprsQosReliability
_C3gGsmMinGprsQosReliability_Object = MibTableColumn
c3gGsmMinGprsQosReliability = _C3gGsmMinGprsQosReliability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 7, 1, 3),
    _C3gGsmMinGprsQosReliability_Type()
)
c3gGsmMinGprsQosReliability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinGprsQosReliability.setStatus("current")
_C3gGsmMinGprsQosPeakRate_Type = C3gGprsQosPeakRate
_C3gGsmMinGprsQosPeakRate_Object = MibTableColumn
c3gGsmMinGprsQosPeakRate = _C3gGsmMinGprsQosPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 7, 1, 4),
    _C3gGsmMinGprsQosPeakRate_Type()
)
c3gGsmMinGprsQosPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinGprsQosPeakRate.setStatus("current")
_C3gGsmMinGprsQosMeanRate_Type = C3gGprsQosMeanRate
_C3gGsmMinGprsQosMeanRate_Object = MibTableColumn
c3gGsmMinGprsQosMeanRate = _C3gGsmMinGprsQosMeanRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 7, 1, 5),
    _C3gGsmMinGprsQosMeanRate_Type()
)
c3gGsmMinGprsQosMeanRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinGprsQosMeanRate.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmMinGprsQosMeanRate.setUnits("octet-per-hour")
_C3gGsmMinGprsQosRowStatus_Type = RowStatus
_C3gGsmMinGprsQosRowStatus_Object = MibTableColumn
c3gGsmMinGprsQosRowStatus = _C3gGsmMinGprsQosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 7, 1, 6),
    _C3gGsmMinGprsQosRowStatus_Type()
)
c3gGsmMinGprsQosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gGsmMinGprsQosRowStatus.setStatus("current")
_C3gGsmNegoGprsQosTable_Object = MibTable
c3gGsmNegoGprsQosTable = _C3gGsmNegoGprsQosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 8)
)
if mibBuilder.loadTexts:
    c3gGsmNegoGprsQosTable.setStatus("current")
_C3gGsmNegoGprsQosEntry_Object = MibTableRow
c3gGsmNegoGprsQosEntry = _C3gGsmNegoGprsQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 8, 1)
)
c3gGsmNegoGprsQosEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gGsmPdpProfileIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmNegoGprsQosEntry.setStatus("current")
_C3gGsmNegoGprsQosPrecedence_Type = C3gGprsQosPrecedence
_C3gGsmNegoGprsQosPrecedence_Object = MibTableColumn
c3gGsmNegoGprsQosPrecedence = _C3gGsmNegoGprsQosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 8, 1, 1),
    _C3gGsmNegoGprsQosPrecedence_Type()
)
c3gGsmNegoGprsQosPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoGprsQosPrecedence.setStatus("current")
_C3gGsmNegoGprsQosDelay_Type = C3gGprsQosDelay
_C3gGsmNegoGprsQosDelay_Object = MibTableColumn
c3gGsmNegoGprsQosDelay = _C3gGsmNegoGprsQosDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 8, 1, 2),
    _C3gGsmNegoGprsQosDelay_Type()
)
c3gGsmNegoGprsQosDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoGprsQosDelay.setStatus("current")
_C3gGsmNegoGprsQosReliability_Type = C3gGprsQosReliability
_C3gGsmNegoGprsQosReliability_Object = MibTableColumn
c3gGsmNegoGprsQosReliability = _C3gGsmNegoGprsQosReliability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 8, 1, 3),
    _C3gGsmNegoGprsQosReliability_Type()
)
c3gGsmNegoGprsQosReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoGprsQosReliability.setStatus("current")
_C3gGsmNegoGprsQosPeakRate_Type = C3gGprsQosPeakRate
_C3gGsmNegoGprsQosPeakRate_Object = MibTableColumn
c3gGsmNegoGprsQosPeakRate = _C3gGsmNegoGprsQosPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 8, 1, 4),
    _C3gGsmNegoGprsQosPeakRate_Type()
)
c3gGsmNegoGprsQosPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoGprsQosPeakRate.setStatus("current")
_C3gGsmNegoGprsQosMeanRate_Type = C3gGprsQosMeanRate
_C3gGsmNegoGprsQosMeanRate_Object = MibTableColumn
c3gGsmNegoGprsQosMeanRate = _C3gGsmNegoGprsQosMeanRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 3, 8, 1, 5),
    _C3gGsmNegoGprsQosMeanRate_Type()
)
c3gGsmNegoGprsQosMeanRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNegoGprsQosMeanRate.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmNegoGprsQosMeanRate.setUnits("octet-per-hour")
_C3gGsmRadio_ObjectIdentity = ObjectIdentity
c3gGsmRadio = _C3gGsmRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4)
)
_C3gGsmRadioTable_Object = MibTable
c3gGsmRadioTable = _C3gGsmRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    c3gGsmRadioTable.setStatus("current")
_C3gGsmRadioEntry_Object = MibTableRow
c3gGsmRadioEntry = _C3gGsmRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 1, 1)
)
c3gGsmRadioEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmRadioEntry.setStatus("current")
_C3gCurrentGsmRssi_Type = C3gRssi
_C3gCurrentGsmRssi_Object = MibTableColumn
c3gCurrentGsmRssi = _C3gCurrentGsmRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 1, 1, 1),
    _C3gCurrentGsmRssi_Type()
)
c3gCurrentGsmRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCurrentGsmRssi.setStatus("current")
_C3gCurrentGsmEcIo_Type = C3gEcIo
_C3gCurrentGsmEcIo_Object = MibTableColumn
c3gCurrentGsmEcIo = _C3gCurrentGsmEcIo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 1, 1, 2),
    _C3gCurrentGsmEcIo_Type()
)
c3gCurrentGsmEcIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gCurrentGsmEcIo.setStatus("current")


class _C3gGsmCurrentBand_Type(Integer32):
    """Custom type c3gGsmCurrentBand based on Integer32"""
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("gsm1800", 6),
          ("gsm1900", 7),
          ("gsm850", 4),
          ("gsm900", 5),
          ("invalid", 2),
          ("lteBand", 12),
          ("none", 3),
          ("unknown", 1),
          ("wcdma1900", 10),
          ("wcdma2100", 11),
          ("wcdma800", 8),
          ("wcdma850", 9))
    )


_C3gGsmCurrentBand_Type.__name__ = "Integer32"
_C3gGsmCurrentBand_Object = MibTableColumn
c3gGsmCurrentBand = _C3gGsmCurrentBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 1, 1, 3),
    _C3gGsmCurrentBand_Type()
)
c3gGsmCurrentBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmCurrentBand.setStatus("current")


class _C3gGsmChannelNumber_Type(Unsigned32):
    """Custom type c3gGsmChannelNumber based on Unsigned32"""
    defaultValue = 0


_C3gGsmChannelNumber_Object = MibTableColumn
c3gGsmChannelNumber = _C3gGsmChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 1, 1, 4),
    _C3gGsmChannelNumber_Type()
)
c3gGsmChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmChannelNumber.setStatus("current")


class _C3gGsmNumberOfNearbyCell_Type(Unsigned32):
    """Custom type c3gGsmNumberOfNearbyCell based on Unsigned32"""
    defaultValue = 0


_C3gGsmNumberOfNearbyCell_Object = MibTableColumn
c3gGsmNumberOfNearbyCell = _C3gGsmNumberOfNearbyCell_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 1, 1, 5),
    _C3gGsmNumberOfNearbyCell_Type()
)
c3gGsmNumberOfNearbyCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNumberOfNearbyCell.setStatus("current")
_C3gGsmNearbyCellTable_Object = MibTable
c3gGsmNearbyCellTable = _C3gGsmNearbyCellTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    c3gGsmNearbyCellTable.setStatus("current")
_C3gGsmNearbyCellEntry_Object = MibTableRow
c3gGsmNearbyCellEntry = _C3gGsmNearbyCellEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 2, 1)
)
c3gGsmNearbyCellEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gGsmNearbyCellIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmNearbyCellEntry.setStatus("current")


class _C3gGsmNearbyCellIndex_Type(Integer32):
    """Custom type c3gGsmNearbyCellIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_C3gGsmNearbyCellIndex_Type.__name__ = "Integer32"
_C3gGsmNearbyCellIndex_Object = MibTableColumn
c3gGsmNearbyCellIndex = _C3gGsmNearbyCellIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 2, 1, 1),
    _C3gGsmNearbyCellIndex_Type()
)
c3gGsmNearbyCellIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c3gGsmNearbyCellIndex.setStatus("current")
_C3gGsmNearbyCellPrimaryScramblingCode_Type = Unsigned32
_C3gGsmNearbyCellPrimaryScramblingCode_Object = MibTableColumn
c3gGsmNearbyCellPrimaryScramblingCode = _C3gGsmNearbyCellPrimaryScramblingCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 2, 1, 2),
    _C3gGsmNearbyCellPrimaryScramblingCode_Type()
)
c3gGsmNearbyCellPrimaryScramblingCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNearbyCellPrimaryScramblingCode.setStatus("current")


class _C3gGsmNearbyCellRscp_Type(Integer32):
    """Custom type c3gGsmNearbyCellRscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_C3gGsmNearbyCellRscp_Type.__name__ = "Integer32"
_C3gGsmNearbyCellRscp_Object = MibTableColumn
c3gGsmNearbyCellRscp = _C3gGsmNearbyCellRscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 2, 1, 3),
    _C3gGsmNearbyCellRscp_Type()
)
c3gGsmNearbyCellRscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNearbyCellRscp.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmNearbyCellRscp.setUnits("dB")
_C3gGsmNearbyCellEcIoMeasurement_Type = C3gEcIo
_C3gGsmNearbyCellEcIoMeasurement_Object = MibTableColumn
c3gGsmNearbyCellEcIoMeasurement = _C3gGsmNearbyCellEcIoMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 2, 1, 4),
    _C3gGsmNearbyCellEcIoMeasurement_Type()
)
c3gGsmNearbyCellEcIoMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNearbyCellEcIoMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmNearbyCellEcIoMeasurement.setUnits("dB")
_C3gGsmHistoryTable_Object = MibTable
c3gGsmHistoryTable = _C3gGsmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    c3gGsmHistoryTable.setStatus("current")
_C3gGsmHistoryEntry_Object = MibTableRow
c3gGsmHistoryEntry = _C3gGsmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 3, 1)
)
c3gGsmHistoryEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmHistoryEntry.setStatus("current")


class _C3gGsmHistoryRssiPerSecond_Type(OctetString):
    """Custom type c3gGsmHistoryRssiPerSecond based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_C3gGsmHistoryRssiPerSecond_Type.__name__ = "OctetString"
_C3gGsmHistoryRssiPerSecond_Object = MibTableColumn
c3gGsmHistoryRssiPerSecond = _C3gGsmHistoryRssiPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 3, 1, 1),
    _C3gGsmHistoryRssiPerSecond_Type()
)
c3gGsmHistoryRssiPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmHistoryRssiPerSecond.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmHistoryRssiPerSecond.setUnits("-dBm")


class _C3gGsmHistoryRssiPerMinute_Type(OctetString):
    """Custom type c3gGsmHistoryRssiPerMinute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_C3gGsmHistoryRssiPerMinute_Type.__name__ = "OctetString"
_C3gGsmHistoryRssiPerMinute_Object = MibTableColumn
c3gGsmHistoryRssiPerMinute = _C3gGsmHistoryRssiPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 3, 1, 2),
    _C3gGsmHistoryRssiPerMinute_Type()
)
c3gGsmHistoryRssiPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmHistoryRssiPerMinute.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmHistoryRssiPerMinute.setUnits("-dBm")


class _C3gGsmHistoryRssiPerHour_Type(OctetString):
    """Custom type c3gGsmHistoryRssiPerHour based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(72, 72),
    )


_C3gGsmHistoryRssiPerHour_Type.__name__ = "OctetString"
_C3gGsmHistoryRssiPerHour_Object = MibTableColumn
c3gGsmHistoryRssiPerHour = _C3gGsmHistoryRssiPerHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 4, 3, 1, 3),
    _C3gGsmHistoryRssiPerHour_Type()
)
c3gGsmHistoryRssiPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmHistoryRssiPerHour.setStatus("current")
if mibBuilder.loadTexts:
    c3gGsmHistoryRssiPerHour.setUnits("-dBm")
_C3gGsmSecurity_ObjectIdentity = ObjectIdentity
c3gGsmSecurity = _C3gGsmSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 5)
)
_C3gGsmSecurityTable_Object = MibTable
c3gGsmSecurityTable = _C3gGsmSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    c3gGsmSecurityTable.setStatus("current")
_C3gGsmSecurityEntry_Object = MibTableRow
c3gGsmSecurityEntry = _C3gGsmSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 5, 1, 1)
)
c3gGsmSecurityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gGsmSecurityEntry.setStatus("current")


class _C3gGsmChv1_Type(Integer32):
    """Custom type c3gGsmChv1 based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("unknown", 1))
    )


_C3gGsmChv1_Type.__name__ = "Integer32"
_C3gGsmChv1_Object = MibTableColumn
c3gGsmChv1 = _C3gGsmChv1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 5, 1, 1, 1),
    _C3gGsmChv1_Type()
)
c3gGsmChv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c3gGsmChv1.setStatus("current")


class _C3gGsmSimStatus_Type(Integer32):
    """Custom type c3gGsmSimStatus based on Integer32"""
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("chv1Blocked", 8),
          ("chv1Rejected", 10),
          ("chv2Blocked", 9),
          ("chv2Rejected", 11),
          ("generalFailure", 6),
          ("initFailure", 5),
          ("locked", 7),
          ("mepLocked", 12),
          ("networkRejected", 13),
          ("notInserted", 3),
          ("ok", 2),
          ("removed", 4),
          ("unknown", 1))
    )


_C3gGsmSimStatus_Type.__name__ = "Integer32"
_C3gGsmSimStatus_Object = MibTableColumn
c3gGsmSimStatus = _C3gGsmSimStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 5, 1, 1, 2),
    _C3gGsmSimStatus_Type()
)
c3gGsmSimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmSimStatus.setStatus("current")


class _C3gGsmSimUserOperationRequired_Type(Integer32):
    """Custom type c3gGsmSimUserOperationRequired based on Integer32"""
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
        *(("enterChv1", 3),
          ("enterChv2", 4),
          ("enterMepCode", 7),
          ("enterUnblockChv1", 5),
          ("enterUnblockChv2", 6),
          ("none", 2),
          ("unknown", 1))
    )


_C3gGsmSimUserOperationRequired_Type.__name__ = "Integer32"
_C3gGsmSimUserOperationRequired_Object = MibTableColumn
c3gGsmSimUserOperationRequired = _C3gGsmSimUserOperationRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 5, 1, 1, 3),
    _C3gGsmSimUserOperationRequired_Type()
)
c3gGsmSimUserOperationRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmSimUserOperationRequired.setStatus("current")


class _C3gGsmNumberOfRetriesRemaining_Type(Unsigned32):
    """Custom type c3gGsmNumberOfRetriesRemaining based on Unsigned32"""
    defaultValue = 0


_C3gGsmNumberOfRetriesRemaining_Object = MibTableColumn
c3gGsmNumberOfRetriesRemaining = _C3gGsmNumberOfRetriesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 3, 5, 1, 1, 4),
    _C3gGsmNumberOfRetriesRemaining_Type()
)
c3gGsmNumberOfRetriesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gGsmNumberOfRetriesRemaining.setStatus("current")
_C3gWanLbs_ObjectIdentity = ObjectIdentity
c3gWanLbs = _C3gWanLbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4)
)
_C3gWanLbsCommon_ObjectIdentity = ObjectIdentity
c3gWanLbsCommon = _C3gWanLbsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1)
)
_C3gWanLbsCommonTable_Object = MibTable
c3gWanLbsCommonTable = _C3gWanLbsCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    c3gWanLbsCommonTable.setStatus("current")
_C3gWanLbsCommonEntry_Object = MibTableRow
c3gWanLbsCommonEntry = _C3gWanLbsCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1)
)
c3gWanLbsCommonEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gWanLbsCommonEntry.setStatus("current")


class _C3gLbsModeSelected_Type(Integer32):
    """Custom type c3gLbsModeSelected based on Integer32"""
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
        *(("msAssist", 4),
          ("msBased", 3),
          ("reserved", 5),
          ("standAlone", 2),
          ("unKnown", 1))
    )


_C3gLbsModeSelected_Type.__name__ = "Integer32"
_C3gLbsModeSelected_Object = MibTableColumn
c3gLbsModeSelected = _C3gLbsModeSelected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 1),
    _C3gLbsModeSelected_Type()
)
c3gLbsModeSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsModeSelected.setStatus("current")


class _C3gLbsState_Type(Integer32):
    """Custom type c3gLbsState based on Integer32"""
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
        *(("gpsAcquiring", 2),
          ("gpsDisabled", 1),
          ("gpsEnabled", 3),
          ("gpsLocError", 4))
    )


_C3gLbsState_Type.__name__ = "Integer32"
_C3gLbsState_Object = MibTableColumn
c3gLbsState = _C3gLbsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 2),
    _C3gLbsState_Type()
)
c3gLbsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsState.setStatus("current")


class _C3gLbsLocFixError_Type(Integer32):
    """Custom type c3gLbsLocFixError based on Integer32"""
    defaultValue = 48

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
              48)
        )
    )
    namedValues = NamedValues(
        *(("additionalAssistanceNeeded", 47),
          ("antennaSwitch", 31),
          ("authenticationFailedLocal", 24),
          ("authenticationFailedNetwork", 25),
          ("authenticationParameterFailed", 23),
          ("clientEnded", 10),
          ("connectionFailed", 8),
          ("desiredFixMethodFailed", 30),
          ("e911", 19),
          ("errorState", 9),
          ("fixError", 16),
          ("gpsDisabled", 7),
          ("mtGguardTimeExpired", 46),
          ("networkAccessError", 15),
          ("networkEnded", 12),
          ("noConnection", 3),
          ("noData", 4),
          ("noErrorFromNetwork", 34),
          ("noFixError", 48),
          ("noResourcesLeftOnNetwork", 35),
          ("noService", 2),
          ("noTxConfirmationReceived", 32),
          ("normalEndOfSession", 33),
          ("offline", 1),
          ("pdeRejected", 17),
          ("positionServerNotAvailable", 36),
          ("privacyLevel", 14),
          ("reserved", 6),
          ("resourceContention", 22),
          ("serverError", 20),
          ("sessionBusy", 5),
          ("smlcTimeout", 45),
          ("ssmolrErrorDataMissing", 40),
          ("ssmolrErrorFacilityNotSupported", 41),
          ("ssmolrErrorPositionMethodFailure", 43),
          ("ssmolrErrorSsSubscriptionViolation", 42),
          ("ssmolrErrorSystemFailure", 38),
          ("ssmolrErrorUndefined", 44),
          ("ssmolrErrorUnexpectedDataValue", 39),
          ("staleBSinformation", 21),
          ("subscriptionViolation", 29),
          ("timeout", 13),
          ("trafficChannelExited", 18),
          ("uiEnded", 11),
          ("unknownSystemError", 27),
          ("unsupportedProtocolVersion", 37),
          ("unsupportedService", 28),
          ("vxLcsAgentAuthFail", 26))
    )


_C3gLbsLocFixError_Type.__name__ = "Integer32"
_C3gLbsLocFixError_Object = MibTableColumn
c3gLbsLocFixError = _C3gLbsLocFixError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 3),
    _C3gLbsLocFixError_Type()
)
c3gLbsLocFixError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsLocFixError.setStatus("current")
_C3gLbsLatitude_Type = SnmpAdminString
_C3gLbsLatitude_Object = MibTableColumn
c3gLbsLatitude = _C3gLbsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 4),
    _C3gLbsLatitude_Type()
)
c3gLbsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsLatitude.setStatus("current")
_C3gLbsLongitude_Type = SnmpAdminString
_C3gLbsLongitude_Object = MibTableColumn
c3gLbsLongitude = _C3gLbsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 5),
    _C3gLbsLongitude_Type()
)
c3gLbsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsLongitude.setStatus("current")
_C3gLbsTimeStamp_Type = SnmpAdminString
_C3gLbsTimeStamp_Object = MibTableColumn
c3gLbsTimeStamp = _C3gLbsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 6),
    _C3gLbsTimeStamp_Type()
)
c3gLbsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsTimeStamp.setStatus("current")


class _C3gLbsLocUncertaintyAngle_Type(Unsigned32):
    """Custom type c3gLbsLocUncertaintyAngle based on Unsigned32"""
    defaultValue = 0


_C3gLbsLocUncertaintyAngle_Object = MibTableColumn
c3gLbsLocUncertaintyAngle = _C3gLbsLocUncertaintyAngle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 7),
    _C3gLbsLocUncertaintyAngle_Type()
)
c3gLbsLocUncertaintyAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsLocUncertaintyAngle.setStatus("current")
if mibBuilder.loadTexts:
    c3gLbsLocUncertaintyAngle.setUnits("degrees")


class _C3gLbsLocUncertaintyA_Type(Unsigned32):
    """Custom type c3gLbsLocUncertaintyA based on Unsigned32"""
    defaultValue = 0


_C3gLbsLocUncertaintyA_Object = MibTableColumn
c3gLbsLocUncertaintyA = _C3gLbsLocUncertaintyA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 8),
    _C3gLbsLocUncertaintyA_Type()
)
c3gLbsLocUncertaintyA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsLocUncertaintyA.setStatus("current")
if mibBuilder.loadTexts:
    c3gLbsLocUncertaintyA.setUnits("meters")


class _C3gLbsLocUncertaintyPos_Type(Unsigned32):
    """Custom type c3gLbsLocUncertaintyPos based on Unsigned32"""
    defaultValue = 0


_C3gLbsLocUncertaintyPos_Object = MibTableColumn
c3gLbsLocUncertaintyPos = _C3gLbsLocUncertaintyPos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 9),
    _C3gLbsLocUncertaintyPos_Type()
)
c3gLbsLocUncertaintyPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsLocUncertaintyPos.setStatus("current")
if mibBuilder.loadTexts:
    c3gLbsLocUncertaintyPos.setUnits("meters")


class _C3gLbsFixtype_Type(Integer32):
    """Custom type c3gLbsFixtype based on Integer32"""
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
        *(("none", 1),
          ("threeDimension", 3),
          ("twoDimension", 2))
    )


_C3gLbsFixtype_Type.__name__ = "Integer32"
_C3gLbsFixtype_Object = MibTableColumn
c3gLbsFixtype = _C3gLbsFixtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 10),
    _C3gLbsFixtype_Type()
)
c3gLbsFixtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsFixtype.setStatus("current")


class _C3gLbsHeightValid_Type(TruthValue):
    """Custom type c3gLbsHeightValid based on TruthValue"""


_C3gLbsHeightValid_Object = MibTableColumn
c3gLbsHeightValid = _C3gLbsHeightValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 11),
    _C3gLbsHeightValid_Type()
)
c3gLbsHeightValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsHeightValid.setStatus("current")


class _C3gLbsHeight_Type(Integer32):
    """Custom type c3gLbsHeight based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_C3gLbsHeight_Type.__name__ = "Integer32"
_C3gLbsHeight_Object = MibTableColumn
c3gLbsHeight = _C3gLbsHeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 12),
    _C3gLbsHeight_Type()
)
c3gLbsHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsHeight.setStatus("current")
if mibBuilder.loadTexts:
    c3gLbsHeight.setUnits("meters")


class _C3gLbsLocUncertaintyVertical_Type(Unsigned32):
    """Custom type c3gLbsLocUncertaintyVertical based on Unsigned32"""
    defaultValue = 0


_C3gLbsLocUncertaintyVertical_Object = MibTableColumn
c3gLbsLocUncertaintyVertical = _C3gLbsLocUncertaintyVertical_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 13),
    _C3gLbsLocUncertaintyVertical_Type()
)
c3gLbsLocUncertaintyVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsLocUncertaintyVertical.setStatus("current")
if mibBuilder.loadTexts:
    c3gLbsLocUncertaintyVertical.setUnits("meters")


class _C3gLbsVelocityValid_Type(TruthValue):
    """Custom type c3gLbsVelocityValid based on TruthValue"""


_C3gLbsVelocityValid_Object = MibTableColumn
c3gLbsVelocityValid = _C3gLbsVelocityValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 14),
    _C3gLbsVelocityValid_Type()
)
c3gLbsVelocityValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsVelocityValid.setStatus("current")


class _C3gLbsHeading_Type(Unsigned32):
    """Custom type c3gLbsHeading based on Unsigned32"""
    defaultValue = 0


_C3gLbsHeading_Object = MibTableColumn
c3gLbsHeading = _C3gLbsHeading_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 15),
    _C3gLbsHeading_Type()
)
c3gLbsHeading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsHeading.setStatus("current")
if mibBuilder.loadTexts:
    c3gLbsHeading.setUnits("degrees")


class _C3gLbsVelocityHorizontal_Type(Unsigned32):
    """Custom type c3gLbsVelocityHorizontal based on Unsigned32"""
    defaultValue = 0


_C3gLbsVelocityHorizontal_Object = MibTableColumn
c3gLbsVelocityHorizontal = _C3gLbsVelocityHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 16),
    _C3gLbsVelocityHorizontal_Type()
)
c3gLbsVelocityHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsVelocityHorizontal.setStatus("current")
if mibBuilder.loadTexts:
    c3gLbsVelocityHorizontal.setUnits("meters per second")


class _C3gLbsVelocityVertical_Type(Unsigned32):
    """Custom type c3gLbsVelocityVertical based on Unsigned32"""
    defaultValue = 0


_C3gLbsVelocityVertical_Object = MibTableColumn
c3gLbsVelocityVertical = _C3gLbsVelocityVertical_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 17),
    _C3gLbsVelocityVertical_Type()
)
c3gLbsVelocityVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsVelocityVertical.setStatus("current")
if mibBuilder.loadTexts:
    c3gLbsVelocityVertical.setUnits("meters per second")


class _C3gLbsHepe_Type(Unsigned32):
    """Custom type c3gLbsHepe based on Unsigned32"""
    defaultValue = 0


_C3gLbsHepe_Object = MibTableColumn
c3gLbsHepe = _C3gLbsHepe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 18),
    _C3gLbsHepe_Type()
)
c3gLbsHepe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsHepe.setStatus("current")
if mibBuilder.loadTexts:
    c3gLbsHepe.setUnits("centimeters")


class _C3gLbsNumSatellites_Type(Gauge32):
    """Custom type c3gLbsNumSatellites based on Gauge32"""
    defaultValue = 0


_C3gLbsNumSatellites_Object = MibTableColumn
c3gLbsNumSatellites = _C3gLbsNumSatellites_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 1, 1, 1, 19),
    _C3gLbsNumSatellites_Type()
)
c3gLbsNumSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gLbsNumSatellites.setStatus("current")
_C3gWanLbsSatelliteInfo_ObjectIdentity = ObjectIdentity
c3gWanLbsSatelliteInfo = _C3gWanLbsSatelliteInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 2)
)
_C3gWanLbsSatelliteInfoTable_Object = MibTable
c3gWanLbsSatelliteInfoTable = _C3gWanLbsSatelliteInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    c3gWanLbsSatelliteInfoTable.setStatus("current")
_C3gWanLbsSatelliteInfoEntry_Object = MibTableRow
c3gWanLbsSatelliteInfoEntry = _C3gWanLbsSatelliteInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 2, 1, 1)
)
c3gWanLbsSatelliteInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-WAN-3G-MIB", "c3gWanLbsSatelliteInfoIndex"),
)
if mibBuilder.loadTexts:
    c3gWanLbsSatelliteInfoEntry.setStatus("current")


class _C3gWanLbsSatelliteInfoIndex_Type(Integer32):
    """Custom type c3gWanLbsSatelliteInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_C3gWanLbsSatelliteInfoIndex_Type.__name__ = "Integer32"
_C3gWanLbsSatelliteInfoIndex_Object = MibTableColumn
c3gWanLbsSatelliteInfoIndex = _C3gWanLbsSatelliteInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 2, 1, 1, 1),
    _C3gWanLbsSatelliteInfoIndex_Type()
)
c3gWanLbsSatelliteInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c3gWanLbsSatelliteInfoIndex.setStatus("current")
_C3gWanLbsSatelliteNumber_Type = Integer32
_C3gWanLbsSatelliteNumber_Object = MibTableColumn
c3gWanLbsSatelliteNumber = _C3gWanLbsSatelliteNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 2, 1, 1, 2),
    _C3gWanLbsSatelliteNumber_Type()
)
c3gWanLbsSatelliteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gWanLbsSatelliteNumber.setStatus("current")
_C3gWanLbsSatelliteElevation_Type = Integer32
_C3gWanLbsSatelliteElevation_Object = MibTableColumn
c3gWanLbsSatelliteElevation = _C3gWanLbsSatelliteElevation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 2, 1, 1, 3),
    _C3gWanLbsSatelliteElevation_Type()
)
c3gWanLbsSatelliteElevation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gWanLbsSatelliteElevation.setStatus("current")
if mibBuilder.loadTexts:
    c3gWanLbsSatelliteElevation.setUnits("degrees")
_C3gWanLbsSatelliteAzimuth_Type = Integer32
_C3gWanLbsSatelliteAzimuth_Object = MibTableColumn
c3gWanLbsSatelliteAzimuth = _C3gWanLbsSatelliteAzimuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 2, 1, 1, 4),
    _C3gWanLbsSatelliteAzimuth_Type()
)
c3gWanLbsSatelliteAzimuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gWanLbsSatelliteAzimuth.setStatus("current")
if mibBuilder.loadTexts:
    c3gWanLbsSatelliteAzimuth.setUnits("degrees")
_C3gWanLbsSatelliteInfoSignalNoiseRatio_Type = Integer32
_C3gWanLbsSatelliteInfoSignalNoiseRatio_Object = MibTableColumn
c3gWanLbsSatelliteInfoSignalNoiseRatio = _C3gWanLbsSatelliteInfoSignalNoiseRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 2, 1, 1, 5),
    _C3gWanLbsSatelliteInfoSignalNoiseRatio_Type()
)
c3gWanLbsSatelliteInfoSignalNoiseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gWanLbsSatelliteInfoSignalNoiseRatio.setStatus("current")
if mibBuilder.loadTexts:
    c3gWanLbsSatelliteInfoSignalNoiseRatio.setUnits("db")


class _C3gWanLbsSatelliteUsed_Type(TruthValue):
    """Custom type c3gWanLbsSatelliteUsed based on TruthValue"""


_C3gWanLbsSatelliteUsed_Object = MibTableColumn
c3gWanLbsSatelliteUsed = _C3gWanLbsSatelliteUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 2, 1, 1, 6),
    _C3gWanLbsSatelliteUsed_Type()
)
c3gWanLbsSatelliteUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gWanLbsSatelliteUsed.setStatus("current")
_C3gWanLbsSatelliteInfoRowStatus_Type = RowStatus
_C3gWanLbsSatelliteInfoRowStatus_Object = MibTableColumn
c3gWanLbsSatelliteInfoRowStatus = _C3gWanLbsSatelliteInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 4, 2, 1, 1, 7),
    _C3gWanLbsSatelliteInfoRowStatus_Type()
)
c3gWanLbsSatelliteInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c3gWanLbsSatelliteInfoRowStatus.setStatus("current")
_C3gWanSmsCommon_ObjectIdentity = ObjectIdentity
c3gWanSmsCommon = _C3gWanSmsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5)
)
_C3gWanSms_ObjectIdentity = ObjectIdentity
c3gWanSms = _C3gWanSms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1)
)
_C3gSmsCommonTable_Object = MibTable
c3gSmsCommonTable = _C3gSmsCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    c3gSmsCommonTable.setStatus("current")
_C3gSmsCommonEntry_Object = MibTableRow
c3gSmsCommonEntry = _C3gSmsCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1)
)
c3gSmsCommonEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    c3gSmsCommonEntry.setStatus("current")


class _C3gSmsServiceAvailable_Type(TruthValue):
    """Custom type c3gSmsServiceAvailable based on TruthValue"""


_C3gSmsServiceAvailable_Object = MibTableColumn
c3gSmsServiceAvailable = _C3gSmsServiceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 1),
    _C3gSmsServiceAvailable_Type()
)
c3gSmsServiceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsServiceAvailable.setStatus("current")
_C3gSmsOutSmsCount_Type = Counter32
_C3gSmsOutSmsCount_Object = MibTableColumn
c3gSmsOutSmsCount = _C3gSmsOutSmsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 2),
    _C3gSmsOutSmsCount_Type()
)
c3gSmsOutSmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsOutSmsCount.setStatus("current")
if mibBuilder.loadTexts:
    c3gSmsOutSmsCount.setUnits("msgs")
_C3gSmsOutSmsErrorCount_Type = Counter32
_C3gSmsOutSmsErrorCount_Object = MibTableColumn
c3gSmsOutSmsErrorCount = _C3gSmsOutSmsErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 3),
    _C3gSmsOutSmsErrorCount_Type()
)
c3gSmsOutSmsErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsOutSmsErrorCount.setStatus("current")
if mibBuilder.loadTexts:
    c3gSmsOutSmsErrorCount.setUnits("msgs")
_C3gSmsInSmsStorageUsed_Type = Gauge32
_C3gSmsInSmsStorageUsed_Object = MibTableColumn
c3gSmsInSmsStorageUsed = _C3gSmsInSmsStorageUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 4),
    _C3gSmsInSmsStorageUsed_Type()
)
c3gSmsInSmsStorageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsInSmsStorageUsed.setStatus("current")
if mibBuilder.loadTexts:
    c3gSmsInSmsStorageUsed.setUnits("msgs")
_C3gSmsInSmsStorageUnused_Type = Gauge32
_C3gSmsInSmsStorageUnused_Object = MibTableColumn
c3gSmsInSmsStorageUnused = _C3gSmsInSmsStorageUnused_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 5),
    _C3gSmsInSmsStorageUnused_Type()
)
c3gSmsInSmsStorageUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsInSmsStorageUnused.setStatus("current")
if mibBuilder.loadTexts:
    c3gSmsInSmsStorageUnused.setUnits("msgs")
_C3gSmsInSmsArchiveCount_Type = Gauge32
_C3gSmsInSmsArchiveCount_Object = MibTableColumn
c3gSmsInSmsArchiveCount = _C3gSmsInSmsArchiveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 6),
    _C3gSmsInSmsArchiveCount_Type()
)
c3gSmsInSmsArchiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsInSmsArchiveCount.setStatus("current")
if mibBuilder.loadTexts:
    c3gSmsInSmsArchiveCount.setUnits("msgs")
_C3gSmsInSmsArchiveErrorCount_Type = Gauge32
_C3gSmsInSmsArchiveErrorCount_Object = MibTableColumn
c3gSmsInSmsArchiveErrorCount = _C3gSmsInSmsArchiveErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 7),
    _C3gSmsInSmsArchiveErrorCount_Type()
)
c3gSmsInSmsArchiveErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsInSmsArchiveErrorCount.setStatus("current")
if mibBuilder.loadTexts:
    c3gSmsInSmsArchiveErrorCount.setUnits("msgs")
_C3gSmsArchiveUrl_Type = SnmpAdminString
_C3gSmsArchiveUrl_Object = MibTableColumn
c3gSmsArchiveUrl = _C3gSmsArchiveUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 8),
    _C3gSmsArchiveUrl_Type()
)
c3gSmsArchiveUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsArchiveUrl.setStatus("current")


class _C3gSmsOutSmsStatus_Type(Integer32):
    """Custom type c3gSmsOutSmsStatus based on Integer32"""
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
        *(("copySmsBody", 4),
          ("copySmsHeader", 3),
          ("receivedOutMsgNumber", 7),
          ("receivedOutMsgStatus", 8),
          ("receivedSentNotification", 6),
          ("sent", 5),
          ("success", 2),
          ("unknown", 1))
    )


_C3gSmsOutSmsStatus_Type.__name__ = "Integer32"
_C3gSmsOutSmsStatus_Object = MibTableColumn
c3gSmsOutSmsStatus = _C3gSmsOutSmsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 9),
    _C3gSmsOutSmsStatus_Type()
)
c3gSmsOutSmsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsOutSmsStatus.setStatus("current")
_C3gSmsInSmsCount_Type = Counter32
_C3gSmsInSmsCount_Object = MibTableColumn
c3gSmsInSmsCount = _C3gSmsInSmsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 10),
    _C3gSmsInSmsCount_Type()
)
c3gSmsInSmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsInSmsCount.setStatus("current")
_C3gSmsInSmsDeleted_Type = Counter32
_C3gSmsInSmsDeleted_Object = MibTableColumn
c3gSmsInSmsDeleted = _C3gSmsInSmsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 11),
    _C3gSmsInSmsDeleted_Type()
)
c3gSmsInSmsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsInSmsDeleted.setStatus("current")
_C3gSmsInSmsStorageMax_Type = Counter64
_C3gSmsInSmsStorageMax_Object = MibTableColumn
c3gSmsInSmsStorageMax = _C3gSmsInSmsStorageMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 12),
    _C3gSmsInSmsStorageMax_Type()
)
c3gSmsInSmsStorageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsInSmsStorageMax.setStatus("current")
if mibBuilder.loadTexts:
    c3gSmsInSmsStorageMax.setUnits("msgs")
_C3gSmsInSmsCallBack_Type = Counter32
_C3gSmsInSmsCallBack_Object = MibTableColumn
c3gSmsInSmsCallBack = _C3gSmsInSmsCallBack_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 13),
    _C3gSmsInSmsCallBack_Type()
)
c3gSmsInSmsCallBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsInSmsCallBack.setStatus("current")
if mibBuilder.loadTexts:
    c3gSmsInSmsCallBack.setUnits("msgs")
_C3gSmsOutSmsPendingCount_Type = Gauge32
_C3gSmsOutSmsPendingCount_Object = MibTableColumn
c3gSmsOutSmsPendingCount = _C3gSmsOutSmsPendingCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 14),
    _C3gSmsOutSmsPendingCount_Type()
)
c3gSmsOutSmsPendingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsOutSmsPendingCount.setStatus("current")
if mibBuilder.loadTexts:
    c3gSmsOutSmsPendingCount.setUnits("msgs")
_C3gSmsOutSmsArchiveCount_Type = Gauge32
_C3gSmsOutSmsArchiveCount_Object = MibTableColumn
c3gSmsOutSmsArchiveCount = _C3gSmsOutSmsArchiveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 15),
    _C3gSmsOutSmsArchiveCount_Type()
)
c3gSmsOutSmsArchiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsOutSmsArchiveCount.setStatus("current")
if mibBuilder.loadTexts:
    c3gSmsOutSmsArchiveCount.setUnits("msgs")
_C3gSmsOutSmsArchiveErrorCount_Type = Gauge32
_C3gSmsOutSmsArchiveErrorCount_Object = MibTableColumn
c3gSmsOutSmsArchiveErrorCount = _C3gSmsOutSmsArchiveErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 16),
    _C3gSmsOutSmsArchiveErrorCount_Type()
)
c3gSmsOutSmsArchiveErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsOutSmsArchiveErrorCount.setStatus("current")
if mibBuilder.loadTexts:
    c3gSmsOutSmsArchiveErrorCount.setUnits("msgs")
_C3gSmsInSmsArchived_Type = Gauge32
_C3gSmsInSmsArchived_Object = MibTableColumn
c3gSmsInSmsArchived = _C3gSmsInSmsArchived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 1, 5, 1, 1, 1, 17),
    _C3gSmsInSmsArchived_Type()
)
c3gSmsInSmsArchived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c3gSmsInSmsArchived.setStatus("current")
if mibBuilder.loadTexts:
    c3gSmsInSmsArchived.setUnits("msgs")
_CiscoWan3gMIBConform_ObjectIdentity = ObjectIdentity
ciscoWan3gMIBConform = _CiscoWan3gMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2)
)
_CiscoWan3gMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWan3gMIBCompliances = _CiscoWan3gMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 1)
)
_CiscoWan3gMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWan3gMIBGroups = _CiscoWan3gMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 2)
)

# Managed Objects groups

ciscoWan3gMIBCommonObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 2, 1)
)
ciscoWan3gMIBCommonObjectGroup.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gStandard"),
        ("CISCO-WAN-3G-MIB", "c3gCapability"),
        ("CISCO-WAN-3G-MIB", "c3gModemState"),
        ("CISCO-WAN-3G-MIB", "c3gPreviousServiceType"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentServiceType"),
        ("CISCO-WAN-3G-MIB", "c3gRoamingStatus"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentSystemTime"),
        ("CISCO-WAN-3G-MIB", "c3gConnectionStatus"),
        ("CISCO-WAN-3G-MIB", "c3gNotifRadioService"),
        ("CISCO-WAN-3G-MIB", "c3gNotifRssi"),
        ("CISCO-WAN-3G-MIB", "c3gNotifEcIo"),
        ("CISCO-WAN-3G-MIB", "c3gModemTemperature"),
        ("CISCO-WAN-3G-MIB", "c3gRssiOnsetNotifThreshold"),
        ("CISCO-WAN-3G-MIB", "c3gRssiAbateNotifThreshold"),
        ("CISCO-WAN-3G-MIB", "c3gEcIoOnsetNotifThreshold"),
        ("CISCO-WAN-3G-MIB", "c3gEcIoAbateNotifThreshold"),
        ("CISCO-WAN-3G-MIB", "c3gModemTemperOnsetNotifThreshold"),
        ("CISCO-WAN-3G-MIB", "c3gModemTemperAbateNotifThreshold"),
        ("CISCO-WAN-3G-MIB", "c3gModemReset"),
        ("CISCO-WAN-3G-MIB", "c3gModemUpNotifEnabled"),
        ("CISCO-WAN-3G-MIB", "c3gModemDownNotifEnabled"),
        ("CISCO-WAN-3G-MIB", "c3gServiceChangedNotifEnabled"),
        ("CISCO-WAN-3G-MIB", "c3gNetworkChangedNotifEnabled"),
        ("CISCO-WAN-3G-MIB", "c3gConnectionStatusChangedNotifFlag"),
        ("CISCO-WAN-3G-MIB", "c3gRssiOnsetNotifFlag"),
        ("CISCO-WAN-3G-MIB", "c3gRssiAbateNotifFlag"),
        ("CISCO-WAN-3G-MIB", "c3gEcIoOnsetNotifFlag"),
        ("CISCO-WAN-3G-MIB", "c3gEcIoAbateNotifFlag"),
        ("CISCO-WAN-3G-MIB", "c3gModemTemperOnsetNotifEnabled"),
        ("CISCO-WAN-3G-MIB", "c3gModemTemperAbateNotifEnabled"),
        ("CISCO-WAN-3G-MIB", "c3gGpsState"))
)
if mibBuilder.loadTexts:
    ciscoWan3gMIBCommonObjectGroup.setStatus("current")

ciscoWan3gMIBCdmaObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 2, 2)
)
ciscoWan3gMIBCdmaObjectGroup.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gCdmaTotalCallDuration"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaTotalTransmitted"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaTotalReceived"),
        ("CISCO-WAN-3G-MIB", "c3gHdrDdtmPreference"),
        ("CISCO-WAN-3G-MIB", "c3gOutgoingCallNumber"),
        ("CISCO-WAN-3G-MIB", "c3gHdrAtState"),
        ("CISCO-WAN-3G-MIB", "c3gHdrSessionState"),
        ("CISCO-WAN-3G-MIB", "c3gUati"),
        ("CISCO-WAN-3G-MIB", "c3gColorCode"),
        ("CISCO-WAN-3G-MIB", "c3gRati"),
        ("CISCO-WAN-3G-MIB", "c3gHdrSessionDuration"),
        ("CISCO-WAN-3G-MIB", "c3gHdrSessionStart"),
        ("CISCO-WAN-3G-MIB", "c3gHdrSessionEnd"),
        ("CISCO-WAN-3G-MIB", "c3gAuthStatus"),
        ("CISCO-WAN-3G-MIB", "c3gHdrDrc"),
        ("CISCO-WAN-3G-MIB", "c3gHdrDrcCover"),
        ("CISCO-WAN-3G-MIB", "c3gHdrRri"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaCurrentTransmitted"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaCurrentReceived"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaCurrentCallStatus"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaCurrentCallDuration"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaCurrentCallType"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaLastCallDisconnReason"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaLastConnError"),
        ("CISCO-WAN-3G-MIB", "c3gMobileIpErrorCode"),
        ("CISCO-WAN-3G-MIB", "c3gEsn"),
        ("CISCO-WAN-3G-MIB", "c3gModemActivationStatus"),
        ("CISCO-WAN-3G-MIB", "c3gAccountActivationDate"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaRoamingPreference"),
        ("CISCO-WAN-3G-MIB", "c3gPrlVersion"),
        ("CISCO-WAN-3G-MIB", "c3gMdn"),
        ("CISCO-WAN-3G-MIB", "c3gMsid"),
        ("CISCO-WAN-3G-MIB", "c3gMsl"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaCurrentServiceStatus"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaHybridModePreference"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaCurrentRoamingStatus"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentIdleDigitalMode"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentSid"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentNid"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentCallSetupMode"),
        ("CISCO-WAN-3G-MIB", "c3gSipUsername"),
        ("CISCO-WAN-3G-MIB", "c3gSipPassword"),
        ("CISCO-WAN-3G-MIB", "c3gServingBaseStationLongitude"),
        ("CISCO-WAN-3G-MIB", "c3gServingBaseStationLatitude"),
        ("CISCO-WAN-3G-MIB", "c3gNumberOfDataProfileConfigurable"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentActiveDataProfile"),
        ("CISCO-WAN-3G-MIB", "c3gNai"),
        ("CISCO-WAN-3G-MIB", "c3gAaaPassword"),
        ("CISCO-WAN-3G-MIB", "c3gMnHaSs"),
        ("CISCO-WAN-3G-MIB", "c3gMnHaSpi"),
        ("CISCO-WAN-3G-MIB", "c3gMnAaaSs"),
        ("CISCO-WAN-3G-MIB", "c3gMnAaaSpi"),
        ("CISCO-WAN-3G-MIB", "c3gReverseTunnelPreference"),
        ("CISCO-WAN-3G-MIB", "c3gHomeAddrType"),
        ("CISCO-WAN-3G-MIB", "c3gHomeAddr"),
        ("CISCO-WAN-3G-MIB", "c3gPriHaAddrType"),
        ("CISCO-WAN-3G-MIB", "c3gPriHaAddr"),
        ("CISCO-WAN-3G-MIB", "c3gSecHaAddrType"),
        ("CISCO-WAN-3G-MIB", "c3gSecHaAddr"),
        ("CISCO-WAN-3G-MIB", "c3gCurrent1xRttRssi"),
        ("CISCO-WAN-3G-MIB", "c3gCurrent1xRttEcIo"),
        ("CISCO-WAN-3G-MIB", "c3gCurrent1xRttChannelNumber"),
        ("CISCO-WAN-3G-MIB", "c3gCurrent1xRttChannelState"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentEvDoRssi"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentEvDoEcIo"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentEvDoChannelNumber"),
        ("CISCO-WAN-3G-MIB", "c3gSectorId"),
        ("CISCO-WAN-3G-MIB", "c3gSubnetMask"),
        ("CISCO-WAN-3G-MIB", "c3gHdrColorCode"),
        ("CISCO-WAN-3G-MIB", "c3gPnOffset"),
        ("CISCO-WAN-3G-MIB", "c3gRxMainGainControl"),
        ("CISCO-WAN-3G-MIB", "c3gRxDiversityGainControl"),
        ("CISCO-WAN-3G-MIB", "c3gTxTotalPower"),
        ("CISCO-WAN-3G-MIB", "c3gTxGainAdjust"),
        ("CISCO-WAN-3G-MIB", "c3gCarrierToInterferenceRatio"),
        ("CISCO-WAN-3G-MIB", "c3g1xRttBandClass"),
        ("CISCO-WAN-3G-MIB", "c3gEvDoBandClass"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaHistory1xRttRssiPerSecond"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaHistory1xRttRssiPerMinute"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaHistory1xRttRssiPerHour"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaHistoryEvDoRssiPerSecond"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaHistoryEvDoRssiPerMinute"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaHistoryEvDoRssiPerHour"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaPinSecurityStatus"),
        ("CISCO-WAN-3G-MIB", "c3gCdmaPowerUpLockStatus"))
)
if mibBuilder.loadTexts:
    ciscoWan3gMIBCdmaObjectGroup.setStatus("current")

ciscoWan3gMIBGsmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 2, 3)
)
ciscoWan3gMIBGsmObjectGroup.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gGsmTotalByteTransmitted"),
        ("CISCO-WAN-3G-MIB", "c3gGsmTotalByteReceived"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPacketSessionStatus"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPdpType"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPdpAddress"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosTrafficClass"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosMaxUpLinkBitRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosMaxDownLinkBitRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosGuaUpLinkBitRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosGuaDownLinkBitRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosOrder"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosErroneousSdu"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosMaxSduSize"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosSer"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosBer"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosDelay"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosPriority"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosSrcStatDescriptor"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoUmtsQosSignalIndication"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoGprsQosPrecedence"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoGprsQosDelay"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoGprsQosReliability"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoGprsQosPeakRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNegoGprsQosMeanRate"),
        ("CISCO-WAN-3G-MIB", "c3gImsi"),
        ("CISCO-WAN-3G-MIB", "c3gImei"),
        ("CISCO-WAN-3G-MIB", "c3gIccId"),
        ("CISCO-WAN-3G-MIB", "c3gMsisdn"),
        ("CISCO-WAN-3G-MIB", "c3gFsn"),
        ("CISCO-WAN-3G-MIB", "c3gModemStatus"),
        ("CISCO-WAN-3G-MIB", "c3gGsmRoamingPreference"),
        ("CISCO-WAN-3G-MIB", "c3gGsmLac"),
        ("CISCO-WAN-3G-MIB", "c3gGsmCurrentServiceStatus"),
        ("CISCO-WAN-3G-MIB", "c3gGsmCurrentServiceError"),
        ("CISCO-WAN-3G-MIB", "c3gGsmCurrentService"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPacketService"),
        ("CISCO-WAN-3G-MIB", "c3gGsmCurrentRoamingStatus"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNetworkSelectionMode"),
        ("CISCO-WAN-3G-MIB", "c3gGsmCountry"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNetwork"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMcc"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMnc"),
        ("CISCO-WAN-3G-MIB", "c3gGsmRac"),
        ("CISCO-WAN-3G-MIB", "c3gGsmCurrentCellId"),
        ("CISCO-WAN-3G-MIB", "c3gGsmCurrentPrimaryScramblingCode"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPlmnSelection"),
        ("CISCO-WAN-3G-MIB", "c3gGsmRegPlmn"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPlmnAbbr"),
        ("CISCO-WAN-3G-MIB", "c3gGsmServiceProvider"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPdpProfileType"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPdpProfileAddr"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPdpProfileApn"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPdpProfileAuthenType"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPdpProfileUsername"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPdpProfilePassword"),
        ("CISCO-WAN-3G-MIB", "c3gGsmPdpProfileRowStatus"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosTrafficClass"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosMaxUpLinkBitRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosMaxDownLinkBitRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosGuaUpLinkBitRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosGuaDownLinkBitRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosOrder"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosErroneousSdu"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosMaxSduSize"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosSer"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosBer"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosDelay"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosPriority"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosSrcStatDescriptor"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosSignalIndication"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqUmtsQosRowStatus"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosTrafficClass"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosMaxUpLinkBitRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosMaxDownLinkBitRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosGuaUpLinkBitRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosGuaDownLinkBitRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosOrder"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosErroneousSdu"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosMaxSduSize"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosSer"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosBer"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosDelay"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosPriority"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosSrcStatDescriptor"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosSignalIndication"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinUmtsQosRowStatus"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqGprsQosPrecedence"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqGprsQosDelay"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqGprsQosReliability"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqGprsQosPeakRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqGprsQosMeanRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmReqGprsQosRowStatus"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinGprsQosPrecedence"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinGprsQosDelay"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinGprsQosReliability"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinGprsQosPeakRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinGprsQosMeanRate"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMinGprsQosRowStatus"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentGsmRssi"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentGsmEcIo"),
        ("CISCO-WAN-3G-MIB", "c3gGsmCurrentBand"),
        ("CISCO-WAN-3G-MIB", "c3gGsmChannelNumber"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNumberOfNearbyCell"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNearbyCellPrimaryScramblingCode"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNearbyCellRscp"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNearbyCellEcIoMeasurement"),
        ("CISCO-WAN-3G-MIB", "c3gGsmHistoryRssiPerSecond"),
        ("CISCO-WAN-3G-MIB", "c3gGsmHistoryRssiPerMinute"),
        ("CISCO-WAN-3G-MIB", "c3gGsmHistoryRssiPerHour"),
        ("CISCO-WAN-3G-MIB", "c3gGsmChv1"),
        ("CISCO-WAN-3G-MIB", "c3gGsmSimStatus"),
        ("CISCO-WAN-3G-MIB", "c3gGsmSimUserOperationRequired"),
        ("CISCO-WAN-3G-MIB", "c3gGsmNumberOfRetriesRemaining"))
)
if mibBuilder.loadTexts:
    ciscoWan3gMIBGsmObjectGroup.setStatus("current")

ciscoWan3gMIBLbsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 2, 5)
)
ciscoWan3gMIBLbsObjectGroup.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gLbsModeSelected"),
        ("CISCO-WAN-3G-MIB", "c3gLbsState"),
        ("CISCO-WAN-3G-MIB", "c3gLbsLocFixError"),
        ("CISCO-WAN-3G-MIB", "c3gLbsLatitude"),
        ("CISCO-WAN-3G-MIB", "c3gLbsLongitude"),
        ("CISCO-WAN-3G-MIB", "c3gLbsTimeStamp"),
        ("CISCO-WAN-3G-MIB", "c3gLbsLocUncertaintyAngle"),
        ("CISCO-WAN-3G-MIB", "c3gLbsLocUncertaintyA"),
        ("CISCO-WAN-3G-MIB", "c3gLbsLocUncertaintyPos"),
        ("CISCO-WAN-3G-MIB", "c3gLbsFixtype"),
        ("CISCO-WAN-3G-MIB", "c3gLbsHeightValid"),
        ("CISCO-WAN-3G-MIB", "c3gLbsHeight"),
        ("CISCO-WAN-3G-MIB", "c3gLbsLocUncertaintyVertical"),
        ("CISCO-WAN-3G-MIB", "c3gLbsVelocityValid"),
        ("CISCO-WAN-3G-MIB", "c3gLbsHeading"),
        ("CISCO-WAN-3G-MIB", "c3gLbsVelocityHorizontal"),
        ("CISCO-WAN-3G-MIB", "c3gLbsVelocityVertical"),
        ("CISCO-WAN-3G-MIB", "c3gLbsHepe"),
        ("CISCO-WAN-3G-MIB", "c3gLbsNumSatellites"),
        ("CISCO-WAN-3G-MIB", "c3gWanLbsSatelliteNumber"),
        ("CISCO-WAN-3G-MIB", "c3gWanLbsSatelliteElevation"),
        ("CISCO-WAN-3G-MIB", "c3gWanLbsSatelliteAzimuth"),
        ("CISCO-WAN-3G-MIB", "c3gWanLbsSatelliteUsed"),
        ("CISCO-WAN-3G-MIB", "c3gWanLbsSatelliteInfoSignalNoiseRatio"),
        ("CISCO-WAN-3G-MIB", "c3gWanLbsSatelliteInfoRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoWan3gMIBLbsObjectGroup.setStatus("current")

ciscoWan3gMIBSmsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 2, 6)
)
ciscoWan3gMIBSmsObjectGroup.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gSmsServiceAvailable"),
        ("CISCO-WAN-3G-MIB", "c3gSmsOutSmsCount"),
        ("CISCO-WAN-3G-MIB", "c3gSmsOutSmsErrorCount"),
        ("CISCO-WAN-3G-MIB", "c3gSmsInSmsStorageUsed"),
        ("CISCO-WAN-3G-MIB", "c3gSmsInSmsStorageUnused"),
        ("CISCO-WAN-3G-MIB", "c3gSmsInSmsArchiveCount"),
        ("CISCO-WAN-3G-MIB", "c3gSmsInSmsArchiveErrorCount"),
        ("CISCO-WAN-3G-MIB", "c3gSmsInSmsArchived"),
        ("CISCO-WAN-3G-MIB", "c3gSmsArchiveUrl"),
        ("CISCO-WAN-3G-MIB", "c3gSmsOutSmsStatus"),
        ("CISCO-WAN-3G-MIB", "c3gSmsInSmsCount"),
        ("CISCO-WAN-3G-MIB", "c3gSmsInSmsDeleted"),
        ("CISCO-WAN-3G-MIB", "c3gSmsInSmsStorageMax"),
        ("CISCO-WAN-3G-MIB", "c3gSmsInSmsCallBack"),
        ("CISCO-WAN-3G-MIB", "c3gSmsOutSmsPendingCount"),
        ("CISCO-WAN-3G-MIB", "c3gSmsOutSmsArchiveCount"),
        ("CISCO-WAN-3G-MIB", "c3gSmsOutSmsArchiveErrorCount"))
)
if mibBuilder.loadTexts:
    ciscoWan3gMIBSmsObjectGroup.setStatus("current")


# Notification objects

c3gModemUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 1)
)
c3gModemUpNotif.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    c3gModemUpNotif.setStatus(
        "current"
    )

c3gModemDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 2)
)
c3gModemDownNotif.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    c3gModemDownNotif.setStatus(
        "current"
    )

c3gServiceChangedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 3)
)
c3gServiceChangedNotif.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gPreviousServiceType"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentServiceType"))
)
if mibBuilder.loadTexts:
    c3gServiceChangedNotif.setStatus(
        "current"
    )

c3gNetworkChangedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 4)
)
c3gNetworkChangedNotif.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gCurrentSid"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentNid"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMcc"),
        ("CISCO-WAN-3G-MIB", "c3gGsmMnc"),
        ("CISCO-WAN-3G-MIB", "c3gRoamingStatus"))
)
if mibBuilder.loadTexts:
    c3gNetworkChangedNotif.setStatus(
        "current"
    )

c3gConnectionStatusChangedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 5)
)
c3gConnectionStatusChangedNotif.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gConnectionStatus"),
        ("CISCO-WAN-3G-MIB", "c3gCurrentServiceType"))
)
if mibBuilder.loadTexts:
    c3gConnectionStatusChangedNotif.setStatus(
        "current"
    )

c3gRssiOnsetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 6)
)
c3gRssiOnsetNotif.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gNotifRadioService"),
        ("CISCO-WAN-3G-MIB", "c3gNotifRssi"))
)
if mibBuilder.loadTexts:
    c3gRssiOnsetNotif.setStatus(
        "current"
    )

c3gRssiAbateNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 7)
)
c3gRssiAbateNotif.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gNotifRadioService"),
        ("CISCO-WAN-3G-MIB", "c3gNotifRssi"))
)
if mibBuilder.loadTexts:
    c3gRssiAbateNotif.setStatus(
        "current"
    )

c3gEcIoOnsetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 8)
)
c3gEcIoOnsetNotif.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gNotifRadioService"),
        ("CISCO-WAN-3G-MIB", "c3gNotifEcIo"))
)
if mibBuilder.loadTexts:
    c3gEcIoOnsetNotif.setStatus(
        "current"
    )

c3gEcIoAbateNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 9)
)
c3gEcIoAbateNotif.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gNotifRadioService"),
        ("CISCO-WAN-3G-MIB", "c3gNotifEcIo"))
)
if mibBuilder.loadTexts:
    c3gEcIoAbateNotif.setStatus(
        "current"
    )

c3gModemTemperOnsetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 10)
)
c3gModemTemperOnsetNotif.setObjects(
    ("CISCO-WAN-3G-MIB", "c3gModemTemperature")
)
if mibBuilder.loadTexts:
    c3gModemTemperOnsetNotif.setStatus(
        "current"
    )

c3gModemTemperAbateNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 11)
)
c3gModemTemperAbateNotif.setObjects(
    ("CISCO-WAN-3G-MIB", "c3gModemTemperature")
)
if mibBuilder.loadTexts:
    c3gModemTemperAbateNotif.setStatus(
        "current"
    )

c3gModemTemperOnsetRecoveryNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 12)
)
c3gModemTemperOnsetRecoveryNotif.setObjects(
    ("CISCO-WAN-3G-MIB", "c3gModemTemperature")
)
if mibBuilder.loadTexts:
    c3gModemTemperOnsetRecoveryNotif.setStatus(
        "current"
    )

c3gModemTemperAbateRecoveryNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 0, 13)
)
c3gModemTemperAbateRecoveryNotif.setObjects(
    ("CISCO-WAN-3G-MIB", "c3gModemTemperature")
)
if mibBuilder.loadTexts:
    c3gModemTemperAbateRecoveryNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoWan3gMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 2, 4)
)
ciscoWan3gMIBNotificationGroup.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gModemUpNotif"),
        ("CISCO-WAN-3G-MIB", "c3gModemDownNotif"),
        ("CISCO-WAN-3G-MIB", "c3gServiceChangedNotif"),
        ("CISCO-WAN-3G-MIB", "c3gNetworkChangedNotif"),
        ("CISCO-WAN-3G-MIB", "c3gConnectionStatusChangedNotif"),
        ("CISCO-WAN-3G-MIB", "c3gRssiOnsetNotif"),
        ("CISCO-WAN-3G-MIB", "c3gEcIoOnsetNotif"),
        ("CISCO-WAN-3G-MIB", "c3gRssiAbateNotif"),
        ("CISCO-WAN-3G-MIB", "c3gEcIoAbateNotif"),
        ("CISCO-WAN-3G-MIB", "c3gModemTemperOnsetNotif"),
        ("CISCO-WAN-3G-MIB", "c3gModemTemperAbateNotif"))
)
if mibBuilder.loadTexts:
    ciscoWan3gMIBNotificationGroup.setStatus(
        "deprecated"
    )

ciscoWan3gMIBNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 2, 7)
)
ciscoWan3gMIBNotificationGroupRev1.setObjects(
      *(("CISCO-WAN-3G-MIB", "c3gModemUpNotif"),
        ("CISCO-WAN-3G-MIB", "c3gModemDownNotif"),
        ("CISCO-WAN-3G-MIB", "c3gServiceChangedNotif"),
        ("CISCO-WAN-3G-MIB", "c3gNetworkChangedNotif"),
        ("CISCO-WAN-3G-MIB", "c3gConnectionStatusChangedNotif"),
        ("CISCO-WAN-3G-MIB", "c3gRssiOnsetNotif"),
        ("CISCO-WAN-3G-MIB", "c3gEcIoOnsetNotif"),
        ("CISCO-WAN-3G-MIB", "c3gRssiAbateNotif"),
        ("CISCO-WAN-3G-MIB", "c3gEcIoAbateNotif"),
        ("CISCO-WAN-3G-MIB", "c3gModemTemperOnsetNotif"),
        ("CISCO-WAN-3G-MIB", "c3gModemTemperAbateNotif"),
        ("CISCO-WAN-3G-MIB", "c3gModemTemperOnsetRecoveryNotif"),
        ("CISCO-WAN-3G-MIB", "c3gModemTemperAbateRecoveryNotif"))
)
if mibBuilder.loadTexts:
    ciscoWan3gMIBNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoWan3gMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWan3gMIBCompliance.setStatus(
        "deprecated"
    )

ciscoWan3gMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoWan3gMIBCompliance1.setStatus(
        "deprecated"
    )

ciscoWan3gMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoWan3gMIBComplianceRev1.setStatus(
        "current"
    )

ciscoWan3gMIBCompliance1Rev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 661, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoWan3gMIBCompliance1Rev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-3G-MIB",
    **{"C3gServiceCapability": C3gServiceCapability,
       "C3gRssi": C3gRssi,
       "C3gEcIo": C3gEcIo,
       "C3gTemperature": C3gTemperature,
       "C3gPdpType": C3gPdpType,
       "C3gUmtsQosTrafficClass": C3gUmtsQosTrafficClass,
       "C3gUmtsQosLinkBitRate": C3gUmtsQosLinkBitRate,
       "C3gUmtsQosOrder": C3gUmtsQosOrder,
       "C3gUmtsQosErroneousSdu": C3gUmtsQosErroneousSdu,
       "C3gUmtsQosSer": C3gUmtsQosSer,
       "C3gUmtsQosBer": C3gUmtsQosBer,
       "C3gUmtsQosPriority": C3gUmtsQosPriority,
       "C3gUmtsQosSrcStatDescriptor": C3gUmtsQosSrcStatDescriptor,
       "C3gUmtsQosSignalIndication": C3gUmtsQosSignalIndication,
       "C3gGprsQosPrecedence": C3gGprsQosPrecedence,
       "C3gGprsQosDelay": C3gGprsQosDelay,
       "C3gGprsQosReliability": C3gGprsQosReliability,
       "C3gGprsQosPeakRate": C3gGprsQosPeakRate,
       "C3gGprsQosMeanRate": C3gGprsQosMeanRate,
       "ciscoWan3gMIB": ciscoWan3gMIB,
       "ciscoWan3gMIBNotifs": ciscoWan3gMIBNotifs,
       "c3gModemUpNotif": c3gModemUpNotif,
       "c3gModemDownNotif": c3gModemDownNotif,
       "c3gServiceChangedNotif": c3gServiceChangedNotif,
       "c3gNetworkChangedNotif": c3gNetworkChangedNotif,
       "c3gConnectionStatusChangedNotif": c3gConnectionStatusChangedNotif,
       "c3gRssiOnsetNotif": c3gRssiOnsetNotif,
       "c3gRssiAbateNotif": c3gRssiAbateNotif,
       "c3gEcIoOnsetNotif": c3gEcIoOnsetNotif,
       "c3gEcIoAbateNotif": c3gEcIoAbateNotif,
       "c3gModemTemperOnsetNotif": c3gModemTemperOnsetNotif,
       "c3gModemTemperAbateNotif": c3gModemTemperAbateNotif,
       "c3gModemTemperOnsetRecoveryNotif": c3gModemTemperOnsetRecoveryNotif,
       "c3gModemTemperAbateRecoveryNotif": c3gModemTemperAbateRecoveryNotif,
       "ciscoWan3gMIBObjects": ciscoWan3gMIBObjects,
       "c3gWanCommonTable": c3gWanCommonTable,
       "c3gWanCommonEntry": c3gWanCommonEntry,
       "c3gStandard": c3gStandard,
       "c3gCapability": c3gCapability,
       "c3gModemState": c3gModemState,
       "c3gPreviousServiceType": c3gPreviousServiceType,
       "c3gCurrentServiceType": c3gCurrentServiceType,
       "c3gRoamingStatus": c3gRoamingStatus,
       "c3gCurrentSystemTime": c3gCurrentSystemTime,
       "c3gConnectionStatus": c3gConnectionStatus,
       "c3gNotifRadioService": c3gNotifRadioService,
       "c3gNotifRssi": c3gNotifRssi,
       "c3gNotifEcIo": c3gNotifEcIo,
       "c3gModemTemperature": c3gModemTemperature,
       "c3gRssiOnsetNotifThreshold": c3gRssiOnsetNotifThreshold,
       "c3gRssiAbateNotifThreshold": c3gRssiAbateNotifThreshold,
       "c3gEcIoOnsetNotifThreshold": c3gEcIoOnsetNotifThreshold,
       "c3gEcIoAbateNotifThreshold": c3gEcIoAbateNotifThreshold,
       "c3gModemTemperOnsetNotifThreshold": c3gModemTemperOnsetNotifThreshold,
       "c3gModemTemperAbateNotifThreshold": c3gModemTemperAbateNotifThreshold,
       "c3gModemReset": c3gModemReset,
       "c3gModemUpNotifEnabled": c3gModemUpNotifEnabled,
       "c3gModemDownNotifEnabled": c3gModemDownNotifEnabled,
       "c3gServiceChangedNotifEnabled": c3gServiceChangedNotifEnabled,
       "c3gNetworkChangedNotifEnabled": c3gNetworkChangedNotifEnabled,
       "c3gConnectionStatusChangedNotifFlag": c3gConnectionStatusChangedNotifFlag,
       "c3gRssiOnsetNotifFlag": c3gRssiOnsetNotifFlag,
       "c3gRssiAbateNotifFlag": c3gRssiAbateNotifFlag,
       "c3gEcIoOnsetNotifFlag": c3gEcIoOnsetNotifFlag,
       "c3gEcIoAbateNotifFlag": c3gEcIoAbateNotifFlag,
       "c3gModemTemperOnsetNotifEnabled": c3gModemTemperOnsetNotifEnabled,
       "c3gModemTemperAbateNotifEnabled": c3gModemTemperAbateNotifEnabled,
       "c3gGpsState": c3gGpsState,
       "c3gWanCdma": c3gWanCdma,
       "c3gCdmaSessionTable": c3gCdmaSessionTable,
       "c3gCdmaSessionEntry": c3gCdmaSessionEntry,
       "c3gCdmaTotalCallDuration": c3gCdmaTotalCallDuration,
       "c3gCdmaTotalTransmitted": c3gCdmaTotalTransmitted,
       "c3gCdmaTotalReceived": c3gCdmaTotalReceived,
       "c3gHdrDdtmPreference": c3gHdrDdtmPreference,
       "c3gCdmaConnectionTable": c3gCdmaConnectionTable,
       "c3gCdmaConnectionEntry": c3gCdmaConnectionEntry,
       "c3gOutgoingCallNumber": c3gOutgoingCallNumber,
       "c3gHdrAtState": c3gHdrAtState,
       "c3gHdrSessionState": c3gHdrSessionState,
       "c3gUati": c3gUati,
       "c3gColorCode": c3gColorCode,
       "c3gRati": c3gRati,
       "c3gHdrSessionDuration": c3gHdrSessionDuration,
       "c3gHdrSessionStart": c3gHdrSessionStart,
       "c3gHdrSessionEnd": c3gHdrSessionEnd,
       "c3gAuthStatus": c3gAuthStatus,
       "c3gHdrDrc": c3gHdrDrc,
       "c3gHdrDrcCover": c3gHdrDrcCover,
       "c3gHdrRri": c3gHdrRri,
       "c3gMobileIpErrorCode": c3gMobileIpErrorCode,
       "c3gCdmaCurrentTransmitted": c3gCdmaCurrentTransmitted,
       "c3gCdmaCurrentReceived": c3gCdmaCurrentReceived,
       "c3gCdmaCurrentCallStatus": c3gCdmaCurrentCallStatus,
       "c3gCdmaCurrentCallDuration": c3gCdmaCurrentCallDuration,
       "c3gCdmaCurrentCallType": c3gCdmaCurrentCallType,
       "c3gCdmaLastCallDisconnReason": c3gCdmaLastCallDisconnReason,
       "c3gCdmaLastConnError": c3gCdmaLastConnError,
       "c3gCdmaIdentityTable": c3gCdmaIdentityTable,
       "c3gCdmaIdentityEntry": c3gCdmaIdentityEntry,
       "c3gEsn": c3gEsn,
       "c3gModemActivationStatus": c3gModemActivationStatus,
       "c3gAccountActivationDate": c3gAccountActivationDate,
       "c3gCdmaRoamingPreference": c3gCdmaRoamingPreference,
       "c3gPrlVersion": c3gPrlVersion,
       "c3gMdn": c3gMdn,
       "c3gMsid": c3gMsid,
       "c3gMsl": c3gMsl,
       "c3gCdmaNetworkTable": c3gCdmaNetworkTable,
       "c3gCdmaNetworkEntry": c3gCdmaNetworkEntry,
       "c3gCdmaCurrentServiceStatus": c3gCdmaCurrentServiceStatus,
       "c3gCdmaHybridModePreference": c3gCdmaHybridModePreference,
       "c3gCdmaCurrentRoamingStatus": c3gCdmaCurrentRoamingStatus,
       "c3gCurrentIdleDigitalMode": c3gCurrentIdleDigitalMode,
       "c3gCurrentSid": c3gCurrentSid,
       "c3gCurrentNid": c3gCurrentNid,
       "c3gCurrentCallSetupMode": c3gCurrentCallSetupMode,
       "c3gSipUsername": c3gSipUsername,
       "c3gSipPassword": c3gSipPassword,
       "c3gServingBaseStationLongitude": c3gServingBaseStationLongitude,
       "c3gServingBaseStationLatitude": c3gServingBaseStationLatitude,
       "c3gCdmaProfile": c3gCdmaProfile,
       "c3gCdmaProfileCommonTable": c3gCdmaProfileCommonTable,
       "c3gCdmaProfileCommonEntry": c3gCdmaProfileCommonEntry,
       "c3gNumberOfDataProfileConfigurable": c3gNumberOfDataProfileConfigurable,
       "c3gCurrentActiveDataProfile": c3gCurrentActiveDataProfile,
       "c3gCdmaProfileTable": c3gCdmaProfileTable,
       "c3gCdmaProfileEntry": c3gCdmaProfileEntry,
       "c3gCdmaProfileIndex": c3gCdmaProfileIndex,
       "c3gNai": c3gNai,
       "c3gAaaPassword": c3gAaaPassword,
       "c3gMnHaSs": c3gMnHaSs,
       "c3gMnHaSpi": c3gMnHaSpi,
       "c3gMnAaaSs": c3gMnAaaSs,
       "c3gMnAaaSpi": c3gMnAaaSpi,
       "c3gReverseTunnelPreference": c3gReverseTunnelPreference,
       "c3gHomeAddrType": c3gHomeAddrType,
       "c3gHomeAddr": c3gHomeAddr,
       "c3gPriHaAddrType": c3gPriHaAddrType,
       "c3gPriHaAddr": c3gPriHaAddr,
       "c3gSecHaAddrType": c3gSecHaAddrType,
       "c3gSecHaAddr": c3gSecHaAddr,
       "c3gCdmaRadio": c3gCdmaRadio,
       "c3gCdma1xRttRadioTable": c3gCdma1xRttRadioTable,
       "c3gCdma1xRttRadioEntry": c3gCdma1xRttRadioEntry,
       "c3gCurrent1xRttRssi": c3gCurrent1xRttRssi,
       "c3gCurrent1xRttEcIo": c3gCurrent1xRttEcIo,
       "c3gCurrent1xRttChannelNumber": c3gCurrent1xRttChannelNumber,
       "c3gCurrent1xRttChannelState": c3gCurrent1xRttChannelState,
       "c3gCdma1xRttBandClassTable": c3gCdma1xRttBandClassTable,
       "c3gCdma1xRttBandClassEntry": c3gCdma1xRttBandClassEntry,
       "c3gBandClassIndex": c3gBandClassIndex,
       "c3g1xRttBandClass": c3g1xRttBandClass,
       "c3gCdmaEvDoRadioTable": c3gCdmaEvDoRadioTable,
       "c3gCdmaEvDoRadioEntry": c3gCdmaEvDoRadioEntry,
       "c3gCurrentEvDoRssi": c3gCurrentEvDoRssi,
       "c3gCurrentEvDoEcIo": c3gCurrentEvDoEcIo,
       "c3gCurrentEvDoChannelNumber": c3gCurrentEvDoChannelNumber,
       "c3gSectorId": c3gSectorId,
       "c3gSubnetMask": c3gSubnetMask,
       "c3gHdrColorCode": c3gHdrColorCode,
       "c3gPnOffset": c3gPnOffset,
       "c3gRxMainGainControl": c3gRxMainGainControl,
       "c3gRxDiversityGainControl": c3gRxDiversityGainControl,
       "c3gTxTotalPower": c3gTxTotalPower,
       "c3gTxGainAdjust": c3gTxGainAdjust,
       "c3gCarrierToInterferenceRatio": c3gCarrierToInterferenceRatio,
       "c3gCdmaEvDoBandClassTable": c3gCdmaEvDoBandClassTable,
       "c3gCdmaEvDoBandClassEntry": c3gCdmaEvDoBandClassEntry,
       "c3gEvDoBandClass": c3gEvDoBandClass,
       "c3gCdmaHistoryTable": c3gCdmaHistoryTable,
       "c3gCdmaHistoryEntry": c3gCdmaHistoryEntry,
       "c3gCdmaHistory1xRttRssiPerSecond": c3gCdmaHistory1xRttRssiPerSecond,
       "c3gCdmaHistory1xRttRssiPerMinute": c3gCdmaHistory1xRttRssiPerMinute,
       "c3gCdmaHistory1xRttRssiPerHour": c3gCdmaHistory1xRttRssiPerHour,
       "c3gCdmaHistoryEvDoRssiPerSecond": c3gCdmaHistoryEvDoRssiPerSecond,
       "c3gCdmaHistoryEvDoRssiPerMinute": c3gCdmaHistoryEvDoRssiPerMinute,
       "c3gCdmaHistoryEvDoRssiPerHour": c3gCdmaHistoryEvDoRssiPerHour,
       "c3gCdmaSecurity": c3gCdmaSecurity,
       "c3gCdmaSecurityTable": c3gCdmaSecurityTable,
       "c3gCdmaSecurityEntry": c3gCdmaSecurityEntry,
       "c3gCdmaPinSecurityStatus": c3gCdmaPinSecurityStatus,
       "c3gCdmaPowerUpLockStatus": c3gCdmaPowerUpLockStatus,
       "c3gWanGsm": c3gWanGsm,
       "c3gGsmIdentityTable": c3gGsmIdentityTable,
       "c3gGsmIdentityEntry": c3gGsmIdentityEntry,
       "c3gImsi": c3gImsi,
       "c3gImei": c3gImei,
       "c3gIccId": c3gIccId,
       "c3gMsisdn": c3gMsisdn,
       "c3gFsn": c3gFsn,
       "c3gModemStatus": c3gModemStatus,
       "c3gGsmRoamingPreference": c3gGsmRoamingPreference,
       "c3gGsmNetworkTable": c3gGsmNetworkTable,
       "c3gGsmNetworkEntry": c3gGsmNetworkEntry,
       "c3gGsmLac": c3gGsmLac,
       "c3gGsmCurrentServiceStatus": c3gGsmCurrentServiceStatus,
       "c3gGsmCurrentServiceError": c3gGsmCurrentServiceError,
       "c3gGsmCurrentService": c3gGsmCurrentService,
       "c3gGsmPacketService": c3gGsmPacketService,
       "c3gGsmCurrentRoamingStatus": c3gGsmCurrentRoamingStatus,
       "c3gGsmNetworkSelectionMode": c3gGsmNetworkSelectionMode,
       "c3gGsmCountry": c3gGsmCountry,
       "c3gGsmNetwork": c3gGsmNetwork,
       "c3gGsmMcc": c3gGsmMcc,
       "c3gGsmMnc": c3gGsmMnc,
       "c3gGsmRac": c3gGsmRac,
       "c3gGsmCurrentCellId": c3gGsmCurrentCellId,
       "c3gGsmCurrentPrimaryScramblingCode": c3gGsmCurrentPrimaryScramblingCode,
       "c3gGsmPlmnSelection": c3gGsmPlmnSelection,
       "c3gGsmRegPlmn": c3gGsmRegPlmn,
       "c3gGsmPlmnAbbr": c3gGsmPlmnAbbr,
       "c3gGsmServiceProvider": c3gGsmServiceProvider,
       "c3gGsmTotalByteTransmitted": c3gGsmTotalByteTransmitted,
       "c3gGsmTotalByteReceived": c3gGsmTotalByteReceived,
       "c3gGsmPdpProfile": c3gGsmPdpProfile,
       "c3gGsmPdpProfileTable": c3gGsmPdpProfileTable,
       "c3gGsmPdpProfileEntry": c3gGsmPdpProfileEntry,
       "c3gGsmPdpProfileIndex": c3gGsmPdpProfileIndex,
       "c3gGsmPdpProfileType": c3gGsmPdpProfileType,
       "c3gGsmPdpProfileAddr": c3gGsmPdpProfileAddr,
       "c3gGsmPdpProfileApn": c3gGsmPdpProfileApn,
       "c3gGsmPdpProfileAuthenType": c3gGsmPdpProfileAuthenType,
       "c3gGsmPdpProfileUsername": c3gGsmPdpProfileUsername,
       "c3gGsmPdpProfilePassword": c3gGsmPdpProfilePassword,
       "c3gGsmPdpProfileRowStatus": c3gGsmPdpProfileRowStatus,
       "c3gGsmPacketSessionTable": c3gGsmPacketSessionTable,
       "c3gGsmPacketSessionEntry": c3gGsmPacketSessionEntry,
       "c3gGsmPacketSessionStatus": c3gGsmPacketSessionStatus,
       "c3gGsmPdpType": c3gGsmPdpType,
       "c3gGsmPdpAddress": c3gGsmPdpAddress,
       "c3gGsmReqUmtsQosTable": c3gGsmReqUmtsQosTable,
       "c3gGsmReqUmtsQosEntry": c3gGsmReqUmtsQosEntry,
       "c3gGsmReqUmtsQosTrafficClass": c3gGsmReqUmtsQosTrafficClass,
       "c3gGsmReqUmtsQosMaxUpLinkBitRate": c3gGsmReqUmtsQosMaxUpLinkBitRate,
       "c3gGsmReqUmtsQosMaxDownLinkBitRate": c3gGsmReqUmtsQosMaxDownLinkBitRate,
       "c3gGsmReqUmtsQosGuaUpLinkBitRate": c3gGsmReqUmtsQosGuaUpLinkBitRate,
       "c3gGsmReqUmtsQosGuaDownLinkBitRate": c3gGsmReqUmtsQosGuaDownLinkBitRate,
       "c3gGsmReqUmtsQosOrder": c3gGsmReqUmtsQosOrder,
       "c3gGsmReqUmtsQosErroneousSdu": c3gGsmReqUmtsQosErroneousSdu,
       "c3gGsmReqUmtsQosMaxSduSize": c3gGsmReqUmtsQosMaxSduSize,
       "c3gGsmReqUmtsQosSer": c3gGsmReqUmtsQosSer,
       "c3gGsmReqUmtsQosBer": c3gGsmReqUmtsQosBer,
       "c3gGsmReqUmtsQosDelay": c3gGsmReqUmtsQosDelay,
       "c3gGsmReqUmtsQosPriority": c3gGsmReqUmtsQosPriority,
       "c3gGsmReqUmtsQosSrcStatDescriptor": c3gGsmReqUmtsQosSrcStatDescriptor,
       "c3gGsmReqUmtsQosSignalIndication": c3gGsmReqUmtsQosSignalIndication,
       "c3gGsmReqUmtsQosRowStatus": c3gGsmReqUmtsQosRowStatus,
       "c3gGsmMinUmtsQosTable": c3gGsmMinUmtsQosTable,
       "c3gGsmMinUmtsQosEntry": c3gGsmMinUmtsQosEntry,
       "c3gGsmMinUmtsQosTrafficClass": c3gGsmMinUmtsQosTrafficClass,
       "c3gGsmMinUmtsQosMaxUpLinkBitRate": c3gGsmMinUmtsQosMaxUpLinkBitRate,
       "c3gGsmMinUmtsQosMaxDownLinkBitRate": c3gGsmMinUmtsQosMaxDownLinkBitRate,
       "c3gGsmMinUmtsQosGuaUpLinkBitRate": c3gGsmMinUmtsQosGuaUpLinkBitRate,
       "c3gGsmMinUmtsQosGuaDownLinkBitRate": c3gGsmMinUmtsQosGuaDownLinkBitRate,
       "c3gGsmMinUmtsQosOrder": c3gGsmMinUmtsQosOrder,
       "c3gGsmMinUmtsQosErroneousSdu": c3gGsmMinUmtsQosErroneousSdu,
       "c3gGsmMinUmtsQosMaxSduSize": c3gGsmMinUmtsQosMaxSduSize,
       "c3gGsmMinUmtsQosSer": c3gGsmMinUmtsQosSer,
       "c3gGsmMinUmtsQosBer": c3gGsmMinUmtsQosBer,
       "c3gGsmMinUmtsQosDelay": c3gGsmMinUmtsQosDelay,
       "c3gGsmMinUmtsQosPriority": c3gGsmMinUmtsQosPriority,
       "c3gGsmMinUmtsQosSrcStatDescriptor": c3gGsmMinUmtsQosSrcStatDescriptor,
       "c3gGsmMinUmtsQosSignalIndication": c3gGsmMinUmtsQosSignalIndication,
       "c3gGsmMinUmtsQosRowStatus": c3gGsmMinUmtsQosRowStatus,
       "c3gGsmNegoUmtsQosTable": c3gGsmNegoUmtsQosTable,
       "c3gGsmNegoUmtsQosEntry": c3gGsmNegoUmtsQosEntry,
       "c3gGsmNegoUmtsQosTrafficClass": c3gGsmNegoUmtsQosTrafficClass,
       "c3gGsmNegoUmtsQosMaxUpLinkBitRate": c3gGsmNegoUmtsQosMaxUpLinkBitRate,
       "c3gGsmNegoUmtsQosMaxDownLinkBitRate": c3gGsmNegoUmtsQosMaxDownLinkBitRate,
       "c3gGsmNegoUmtsQosGuaUpLinkBitRate": c3gGsmNegoUmtsQosGuaUpLinkBitRate,
       "c3gGsmNegoUmtsQosGuaDownLinkBitRate": c3gGsmNegoUmtsQosGuaDownLinkBitRate,
       "c3gGsmNegoUmtsQosOrder": c3gGsmNegoUmtsQosOrder,
       "c3gGsmNegoUmtsQosErroneousSdu": c3gGsmNegoUmtsQosErroneousSdu,
       "c3gGsmNegoUmtsQosMaxSduSize": c3gGsmNegoUmtsQosMaxSduSize,
       "c3gGsmNegoUmtsQosSer": c3gGsmNegoUmtsQosSer,
       "c3gGsmNegoUmtsQosBer": c3gGsmNegoUmtsQosBer,
       "c3gGsmNegoUmtsQosDelay": c3gGsmNegoUmtsQosDelay,
       "c3gGsmNegoUmtsQosPriority": c3gGsmNegoUmtsQosPriority,
       "c3gGsmNegoUmtsQosSrcStatDescriptor": c3gGsmNegoUmtsQosSrcStatDescriptor,
       "c3gGsmNegoUmtsQosSignalIndication": c3gGsmNegoUmtsQosSignalIndication,
       "c3gGsmReqGprsQosTable": c3gGsmReqGprsQosTable,
       "c3gGsmReqGprsQosEntry": c3gGsmReqGprsQosEntry,
       "c3gGsmReqGprsQosPrecedence": c3gGsmReqGprsQosPrecedence,
       "c3gGsmReqGprsQosDelay": c3gGsmReqGprsQosDelay,
       "c3gGsmReqGprsQosReliability": c3gGsmReqGprsQosReliability,
       "c3gGsmReqGprsQosPeakRate": c3gGsmReqGprsQosPeakRate,
       "c3gGsmReqGprsQosMeanRate": c3gGsmReqGprsQosMeanRate,
       "c3gGsmReqGprsQosRowStatus": c3gGsmReqGprsQosRowStatus,
       "c3gGsmMinGprsQosTable": c3gGsmMinGprsQosTable,
       "c3gGsmMinGprsQosEntry": c3gGsmMinGprsQosEntry,
       "c3gGsmMinGprsQosPrecedence": c3gGsmMinGprsQosPrecedence,
       "c3gGsmMinGprsQosDelay": c3gGsmMinGprsQosDelay,
       "c3gGsmMinGprsQosReliability": c3gGsmMinGprsQosReliability,
       "c3gGsmMinGprsQosPeakRate": c3gGsmMinGprsQosPeakRate,
       "c3gGsmMinGprsQosMeanRate": c3gGsmMinGprsQosMeanRate,
       "c3gGsmMinGprsQosRowStatus": c3gGsmMinGprsQosRowStatus,
       "c3gGsmNegoGprsQosTable": c3gGsmNegoGprsQosTable,
       "c3gGsmNegoGprsQosEntry": c3gGsmNegoGprsQosEntry,
       "c3gGsmNegoGprsQosPrecedence": c3gGsmNegoGprsQosPrecedence,
       "c3gGsmNegoGprsQosDelay": c3gGsmNegoGprsQosDelay,
       "c3gGsmNegoGprsQosReliability": c3gGsmNegoGprsQosReliability,
       "c3gGsmNegoGprsQosPeakRate": c3gGsmNegoGprsQosPeakRate,
       "c3gGsmNegoGprsQosMeanRate": c3gGsmNegoGprsQosMeanRate,
       "c3gGsmRadio": c3gGsmRadio,
       "c3gGsmRadioTable": c3gGsmRadioTable,
       "c3gGsmRadioEntry": c3gGsmRadioEntry,
       "c3gCurrentGsmRssi": c3gCurrentGsmRssi,
       "c3gCurrentGsmEcIo": c3gCurrentGsmEcIo,
       "c3gGsmCurrentBand": c3gGsmCurrentBand,
       "c3gGsmChannelNumber": c3gGsmChannelNumber,
       "c3gGsmNumberOfNearbyCell": c3gGsmNumberOfNearbyCell,
       "c3gGsmNearbyCellTable": c3gGsmNearbyCellTable,
       "c3gGsmNearbyCellEntry": c3gGsmNearbyCellEntry,
       "c3gGsmNearbyCellIndex": c3gGsmNearbyCellIndex,
       "c3gGsmNearbyCellPrimaryScramblingCode": c3gGsmNearbyCellPrimaryScramblingCode,
       "c3gGsmNearbyCellRscp": c3gGsmNearbyCellRscp,
       "c3gGsmNearbyCellEcIoMeasurement": c3gGsmNearbyCellEcIoMeasurement,
       "c3gGsmHistoryTable": c3gGsmHistoryTable,
       "c3gGsmHistoryEntry": c3gGsmHistoryEntry,
       "c3gGsmHistoryRssiPerSecond": c3gGsmHistoryRssiPerSecond,
       "c3gGsmHistoryRssiPerMinute": c3gGsmHistoryRssiPerMinute,
       "c3gGsmHistoryRssiPerHour": c3gGsmHistoryRssiPerHour,
       "c3gGsmSecurity": c3gGsmSecurity,
       "c3gGsmSecurityTable": c3gGsmSecurityTable,
       "c3gGsmSecurityEntry": c3gGsmSecurityEntry,
       "c3gGsmChv1": c3gGsmChv1,
       "c3gGsmSimStatus": c3gGsmSimStatus,
       "c3gGsmSimUserOperationRequired": c3gGsmSimUserOperationRequired,
       "c3gGsmNumberOfRetriesRemaining": c3gGsmNumberOfRetriesRemaining,
       "c3gWanLbs": c3gWanLbs,
       "c3gWanLbsCommon": c3gWanLbsCommon,
       "c3gWanLbsCommonTable": c3gWanLbsCommonTable,
       "c3gWanLbsCommonEntry": c3gWanLbsCommonEntry,
       "c3gLbsModeSelected": c3gLbsModeSelected,
       "c3gLbsState": c3gLbsState,
       "c3gLbsLocFixError": c3gLbsLocFixError,
       "c3gLbsLatitude": c3gLbsLatitude,
       "c3gLbsLongitude": c3gLbsLongitude,
       "c3gLbsTimeStamp": c3gLbsTimeStamp,
       "c3gLbsLocUncertaintyAngle": c3gLbsLocUncertaintyAngle,
       "c3gLbsLocUncertaintyA": c3gLbsLocUncertaintyA,
       "c3gLbsLocUncertaintyPos": c3gLbsLocUncertaintyPos,
       "c3gLbsFixtype": c3gLbsFixtype,
       "c3gLbsHeightValid": c3gLbsHeightValid,
       "c3gLbsHeight": c3gLbsHeight,
       "c3gLbsLocUncertaintyVertical": c3gLbsLocUncertaintyVertical,
       "c3gLbsVelocityValid": c3gLbsVelocityValid,
       "c3gLbsHeading": c3gLbsHeading,
       "c3gLbsVelocityHorizontal": c3gLbsVelocityHorizontal,
       "c3gLbsVelocityVertical": c3gLbsVelocityVertical,
       "c3gLbsHepe": c3gLbsHepe,
       "c3gLbsNumSatellites": c3gLbsNumSatellites,
       "c3gWanLbsSatelliteInfo": c3gWanLbsSatelliteInfo,
       "c3gWanLbsSatelliteInfoTable": c3gWanLbsSatelliteInfoTable,
       "c3gWanLbsSatelliteInfoEntry": c3gWanLbsSatelliteInfoEntry,
       "c3gWanLbsSatelliteInfoIndex": c3gWanLbsSatelliteInfoIndex,
       "c3gWanLbsSatelliteNumber": c3gWanLbsSatelliteNumber,
       "c3gWanLbsSatelliteElevation": c3gWanLbsSatelliteElevation,
       "c3gWanLbsSatelliteAzimuth": c3gWanLbsSatelliteAzimuth,
       "c3gWanLbsSatelliteInfoSignalNoiseRatio": c3gWanLbsSatelliteInfoSignalNoiseRatio,
       "c3gWanLbsSatelliteUsed": c3gWanLbsSatelliteUsed,
       "c3gWanLbsSatelliteInfoRowStatus": c3gWanLbsSatelliteInfoRowStatus,
       "c3gWanSmsCommon": c3gWanSmsCommon,
       "c3gWanSms": c3gWanSms,
       "c3gSmsCommonTable": c3gSmsCommonTable,
       "c3gSmsCommonEntry": c3gSmsCommonEntry,
       "c3gSmsServiceAvailable": c3gSmsServiceAvailable,
       "c3gSmsOutSmsCount": c3gSmsOutSmsCount,
       "c3gSmsOutSmsErrorCount": c3gSmsOutSmsErrorCount,
       "c3gSmsInSmsStorageUsed": c3gSmsInSmsStorageUsed,
       "c3gSmsInSmsStorageUnused": c3gSmsInSmsStorageUnused,
       "c3gSmsInSmsArchiveCount": c3gSmsInSmsArchiveCount,
       "c3gSmsInSmsArchiveErrorCount": c3gSmsInSmsArchiveErrorCount,
       "c3gSmsArchiveUrl": c3gSmsArchiveUrl,
       "c3gSmsOutSmsStatus": c3gSmsOutSmsStatus,
       "c3gSmsInSmsCount": c3gSmsInSmsCount,
       "c3gSmsInSmsDeleted": c3gSmsInSmsDeleted,
       "c3gSmsInSmsStorageMax": c3gSmsInSmsStorageMax,
       "c3gSmsInSmsCallBack": c3gSmsInSmsCallBack,
       "c3gSmsOutSmsPendingCount": c3gSmsOutSmsPendingCount,
       "c3gSmsOutSmsArchiveCount": c3gSmsOutSmsArchiveCount,
       "c3gSmsOutSmsArchiveErrorCount": c3gSmsOutSmsArchiveErrorCount,
       "c3gSmsInSmsArchived": c3gSmsInSmsArchived,
       "ciscoWan3gMIBConform": ciscoWan3gMIBConform,
       "ciscoWan3gMIBCompliances": ciscoWan3gMIBCompliances,
       "ciscoWan3gMIBCompliance": ciscoWan3gMIBCompliance,
       "ciscoWan3gMIBCompliance1": ciscoWan3gMIBCompliance1,
       "ciscoWan3gMIBComplianceRev1": ciscoWan3gMIBComplianceRev1,
       "ciscoWan3gMIBCompliance1Rev1": ciscoWan3gMIBCompliance1Rev1,
       "ciscoWan3gMIBGroups": ciscoWan3gMIBGroups,
       "ciscoWan3gMIBCommonObjectGroup": ciscoWan3gMIBCommonObjectGroup,
       "ciscoWan3gMIBCdmaObjectGroup": ciscoWan3gMIBCdmaObjectGroup,
       "ciscoWan3gMIBGsmObjectGroup": ciscoWan3gMIBGsmObjectGroup,
       "ciscoWan3gMIBNotificationGroup": ciscoWan3gMIBNotificationGroup,
       "ciscoWan3gMIBLbsObjectGroup": ciscoWan3gMIBLbsObjectGroup,
       "ciscoWan3gMIBSmsObjectGroup": ciscoWan3gMIBSmsObjectGroup,
       "ciscoWan3gMIBNotificationGroupRev1": ciscoWan3gMIBNotificationGroupRev1}
)
