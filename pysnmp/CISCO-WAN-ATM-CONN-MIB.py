# SNMP MIB module (CISCO-WAN-ATM-CONN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-ATM-CONN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:46 2024
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoWanAtmConnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 1)
)
ciscoWanAtmConnMIB.setRevisions(
        ("2003-03-30 00:00",
         "2002-09-18 00:00",
         "2002-03-24 00:00",
         "2001-02-09 00:00",
         "2001-01-03 00:00",
         "2000-11-15 00:00",
         "2000-07-17 00:00",
         "2000-06-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoAtmServiceCategory(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("abr", 10),
          ("cbr1", 1),
          ("cbr2", 11),
          ("cbr3", 12),
          ("ubr1", 8),
          ("ubr2", 9),
          ("vbr1RT", 2),
          ("vbr1nRT", 5),
          ("vbr2RT", 3),
          ("vbr2nRT", 6),
          ("vbr3RT", 4),
          ("vbr3nRT", 7))
    )



class CiscoWanLpbkTypes(Integer32, TextualConvention):
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
        *(("destructive", 2),
          ("noLpbk", 1),
          ("nonDestructive", 3))
    )



class CiscoWanLpbkDir(Integer32, TextualConvention):
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
        *(("external", 1),
          ("forward", 3),
          ("internal", 2),
          ("reverse", 4))
    )



class CiscoWanTestStatus(Integer32, TextualConvention):
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
        *(("lpbkAbort", 4),
          ("lpbkInEffect", 6),
          ("lpbkInProgress", 2),
          ("lpbkSuccess", 3),
          ("lpbkTimeOut", 5),
          ("noStatus", 1))
    )



class CiscoWanOperStatus(Integer32, TextualConvention):
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
        *(("adminDown", 3),
          ("operFail", 2),
          ("operOk", 1))
    )



class CiscoWanNsapAtmAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )



class CiscoWanAlarmState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("ccFail", 16),
          ("conditioned", 4),
          ("egrAisRdi", 2),
          ("ingAbitFail", 64),
          ("ingAisRdi", 1),
          ("interfaceFail", 8),
          ("mismatch", 32))
    )



class CiscoWanXmtState(Integer32, TextualConvention):
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
        *(("normal", 1),
          ("sendingAIS", 2),
          ("sendingRDI", 3))
    )



class CiscoWanRcvState(Integer32, TextualConvention):
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
        *(("ccFailure", 4),
          ("normal", 1),
          ("receivingAIS", 3),
          ("receivingRDI", 2))
    )



class CiscoWanERSConfg(Integer32, TextualConvention):
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
        *(("enableBoth", 4),
          ("enableEgress", 3),
          ("enableIngress", 2),
          ("none", 1))
    )



class CiscoWanVSVDConfg(Integer32, TextualConvention):
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
        *(("switchDefault", 3),
          ("vsvdOff", 1),
          ("vsvdOn", 2))
    )



class CiscoWanAisIW(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e2eAisCapable", 1),
          ("segAisCapable", 2))
    )



class AbrRateFactors(Integer32, TextualConvention):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("one", 16),
          ("oneOver1024", 6),
          ("oneOver128", 9),
          ("oneOver16", 12),
          ("oneOver16384", 2),
          ("oneOver2", 15),
          ("oneOver2048", 5),
          ("oneOver256", 8),
          ("oneOver32", 11),
          ("oneOver32768", 1),
          ("oneOver4", 14),
          ("oneOver4096", 4),
          ("oneOver512", 7),
          ("oneOver64", 10),
          ("oneOver8", 13),
          ("oneOver8192", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CwConnMibObjects_ObjectIdentity = ObjectIdentity
cwConnMibObjects = _CwConnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1)
)
_CwAtmChanCnfg_ObjectIdentity = ObjectIdentity
cwAtmChanCnfg = _CwAtmChanCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1)
)
_CwAtmChanCnfgTable_Object = MibTable
cwAtmChanCnfgTable = _CwAtmChanCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwAtmChanCnfgTable.setStatus("current")
_CwAtmChanCnfgEntry_Object = MibTableRow
cwAtmChanCnfgEntry = _CwAtmChanCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1)
)
cwAtmChanCnfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVpi"),
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVci"),
)
if mibBuilder.loadTexts:
    cwAtmChanCnfgEntry.setStatus("current")


class _CwaChanVpi_Type(Unsigned32):
    """Custom type cwaChanVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwaChanVpi_Type.__name__ = "Unsigned32"
_CwaChanVpi_Object = MibTableColumn
cwaChanVpi = _CwaChanVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 1),
    _CwaChanVpi_Type()
)
cwaChanVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwaChanVpi.setStatus("current")


class _CwaChanVci_Type(Unsigned32):
    """Custom type cwaChanVci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwaChanVci_Type.__name__ = "Unsigned32"
_CwaChanVci_Object = MibTableColumn
cwaChanVci = _CwaChanVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 2),
    _CwaChanVci_Type()
)
cwaChanVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwaChanVci.setStatus("current")
_CwaChanServiceCategory_Type = CiscoAtmServiceCategory
_CwaChanServiceCategory_Object = MibTableColumn
cwaChanServiceCategory = _CwaChanServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 3),
    _CwaChanServiceCategory_Type()
)
cwaChanServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanServiceCategory.setStatus("current")
_CwaChanVpcFlag_Type = TruthValue
_CwaChanVpcFlag_Object = MibTableColumn
cwaChanVpcFlag = _CwaChanVpcFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 4),
    _CwaChanVpcFlag_Type()
)
cwaChanVpcFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanVpcFlag.setStatus("current")


class _CwaChanIdentifier_Type(Unsigned32):
    """Custom type cwaChanIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwaChanIdentifier_Type.__name__ = "Unsigned32"
_CwaChanIdentifier_Object = MibTableColumn
cwaChanIdentifier = _CwaChanIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 5),
    _CwaChanIdentifier_Type()
)
cwaChanIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanIdentifier.setStatus("current")


class _CwaChanUploadCounter_Type(Unsigned32):
    """Custom type cwaChanUploadCounter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwaChanUploadCounter_Type.__name__ = "Unsigned32"
_CwaChanUploadCounter_Object = MibTableColumn
cwaChanUploadCounter = _CwaChanUploadCounter_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 6),
    _CwaChanUploadCounter_Type()
)
cwaChanUploadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanUploadCounter.setStatus("current")


class _CwaChanStatsEnable_Type(TruthValue):
    """Custom type cwaChanStatsEnable based on TruthValue"""


_CwaChanStatsEnable_Object = MibTableColumn
cwaChanStatsEnable = _CwaChanStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 7),
    _CwaChanStatsEnable_Type()
)
cwaChanStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanStatsEnable.setStatus("current")


class _CwaChanCCEnable_Type(TruthValue):
    """Custom type cwaChanCCEnable based on TruthValue"""


_CwaChanCCEnable_Object = MibTableColumn
cwaChanCCEnable = _CwaChanCCEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 8),
    _CwaChanCCEnable_Type()
)
cwaChanCCEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanCCEnable.setStatus("current")


class _CwaChanLocalVpi_Type(Unsigned32):
    """Custom type cwaChanLocalVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwaChanLocalVpi_Type.__name__ = "Unsigned32"
_CwaChanLocalVpi_Object = MibTableColumn
cwaChanLocalVpi = _CwaChanLocalVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 9),
    _CwaChanLocalVpi_Type()
)
cwaChanLocalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanLocalVpi.setStatus("current")


class _CwaChanLocalVci_Type(Unsigned32):
    """Custom type cwaChanLocalVci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwaChanLocalVci_Type.__name__ = "Unsigned32"
_CwaChanLocalVci_Object = MibTableColumn
cwaChanLocalVci = _CwaChanLocalVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 10),
    _CwaChanLocalVci_Type()
)
cwaChanLocalVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanLocalVci.setStatus("current")
_CwaChanLocalNSAPAddr_Type = CiscoWanNsapAtmAddress
_CwaChanLocalNSAPAddr_Object = MibTableColumn
cwaChanLocalNSAPAddr = _CwaChanLocalNSAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 11),
    _CwaChanLocalNSAPAddr_Type()
)
cwaChanLocalNSAPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanLocalNSAPAddr.setStatus("current")


class _CwaChanRemoteVpi_Type(Unsigned32):
    """Custom type cwaChanRemoteVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwaChanRemoteVpi_Type.__name__ = "Unsigned32"
_CwaChanRemoteVpi_Object = MibTableColumn
cwaChanRemoteVpi = _CwaChanRemoteVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 12),
    _CwaChanRemoteVpi_Type()
)
cwaChanRemoteVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRemoteVpi.setStatus("current")


class _CwaChanRemoteVci_Type(Unsigned32):
    """Custom type cwaChanRemoteVci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwaChanRemoteVci_Type.__name__ = "Unsigned32"
_CwaChanRemoteVci_Object = MibTableColumn
cwaChanRemoteVci = _CwaChanRemoteVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 13),
    _CwaChanRemoteVci_Type()
)
cwaChanRemoteVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRemoteVci.setStatus("current")
_CwaChanRemoteNSAPAddr_Type = CiscoWanNsapAtmAddress
_CwaChanRemoteNSAPAddr_Object = MibTableColumn
cwaChanRemoteNSAPAddr = _CwaChanRemoteNSAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 14),
    _CwaChanRemoteNSAPAddr_Type()
)
cwaChanRemoteNSAPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRemoteNSAPAddr.setStatus("current")


class _CwaChanControllerId_Type(Unsigned32):
    """Custom type cwaChanControllerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CwaChanControllerId_Type.__name__ = "Unsigned32"
_CwaChanControllerId_Object = MibTableColumn
cwaChanControllerId = _CwaChanControllerId_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 15),
    _CwaChanControllerId_Type()
)
cwaChanControllerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanControllerId.setStatus("current")


class _CwaChanRoutingMastership_Type(TruthValue):
    """Custom type cwaChanRoutingMastership based on TruthValue"""


_CwaChanRoutingMastership_Object = MibTableColumn
cwaChanRoutingMastership = _CwaChanRoutingMastership_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 16),
    _CwaChanRoutingMastership_Type()
)
cwaChanRoutingMastership.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRoutingMastership.setStatus("current")


class _CwaChanMaxCost_Type(Unsigned32):
    """Custom type cwaChanMaxCost based on Unsigned32"""
    defaultHexValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwaChanMaxCost_Type.__name__ = "Unsigned32"
_CwaChanMaxCost_Object = MibTableColumn
cwaChanMaxCost = _CwaChanMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 17),
    _CwaChanMaxCost_Type()
)
cwaChanMaxCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanMaxCost.setStatus("current")


class _CwaChanReroute_Type(TruthValue):
    """Custom type cwaChanReroute based on TruthValue"""


_CwaChanReroute_Object = MibTableColumn
cwaChanReroute = _CwaChanReroute_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 18),
    _CwaChanReroute_Type()
)
cwaChanReroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanReroute.setStatus("current")


class _CwaChanFrameDiscard_Type(TruthValue):
    """Custom type cwaChanFrameDiscard based on TruthValue"""


_CwaChanFrameDiscard_Object = MibTableColumn
cwaChanFrameDiscard = _CwaChanFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 19),
    _CwaChanFrameDiscard_Type()
)
cwaChanFrameDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanFrameDiscard.setStatus("current")
_CwaChanOperStatus_Type = CiscoWanOperStatus
_CwaChanOperStatus_Object = MibTableColumn
cwaChanOperStatus = _CwaChanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 20),
    _CwaChanOperStatus_Type()
)
cwaChanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanOperStatus.setStatus("current")


class _CwaChanPCR_Type(Unsigned32):
    """Custom type cwaChanPCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwaChanPCR_Type.__name__ = "Unsigned32"
_CwaChanPCR_Object = MibTableColumn
cwaChanPCR = _CwaChanPCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 21),
    _CwaChanPCR_Type()
)
cwaChanPCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanPCR.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanPCR.setUnits("cells per second")


class _CwaChanMCR_Type(Unsigned32):
    """Custom type cwaChanMCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwaChanMCR_Type.__name__ = "Unsigned32"
_CwaChanMCR_Object = MibTableColumn
cwaChanMCR = _CwaChanMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 22),
    _CwaChanMCR_Type()
)
cwaChanMCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanMCR.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanMCR.setUnits("cells per second")


class _CwaChanSCR_Type(Unsigned32):
    """Custom type cwaChanSCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwaChanSCR_Type.__name__ = "Unsigned32"
_CwaChanSCR_Object = MibTableColumn
cwaChanSCR = _CwaChanSCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 23),
    _CwaChanSCR_Type()
)
cwaChanSCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanSCR.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanSCR.setUnits("cells per second")


class _CwaChanCDV_Type(Unsigned32):
    """Custom type cwaChanCDV based on Unsigned32"""
    defaultHexValue = 16777215

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CwaChanCDV_Type.__name__ = "Unsigned32"
_CwaChanCDV_Object = MibTableColumn
cwaChanCDV = _CwaChanCDV_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 24),
    _CwaChanCDV_Type()
)
cwaChanCDV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanCDV.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanCDV.setUnits("microseconds")


class _CwaChanCTD_Type(Unsigned32):
    """Custom type cwaChanCTD based on Unsigned32"""
    defaultHexValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwaChanCTD_Type.__name__ = "Unsigned32"
_CwaChanCTD_Object = MibTableColumn
cwaChanCTD = _CwaChanCTD_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 25),
    _CwaChanCTD_Type()
)
cwaChanCTD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanCTD.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanCTD.setUnits("milliseconds")


class _CwaChanMBS_Type(Unsigned32):
    """Custom type cwaChanMBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000000),
    )


_CwaChanMBS_Type.__name__ = "Unsigned32"
_CwaChanMBS_Object = MibTableColumn
cwaChanMBS = _CwaChanMBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 26),
    _CwaChanMBS_Type()
)
cwaChanMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanMBS.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanMBS.setUnits("cells")


class _CwaChanCDVT_Type(Unsigned32):
    """Custom type cwaChanCDVT based on Unsigned32"""
    defaultHexValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwaChanCDVT_Type.__name__ = "Unsigned32"
_CwaChanCDVT_Object = MibTableColumn
cwaChanCDVT = _CwaChanCDVT_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 27),
    _CwaChanCDVT_Type()
)
cwaChanCDVT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanCDVT.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanCDVT.setUnits("microseconds")


class _CwaChanPercentUtil_Type(Unsigned32):
    """Custom type cwaChanPercentUtil based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CwaChanPercentUtil_Type.__name__ = "Unsigned32"
_CwaChanPercentUtil_Object = MibTableColumn
cwaChanPercentUtil = _CwaChanPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 28),
    _CwaChanPercentUtil_Type()
)
cwaChanPercentUtil.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanPercentUtil.setStatus("current")


class _CwaChanRemotePCR_Type(Unsigned32):
    """Custom type cwaChanRemotePCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwaChanRemotePCR_Type.__name__ = "Unsigned32"
_CwaChanRemotePCR_Object = MibTableColumn
cwaChanRemotePCR = _CwaChanRemotePCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 29),
    _CwaChanRemotePCR_Type()
)
cwaChanRemotePCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRemotePCR.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanRemotePCR.setUnits("cells per second")


class _CwaChanRemoteMCR_Type(Unsigned32):
    """Custom type cwaChanRemoteMCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwaChanRemoteMCR_Type.__name__ = "Unsigned32"
_CwaChanRemoteMCR_Object = MibTableColumn
cwaChanRemoteMCR = _CwaChanRemoteMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 30),
    _CwaChanRemoteMCR_Type()
)
cwaChanRemoteMCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRemoteMCR.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanRemoteMCR.setUnits("cells per second")


class _CwaChanRemoteSCR_Type(Unsigned32):
    """Custom type cwaChanRemoteSCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwaChanRemoteSCR_Type.__name__ = "Unsigned32"
_CwaChanRemoteSCR_Object = MibTableColumn
cwaChanRemoteSCR = _CwaChanRemoteSCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 31),
    _CwaChanRemoteSCR_Type()
)
cwaChanRemoteSCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRemoteSCR.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanRemoteSCR.setUnits("cells per second")


class _CwaChanRemoteCDV_Type(Unsigned32):
    """Custom type cwaChanRemoteCDV based on Unsigned32"""
    defaultHexValue = 16777215

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CwaChanRemoteCDV_Type.__name__ = "Unsigned32"
_CwaChanRemoteCDV_Object = MibTableColumn
cwaChanRemoteCDV = _CwaChanRemoteCDV_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 32),
    _CwaChanRemoteCDV_Type()
)
cwaChanRemoteCDV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRemoteCDV.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanRemoteCDV.setUnits("microseconds")


class _CwaChanRemoteCTD_Type(Unsigned32):
    """Custom type cwaChanRemoteCTD based on Unsigned32"""
    defaultHexValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwaChanRemoteCTD_Type.__name__ = "Unsigned32"
_CwaChanRemoteCTD_Object = MibTableColumn
cwaChanRemoteCTD = _CwaChanRemoteCTD_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 33),
    _CwaChanRemoteCTD_Type()
)
cwaChanRemoteCTD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRemoteCTD.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanRemoteCTD.setUnits("milliseconds")


class _CwaChanRemoteMBS_Type(Unsigned32):
    """Custom type cwaChanRemoteMBS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000000),
    )


_CwaChanRemoteMBS_Type.__name__ = "Unsigned32"
_CwaChanRemoteMBS_Object = MibTableColumn
cwaChanRemoteMBS = _CwaChanRemoteMBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 34),
    _CwaChanRemoteMBS_Type()
)
cwaChanRemoteMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRemoteMBS.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanRemoteMBS.setUnits("cells")


class _CwaChanRemoteCDVT_Type(Unsigned32):
    """Custom type cwaChanRemoteCDVT based on Unsigned32"""
    defaultHexValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwaChanRemoteCDVT_Type.__name__ = "Unsigned32"
_CwaChanRemoteCDVT_Object = MibTableColumn
cwaChanRemoteCDVT = _CwaChanRemoteCDVT_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 35),
    _CwaChanRemoteCDVT_Type()
)
cwaChanRemoteCDVT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRemoteCDVT.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwaChanRemoteCDVT.setUnits("cells")


class _CwaChanRemotePercentUtil_Type(Unsigned32):
    """Custom type cwaChanRemotePercentUtil based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CwaChanRemotePercentUtil_Type.__name__ = "Unsigned32"
_CwaChanRemotePercentUtil_Object = MibTableColumn
cwaChanRemotePercentUtil = _CwaChanRemotePercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 36),
    _CwaChanRemotePercentUtil_Type()
)
cwaChanRemotePercentUtil.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRemotePercentUtil.setStatus("current")


class _CwaChanAbrICR_Type(Unsigned32):
    """Custom type cwaChanAbrICR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwaChanAbrICR_Type.__name__ = "Unsigned32"
_CwaChanAbrICR_Object = MibTableColumn
cwaChanAbrICR = _CwaChanAbrICR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 37),
    _CwaChanAbrICR_Type()
)
cwaChanAbrICR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanAbrICR.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanAbrICR.setUnits("cells/sec")


class _CwaChanAbrADTF_Type(Unsigned32):
    """Custom type cwaChanAbrADTF based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_CwaChanAbrADTF_Type.__name__ = "Unsigned32"
_CwaChanAbrADTF_Object = MibTableColumn
cwaChanAbrADTF = _CwaChanAbrADTF_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 38),
    _CwaChanAbrADTF_Type()
)
cwaChanAbrADTF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanAbrADTF.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanAbrADTF.setUnits("10 milliseconds")
_CwaChanAbrRDF_Type = AbrRateFactors
_CwaChanAbrRDF_Object = MibTableColumn
cwaChanAbrRDF = _CwaChanAbrRDF_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 39),
    _CwaChanAbrRDF_Type()
)
cwaChanAbrRDF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanAbrRDF.setStatus("current")
_CwaChanAbrRIF_Type = AbrRateFactors
_CwaChanAbrRIF_Object = MibTableColumn
cwaChanAbrRIF = _CwaChanAbrRIF_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 40),
    _CwaChanAbrRIF_Type()
)
cwaChanAbrRIF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanAbrRIF.setStatus("current")


class _CwaChanAbrNRM_Type(Integer32):
    """Custom type cwaChanAbrNRM based on Integer32"""
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
        *(("nrm128", 7),
          ("nrm16", 4),
          ("nrm2", 1),
          ("nrm256", 8),
          ("nrm32", 5),
          ("nrm4", 2),
          ("nrm64", 6),
          ("nrm8", 3))
    )


_CwaChanAbrNRM_Type.__name__ = "Integer32"
_CwaChanAbrNRM_Object = MibTableColumn
cwaChanAbrNRM = _CwaChanAbrNRM_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 41),
    _CwaChanAbrNRM_Type()
)
cwaChanAbrNRM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanAbrNRM.setStatus("current")


class _CwaChanAbrTRM_Type(Integer32):
    """Custom type cwaChanAbrTRM based on Integer32"""
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
        *(("trm0point78125", 1),
          ("trm100", 8),
          ("trm12point5", 5),
          ("trm1point5625", 2),
          ("trm25", 6),
          ("trm3point125", 3),
          ("trm50", 7),
          ("trm6point25", 4))
    )


_CwaChanAbrTRM_Type.__name__ = "Integer32"
_CwaChanAbrTRM_Object = MibTableColumn
cwaChanAbrTRM = _CwaChanAbrTRM_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 42),
    _CwaChanAbrTRM_Type()
)
cwaChanAbrTRM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanAbrTRM.setStatus("current")


class _CwaChanAbrCDF_Type(Integer32):
    """Custom type cwaChanAbrCDF based on Integer32"""
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
        *(("cdf0", 1),
          ("cdfOne", 8),
          ("cdfOneOver16", 4),
          ("cdfOneOver2", 7),
          ("cdfOneOver32", 3),
          ("cdfOneOver4", 6),
          ("cdfOneOver64", 2),
          ("cdfOneOver8", 5))
    )


_CwaChanAbrCDF_Type.__name__ = "Integer32"
_CwaChanAbrCDF_Object = MibTableColumn
cwaChanAbrCDF = _CwaChanAbrCDF_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 43),
    _CwaChanAbrCDF_Type()
)
cwaChanAbrCDF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanAbrCDF.setStatus("current")


class _CwaChanAbrFRTT_Type(Unsigned32):
    """Custom type cwaChanAbrFRTT based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16700000),
    )


_CwaChanAbrFRTT_Type.__name__ = "Unsigned32"
_CwaChanAbrFRTT_Object = MibTableColumn
cwaChanAbrFRTT = _CwaChanAbrFRTT_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 44),
    _CwaChanAbrFRTT_Type()
)
cwaChanAbrFRTT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanAbrFRTT.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanAbrFRTT.setUnits("microseconds")


class _CwaChanAbrTBE_Type(Unsigned32):
    """Custom type cwaChanAbrTBE based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CwaChanAbrTBE_Type.__name__ = "Unsigned32"
_CwaChanAbrTBE_Object = MibTableColumn
cwaChanAbrTBE = _CwaChanAbrTBE_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 45),
    _CwaChanAbrTBE_Type()
)
cwaChanAbrTBE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanAbrTBE.setStatus("current")


class _CwaChanAbrERS_Type(CiscoWanERSConfg):
    """Custom type cwaChanAbrERS based on CiscoWanERSConfg"""


_CwaChanAbrERS_Object = MibTableColumn
cwaChanAbrERS = _CwaChanAbrERS_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 46),
    _CwaChanAbrERS_Type()
)
cwaChanAbrERS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanAbrERS.setStatus("deprecated")


class _CwaChanAbrVSVDEnable_Type(TruthValue):
    """Custom type cwaChanAbrVSVDEnable based on TruthValue"""


_CwaChanAbrVSVDEnable_Object = MibTableColumn
cwaChanAbrVSVDEnable = _CwaChanAbrVSVDEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 47),
    _CwaChanAbrVSVDEnable_Type()
)
cwaChanAbrVSVDEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanAbrVSVDEnable.setStatus("current")
_CwaChanRowStatus_Type = RowStatus
_CwaChanRowStatus_Object = MibTableColumn
cwaChanRowStatus = _CwaChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 48),
    _CwaChanRowStatus_Type()
)
cwaChanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRowStatus.setStatus("current")


class _CwaChanIntAbrVSVD_Type(CiscoWanVSVDConfg):
    """Custom type cwaChanIntAbrVSVD based on CiscoWanVSVDConfg"""


_CwaChanIntAbrVSVD_Object = MibTableColumn
cwaChanIntAbrVSVD = _CwaChanIntAbrVSVD_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 49),
    _CwaChanIntAbrVSVD_Type()
)
cwaChanIntAbrVSVD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanIntAbrVSVD.setStatus("current")


class _CwaChanExtAbrVSVD_Type(CiscoWanVSVDConfg):
    """Custom type cwaChanExtAbrVSVD based on CiscoWanVSVDConfg"""


_CwaChanExtAbrVSVD_Object = MibTableColumn
cwaChanExtAbrVSVD = _CwaChanExtAbrVSVD_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 50),
    _CwaChanExtAbrVSVD_Type()
)
cwaChanExtAbrVSVD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanExtAbrVSVD.setStatus("current")


class _CwaChanAisIWCapability_Type(CiscoWanAisIW):
    """Custom type cwaChanAisIWCapability based on CiscoWanAisIW"""


_CwaChanAisIWCapability_Object = MibTableColumn
cwaChanAisIWCapability = _CwaChanAisIWCapability_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 51),
    _CwaChanAisIWCapability_Type()
)
cwaChanAisIWCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanAisIWCapability.setStatus("deprecated")


class _CwaChanCLR_Type(Unsigned32):
    """Custom type cwaChanCLR based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CwaChanCLR_Type.__name__ = "Unsigned32"
_CwaChanCLR_Object = MibTableColumn
cwaChanCLR = _CwaChanCLR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 52),
    _CwaChanCLR_Type()
)
cwaChanCLR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanCLR.setStatus("current")


class _CwaChanRemoteCLR_Type(Unsigned32):
    """Custom type cwaChanRemoteCLR based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CwaChanRemoteCLR_Type.__name__ = "Unsigned32"
_CwaChanRemoteCLR_Object = MibTableColumn
cwaChanRemoteCLR = _CwaChanRemoteCLR_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 53),
    _CwaChanRemoteCLR_Type()
)
cwaChanRemoteCLR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRemoteCLR.setStatus("current")


class _CwaChanOamSegEpEnable_Type(Integer32):
    """Custom type cwaChanOamSegEpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonOamSegEp", 2),
          ("oamSegEp", 1))
    )


_CwaChanOamSegEpEnable_Type.__name__ = "Integer32"
_CwaChanOamSegEpEnable_Object = MibTableColumn
cwaChanOamSegEpEnable = _CwaChanOamSegEpEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 54),
    _CwaChanOamSegEpEnable_Type()
)
cwaChanOamSegEpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanOamSegEpEnable.setStatus("current")


class _CwaChanSlaveType_Type(Integer32):
    """Custom type cwaChanSlaveType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonPersistentSlave", 2),
          ("persistentSlave", 1))
    )


_CwaChanSlaveType_Type.__name__ = "Integer32"
_CwaChanSlaveType_Object = MibTableColumn
cwaChanSlaveType = _CwaChanSlaveType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 55),
    _CwaChanSlaveType_Type()
)
cwaChanSlaveType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanSlaveType.setStatus("current")


class _CwaChanRoutingPriority_Type(Integer32):
    """Custom type cwaChanRoutingPriority based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CwaChanRoutingPriority_Type.__name__ = "Integer32"
_CwaChanRoutingPriority_Object = MibTableColumn
cwaChanRoutingPriority = _CwaChanRoutingPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 56),
    _CwaChanRoutingPriority_Type()
)
cwaChanRoutingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanRoutingPriority.setStatus("current")


class _CwaChanP2MP_Type(TruthValue):
    """Custom type cwaChanP2MP based on TruthValue"""


_CwaChanP2MP_Object = MibTableColumn
cwaChanP2MP = _CwaChanP2MP_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 57),
    _CwaChanP2MP_Type()
)
cwaChanP2MP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanP2MP.setStatus("current")


class _CwaChanPrefRouteId_Type(Integer32):
    """Custom type cwaChanPrefRouteId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwaChanPrefRouteId_Type.__name__ = "Integer32"
_CwaChanPrefRouteId_Object = MibTableColumn
cwaChanPrefRouteId = _CwaChanPrefRouteId_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 58),
    _CwaChanPrefRouteId_Type()
)
cwaChanPrefRouteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanPrefRouteId.setStatus("current")


class _CwaChanDirectRoute_Type(TruthValue):
    """Custom type cwaChanDirectRoute based on TruthValue"""


_CwaChanDirectRoute_Object = MibTableColumn
cwaChanDirectRoute = _CwaChanDirectRoute_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 1, 1, 1, 59),
    _CwaChanDirectRoute_Type()
)
cwaChanDirectRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaChanDirectRoute.setStatus("current")
_CwAtmChanState_ObjectIdentity = ObjectIdentity
cwAtmChanState = _CwAtmChanState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2)
)
_CwAtmChanStateTable_Object = MibTable
cwAtmChanStateTable = _CwAtmChanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwAtmChanStateTable.setStatus("current")
_CwAtmChanStateEntry_Object = MibTableRow
cwAtmChanStateEntry = _CwAtmChanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1, 1)
)
cwAtmChanStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVpi"),
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVci"),
)
if mibBuilder.loadTexts:
    cwAtmChanStateEntry.setStatus("current")
_CwaChanAlarmState_Type = CiscoWanAlarmState
_CwaChanAlarmState_Object = MibTableColumn
cwaChanAlarmState = _CwaChanAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1, 1, 1),
    _CwaChanAlarmState_Type()
)
cwaChanAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanAlarmState.setStatus("current")
_CwaChanEgressXmtState_Type = CiscoWanXmtState
_CwaChanEgressXmtState_Object = MibTableColumn
cwaChanEgressXmtState = _CwaChanEgressXmtState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1, 1, 2),
    _CwaChanEgressXmtState_Type()
)
cwaChanEgressXmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanEgressXmtState.setStatus("current")
_CwaChanEgressRcvState_Type = CiscoWanRcvState
_CwaChanEgressRcvState_Object = MibTableColumn
cwaChanEgressRcvState = _CwaChanEgressRcvState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1, 1, 3),
    _CwaChanEgressRcvState_Type()
)
cwaChanEgressRcvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanEgressRcvState.setStatus("current")
_CwaChanIngressXmtState_Type = CiscoWanXmtState
_CwaChanIngressXmtState_Object = MibTableColumn
cwaChanIngressXmtState = _CwaChanIngressXmtState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1, 1, 4),
    _CwaChanIngressXmtState_Type()
)
cwaChanIngressXmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanIngressXmtState.setStatus("current")
_CwaChanIngressRcvState_Type = CiscoWanRcvState
_CwaChanIngressRcvState_Object = MibTableColumn
cwaChanIngressRcvState = _CwaChanIngressRcvState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 2, 1, 1, 5),
    _CwaChanIngressRcvState_Type()
)
cwaChanIngressRcvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanIngressRcvState.setStatus("current")
_CwAtmChanTest_ObjectIdentity = ObjectIdentity
cwAtmChanTest = _CwAtmChanTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3)
)
_CwAtmChanTestTable_Object = MibTable
cwAtmChanTestTable = _CwAtmChanTestTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwAtmChanTestTable.setStatus("current")
_CwAtmChanTestEntry_Object = MibTableRow
cwAtmChanTestEntry = _CwAtmChanTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1, 1)
)
cwAtmChanTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVpi"),
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwaChanVci"),
)
if mibBuilder.loadTexts:
    cwAtmChanTestEntry.setStatus("current")


class _CwaChanTestType_Type(CiscoWanLpbkTypes):
    """Custom type cwaChanTestType based on CiscoWanLpbkTypes"""


_CwaChanTestType_Object = MibTableColumn
cwaChanTestType = _CwaChanTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1, 1, 1),
    _CwaChanTestType_Type()
)
cwaChanTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwaChanTestType.setStatus("current")
_CwaChanTestDir_Type = CiscoWanLpbkDir
_CwaChanTestDir_Object = MibTableColumn
cwaChanTestDir = _CwaChanTestDir_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1, 1, 2),
    _CwaChanTestDir_Type()
)
cwaChanTestDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwaChanTestDir.setStatus("current")


class _CwaChanTestIterations_Type(Unsigned32):
    """Custom type cwaChanTestIterations based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CwaChanTestIterations_Type.__name__ = "Unsigned32"
_CwaChanTestIterations_Object = MibTableColumn
cwaChanTestIterations = _CwaChanTestIterations_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1, 1, 3),
    _CwaChanTestIterations_Type()
)
cwaChanTestIterations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwaChanTestIterations.setStatus("current")


class _CwaChanTestState_Type(CiscoWanTestStatus):
    """Custom type cwaChanTestState based on CiscoWanTestStatus"""


_CwaChanTestState_Object = MibTableColumn
cwaChanTestState = _CwaChanTestState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1, 1, 4),
    _CwaChanTestState_Type()
)
cwaChanTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanTestState.setStatus("current")


class _CwaChanTestRoundTripDelay_Type(Unsigned32):
    """Custom type cwaChanTestRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000000),
    )


_CwaChanTestRoundTripDelay_Type.__name__ = "Unsigned32"
_CwaChanTestRoundTripDelay_Object = MibTableColumn
cwaChanTestRoundTripDelay = _CwaChanTestRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 3, 1, 1, 5),
    _CwaChanTestRoundTripDelay_Type()
)
cwaChanTestRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanTestRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    cwaChanTestRoundTripDelay.setUnits("microseconds")
_CwAtmChanInformation_ObjectIdentity = ObjectIdentity
cwAtmChanInformation = _CwAtmChanInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 4)
)
_CwaChanNumVPCsInAlarm_Type = Unsigned32
_CwaChanNumVPCsInAlarm_Object = MibScalar
cwaChanNumVPCsInAlarm = _CwaChanNumVPCsInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 4, 1),
    _CwaChanNumVPCsInAlarm_Type()
)
cwaChanNumVPCsInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanNumVPCsInAlarm.setStatus("current")
_CwaChanNumVCCsInAlarm_Type = Unsigned32
_CwaChanNumVCCsInAlarm_Object = MibScalar
cwaChanNumVCCsInAlarm = _CwaChanNumVCCsInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 4, 2),
    _CwaChanNumVCCsInAlarm_Type()
)
cwaChanNumVCCsInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwaChanNumVCCsInAlarm.setStatus("current")
_CwGlobalChanDataGroup_ObjectIdentity = ObjectIdentity
cwGlobalChanDataGroup = _CwGlobalChanDataGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 5)
)
_CwGlobalChanDataTable_Object = MibTable
cwGlobalChanDataTable = _CwGlobalChanDataTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cwGlobalChanDataTable.setStatus("current")
_CwGlobalChanDataEntry_Object = MibTableRow
cwGlobalChanDataEntry = _CwGlobalChanDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 5, 1, 1)
)
cwGlobalChanDataEntry.setIndexNames(
    (0, "CISCO-WAN-ATM-CONN-MIB", "cwSlotIndex"),
)
if mibBuilder.loadTexts:
    cwGlobalChanDataEntry.setStatus("current")


class _CwSlotIndex_Type(Unsigned32):
    """Custom type cwSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496729),
    )


_CwSlotIndex_Type.__name__ = "Unsigned32"
_CwSlotIndex_Object = MibTableColumn
cwSlotIndex = _CwSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 5, 1, 1, 1),
    _CwSlotIndex_Type()
)
cwSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwSlotIndex.setStatus("current")


class _CwChanGlobalTransactionId_Type(Unsigned32):
    """Custom type cwChanGlobalTransactionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwChanGlobalTransactionId_Type.__name__ = "Unsigned32"
_CwChanGlobalTransactionId_Object = MibTableColumn
cwChanGlobalTransactionId = _CwChanGlobalTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 1, 5, 1, 1, 2),
    _CwChanGlobalTransactionId_Type()
)
cwChanGlobalTransactionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwChanGlobalTransactionId.setStatus("current")
_CiscoWanAtmConnMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanAtmConnMIBConformance = _CiscoWanAtmConnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2)
)
_CiscoWanAtmConnMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanAtmConnMIBCompliances = _CiscoWanAtmConnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 1)
)
_CiscoWanAtmConnMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanAtmConnMIBGroups = _CiscoWanAtmConnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2)
)

# Managed Objects groups

ciscoWanAtmConnChanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 1)
)
ciscoWanAtmConnChanMIBGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-MIB", "cwaChanServiceCategory"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanVpcFlag"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanStatsEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCCEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanUploadCounter"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIdentifier"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVpi"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVci"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalNSAPAddr"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVpi"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVci"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteNSAPAddr"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanControllerId"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRoutingMastership"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMaxCost"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanReroute"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanFrameDiscard"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOperStatus"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanSCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDV"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCTD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMBS"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDVT"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPercentUtil"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteSCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCDV"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCTD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMBS"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCDVT"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePercentUtil"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrICR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrADTF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRDF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRIF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrNRM"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTRM"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrCDF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrFRTT"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTBE"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrERS"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrVSVDEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRowStatus"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIntAbrVSVD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanExtAbrVSVD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAisIWCapability"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCLR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCLR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestType"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestDir"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestIterations"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestState"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestRoundTripDelay"))
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnChanMIBGroup.setStatus("deprecated")

ciscoWanAtmConnStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 2)
)
ciscoWanAtmConnStateGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-MIB", "cwaChanAlarmState"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanEgressXmtState"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanEgressRcvState"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIngressXmtState"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIngressRcvState"))
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnStateGroup.setStatus("current")

ciscoWanAtmConnChan2MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 3)
)
ciscoWanAtmConnChan2MIBGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-MIB", "cwaChanServiceCategory"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanVpcFlag"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanStatsEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCCEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanUploadCounter"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIdentifier"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVpi"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVci"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalNSAPAddr"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVpi"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVci"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteNSAPAddr"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanControllerId"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRoutingMastership"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMaxCost"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanReroute"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanFrameDiscard"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOperStatus"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanSCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDV"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCTD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMBS"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDVT"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPercentUtil"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteSCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCDV"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCTD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMBS"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePercentUtil"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrICR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrADTF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRDF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRIF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrNRM"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTRM"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrCDF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrFRTT"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTBE"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrERS"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrVSVDEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRowStatus"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIntAbrVSVD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanExtAbrVSVD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAisIWCapability"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCLR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCLR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOamSegEpEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestType"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestDir"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestIterations"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestState"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestRoundTripDelay"))
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnChan2MIBGroup.setStatus("deprecated")

ciscoWanAtmConnChan3MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 4)
)
ciscoWanAtmConnChan3MIBGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-MIB", "cwaChanServiceCategory"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanVpcFlag"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanStatsEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCCEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanUploadCounter"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIdentifier"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVpi"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVci"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalNSAPAddr"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVpi"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVci"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteNSAPAddr"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanControllerId"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRoutingMastership"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMaxCost"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanReroute"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanFrameDiscard"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOperStatus"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanSCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDV"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCTD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMBS"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDVT"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPercentUtil"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteSCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCDV"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCTD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMBS"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePercentUtil"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrICR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrADTF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRDF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRIF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrNRM"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTRM"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrCDF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrFRTT"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTBE"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrVSVDEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRowStatus"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIntAbrVSVD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanExtAbrVSVD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCLR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCLR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOamSegEpEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanSlaveType"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRoutingPriority"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestType"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestDir"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestIterations"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestState"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestRoundTripDelay"))
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnChan3MIBGroup.setStatus("deprecated")

ciscoWanAtmInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 5)
)
ciscoWanAtmInformationGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-MIB", "cwaChanNumVPCsInAlarm"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanNumVCCsInAlarm"))
)
if mibBuilder.loadTexts:
    ciscoWanAtmInformationGroup.setStatus("current")

ciscoWanAtmConnChan4MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 6)
)
ciscoWanAtmConnChan4MIBGroup.setObjects(
      *(("CISCO-WAN-ATM-CONN-MIB", "cwaChanServiceCategory"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanVpcFlag"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanStatsEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCCEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanUploadCounter"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIdentifier"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVpi"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalVci"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanLocalNSAPAddr"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVpi"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteVci"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteNSAPAddr"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanControllerId"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRoutingMastership"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMaxCost"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanReroute"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanFrameDiscard"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOperStatus"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanSCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDV"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCTD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanMBS"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCDVT"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPercentUtil"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteSCR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCDV"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCTD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteMBS"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemotePercentUtil"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrICR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrADTF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRDF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrRIF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrNRM"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTRM"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrCDF"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrFRTT"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrTBE"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanAbrVSVDEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRowStatus"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanIntAbrVSVD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanExtAbrVSVD"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanCLR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRemoteCLR"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanOamSegEpEnable"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanSlaveType"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanRoutingPriority"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanP2MP"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanPrefRouteId"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanDirectRoute"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestType"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestDir"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestIterations"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestState"),
        ("CISCO-WAN-ATM-CONN-MIB", "cwaChanTestRoundTripDelay"))
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnChan4MIBGroup.setStatus("current")

ciscoWanConMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 2, 7)
)
ciscoWanConMIBGroup.setObjects(
    ("CISCO-WAN-ATM-CONN-MIB", "cwChanGlobalTransactionId")
)
if mibBuilder.loadTexts:
    ciscoWanConMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanAtmConnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnMIBCompliance.setStatus(
        "deprecated"
    )

ciscoWanAtmConnMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoWanAtmConnMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnMIBCompliance3.setStatus(
        "deprecated"
    )

ciscoWanAtmConnMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoWanAtmConnMIBCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-ATM-CONN-MIB",
    **{"CiscoAtmServiceCategory": CiscoAtmServiceCategory,
       "CiscoWanLpbkTypes": CiscoWanLpbkTypes,
       "CiscoWanLpbkDir": CiscoWanLpbkDir,
       "CiscoWanTestStatus": CiscoWanTestStatus,
       "CiscoWanOperStatus": CiscoWanOperStatus,
       "CiscoWanNsapAtmAddress": CiscoWanNsapAtmAddress,
       "CiscoWanAlarmState": CiscoWanAlarmState,
       "CiscoWanXmtState": CiscoWanXmtState,
       "CiscoWanRcvState": CiscoWanRcvState,
       "CiscoWanERSConfg": CiscoWanERSConfg,
       "CiscoWanVSVDConfg": CiscoWanVSVDConfg,
       "CiscoWanAisIW": CiscoWanAisIW,
       "AbrRateFactors": AbrRateFactors,
       "ciscoWanAtmConnMIB": ciscoWanAtmConnMIB,
       "cwConnMibObjects": cwConnMibObjects,
       "cwAtmChanCnfg": cwAtmChanCnfg,
       "cwAtmChanCnfgTable": cwAtmChanCnfgTable,
       "cwAtmChanCnfgEntry": cwAtmChanCnfgEntry,
       "cwaChanVpi": cwaChanVpi,
       "cwaChanVci": cwaChanVci,
       "cwaChanServiceCategory": cwaChanServiceCategory,
       "cwaChanVpcFlag": cwaChanVpcFlag,
       "cwaChanIdentifier": cwaChanIdentifier,
       "cwaChanUploadCounter": cwaChanUploadCounter,
       "cwaChanStatsEnable": cwaChanStatsEnable,
       "cwaChanCCEnable": cwaChanCCEnable,
       "cwaChanLocalVpi": cwaChanLocalVpi,
       "cwaChanLocalVci": cwaChanLocalVci,
       "cwaChanLocalNSAPAddr": cwaChanLocalNSAPAddr,
       "cwaChanRemoteVpi": cwaChanRemoteVpi,
       "cwaChanRemoteVci": cwaChanRemoteVci,
       "cwaChanRemoteNSAPAddr": cwaChanRemoteNSAPAddr,
       "cwaChanControllerId": cwaChanControllerId,
       "cwaChanRoutingMastership": cwaChanRoutingMastership,
       "cwaChanMaxCost": cwaChanMaxCost,
       "cwaChanReroute": cwaChanReroute,
       "cwaChanFrameDiscard": cwaChanFrameDiscard,
       "cwaChanOperStatus": cwaChanOperStatus,
       "cwaChanPCR": cwaChanPCR,
       "cwaChanMCR": cwaChanMCR,
       "cwaChanSCR": cwaChanSCR,
       "cwaChanCDV": cwaChanCDV,
       "cwaChanCTD": cwaChanCTD,
       "cwaChanMBS": cwaChanMBS,
       "cwaChanCDVT": cwaChanCDVT,
       "cwaChanPercentUtil": cwaChanPercentUtil,
       "cwaChanRemotePCR": cwaChanRemotePCR,
       "cwaChanRemoteMCR": cwaChanRemoteMCR,
       "cwaChanRemoteSCR": cwaChanRemoteSCR,
       "cwaChanRemoteCDV": cwaChanRemoteCDV,
       "cwaChanRemoteCTD": cwaChanRemoteCTD,
       "cwaChanRemoteMBS": cwaChanRemoteMBS,
       "cwaChanRemoteCDVT": cwaChanRemoteCDVT,
       "cwaChanRemotePercentUtil": cwaChanRemotePercentUtil,
       "cwaChanAbrICR": cwaChanAbrICR,
       "cwaChanAbrADTF": cwaChanAbrADTF,
       "cwaChanAbrRDF": cwaChanAbrRDF,
       "cwaChanAbrRIF": cwaChanAbrRIF,
       "cwaChanAbrNRM": cwaChanAbrNRM,
       "cwaChanAbrTRM": cwaChanAbrTRM,
       "cwaChanAbrCDF": cwaChanAbrCDF,
       "cwaChanAbrFRTT": cwaChanAbrFRTT,
       "cwaChanAbrTBE": cwaChanAbrTBE,
       "cwaChanAbrERS": cwaChanAbrERS,
       "cwaChanAbrVSVDEnable": cwaChanAbrVSVDEnable,
       "cwaChanRowStatus": cwaChanRowStatus,
       "cwaChanIntAbrVSVD": cwaChanIntAbrVSVD,
       "cwaChanExtAbrVSVD": cwaChanExtAbrVSVD,
       "cwaChanAisIWCapability": cwaChanAisIWCapability,
       "cwaChanCLR": cwaChanCLR,
       "cwaChanRemoteCLR": cwaChanRemoteCLR,
       "cwaChanOamSegEpEnable": cwaChanOamSegEpEnable,
       "cwaChanSlaveType": cwaChanSlaveType,
       "cwaChanRoutingPriority": cwaChanRoutingPriority,
       "cwaChanP2MP": cwaChanP2MP,
       "cwaChanPrefRouteId": cwaChanPrefRouteId,
       "cwaChanDirectRoute": cwaChanDirectRoute,
       "cwAtmChanState": cwAtmChanState,
       "cwAtmChanStateTable": cwAtmChanStateTable,
       "cwAtmChanStateEntry": cwAtmChanStateEntry,
       "cwaChanAlarmState": cwaChanAlarmState,
       "cwaChanEgressXmtState": cwaChanEgressXmtState,
       "cwaChanEgressRcvState": cwaChanEgressRcvState,
       "cwaChanIngressXmtState": cwaChanIngressXmtState,
       "cwaChanIngressRcvState": cwaChanIngressRcvState,
       "cwAtmChanTest": cwAtmChanTest,
       "cwAtmChanTestTable": cwAtmChanTestTable,
       "cwAtmChanTestEntry": cwAtmChanTestEntry,
       "cwaChanTestType": cwaChanTestType,
       "cwaChanTestDir": cwaChanTestDir,
       "cwaChanTestIterations": cwaChanTestIterations,
       "cwaChanTestState": cwaChanTestState,
       "cwaChanTestRoundTripDelay": cwaChanTestRoundTripDelay,
       "cwAtmChanInformation": cwAtmChanInformation,
       "cwaChanNumVPCsInAlarm": cwaChanNumVPCsInAlarm,
       "cwaChanNumVCCsInAlarm": cwaChanNumVCCsInAlarm,
       "cwGlobalChanDataGroup": cwGlobalChanDataGroup,
       "cwGlobalChanDataTable": cwGlobalChanDataTable,
       "cwGlobalChanDataEntry": cwGlobalChanDataEntry,
       "cwSlotIndex": cwSlotIndex,
       "cwChanGlobalTransactionId": cwChanGlobalTransactionId,
       "ciscoWanAtmConnMIBConformance": ciscoWanAtmConnMIBConformance,
       "ciscoWanAtmConnMIBCompliances": ciscoWanAtmConnMIBCompliances,
       "ciscoWanAtmConnMIBCompliance": ciscoWanAtmConnMIBCompliance,
       "ciscoWanAtmConnMIBCompliance2": ciscoWanAtmConnMIBCompliance2,
       "ciscoWanAtmConnMIBCompliance3": ciscoWanAtmConnMIBCompliance3,
       "ciscoWanAtmConnMIBCompliance4": ciscoWanAtmConnMIBCompliance4,
       "ciscoWanAtmConnMIBGroups": ciscoWanAtmConnMIBGroups,
       "ciscoWanAtmConnChanMIBGroup": ciscoWanAtmConnChanMIBGroup,
       "ciscoWanAtmConnStateGroup": ciscoWanAtmConnStateGroup,
       "ciscoWanAtmConnChan2MIBGroup": ciscoWanAtmConnChan2MIBGroup,
       "ciscoWanAtmConnChan3MIBGroup": ciscoWanAtmConnChan3MIBGroup,
       "ciscoWanAtmInformationGroup": ciscoWanAtmInformationGroup,
       "ciscoWanAtmConnChan4MIBGroup": ciscoWanAtmConnChan4MIBGroup,
       "ciscoWanConMIBGroup": ciscoWanConMIBGroup}
)
